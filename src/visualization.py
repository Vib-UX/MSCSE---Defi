import matplotlib.pyplot as plt

def plot_average_liquidity_rate(years, avg_liquidity_rates):
    plt.figure(figsize=(10, 6))
    plt.plot(years, avg_liquidity_rates, marker='o', linestyle='-', color='b')
    plt.title('Average Liquidity Rate by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Liquidity Rate (Normalized)')
    plt.grid(True)
    plt.show()
