Lesson 2
## string,list,dictionary,truple,set
print (0) 
print('hello Sardar')
#string---text
name = 'Sardar'
type(name)
country = "uzbekistan"
print (country) 
message ='''we are learninig python and and everiyhing film''' 
name = "a'lo"
message = 'uzbekistan\nRepublic'
print(message)
message = 'uzbekistan\tRepublic'
print(message)
message = 'uzbekistan\bRepublic'
print(message)
message = 'uzbekistan\b\bRepublic'
print(message)
country =  'uzbekistan'
#indexing
#slicing

country[1]
country ='uzbekistan'
country[0:5]
country ='uzbekistan'
country [2:50]
country ='uzbekistan'
country [::2]
txt = 'lmaasleitbtui'
txt [::2]
txt = 'lmaasleitbtui'
txt [1::2]
score = 45
message = 'python'

msg * 10
# mutable \ immutable 
name = 'azamat'
name
msg = 'hello Azamat, how are you?'
print(msg)
msg = 'hello {}, how are you?'. format('Sardar')
print(msg)
is =['azamat','akmal','malika','rustam']
for i in is:
    msg = 'hello {},how are you?'.format(i)
    print (msg)
txt = 'my name is {} I am {} developer'.format("husan","sql")
print(txt)
name ="kamron"
tool = "sql"
txt = f'my name is {name} I am {tool} developer'
print(txt)
print = "sfasfasf"

### LIST

ls = [1,2,3,4,5,6,7,8,9]
print(ls[6])
ls.append(10)
ls
ls.insert(0,100)
ls
ls.append(['a','b','c'])
ls
ls =[1,2,3,4]

ls2 =['a','b','c']
ls.append(ls2)
ls
ls.extend(ls2)
ls
list_to_str = ['I','am','python','developer']
msg = ' '.join(list_to_str)
msg
str_to_list = 'I am python developer'
str_to_list.split(' ')
