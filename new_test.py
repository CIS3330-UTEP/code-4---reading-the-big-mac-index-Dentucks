import pandas as pd

big_mac_file = './big-mac-full-index.csv'

# Function to get the mean price of a Big Mac in a specific year for a country
def get_big_mac_price_by_year(year, country_code):
    df = pd.read_csv(big_mac_file)
    # Filter by year and country code
    filtered_data = df[(df['iso_a3'].str.lower() == country_code.lower()) & (df['date'].str.contains(str(year)))]
    if not filtered_data.empty:
        return round(filtered_data['dollar_price'].mean(), 2)
    else:
        return f"No data available for {country_code.upper()} in {year}"

# Function to get the mean price of a Big Mac for a country
def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    # Filter by country code
    filtered_data = df[df['iso_a3'].str.lower() == country_code.lower()]
    if not filtered_data.empty:
        avg_price = round(filtered_data['dollar_price'].mean(), 2)
        return avg_price
    else:
        return f"No data available for {country_code.upper()}"

# Function to find the country with the cheapest Big Mac in a specific year
def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    # Filter by year
    filtered_data = df[df['date'].str.contains(str(year))]
    if not filtered_data.empty:
        # Find the country with the minimum price
        min_price_row = filtered_data.loc[filtered_data['dollar_price'].idxmin()]
        result = f"{min_price_row['name']}({min_price_row['iso_a3']}): ${min_price_row['dollar_price']:.1f}"
        return result
    else:
        return f"No data available for the year {year}"

# Function to find the country with the most expensive Big Mac in a specific year
def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    # Filter by year
    filtered_data = df[df['date'].str.contains(str(year))]
    if not filtered_data.empty:
        # Find the country with the maximum price
        max_price_row = filtered_data.loc[filtered_data['dollar_price'].idxmax()]
        result = f"{max_price_row['name']}({max_price_row['iso_a3']}): ${max_price_row['dollar_price']:.1f}"
        return result
    else:
        return f"No data available for the year {year}"

# Main block for testing the functions
if __name__ == "__main__":
    mac1 = get_big_mac_price_by_year(2008, 'rus')
    print(mac1)
    
    mac2 = get_big_mac_price_by_country('rus')
    print(mac2)
    
    mac3 = get_the_cheapest_big_mac_price_by_year(2008)
    print(mac3)
    
    mac4 = get_the_most_expensive_big_mac_price_by_year(2003)
    print(mac4)