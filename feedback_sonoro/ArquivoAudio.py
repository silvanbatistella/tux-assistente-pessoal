from os import path


def teste():
    arquivo_audio = ArquivoAudio('/home/batistella/lab/tux/feedback_sonoro/sounds/moeda.mp3')
    print(arquivo_audio.get_path())


class ArquivoAudio:
    def __init__(self, nome_arquivo: str):
        self.__path = nome_arquivo
        if not self.__arquivo_existe():
            self.__set_path('home/batistella/lab/tux/feedback_sonoro/sounds/erro.mp3')

    def __arquivo_existe(self):
        return path.exists(self.get_path())

    def get_path(self):
        return self.__path

    def __set_path(self, caminho: str):
        self.__path = caminho


if __name__ == '__main__':
    teste()
