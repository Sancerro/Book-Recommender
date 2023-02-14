
import pandas as pd

def load_data():
    books_df = pd.read_csv('Books.csv')
    ratings_df = pd.read_csv('Ratings.csv')
    books_df = pd.merge(books_df, ratings_df, on="ISBN")
    return books_df

def get_book_suggestions(books_df, prefix, type):
    suggestions = []
    if type == "author":
        for author in books_df['Book-Author'].dropna().unique():
         if author.startswith(prefix.title()):
            suggestions.append(author)
    else:
        for title in books_df['Book-Title'].dropna().unique():
         if title.startswith(prefix.title()):
            suggestions.append(title)
    
    return suggestions

def display_suggestions(suggestions):
    if suggestions == []:
        print("No books found")
    else:
        print("Suggestions:")        
        for i, suggestion in enumerate(suggestions):
            print(f"{i+1}. {suggestion}")
        return input("Choose a suggestion by typing its number or type 'back' to search again: ")

def display_books_by_author(selected_suggestion, books_df):
    books = books_df[books_df['Book-Author'] == selected_suggestion]
    books = books.sort_values("Book-Rating", ascending=False)
    print(f"Books by {selected_suggestion}:")
    for i, book in enumerate(books['Book-Title']):
        print(f"{i+1}. {book} ({books.iloc[i]['Book-Rating']})")
    return input("Choose a book by typing its number or type 'back' to search again: ")

def display_book_details(selected_book, books_df):
    book = books_df[books_df['Book-Title'] == selected_book].iloc[0]
    print(f"Title: {book['Book-Title']}")
    print(f"Author: {book['Book-Author']}")
    print(f"Year of Publication: {book['Year-Of-Publication']}")
    print(f"Publisher: {book['Publisher']}")
    print(f"Rating: {book['Book-Rating']}")

def greeting():
    print("Welcome to the book recommendation system!")
    print("You can search for books based on either the author's name or the book title.")
    print("Type 'quit' at any time to exit the program.")
    print("")

def main():
    books_df = load_data()
    greeting()
    
    while True:
        
        choice = ""
        while choice not in ["author","title","quit"]:
            choice = input("Choose whether you want to search by author or title by typing either\n")
        
        if choice == "quit":
            break
        
        prefix = ""
        while not prefix:
            prefix = input("Type the prefix you want to search\n")
        
        if prefix == "quit":
            break
        suggestions = []
        
        if choice == "author":
            suggestions = get_book_suggestions(books_df, prefix, "author")
        
        else:
            suggestions = get_book_suggestions(books_df, prefix, "title")
        
        if suggestions == []:
            print("No books found")
        else:
            print("Suggestions:")        
            for i, suggestion in enumerate(suggestions):
                print(f"{i+1}. {suggestion}")
            selected_suggestion = display_suggestions(suggestions)
            if selected_suggestion.isdigit() and int(selected_suggestion) > 0 and int(selected_suggestion) <= len(suggestions):
                selected_suggestion = suggestions[int(selected_suggestion) - 1]
            
                if choice == "author":
                    selected_book = display_books_by_author(selected_suggestion, books_df)
                    if books_df[books_df['Book-Title'] == selected_book].empty:
                        print("Sorry, the book you selected is not present in our database.")
                    else:
                        book = books_df[books_df['Book-Title'] == selected_book].iloc[0]

                else:
                    selected_book = selected_suggestion
                    display_book_details(selected_book, books_df)
            
            elif selected_suggestion == "back":
                continue
            
            else:
                print("Invalid input.")
                

if __name__ == "__main__":
    main()