
class FeatureExtractor(object):
    # Counts unique words and special characters from data set, creating feature vector
    _word_map = []

    def __init__(self, all_data):
        self._create_word_map(all_data)

    def _create_word_map(self, data_set):
        word_indexes_map = dict()
        for proj in data_set:
            for code in proj.codes:
                    splitted_code = self._split_words_and_characters(code)
                    self._add_words_to_map(splitted_code, word_indexes_map)
        self._word_map = word_indexes_map

    @classmethod
    def _add_spaces_between_special_characters(cls, string):
        for character in string:
            if(not character. isalpha() and character != ' '):
                string = string.replace(character, " %s " % character)
        return string

    @classmethod
    def _add_words_to_map(cls, splitted_code, words_dictionary):
            for word in splitted_code:
                if (not word in words_dictionary and not word.isdigit()):
                    words_dictionary[word] = len(words_dictionary)

    @classmethod
    def _split_words_and_characters(cls, string):
        code_with_separated_characters = cls._add_spaces_between_special_characters(string)
        splitted_code = code_with_separated_characters.split()
        return splitted_code

    def _get_words_count(self, code):
        features = [0] * len(self._word_map)
        splitted_code = self._split_words_and_characters(code)
        for word in splitted_code:
            if(not word.isdigit()):
                feature_index = self._word_map[word]
                features[feature_index] = features[feature_index] + 1
        return features

    def _get_words_presence(self, code):
        # similiar to method above, but instead of count, returns binary feature
        features = [0] * len(self._word_map)
        splitted_code = self._split_words_and_characters(code)
        for word in splitted_code:
            if(not word.isdigit()):
                feature_index = self._word_map[word]
                features[feature_index] = 1
        return features

    def get_feature_vector(self, code):
        #
        feature_vector = self._get_words_count(code)
        #feature_vector = self._get_words_presence(code)
        return feature_vector
