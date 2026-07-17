import random

def gerar_jogos_arquivo(qtd_jogos, numeros_por_jogo, limite_superior, nome_arquivo="jogos.txt"):
    todos_jogos = []
    
    print(f"--- Gerando {qtd_jogos} combinações... ---")
    
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for i in range(qtd_jogos):
            jogo = random.sample(range(1, limite_superior + 1), numeros_por_jogo)
            jogo.sort()
            
            todos_jogos.append(jogo)
            
            jogo_formatado = [f"{num:02d}" for num in jogo]
            
            linha = f"Jogo {i+1:03d}: {', '.join(jogo_formatado)}\n"
            
            arquivo.write(linha)

    print(f"--- Sucesso! Os jogos foram salvos no arquivo '{nome_arquivo}' ---")
    return todos_jogos

if __name__ == "__main__":
    QTD_JOGOS = 10
    NUMS_POR_JOGO = 6
    MAX_NUMERO = 60
    NOME_DO_ARQUIVO = "resultados_loteria.txt"
    
    gerar_jogos_arquivo(QTD_JOGOS, NUMS_POR_JOGO, MAX_NUMERO, NOME_DO_ARQUIVO)