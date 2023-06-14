# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def insert_in_all_positions(char, word_list):  # ["bc", "cb"] -> [["b", "c"], ["c", "b"]]
    ext_lst = []
    output_lst = []
    for elem in word_list:
        ext_lst.append(list(elem))

    for lst in ext_lst:
        for i in range(len(lst) + 1):
            lst.insert(i, char)
            output_lst.append("".join(lst))
            lst.remove(char)

    return output_lst


def remove_dupes(perms):
    for elem in perms[:]:
        if perms.count(elem) > 1:
            perms.remove(elem)
    return perms


def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    # >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    if len(sequence) <= 1:
        return list(sequence)
    else:
        return insert_in_all_positions(sequence[0], get_permutations(sequence[1::]))


if __name__ == '__main__':
    # #EXAMPLE
    # example_input = 'abc'
    # print('Input:', example_input)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input))
    #
    # # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a
    # sequence of length n)

    example_input_1 = 'abc'
    print('Input:', example_input_1)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', sorted(get_permutations(example_input_1)))

    example_input_2 = 'cdl'
    print('Input:', example_input_2)
    print('Expected Output:', ['cdl', 'cld', 'dcl', 'dlc', 'lcd', 'ldc'])
    print('Actual Output:', sorted(get_permutations(example_input_2)))

    example_input_3 = 'nba'
    print('Input:', example_input_3)
    print('Expected Output:', ['abn', 'anb', 'ban', 'bna', 'nab', 'nba'])
    print('Actual Output:', sorted(get_permutations(example_input_3)))
