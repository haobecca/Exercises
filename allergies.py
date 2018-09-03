class Allergies(object):
   
    def __init__(self, score):
        Allergies._score = score
        Allergies._list = []
        items = [
            'cats', 'pollen', 'chocolate', 'tomatoes',
            'strawberries', 'shellfish', 'peanuts','eggs'
            ]
        scores = [128, 64, 32, 16, 8, 4, 2, 1]
        allergy_dict = dict(zip(items, scores))
        if self._score > 256:
            self._score -= 256

        for x in items:
                if (self._score - allergy_dict[x]) >= 0:
                    self._list.append(x)
                    self._score -= allergy_dict[x]

    def is_allergic_to(self, item):
        return item in self._list

    @property
    def lst(self):
        return self._list[::-1]
                