import string
   
   
class TellTime():
    """
        TellTime class converts time digits (10:25) to text (twenty-five after ten)
        It has now support for English, Dutch and German
        In Dutch and German there are some differences in conversion, like 10:35 is "vijf over half 11"
        In English make a diffrence between midnight and noon
    """
    
    def __init__(self):
        self.units = (
                     ('noon', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                         'seventeen', 'eighteen', 'nineteen', 'twenty',
                         'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'midnight'),
                     ('twaalf', 'één', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht',
                         'negen', 'tien', 'elf', 'twaalf', 'dertien', 'veertien',
                         'vijftien', 'zestien', 'zeventien', 'achttien', 'negentien',
                         'twintig', 'eenentwintig', 'tweeentwintig', 'drieentwintig', 'vierentwintig', 'twaalf'),
                     ('zwölf', 'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht',
                         'neun', 'zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn',
                         'sechzehn', 'siebsehn', 'achtzehn', 'neunzehn', 'zwanzig',
                         'einundzwanzig', 'zweiundzwanzig', 'dreiundzwanzig', 'vierundzwanzieg', 'zwölf')
                     )
        
        self.tens = (
                    ('', 'ten', 'twenty-', 'thirty-', 'fourty-', 'fifty-'),
                    ('', 'tien', 'twintig', 'derig', 'veertig', 'vijftig'),
                    ('', 'zehn', 'zwanzig', 'dreiẞig', 'vierzig', 'fünfzig')
                    )
        
        self.strings = (
                       (' ', 'minute ', 'minutes ', " o'clock", 'hours', 'to ', 'past ', 'quarter ', 'half '),
                       (' ', 'minuut ', 'minuten ', ' uur', 'uren', 'voor ', 'over ', 'kwart ', 'half '),
                       (' ', 'minute ', 'minuten ', ' Uhr ', 'Uhren ', 'vor ', 'nach ', 'viertel ', 'halb '))
                        
    def set_language(self, lang):
        match lang:
            case 'en_US': self.language = 0
            case 'nl_NL': self.language = 1
            case 'de_DE': self.language = 2
            case '_': self.language = 0
            
    def minutes_tell(self, m):
        """
            Numbers up to 20 sometimes spelled and pronounced differently:
            thirteen and not threeteen
            veertien and not viertien
            siebsehn and not siebensehn
            Thats why they are included in the tuple
        """
        minute_units = m % 10
        minute_tens = int(m / 10)
        if (m < 25):
            minutes = self.units[self.language][m] + ' '
        else:
            minutes = self.tens[self.language][minute_tens] + self.units[self.language][minute_units] + ' '
        return minutes
        
    def translate(self, hours, minutes, commands):
        command_list = commands.split(' ')
        s = ''
        for command in command_list:
            match command:
                case 'hour': 
                    s += self.units[self.language][25] if hours == 0 \
                    else self.units[self.language][hours % 12]
                case 'minutes_after_hour': s += self.minutes_tell(minutes)
                case 'minutes_to_half': s += self.minutes_tell(30 - minutes)
                case 'minutes_to_hour': s += self.minutes_tell(60 - minutes)
                case 'minutes_after_half': s += self.minutes_tell(minutes - 30)
                case 'next_hour': s += self.units[self.language][hours + 1]
                case 'MINUTE': s += self.strings[self.language][1]  # minute
                case 'MINUTES': s += self.strings[self.language][2]  # minutes
                case 'HOUR': s += self.strings[self.language][3]  # o'clock'
                case 'HOURS': s += self.strings[self.language][4]  # hours
                case 'TO': s += self.strings[self.language][5]  # to
                case 'PAST': s += self.strings[self.language][6]  # past
                case 'QUARTER': s += self.strings[self.language][7]  # quarter
                case 'HALF': s += self.strings[self.language][8]  # half
                case '_':  s += ' '
                case 'E':  s += 'Error'
        return s

    ''' lower case: value, upper case: text '''
    def tell(self, hours, minutes):
        """
           There are up to 8 distinct ways to pronounce minutes time,
               0, 1-14, 15, 16-29, 30, 31-44, 45, 46-59
        """
        match minutes:
            case 0: s = 'hour HOUR'
            case n if n in range(1, 15): s = 'minutes_after_hour PAST hour'
            case 15: s = 'QUARTER PAST hour'
            case n if n in range(16, 30): s = 'minutes_after_hour PAST hour' if self.language == 0 \
                else 'minutes_to_half TO HALF next_hour'
            case 30: s = 'HALF PAST hour' if self.language == 0 else 'HALF next_hour'
            case n if n in range(31, 45): s = 'minutes_after_hour PAST hour' if self.language == 0 \
                else 'minutes_after_half PAST HALF next_hour'
            case 45: s = 'QUARTER TO next_hour'
            case n if n in range(46, 60): s = 'minutes_to_hour TO next_hour'
            case _: s = 'Error'
            
         
        return self.translate(hours, minutes, s)


telltime = TellTime()
    
    telltime.set_language('nl_NL')
    for n in range(0, 60, 1):
        print(f'8:{n}  {telltime.tell(8, n)}')
print('-' * 30)

for n in range(0, 24, 1):
    print(f'{n}:15  {telltime.tell(n, 15)}')
print('-' * 30)  
   
telltime.set_language('en_US')
for n in range(0, 60, 1):
    print(f'8:{n}  {telltime.tell(8, n)}')
print('-' * 30) 
   
for n in range(0, 24, 1):
    print(f'{n}:15 {telltime.tell(n, 15)}')
print('-' * 30)  

telltime.set_language('de_DE')
for n in range(0, 60, 1):
    print(f'8:{n}  {telltime.tell(8, n)}')
print('-' * 30) 

for n in range(0, 24, 1):
    print(f'{n}:8  {telltime.tell(n, 15)}')

