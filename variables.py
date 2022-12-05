# L'opérateur d'affectation = permet d'injecter une valeur dans une variable.
foo = "lorem ipsum"
# Affectation de valeur à partir d'une variable
bar = foo
print(bar)

my_number1 = 123
my_number2 = -42

print(my_number1)
print(my_number2)

my_text1 = "Ceci est une chaîne de caractères"
my_text2 = 'Ceci est aussi une chaîne de caractères'

print(my_text1)
print(my_text2)


# Exercice

a = 123
b = 42

a,b = b, a
print(a, b)

a = 123
b = 42
#---------------------------------------------



# Variante qui ne marche qu'avec des nombres.
c = a + b
a = c - a
b = c - b
print(a, b)