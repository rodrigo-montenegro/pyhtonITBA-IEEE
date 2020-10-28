"""
Ejemplos:

traducir( "𐌀𐌋𐌅𐌀𐌁𐌄𐌕𐌏" ) => "ALFABETO"

traducir( "¡𐌐𐌄𐌓𐌃𐌉!" ) => "¡PERDI!

traducir( "¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉." ) => "¿SI O NO? MMM... SI."
"""

alfabeto = {
    '𐌀': 'A',
    '𐌁': 'B',
    '𐌂': 'C',
    '𐌃': 'D',
    '𐌄': 'E',
    '𐌅': 'F',
    '𐌆': 'Z',
    '𐌇': 'H',
    '𐌉': 'I',
    '𐌊': 'K',
    '𐌋': 'L',
    '𐌌': 'M',
    '𐌍': 'N',
    '𐌏': 'O',
    '𐌐': 'P',
    '𐌒': 'Q',
    '𐌓': 'R',
    '𐌔': 'S',
    '𐌕': 'T',
    '𐌖': 'V',
    '𐌗': 'X'}


def traducir(frase):
    traduccion = ""
    for x in frase:
        if x in alfabeto:
            contenido = alfabeto.get(x)
            traduccion = traduccion + contenido
        else:
            traduccion = traduccion + x
    return str(traduccion)


print(traducir("¡𐌐𐌄𐌓𐌃𐌉!"))
print(traducir("¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉."))
