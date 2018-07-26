"""
Doc
"""


def plus_one(num):
    """
    Doc
    """
    return num + 1


# Make a warning at static analysis phase
def test_plus_one():
    '''
    DOc
    '''
    # Make an error at unnitest phase
    assert plus_one(3) == 3
