class MorseMsg:
    """A class representing a message in Morse code."""
    
    MORSE_ENG = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }
    
    MORSE_RU = {
        '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
        '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
        '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
        '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
        '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
        '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '.-.-': 'Э',
        '..--': 'Ю', '.-..-': 'Я'
    }
    
    VOWELS_ENG = {'A', 'E', 'I', 'O', 'U', 'Y'}
    
    VOWELS_RU = {'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я'}
    
    def __init__(self, *args):
        """
        Initialize a MorseMsg instance.
        
        Args:
            *args: Variable number of strings. Can be either:
                   - Individual Morse code patterns for each letter, or
                   - A single string with space-separated Morse patterns
        """
        if len(args) == 1 and ' ' in args[0]:
            self.morse_letters = args[0].split()
        else:
            self.morse_letters = list(args)
    
    def eng_decode(self):
        """
        Decode the Morse code message into English letters.
        
        Returns:
            str: The decoded message in uppercase English letters.
        """
        result = ''
        for morse in self.morse_letters:
            if morse in self.MORSE_ENG:
                result += self.MORSE_ENG[morse]
        return result
    
    def ru_decode(self):
        """
        Decode the Morse code message into Russian Cyrillic letters.
        
        Returns:
            str: The decoded message in uppercase Russian letters.
        """
        result = ''
        for morse in self.morse_letters:
            if morse in self.MORSE_RU:
                result += self.MORSE_RU[morse]
        return result
    
    def get_vowels(self, lang):
        """
        Get the vowels from the decoded message in the specified language.
        
        Args:
            lang (str): The language code, either 'eng' or 'ru'.
            
        Returns:
            list: A list of vowels in the order they appear in the message.
        """
        if lang == 'eng':
            decoded = self.eng_decode()
            vowels = self.VOWELS_ENG
        elif lang == 'ru':
            decoded = self.ru_decode()
            vowels = self.VOWELS_RU
        else:
            return []
        
        return [char for char in decoded if char in vowels]
    
    def get_consonants(self, lang):
        """
        Get the consonants from the decoded message in the specified language.
        
        Args:
            lang (str): The language code, either 'eng' or 'ru'.
            
        Returns:
            list: A list of consonants in the order they appear in the message.
        """
        if lang == 'eng':
            decoded = self.eng_decode()
            vowels = self.VOWELS_ENG
        elif lang == 'ru':
            decoded = self.ru_decode()
            vowels = self.VOWELS_RU
        else:
            return []
        
        return [char for char in decoded if char not in vowels]
    
    def __str__(self):
        """
        Return a string representation of the Morse code message.
        
        Returns:
            str: The Morse code letters separated by spaces.
        """
        return ' '.join(self.morse_letters)