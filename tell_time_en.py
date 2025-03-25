'''
TellTime class, convert time digits to words

12:00 12 o'clock, twelve o'clock.
11:15 quarter past 11, quarter past eleven
10:30 half past 10, half past ten
9:45 quarter to 10, quarter to ten
8:20 20 past 8, twenty past eight
7:40 20 to 8, twenty to eight
'''

import speech
import time

class TellTime():
    
    
    def __init__(self, say_minutes):
        self.units = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
        self.tens = ('', 'ten', 'twenty', 'thirty', 'forty', 'fifty')
        self.say_minutes = say_minutes
        
    def tell_digits(self, hours, minutes):
        minute_units = minutes % 10
        minute_tens = int(minutes / 10)
        match minutes:
            case 0:
                s = f"{hours} o'clock"
            case n if n in range(1, 15):
                s = f'{minutes} past {hours}'
            case 15:
                s = f'Quarter past {hours}'
            case n if n in range(16, 30):
                s = f'{minutes} past {hours}'
            case 30:
                s = f'Half past {hours}'
            case n if n in range(31, 45):
                s = f'{60 -minutes } to {hours + 1 if (hours < 12) else (hours - 11)}'
            case 45:
                s = f'Quarter to {hours + 1 if (hours < 12) else (hours - 11)}'
            case n if n in range(46, 60):
                s = f'{60 - minutes} to {hours + 1 if (hours < 12) else (hours - 11)}'
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
            tell += ' minute '  
        if (m > 1 and self.say_minutes):
            tell += ' minutes '
            
        return tell   
            
    def tell(self, hours, minutes):
        match minutes:
            case 0:
                s = f"{self.units[hours]} o'clock"
            case n if n in range(1, 15):
                s = f'{self.minutes_tell(minutes)} past {self.units[hours]}'
            case 15:
                s = f'Quarter past {self.units[hours]}'
            case n if n in range(16, 30):
                s = f'{self.minutes_tell(minutes)} past {self.units[hours]}'
            case 30:
                s = f'Half past {self.units[hours]}'
            case n if n in range(31, 45):
                s = f'{self.minutes_tell(60 -minutes)} to {self.units[hours + 1] if (hours < 12) else self.units[(hours - 11)]}'
            case 45:
                s = f'Quarter to {self.units[hours + 1] if (hours < 12) else self.units[(hours - 11)]}'
            case n if n in range(46, 60):
                s = f'{self.minutes_tell(60 - minutes)} to {self.units[hours + 1] if (hours < 12) else self.units[(hours - 11)]}'
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
    speech.say(tell_time.tell(8, n), 'en_US')
    finish_speaking()
    
for n in range(24):
    print(f'{n}:45  {tell_time.tell(n, 45)} / {tell_time.tell_digits(n, 45)}')
    


