'''
TellTime class, convert time digits to words

12:00 12 uur, twaalf uur
11:15 kwart over 11, kwart over elf
10:30 half 11, half elf
9:45 kwart voor 10, kwart voor tien
8:20 tien voor half 9, tien voor half negen
7:40 tien over half 8, tien over half acht
'''

import speech
import time

class TellTime():
    
    
    def __init__(self, say_minutes):
        self.units = ('', 'een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen', 'tien', 'elf', 'twaalf', 'dertien', 'veertien', 'vijftien', 'zestien', 'zeventien', 'achttien', 'negentien', 'twintig')
        self.tens = ('', 'ten', 'twenty', 'thirty', 'forty', 'fifty')
        self.say_minutes = say_minutes
        
    def tell_digits(self, hours, minutes):
        minute_units = minutes % 10
        minute_tens = int(minutes / 10)
        match minutes:
            case 0:
                s = f"{hours} uur"
            case n if n in range(1, 15):
                s = f'{minutes} over {hours}'
            case 15:
                s = f'kwart over {hours}'
            case n if n in range(16, 30):
                s = f'{30 - minutes} voor half {hours}'
            case 30:
                s = f'half {hours}'
            case n if n in range(31, 45):
                s = f'{minutes - 30} over half {hours + 1 if (hours < 12) else (hours - 11)}'
            case 45:
                s = f'kwart voor {hours + 1 if (hours < 12) else (hours - 11)}'
            case n if n in range(46, 60):
                s = f'{60 - minutes} voor {hours + 1 if (hours < 12) else (hours - 11)}'
            case _:
                s = 'Error'
        return s

    def minutes_tell(self, m):
        minute_units = m % 10
        minute_tens = int(m / 10)
        if (m < 21):
            tell = self.units[m]
        else:
            tell = self.tens[minute_tens] + '-' + self.units[minute_units]
 
        if (m == 1 and self.say_minutes):
            tell += ' minuut '  
        if (m > 1 and self.say_minutes):
            tell += ' minuten '
            
        return tell   
            
    def tell(self, hours, minutes):
        match minutes:
            case 0:
                s = f"{self.units[hours]} uur"
            case n if n in range(1, 15):
                s = f'{self.minutes_tell(minutes)} over {self.units[hours]}'
            case 15:
                s = f'kwart over {self.units[hours]}'
            case n if n in range(16, 30):
                s = f'{self.minutes_tell(30 - minutes)} voor half {self.units[hours + 1] if (hours < 12) else self.units[(hours - 11)]}'
            case 30:
                s = f'half {self.units[hours + 1] if (hours < 12) else self.units[(hours - 11)]}'
            case n if n in range(31, 45):
                s = f'{self.minutes_tell(minutes - 30 )} over half {self.units[hours + 1] if (hours < 12) else self.units[(hours - 11)]}'
            case 45:
                s = f'kwart voor {self.units[hours + 1] if (hours < 12) else self.units[(hours - 11)]}'
            case n if n in range(46, 60):
                s = f'{self.minutes_tell(60 - minutes)} voor {self.units[hours + 1] if (hours < 12) else self.units[(hours - 11)]}'
            case _:
                s = 'Error'
        return s

''' Test TimeTell class '''                
tell_time = TellTime(True)

def finish_speaking():
    # Block until speech synthesis has finished
    while speech.is_speaking():
        time.sleep(0.1)

print(tell_time.tell(12, 0))
print(tell_time.tell(11, 15)) 
print(tell_time.tell(10, 30)) 
print(tell_time.tell(9, 45)) 
print(tell_time.tell(8, 14)) 
print(tell_time.tell(7, 40)) 

for n in range(60):
    print(f'8:{n}  {tell_time.tell(8, n)} / {tell_time.tell_digits(8, n)}') 
    #speech.say(tell_time.tell(8, n), 'nl_NL')
    #finish_speaking()
    
for n in range(24):
    print(f'{n}:45  {tell_time.tell(n, 45)} / {tell_time.tell_digits(n, 45)}')
    


