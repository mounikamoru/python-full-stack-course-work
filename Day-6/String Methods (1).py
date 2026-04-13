#1.case conversion methods

"mounika".upper()
'MOUNIKA'
'MOUNIKA'.lower()
'mounika'
'mounika'.capitalize()
'Mounika'
'Mounika sree'.title()
'Mounika Sree'
'MounikaSree'.swapcase()
'mOUNIKAsREE'
'mounika'.casefold()
'mounika'
'MOUNIKA'.casefold()
'mounika'
'Mounika'.casefold()
'mounika'

#2.Alignment & Formatting

'mounika'.center(7,"*")
'mounika'
'mounika'.center(12,"*")
'**mounika***'
'mounika'.ljust(9,'&')
'mounika&&'
'mounika'.rjust(9,'&')
'&&mounika'
'mounika'.zfill(8)
'0mounika'

#3.search & find methods

'mounika'.find("1")
-1
'mounika'.find("m")
0
'mounika'.rfind("n")
3
'mounika'.rfind("u")
2

'mounika'.index("m")
0
'mounika'.index('n')
# ValueError: substring not found
'mounika'.rindex("a")
6

'mounika'.count("a")
1

#4.string testing methods
'mounika'.startswith('mou')
True
'mounika'.endswith('ika')
True
'mounika'.isalpha()
True
'mounika1'.isalnum()
True
"mounika".islower()
True
'MOUNIKA'.isupper()
True
" ".isspace()
True
"Mounika Sree".istitle()
True
"var1".isidentifier()
True
# 10.isliteral() -> invalid syntax

#5.Replace & modify methods:

"mounikasree".replace("sree","mounika")
'mounikamounika'
'mounika'.translate(str.maketrans("m","x"))
'xounika'
'mounika'.maketrans("moun","sree")
{109: 115, 111: 114, 117: 101, 110: 101}

#6.splitting & joining methods
"m,o,u,n,i,k,a".split(",")
['m', 'o', 'u', 'n', 'i', 'k', 'a']
"m,o,u,n,i,k,a".rsplit(",", 1)
['m,o,u,n,i,k', 'a']
"Mounika\nSree".splitlines()
['Mounika', 'Sree']
" ".join(["Hello", "world"])
'Hello world'
"mounika-sree".partition("-")
('mounika', '-', 'sree')
"mounika-sree".rpartition("-")
('mounika', '-', 'sree')

#7.whitespace & trimming methods
"  mounika  ".strip()
'mounika'
"--mounika".lstrip()
'--mounika'
"--mounika".lstrip("-")
'mounika'
"mounika--".rstrip("-")
'mounika'

#8.encoding & decoding:

"mounika".encode("utf-8")
b'mounika'
b"mounika".decode("utf-8")
'mounika'