import random

words=["аист","акула","бабуин","баран","барсук","бобр","бык","варан","верблюд","волк","вомбат","воробей","ворон","выдра",
"голубь","гусь","додо","дятел","енот","ехидна","ёж","жаба","жираф","журавль","заяц","зебра","землеройка","зяблик",
"игуана","кабан","казуар","кайман","какаду","кальмар","камбала","канарейка","каракатица","карп","кенгуру",
"киви","кит","лама","ламантин","ласка","ласточка","лебедь","лев","лемур","ленивец","леопард","лиса","лягушка",
"мотылек","муравьед","муравей","мангуст","медведь","морж","муха","мышь","медуза","нарвал","носорог","орёл","омар","олень","овцебык",
"осьминог","осел","оса","овца","опоссум","обезьяна","паук","пескарь","пингвин","пиранья","попугай",
"пчела","рысь","рыба","росомаха","страус","сурок","стрекоза","сорока","сова","снегирь","сокол","собака","слон",
"скорпион","скворец","скат","сельдь","свинья","сурикат","скунс","слизень","светлячок","тюлень","тукан","тигр",
"трясогузка","термит","тетерев","тунец","тритон","тарантул","таракан","тля","утконос","уж","устрица","улитка","угорь","фазан","фламинго",
"форель","хорёк","хомяк","хамелеон","цапля","цесарка","цикада","черепаха","червь","чайка","шимпанзе","шиншила",
"щука","эму","ящерица","ястреб","як","ягуар"]
word=words[random.randrange(5)]
len_word=len(word)
health=10
test=False
used_letters=""
win_word=[]
# заполнение массива для слова в игре
for i in range(len(word)):
    win_word+="_"

while len_word!=0 and health!=0:
    test=False
    #ввод буквы и проверка на повтор
    while True:
        letter=input("\nвведите букву")
        if letter in used_letters or len(letter)>1:
            print("\nНе больше одноого символа,попроуйте снова!")
        else:
            used_letters+=letter
            break
    count=0
    for i in word:
        if letter in i:
            len_word-=1
            test=True
            win_word[count]=letter
        count+=1





    if not test:
        health-=1
        print("Неверно")
    else:
        print("Верно")
        print(win_word)
    print("Ваше здоровье = ",health)
if (len_word == 0):
    print("\nПОБЕДИТЕЛЬ!!!Слово было ",word.upper())
else:
    print("\nВЫ ПРОИГРАЛИ! ПОПРОБУЙТЕ СНОВА!  {}.".format(word))


