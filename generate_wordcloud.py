# Import packages
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import sys

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");

# MAIN SCRIPT BODY                
if len(sys.argv) < 2:
    print("Usage: synergy_parse.py <transcript file>")
    exit()

infile = sys.argv[1]
prefix = infile.split('/')[1].strip('.txt')
with open(infile, 'r+') as f:
    text = f.read().lower()


# Generate word cloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=42, background_color='black', colormap='Set2', collocations=True, stopwords = STOPWORDS).generate(text)
# Plot
wc = plot_cloud(wordcloud)
# plt.show()

# Save image
wordcloud.to_file("wordclouds/" + prefix + ".png")