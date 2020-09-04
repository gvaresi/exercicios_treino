import requests
# from setuptools.build_meta import get_requires_for_build_wheel


def buscar_avatar(usuario):
    """
    Busca um avatar no git hub
    :param usuario: str com  nome do usuario
    :return: str link avatar do usuario
    """

    url = f'https://api.github.com/users/{usuario}'
    resul = requests.get(url)
    return resul.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar(input('digite o usuario github')))
