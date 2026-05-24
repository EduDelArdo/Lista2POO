from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo: str, duracao: int):
        self.titulo = titulo
        self.duracao = duracao  # Duracao em minutos

    def mostrar_info(self):
        print(f"Mídia: {self.titulo} ({self.duracao} min)")

    @abstractmethod
    def reproduzir(self):
        pass

class Video(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"Reproduzindo vídeo '{self.titulo}' na resolução {self.resolucao}...")

class Podcast(Midia):
    def __init__(self, titulo: str, duracao: int, apresentador: str):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self):
        print(f"Tocando podcast '{self.titulo}', apresentado por {self.apresentador}...")

class TextoNarrado(Midia):
    def __init__(self, titulo: str, duracao: int, narrador: str):
        super().__init__(titulo, duracao)
        self.narrador = narrador

    def reproduzir(self):
        print(f"Lendo texto '{self.titulo}', narrado por {self.narrador}...")
class Plataforma:
    def __init__(self):
        self.catalogo = []

    def adicionar_midia(self, midia: Midia):
        self.catalogo.append(midia)
        print(f"'{midia.titulo}' adicionado à plataforma.")

    def reproduzir_todas(self):
        print("\n---  INICIANDO REPRODUÇÃO EM MASSA ---")
        for midia in self.catalogo:
            midia.mostrar_info()  
            midia.reproduzir()  
            print("-" * 40)

# --- Área de Testes ---
if __name__ == "__main__":
    netflix_da_ufam = Plataforma()

    # Criando as mídias
    aula_poo = Video("Classe abstrata", 45, "1080p")
    DevCast = Podcast("POO", 60, "Prof. Alternei")
    audiobook = TextoNarrado("Naruto  - Capítulo 1", 20, "Voz do Google")


    netflix_da_ufam.add_midia = netflix_da_ufam.adicionar_midia(aula_poo)
    netflix_da_ufam.add_midia = netflix_da_ufam.adicionar_midia(DevCast)
    netflix_da_ufam.add_midia = netflix_da_ufam.adicionar_midia(audiobook)

    # Executando o polimorfismo
    netflix_da_ufam.reproduzir_todas()

