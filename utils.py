
import pandas as pd


def calculate_daily_totals(df):
    """Return total kWh consumption per day."""
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df.resample('D', on='timestamp')['energy_kwh'].sum()


def calculate_weekly_aggregates(df):
    """Return weekly aggregated kWh consumption."""
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df.resample('W', on='timestamp')['energy_kwh'].sum()


def building_wise_summary(df):
    """Return summary statistics for each building."""
    return df.groupby("building")['energy_kwh'].agg([
        'min', 'max', 'mean', 'sum'
    ])
