# Import packages
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");

with open('transcripts/glass_animals_heat_waves.txt', 'r+') as f:
    text = f.read()

# Generate word cloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=42, background_color='black', colormap='Set2', collocations=True, stopwords = STOPWORDS).generate(text)
# Plot
wc = plot_cloud(wordcloud)
# plt.show()

# Save image
wordcloud.to_file("wordclouds/glass_animals_heat_waves_wc.png")