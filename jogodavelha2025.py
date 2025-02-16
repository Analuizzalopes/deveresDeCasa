def desenhar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True
    
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    
    return False

def jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogadores = ['X', 'O']
    jogadas = 0
    
    while jogadas < 9:
        desenhar_tabuleiro(tabuleiro)
        jogador_atual = jogadores[jogadas % 2]
        print(f"Vez do jogador {jogador_atual}")
        
        try:
            linha = int(input("Digite a linha (0, 1, 2): "))
            coluna = int(input("Digite a coluna (0, 1, 2): "))
            
            if tabuleiro[linha][coluna] != ' ':
                print("Posição já ocupada! Tente novamente.")
                continue
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1
            
            if verificar_vitoria(tabuleiro, jogador_atual):
                desenhar_tabuleiro(tabuleiro)
                print(f"PARABÉNS, {jogador_atual}! Você venceu!")
                return
        except (ValueError, IndexError):
            print("Entrada inválida! Digite um número entre 0 e 2.")
            continue
    
    desenhar_tabuleiro(tabuleiro)
    print("VELHA! O jogo empatou.")

if __name__ == "__main__":
    jogo_da_velha()