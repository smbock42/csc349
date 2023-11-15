import sys
def main():
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    ed = edit_distance(word1, word2)
    print(ed)
    return ed

def edit_distance(word1, word2):
    # Create a matrix of size len(word1) + 1 by len(word2) + 1
    matrix = [[0 for x in range(len(word1) + 1)] for y in range(len(word2) + 1)]
    # Fill in the first row
    for i in range(len(word1) + 1):
        matrix[0][i] = i
    # Fill in the first column
    for j in range(len(word2) + 1):
        matrix[j][0] = j
    # Fill in the rest of the matrix
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            # If the characters are the same, the cost is 0
            if word1[i - 1] == word2[j - 1]:
                matrix[j][i] = matrix[j - 1][i - 1]
            # If the characters are different, the cost is 1
            else:
                matrix[j][i] = min(matrix[j - 1][i - 1], matrix[j - 1][i], matrix[j][i - 1]) + 1
    # Return the bottom right corner
    return matrix[len(word2)][len(word1)]




if __name__ == '__main__':
    main()