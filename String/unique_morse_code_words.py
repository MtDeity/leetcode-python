class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabets = (
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        )
        morse_sets = set()
        for word in words:
            morse = ""
            for letter in word:
                morse += alphabets[ord(letter) - ord("a")]
            morse_sets.add(morse)
        return len(morse_sets)
