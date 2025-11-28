# what is named entity recognition in NLP?
# Named Entity Recognition (NER) is a subtask of natural language processing (NLP)
# that involves identifying and classifying named entities mentioned in unstructured text into predefined categories.
# These categories can include names of people, organizations, locations, dates, quantities, monetary values,
# percentages, and more. NER helps in extracting meaningful information from text data, making it easier to analyze and understand.
# NER is widely used in various applications such as information retrieval, question answering systems,
# machine translation, and text summarization.



import nltk
from nltk.tokenize import word_tokenize
from nltk.chunk import ne_chunk
nltk.download('maxent_ne_chunker')

nltk.download('maxent_ne_chunker_tab')

nltk.download('words')


sentence = """The eiffel tower is one of the most famous landmarks in Paris.
            it was constructed in 1889 and stands at a height of 324 meters.
            Built by the French engineer Gustave Eiffel, the tower attracts millions of visitors each year.
            It costed 7.8 million francs to build the tower and was initially criticized by some of the leading artists and intellectuals of the time.
        """

# expected output : [('eiffel tower', 'GPE'), ('Paris', 'GPE'), ('1889', 'DATE'), ('324 meters', 'QUANTITY'), 
# ('Gustave Eiffel', 'PERSON'), ('7.8 million francs', 'MONEY')]

words = word_tokenize(sentence)
tag_elements = nltk.pos_tag(words)
named_entities = ne_chunk(tag_elements).draw()
print(named_entities, " named entities")
# ne_chunk returns a tree structure with named entities labeled


