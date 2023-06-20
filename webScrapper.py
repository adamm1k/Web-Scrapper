import requests
import customtkinter
from bs4 import BeautifulSoup
import tkinter as tk


def scrape_articles(url):
    # Send a GET request
    response = requests.get(url)

    # BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the article elements on the page
    articles = soup.find_all('article')

    # Iterate over each article and extract the title, URL, and description
    for article in articles:
        title = article.find('h2').text.strip()
        url = article.find('a')['href']
        
        # Extract the description if available
        description = article.find('p').text.strip() if article.find('p') else ""

        # Display the results in the GUI window
        result_text.insert(customtkinter.END, f"Title: {title}\n\n")
        result_text.insert(customtkinter.END, f"URL: {url}\n\n")
        result_text.insert(customtkinter.END, f"Description: {description}\n\n")

def scrape_button_click():
    # Clear the previous results
    result_text.delete('1.0', tk.END)

    # Get the URL from the user input
    url = url_entry.get()

    # Scrape the articles and display the results
    scrape_articles(url)

# Create the GUI window
window = customtkinter.CTk()
window.title("SiteScouter")
window.geometry("600x400")
window.iconbitmap(r"C:\Users\theli\Downloads\spider.ico")

# Title of the GUI
title_label = customtkinter.CTkLabel(window, text="SiteScouter", font=("Georgia", 20, "bold"))
title_label.pack(pady=10)

# Create and position the URL entry field
url_label = customtkinter.CTkLabel(window, text="Enter URL:")
url_label.pack()
url_entry = customtkinter.CTkEntry(window, width=200)
url_entry.pack()

# Create and position the Scrape button
scrape_button = customtkinter.CTkButton(window, text="Scrape Articles", command=scrape_button_click)
scrape_button.pack()

# Create and position the result text area
result_label = customtkinter.CTkLabel(window, text="Scraped Articles:")
result_label.pack()
result_text = customtkinter.CTkTextbox(window, width=300, height=170)
result_text.pack()

#Links
link_text = customtkinter.CTkLabel(window, text="(Contact Info) Github: adamm1k | E-Mail: adammengistu13@outlook.com")
link_text.pack(side = "bottom", pady = 10)

# Start the GUI event loop
window.mainloop()
