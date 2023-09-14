# INF601 - Advanced Programming in Python
# Kelton DeBord
# Mini Project 1
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
# (10/10 points) Store this information in a list that you will convert to a ndarray in NumPy.
# (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="15d")
    closingList = [round(price) for price in hist['Close']]
    return closingList

# Create our /charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

stocks = ["SONY", "KO", "AAPL", "UAL", "NVDA"]

# Create separate plots for each stock
for stock_symbol in stocks:
    stockClosing = np.array(getClosing(stock_symbol))
    days = list(range(1, len(stockClosing) + 1))

    # Create a new figure and axis for each stock
    plt.figure()
    plt.plot(days, stockClosing)
    plt.xlabel("Days")
    plt.ylabel("Closing Price (USD $)")
    plt.title(f"Closing Price for {stock_symbol}")

    #Builds file name and saves to file
    saveFile = f"charts/{stock_symbol}.png"
    plt.savefig(saveFile)

# Show all the plots
plt.show()

def getStocks():
    print("Please enter 5 stocks to graph:")
    for i in range(1, 6):
        stock_symbol = input(f"Enter stock ticker number {i}: ").strip().upper()
        stocks.append(stock_symbol)

