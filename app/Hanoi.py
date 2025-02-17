def hanoi(n, origen, dest, aux):
    if n == 1:
        print(f"Mover disco {n} de {origen} al {dest}")
        return

    hanoi( n-1, origen, aux, dest)
    print(f"Mover disco {n} de {origen} al {dest}")
    hanoi(n-1, aux, dest, origen)

hanoi(5, "A","B", "C")