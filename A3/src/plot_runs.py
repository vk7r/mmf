from mplsoccer import Pitch
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def plot_player_runs(df, player_name):
    # Filter for selected player
    player_df = df[df["player"] == player_name]
    if player_df.empty:
        print(f"No runs found for {player_name}")
        return

    # --- Filter runs inside pitch ---
    # player_df = player_df[
    #     (player_df["start_x"].between(0, 120)) &
    #     (player_df["end_x"].between(0, 120)) &
    #     (player_df["start_y"].between(0, 80)) &
    #     (player_df["end_y"].between(0, 80))
    # ]
    player_df = player_df[
        (player_df["start_x"].between(0, 100)) &
        (player_df["end_x"].between(0, 100)) &
        (player_df["start_y"].between(0, 100)) &
        (player_df["end_y"].between(0, 100))
    ]


    if player_df.empty:
        print(f"No runs inside the pitch for {player_name}")
        return

    # Print all runs that will be plotted
    # print("Runs to be plotted:")
    # print(player_df[["start_x", "start_y", "end_x", "end_y"]])

    x_start = player_df["start_x"]
    y_start = player_df["start_y"]
    x_end = player_df["end_x"]
    y_end = player_df["end_y"]
    dx = x_end - x_start
    dy = y_end - y_start


    run_speed = player_df["avg_speed"].to_numpy()*1.60934 if "avg_speed" in player_df.columns else np.sqrt(dx**2 + dy**2)

    # --- Custom colormap: blue (slow) -> red (fast) ---
    speed_cmap = LinearSegmentedColormap.from_list("speed_cmap", ["blue", "red"])

    # --- Draw pitch ---
    # pitch = Pitch(pitch_type='opta', pitch_color='white', line_color='black')
    pitch = Pitch(pitch_type='custom', pitch_length=100, pitch_width=100,
              pitch_color='white', line_color='black')

    fig, ax = pitch.draw(figsize=(10, 10))

    ax.scatter(97.6, 31.8, color='gold',edgecolors="black", s=200, marker='*', label='Unintended Assist')

    # --- Plot runs ---
    quiv = ax.quiver(
        x_start, y_start, dx, dy,
        run_speed,
        cmap=speed_cmap,
        scale_units='xy', scale=1,
        width=0.003,
        alpha=1.0
    )

    # --- Small colorbar ---
    cbar = fig.colorbar(quiv, ax=ax, fraction=0.03, pad=0.04)
    cbar.set_label("Average Speed (km/h)")

    ax.set_title(f"{player_name} - Runs color-coded by speed", fontsize=16, pad=20)
    plt.show()
