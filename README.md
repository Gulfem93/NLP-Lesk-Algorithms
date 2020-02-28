# NLP-Lesk-Algorithms

The Lesk algorithm is based on the assumption that words in a given "neighborhood" (section of text) will tend to share a common topic. A simplified version of the Lesk algorithm is to compare the dictionary definition of an ambiguous word with the terms contained in its neighborhood. Versions have been adapted to use WordNet. An implementation might look like this:

1)for every sense of the word being disambiguated one should count the amount of words that are in both neighborhood of that word and in the dictionary definition of that sense

2)the sense that is to be chosen is the sense which has the biggest number of this count

## Ex:
# PINE 
1. kinds of evergreen tree with needle-shaped leaves
2. waste away through sorrow or illness
# CONE 
1. solid body which narrows to a point
2. something of this shape whether solid or hollow
3. fruit of certain evergreen trees
