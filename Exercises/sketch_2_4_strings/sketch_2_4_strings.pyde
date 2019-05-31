size(500, 500)
background('#004477')

hello = 'hello world'
print(hello)

whatsup = "what\'s up!"
question = 'is your name really "world"?'
print(whatsup)
print(question)

all = hello + '. ' + whatsup + ' ' + question
print(all)

print( len(all) )  # displays total number of characters (52)
print( all[0] )    # displays the first character (h)
print( all[1] )    # displays character at index 1 (e)
print( all[4] )    # displays character at index 4 (o)
print( all[1:4] )  # displays: ell
print( all[:-4] )  # ...our name really "wor

print( all.upper() )

print(all[:5].title() + '. ' + all[13:17].title() + ' ' + all[24:36] + "?")
