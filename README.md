# Malaysia-IC-Generator
This is a tool to generate list of Malaysia IC with multiple flexible arguments to limit the scope. Useful for dictionary attack.

## Install
```
git clone https://github.com/wongcheehong/Malaysia-IC-Generator.git
cd Malaysia-IC-Generator
python IC_generator_tool.py --help
```

## Usage 
### Basic Usage:
```
python IC_generator_tool.py -s STARTYEAR -e ENDYEAR [-pb] <PLACEBIRTH> [-n] <0-9> [-g] <F,M>
```
### Help
```
python IC_generator_tool.py -h
```
![image](https://user-images.githubusercontent.com/11075969/121502714-01e66d80-ca13-11eb-9564-6612fa3975d6.png)
### Example 1: Generate IC from 1990 to 2001:
```
python IC_generator_tool.py -s 1990 -e 2001
```
### Example 2: Generate IC from 1990 to 2001 in Johor:
```
python IC_generator_tool.py -s 1990 -e 2001 -pb JHR
```
### Example 3: Generate IC from 1990 to 2001 with custom 2-digit numbers:
```
python IC_generator_tool.py -s 1990 -e 2001 -pb 01,02,...
```
### Example 4: Generate IC from 1990 to 2001 with male gender
```
python IC_generator_tool.py -s 1990 -e 2001 -g M
```
### Example 5: Generate IC in 2003 who born in Kuala Lumpur or Selangor and is Male. -n will overwrite the default digits(5,6,7,0): 
```
python IC_generator_tool.py -s 2003 -e 2003 -pb KUL,SGR -n 0 -g M
```
![image](https://user-images.githubusercontent.com/11075969/121502432-c21f8600-ca12-11eb-936d-7550ad879bc4.png)

## For your information
### Malaysia IC Format
**YYMMDDPBN##G**
### Birthdate (YYMMDD)
The first six digits YYMMDD signify the person's date of birth in the ISO 8601:2000 format. For examople, a person born on 24 June 1980 would be 800624.

### Place of birth (PB)
| State | State Abbrevation | PB code |
| :---: | :---: | :---: |
| Johor | JHR | 01, 21, 22, 23, 24 |
| Kedah | KDH | 02, 25, 26, 27 |
| Kelantan | KTN | 03, 28, 29 |
| Malacca | MLK | 04, 30 |
| Negeri Sembilan | NSN | 05, 31, 59 |
| Pahang | PHG | 06, 32, 33 |
| Penang | PNG | 07, 34, 35 |
| Perak | PRK | 08, 36, 37, 38, 39 |
| Perlis | PLS | 09, 40 |
| Selangor | SGR | 10, 41, 42, 43, 44 |
| Terengganu | TRG | 11, 45, 46 |
| Sabah | SBH | 12, 47, 48, 49 |
| Sarawak | SWK | 13, 50, 51, 52, 53 |
| Federal Territory of Kuala Lumpur | KUL | 14, 54, 55, 56, 57 |
| Federal Territory of Labuan | LBN | 15, 58 |
| Federal Territory of Putrajaya | PJY | 16 |

If `-pb` is not specify, it will generate all possible outcome. Proceed with caution as this will generate large numbers of lines.
**Note:** `-pb` accept list of state abbrevations and list of PB codes (comma seperated). Mixed of state abbrevation and PB code is not allowed.

### The Ninth Digit (N)
Usually, a person born prior and in the year 1999 will have the number started with 5## or 6## or 7## while a person born after and in the year 2000 will have the number started with 0##. This tool default will generate all possible digit (5,6,7,0) regardless of the year. Use `-n` arguement to overwrite this behaviour.
**Note:** `-n` accept list of 1-digit integeter (comma seperated).

### Gender (G)
G, the last digit of the IC represents the gender of the person.
Odd numbers (1,3,5,7,9) denote male
Even numbers (2,4,6,9,0) denote female
This tool generate all possible digit (0-9) by default. Use `-g` argument to overwrite this behaviour. 

### Source
https://en.wikipedia.org/wiki/Malaysian_identity_card
