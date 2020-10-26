#-*- coding: utf-8 -*-
import os
#Zadanie numer 1
#Patrycja Grantze, Jonatan Bresa



#funkcja odczytyjąca z pliku txt
def open_file ():
    f = open (nazwa_pliku , "r" , encoding='utf8')
    plain = ""
    for i in f :
        plain = plain + i
    g = f. read ()
    print("Plik otwarty pomyślnie.")
    return plain
    



#funkcja czyszcząca ze znaków interpunkcyjncyh
def clean_text_inter(plik):
    text = plik.strip()
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("?", "")
    text = text.replace(":", "")
    text = text.replace(";", "")
    text = text.replace("!", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("-", "")
    text = text.replace("\"", "")
    print("Z tekstu zostały usunięte znaki interpunkcyjne.")
    return text

#funkcja czyszcząca ze znaków specjalnych
def clean_text_special(plik):
    text = plik.strip()
    text = text.replace("/", "")
    text = text.replace("'", "")
    text = text.replace(">", "")
    text = text.replace("<", "")
    text = text.replace("@", "")
    text = text.replace("#", "")
    text = text.replace("$", "")
    text = text.replace("%", "")
    text = text.replace("^", "")
    text = text.replace("&", "")
    text = text.replace("*", "")
    text = text.replace("_", "")
    text = text.replace("+", "")
    text = text.replace("=", "")
    text = text.replace("`", "")
    text = text.replace("~", "")
    text = text.replace("|", "")
    text = text.replace("]", "")
    text = text.replace("[", "")   
    text = text.replace("}", "") 
    text = text.replace("{", "")  
    print("Tekst został oczyszczony ze znaków specjalnych.")
    return text

#funkcja czyszcząca ze spacji
def clean_text_space(plik):
    text = plik.strip()
    text = text.replace(" ", "")
    print("Tekst został oczyszczony ze spacji.")
    return text

#funkcja czyszcząca ze wszystkich przejć do nowej linii
def clean_text_newline(plik):
    text = plik.strip()
    text = text.replace("\n", "")
    print("Z tesktu usunięto wszystkie przejścia do nowej linii.")
    return text

#funkcja czyszcząca ze wszsystkich tabulatorów
def clean_text_tab(plik):
    text = plik.strip()
    text = text.replace("\t", "")
    print("Z tekstu usunięto wszystkie tabulatory.")
    return text


#funkcja czyszcząca tekst z liczb
def clean_num(plik):
    text = plik.strip()
    #print ( text )
    text = text.replace ("1" ," ")
    text = text.replace ("2" , " ")
    text = text.replace ("3" , " ")
    text = text.replace ("4" , " ")
    text = text.replace ("5" , " ")
    text = text.replace ("6" , " ")
    text = text.replace ("7" , " ")
    text = text.replace ("8" , " ")
    text = text.replace ("9" , " ")
    text = text.replace ("0" , " ")
    print ("Z tekstu pomyślnie usunięto cyfry.")
    return text

#funkcja czyszcząca ze znaków diakrytycznych
def removeAccents(s):
    transliteration = [[
    'Ĳ' , 'I'],[ 'Ö' , 'O'],['Œ' , 'O'],['Ü' , 'U'],['ä' , 'a'],['æ' , 'a'],[
    'ĳ' , 'i'],['ö' , 'o'],['œ' , 'o'],['ü' , 'u'],['ß' , 's'],['ſ' , 's'],[
    'À' , 'A'],['Á' , 'A'],['Â' , 'A'],['Ã' , 'A'],['Ä' , 'A'],['Å' , 'A'],[
    'Æ' , 'A'],['Ā' , 'A'],['Ą' , 'A'],['Ă' , 'A'],['Ç' , 'C'],['Ć' , 'C'],[
    'Č' , 'C'],['Ĉ' , 'C'],['Ċ' , 'C'],['Ď' , 'D'],['Đ' , 'D'],['È' , 'E'],[
    'É' , 'E'],['Ê' , 'E'],['Ë' , 'E'],['Ē' , 'E'],['Ę' , 'E'],['Ě' , 'E'],[
    'Ĕ' , 'E'],['Ė' , 'E'],['Ĝ' , 'G'],['Ğ' , 'G'],['Ġ' , 'G'],['Ģ' , 'G'],[
    'Ĥ' , 'H'],['Ħ' , 'H'],['Ì' , 'I'],['Í' , 'I'],['Î' , 'I'],['Ï' , 'I'],[
    'Ī' , 'I'],['Ĩ' , 'I'],['Ĭ' , 'I'],['Į' , 'I'],['İ' , 'I'],['Ĵ' , 'J'],[
    'Ķ' , 'K'],['Ľ' , 'K'],['Ĺ' , 'K'],['Ļ' , 'K'],['Ŀ' , 'K'],['Ł' , 'L'],[
    'Ñ' , 'N'],['Ń' , 'N'],['Ň' , 'N'],['Ņ' , 'N'],['Ŋ' , 'N'],['Ò' , 'O'],[
    'Ó' , 'O'],['Ô' , 'O'],['Õ' , 'O'],['Ø' , 'O'],['Ō' , 'O'],['Ő' , 'O'],[
    'Ŏ' , 'O'],['Ŕ' , 'R'],['Ř' , 'R'],['Ŗ' , 'R'],['Ś' , 'S'],['Ş' , 'S'],[
    'Ŝ' , 'S'],['Ș' , 'S'],['Š' , 'S'],['Ť' , 'T'],['Ţ' , 'T'],['Ŧ' , 'T'],[
    'Ț' , 'T'],['Ù' , 'U'],['Ú' , 'U'],['Û' , 'U'],['Ū' , 'U'],['Ů' , 'U'],[
    'Ű' , 'U'],['Ŭ' , 'U'],['Ũ' , 'U'],['Ų' , 'U'],['Ŵ' , 'W'],['Ŷ' , 'Y'],[
    'Ÿ' , 'Y'],['Ý' , 'Y'],['Ź' , 'Z'],['Ż' , 'Z'],['Ž' , 'Z'],['à' , 'a'],[
    'á' , 'a'],['â' , 'a'],['ã' , 'a'],['ā' , 'a'],['ą' , 'a'],['ă' , 'a'],[
    'å' , 'a'],['ç' , 'c'],['ć' , 'c'],['č' , 'c'],['ĉ' , 'c'],['ċ' , 'c'],[
    'ď' , 'd'],['đ' , 'd'],['è' , 'e'],['é' , 'e'],['ê' , 'e'],['ë' , 'e'],[
    'ē' , 'e'],['ę' , 'e'],['ě' , 'e'],['ĕ' , 'e'],['ė' , 'e'],['ƒ' , 'f'],[
    'ĝ' , 'g'],['ğ' , 'g'],['ġ' , 'g'],['ģ' , 'g'],['ĥ' , 'h'],['ħ' , 'h'],[
    'ì' , 'i'],['í' , 'i'],['î' , 'i'],['ï' , 'i'],['ī' , 'i'],['ĩ' , 'i'],[
    'ĭ' , 'i'],['į' , 'i'],['ı' , 'i'],['ĵ' , 'j'],['ķ' , 'k'],['ĸ' , 'k'],[
    'ł' , 'l'],['ľ' , 'l'],['ĺ' , 'l'],['ļ' , 'l'],['ŀ' , 'l'],['ñ' , 'n'],[
    'ń' , 'n'],['ň' , 'n'],['ņ' , 'n'],['ŉ' , 'n'],['ŋ' , 'n'],['ò' , 'o'],[
    'ó' , 'o'],['ô' , 'o'],['õ' , 'o'],['ø' , 'o'],['ō' , 'o'],['ő' , 'o'],[
    'ŏ' , 'o'],['ŕ' , 'r'],['ř' , 'r'],['ŗ' , 'r'],['ś' , 's'],['š' , 's'],[
    'ť' , 't'],['ù' , 'u'],['ú' , 'u'],['û' , 'u'],['ū' , 'u'],['ů' , 'u'],[
    'ű' , 'u'],['ŭ' , 'u'],['ũ' , 'u'],['ų' , 'u'],['ŵ' , 'w'],['ÿ' , 'y'],[
    'ý' , 'y'],['ŷ' , 'y'],['ż' , 'z'],['ź' , 'z'],['ž' , 'z'],['Α' , 'A'],[
    'Ά' , 'A'],['Ἀ' , 'A'],['Ἁ' , 'A'],['Ἂ' , 'A'],['Ἃ' , 'A'],['Ἄ' , 'A'],[
    'Ἅ' , 'A'],['Ἆ' , 'A'],['Ἇ' , 'A'],['ᾈ' , 'A'],['ᾉ' , 'A'],['ᾊ' , 'A'],[
    'ᾋ' , 'A'],['ᾌ' , 'A'],['ᾍ' , 'A'],['ᾎ' , 'A'],['ᾏ' , 'A'],['Ᾰ' , 'A'],[
    'Ᾱ' , 'A'],['Ὰ' , 'A'],['ᾼ' , 'A'],['Β' , 'B'],['Γ' , 'G'],['Δ' , 'D'],[
    'Ε' , 'E'],['Έ' , 'E'],['Ἐ' , 'E'],['Ἑ' , 'E'],['Ἒ' , 'E'],['Ἓ' , 'E'],[
    'Ἔ' , 'E'],['Ἕ' , 'E'],['Ὲ' , 'E'],['Ζ' , 'Z'],['Η' , 'I'],['Ή' , 'I'],[
    'Ἠ' , 'I'],['Ἡ' , 'I'],['Ἢ' , 'I'],['Ἣ' , 'I'],['Ἤ' , 'I'],['Ἥ' , 'I'],[
    'Ἦ' , 'I'],['Ἧ' , 'I'],['ᾘ' , 'I'],['ᾙ' , 'I'],['ᾚ' , 'I'],['ᾛ' , 'I'],[
    'ᾜ' , 'I'],['ᾝ' , 'I'],['ᾞ' , 'I'],['ᾟ' , 'I'],['Ὴ' , 'I'],['ῌ' , 'I'],[
    'Θ' , 'T'],['Ι' , 'I'],['Ί' , 'I'],['Ϊ' , 'I'],['Ἰ' , 'I'],['Ἱ' , 'I'],[
    'Ἲ' , 'I'],['Ἳ' , 'I'],['Ἴ' , 'I'],['Ἵ' , 'I'],['Ἶ' , 'I'],['Ἷ' , 'I'],[
    'Ῐ' , 'I'],['Ῑ' , 'I'],['Ὶ' , 'I'],['Κ' , 'K'],['Λ' , 'L'],['Μ' , 'M'],[
    'Ν' , 'N'],['Ξ' , 'K'],['Ο' , 'O'],['Ό' , 'O'],['Ὀ' , 'O'],['Ὁ' , 'O'],[
    'Ὂ' , 'O'],['Ὃ' , 'O'],['Ὄ' , 'O'],['Ὅ' , 'O'],['Ὸ' , 'O'],['Π' , 'P'],[
    'Ρ' , 'R'],['Ῥ' , 'R'],['Σ' , 'S'],['Τ' , 'T'],['Υ' , 'Y'],['Ύ' , 'Y'],[
    'Ϋ' , 'Y'],['Ὑ' , 'Y'],['Ὓ' , 'Y'],['Ὕ' , 'Y'],['Ὗ' , 'Y'],['Ῠ' , 'Y'],[
    'Ῡ' , 'Y'],['Ὺ' , 'Y'],['Φ' , 'F'],['Χ' , 'X'],['Ψ' , 'P'],['Ω' , 'O'],[
    'Ώ' , 'O'],['Ὠ' , 'O'],['Ὡ' , 'O'],['Ὢ' , 'O'],['Ὣ' , 'O'],['Ὤ' , 'O'],[
    'Ὥ' , 'O'],['Ὦ' , 'O'],['Ὧ' , 'O'],['ᾨ' , 'O'],['ᾩ' , 'O'],['ᾪ' , 'O'],[
    'ᾫ' , 'O'],['ᾬ' , 'O'],['ᾭ' , 'O'],['ᾮ' , 'O'],['ᾯ' , 'O'],['Ὼ' , 'O'],[
    'ῼ' , 'O'],['α' , 'a'],['ά' , 'a'],['ἀ' , 'a'],['ἁ' , 'a'],['ἂ' , 'a'],[
    'ἃ' , 'a'],['ἄ' , 'a'],['ἅ' , 'a'],['ἆ' , 'a'],['ἇ' , 'a'],['ᾀ' , 'a'],[
    'ᾁ' , 'a'],['ᾂ' , 'a'],['ᾃ' , 'a'],['ᾄ' , 'a'],['ᾅ' , 'a'],['ᾆ' , 'a'],[
    'ᾇ' , 'a'],['ὰ' , 'a'],['ᾰ' , 'a'],['ᾱ' , 'a'],['ᾲ' , 'a'],['ᾳ' , 'a'],[
    'ᾴ' , 'a'],['ᾶ' , 'a'],['ᾷ' , 'a'],['β' , 'b'],['γ' , 'g'],['δ' , 'd'],[
    'ε' , 'e'],['έ' , 'e'],['ἐ' , 'e'],['ἑ' , 'e'],['ἒ' , 'e'],['ἓ' , 'e'],[
    'ἔ' , 'e'],['ἕ' , 'e'],['ὲ' , 'e'],['ζ' , 'z'],['η' , 'i'],['ή' , 'i'],[
    'ἠ' , 'i'],['ἡ' , 'i'],['ἢ' , 'i'],['ἣ' , 'i'],['ἤ' , 'i'],['ἥ' , 'i'],[
    'ἦ' , 'i'],['ἧ' , 'i'],['ᾐ' , 'i'],['ᾑ' , 'i'],['ᾒ' , 'i'],['ᾓ' , 'i'],[
    'ᾔ' , 'i'],['ᾕ' , 'i'],['ᾖ' , 'i'],['ᾗ' , 'i'],['ὴ' , 'i'],['ῂ' , 'i'],[
    'ῃ' , 'i'],['ῄ' , 'i'],['ῆ' , 'i'],['ῇ' , 'i'],['θ' , 't'],['ι' , 'i'],[
    'ί' , 'i'],['ϊ' , 'i'],['ΐ' , 'i'],['ἰ' , 'i'],['ἱ' , 'i'],['ἲ' , 'i'],[
    'ἳ' , 'i'],['ἴ' , 'i'],['ἵ' , 'i'],['ἶ' , 'i'],['ἷ' , 'i'],['ὶ' , 'i'],[
    'ῐ' , 'i'],['ῑ' , 'i'],['ῒ' , 'i'],['ῖ' , 'i'],['ῗ' , 'i'],['κ' , 'k'],[
    'λ' , 'l'],['μ' , 'm'],['ν' , 'n'],['ξ' , 'k'],['ο' , 'o'],['ό' , 'o'],[
    'ὀ' , 'o'],['ὁ' , 'o'],['ὂ' , 'o'],['ὃ' , 'o'],['ὄ' , 'o'],['ὅ' , 'o'],[
    'ὸ' , 'o'],['π' , 'p'],['ρ' , 'r'],['ῤ' , 'r'],['ῥ' , 'r'],['σ' , 's'],[
    'ς' , 's'],['τ' , 't'],['υ' , 'y'],['ύ' , 'y'],['ϋ' , 'y'],['ΰ' , 'y'],[
    'ὐ' , 'y'],['ὑ' , 'y'],['ὒ' , 'y'],['ὓ' , 'y'],['ὔ' , 'y'],['ὕ' , 'y'],[
    'ὖ' , 'y'],['ὗ' , 'y'],['ὺ' , 'y'],['ῠ' , 'y'],['ῡ' , 'y'],['ῢ' , 'y'],[
    'ῦ' , 'y'],['ῧ' , 'y'],['φ' , 'f'],['χ' , 'x'],['ψ' , 'p'],['ω' , 'o'],[
    'ώ' , 'o'],['ὠ' , 'o'],['ὡ' , 'o'],['ὢ' , 'o'],['ὣ' , 'o'],['ὤ' , 'o'],[
    'ὥ' , 'o'],['ὦ' , 'o'],['ὧ' , 'o'],['ᾠ' , 'o'],['ᾡ' , 'o'],['ᾢ' , 'o'],[
    'ᾣ' , 'o'],['ᾤ' , 'o'],['ᾥ' , 'o'],['ᾦ' , 'o'],['ᾧ' , 'o'],['ὼ' , 'o'],[
    'ῲ' , 'o'],['ῳ' , 'o'],['ῴ' , 'o'],['ῶ' , 'o'],['ῷ' , 'o'],['А' , 'A'],[
    'Б' , 'B'],['В' , 'V'],['Г' , 'G'],['Д' , 'D'],['Е' , 'E'],['Ё' , 'E'],[
    'Ж' , 'Z'],['З' , 'Z'],['И' , 'I'],['Й' , 'I'],['К' , 'K'],['Л' , 'L'],[
    'М' , 'M'],['Н' , 'N'],['О' , 'O'],['П' , 'P'],['Р' , 'R'],['С' , 'S'],[
    'Т' , 'T'],['У' , 'U'],['Ф' , 'F'],['Х' , 'K'],['Ц' , 'T'],['Ч' , 'C'],[
    'Ш' , 'S'],['Щ' , 'S'],['Ы' , 'Y'],['Э' , 'E'],['Ю' , 'Y'],['Я' , 'Y'],[
    'а' , 'A'],['б' , 'B'],['в' , 'V'],['г' , 'G'],['д' , 'D'],['е' , 'E'],[
    'ё' , 'E'],['ж' , 'Z'],['з' , 'Z'],['и' , 'I'],['й' , 'I'],['к' , 'K'],[
    'л' , 'L'],['м' , 'M'],['н' , 'N'],['о' , 'O'],['п' , 'P'],['р' , 'R'],[
    'с' , 'S'],['т' , 'T'],['у' , 'U'],['ф' , 'F'],['х' , 'K'],['ц' , 'T'],[
    'ч' , 'C'],['ш' , 'S'],['щ' , 'S'],['ы' , 'Y'],['э' , 'E'],['ю' , 'Y'],[
    'я' , 'Y'],['ð' , 'd'],['Ð' , 'D'],['þ' , 't'],['Þ' , 'T'],['ა' , 'a'],[
    'ბ' , 'b'],['გ' , 'g'],['დ' , 'd'],['ე' , 'e'],['ვ' , 'v'],['ზ' , 'z'],[
    'თ' , 't'],['ი' , 'i'],['კ' , 'k'],['ლ' , 'l'],['მ' , 'm'],['ნ' , 'n'],[
    'ო' , 'o'],['პ' , 'p'],['ჟ' , 'z'],['რ' , 'r'],['ს' , 's'],['ტ' , 't'],[
    'უ' , 'u'],['ფ' , 'p'],['ქ' , 'k'],['ღ' , 'g'],['ყ' , 'q'],['შ' , 's'],[
    'ჩ' , 'c'],['ც' , 't'],['ძ' , 'd'],['წ' , 't'],['ჭ' , 'c'],['ხ' , 'k'],[
    'ჯ' , 'j'],['ჰ' , 'h']]
    new_s = ''
    for t in s:
        check = False
        for j in transliteration:
            if t == j[0]:
                new_s += j[1]
                check = True
                break;
        if check == False:
            new_s += t
    print("Wszystkie znaki diakrytyczne zostały usunięte.")
    return new_s;
    
#funkcja czyszcząca tekst z wielkich liter
def clean_acc(plik):
    text = plik.strip()
    text = text.lower()
    print ( "Wszystkie litery wielkie zostały pomyślnie zamienione na litery małe." )
    return text

#funkcja dzieląca tekst na 7 kolumn po 5 znaków każdy
def col_text(plik):
    text = plik.strip()
    length = len(text)
    print(length)
    row = length//35 +1
    cols = text
    for i in range(0,row):
        cols = cols [0:(5+(42*i))]+ " " + cols[(5+42*i): len( cols )]
        cols = cols [0:(11+42*i)]+ " "+ cols [(11+42*i): len( cols )]
        cols = cols [0:(17+42*i)]+ " "+ cols [(17+42*i): len( cols )]
        cols = cols [0:(23+42*i)]+ " "+ cols [(23+42*i): len( cols )]
        cols = cols [0:(29+42*i)]+ " "+ cols [(29+42*i): len( cols )]
        cols = cols [0:(35+42*i)]+ " "+ cols [(35+42*i): len( cols )]
        cols = cols [0:(41+42*i)]+ "\n"+ cols [(41+42*i): len( cols )]
    print(cols)
    return cols

#funkcja do zapisu naszego tekstu wyjsciowego
def save_file (plik, name):
    file = open (name , "w" )
    file.write(plik)
    file.close()



#start programu
#pętla while odpowiedzialna na pobranie nazwy pliku
#ewentualny brak pliku lub błąd otwarcia zwraca error
status = 0
while status == 0 :
    nazwa_pliku = input("Podaj nazwę pliku z danymi ")
    #print(nazwa_pliku)
    if os.path.exists(nazwa_pliku):
        plik = open_file();
        status =1 ;
    else:
        print("Podano błędną nazwę pliku lub podany plik nie znajduję się w katalogu z plikiem głównym. Proszę spróbuj ponownie :)")
        status = 0 


#pętla while odpowiedzialna na pobranie decyzji użytkownika i zastosowania niej
#odnosnie usuwania cyfr z pliku
status = 0
while status == 0:
    num_perm = input("Czy z pliku usunąć cyfry? T/N ")
    if num_perm =="T":
        plik = clean_num(plik)
        status =1
    elif num_perm == "N":
        print("Cyfry w tekscie zachowane.")
        status = 1
    else:
        print("Podano błędną odpowiedź. Zwróć uwagę na wielkie litery i spróbuj jeszcze raz :)")
        status = 0
#odnosnie znaków interpunkcyjnych
status_0 = 0
while status_0 == 0:
    answer_0 = input ("Czy usunąć z pliku znaki interpunkcyjne? T/N ")
    if answer_0 =="T":
        plik = clean_text_inter(plik)
        status_0 =1
    elif answer_0 == "N":
        print("Znaki interpunkcyjne w tekście zachowane.")
        status_0 = 1
    else:
        print("Podano błędną odpowiedź. Zwróć uwagę na wielkie litery i spróbuj jeszcze raz :)")
        status_0 = 0
#odnosnie znakow specjalnych
status_1 = 0
while status_1 == 0:
    answer_1 = input ("Czy usunąć z pliku znaki specjalne? T/N ")
    if answer_1 =="T":
        plik = clean_text_special(plik)
        status_1 =1
    elif answer_1 == "N":
        print("Znaki specjalne w tekście zachowane.")
        status_1 = 1
    else:
        print("Podano błędną odpowiedź. Zwróć uwagę na wielkie litery i spróbuj jeszcze raz :)")
        status_1 = 0
#odnosnie spacji
status_2 = 0
while status_2 == 0:
    answer_2 = input ("Czy usunąć z pliku spacje? T/N ")
    if answer_2 =="T":
        plik = clean_text_space(plik)
        status_2 =1
    elif answer_2 == "N":
        print("Spacje w tekście zachowane.")
        status_2 = 1
    else:
        print("Podano błędną odpowiedź. Zwróć uwagę na wielkie litery i spróbuj jeszcze raz :)")
        status_2 = 0
# odnosnie przejsc do nowych linii    
status_3 = 0
while status_3 == 0:
    answer_3 = input ("Czy usunąć z pliku przejścia do nowej linii? T/N ")
    if answer_3 =="T":
        plik = clean_text_newline(plik)
        status_3 =1
    elif answer_3 == "N":
        print("Przejscia do nowej linii w tekście zachowane.")
        status_3 = 1
    else:
        print("Podano błędną odpowiedź. Zwróć uwagę na wielkie litery i spróbuj jeszcze raz :)")
        status_3 = 0
#odnosnie tabulatorów     
status_4 = 0
while status_4 == 0:
    answer_4 = input ("Czy usunąć z pliku tabulatory? T/N ")
    if answer_4 =="T":
        plik = clean_text_tab(plik)
        status_4 =1
    elif answer_4 == "N":
        print("Tabulatotry w tekście zachowane.")
        status_4 = 1
    else:
        print("Podano błędną odpowiedź. Zwróć uwagę na wielkie litery i spróbuj jeszcze raz :)")
        status_4 = 0
#odnosnie wielkich liter
status_5 = 0
while status_5 == 0:
    answer_5 = input ("Czy zamienić wszystkie litery duże na litery małe? T/N ")
    if answer_5 =="T":
        plik = clean_acc(plik)
        status_5 =1
    elif answer_5 == "N":
        print("Litery wielkie w tekście zachowane.")
        status_5 = 1
    else:
        print("Podano błędną odpowiedź. Zwróć uwagę na wielkie litery i spróbuj jeszcze raz :)")
        status_5 = 0
#odnosnie znaków diakrytycznych
status_6 = 0
while status_6 == 0:
    answer_6 = input ("Czy z tektu usunąć wszystkie znaki diakrytyczne? T/N ")
    if answer_6 =="T":
        plik = removeAccents(plik)
        status_6 =1
    elif answer_6 == "N":
        print("Znaki diakrytyczne w tekVcie zostały zachowane.")
        status_6 = 1
    else:
        print("Podano błędną odpowiedź. Zwróć uwagę na wielkie litery i spróbuj jeszcze raz :)")
        status_6 = 0

# gotowy tekst formułujemy w kolumny
plik = col_text(plik)

#Pętla while pobiera nazwę pliku wyjciowego, do którego zapisuje wynik koncowy
#Ewentualnie gdy plik istnieje już mozna go nadpisać
#zwraca error gdy podana zostanie błędna odpowiedź
status = 0 
while status == 0:
    nazwa_zapisu = input("Pod jaką nazwą zapisać wynik końcowy?  ")
    if os.path.exists(nazwa_zapisu):
        second_status =0
        while second_status == 0:
            answer = input("Plik o podanej nazwie już istnieje. Czy chcesz nadpisać plik? T/N ")
            if answer == "T":
                save_file (plik, nazwa_zapisu)
                status = 1
                second_status = 1
            elif answer == "N":
                second_status=1
            else:
                print("Podano błędną odpowiedź. Zwróć uwagę na wielkie litery i spróbuj jeszcze raz :)")
                second_status = 0
        
    else:
        save_file (plik, nazwa_zapisu)
        status = 1
    
    
