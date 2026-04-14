# import nltk


# papers = {
#     'Madison': [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
#     'Hamilton': [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
#                  25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
#                  61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
#                  78, 79, 80, 81, 82, 83, 84, 85],
#     'Jay': [2, 3, 4, 5],
#     'Shared': [18, 19, 20],
#     'Disputed': [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
#     'TestCase': [64]
# }

# def read_files(filename):
#     string=[]

#     for file in filename:
#         with open (f'D:\\coding\\python\\Joy of computing using python\\Week 9\\stylometry-federalist\\data\\federalist_{file}.txt') as f:
#             string.append(f.read())
#     return('\n'.join(string))

# federalist_by_author ={}

# for author , files in papers.items():
#     federalist_by_author[author]= read_files(files)

# authors =('Hamilton','Madison','Jay','Shared','Disputed','TestCase')
    

# author_tokens={}
# length_distribution={}

# for author in authors:
#     tokens = nltk.word_tokenize(federalist_by_author[author])

#     author_tokens[author]=([token for token in tokens if any(c.isalpha() for c in token)])
#     token_lengths= [len(token) for token in author_tokens[author]]

#     length_distribution[author] = nltk.FreqDist(token_lengths)

#     length_distribution[author].plot(15, title=author)


import nltk
import matplotlib.pyplot as plt

# download required data
nltk.download('punkt')

# paper groups
papers = {
    'Madison': [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
    'Hamilton': [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                 61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                 78, 79, 80, 81, 82, 83, 84, 85],
    'Jay': [2, 3, 4, 5],
    'Shared': [18, 19, 20],
    'Disputed': [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
    'TestCase': [64]
}

# read files
def read_files(filenames):
    text = []
    for file in filenames:
        path = f'D:\\coding\\python\\Joy of computing using python\\Week 9\\stylometry-federalist\\data\\federalist_{file}.txt'
        
        try:
            with open(path, encoding='utf-8') as f:
                text.append(f.read())
        except FileNotFoundError:
            print("File not found:", path)
    
    return '\n'.join(text)

# store data
federalist_by_author = {}

for author, files in papers.items():
    federalist_by_author[author] = read_files(files)

authors = ('Hamilton','Madison','Jay','Shared','Disputed','TestCase')

author_tokens = {}
length_distribution = {}

# process each author
for author in authors:
    print("Processing:", author)

    text = federalist_by_author[author]

    if not text:
        print("No data found for", author)
        continue

    tokens = nltk.word_tokenize(text)

    # keep only words
    filtered_tokens = [t.lower() for t in tokens if t.isalpha()]
    author_tokens[author] = filtered_tokens

    # word lengths
    token_lengths = [len(t) for t in filtered_tokens]

    # frequency distribution
    length_distribution[author] = nltk.FreqDist(token_lengths)

    # plot
    length_distribution[author].plot(15, title=f"{author} Word Length Distribution")

# show all graphs
plt.show()