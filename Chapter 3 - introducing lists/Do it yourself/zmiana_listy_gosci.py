lista_gosci = ['yarek', 'kinga', 'grzesiek', 'asia']
komunikat = ", zapraszam Cię na obiad!"
print(lista_gosci[0].title() + komunikat)
print(lista_gosci[1].title() + komunikat)
print(lista_gosci[-1].title() + komunikat)
print(lista_gosci[-2].title() + komunikat)

print(lista_gosci[1].title() + " nie może uczestniczyć w wydarzeniu!")

lista_gosci[1] = 'ania'
print(lista_gosci[0].title() + komunikat)
print(lista_gosci[1].title() + komunikat)
print(lista_gosci[-1].title() + komunikat)
print(lista_gosci[-2].title() + komunikat)
