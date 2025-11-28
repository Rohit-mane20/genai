# what is one_hot_encoding
# One-hot encoding is a technique used in machine learning and
# natural language processing to convert categorical data into a binary vector representation. Each category is represented
# as a vector where only one element is "hot" (set to 1) and all other elements are "cold" (set to 0). This allows algorithms to
# process categorical data without assuming any ordinal relationship between the categories.

review1 = "the food is good"
review2 = "the food is bad"
review3  = "pizza is amazing"

# Create a vocabulary from the reviews
vocabulary = set(review1.split() + review2.split() + review3.split())
vocabulary = list(vocabulary)
print("Vocabulary:", vocabulary)

#  the food is good bad  pizza amazing
# one-hot encode the reviews
d1 = [
    
    [ 1 if word in review1.split() else 0 for word in vocabulary ],
    [ 1 if word in review2.split() else 0 for word in vocabulary ],
    [ 1 if word in review3.split() else 0 for word in vocabulary ]
]
# ouptput
print("One-hot Encoded Vectors:")
print( d1 )
d1 = []


# advantages  of one-hot encoding
# 1. Simplicity: One-hot encoding is straightforward to implement and understand.
# 

# disadvantages of one-hot encoding
# 1.overfitting: One-hot encoding can lead to overfitting, especially with high-cardinality categorical variables.
# 2. Increased Dimensionality: One-hot encoding can significantly increase the dimensionality of the dataset,
# especially when dealing with categorical variables with many unique values.
# 3.we need fixed size of vocabulary but in real world its not possible always.