def add_internet_ad_budget(data):
    """Create 'Internet Ad Budget' based on the TV and Radio budgets."""
    data['Internet Ad Budget'] = (data['TV Ad Budget ($)'] + data['Radio Ad Budget ($)']) / 2
    data = data[['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)', 'Internet Ad Budget', 'Sales ($)']]
    
    # Optional: rename columns for simplicity
    data.columns = ['TV Ad Budget', 'Radio Ad Budget', 'Newspaper Ad Budget', 'Internet Ad Budget', 'Sales']
    
    return data

def adjust_sales_with_internet(data, impact_factor=0.1):
    """Adjust sales based on the Internet Ad Budget."""
    data['Adjusted Sales'] = data['Sales'] + (data['Internet Ad Budget'] * impact_factor)
    return data.drop('Sales', axis=1)