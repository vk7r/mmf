import pandas as pd

def load_data(filepath):
    """Load the run data from a Parquet file and return as DataFrame."""
    df = pd.read_parquet(filepath)
    print("Data loaded. Columns:", df.columns)
    print("Number of runs:", len(df))
    return df


def load_player_runs(filepath, player_name):
    # Load full dataset
    df = pd.read_parquet(filepath)
    print("Data loaded. Columns:", df.columns)
    print("Total runs in dataset:", len(df))

    # Filter for the specific player
    player_df = df[df['player'] == player_name]
    print(f"Number of runs for {player_name}: {len(player_df)}")

    return player_df