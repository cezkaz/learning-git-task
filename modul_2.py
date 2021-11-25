# for i in range(0, 5):
#     how_many_stars = i + 1
#     print("*" * how_many_stars)
#
# ==============================
# Listę w Pythonie można zadeklarować jawnie poprzez wywołanie
# my_list = list()
# # albo z wykorzystaniem nawiasów kwadratowych
# my_list = []
# # Takie to proste. W obu wypadkach stworzyliśmy zmienną. Ma ona specyficzny typ, właściwy dla typu kolekcji, którą tworzy. Zabawimy się w detektywa i zobaczmy, co kotek ma w środku:
# print(type(my_list))
#
# # ========================
# for i in range(0, 5):
#     print(i)
# Zapiszemy to teraz z użyciem listy.

# my_list = [0,1,2,3,4]
# for i in my_list:
#     print(i)

# =================
# my_list = list([0,1,2,3,4])
# for i in my_list:
#     print(i)

# =======================
# sentence = ["Zacznij", "kodować", "z", "Kodillą"]
# for word in sentence:
#     print(word)

# =============================
# sentence = ["Nazywam", "się", "Cezary", "Cezary", "Cezary"]
# for word in sentence:
#     print(word)
# =========================
# tasty_cocktail = [1, "mydło", None, "powidło", 0.1]
# print(tasty_cocktail)

# =============================
# pierwotna lista
# shopping_list = ["mielonka", "jajka", "boczek"]
# # domyślasz się już dokąd to zmierza?
# shopping_list.append("mielonka")
# print(shopping_list)
# ======================
# my_list = ["Nazwisko", "Imię", "lat", 34, "Rok urodzenia", 1980]
# my_list.append(55)
# print(my_list)
# ===============================
# shopping_list = ["mielonka", "jajka", "boczek"]
# print(f"Pierwszy element listy zakupów to {shopping_list[0]}")
# print(f"Drugi element listy zakupów to {shopping_list[1]}")
# ==========================
# shopping_list = ["kasza gryczana", "ryby", "brokuł", "ziemniaki", "pierś indyka", "sałata", "śmietana" , "jogurt grecki"]
# print(f"Pierwszy element listy to: {shopping_list[0]}")
# print(f"Piąty element listy to: {shopping_list[4]}")
# =====================================

# KROTKA

# W Pythonie występuje zbiór, który po angielsku nazywamy tuple i
# można spotkać się z polskim odpowiednikiem krotka. Jest to byt bardzo podobny
# do listy, z tą różnicą, że gdy raz się go zadeklaruje,
# nie można go już modyfikować (czyli jest niemutowalny).
# Krotka służy więc do przechowywania różnego rodzaju elementów,
# których nie będziemy zamieniać lub przestawiać.

# days = ("pon","wto","śro","czw","pią","sob","nie")
# print(type(days))

# days = tuple(["pon","wto","śro","czw","pią","sob","nie"])
# print(days)

# ==========================
# dni_tygodnia = "pon","wto","śro","czw","pią","sob","nie"
# print(type(dni_tygodnia))
# ====================

# ZBIÓR

# Kolejną kolekcją jest zbiór (ang. set). Zbiór różni się od pozostałych kolekcji tym,
# że zawiera elementy, które się nie powtarzają. Zawarte w nim elementy są unikalne.

# my_set = set([1, 2, 3])
# print(type(my_set))

# my_set = {1, 2, 3}
# print(type(my_set))

# my_set = {1, 2, 1}
# print(my_set)

# ==============

# Słownik

# słownik (ang. dictionary / dict). Jest on popularny między innymi dlatego,
# że stał się naturalnym nośnikiem danych w dzisiejszym świecie informatyki.
# Czasami określa się go także „mapą”.

# my_list = [1, 2]
# element_0 = my_list[0]
# print(element_0)

# Słownik definiujemy poprzez funkcję dict albo użycie nawiasów klamrowych.
# Porównując to z przepisem na zbiór, zwróć uwagę
# na obecność dwukropków, oddzielających klucze i wartości.

# my_dictionary = {
#     "klucz1": "wartosc1",
#     "klucz2": "wartosc2"
# }
# print(my_dictionary)


# my_dictionary = dict((("klucz1", "wartosc1"), ("klucz2", "wartosc2")))
# print(my_dictionary)

# Kluczem może być wszystko to, co jest niemutowalne,
# czyli string, liczba, a nawet krotka. Natomiast lista już nie, bo jest mutowalna
#
# Wartość może być dowolna, tutaj możesz wykorzystać obiekt, jaki Ci się żywnie podoba, nawet listę!

# shopping_dict = {
#     "warzywniak": ["buraki", "ziemniaki"],
#     "piekarnia": ["bułka", "chleb"]
# }
# print(shopping_dict)

# Indeksowanie

# shopping_dict = {
#      "warzywniak": ["buraki", "ziemniaki"],
#      "piekarnia": ["bułka", "chleb"]
# }
# print("Wchodzę do piekarni")
# print(shopping_dict["piekarnia"])

# ================


# Kolekcja	Składnia
# lista	my_list = [1,2,3]
# my_list = list([1,2,3])
#
# krotka	my_tuple = ("mon","tue","wed")
# my_tuple = tuple(["mon","tue","wed"])
#
# zbiór	my_set = {1, 2, 3}
# my_set = set([1, 2, 3])
#
# słownik	my_dictionary = {"key1": "value1", "key2": "value2"}
# my_dictionary = dict((("key1", "value1"), ("key2", "value2")))


# Funkcje

# greetings = "cześć, poskramiaczu lwów"
# print(greetings)

# greetings = "cześć, poskramiaczu lwów"
# print(greetings.upper())


# greetings = "cześć, poskramiaczu lwów"
# print(dir(greetings))

# Funkcje listy

# shopping_list = ["buraki", "masło", "chleb"]
# print(len(shopping_list))

# my_list = list()
# print(dir(my_list))

# Krotka funkcje

# Krotka w przeciwieństwie do list,
# nie jest mutowalna, czyli raz stworzona, zachowuje swój obraz.
#
# Tak naprawdę, dostępne metody dla krotki są niemal identyczne,
# jak w przypadku listy, z tą różnicą, że brakuje metod, które modyfikują zawartość.

# Rozpakowywanie

# days = ("pon", "wto", "śro")
# day_1, day_2, day_3 = days
# print(day_2)
# print(days[1])

# week_days = ("pon", "wto", "śro" , "czw", "pią" , "sob", "nie")
# day_1, day_2, day_3, day_4, day_5, day_6, day_7 = week_days
# print(week_days[4])
# print(day_5)


# Funkcje zbiorów

# shopping_A = {"pieczywo", "masło", "ser"}
# shopping_B = {"wędlina", "masło", "cytryna"}

# Zbiory mają swoje różnice, sumy i iloczyny.
# Takie operacje są dostępne zarówno z użyciem operatorów, jak i funkcji.

# suma
# Suma zbiorów to jest połączenie wszystkich ich elementów.
# Jest to osiągalne poprzez użycie operatora | oraz funkcji union

# shopping_A = {"pieczywo", "masło", "ser"}
# shopping_B = {"wędlina", "masło", "cytryna"}
# sets_sum = shopping_A | shopping_B
# print(sets_sum)

# shopping_A = {"pieczywo", "masło", "ser"}
# shopping_B = {"wędlina", "masło", "cytryna"}
# sets_sum = shopping_A.union(shopping_B)
# print(sets_sum)

# ilozyn

# Iloczyn zbiorów to jest ich część wspólna. Tutaj będziemy korzystać ze znaku & albo funkcji intersection.

# shopping_A = {"pieczywo", "masło", "ser"}
# shopping_B = {"wędlina", "masło", "cytryna"}
# sets_multiplication = shopping_B & shopping_A
# print(sets_multiplication)

# shopping_A = {"pieczywo", "masło", "ser"}
# shopping_B = {"wędlina", "masło", "cytryna"}
# sets_multiplication = shopping_B.intersection(shopping_A)
# print(sets_multiplication)

# shopping_A = {"pieczywo", "indyk", "ser", "ryby", "ziemniaki", "pomidory"}
# shopping_B = {"wędlina", "masło", "cytryna"}
# sets_multiplication = shopping_B.intersection(shopping_A)
# print(sets_multiplication)

# Różnica zbiorów

# Obliczysz ją w Pythonie z użyciem operatora odejmowania - albo funkcji difference.

# shopping_A = {"pieczywo", "indyk", "ser", "ryby", "ziemniaki", "pomidory"}
# shopping_B = {"wędlina", "masło", "cytryna"}
# sets_difference = shopping_A - shopping_B
# print(sets_difference)

# shopping_A = {"pieczywo", "masło", "ser"}
# shopping_B = {"wędlina", "masło", "cytryna"}
# sets_difference = shopping_A.difference(shopping_B)
# print(sets_difference)

# Słownik funkcje

# shopping_dict = {
#     "warzywniak": ["buraki", "ziemniaki"],
#     "piekarnia": ["bułka", "chleb"]
# }
# print(shopping_dict.keys())
# print(shopping_dict.values())
#
# shopping_dict = {
#     "warzywniak": ["buraki", "ziemniaki"],
#     "piekarnia": ["bułka", "chleb"]
# }
# print(shopping_dict.get("warzywniak"))

# ========================

# Modyfikacje kolekcji

# Podmiana

# shopping_list = ["buraki", "masło", "chleb"]
# shopping_list[2] = "chleb bezglutenowy"
# print(shopping_list)

# Powiększanie

# shopping_list = ["buraki", "masło", "chleb"]
# shopping_list.append("tuńczyk")
# print(shopping_list)

# Metoda append dodaje element na koniec listy. Zastosujmy to samo z użyciem operatora +.

# shopping_list = ["buraki", "masło", "chleb"]
# # dostajesz SMS
# shopping_list = shopping_list + ["tuńczyk"]
# print(shopping_list)

# directions = ["pólnoc", "południe"]
# directions = directions + ["zachód"]
# directions.append("wschód")
# print(directions)

# Pomniejszanie

# Lista umożliwia też usuwanie elementów. Mamy tutaj dwa sposoby.
# Pierwszy używa indeksów, więc w tym przypadku musisz
# "pamiętać”, gdzie jest element, który chcesz usunąć

# shopping_list = ["buraki", "masło", "chleb"]
# # nie chce Ci się nosić buraków
# del shopping_list[0]
# print(shopping_list)

# Drugi sposób usuwania to użycie funkcji remove. Tutaj wystarczy znać wartość elementu – w tym wypadku string.
# shopping_list = ["buraki", "masło", "chleb"]
# # nie chce Ci się nosić buraków
# shopping_list.remove("buraki")
# print(shopping_list)

# ============

# directions = ["pólnoc", "południe"]
# directions = directions + ["zachód"]
# directions.append("wschód")
# print(f"Po dodaniu funkcjami append oraz + lista ma wygląd: {directions}")
#
# del directions[0]
# directions.remove("południe")
# print(f"Po  usunięciu funkcjami del oraz remove na liście pozostało: {directions}")
# ===================================

# Porządkowanie

# Najprostszym przykładem sortowania listy z tekstami będzie ułożenie jej elementów w porządku alfabetycznym.
# Sortować możesz funkcją dostępną dla obiektu albo wbudowaną

# shopping_list = ["buraki", "masło", "chleb"]
# sorted_shopping_list = sorted(shopping_list)
# print(f"Lista po sortowaniu {sorted_shopping_list}")
# print(f"Lista pierwotna {shopping_list}")

# Używamy tutaj wbudowanej funkcji sorted. Co ciekawe, nie modyfikuje ona kolekcji jako takiej.
# pierwotna lista pozostała nienaruszona.

# podobny efekt poprzez użycie funkcji sort.

# shopping_list = ["buraki", "masło", "chleb"]
# shopping_list.sort()
# print(f"Lista po sortowaniu {shopping_list}")

# Ćwiczenie

# numbers = [55, 44, 3, 5, 77, 2, 1, -313, -22, 442, 5, 88]
# numbers.sort()
# print(numbers)

# numbers = [55, 44, 3, 5, 77, 2, 1, -313, -22, 442, 5, 88]
# sorted_numbers = sorted(numbers)
# print(f"Lista pierwotna: {numbers}")
# print(f"Lista po sortowaniu: {sorted_numbers}")

# ===================

# Krotka

# Krotka jest podobna do listy, ale... no właśnie, to ważne “ale”. Nie jest mutowalna.
# Dobrym sprawdzianem tego jest próba wywołania na niej metod append lub remove,

# krotka = (1, 2, 3)
# del krotka[0]

# ===========

# Zbiór

# do zbiorów nie możemy się odwoływać po indeksie,
# jesteśmy w stanie aktualizować ich zawartość funkcją update

# my_set = {1, 2, 4}
# print(f"przed zmianami zbiór to {my_set}")
# my_set.update({3})
# print(f"po zmianach zbiór to {my_set}")

# Cwiczenie

# week_days = {'pon', 'wto', 'sro', 'pia', 'sob', 'nie'}
# print(f"Przed zmianami zbiór: {week_days}")
# week_days.update({'czw'})
# print(f"Zbiór po zmianach: {week_days}")
# ====================

# Słownik

# Analogicznie do listy, słownik możemy modyfikować i sortować.
# Pamiętajmy jednak, że tutaj mamy do czynienia z nierozłącznymi parami klucz-wartość.

# salads = {
#     "owocowa": ["ananas", "truskawka", "jagody"],
#     "moja_buraczana": ["buraki", "ser kozi", "rukola"],
#     "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
# }
#
# print(salads.values())
# print(salads.keys())
#
# print(salads.get("owocowa"))
# print(salads.get("moja_buraczana"))

# Dodawanie elementów

# Dodawanie elementów do słownika jest proste.
# Należy odwołać się do nowego, nieistniejącego jeszcze klucza i wpisać jego wartość.

# salads = {
#     "owocowa": ["ananas", "truskawka", "jagody"],
#     "moja_buraczana": ["buraki", "ser kozi", "rukola"],
#     "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
# }
#
# salads["mięsna"] = ["szynka", "kurczak", "ryż", "ogórek"]
# print(salads.keys())

# Podmiana

# możemy podmienić jej elementy poprzez przypisanie nowej listy do odpowiedniej nazwy klucza

# salads = {
#     "owocowa": ["ananas", "truskawka", "jagody"],
#     "moja_buraczana": ["buraki", "ser kozi", "rukola"],
#     "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
# }
# salads["owocowa"] = ["ananas", "truskawka", "jagody", "jogurt grecki"]
# print(salads["owocowa"])

# salads = {
#     "owocowa": ["ananas", "truskawka", "jagody"],
#     "moja_buraczana": ["buraki", "ser kozi", "rukola"],
#     "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
# }
# salads["owocowa"].append("jogurt 10%")
# print(salads["owocowa"])

# Usuwanie

# Pozbywamy się elementów ze słownika, odwołując się do ich kluczy. Używamy operatora del

# salads = {
#     "owocowa": ["ananas", "truskawka", "jagody"],
#     "moja_buraczana": ["buraki", "ser kozi", "rukola"],
#     "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
# }
# salads["owocowa"].append("jogurt 10%")
# print(salads["owocowa"])
#
# print(salads.keys())
# del salads['mamina']
# print(salads.keys())

# my_dict = {
#     "python": "pyton",
#     "tree": "drzewo"
# }
# print(my_dict)
#
# translation = my_dict.get("python")
# print(translation)

# my_dict = {
#     "tree": "drzewo"
# }
# print(my_dict)
#
# translation = my_dict.setdefault("python",
# "super język")
# print(translation)
# print(my_dict)

# ==========================================
# zadanie 1

# print("Zadanie 1")
#
# name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
# for word in name_list:
#     print(len(word))
#
# name_dictionary = {
#     name_list[0]: len(name_list[0]),
#     name_list[1]: len(name_list[1]),
#     name_list[2]: len(name_list[2]),
#     name_list[3]: len(name_list[3]),
#     name_list[4]: len(name_list[4])
# }
# print(name_dictionary)
#
# print("=" * 25)
# # =============================
#
# print("wersja 2")
# name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
# words = [word for word in name_list]
# name_dictionary = {
#     name_list[0]: len(words[0]),
#     name_list[1]: len(words[1]),
#     name_list[2]: len(words[2]),
#     name_list[3]: len(words[3]),
#     name_list[4]: len(words[4])
# }
# print(name_dictionary)
# # =============================
# print("=" * 25)
# =====================
# Zadanie 2

# print("Zadanie 2")
#
# def czy_pierwsza(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False
#
#     pierw = int(n**0.5) + 1
#     for dzielnik in range(3, pierw, 2):
#         if n % dzielnik == 0:
#             return False
#     return True
#
# # ================
#
# def czy_pierwsza(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(czy_pierwsza(12))
# print(czy_pierwsza(13))
#
# # ===============
# import math
#
# def czyPierwsza(a):
#     if a< 0:
#         return False
#     for i in (range(2, int(math.sqrt(a)))):
#         if a % i == 0:
#             return False
#     return True
# print("Program sprawdzający czy liczba jest liczbą pierwszą.")
# print("Podaj liczbę: ")
# a = int(input())
# print(czyPierwsza(a))
# ======================
# Zadanie 2
# print("=" * 25)
# print("Zadanie 2\n")
# digit_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
# digit_first = digit_list[0]
# digit_last = digit_list[-1]
# for i in range(digit_first, digit_last +1):
#     if i > 1:
#         for j in range(2, i):
#             if(i % j == 0):
#                 break
#         else:
#             print(i)
# # ==============================
# print("=" * 25)
# print("Zadanie 3\n")
#
# week_days = ['pon','śro','pią','sob']
# week_days.insert(1, 'wto')
# week_days.insert(3, 'czw')
# week_days.insert(6, 'nie')
# print(week_days)
#
# # ===============
# print("=" * 25)
# print("Zadanie 4\n")
# make_tea_unsorted = ['włącz czajnik', 'znajdź opakowanie herbaty', 'zalej herbatę',
#                      'nalej wody do czajnika', 'wyjmij kubek', 'włóż herbatę do kubka']
# make_tea = [
#     {'sequence': 2, 'action': 'włącz czajnik'},
#     {'sequence': 3, 'action': 'znajdź opakowanie herbaty'},
#     {'sequence': 6, 'action': 'zalej herbatę'},
#     {'sequence': 1, 'action': 'nalej wody do czajnika'},
#     {'sequence': 4, 'action': 'wyjmij kubek'},
#     {'sequence': 5, 'action': 'włóż herbatę do kubka'},
# ]
# def get_sequence(make_tea):
#     return make_tea.get('sequence')
# def get_action(make_tea):
#     return make_tea.get('action')
# make_tea.sort(key = get_sequence)
# print(f"Sekwencja niesortowana: {make_tea_unsorted}")
# print(f"Sekwencja posortowana: {make_tea}", end='\n')

# ==================
# Iterator

# Iterator to specyficzny obiekt, który ułatwia pracę na kolekcji.
# Wywołujemy go funkcją iter. Zobaczmy na przykładzie, jak można go użyć.
# Najpierw stworzymy listę.

# vegetables = ["burak", "ziemniak", "szczypior", "cebula"]
# # for vegetable in vegetables:
# #     print(vegetable)
# veggie_iterator = iter(vegetables)
# print(veggie_iterator)
# for vegetable in veggie_iterator:
#     print(vegetable)

# ==============
# NEXT
# vegetables = ["burak", "ziemniak", "szczypior", "cebula"]
# veggie_iterator = iter(vegetables)
# print(next(veggie_iterator))
# print(next(veggie_iterator))
# print(next(veggie_iterator))

# ================

# Iteracja po krotkach i słownikach

# shopping = [("buraki", 1.25), ("mleko", 4.0), ("chleb", 3.50), ("wino", 15)]
# for product, price in shopping:
#     print(product)

# Możemy też powyższą sytuację zamodelować jako słownik.
# Stworzenie go z listy krotek jest bardzo proste,
# musimy tylko objąć istniejącą listę w funkcję dict
# shopping_dict = dict(shopping)
# print(shopping_dict)
#
# for product in shopping_dict:
#     print(product)

# Iteracja po słowniku nie zwraca kompletnych obiektów-par, a jedynie klucze.
# Jeśli chcielibyśmy odnieść się do całości,
# musielibyśmy użyć metody items na obiekcie słownika
# for product in shopping_dict.items():
#     print(product)

# print("ćwiczenie \nStwórz słownik z nazwami krajów (klucze) i ich stolic (wartości) "
#       "dla wszystkich sąsiadów Polski.\n "
#       "Następnie przejdź przez słownik i wydrukuj wszystkie pary klucz-stolica")
#
# polish_neighbours_dict = {
#     "Rosja": "Moskwa",
#     "Białoruś": "Mińsk",
#     "Ukraina": "Kijów",
#     "Słowacja": "Bratysława",
#     "Czechy": "Praga",
#     "Niemcy": "Berlin"
# }
# # print(polish_neighbours_dict)
# # for key in polish_neighbours_dict.items():
# #     print(polish_neighbours_dict)
# items = polish_neighbours_dict.items()
# print(items)

# ======================
# OPERACJE NA DANYCH

#  Dla zadanej listy liczb chcemy stworzyć kolejną,
#  złożoną z kwadratów tych liczb –
#  dla każdej liczby będziemy szukać jej drugiej potęgi.

# numbers = [1, 3, 5, 11, 20]
# squares = []
# for number in numbers:
#     squares.append(number * number)
# print(f"Na wstępie mieliśmy taką listę {numbers}")
# print(f"A oto jej kwadraty {squares}")

# ===============
# Lista składana - list comprehension.

# Jej podstawowa konstrukcja to:
# [wyrażenie for element in lista]
# numbers = [1, 3, 5, 11, 20]
# squares = [number * number for number in numbers]
# print(f"Te kwadraty {squares} uzyskano dzięki list comprehension")

# ===============
# Filtrowanie w liście składanej

# Lista składana umożliwia także filtrowanie elementów kolekcji.
# Wtedy zapis rozszerza się do poniższego:
#
# [wyrażenie for element in lista if warunek]

# numbers = [1, 2, 0, 3, 0, 0, 0]
# squares = []
# for number in numbers:
#     if number > 0:
#         squares.append(number * number)

# numbers = [1, 2, 0, 3, 0, 0, 0]
# squares = [number * number for number in numbers if number > 0]
# print(squares)

# print("Cwiczenie")
#
# philosophers = ['Arystoteles','Platon','Sokrates']
# lenght_of_name = [len(word) for word in philosophers]
# print(lenght_of_name)

# =================

# Slicing (krojenie)

# Zakresy

# weekdays = ["pon", "wto", "śro", "czw", "pią", "sob", "nie"]
# indeks:     0      1      2      3      4      5      6

# Gdy chcemy pobrać 2 pierwsze elementy,
# możemy użyć zakresu, którego dolną i
# górną granicę oddzielamy dwukropkiem np.

# weekdays[0:2]
# # to elementy od indeksu nr 0 (włącznie) do indeksu nr 2 (ale już bez niego), czyli dwa pierwsze elementy
#
# weekdays[3:6]
# # to trzy elementy listy, od 3 (włącznie) do 6.
#
# weekdays[:4] # pokazuje pierwsze 4 elementy
#
# # Ujemne indeksy
# # żeby odwołać się do ostatniego elementu listy, piszemy po prostu
# weekdays[-1]
#
# # Ujemne indeksowanie należy czytać w ten sposób:
# # ile mamy elementów od końca. Jeśli więc dajemy taki zakres:
# weekdays[-2:]

# =====================
# Zadanie: listy składane

print("Zadanie 1\n  Użyj listy składanej, aby stworzyć listę sześcianów (potęgi trzeciej)"
      "\nliczb z zakresu od 1 do 10. Następnie użyj pętli for in, "
      "\naby zwrócić w konsoli liczby niepodzielne przez 2\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 3
third_power = [pow(number, x) for number in numbers]
divisible_by_2 = [pow(number, x) for number in numbers if number % 2 == 0]
print(f"liczby: {numbers} \ndo sześcianu dają: {third_power}, \na sześciany podzielne przez 2 to: {divisible_by_2}")

# ================
print("=" * 25)
print("Zadanie 2")

digits = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
sorted_digits = sorted(digits)
zero_digits = sorted_digits[0:10]
# print(sorted_digits)
non_zero_digits = sorted_digits[10:14]
print(f"Lista z zerami: {zero_digits}")
print(f"Lista bez zer: {non_zero_digits}")
