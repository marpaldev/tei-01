def saudacao(nome: str, repet: int = 0) -> str:
    if not repet == 0:
        r = 0
        while r < repet:
            print(f"Olá, {nome}. Bem-vindo ao programa.")
            r += 1
    else:
        print(f"Olá, {nome}. Bem-vindo ao programa.")

if __name__ == "__main__":
    saudacao("Mundo", 5)