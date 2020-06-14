#Exam Soal No 1
def Hashtag(string):
    kalimat = []
    string1 = string.split()
    for a in string1:
            kalimat.append(a.capitalize())
    n = ''.join(kalimat)
    if len(n) > 140 or len(n) == 0:
        print(False)
    else:
        print(f'#{n}')

Hashtag('hellO WorLd how are you doing')

#Exam Soal No 2
def create_phone_number(n):
    
            if len(n) <= 10 and len(n) == 10:
                for i in n:
                    if type(i) == int:
                        phone1 = str(n[0]) + str(n[1]) + str(n[2])
                        phone2 = str(n[3]) + str(n[4]) + str(n[5])
                        phone3 = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
                        
                        
                    

                    else:
                        return False
                print(f'({phone1}) {phone2}-{phone3}')
            else:
                print('invalid input')
                  
            
           
    

        
   
        
create_phone_number([1, 2, 3, 4, 5,6 ,7, 8, 9, 0])

#Exam Soal No 3
def sort_odd_even(b):
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            if b[i]%2 == 1 and b[j]%2 == 1:
                if b[i] > b[j]:
                    temp = b[i]
                    b[i] = b[j]
                    b[j] = temp
            elif b[i]%2 == 0  and b[j]%2 == 0 or b[i] == 0:
                if b[i] < b[j]:
                    temp = b[i]
                    b[i] = b[j]
                    b[j] = temp
            elif b == '':
                return b
            
            
            
    print(b)

sort_odd_even([5, 3, 2, 8, 1, 4])