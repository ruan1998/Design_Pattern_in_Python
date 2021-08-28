from collections import Counter
from string import ascii_lowercase as alphabet
import matplotlib.pyplot as plt

class CharCounter(Counter):
    def load(self, content):
        self.update(content)

    @property
    def alphabet_count(self):
        return {letter: self[letter] for letter in alphabet}

    @property
    def alphabet_freq(self):
        total = sum(self.alphabet_count.values())
        return {letter:  round(freq/ total, 3) 
                for letter, freq in self.alphabet_count.items()}

class FileManager:
    @staticmethod
    def load(path):
        with open(path, 'r', encoding="utf-8") as file:
            content = file.read().lower()
        return content

    @staticmethod
    def save(content, file_path):
        pass

class DictSorter:
    @staticmethod
    def by_value(dict_obj):
        return dict(sorted(dict_obj.items(), key=lambda row:row[1]))

if __name__ == '__main__':
    novel_path = "../data/txt/The_mysterious_island.txt"
    content = FileManager.load(novel_path)
    cc = CharCounter()
    cc.load(content)
    # print(cc.most_common(20))
    # print(cc.alphabet_count)

    letters, pcts = cc.alphabet_freq.keys(), cc.alphabet_freq.values()

    plt.figure(figsize=(8, 2))
    plt.subplot(121)
    plt.bar(letters, pcts)

    plt.subplot(122)
    plt.bar(*list(zip(*DictSorter.by_value(cc.alphabet_freq).items())))
    plt.show()