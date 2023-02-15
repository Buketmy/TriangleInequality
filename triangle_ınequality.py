kenarlar = "kenar_a", "kenar_b", "kenar_c"
kenar_a = int(input("a:"))
kenar_b = int(input("b:"))
kenar_c = int(input("c:"))
ücgen = kenar_a < kenar_b + kenar_c or kenar_b < kenar_a + kenar_c or kenar_c < kenar_a + kenar_b and kenarlar < 0
def triangle():
    if kenar_a == kenar_b == kenar_c and ücgen:
        print("Eşkenar Üçgen")
    elif kenar_a != kenar_b != kenar_c and ücgen:
        print("Çeşitkenar Üçgen")
    elif ücgen:
        print("İkizkenar Üçgen")
triangle()