from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load built-in MovieLens 100k dataset
data = Dataset.load_builtin('ml-100k')
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Train model using SVD
algo = SVD()
algo.fit(trainset)

# Evaluate
predictions = algo.test(testset)
rmse = accuracy.rmse(predictions)
print("RMSE:", rmse)

# Recommend for user
def recommend_for_user(user_id, n=5):
    trainset_full = data.build_full_trainset()
    algo.fit(trainset_full)

    # Get all item ids
    all_items = trainset_full._raw2inner_id_items.keys()
    rated_items = set([j for (j, _) in trainset_full.ur[trainset_full.to_inner_uid(user_id)]])
    unseen_items = [iid for iid in all_items if iid not in rated_items]

    predictions = [algo.predict(user_id, iid) for iid in unseen_items]
    predictions.sort(key=lambda x: x.est, reverse=True)

    top_n = predictions[:n]
    for pred in top_n:
        print(f"Movie ID: {pred.iid}, Predicted Rating: {pred.est:.2f}")

# Test
if __name__ == "__main__":
    print("\nTop recommendations for user 196:")
    recommend_for_user('196')
