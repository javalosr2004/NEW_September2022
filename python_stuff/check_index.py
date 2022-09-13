import re


'''returns all matches and their indexes of a matching keyword(s) in a given text

returns (keyword, start_index, end_index)
'''
def check_index(text : str, keyword : str, *args):
    all_matches = []
    keyword_list = []
    if len(args) < 1:
        keyword_list.append(keyword)
    else:
        keyword_list.append(keyword)
        keyword_list.extend(args)
    for keyword in keyword_list:
        for m in re.finditer(keyword, text):
            all_matches.append((m.group(), m.start(), m.end()))
    return all_matches

'''returns all matches and their indexes from a list of words and given keyword(s), 
it also returns the index of the text where the keyword was found

returns (index, keyword, start_index, end_index)

'''
def check_indexes(text_list : list, keyword : str, *args):
    all_matches = {}
    if len(args) < 1:
        for index_text in range(len(text_list)):
            for m in re.finditer(keyword, text_list[index_text]):
                all_matches[f'Index: {(index_text)}'] = ((index_text, m.group(), m.start(), m.end()))
    else:
        keyword_list = []
        keyword_list.append(keyword)
        keyword_list.extend(args)
        for index_text in range(len(text_list)):
            for keyword in keyword_list:
                for m in re.finditer(keyword, text_list[index_text]):
                    all_matches[f'Index: {(index_text)}'] = ((index_text, m.group(), m.start(), m.end()))
    return all_matches


if __name__ == '__main__':
    
    #example of how this function works with a single text and multiple keywords
    word = 'this is an extreme example of a python string and regex in action and extreme example'
    regex_found = check_index(word, 'extreme example', 'python')
    print(regex_found)

    #how this function works with multiple words and a singular keyword
    word_list = ['blah blah blah ssn blah blah', 'the duck ate a peice of bread', 'so I just opened up a new bank account with my ssn', "I don't know why banks use peoples ssn"]
    regex_found_multiple = check_indexes(word_list, 'ssn')
    print(regex_found_multiple) #finds multiple times that ssn was found
    
    
