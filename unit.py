class Feet:
    def __init__(self, feet : float = 0.0):
        self.feet = feet

    def _comparable(self):
        return int(f'{round((self.feet - int(self.feet)) / 0.25) * 0.25 * 100:.0f}')
    
    def _fraction(self):
        match f'{round((self.feet - int(self.feet)) / 0.25) * 0.25:.2f}':
            case '0.00':
                return ''
            case '0.25':
                return ' 1/4'
            case '0.50':
                return ' 1/2'
            case '0.75':
                return ' 3/4'
            case _:
                return 'ADD 1'
    
    def __str__(self):
        fraction = self._fraction()
        if fraction == 'ADD 1':
            return f'{int(self.feet) + 1} {{unit.feet.shorthand}}'
        else:
            return f'{int(self.feet)}{fraction} {{unit.feet.shorthand}}'
    
    def __eq__(self, value):
        if not isinstance(value, Feet):
            return False
        
        self_feet = self._comparable()
        cmpr_feet = value._comparable()

        return self_feet == cmpr_feet
    
    def __lt__(self, value):
        if not isinstance(value, Feet):
            return False
        
        self_feet = self._comparable()
        cmpr_feet = value._comparable()

        return self_feet < cmpr_feet
    
    def __gt__(self, value):
        if not isinstance(value, Feet):
            return False
        
        self_feet = self._comparable()
        cmpr_feet = value._comparable()

        return self_feet > cmpr_feet
    
    def __le__(self, value):
        return self.__lt__(value) or self.__eq__(value)
    
    def __ge__(self, value):
        return self.__gt__(value) or self.__eq__(value)