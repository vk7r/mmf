from src.load_data import load_data
from src.load_data import load_player_runs
from src.plot_runs import plot_player_runs
from src.metrics import run_direction_metrics

if __name__ == "__main__":
    # player_name = "İlkay Gündoğan"
    # player_name = "Erling Haaland"
    player_name = "Bernardo Silva"
    # player_name = "Rodri"

    # Load the runs.parquet file
    df = load_data("Data/18768058_runs.parquet")
    # df = load_player_runs("Data/18768058_runs.parquet", player_name=player_name)
    # print("Available players:", df["player"].unique())
    
    # Plot runs
    plot_player_runs(df, player_name)
    
    # Compute direction metrics
    avg_dir, var_dir = run_direction_metrics(df, player_name)
