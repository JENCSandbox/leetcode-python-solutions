class Solution():

    def stringToDictionary(self, text, dictionary):
        for character in text:
            self.addToStringDictionary(character, dictionary)

    def addToStringDictionary(self, character, dictionary):
        if (dictionary.get(character) != None):
            dictionary[character] = dictionary.get(character) + 1
        else:
            dictionary[character] = 1

    def getFromStringDictionary(self, character, dictionary):
        if (dictionary.get(character) == None):
            return 0
        return dictionary.get(character)

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magaginzeDictionary = {}
        self.stringToDictionary(magazine, magaginzeDictionary)

        ransomeDictionary = {}
        self.stringToDictionary(ransomNote, ransomeDictionary)

        result = True
        for character in ransomeDictionary:
            countInRansomNote = self.getFromStringDictionary(character, ransomeDictionary)
            countInMagazine = self.getFromStringDictionary(character, magaginzeDictionary)

            if (countInMagazine < countInRansomNote):
                result = False
                break

        return result