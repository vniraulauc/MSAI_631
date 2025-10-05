from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "ml-100k")
ratings_file = os.path.join(DATA_DIR, "u.data")
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file(ratings_file, reader=reader)

algo = SVD(n_factors=50, biased=True)
print("Cross-validating (5 folds)...")
cv = cross_validate(algo, data, measures=['RMSE','MAE'], cv=5, verbose=True)
print("Done.")
