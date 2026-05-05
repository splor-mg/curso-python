from pathlib import Path

path = Path('aulas/034/ecommerce')
for arquivo in path.glob('*.py'):
    print(arquivo)