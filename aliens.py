
def request_for(msg: str):
    return input(msg)

class HandleTranslate:

    DEFAULT_ALPHABETICAL_ORDER = 'zyxwvutsrqpoñnmlkjihgfedcba'

    def __init__(self, 
        alphabetical_order: str=None,
        words: str=""
        ):
        self.alphabetical_order = alphabetical_order or self.DEFAULT_ALPHABETICAL_ORDER
        self.words = words

    @classmethod
    def make_alpha_dict(cls, alphabetical_order):
        return {x: [] for x in alphabetical_order}
    
    @classmethod
    def separate_words(cls, words):
        return words.split(",")
    
    @classmethod
    def clean_word(cls, word):
        return word.strip()

    @classmethod
    def validate(cls, letters, words):
        words = words.replace(",","").replace(" ","")
        for w in words:
            if not w in letters:
                raise BaseException("Ups, your letter '{}' is not in your dictionary".format(w))

    @classmethod
    def bubble_sort(cls, words):
        n = len(words)
        for i in range(1, n):
            for j in range(0, n - 1):
                if words[j] > words[j + 1]:
                    temp = words[j]
                    words[j] = words[j + 1]
                    words[j + 1] = temp
            i += 1
        return words

    def order_words_by_alphabetical_order(self):
        alpha_dict = self.make_alpha_dict(self.alphabetical_order)
        self.validate(alpha_dict.keys(), self.words)
        sw = self.separate_words(self.words)
        for word in sw:
            cw = self.clean_word(word)
            alpha_dict[cw[0]].append(cw)
        
        ordered_words = []
        for words in alpha_dict.values():
            ordered_words += self.bubble_sort(words)

        return ordered_words
            

if __name__ == "__main__":
    name = request_for("Please tell me your name (only string): ")
    print(f"Hello dear {name}")
    alphabetical_order = request_for("Please tell me how your alphabet is ordered: ")
    words = request_for("Please write me the words you want me to order (Separated by comma): ")
    ht = HandleTranslate(alphabetical_order, words)
    print(ht.order_words_by_alphabetical_order())
    