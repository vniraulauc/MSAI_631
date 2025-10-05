# src/recommend.py
import os
import pandas as pd
import joblib
from surprise import Dataset, Reader

BASE = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(BASE, "data", "ml-100k")
MOVIES_FILE = os.path.join(DATA_DIR, "u.item")  # movie metadata
MODEL_FILE = os.path.join(BASE, "model_joblib.pkl")

# load model
algo = joblib.load(MODEL_FILE)

# load movies metadata (MovieLens u.item with '|' separator)
cols = ["movie_id", "title"] + [f"col{i}" for i in range(22)]
movies = pd.read_csv(MOVIES_FILE, sep='|', encoding='latin-1', header=None, names=cols, usecols=[0,1])
movies.movie_id = movies.movie_id.astype(int)

# helper: top N predictions for given user (user id is MovieLens user id)
def top_n_for_user(user_id, n=10):
    # build list of all movie ids
    all_ids = movies.movie_id.tolist()

    # load ratings to find which movies user has already rated
    ratings_file = os.path.join(DATA_DIR, "u.data")
    df_r = pd.read_csv(ratings_file, sep='\t', header=None, names=["user","item","rating","ts"])
    seen = set(df_r[df_r.user == int(user_id)].item.tolist())

    candidates = [i for i in all_ids if i not in seen]
    preds = []
    for item in candidates:
        pred = algo.predict(str(user_id), str(item))
        preds.append((item, pred.est))
    preds.sort(key=lambda x: x[1], reverse=True)
    top = preds[:n]
    return [(movies[movies.movie_id==int(i)].title.values[0], score) for i,score in top]

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python recommend.py <user_id> [N]")
        sys.exit(1)
    uid = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
    for title,score in top_n_for_user(uid,n):
        print(f"{title}  — predicted rating: {score:.2f}")
