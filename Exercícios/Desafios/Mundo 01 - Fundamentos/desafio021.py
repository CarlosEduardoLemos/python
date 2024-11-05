import pygame
import os

try:
    pygame.init()
    print("Pygame inicializado com sucesso.")
    
    pygame.mixer.init()
    print("Mixer inicializado com sucesso.")
    
    music_file = 'loveofmylife.mp3'
    if not os.path.isfile(music_file):
        raise FileNotFoundError(f"Arquivo {music_file} não encontrado no diretório de trabalho.")
    
    pygame.mixer.music.load(music_file)
    print("Arquivo de música carregado com sucesso.")
    
    pygame.mixer.music.play()
    print("Reprodução da música iniciada.")
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
except pygame.error as e:
    print(f"Erro ao carregar ou reproduzir a música: {e}")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
