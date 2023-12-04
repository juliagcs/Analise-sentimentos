from functools import reduce
import re

# le os arquivos
data = open('2022-10-17-MXRF11.json', 'r')

# filtra o texto relevante do json
text_ids = re.findall(r'"text": "(.*?)"', data.read())

# caracteres para decodificar
subs = {
        '\\n':'\n',
        '\\u00e3':'ã',
        '\\u00e1':'á',
        '\\u00e9':'é',
        '\\u00ea':'ê',
        '\\u00ed':'í',
        '\\u00f3':'ó',
        '\\u00f5':'õ',
        '\\u00fa':'ú',
        '\\u00e7':'ç',
        '\\u201c':'“',
        '\\u201d':'”',
        '\\u2019':'’',
        '\\u00b2':'²',
        '\\u2022':'•',
        '\\u00ba':'º',
        '\\u2026':'…',
        '\\ud83d\\udd34':'🔴',
        '\\ud83d\\udfe2':'🟢',
        '\\u26aa\\ufe0f':'⚪',
        '\\ud83c\\udfe2':'🏢',
        '\\ud83d\\udcc9':'📉',
        '\\ud83d\\udcb0':'💰',
        '\\ud83d\\udc47':'👇',
        '\\ud83c\\udffb':'🏻',
        '\\ud83c\\udfed':'🏭',
        '\\ud83c\\udf07':'🌇',
        '\\u2b06\\ufe0f':'⬆️',
        '\\u2b07\\ufe0f':'⬇️',
        '\\ud83d\\udd25':'🔥',
        '\\ud83d\\udce1':'📡',
        '\\ud83d\\ude33':'😳',
        '\\ud83e\\udd11':'🤑',
        '\\ud83d\\udcca':'📊',
        '\\ud83c\\udffc':'🏼',
        '\\ud83d\\udccc':'📌',
        '\\ud83d\\udcc8':'📈',
        '\\ud83d\\ude2c':'😬',
        '\\ud83d\\udc94':'💔',
        '\\ud83e\\udd23':'🤣',
        '\\ud83e\\udd14':'🤔',
        '\\ud83d\\udc80':'💀',
        '\\u23f3':'⏳',
        '\\u2705':'✅',
        }

def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

# printar
for text in text_ids:
    print(multiple_replace(text, subs))
