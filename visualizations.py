
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""




def plot_orderbook(ob_data_plot):
    # Find the day with the highest total volume
    highest_volume_day = max(ob_data_plot, key=lambda x: x['volume'])

    # Extract the first 20 levels for Bid and Ask sides
    bid_levels = highest_volume_day['bids'][:20]
    ask_levels = highest_volume_day['asks'][:20]

    # Prepare the data for plotting
    bid_prices = [level['price'] for level in bid_levels]
    bid_volumes = [level['volume'] for level in bid_levels]

    ask_prices = [level['price'] for level in ask_levels]
    ask_volumes = [level['volume'] for level in ask_levels]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(bid_prices)), bid_volumes, color='green', alpha=0.6)
    plt.barh(range(len(ask_prices)), ask_volumes, color='red', alpha=0.6)

    # Set axis labels and title
    plt.xlabel('Volume')
    plt.ylabel('Level')
    plt.title('Order Book - Highest Volume Day')

    # Set tick labels
    plt.yticks(range(len(bid_prices)), bid_prices)
    plt.gca().invert_yaxis()

    # Show the plot
    plt.show()
    

# Q6




# Q7

def boxplot(df_ts_tob):

    # Extract the hour from the date column
    df_ts_tob['hour'] = pd.to_datetime(df_ts_tob['date']).dt.hour

    # Group the data by hour and calculate the spread for each group
    grouped_data = df_ts_tob.groupby('hour')['spread'].apply(list)

    # Create a boxplot using Plotly Express
    fig = px.box(df_ts_tob, x='hour', y='spread', title='Spread Distribution by Hour')
    fig.show()
    
    return result




    
    