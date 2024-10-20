user_input = input("text: ")
sentence_list = user_input.split()
sentence_dict = {word:sentence_list.count(word) for word in sentence_list}
sorted_dict = dict(sorted(sentence_dict.items()))
for word in sorted_dict:
    count = 0
    if len(word) > count:
        count = len(word)
for word, value in sorted_dict.items():
    print(f"{word :<{count}} : {value}")
"""for word, value in sentence_dict.items():
    if word == word:
        value = value + value
    else:"""

