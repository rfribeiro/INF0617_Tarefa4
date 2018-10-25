import sys

vocab = {}

for line in sys.stdin:

    file, word, count = line.split(',')
    count = int(count)
    if word not in vocab :
        vocab[word] = count
    else :
        vocab[word] = vocab[word] + count

sorted_vocab = sorted(vocab.items(), key=lambda kv: kv[1], reverse = True)
[print(i) for i,v in sorted_vocab[:3000]]