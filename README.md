### ShiftCipherAndTranspositionCipher 🖥️
In this repository, we can see the decryption and encryption based on Shift Cipher and Transposition Cipher.

The Shift Cipher is a type of cipher where each letter in the text is shifted by a specific number and substituted by another letter, with all letters sharing the same displacement. For example, if the letter "a" in the original text is shifted by 3, it becomes "d" in the encrypted text. Similarly, if we have "c" in the original text, it will be shifted to "f," and so on.

To decrypt the Shift Cipher, we can use frequency analysis, which has a complexity of O(n+klogk). Frequency analysis is more effective when the text contains over 1000 words, as this improves accuracy. Alternatively, we can use brute force, which has a complexity of O(n⋅m). However, brute force tends to be slower for large texts.


Transposition Cipher is a method of encryption where the positions of the characters in the message are rearranged according to a key. First, the message is written into a matrix with a set number of columns, determined by the key. After filling the matrix row by row, the encrypted message is created by reading the columns in the order specified by the key. To decrypt the message, the receiver needs the same key to reverse the process: reconstruct the matrix by reading the columns in the original order, and then read the message row by row.

When you know the encryption method is a transposition cipher and you have the key, the decryption process typically runs with a time complexity of O(n⋅m), where n is the number of rows and m is the number of columns in the transposition matrix. This is because you need to fill and read from a matrix based on the key's column order, and each element of the matrix must be accessed once.

However, when trying to decrypt without the key (like in the attempt_decrypt function), you need to test all possible permutations of the column orders, which adds significant complexity. The time complexity of this brute force approach is O(m!⋅n⋅m), where m is the number of columns and n is the number of rows. The m! term comes from the fact that there are m! possible permutations of m columns to check. Since factorial growth is very fast, this makes the decryption process exponentially slower as the number of columns increases.
