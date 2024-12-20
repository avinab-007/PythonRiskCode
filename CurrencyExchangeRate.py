import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.sandbox.tsa.diffusion2 import JumpDiffusionMerton

# Load the CSV file (adjust the path as needed)
file_path = '/Users/avi/PythonProjects/Banking/CSVData/currency_exchange_rates.csv'
data = pd.read_csv(file_path)
#print(data)
#print("Columns in dataset:", data.columns)
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year
data['Quarter'] = data['Date'].dt.to_period('Q').astype(str)

# Quarter-on-Quarter analysis
def quarter_on_quarter(data):
    # Select only currency-related numeric columns
    numeric_cols = ['USD', 'GBP', 'EURO', 'YEN']

    # Group by Quarter and calculate quarterly averages
    quarterly_avg = data.groupby('Quarter')[numeric_cols].mean().reset_index()

    # Calculate quarter-on-quarter growth/fall
    for currency in numeric_cols:
        quarterly_avg[f'{currency}_QoQ'] = quarterly_avg[currency].pct_change()

    # Plotting results
    plt.figure(figsize=(12, 6))
    for currency in numeric_cols:
        plt.plot(
            quarterly_avg['Quarter'],
            quarterly_avg[f'{currency}_QoQ'],
            label=currency,
            marker='o'
        )

    plt.title('Quarter-on-Quarter Growth/Fall')
    plt.xlabel('Quarter')
    plt.ylabel('Growth/Fall (%)')
    plt.xticks(rotation=45)
    plt.legend(title="Currency")
    plt.grid()
    plt.tight_layout()
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file

# Convert the 'Date' column to datetime for easier manipulation


def year_wise_analysis(data):
    # Group data by year and calculate the average exchange rate for each currency
    yearly_avg_rates = data.groupby('Year')[['USD', 'GBP', 'EURO', 'YEN']].mean()

    # Plot the exact exchange rates year-wise
    plt.figure(figsize=(12, 8))
    for currency in ['USD', 'GBP', 'EURO', 'YEN']:
        plt.plot(yearly_avg_rates.index, yearly_avg_rates[currency], label=currency, marker='o')

    # Chart title and labels
    plt.title('Year-wise Exchange Rates (INR)', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Exchange Rate (INR)', fontsize=14)
    plt.ylim(50, yearly_avg_rates.max().max() + 10)
    plt.yticks(range(50, int(yearly_avg_rates.max().max()) + 20, 10))
    plt.legend(title="Currency", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Show the chart
    plt.tight_layout()
    plt.show()

# Usage
quarter_on_quarter(data)
year_wise_analysis(data)