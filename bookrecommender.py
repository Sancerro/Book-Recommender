
import pandas as pd

def load_data():
    books_df = pd.read_csv('Books.csv')
    ratings_df = pd.read_csv('Ratings.csv')
    books_df = pd.merge(books_df, ratings_df, on="ISBN")
    return books_df

def get_book_suggestions(books_df, prefix, type):
    suggestions = []
    if type == "author":
        for author in books_df['Book-Author'].unique():
         if author.startswith(prefix):
            suggestions.append(author)
    else:
        for title in books_df['Book-Title'].unique():
         if title.startswith(prefix):
            suggestions.append(title)
    
    return suggestions


