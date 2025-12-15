kpop = ['Soobin', 'Hwasa', 'The8', 'Nayeon', 'Suho', 'Jimin', 'Lisa']
# Index      0      1         2        3        4      5          6  
print(kpop[-1])

# {Keys : Values, Keys : Values}    
kpop_dictionary = {'Txt':'Soobin', 'Mamamoo':'Hwasa', 'Svt':'The8', 'Twice':'Nayeon', 'Exo':'Suho', 'Bts':'Jimin', 'Bp':'Lisa'}
print(kpop_dictionary['seeded'])

# Adding item
kpop_dictionary['2ne1'] = 'Sandara'
print(kpop_dictionary)

# Removing item
kpop_dictionary.pop('Txt')
print(kpop_dictionary)