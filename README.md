### ShiftCipherAndTranspositionCipher 🖥️
In this repository, we can see the decryption and encryption based on Shift Cipher and Transposition Cipher.

The Shift Cipher is a type of cipher where each letter in the text is shifted by a specific number and substituted by another letter, with all letters sharing the same displacement. For example, if the letter "a" in the original text is shifted by 3, it becomes "d" in the encrypted text. Similarly, if we have "c" in the original text, it will be shifted to "f," and so on.

To decrypt the Shift Cipher, we can use frequency analysis, which has a complexity of O(n+klogk). Frequency analysis is more effective when the text contains over 1000 words, as this improves accuracy. Alternatively, we can use brute force, which has a complexity of O(n⋅m). However, brute force tends to be slower for large texts.
