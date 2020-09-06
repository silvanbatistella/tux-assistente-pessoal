from os import getcwd

import yaml


def carregar_configs(caminho_projeto):
    caminho_projeto = get_caminho_projeto(caminho_projeto)
    with open(f'{caminho_projeto}/config/config.yaml') as arquivo:
        configs = yaml.load(arquivo, Loader=yaml.FullLoader)
        arquivo.close()
        return configs


def get_caminho_projeto(caminho_projeto):
    if 'tux' in caminho_projeto:
        tamanho_caminho = len(caminho_projeto)
        posicaotux = caminho_projeto.index('/tux') + 4
        if tamanho_caminho != posicaotux:
            caminho_projeto = caminho_projeto[0: caminho_projeto.index('/tux') + 4]
        return caminho_projeto
    return ''


class Config:

    def __init__(self, caminho_projeto=getcwd()):
        self.__configs = carregar_configs(caminho_projeto)
        self.__existe_config()

    def __existe_config(self):
        if not self.__configs['PATH']:
            self.__configs['PATH'] = get_caminho_projeto()
            arquivo = open('./config/config.yaml', 'w')
            yaml.dump(self.__configs, arquivo)
            arquivo.close()

    def get_propriedade(self, propriedade: str):
        if propriedade in self.__configs:
            return self.__configs[propriedade]
        else:
            return ''


def init():
    config = Config(getcwd())
    print(config.get_propriedade('PATH'))


if __name__ == '__main__':
    init()
