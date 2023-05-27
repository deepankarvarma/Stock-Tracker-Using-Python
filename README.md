# Stock Tracker using Python

This repository contains code for a simple stock tracker web application built with Python and Streamlit. The application allows users to track the stock prices of various companies using the `yfinance` library and visualizes the data using line charts and tables.

## Installation

To run the stock tracker application locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/<username>/<repository>.git
   ```

2. Navigate to the project directory:

   ```shell
   cd <repository>
   ```

3. Install the required dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

4. Run the application:

   ```shell
   streamlit run app.py
   ```

   The application will be accessible at [http://localhost:8501](http://localhost:8501) in your web browser.

## Usage

1. Open the application in your web browser.

2. Enter the stock ticker symbol in the text input box (e.g., AAPL for Apple Inc., INTC for Intel Corporation).

3. Press Enter or click outside the input box to update the visualization.

4. The application will display a line chart representing the closing prices of the stock over time.

5. Additionally, a table containing the stock data will be displayed below the chart.

## About the Code

The main code file `app.py` contains the following components:

- Importing the required libraries: `streamlit`, `yfinance`, and `pandas`.
- Setting the page title and background image using Streamlit's `set_page_config` and `markdown` functions.
- Defining a function `get_stock_data` that uses the `yf.download` function from `yfinance` to retrieve stock data for a given ticker symbol.
- Using Streamlit's `sidebar` and `text_input` functions to allow users to input a stock ticker.
- Calling the `get_stock_data` function to retrieve the stock data for the entered ticker.
- Displaying the stock data in a line chart using Streamlit's `line_chart` function.
- Displaying the stock data in a table using Streamlit's `write` function.

## Additional Information

The stock tracker application is deployed using Streamlit and can be accessed online at [Stock Tracker App](https://deepankarvarma-stock-tracker-using-python-app-sos8ew.streamlit.app/).

For more information about Streamlit, refer to the [Streamlit documentation](https://docs.streamlit.io/).

## Contributing

Contributions to the repository are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
