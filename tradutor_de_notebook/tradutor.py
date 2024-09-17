from deep_translator import GoogleTranslator
import json


# Carregar o arquivo notebook
with open('1 - Sequence to Sequence Learning with Neural Networks.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)
# Inicializar o tradutor
translator = GoogleTranslator(source='auto', target='pt')

# Iterar pelas células e traduzir o texto markdown e os comentários do código
for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown':
        # Traduzir o conteúdo do markdown
        cell['source'] = [translator.translate(line) for line in cell['source']]
    elif cell['cell_type'] == 'code':
        # Traduzir comentários dentro do código
        cell['source'] = [translator.translate(line) if line.strip().startswith('#') else line for line in cell['source']]

# Salvar o notebook traduzido
with open('meu_notebook_traduzido.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=4)





