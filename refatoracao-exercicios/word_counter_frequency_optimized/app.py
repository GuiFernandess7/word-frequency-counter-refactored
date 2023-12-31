import argparse
import collections
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def get_frequency(iterable):
    """Frequency of words/letters in iterable"""
    freq_group = collections.Counter(iterable)
    return freq_group.items()

def extract_file_content(file: str):
    """Extrai o conteúdo do arquivo de text"""
    with open(os.path.join(BASE_PATH, f'data/{file}')) as f:
        content = f.readline().split()
        content_lower = list(map(lambda x: x.lower(), content)) 
        return content_lower

def top(freq_group):
    return sorted(freq_group, key=lambda x:x[1], reverse=True)[:20]

def accumulate(sorted_alpha):
    return '\n'.join(f'{w} {c}' for w, c in sorted_alpha)

def word_counter(file_content, order):
    return accumulate(order(get_frequency(file_content)))

def print_words(file: str):
    """Printa a frequência de letras/palavras por ordem alfabética"""
    file_content = extract_file_content(file)
    return word_counter(file_content, sorted)

def print_top(file: str):
    """Printa a frequência de letras/palavras por ordem decrescente de frequência"""
    file_content = extract_file_content(file)
    return word_counter(file_content, top)

def main(args):
    if args.count:
        print(print_words(args.count))
    elif args.topcount:
        print(print_top(args.topcount))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Word Frequency Counter")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--count', type=str, help='Nome do arquivo txt')
    group.add_argument('--topcount', type=str, help='Nome do arquivo txt')
    args = parser.parse_args()
    main(args)