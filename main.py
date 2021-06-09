from Igrac import Igrac
from Ploca import Ploca
from Brod import Brod
import os


def has_lost(i1):
    for row in i1.mainPloca.arr:
        for value in row:
            if value == 1:
                return 0
    return 1


def main():
    ltr_2_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    arr1 = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    arr2 = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    p1 = Ploca(arr1)
    p2 = Ploca(arr2)

    i1 = Igrac(input("Ime Prvog Igraca: "), p1)
    i2 = Igrac(input("Ime Drugog Igraca: "), p2)

    for igrac in [i1, i2]:
        for brod in igrac.brodovi:
            coords = []
            print(igrac.mainPloca)
            while True:
                #   Igrac unosi koordinatu za postavljanje broda na plocu
                brod_coord = input(f"[{igrac.name}] Postavi brod ({brod.length}) {brod}: ")
                if len(brod_coord) > 2 or len(brod_coord) < 1:
                    print("Krivi unos, pokusajte ponovo")
                    continue
                try:
                    num_y = ltr_2_num.get(brod_coord[0])
                except:
                    print("Krivi unos, pokusajte ponovo")
                    continue
                try:
                    num_x = int(brod_coord[1])
                except:
                    print("Krivi unos, pokusajte ponovo")
                    continue
                if 0 > num_x or num_x > 7:
                    print("Krivi unos, pokusajte ponovo")
                    continue

            #   TODO: popravi overlappanje brodova

                #   Igrac unosi smjer (orijentaciju) broda
                smjer = input("[H]orizontalno ili [O]komito: ")
                if smjer.upper() == "H":
                    if num_y + brod.length > 8:
                        print("Tu se brod ne moze postaviti")
                        continue
                    for n in range(brod.length):
                        igrac.mainPloca.arr[num_x][num_y+n] = 1
                        coords.append((num_x, num_y+n))
                    brod.coords = coords

                elif smjer.upper() == "O":
                    if num_x + brod.length > 8:
                        print("Tu se brod ne moze postaviti")
                        continue
                    for n in range(brod.length):
                        igrac.mainPloca.arr[num_x + n][num_y] = 1
                        coords.append((num_x + n, num_y))
                    brod.coords = coords
                else:
                    print("Krivi unos, pokusajte ponovo")
                    continue
                break

    otherPlayer = i1
    currentPlayer = i2

    while True:
        print(otherPlayer)
        print(currentPlayer.guessPloca)
        print()
        print(currentPlayer)
        print(currentPlayer.mainPloca)

        coord = input("Unesi koordinatu: ")

        #   Veliki blok sinteze input-a
        if 1 > len(coord) or len(coord) > 2:
            print("Krivi unos, pokusajte ponovo")
            input("Pritisnite neku tipku za nastavak...")
            continue

        try:
            num_y = ltr_2_num[coord[0]]
        except:
            print("Krivi unos, pokusajte ponovo")
            input("Pritisnite neku tipku za nastavak...")
            continue

        try:
            num_x = int(coord[1])
        except ValueError:
            print("Krivi unos, pokusajte ponovo")
            input("Pritisnite neku tipku za nastavak...")
            continue
        if 0 > num_x or num_x > 7:
            print("Krivi unos, pokusajte ponovo")
            input("Pritisnite neku tipku za nastavak...")
            continue

        #   Testira se tablica protivnika za pogodak
        hit = otherPlayer.mainPloca.guess_hit(num_x, num_y)
        if hit < 0:
            print("Mjesto je vec pogodeno, pokusajte ponovo:")
            input("Pritisnite neku tipku za nastavak...")
            continue

        #   Rezultat pogotka se zrcali na nasoj tablici pogadanja
        currentPlayer.guessPloca.set_hit(num_x, num_y, hit)

        if hit != 2:
            #   Ako je promasaj mijanju se strane
            print(">>>MISS<<<")
            igrac = currentPlayer
            currentPlayer = otherPlayer
            otherPlayer = igrac
        else:
            #   Ako je pogodak, igrac koji je pogodio nastavlja igru
            print(">>>HIT<<<")

        #   Za lakse citanje rezultata
        input("Pritisnite neku tipku za nastavak...")

        #   Ocistiti konzolu
        clear = lambda: os.system('cls')
        clear()

        #   Trenutni win condition (ako jedan od igraca ima nula jedinica u svojoj main Ploci)
        if has_lost(i1):
            print(f"Igrac {i2.name} je pobjednik!")
            break
        elif has_lost(i2):
            print(f"Igrac {i1.name} je pobjednik!")
            break


if __name__ == '__main__':
    main()
