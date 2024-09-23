import math

def clean_text(txt):
    """parameter: a string
       returns a list containing the words in lower cases and without punctuation marks
    """
    low = txt.lower()
    for symbol in """.,?"'!;:""":
        low = low.replace(symbol, '')
    final = low.split(' ')
    return final

class TextModel:
    """blueprint for objects that model a body of text
    """
    def __init__(self, model_name):
        """constructs a new TextModel object by accepting a string model_name as a /
           parameter and initializing a string and 5 lists
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuations = {}
    
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuations: ' + str(len(self.punctuations)) + '\n'
        return s
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
        words = 0
        for w in s.split():
            if w[-1] in ['!', '?', '.']:
                words += 1
                if words not in self.sentence_lengths:
                    self.sentence_lengths[words] = 1
                else:
                    self.sentence_lengths[words] += 1
                words = 0
            else:
                words += 1
                
        for w in s.split():
            if w[-1] in ['!', '?', '.']:
                punctuation = w[-1]
                if punctuation not in self.punctuations:
                    self.punctuations[punctuation] = 1
                else:
                    self.punctuations[punctuation] += 1
        
        word_list = clean_text(s)
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
                if len(w) not in self.word_lengths:
                    self.word_lengths[len(w)] = 1
                else:
                    self.word_lengths[len(w)] += 1
            else:
                self.words[w] += 1
                self.word_lengths[len(w)] += 1
        
        for w in word_list:
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
            else:
                self.stems[stem(w)] += 1
                
    def add_file(self, filename):
        """reads the file and updates the lists
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        txt = f.read()
        f.close()
        self.add_string(txt)
        
    def save_model(self):
        """ saves the TextModel self by writting the 5 dictionaries to files
        """
        file_name_words = self.name + '_' + 'words'
        file_name_word_lengths = self.name + '_' + 'word_lengths'
        file_name_stems = self.name + '_' + 'stems'
        file_name_sentence_lengths = self.name + '_' + 'sentence_lengths'
        file_name_punctuations = self.name + '_' + 'punctuations'
        
        nw_d = self.words
        nwl_d = self.word_lengths
        ns_d = self.stems
        nsl_d = self.sentence_lengths
        np_d = self.punctuations
        
        f = open(file_name_words, 'w') 
        f.write(str(nw_d))
        f.close()
        
        f = open(file_name_word_lengths, 'w')
        f.write(str(nwl_d))
        f.close()
        
        f = open(file_name_stems, 'w')
        f.write(str(ns_d))
        f.close()
        
        f = open(file_name_sentence_lengths, 'w')
        f.write(str(nsl_d))
        f.close()
        
        f = open(file_name_punctuations, 'w')
        f.write(str(np_d))
        f.close()
        
    def read_model(self):
        """ reads stored dictionaries and assigns them to the attributes of called TextModel
        """
        file_name_words = self.name + '_' + 'words'
        file_name_word_lengths = self.name + '_' + 'word_lengths'
        file_name_stems = self.name + '_' + 'stems'
        file_name_sentence_lengths = self.name + '_' + 'sentence_lengths'
        file_name_punctuations = self.name + '_' + 'punctuations'
        
        f = open(file_name_words, 'r')
        d_str = f.read()
        f.close()
        self.words = dict(eval(d_str))
                
        f = open(file_name_word_lengths, 'r')
        d_str = f.read()
        f.close()
        self.word_lengths = dict(eval(d_str))
        
        f = open(file_name_stems, 'r')
        d_str = f.read()
        f.close()
        self.stems = dict(eval(d_str))
        
        f = open(file_name_sentence_lengths, 'r')
        d_str = f.read()
        f.close()
        self.sentence_lengths = dict(eval(d_str))
        
        f = open(file_name_punctuations, 'r')
        d_str = f.read()
        f.close()
        self.punctuations = dict(eval(d_str))
        
    def similarity_scores(self, other):
        all_scores = []
        words_score = compare_dictionaries(other.words, self.words)
        all_scores += [words_score]
        word_lengths = compare_dictionaries(other.word_lengths, self.word_lengths)
        all_scores += [word_lengths]
        stems_score = compare_dictionaries(other.stems, self.stems)
        all_scores += [stems_score]
        sentence_lengths = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        all_scores += [sentence_lengths]
        punctuations_score = compare_dictionaries(other.punctuations, self.punctuations)
        all_scores += [punctuations_score]
        return all_scores

    def classify(self, source1, source2):
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name + ': ' + str(scores1))
        print('scores for ' + source2.name + ': ' + str(scores2))
        weighted_sum1 = 10*scores1[0] + 6*scores1[1] + 8*scores1[2] + 5*scores1[3] + 4*scores1[4]
        weighted_sum2 = 10*scores2[0] + 6*scores2[1] + 8*scores2[2] + 5*scores2[3] + 4*scores2[4]
        if weighted_sum1 > weighted_sum2:
            print(self.name + ' is more likely to have come from ' + source1.name)
        else:
            print(self.name + ' is more likely to have come from ' + source2.name)
        
def stem(s):
    if len(s) <= 3:
        return s
    else:
        if s[:2] in ['re', 'up', 'im', 'in', 'un', 'co']:
            return stem(s[2:])
        elif s[:3] in ['dis', 'mis', 'pre', 'sub', 'non']:
            return stem(s[3:])
        elif s[:5] in ['inter', 'extra']:
            return stem(s[5:])
        if s[-2:] == 'es':
            return stem(s[:-2])
        if s[-1] == 's':
            return stem(s[:-1])
        elif s[-1] == 'e':
            return stem(s[:-1])
        elif s[-1] == 'y':
            return stem(s[:-1] + 'i')
        elif s[-3:] == 'ing':  
            if len(s) > 5:
                if s[-4] == s[-5]:
                    return stem(s[0:-4])
            else:
                return stem(s[:-3])
        elif s[-2:] == 'er':
            if s[-3] == s[-4]:
                return stem(s[:-3])
            else:
                return stem(s[:-2])
        elif s[-2:] == 'ed':
            if s[-3] == s[-4]:
                return stem(s[:-3])
            else:
                return stem(s[:-2])
        elif s[-2:] == 'ly':
            return stem(s[:-2])
        else:
            return s
        
def compare_dictionaries(d1, d2):
    if d1 == {}:
        return -50
    score = 0
    total = 0
    for key in d1:
        total += d1[key]
    for key in d2:
        if key in d1:
            prob = math.log(d1[key]/total) * d2[key]
            score += prob
        else:
            prob = math.log(0.5/total) * d2[key]
            score += prob
    return score


def run_tests():
    """ your docstring goes here """
    source1 = TextModel('Stephen King')
    source1.add_file('StephenKing.txt')

    source2 = TextModel('JK Rowling')
    source2.add_file('JKRowling.txt')

    new1 = TextModel('Rick Riordan')
    new1.add_file('RickRiordan.txt')
    new1.classify(source1, source2)

if __name__ == '__main__':
    run_tests()