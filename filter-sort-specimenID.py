# This scipt reads a CSV file into a list, populates a new list without duplicates, and sorts the list.
# I use this to count the number of times I have sequenced a particular individual for a particular primer pair. 
# This is hard to do in Geneious so I export the specimenID names for each plate I run on the ABI, concatenate
# the names into one CSV file, then use this script to count the number of unique IDs for each primer pair. 

datafile = open('/Users/name/file.csv', 'r')
data = []
for row in datafile:
    data.append(row.strip())
specimenID = []
for item in data:
    if item not in specimenID:
        specimenID.append(item)
specimenID.sort()
