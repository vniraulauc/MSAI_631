import os
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import joblib

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "ml-100k")
ratings_file = os.path.join(DATA_DIR, "u.data")  # MovieLens 100k ratings

# MovieLens u.data: user id | item id | rating | timestamp (tab separated)
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file(ratings_file, reader=reader)

trainset, testset = train_test_split(data, test_size=0.2, random_state=42)
algo = SVD(n_factors=50, biased=True, verbose=True)
print("Training SVD...")
algo.fit(trainset)
print("Evaluating on test set (RMSE)...")
preds = algo.test(testset)
# compute RMSE
from surprise import accuracy
rmse = accuracy.rmse(preds, verbose=True)

# Save model
model_path = os.path.join(os.path.dirname(__file__), "..", "model_joblib.pkl")
joblib.dump(algo, model_path)
print("Saved model to", model_path)
