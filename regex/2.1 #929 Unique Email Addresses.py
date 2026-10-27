# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: se recorre la lista emails una sola vez (solo es un for)
#se va guardando cada email y en cada iteracion se guarda solo nom y dominio, po lo que es lineal 
class Solution:
    import re
    def numUniqueEmails(self, emails: list[str]) -> int:
        correos=set()
        for n in emails:

            separada =re.split(r'\@',n)
            nombre = separada[0]
            nom = re.sub(r'\.','',nombre)
            nom = re.split(r'\+',nom)
            nom = nom[0]
            
            dominio=separada[1]

            ncorreo = nom+'@'+dominio
            correos.add(ncorreo)

        return(len(correos))