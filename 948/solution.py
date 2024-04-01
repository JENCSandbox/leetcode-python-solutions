class Solution(object):
    _score = 0
    _power = 0
    _tokens = []
    def face_up_token(self, token_index):
    def face_down_token(self, token_index):
    def find_next_index_of_min_card(self):
        token_index = 0
        token_value = self._tokens[0]
        for current_token_index in range(1, len(self._tokens)):
            current_token_value = self._tokens[current_token_index]
            if current_token_value < token_value:
                token_value = current_token_value
                token_index =  current_token_index
        return token_index, token_value
    def find_next_index_of_max_card(self):
        token_index = 0
        token_value = self._tokens[0]
        for current_token_index in range(1, len(self._tokens)):
            current_token_value = self._tokens[current_token_index]
            if current_token_value > token_value:
                token_value = current_token_value
                token_index = current_token_index
        return token_index, token_value
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        self._power = power
        self._tokens = tokens

        for token_index in range(0,len(self._tokens)):
            [min_token_index, min_token_value] = self.find_next_index_of_min_card()

            [max_token_index, max_token_value] = self.find_next_index_of_max_card()

            if self._power > min_token_value:

            elif self._score > 0:


