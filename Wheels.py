#Create the pre-defined song values and empty variables...NOT SURE IF LISTS OR TUPLES ARE BETTER...Proper names not used so each starting letter would be unique

numbers = (1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 )

letters = ['a ','b ','c ','d ','e ','f ','g ','h ','i ','j ','k ','l ','m ','n ','o ','p ','q ','r ']

roman = ['I ', 'II ', 'III ', 'IV ', 'V ', 'VI ', 'VII ', 'VIII ', 'IX ', 'X ', 'XI ', 'XII ', 'XIII ', 'XIV ', 'XV ', 'XVI ', 'XVII ', 'XVIII']

military = ['alpha ', 'bravo ', 'charlie ', 'delta ', 'echo ', 'foxtrot ', 'golf ', 'hotel ', 'india ', 'juliet ', 'kilo ', 'lima ', 'mike ', 'november ', 'oscar ', 'papa ', 'quebec ', 'romeo ']

german = ['eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn']

pi = ['3 ','point ','1 ','4 ','1 ','5 ','9 ','2 ','6 ','5 ','3 ','5 ','8 ','9 ','7 ','9 ','3 ','2 ']

##Build morse code sequences
t = 'dot'
s = 'dash'
m1 = t, s, s, s, s
m2 = t, t, s, s, s
m3 = t, t, t, s, s
m4 = t, t, t, t, s
m5 = t, t, t, t, t
m6 = s, t, t, t, t
m7 = s, s, t, t, t
m8 = s, s, s, t, t
m9 = s, s, s, s, t
m0 = s, s, s, s, s
code = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m1 + m0, m1 + m1, m1 + m2, m1 + m3, m1 + m4, m1 + m5, m1 + m6, m1 + m7, m1 + m8]

##Other ideas: piglatin, japanese, spanish, prime, tau, e, ...

sing = 'y'

##Now to the good stuff......NEED TO ADD INVALID ENTRY CATCHES

print("Hello, let's sing a song that everybody loves!\n")

while sing == 'y':       

    variation = input ("Please input what variation you wish to perform be entering 'numbers', 'letters', 'roman', 'military', 'pi', 'german', 'code', or 'user' to make your own song: \n").lower().strip()

##Seeming silly switching of strings to list types
    if variation == "numbers":
        variation = numbers
    elif variation == "letters":
        variation = letters
    elif variation == "roman":
        variation = roman
    elif variation == "military":
        variation = military
    elif variation == "pi":
        variation = pi
    elif variation == "german":
        variation = german
    elif variation == "code":
        variation = code

#Create a function to build a list of user defined inputs (while len < 18)

#    user = []
#    if variation == "user":
#       user_def ()

#User input to select the song pattern...BROKEN
##    pattern = input ("\nNow please tell me what pattern to use by entering 'forward', 'backward', 'even', or 'odd':\n")

    print ("\nHere we go: \n\n")

#Now to create a function to print the desired then the variation and pattern to see if it works.
#Instead of printing, what is really needed is to set the value of a new object so it can then be displayed in the final assembled song.
#Assembled order should be modified var (forward, backward, skipping first or second)

##THIS IS BROKEN....Use pattern.startswith()?...Also, might be better to seperate forward/backward and even/odd choices.
    if pattern == 'forward' or 'f':
        varpat = variation
    elif pattern == 'backward' or 'b':
        varpat = variation[::-1]
    elif pattern == 'odd' or 'o':
        varpat = variation[::2]
    elif pattern == 'even' or 'e':
        varpat = variation[1::]

#Asemble the song

    song1 = "Oh, there are "
    song2 = " wheels on a big rig truck!\n\n"
    print (song1, varpat, song2)

    sing = input('Would you like to sing it again? (y/n) ').lower()
else:
   print ("\nOK, Goodbye!")

#Create function and pass it the variable for it to fill and then send back to the script
#def user_def (user)
##           while len(user) < 18:
###               user.append [input "Enter a word: "]
            
           
