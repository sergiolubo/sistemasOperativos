procesos = [
    {"pid": "P1", "llegada": 0, "rafaga": 8},
    {"pid": "P2", "llegada": 1, "rafaga": 4},
    {"pid": "P3", "llegada": 2, "rafaga": 9},
    {"pid": "P4", "llegada": 3, "rafaga": 5},
]

def fcfs(lista):
    tiempo = 0
    resultado = []

    for p in sorted(lista, key=lambda x: x["llegada"]):
        if tiempo < p["llegada"]:
            tiempo = p["llegada"]
        inicio = tiempo
        fin = tiempo + p["rafaga"]
        espera = inicio - p["llegada"]
        retorno = fin - p["llegada"]
        resultado.append({
            "pid": p["pid"],
            "inicio": inicio,
            "fin": fin,
            "espera": espera,
            "retorno": retorno
        })
        tiempo = fin
    return resultado

def round_robin(lista, quantum):
    tiempo = 0
    cola = []
    procesos_restantes = [
        {"pid": p["pid"], "llegada": p["llegada"], "restante": p["rafaga"], "rafaga": p["rafaga"]}
        for p in lista
    ]

    completados = {}
    gantt = []

    while procesos_restantes or cola:
        for p in procesos_restantes[:]:
            if p["llegada"] <= tiempo:
                cola.append(p)
                procesos_restantes.remove(p)

        if not cola:
            tiempo += 1
            continue

        actual = cola.pop(0)
        ejecucion = min(quantum, actual["restante"])
        inicio = tiempo
        tiempo += ejecucion
        actual["restante"] -= ejecucion

        gantt.append((actual["pid"], inicio, tiempo))

        for p in procesos_restantes[:]:
            if p["llegada"] <= tiempo:
                cola.append(p)
                procesos_restantes.remove(p)

        if actual["restante"] > 0:
            cola.append(actual)
        else:
            completados[actual["pid"]] = tiempo

    resultado = []
    for p in lista:
        fin = completados[p["pid"]]
        retorno = fin - p["llegada"]
        espera = retorno - p["rafaga"]
        resultado.append({
            "pid": p["pid"],
            "fin": fin,
            "espera": espera,
            "retorno": retorno
        })

    return resultado, gantt

print("=== FCFS ===")
r_fcfs = fcfs(procesos)
for r in r_fcfs:
    print(r)

print("\n=== Round Robin, quantum = 3 ===")
r_rr, gantt = round_robin(procesos, 3)
for r in r_rr:
    print(r)

print("\nDiagrama de ejecución Round Robin:")
for item in gantt:
    print(item)
