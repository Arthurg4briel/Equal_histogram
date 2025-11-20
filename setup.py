from setuptools import setup, find_packages

setup(
    name='projeto_equalizacao',
    version='0.1.0',
    description='Um pacote para aplicar equalização de histograma em imagens.',
    
    # Encontra automaticamente todos os pacotes (pastas com __init__.py)
    packages=find_packages(exclude=['tests', 'assets']),
    
    # Lista as dependências
    install_requires=[
        'numpy',
        'opencv-python',
    ],
    
    # Permite executar o main.py como um comando
    entry_points={
        'console_scripts': [
            'run_equalizacao=main:run',
        ],
    }
)