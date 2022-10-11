filename = ['1.txt', '2.txt', '3.txt']
spisok = []
for fname in filename:
    with open (fname, 'rt', encoding='utf8') as file_object:
        string = file_object.readlines()
        spisok.append(string)
        spisok.sort(key=len)

for string in spisok:
    with open ('4.txt', 'a', encoding='utf8') as content:
        l = len(string)
        content.writelines(f"\n{l}\n")
        content.writelines(string)

      

           