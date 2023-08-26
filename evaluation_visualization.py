import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy as np
import pandas as pd

import evaluation_functions

df_cleaned_initial = evaluation_functions.df_cleaned_initial


def run_function(df, function, title="Words proportion for each year"):
    function(df, title)
    return


def visualize_parts_venn(df, title):
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.ravel()

    # Loop through years and create Venn diagrams
    for i, year in enumerate(df.columns):
        total_words = set(range(df.loc[df.index[0], year]))
        unique_words = set(range(df.loc[df.index[1], year]))

        venn2(
            [total_words, unique_words],
            set_labels=(df.index[0], df.index[1]),
            ax=axs[i],
        )

        axs[i].set_title(f"Year {year}")
    # Add a title for the entire plot
    plt.suptitle(title)

    # Display the plot
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


def visualize_parts_circles(df, title):
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.ravel()

    # Loop through years and create pie charts
    for i, year in enumerate(df.columns):
        total_words = df.loc[df.index[0], year]
        unique_words = df.loc[df.index[1], year]
        common_words = total_words - unique_words

        labels = df.index[0], df.index[1]
        sizes = [common_words, unique_words]
        colors = ["blue", "orange"]

        axs[i].pie(
            sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140
        )
        axs[i].axis(
            "equal"
        )  # Equal aspect ratio ensures that pie is drawn as a circle.

        axs[i].set_title(f"Year {year}")

    # Add a title for the entire plot
    plt.suptitle(title)

    # Display the plot
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


def visualize_parts_barchart(df, title):
    # Get years from the DataFrame columns
    years = df.columns

    # Get word counts from the DataFrame
    word_counts = {
        "All words": df.loc["All words"],
        "Unique words": df.loc["Unique words"],
    }

    x = np.arange(len(years))  # the label locations
    width = 0.4  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots()

    for attribute, counts in word_counts.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, counts, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("Word Count")
    ax.set_title(title)
    ax.set_xticks(x + width / 2, years)
    ax.legend(loc="upper right")
    ax.set_ylim(0, 2200)

    plt.tight_layout()
    plt.show()


run_function(df_cleaned_initial, visualize_parts_barchart)
