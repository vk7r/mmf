import numpy as np
from scipy.stats import circmean, circstd

def run_direction_metrics(df, player_name):
    """Calculate average run direction and variation for a player."""
    player_runs = df[df['player'] == player_name]
    dx = player_runs['end_x'] - player_runs['start_x']
    dy = player_runs['end_y'] - player_runs['start_y']

    angles = np.arctan2(dy, dx)
    
    avg_angle = circmean(angles, high=np.pi, low=-np.pi)
    variation = circstd(angles, high=np.pi, low=-np.pi)
    
    print(f"Average run direction (radians): {avg_angle}")
    print(f"Run direction variation (radians): {variation}")
    
    return avg_angle, variation
