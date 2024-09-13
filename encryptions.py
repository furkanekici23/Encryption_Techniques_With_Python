import math
alfabe_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabe_tr = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']

language_cntrl=1
while language_cntrl ==1:
    language= int(input("Bu programı ingilizce kullanmak için '1', Türkçe kullanmak için '2' giriniz. \n(Enter '1' to use this program in English or '2' to use it in Turkish.):\n"))
    if language == 1 or 2:
        break
    else:
        continue
    

abc_cntrl=1
while abc_cntrl==1 :
 if language==1:
     abc = int(input("Enter '1' to use the English alphabet or '2' to use the Turkish alphabet: "))
 else:
     abc = int(input("İngiliz alfabesi kullanmak için '1', Türk alfabesi kullanmak için '2' giriniz: "))
     
 if abc == 1:
    alfabe = alfabe_en
    xyz = 26
    abc_cntrl=2
    break
 if abc == 2:
    alfabe = alfabe_tr
    xyz = 29
    break
 else :
     print("\nLütfen '1' ve '2' sayılarından birini girdiğinize emin olunuz\nPlease be sure if you entered '1' or '2' \n")

sec = 12
while sec > 11: 
    if language ==1:
        print("\n1) Atbash Encryption Method \
            \n2) Caesar Cipher Method \
            \n3) (A1Z26) Numerical Substitution Encryption Method\
            \n4) Linear Encryption (Affine Cipher) Method\
            \n5) Vigenère Cipher Method (Encryption) [Also works for Vernam Method.]\
            \n6) Vigenere Cipher Method (Decryption) [Also works for Vernam Method.]\
            \n7) RSA Method (Encryption) \
            \n8) RSA Method (Decryption)  \
            \n9) Morse Code (Encryption) \
            \n10) Morse Code (Decryption)\
            \n[Use '-' for dash in Morse Code options.] \
            \n11)AES (Advanced Encryption Standard) \
            \nTo use one of the above Encryption Algorithms, enter the sequence number:")
        sec = int(input(" "))
        if sec > 11 :
            print("\nPlease enter a valid number from the list.")

    if language ==2:
        print("1) Atbash Şifreleme Yöntemi \
            \n2) Sezar Şifreleme Yöntemi \
            \n3) (A1Z26) Sayısal İkame Şifreleme Yöntemi \
            \n4) Doğrusal Şifreleme (Affine Cipher) Yöntemi \
            \n5) Vigenère Cipher Yöntemi (Şifreleme) [Vernam Yöntemi için de çalışır.] \
            \n6) Vigenere Cipher Yöntemi (Şifre kırma) [Vernam Yöntemi için de çalışır.] \
            \n7) RSA Yöntemi (Şifreleme) \
            \n8) RSA Yöntemi (Şifre kırma)  \
            \n9) Morse Code (Şifreleme) [Seçtiğiniz alfabeden bağımsız olarak ingiliz alfabesi kullanılacaktır.]  \
            \n10) Morse Code (Şifre kırma)[Seçtiğiniz alfabeden bağımsız olarak ingiliz alfabesi kullanılacaktır.] \
            \n[Morse Kodu seçeneklerinde tire için '-' kullanınız.]   \
            \n11)AES (Advanced Encryption Standard) \
            \nYukarıdaki Şifreleme Algoritmalarından birini kullanmak için sıra numarasını giriniz:")
        sec = int(input(" "))
        if sec > 11 :
            print("\nLütfen listeden geçerli bir sayı giriniz.")


if sec == 1 and language ==1 :
      word = input("Please input the sentence : ")
      length = len(word)
      word_list = list(word)
      new_word_list = []
      for i in range (length) :
          letter= word_list[i]
          if letter != ' ':
              list_no= alfabe.index(letter) 
              new_list_no= xyz - list_no
              new_word_list.append(alfabe[new_list_no - 1])
          else:
              new_word_list.append(' ')
    
      new_word=''.join(new_word_list)
      print("The equivalent of the word you entered in the Atbash Encryption Method: " + new_word)
    
if sec == 1 and language==2  :
      word = input("Cümleyi giriniz  : ")
      length = len(word)
      word_list = list(word)
      new_word_list = []
      for i in range (length) :
          letter= word_list[i]
          if letter != ' ':
              list_no= alfabe.index(letter) 
              new_list_no= xyz - list_no
              list_no= alfabe.index(letter) 
              new_list_no= xyz - list_no
              new_word_list.append(alfabe[new_list_no - 1])
          else:
              new_word_list.append(' ')
    
      new_word=''.join(new_word_list)
      print("Girdiğiniz kelimenin Atbash Şifreleme Yöntemi'ndeki karşılığı: " + new_word)


if sec == 2 and language==1 :
      key= int(input("If you want to encrypt the normal word with the Caesar method, enter the number '1', to convert the encrypted word to the original word, enter the number '2':"))
      key_number= int(input("Enter the key number for the Caesar Cipher:"))
      if key == 1:
           sezar_key = key_number
      else :
           sezar_key = -key_number  

      word = input("Enter the word: ")
      length = len(word)
      word_list = list(word)
      new_word_list = []
      for i in range (length) :
          letter= word_list[i]
          if letter != ' ':
            list_no= alfabe.index(letter) 
            new_list_no= (sezar_key + list_no) % len(alfabe) #bazı durumlarda alfabe indekslerinin sınırlarını aşma durumu için çözüm mod almak.
            new_word_list.append(alfabe[new_list_no])    
          else:
              new_word_list.append(' ')
              
      new_word=''.join(new_word_list)
      print("The Caesar Cipher Method equivalent of the word you entered:" + new_word)

if sec == 2 and language==2 :
      key= int(input("Normal kelimeyi Sezar yöntemiyle şifrelemek istiyorsanız '1' sayısını,şifrelenmiş kelimeyi asıl kelimeye çevirmek için '2' sayısını giriniz: "))
      key_number= int(input("Sezar Şifrelemesi için anahtar sayıyı giriniz:"))
      if key == 1:
           sezar_key = key_number
      else :
           sezar_key = -key_number  

      word = input("Kelimeyi giriniz: ")
      length = len(word)
      word_list = list(word)
      new_word_list = []
      for i in range (length) :
          letter= word_list[i]
          if letter != ' ':
              list_no= alfabe.index(letter) 
              new_list_no= (sezar_key + list_no) % len(alfabe) #bazı durumlarda alfabe indekslerinin sınırlarını aşma durumu için çözüm mod almak.
              new_word_list.append(alfabe[new_list_no])    
          else:
              new_word_list.append(' ')
      new_word=''.join(new_word_list)
      print("Girdiğiniz kelimenin Sezar Şifreleme Yöntemi'ndeki karşılığı: " + new_word)

if sec == 3 and language==1 :

    word= input("Enter the numbers (Enter the letter 'l' after each number you type.)")
    length=len(word)
    word_list = list(word)
    new_word_list =[]
    temp = [ ] 
    
    for i in range (length):
     symbol = word_list[i]
     if symbol == ' ' :
         new_word_list.append(' ')

     elif symbol == 'l' :
          nm = int(''.join(temp)) - 1
          new_word_list.append(alfabe[nm])
          temp = []

     else :
         temp.append(symbol)
        
    new_word = ''.join(new_word_list)
    print(new_word) 

if sec == 3 and language==2 :

    word= input("Sayıları giriniz  (Yazdığın her sayıdan sonra 'l' harfini  giriniz.)")
    length=len(word)
    word_list = list(word)
    new_word_list =[]
    temp = [ ] 
    
    for i in range (length):
     symbol = word_list[i]
     if symbol == ' ' :
         new_word_list.append(' ')

     elif symbol == 'l' :
          nm = int(''.join(temp)) - 1
          new_word_list.append(alfabe[nm])
          temp = []

     else :
         temp.append(symbol)
        
    new_word = ''.join(new_word_list)
    print(new_word)         

if sec == 4  and language ==1:
    print ("For y=ax+b method: ")
    a=int(input("Enter the value a: "))
    b=int(input("Enter the value b: "))
    word = input("Enter the word: ")
    length=len(word)
    word_list = list(word)
    new_word_list =[]

    for i in range (length):
        letter = word_list[i]
        list_no= alfabe.index(letter)
        x=list_no
        y= ((a*x)+b) % len(alfabe)
        new_letter=alfabe[y]
        new_word_list.append(new_letter)


    new_word = ''.join(new_word_list)
    print("Word according to Affine Cipher Method: "+new_word)

if sec == 4  and language ==2:
    print ("y=ax+b methodu için: ")
    a=int(input("a değerini giriniz: "))
    b=int(input("b değerini giriniz: "))
    word = input("Kelimeyi giriniz: ")
    length=len(word)
    word_list = list(word)
    new_word_list =[]

    for i in range (length):
        letter = word_list[i]
        list_no= alfabe.index(letter)
        x=list_no
        y= ((a*x)+b) % len(alfabe)
        new_letter=alfabe[y]
        new_word_list.append(new_letter)


    new_word = ''.join(new_word_list)
    print("Affine Cipher Yöntemine göre kelime: "+new_word)

if sec == 5 and language ==1:
    table = []
    for i in range(len(alfabe)):
         row = []
         for j in range(len(alfabe)):
             row.append(alfabe[(i + j) % len(alfabe)])
         table.append(row)

    # Vigenère has been created

    word = input("Enter the sentence ")
    key = input("Enter the key: \n(If the key consists of more than one word, please write it one after the other without leaving a space in between.) ")

    length = len(word)   
    key_list_main = list(key)
    key_list = list(key)
    word_list = list(word)
    k=0
    if len(key) < length:
         key_list=[]
    for i in range(length):
         if word_list[i] == ' ':
              key_list.append(' ')
         else:
            key_list.append(key_list_main[k])
            k=k+1
            if k>= len(key):
                 k=0            
    new_word_list = []
     

    for i in range(length):
         if word_list[i] == ' ':
             new_word_list.append(' ')
         
         else:
             letter_1 = word_list[i] 
             letter_2 = key_list[i]
             index_1 = alfabe.index(letter_1)
             index_2 = alfabe.index(letter_2)
             letter = table[index_1][index_2]
             new_word_list.append(letter)

    new_word = ''.join(new_word_list)
    print("The Vigenere Encryption Method equivalent of the word you entered: " + new_word)

if sec == 5 and language ==2:
    table = []
    for i in range(len(alfabe)):
         row = []
         for j in range(len(alfabe)):
             row.append(alfabe[(i + j) % len(alfabe)])
         table.append(row)

    # Vigenère tablosu oluşturuldu

    word = input("Cümleyi giriniz: ")
    key = input("Anahtar kelimeyi yazınız: \n(Anahtar birden fazla kelimeden oluşuyorsa lütfen arada boşluk bırakmadan peşpeşe yazın.) ")

    length = len(word)   
    key_list_main = list(key)
    key_list = list(key)
    word_list = list(word)
    k=0
    if len(key) < length:
         key_list=[]
    for i in range(length):
         if word_list[i] == ' ':
              key_list.append(' ')
         else:
            key_list.append(key_list_main[k])
            k=k+1
            if k>= len(key):
                 k=0            
    new_word_list = []
     

    for i in range(length):
         if word_list[i] == ' ':
             new_word_list.append(' ')
         
         else:
             letter_1 = word_list[i] 
             letter_2 = key_list[i]
             index_1 = alfabe.index(letter_1)
             index_2 = alfabe.index(letter_2)
             letter = table[index_1][index_2]
             new_word_list.append(letter)

    new_word = ''.join(new_word_list)
    print("Girdiğiniz kelimenin Vigenere Şifreleme Yöntemi'ndeki karşılığı: " + new_word)

if sec == 6 and language ==1:
    table = []
    for i in range(len(alfabe)):
        row = []
        for j in range(len(alfabe)):
            row.append(alfabe[(i + j) % len(alfabe)])
            table.append(row)

    # Vigenère table has been created

    word = input("Enter the cipher: ")
    key = input("Enter the key: \n(If the key consists of more than one word, please write it one after the other without leaving a space in between.) ")
    length = len(word)   
    key_list_main = list(key)
    key_list = list(key)
    word_list = list(word)
    k=0
    if len(key) < length:
        key_list=[]
    for i in range(length):
        if word_list[i] == ' ':
            key_list.append(' ')
        else:
            key_list.append(key_list_main[k])
            k=k+1
            if k>= len(key):
                k=0            
    new_word_list = []
     
    
    for i in range(length):
        if word_list[i] == ' ':
            new_word_list.append(' ')
        
        else:
            letter_1 = word_list[i]
            letter_2 = key_list[i]
            index_1 = alfabe.index(word_list[i])
            index_2 = alfabe.index(key_list[i])
            result = (index_1 -index_2)
            if index_1 -index_2 < 0:
                result=result + xyz

            letter = alfabe[result]
            new_word_list.append(letter)


    new_word = ''.join(new_word_list)
    print("The Vigenere Encryption Method equivalent of the cipher you entered: " + new_word)
    
if sec == 6 and language ==2:
    table = []
    for i in range(len(alfabe)):
        row = []
        for j in range(len(alfabe)):
            row.append(alfabe[(i + j) % len(alfabe)])
            table.append(row)

    # Vigenère tablosu oluşturuldu

    word = input("Şifreyi giriniz: ")
    key = input("Anahtar kelimeyi  yazınız: \n(Anahtar birden fazla kelimeden oluşuyorsa lütfen arada boşluk bırakmadan peşpeşe yazın.) ")
    length = len(word)   
    key_list_main = list(key)
    key_list = list(key)
    word_list = list(word)
    k=0
    if len(key) < length:
        key_list=[]
    for i in range(length):
        if word_list[i] == ' ':
            key_list.append(' ')
        else:
            key_list.append(key_list_main[k])
            k=k+1
            if k>= len(key):
                k=0            
    new_word_list = []
     
    
    for i in range(length):
        if word_list[i] == ' ':
            new_word_list.append(' ')
        
        else:
            letter_1 = word_list[i]
            letter_2 = key_list[i]
            index_1 = alfabe.index(word_list[i])
            index_2 = alfabe.index(key_list[i])
            result = (index_1 -index_2)
            if index_1 -index_2 < 0:
                result=result + xyz

            letter = alfabe[result]
            new_word_list.append(letter)


    new_word = ''.join(new_word_list)
    print("Girdiğiniz şifrenin Vigenere Şifreleme Yöntemi'ndeki karşılığı: " + new_word)
    
if sec == 7 and language ==1 :
     word = input("Enter the message you want to encrypt with the RSA algorithm:")
     new_word_list = []
    
     while(True):
        print("Please enter the numbers p and q, which have to be coprime.")
        p=int(input("p : "))
        q=int(input("q : "))
        if   math.gcd(p,q) == 1:
            n=p*q
            fi=(p-1)*(q-1)
            break
        else :
            print("p and q have to be coprime.Try again !")

     while(True):
         print("phi : ",fi)          
         e= int(input("Enter a number e that satisfies the inequality 1 < e < phi and is coprime to phi:"))
         if   (math.gcd(e,fi)) != 1:
             print("e and phi have to be coprime.Try again !")
         else :
             length = len(word)
             word_list=list(word)
             for i in range (length):
                 an=ord(word_list[i])
                 bn=(((an)**e) %  n)
                 
                 new_word_list.append(str(bn))  
                 new_word_list.append(' ')

             temp=1
             d=0
             while (temp<2) :
                 check = (e*d) % fi  
                 if check == 1:
                     break
                 else:
                     d=d+1   
              
             new_word=' '.join(new_word_list)
             print("The encrypted text according to the RSA method: ",new_word)
             print("The number d to be used as a secret key: ",d)
             break

if sec == 7 and language ==2 :
     word = input("RSA algoritmasıyla şifrelemek istediğiniz mesajı giriniz: ")
     new_word_list = []
    
     while(True):
        print("Aralarında asal olmak üzere p ve q sayılarını sırasıyla giriniz.")
        p=int(input("p : "))
        q=int(input("q : "))
        if   math.gcd(p,q) == 1:
            n=p*q
            fi=(p-1)*(q-1)
            break
        else :
            print("p ve q aralarında asal olmalı.Tekrar deneyin !")

     while(True):
         print("fi : ",fi)          
         e= int(input("1 < e  <  fi eşitsizliğini sağlayan ve fi ile aralarında asal olan bir e sayısı giriniz: "))
         if   (math.gcd(e,fi)) != 1:
             print("e ve fi aralarında asal olmalı.Tekrar deneyin !")
         else :
             length = len(word)
             word_list=list(word)
             for i in range (length):
                 an=ord(word_list[i])
                 bn=(((an)**e) %  n)
             
                 new_word_list.append(str(bn))
                 new_word_list.append(' ') 
                 
             
             temp=1
             d=0
             while (temp<2) :
                 check = (e*d) % fi  
                 if check == 1:
                     break
                 else:
                     d=d+1

             new_word=' '.join(new_word_list)
             print("RSA yöntemine göre şifrelenmiş metin: ",new_word)
             print("Gizli anahtar olarak kullanılacak d sayısı: ",d)
             
             break
            
if sec == 8 and language ==1:
 number_list=[] 
 new_word_list = []

 print("Enter the numbers which encrypted with RSA Method one by one: \n(Press 'enter' after every single number.When the numbers run out, press '0' to break the loop.)")

 numbers=1
 while numbers > 0:
     numbers = int(input("enter the next number: "))
     if numbers < 1:
         break
     else:
         number_list.append(numbers) 

 while(True):
     print("Please enter the numbers p and q, which have to be coprime.")
     p=int(input("p : "))
     q=int(input("q : "))
     if   math.gcd(p,q) == 1:
         n=p*q
         fi=(p-1)*(q-1)
         break
     else :
         print("p and q have to be coprime.Try again !")


 d=int(input("Enter the number d: "))


 length=len(number_list)

 for i in range (length):
    
     bn=int(number_list[i])
     decripted_number= (bn**d) % n
     letter= chr(decripted_number)
     new_word_list.append(letter)
         


 new_word = ''.join(new_word_list)
 print("The RSA Encryption equivalent of the number you entered for the q, p, e, fi values ​​you entered: ",new_word)

     

if sec == 8 and language ==2:
 number_list=[]
 new_word_list = []

 print("RSA yöntemiyle şifrelenmiş mesajın sayılarını sıra sıra giriniz: \n(Her girdiğiniz sayıdan sonra enter'a basınız.Sayılar bittiğinde döngüyü kırmak için '0'ı tuşlayınız.)")

 numbers=1
 while numbers > 0:
     numbers = int(input("sıradaki sayıyı giriniz: "))
     if numbers < 1:
         break
     else:
         number_list.append(numbers) 

 while(True):
     print("Aralarında asal olmak üzere p ve q sayılarını sırasıyla giriniz.")
     p=int(input("p : "))
     q=int(input("q : "))
     if   math.gcd(p,q) == 1:
         n=p*q
         fi=(p-1)*(q-1)
         break
     else :
         print("p ve q aralarında asal olmalı.Tekrar deneyin !")


 d=int(input("d sayısını giriniz: "))

 
 length=len(number_list)

 for i in range (length):
    
     bn=int(number_list[i])
     decripted_number= (bn**d) % n
     letter= chr(decripted_number)
     new_word_list.append(letter)
         

 
 new_word = ''.join(new_word_list)
 print("Girdiğiniz sayının,girdiğiniz q,p,e,fi değerleri için RSA Şifrelemesindeki karşılığı: ",new_word)
    

alfabe_morse=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
numbers_morse=['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
united_morse=['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']

if sec == 9 and language ==1 :
   alfabe=alfabe_en
   word=input("Please enter the message you want to convert to morse code: ")
   word_list=[]
   morse_list=[]
   length=len(word)
   word_list=list(word)
   for i in range (length) :
      letter= word_list[i]

      if letter == ' ':
         morse_list.append(' ')

      elif ord(letter)>47 and ord(letter)<58 :
         morse_letter=numbers_morse[int(letter)]
         morse_list.append(morse_letter)
      
      else :
        index=alfabe.index(letter)
        morse_letter= alfabe_morse[index]
        morse_list.append(morse_letter)
  
   morse_message=' '.join(morse_list)
   print("Morse code equivalent of the message you entered: ",morse_message)

if sec == 9 and language ==2 :
   alfabe=alfabe_en
   word=input("Lütfen morse koduna çevirmek istediğiniz mesajı giriniz: ")
   word_list=[]
   morse_list=[]
   length=len(word)
   word_list=list(word)

   for i in range (length) :
      letter= word_list[i]

      if letter == ' ':
         morse_list.append(' ')

      elif ord(letter)>47 and ord(letter)<58 :
         morse_letter=numbers_morse[int(letter)]
         morse_list.append(morse_letter)
      
      else :
        index=alfabe.index(letter)
        morse_letter= alfabe_morse[index]
        morse_list.append(morse_letter)
  
   morse_message=' '.join(morse_list)
   print("Girdiğiniz mesajın morse kodu karşılığı: ",morse_message)        
      

if sec == 10 and language ==1 :
   alfabe=alfabe_en
   morse_code=input("Enter the Morse code you want to translate into English by adding a space at the end of each Morse letter and adding an extra space when you want to leave a space:")
   length=len(morse_code)
   morse_list=list(morse_code)
   temp_list=[]
   letter_list=[]
   word_list=[]

   for i in range (length):
      if morse_list[i] == '.' or morse_list[i] == '-':
         temp_list.append(morse_list[i])
      elif morse_list[i] == ' ' and len(temp_list) != 0:
        morse_letter=''.join(temp_list)
        temp_list.clear()
        index=united_morse.index(str(morse_letter))
        if index < 10:
           word_list.append(index)
        else:
           index = index-10
           word_list.append(alfabe[index])
   
      elif morse_list[i] == ' ' and len(temp_list) == 0:
         word_list.append(' ')
      else:
         print("When writing morse code,please use only '.','-',' '.")
   
   
   word=''.join(word_list)
   print("The Morse code you entered is translated into English: ",word)

if sec == 10 and language ==2 :
   alfabe=alfabe_en
   morse_code=input("Türkçeye çevirmek istediğiniz morse kodunu her morse harfinin sonuna boşluk ekleyerek ve boşluk bırakmak istediğinizde ekstra boşluk ekleyerek giriniz: ")
   length=len(morse_code)
   morse_list=list(morse_code)
   temp_list=[]
   letter_list=[]
   word_list=[]

   for i in range (length):
      if morse_list[i] == '.' or morse_list[i] == '-':
         temp_list.append(morse_list[i])
      elif morse_list[i] == ' ' and len(temp_list) != 0:
        morse_letter=''.join(temp_list)
        temp_list.clear()
        index=united_morse.index(str(morse_letter))
        if index < 10:
           word_list.append(index)
        else:
           index = index-10
           word_list.append(alfabe[index])
   
      elif morse_list[i] == ' ' and len(temp_list) == 0:
         word_list.append(' ')
      else:
         print("morse kodu yazarken yalnızca '.','-',' ' kullanınız.")
   
   
   word=''.join(word_list)
   print("Girdiğiniz morse kodunun Türkçe'ye çevrilmiş hali: ",word)

#if sec == 11 and language ==1 : #AES (Advanced Encryption Standard)


#if sec == 11 and language ==2 : #AES (Advanced Encryption Standard)







    

      
     

  
    


