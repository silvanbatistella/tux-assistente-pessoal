from pygame import mixer

from feedback_sonoro.ArquivoAudio import ArquivoAudio


class FeedbackSonoro:
    def __init__(self, caminho_som: str):
        self.__arquivo_audio = ArquivoAudio(caminho_som).get_path()

    def __get_arquivo_audio(self):
        return self.__arquivo_audio

    def executar(self):
        mixer.init()
        mixer.music.load(self.__get_arquivo_audio())
        mixer.music.play()
        while mixer.music.get_busy():
            continue


def teste():
    feedback_sonoro = FeedbackSonoro('moeda')
    feedback_sonoro.executar()


if __name__ == '__main__':
    teste()
