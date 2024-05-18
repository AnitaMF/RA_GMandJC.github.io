# testing fuctions work on text_example.txt file  + local examples
import text_counts as tc
import pytest
def get_input():
    filename = "text_example.txt"
    with open(filename) as fh:
        return fh.read()
    
@pytest.mark.parametrize("file_input,expected_characters", [
    (get_input(),38),
    ("character",9)
 ])    

def test_count_ch(file_input, expected_characters):
    result = tc.count_ch(file_input)
    assert result == expected_characters

@pytest.mark.parametrize("file_input,expected_words", [
    (get_input(), 10),
    ("can the function count words?",5)
])
def test_word(file_input, expected_words):
    result = tc.count_words(file_input)
    assert result == expected_words

@pytest.mark.parametrize("file_input,expected_lines", [
    (get_input(), 10),
    ("each\nslash\nis\na\nline",5)
])
def test_lines(file_input, expected_lines):
    result = tc.count_lines(file_input)
    assert result == expected_lines