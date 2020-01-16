import string

r1=r2=r3='E'
r4=r5=r6='T'
r7=r8=r9='F'

class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def tokenize_string(data):
    digits = '0123456789'
    buf = ['']
    last = 'c'
    for el in data:
        if ((el in string.ascii_letters) or (el in digits)) and (last == 'c'):
            buf[-1] += el
        else:
            buf.append(el)
            last = 'n'
            if ((el in string.ascii_letters) or (el in digits)):
                last = 'c'
    if buf[0]=='':
      buf.remove('')
    data = buf
    return data

def id_or_num(string):
  try:
    float(string)
    return 'num'
  except ValueError:
    return 'id'

def switch(s):
    if s=='+' or s=='-' or s=='*' or s=='/' or s=='(' or s==')' or s=='$':
        return s
    else:
        return id_or_num(s)

tabl={('0','id'):'S5',('4','id'):'S5',('7','id'):'S5',('8','id'):'S5',('9','id'):'S5',('10','id'):'S5',
('0','num'):'S6',('4','num'):'S6',('7','num'):'S6',('8','num'):'S6',('9','num'):'S6',('10','num'):'S6',
('1','+'):'S7',('2','+'):'r3',('3','+'):'r6',('5','+'):'r7',('6','+'):'r8',('11','+'):'r1',('12','+'):'r2',('13','+'):'r4',('14','+'):'r5',('15','+'):'S7',('16','+'):'r9',
('1','-'):'S8',('2','-'):'r3',('3','-'):'r6',('5','-'):'r7',('6','-'):'r8',('11','-'):'r1',('12','-'):'r2',('13','-'):'r4',('14','-'):'r5',('15','-'):'S8',('16','-'):'r9',
('2','*'):'S9',('3','*'):'r6',('5','*'):'r7',('6','*'):'r8',('11','*'):'S9',('12','*'):'S9',('13','*'):'r4',('14','*'):'r5',('16','*'):'r9',
('2','/'):'S10',('3','/'):'r6',('5','/'):'r7',('6','/'):'r8',('11','/'):'S10',('12','/'):'S10',('13','/'):'r4',('14','/'):'r5',('16','/'):'r9',
('0','('):'S4',('4','('):'S4',('7','('):'S4',('8','('):'S4',('9','('):'S4',('10','('):'S4',
('2',')'):'r3',('3',')'):'r6',('5',')'):'r7',('6',')'):'r8',('11',')'):'r1',('12',')'):'r2',('13',')'):'r4',('14',')'):'r5',('15',')'):'S16',('16',')'):'r9',
('1','$'):'accept',('2','$'):'r3',('3','$'):'r6',('5','$'):'r7',('6','$'):'r8',('11','$'):'r1',('12','$'):'r2',('13','$'):'r4',('14','$'):'r5',('16','$'):'r9',
('0','E'):'1',('4','E'):'15',
('0','T'):'2',('4','T'):'2',('7','T'):'11',('8','T'):'12',
('0','F'):'3',('4','F'):'3',('7','F'):'3',('8','F'):'3',('9','F'):'13',('10','F'):'14'}
stack=Stack()
stack.push('0')
lenta=tokenize_string(input("Введите строку\n"))
lenta.append('$')
list_rule=[]
while 10>0:
    char=stack.pop()
    TOKEN=switch(lenta[0])
    try:
        rule=tabl[(char,TOKEN)]
        if rule[0]=='S':
            lenta.remove(lenta[0])
            stack.push(char)
            stack.push(TOKEN)
            stack.push(rule[1:len(rule)])
        elif rule[0]=='r':
            r=0
            if rule[1]=='1' or rule[1]=='2' or rule[1]=='4' or rule[1]=='5' or rule[1]=='9':
                i=0
                while i<5:
                    stack.pop()
                    i=i+1
                if rule[1]=='1':
                    r=r1
                    list_rule.append(1)
                elif rule[1]=='2':
                    r=r2
                    list_rule.append(2)
                elif rule[1]=='4':
                    r=r4
                    list_rule.append(4)
                elif rule[1]=='5':
                    r=r5
                    list_rule.append(5)
                elif rule[1]=='9':
                    r=r9
                    list_rule.append(9)
                char=stack.pop()
                stack.push(char)
                stack.push(r)
                stack.push(tabl[(char,r)])
            else:
                if rule[1]=='3':
                    r=r3
                    list_rule.append(3)
                elif rule[1]=='6':
                    list_rule.append(6)
                    r=r6
                elif rule[1]=='7':
                    list_rule.append(7)
                    r=r7
                elif rule[1]=='8':
                    list_rule.append(8)
                    r=r8
                stack.pop()
                char=stack.pop()
                stack.push(char)
                stack.push(r)
                stack.push(tabl[(char,r)])
        elif rule=='accept':
            print('Строка принадлежит грамматике')
            print('Список правил:',list_rule)
            break
    except KeyError:
        print('Ошибка')
        break
input('Нажмите Enter для выхода\n')
