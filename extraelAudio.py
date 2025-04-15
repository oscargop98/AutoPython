from moviepy.editor import VideoFileClip
import os

def extraer_audio_de_video(video_path, salida_audio_path=None):
    """
    Extrae el audio de un video y lo guarda como archivo MP3.
    
    Parámetros:
        video_path (str): Ruta del archivo de video.
        salida_audio_path (str, opcional): Ruta para guardar el archivo de audio.
                                          Si no se especifica, se usará el mismo nombre
                                          que el video pero con extensión .mp3
    """
    try:
        # Cargar el video
        video = VideoFileClip(video_path)
        
        # Determinar la ruta de salida si no se especifica
        if salida_audio_path is None:
            nombre_base = os.path.splitext(os.path.basename(video_path))[0]
            salida_audio_path = f"{nombre_base}.mp3"
        
        # Extraer el audio y guardarlo
        video.audio.write_audiofile(salida_audio_path)
        
        print(f"Audio extraído correctamente y guardado en: {salida_audio_path}")
        
    except Exception as e:
        print(f"Error al extraer el audio: {e}")
    finally:
        # Cerrar el video para liberar recursos
        if 'video' in locals():
            video.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Reemplaza con la ruta de tu video
    video_entrada = "tu_video.mp4"
    
    # Puedes especificar una ruta de salida o dejar que se genere automáticamente
    audio_salida = "audio_extraido.mp3"
    
    extraer_audio_de_video(video_entrada, audio_salida)