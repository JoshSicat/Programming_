import tkinter as tk
from tkinter import ttk
import requests

class MovieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie App")

        #Creating the widgets
        self.label = ttk.Label(root, text="Enter movie title:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(root, width=30)
        self.entry.pack(pady=10)

        self.get_movie_button = ttk.Button(root, text="Get Movie Info", command=self.get_movie_info)
        self.get_movie_button.pack(pady=10)

        self.result_text = tk.Text(root, height=15, width=50)
        self.result_text.pack(pady=10)

        self.label = ttk.Label(root, text="lift")
        self.label.pack

    def fetch_movie_details(self, movie_title):
        #Replace 'YOUR_OMDB_API_KEY' with your actual OMDB API key
        api_key = "http://www.omdbapi.com/"
        base_url = "https://ww2.123moviesfree.net/"
        params = {"t": movie_title}
        if api_key:
            params["apikey"] = api_key
        response = requests.get(base_url, params=params)
        data = response.json()
        return data

    def display_movie_details(self, movie_details):
        if movie_details.get("Response") == "True":
            self.result_text.insert(tk.END, f"Title: {movie_details['Title']}\n")
            self.result_text.insert(tk.END, f"Year: {movie_details['Year']}\n")
            self.result_text.insert(tk.END, f"Genre: {movie_details['Genre']}\n")
            self.result_text.insert(tk.END, f"Director: {movie_details['Director']}\n")
            self.result_text.insert(tk.END, f"Plot: {movie_details['Plot']}\n")
        else:
            self.result_text.insert(tk.END, f"Movie details not found for '{self.entry.get()}'.")

    #crating the infomation
    def get_movie_info(self):
        
        self.result_text.delete(1.0, tk.END)

        # Get movie title from the entry widget
        movie_title = self.entry.get()

        if movie_title:
            
            movie_details = self.fetch_movie_details(movie_title)            
            self.display_movie_details(movie_details)
        else:
            self.result_text.insert(tk.END, "Please enter a movie title.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()
