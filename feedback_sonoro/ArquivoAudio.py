from os import path

from config import Config


class ArquivoAudio:
    def __init__(self, nome_arquivo: str):
        self.__path = construir_caminho(nome_arquivo)
        if not self.__arquivo_existe():
            self.__set_path(construir_caminho('erro'))

    def __arquivo_existe(self):
        return path.exists(self.get_path())

    def get_path(self):
        return self.__path

    def __set_path(self, caminho: str):
        self.__path = caminho


def construir_caminho(nome_arquivo: str):
    config = Config()
    caminho_aplicacao = config.get_propriedade('PATH')
    return f'{caminho_aplicacao}/feedback_sonoro/sounds/{nome_arquivo}.mp3'


def teste():
    arquivo_audio = ArquivoAudio('moeda')
    print(arquivo_audio.get_path())


if __name__ == '__main__':
    teste()
