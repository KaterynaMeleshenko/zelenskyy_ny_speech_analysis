# def draw_plot(data_point):
#     """
#     Draw plot of the most common words.

#     Keyword argument:
#     text -- list of tulpes, where 1st value is a word and 2nd value is frequencies
#     """

#     words = [word for word, _ in data_point[1]]
#     frequencies = [freq for _, freq in data_point[1]]
#     max_freq = max(frequencies)

#     plt.figure(figsize=(words_num, max_freq))
#     plt.bar(words, frequencies, color='blue')
#     plt.xlabel('Words')
#     plt.ylabel('Frequencies')
#     plt.title('Most Common Words and Their Frequencies')
#     plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
#     plt.tight_layout()

#     plt.show()

# def draw_multiple_plots(data):

#     fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
#     plots_list = [ax1, ax2, ax3, ax4]

#     for plot in plots_list:
#         index = plots_list.index(plot)
#         words = [word for word, _ in data[index][1]]
#         frequencies = [freq for _, freq in data[index][1]]
#         max_freq = max(frequencies)
#         plot.bar(words,frequencies)
#         plot.set_title(data[index][0])
#         # plot.set_xlabel("Words")
#         # plot.set_ylabel("Frequencies ")

#         # Rotate x-axis labels for each plot
#         plot.set_xticklabels(words, rotation=45, ha='right')

#     # Adjust the spacing between subplots
#     plt.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9, hspace=0.4)

#     # Show the plot
#     plt.show()


# data = list()
# for path in file_paths:
#     data.append(count_common_words(path, 15))

# draw_multiple_plots(data)
