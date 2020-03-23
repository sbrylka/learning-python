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

print("Mogę zaprosić jedynie dwie osoby.")

odwolany_gosc = lista_gosci.pop()
print("Przykro mi, " + odwolany_gosc.title() + ", niestety liczba miejsc przy stole zmusiła mnie do ograniczenia liczby gości, zobaczymy się innym razem.")
odwolany_gosc = lista_gosci.pop()
print("Przykro mi, " + odwolany_gosc.title() + ", niestety liczba miejsc przy stole zmusiła mnie do ograniczenia liczby gości, zobaczymy się innym razem.")
print(lista_gosci[0].title() + komunikat)
print(lista_gosci[1].title() + komunikat)

del lista_gosci[1]
del lista_gosci[0]
print(lista_gosci)
