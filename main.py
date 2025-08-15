import random 

# Self explanatory...right?
def readFile(file_path):
    try:
        with open(file_path, 'r') as file:
            dictionary = file.readlines()
        dictionary = [word.strip() for word in dictionary]
        return dictionary
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found.")
    except Exception as e:
        print(f'An error occurred: {e}')

def makeSentence(length, dictionary): 
    sentence = []
    for i in range(length):
        # random number between 0 and length of dict
        word = dictionary[random.randint(0, len(dictionary))]
        sentence.append(word)

    return sentence

def main():
    # Start by reading the dictionary file into a list
    file_path = "dictionary.txt"
    dictionary = readFile(file_path)

    # Make new sentence of length 5 words
    sentence = makeSentence(5, dictionary)
    print(sentence)

if __name__ == '__main__':
    main()

