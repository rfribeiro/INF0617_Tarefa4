import sys
import csv

authors = {}

f = open('/tmp/data/gut/master_list.csv')
reader = csv.reader(f)
for i in range(5):
    next(reader)

for row in reader :
    authors[row[4]] = row[3]

f.close()

vocab = {}
with open('/tmp/data/vocabulary/part-00000') as f:
    for line in f:
        vocab[line.strip()] = True

#print(vocab)

counts = {}

for line in sys.stdin:

    file, word, count = line.split(',')
    
    try :
        author = authors[file]
    except :
        continue
        
    if author not in counts :
            counts[author] = {word: (0 if word in vocab else 1)}
    else :
        if word not in counts[author] :
            counts[author][word] = (0 if word in vocab else 1)

result = {author: round(sum(counts[author].values())/len(counts[author]), 3) for author in counts}

[print(i+", "+str(v)) for i,v in sorted(result.items(), key=lambda x: x[1], reverse = True)]