#Random matching of ascii characters for range of [33, 125]
import random
def randmatch(lst1 = [chr(a) for a in range(33, 126)]): 
        dc, not_rept_lst= {}, []
        while len(dc) != len(lst1):
                indx = random.randrange(len(lst1))
                if indx not in not_rept_lst:
                    not_rept_lst.append(indx)
                    dc[lst1[len(not_rept_lst)-1]] = lst1[indx]
        return dc
cnt = int(input('How many rotors you want to creat?'))
rotors = list(randmatch() for _ in range(cnt)) #Creating list of dictionaries
print(rotors)
'''
f = open('C:/Users/1954513/Desktop/PythonOut.txt', mode = 'w')
for K in rotors:
        s = '{'
        for k, v in K.items():
                s = f'{k}: {v}'
                f.write(s)
        f.write('}\n')
f.close()
'''
'''
def test_if_has_my_password_characters(entered_your_password, lst = lst_2):
    for x in entered_your_password:
        if x not in lst:
            return 'Hey! Issue'
    return 'We are good to go!'
K = input()
print(test_if_has_my_password_characters(K))
for k in lst:
    print(k)
for u in lst_2:
    print(u)
'''

