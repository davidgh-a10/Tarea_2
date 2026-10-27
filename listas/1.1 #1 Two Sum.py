# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: se recorre la lista nums una sola vez(solo es un for)
# solo se va guardando cada indice de cada elemento recorrido
class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
         
        numeros = {}
    
        for i,n in enumerate(nums):
            complemento = target - n
        
            if complemento in numeros:
                return [numeros[complemento], i]
              
            numeros[n] = i

        return[]