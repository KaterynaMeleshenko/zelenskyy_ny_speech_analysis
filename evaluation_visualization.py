import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy as np
import pandas as pd

import evaluation_functions

df_cleaned_initial = evaluation_functions.df_evaluate


def run_function(df, function, title, bar_1, bar_2):
    function(df, title, bar_1, bar_2)
    return


# def visualize_parts_venn(df, title):
#     # Create subplots
#     fig, axs = plt.subplots(2, 2, figsize=(12, 10))
#     axs = axs.ravel()

#     # Loop through years and create Venn diagrams
#     for i, year in enumerate(df.columns):
#         total_words = set(range(df.loc[df.index[0], year]))
#         unique_words = set(range(df.loc[df.index[1], year]))

#         venn2(
#             [total_words, unique_words],
#             set_labels=(df.index[0], df.index[1]),
#             ax=axs[i],
#         )

#         axs[i].set_title(f"Year {year}")
#     # Add a title for the entire plot
#     plt.suptitle(title)

#     # Display the plot
#     plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#     plt.show()


# def visualize_parts_circles(df, title):
#     # Create subplots
#     fig, axs = plt.subplots(2, 2, figsize=(12, 10))
#     axs = axs.ravel()

#     # Loop through years and create pie charts
#     for i, year in enumerate(df.columns):
#         total_words = df.loc[df.index[0], year]
#         unique_words = df.loc[df.index[1], year]
#         common_words = total_words - unique_words

#         labels = df.index[0], df.index[1]
#         sizes = [common_words, unique_words]
#         colors = ["blue", "orange"]

#         axs[i].pie(
#             sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140
#         )
#         axs[i].axis(
#             "equal"
#         )  # Equal aspect ratio ensures that pie is drawn as a circle.

#         axs[i].set_title(f"Year {year}")

#     # Add a title for the entire plot
#     plt.suptitle(title)

#     # Display the plot
#     plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#     plt.show()


def visualize_parts_barchart(df, title, bar_1, bar_2):
    # Get years from the DataFrame columns
    years = df.columns

    # Get word counts from the DataFrame
    word_counts = {
        bar_1: df.loc[bar_1],
        bar_2: df.loc[bar_2],
    }

    x = np.arange(len(years))  # the label locations
    width = 0.4  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots()

    for attribute, counts in word_counts.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, counts, width, label=attribute)
        ax.bar_label(rects, padding=3)

        if attribute == bar_2:
            total_words_counts = df.loc[bar_1]  # Total words counts for each year
            percentages = [
                count / total * 100 for count, total in zip(counts, total_words_counts)
            ]
            for i, rect in enumerate(rects):
                ax.annotate(
                    f"{percentages[i]:.1f}%",
                    xy=(rect.get_x() + rect.get_width() / 2, rect.get_height()),
                    xytext=(
                        0,
                        -15,
                    ),  # Adjust the y-coordinate here for vertical positioning
                    textcoords="offset points",
                    ha="center",
                    va="bottom",
                )

        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("Word Count")
    ax.set_title(title)
    ax.set_xticks(x + width / 2, years)
    ax.legend(loc="upper right")
    ax.set_ylim(0, 2200)

    plt.tight_layout()
    plt.show()


run_function(
    df_cleaned_initial,
    visualize_parts_barchart,
    "Words proportion for each year",
    "All words",
    "Unique words",
)
run_function(
    df_cleaned_initial,
    visualize_parts_barchart,
    "Words proportion for each year",
    "All words",
    "Filtered unique words",
)
run_function(
    df_cleaned_initial,
    visualize_parts_barchart,
    "Words proportion for each year",
    "Unique words",
    "Filtered unique words",
)

#just a comment