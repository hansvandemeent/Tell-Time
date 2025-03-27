'''
12:00 12 o'clock, twelve o'clock.
11:15 quarter past 11, quarter past eleven
10:30 half past 10, half past ten
9:45 quarter to 10, quarter to ten
8:20 20 past 8, twenty past eight
7:40 20 to 8, twenty to eight
class TellTime():
'''
    
class TellTime():
    
    def __init__(self):
        self.units = \
        (('', 'één', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen', 'tien', \
        'elf', 'twaalf', 'dertien', 'veertien', 'vijftien', 'zestien', 'zeventien', 'achttien', 'negentien', 'twintig'),
        ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', \
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'), \
        ('', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'zechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebsehn', 'achtzehn', 'neunzehn', 'zwanstig'))
        
        self.tens = (('', 'tien', 'twintig', 'derig', 'veertig', 'vijftig'), \
                     ('', 'ten', 'twenty-', 'thirty-', 'fourty-', 'fifty-'), \
                     ('', 'zehn', 'zwanstig', 'dreizig', 'vierzig', 'fünfzig'))
        
        
        self.strings = ((' ', 'minuut', 'minuten', 'uur', 'uren', 'voor', 'over', 'kwart', 'half'),  \
                        (' ', 'minute', 'minutes', "o'clock", 'hours', 'to', 'past', 'quarter', 'half'), \
                        (' ', 'minute', 'minuten', 'Uhr', 'Uhren', 'vor', 'nach', 'viertel', 'halb'))
     
    def minutes_tell(self, m, language):
        minute_units = m % 10
        minute_tens = int(m / 10)
        if (m < 21):
            minutes = self.units[language][m]
        else:
            minutes= self.tens[language][minute_tens] + self.units[language][minute_units]
            
        return minutes
        
                
    def translate(self, hours, minutes, cmd, language):
        s = ''
        for c in cmd:
            match c:
                case 'h': s+= self.units[language][hours]
                case 'm': s+= self.units[language][minutes]
                case 'n': s+= self.minutes_tell(30 - minutes, language)
                case 'o': s+= self.minutes_tell(60 - minutes, language)
                case 'p': s+= self.minutes_tell(minutes - 30, language)
                case 'r': s+= self.units[language][hours + 1]
                case 'M': s+= self.strings[language][1] # minute
                case 'N': s+= self.strings[language][2] # minutes
                case 'H': s+= self.strings[language][3] # o'clock'
                case 'I': s+= self.strings[language][4] # hours
                case 'T': s+= self.strings[language][5] # to
                case 'O': s+= self.strings[language][6] # past
                case 'Q': s+= self.strings[language][7] # quarter
                case 'S': s+= self.strings[language][8] # half
                case ' ': s+= ' '
                case 'E': s+= 'Error'
        return s

    def tell(self, hours, minutes, language):
        match minutes:
            case 0: s = 'h H'
            case n if n in range(1, 15): s = 'm O h'
            case 15: s = 'Q O h'
            case n if n in range(16, 30): s = 'n T S r' if language == 0 else 'h m'
            case 30: s = 'S r' if language == 0 else 'S O h'
            case n if n in range(31, 45): s = 'p O S r' if language == 0 else 'o T r'
            case 45: s = 'Q T r'
            case n if n in range(46, 60): s = 'o T r'
            case _: s = 'Error'
        return  self.translate(hours, minutes, s, language)

telltime = TellTime()   

print('8:00 ' + telltime.tell(8, 0, 0) + '  ' + telltime.tell(8, 0, 1) + '  ' + telltime.tell(8, 0, 2))
print('8:10 ' + telltime.tell(8, 10, 0) + '  ' + telltime.tell(8, 10, 1))
print('8:15 ' + telltime.tell(8, 15, 0) + '  ' + telltime.tell(8, 15, 1))
print('8:20 ' + telltime.tell(8, 20, 0) + '  ' + telltime.tell(8, 20, 1))
print('8:30 ' + telltime.tell(8, 30, 0) + '  ' + telltime.tell(8, 30, 1))
print('8:35 ' + telltime.tell(8, 35, 0) + '  ' + telltime.tell(8, 35, 1))
print('8:45 ' + telltime.tell(8, 45, 0) + '  ' + telltime.tell(8, 45, 1))
print('8:55 ' + telltime.tell(8, 55, 0) + '  ' + telltime.tell(8, 55, 1))
