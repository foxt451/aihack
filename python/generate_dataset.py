import os
import pandas as pd

# Create a list to store the text files
texts = []
base_dir = "../prompt_data/raw_text/docs"
# Get all the text files in the text directory
for file in os.listdir(base_dir):

    # Open the file and read the text
    with open(base_dir + "/" + file, "r", encoding="UTF-8") as f:
        text = f.read()
        texts.append((file, text))

# Create a dataframe from the list of texts
df = pd.DataFrame(texts, columns=['fname', 'text'])

# Set the text column to be the raw text with the newlines removed
df['text'] = df.fname + ". " + df.text
df.to_csv('../prompt_data/processed/all.csv')
df.head()
