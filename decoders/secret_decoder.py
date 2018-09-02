def get_characters_count_map(string):
    """
    Returns a dict of characters and it occurrence in a string
    :param string: a string
    :return: dict (character: occurrence)
    """
    char_map = {}
    for ch in string:
        char_count = char_map.get(ch.lower(), 0) + 1
        char_map[ch.lower()] = char_count
    return char_map


def is_possible_to_build_string(string, char_occurrence_dict):
    """
    Checks if given input string can be build using characters in given dict
    :param string: a string
    :param char_occurrence_dict: dict of character occurrences
    :return: True if string can be build, otherwise false
    """
    string_occurrence_dict = get_characters_count_map(string)
    for key in string_occurrence_dict.keys():
        if not char_occurrence_dict.get(key):
            return False
        if char_occurrence_dict.get(
                key, 0) < string_occurrence_dict.get(key):
            return False
    return True


def decode_secret(secret_message, codes):
    """
    Decodes embedded code in a secret message
    :param secret_message: message to be decoded
    :param codes: codes to be decoded from message
    :return: decoded code if any, otherwise None
    """
    if not secret_message:
        return None
    char_count_map = get_characters_count_map(secret_message)
    for code in codes:
        if is_possible_to_build_string(code, char_count_map):
            # assuming that only one code is encoded in secret
            return code
    return None
