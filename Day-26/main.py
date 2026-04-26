import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv") #data is in table format
#read csv through pandas
new_dict={row.letter:row.code for (index, row) in data.iterrows()}
#we are creating a new dict from data in csv using dict comprehension
#here we iterate throw rows using iterrows() new_dict={take row.letter ie from index 0 that row letter which is A
#then  from index 0 that row code hich is Alpha
#thus we get 1st key value as A:Alpha
print(new_dict)

word=input("Enter a word: ").upper()
list_of_nato=[new_dict[letter] for letter in word if letter in new_dict]
print(list_of_nato)
