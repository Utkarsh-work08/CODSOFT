# 🎬 Movie Recommendation System

This is a simple movie recommendation system using:
- ✅ Content-Based Filtering (TF-IDF + Cosine Similarity)
- ✅ Collaborative Filtering (Matrix Factorization using SVD)

## 📁 Dataset
- [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/100k/)
- Includes user ratings and movie genres

## 🔧 Technologies Used
- Python
- Pandas
- Scikit-learn
- Surprise (for collaborative filtering)
- Jupyter Notebook / VS Code

## 📂 Project Structure

```
recommendation-system/
│
├── data/                        # Dataset files
│   └── movies.csv
│   └── ratings.csv
│
├── src/                         # Python source code
│   └── content_based.py
│   └── collaborative.py
│
├── notebook/                    # Jupyter Notebooks
│   └── Movie_Recommendation_System.ipynb
│
├── README.md                    # Project documentation
├── requirements.txt             # Python packages
└── .gitignore                   # Optional
```

## 🚀 How to Run

1. Clone the repository
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the notebook:

```bash
jupyter notebook notebook/Movie_Recommendation_System.ipynb
```

## 📌 Features

- Recommend similar movies based on genres using content-based filtering
- Suggest top movies to users using collaborative filtering with SVD
- Uses MovieLens 100k dataset

## 📷 Sample Output

```
Recommended movies for 'Toy Story':
- Jumanji
- Shrek
- Monsters, Inc.
- Ice Age
```

## 🤝 Contributing
Feel free to fork and enhance!

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
