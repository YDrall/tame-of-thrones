import unittest
from decoders import secret_decoder


class DecodeSecretTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_string_and_empty_codes(self):
        secret = ""
        codes = []
        expected_message = None
        decoded_message = secret_decoder.decode_secret(secret, codes)
        self.assertEqual(expected_message, decoded_message)

    def test_empty_string_and_not_empty_codes(self):
        secret = ""
        codes = ["owl"]
        expected_message = None
        decoded_message = secret_decoder.decode_secret(secret, codes)
        self.assertEqual(expected_message, decoded_message)

    def test_secret_with_matching_codes(self):
        secret = "a1d22n333a4444P"
        codes = ["owl", "panda"]
        expected_message = "panda"
        decoded_message = secret_decoder.decode_secret(secret, codes)
        self.assertEqual(expected_message, decoded_message)

    def test_random(self):
        secret = "Go, risk it all"
        codes = ["gorilla"]
        expected_message = "gorilla"
        decoded_message = secret_decoder.decode_secret(secret, codes)
        self.assertEqual(expected_message, decoded_message)


class CharacterCountTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_string(self):
        empty_string = ""
        count_map = secret_decoder.get_characters_count_map(empty_string)
        self.assertEqual(count_map, {})

    def test_one_character_string(self):
        string = "a"
        count_map = secret_decoder.get_characters_count_map(string)
        self.assertEqual(count_map, {'a': 1})

    def test_all_same_characters_string(self):
        string = "bbbbbbbb"
        count_map = secret_decoder.get_characters_count_map(string)
        self.assertEqual(count_map, {'b': 8})

    def test_random_string(self):
        string = "abaabbccddd"
        expected_map = {
            'a': 3,
            'b': 3,
            'c': 2,
            'd': 3
        }
        count_map = secret_decoder.get_characters_count_map(string)
        self.assertEqual(count_map, expected_map)

    def test_random_string2(self):
        string = "a1d22n333a4444p"
        expected_map = {
            'a': 2,
            '1': 1,
            'd': 1,
            '2': 2,
            'n': 1,
            '3': 3,
            '4': 4,
            'p': 1
        }
        count_map = secret_decoder.get_characters_count_map(string)
        self.assertEqual(count_map, expected_map)


class BuildStringCheckTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_string_should_match(self):
        string = ""
        count_map = {'a': 1, 'b': 5}
        expected_result = True
        returned_result = secret_decoder.is_possible_to_build_string(string, count_map)
        self.assertEqual(returned_result, expected_result)

    def test_string_with_more_than_one_occurrence_with_insufficient_characters_count(self):
        string = "aabb"
        count_map = {'a': 1, 'b': 5}
        expected_result = False
        returned_result = secret_decoder.is_possible_to_build_string(string, count_map)
        self.assertEqual(returned_result, expected_result)

    def test_string_with_more_than_one_occurrence_with_sufficient_characters_count(self):
        string = "aabb"
        count_map = {'a': 2, 'b': 2}
        expected_result = True
        returned_result = secret_decoder.is_possible_to_build_string(string, count_map)
        self.assertEqual(returned_result, expected_result)

    def test_string_with_more_than_one_occurrence_with_more_that_sufficient_characters_count(self):
        string = "aabb"
        count_map = {'a': 5, 'b': 5}
        expected_result = True
        returned_result = secret_decoder.is_possible_to_build_string(string, count_map)
        self.assertEqual(returned_result, expected_result)

    def test_string_random(self):
        string = "panda"
        count_map = {'a': 2, 'p': 1, 'n': 1, 'd': 1}
        expected_result = True
        returned_result = secret_decoder.is_possible_to_build_string(string, count_map)
        self.assertEqual(returned_result, expected_result)

if __name__ == '__main__':
    unittest.main()
