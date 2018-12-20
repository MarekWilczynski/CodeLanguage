from unittest import TestCase
import feature_extraction as fe
import collections
class TestFeatureExtractor(TestCase):
    def test__add_spaces_between_special_characters(self):
        # given
        test_string = "k a!wk.a[ple{go}c#ze"

        # when
        result = fe.FeatureExtractor._add_spaces_between_special_characters(test_string)

        # then
        expected_result = "k a ! wk . a [ ple { go } c # ze"
        self.assertEqual(result, expected_result)

    def test__add_words_to_map(self):
        # given
        test_data = [["h e h e { niezły test.bardzo } "]]
        extractor = fe.FeatureExtractor(test_data)

        # when
        result = extractor._word_map

        # then
        expected_result = dict({'h' : 0, 'e' : 1, '{' : 2, 'niezły' : 3, 'test' : 4, '.' : 5, 'bardzo': 6, '}' : 7})
        self.assertEqual(result, expected_result)

    def test_get_word_count(self):
        # given
        test_data = [["niezły niezły test"]]
        extractor = fe.FeatureExtractor(test_data)

        # when
        result = extractor._get_words_count(test_data[0][0])

        # then
        expected_result = [2, 1]
        self.assertEqual(result, expected_result)

    def test_get_word_presence(self):
        # given
        test_data = [["niezły niezły test"]]
        extractor = fe.FeatureExtractor(test_data)

        # when
        result = extractor._get_words_presence(test_data[0][0])

        # then
        expected_result = [1, 1]
        self.assertEqual(result, expected_result)
