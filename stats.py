
def get_total_words(text):
    num_words = len(text.split())
    return num_words

def get_word_repetitions(text):
    word_count_dict = {}
    for word in text:
        word = word.lower()
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict

def sort_dictionary(dict):
    def sort_on(items):
        return items["num"]

    sorted_dicts = []
    for key, value in dict.items():
        sorted_dicts.append({"char": key, "num" : value})
    sorted_dicts.sort(reverse=True, key=sort_on)

    return sorted_dicts


