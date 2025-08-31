import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ""

print("Сколько паролей вам нужно сгенерировать?")
kolvo = int(input())
print("Какая длина будет у пароля(ей)")
dlina = int(input())
print("Включать ли в пароль(и) цифры? (Y - yes, N - no)")
numbers = input()
print("Включать ли в пароль(и) прописные буквы? (Y - yes, N - no)")
prop_b = input()
print("Включать ли в пароль(и) строчные буквы? (Y - yes, N - no)")
stok_b = input()
print("Включать ли в пароль(и) символы, например: @? (Y - yes, N - no)")
simv = input()
print(
    "Исключить ли из пароля(ей) неоднозначиные символы, например: i, l, 1, L? (Y - yes, N - no)"
)
neod = input()


if numbers.lower() == "y":
    chars += digits
if prop_b.lower() == "y":
    chars += uppercase_letters
if stok_b.lower() == "y":
    chars += lowercase_letters
if simv.lower() == "y":
    chars += punctuation
if neod.lower() == "y":
    for c in "il1Lo0O":
        chars = chars.replace(c, "")

again = ""
while again.lower() != "n":
    for i in range(kolvo):
        res = random.sample(chars, dlina)
        print(*res, sep="")
    print("Сгенерировать еще пароль(и)? (Y - yes, N - no)")
    again = input()

print("До новых встреч!")
