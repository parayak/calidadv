from gtts import gTTS
import os

def main():
    while True:
        # Paso 1: Lee desde el teclado la variable frase
        frase = input("Introduce una frase en español (o 'chao pescao' para salir): ")

        # Paso 3: Si recibe la frase 'chao pescao', el programa termina
        if frase.lower() == 'chao pescao':
            print("¡Hasta luego!")
            break

        # Paso 2: Emite por el altavoz la frase pero en inglés
        # Generamos el archivo de audio en español
        tts_es = gTTS(text=frase, lang='es')
        tts_es.save("temp_es.mp3")

        # Generamos el archivo de audio en inglés (traducción)
        tts_en = gTTS(text=frase, lang='en')
        tts_en.save("temp_en.mp3")

        # Reproducimos el archivo de audio en inglés
        os.system("start temp_en.mp3")  # Esto abrirá el archivo de audio en inglés con el reproductor predeterminado

        # Eliminamos los archivos temporales después de reproducir el audio en inglés
        os.remove("temp_es.mp3")
        os.remove("temp_en.mp3")

if __name__ == "__main__":
    main()
