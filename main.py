import csv
import json
from datetime import datetime

LIMITE_SUSPEITO = 10000.00

def ler_transacoes(nome_arquivo):
    try:
        with open(nome_arquivo, encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            return list(leitor)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []

def validar_transacao(linha):
    try:
        id_transacao = int(linha["id"])

        cliente = linha["cliente_id"].strip()
        if cliente == "":
            return None

        data = datetime.strptime(linha["data"], "%Y-%m-%d")

        tipo = linha["tipo"].lower()
        if tipo not in ("credito", "debito"):
            return None

        valor = float(linha["valor"])
        if valor <= 0:
            return None

        return {
            "id": id_transacao,
            "data": data,
            "cliente_id": cliente,
            "tipo": tipo,
            "valor": valor,
            "descricao": linha["descricao"],
            "categoria": linha["categoria"]
        }

    except (ValueError, KeyError):
        return None


def gerar_relatorio(transacoes):
    resumo = {}
    suspeitas = []

    for t in transacoes:

        mes = t["data"].strftime("%Y-%m")

        if mes not in resumo:
            resumo[mes] = {
                "quantidade":0,
                "total_credito":0,
                "total_debito":0,
                "saldo":0,
                "media":0,
                "maior":t["valor"],
                "menor":t["valor"],
                "soma":0
            }

        r = resumo[mes]

        r["quantidade"] += 1
        r["soma"] += t["valor"]

        if t["tipo"] == "credito":
            r["total_credito"] += t["valor"]
        else:
            r["total_debito"] += t["valor"]

        r["maior"] = max(r["maior"], t["valor"])
        r["menor"] = min(r["menor"], t["valor"])

        if t["valor"] > LIMITE_SUSPEITO:
            suspeitas.append(t)

    for r in resumo.values():
        r["saldo"] = r["total_credito"] - r["total_debito"]
        r["media"] = r["soma"] / r["quantidade"]
        del r["soma"]

    return resumo, suspeitas

def exibir_relatorio(resumo, suspeitas, validas, invalidas, datas):

    print("="*40)
    print("RELATÓRIO MENSAL")
    print("="*40)

    print(f"Período: {min(datas).date()} até {max(datas).date()}")
    print(f"Transações válidas: {validas}")
    print(f"Transações inválidas: {invalidas}")

    for mes, r in resumo.items():
        print("\n", mes)
        print(f"Quantidade: {r['quantidade']}")
        print(f"Crédito: R$ {r['total_credito']:.2f}")
        print(f"Débito: R$ {r['total_debito']:.2f}")
        print(f"Saldo: R$ {r['saldo']:.2f}")
        print(f"Média: R$ {r['media']:.2f}")
        print(f"Maior: R$ {r['maior']:.2f}")
        print(f"Menor: R$ {r['menor']:.2f}")

    print("\n===== TRANSAÇÕES SUSPEITAS =====")

    if suspeitas:
        for s in suspeitas:
            print(
                f'ID:{s["id"]} '
                f'Cliente:{s["cliente_id"]} '
                f'Data:{s["data"].date()} '
                f'Valor:R$ {s["valor"]:.2f}'
            )
    else:
        print("Nenhuma transação suspeita encontrada.")


def salvar_json(resumo, validas, invalidas):
    dados = {
        "gerado_em": datetime.now().strftime("%Y-%m-%d"),
        "total_transacoes_validas": validas,
        "total_transacoes_invalidas": invalidas,
        "resumo_mensal": resumo
    }

    with open("relatorio.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)


transacoes_brutas = ler_transacoes("transacoes.csv")

validas = []
invalidas = 0

for linha in transacoes_brutas:
    t = validar_transacao(linha)

    if t:
        validas.append(t)
    else:
        invalidas += 1

resumo, suspeitas = gerar_relatorio(validas)

datas = [t["data"] for t in validas]

exibir_relatorio(
    resumo,
    suspeitas,
    len(validas),
    invalidas,
    datas
)

salvar_json(
    resumo,
    len(validas),
    invalidas
)