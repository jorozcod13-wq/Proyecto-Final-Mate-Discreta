from combinaciones import combinaciones

assert combinaciones(5, 2) == 10
assert combinaciones(6, 3) == 20
assert combinaciones(4, 1) == 4
assert combinaciones(5, 0) == 1
assert combinaciones(5, 5) == 1
assert combinaciones(0, 0) == 1
assert combinaciones(8, 4) == 70
assert combinaciones(10, 5) == 252

for n, r in [(-1, 0), (5, -1), (3, 4), (2.5, 1)]:
    try:
        combinaciones(n, r)
    except ValueError:
        pass
    else:
        raise AssertionError(
            f"Se esperaba un error para n={n}, r={r}"
        )

print("Todas las pruebas fueron satisfactorias.")

# otros casos de prueba meliiii 