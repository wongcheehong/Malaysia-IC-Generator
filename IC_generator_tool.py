from calendar import monthrange
from datetime import date
import argparse

state_birth = {
    "JHR": ['01', '21', '22', '23', '24'],
    "KDH": ['02', '25', '26', '27'],
    "KTN": ['03', '28', '29'],
    "MLK": ['04', '30'],
    "NSN": ['05', '31', '59'],
    "PHG": ['06', '32', '33'],
    "PNG": ['07', '34', '35'],
    "PRK": ['08', '36', '37', '38', '39'],
    "PLS": ['09', '40'],
    "SGR": ['10', '41', '42', '43', '44'],
    "TRG": ['11', '45', '46'],
    "SBH": ['12', '47', '48', '49'],
    "SWK": ['13', '50', '51', '52', '53'],
    "KUL": ['14', '54', '55', '56', '57'],
    "LBN": ['15', '58'],
    "PJY": ['16']
}

class YearRange(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values < 1900 or values > 2100:
            print("Year Error: Please enter year between 1900 to 2100")
            exit(1)
        setattr(namespace, self.dest, values)

class PlaceBirth(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        pb_list = values.split(',')
        try:
            for item in pb_list: # Make sure all is integer
                int(item)
                if len(item) != 2:
                    print("Place Birth Error: Make sure you enter only 2-digits numbers")
                    exit(1)
        except ValueError:
            temp_list = []
            for state in pb_list:
                if state.upper() in state_birth:
                    temp_list += state_birth[state.upper()]
                else:
                    print("Place Birth Error: Please enter state(s) abbreviation correctly")
                    exit(1)
            pb_list = temp_list
        setattr(namespace, self.dest, pb_list)

class NinthDigit(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        values = values.split(',')
        for n in values:
            if len(n) != 1:
                print("Ninth Digit Error: Enter only number from 0 to 9")
                exit(1)
            try:
                int(n)
            except:
                print("Ninth Digit Error: String not allowed. Enter 1-digit number only")
                exit(1)
        setattr(namespace, self.dest, values)

ap = argparse.ArgumentParser()

ap.add_argument("-s", "--startyear", required=True, help="Start Year (eg. 1980)", type=int, action=YearRange)
ap.add_argument("-e", "--endyear", required=True, help="End Year (eg. 2001)", type=int, action=YearRange)
ap.add_argument("-pb", "--placebirth", required=False, help="Place of birth. Use either state(s) abbreviation or 2-digit number(s)",  action=PlaceBirth)
ap.add_argument("-n", "--ninthdigit", required=False, metavar="[0-9]", help="For overwriting the default ninth digit (5, 6, 7, 0)", action=NinthDigit)
ap.add_argument("-g", "--gender", required=False, choices=['F', 'M'], help="F for female, M for male (Usually even numbers denote femlae while odd numbers denote male). \nMissing <gender> will default generate all")
args = vars(ap.parse_args())

if args['endyear'] < args['startyear']:
    print("Error: End year should be larger than or equal to start year")
    exit(1)

if args['placebirth'] is None:
    args['placebirth'] = [f"{pb:02d}" for pb in range(1,60) if pb not in range(17, 21)]

if args['ninthdigit'] is None:
    args['ninthdigit'] = ['5', '6', '7', '0']

if args['gender'] is None:
    last_digit = [str(n) for n in range(10)]
elif args['gender'] == 'F':
    last_digit = [str(num) for num in range(10) if num%2 == 0]
else:
    last_digit = [str(num) for num in range(10) if num%2 == 1]

print('''
 ___ ____    ____                           _
|_ _/ ___|  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
 | | |     | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | | |___  | |_| |  __/ | | |  __/ | | (_| | || (_) | |
|___\____|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|
''')
print("IC Format: YYMMDD-PB-N##G")
print(f"Start Year: {args['startyear']}")
print(f"End Year: {args['endyear']}")
print("Place Birth (PB): " + ', '.join(args['placebirth']))
print("Ninth-Digit (N): " + ', '.join(args['ninthdigit']))
print("Gender/Last Digit (G): " + ', '.join(last_digit))
days = (date(args['endyear'], 12, 31) - date(args['startyear'], 1, 1)).days + 1
line_count = days * len(args['placebirth']) * len(args['ninthdigit']) * 100 * len(last_digit)
print(f"\nGenerating {line_count} lines of IC numbers (CTRL+C to stop if it take too long to generate)")

with open(f"IC-wordlist-{args['startyear']}-{args['endyear']}", "w", buffering=-1) as f:
    for year in range(int(args['startyear']), int(args['endyear'])+1):
        YY=""
        YY+=str(year)[-2:]
        for month in range(1, 13):
            YYMM = YY + f"{month:02d}"
            for day in range(1, monthrange(year, month)[1]+1): # Day 1 until last day of the month
                YYMMDD = YYMM + f"{day:02d}"
                for pb in args['placebirth']:
                    YYMMDDPB = YYMMDD + pb
                    for ninth_digit in args['ninthdigit']:
                        YYMMDDPBN = YYMMDDPB + ninth_digit
                        for xx in range(0, 100):
                            YYMMDDPBNXX = YYMMDDPBN + f"{xx:02d}"
                            for g in last_digit:
                                ic_number = YYMMDDPBNXX + g
                                f.write(ic_number+'\n')

print("Done generating dictionary. Quiting")
