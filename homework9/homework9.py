import re
mail = 'danil.shtus3232@mail.ru'
p=mail[0]
pos=mail[-1]
s='r'
if p.isdigit() or p in '.-_' or pos in '.-_':
    print('Почта не может начинаться или заканчиваться с цифры, тире, точки и подчеркивания')
elif '@' not in mail or '.' not in mail:
    print('Введенная строка не почта')
elif ' ' in mail:
    print('В почте не может быть пробелов')
elif mail.count('@')>1:
    print('В почте не может быть больше одной @')
else:
    for i in range(len(mail)):
        if s[-1]=="g" and mail[i]=='.':
            print('Указанные вами данные не могут быть почтой')
            F=False
            break
        elif mail[i]=="@":
            s+='g'
        elif mail[i]==".":
            s+='T'
        elif mail[i]=="-":
            s+='t'
        elif mail[i]=="_":
            s+='p'
        else:
            if s[-1]=="r":
                continue
            else:
                s+='r'
        F=True
    if F:
        a=s.replace('r', '(\\w+)').replace('T', '\\.').replace('t', '\\-').replace('p', '\\_').replace('g', '\\@')
        print("Наша почта в регулярном представлении", a) 
        res=re.search(a, mail)
        #print(res) использовалось для проверки
        prov=re.split('\\@', a)
        #print(prov)
        #print(prov[0])
        #print(prov[-1])
        username=prov[0][:-1]
        user=re.search(username, mail)
        print(f"Наш username:{user}")
        doma='\\@'+prov[-1]
        domain=re.search(doma, mail)
        domainn=str(domain)
        domainnn=domainn.replace('@', '')
        print(f"Наш домен: {domainnn}")