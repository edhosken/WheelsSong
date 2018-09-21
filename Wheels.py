#Create the pre-defined song values and empty variables...Correct names not used so each starting letter would be unique

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

##NEED TO ADD INVALID ENTRY CATCHES

print("Hello, let's sing a song that everybody loves!\n")
sing = 'y'
while sing == 'y':
    user = []
    variation = input ("Please input what variation you wish to perform be entering 'numbers', 'letters', 'roman', 'military', 'pi', 'german', 'code', or 'user' to make your own song: \n").lower().strip()

##Seeming silly switching of strings to list types
    if variation == "numbers" or variation == "n":
        variation = numbers
    elif variation == "letters" or variation == "l":
        variation = letters
    elif variation == "roman" or variation == "r":
        variation = roman
    elif variation == "military" or variation == "m":
        variation = military
    elif variation == "pi" or variation == "p":
        variation = pi
    elif variation == "german" or variation == "g":
        variation = german
    elif variation == "code" or variation == "c":
        variation = code
    elif variation == "user" or variation == "u":
        while len(user) < 18:
            user.append(input ("Enter a word: "))

#User input to select the song pattern
    pattern = input ("\nNow please tell me what pattern to use by entering 'forward', 'backward', 'even', or 'odd':\n")

    print ("\nHere we go: \n\n")

#Asemble the song...IMPROVE FORMAT SO OUTPUT IS EASIER TO READ

    song1 = "Oh, there are "
    song2 = " wheels on a big rig truck!"
    a = song1, variation[::], song2
    b = song1, variation[::-1], song2
    c = song1, variation[::2], song2
    d = song1, variation[1::2], song2

##Use pattern.startswith()?...Also, might be better to seperate forward/backward and even/odd choices.  
    if pattern == 'forward' or pattern == 'f':
        print (a)
    elif pattern == 'backward' or pattern == 'b':
        print (b)
    elif pattern == 'odd' or pattern == 'o':
        print (c)
    elif pattern == 'even' or pattern == 'e':
        print (d)

    sing = input('\n\nWould you like to sing it again? (y/n) ').lower()

## This is the end of the while loop
else:
   print ("\nOK, Goodbye!")


            
           
