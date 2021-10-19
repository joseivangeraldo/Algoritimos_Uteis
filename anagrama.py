##Anagrama  duas palavras distintas que 
#possuem as mesmas letras.
'''
A função pega duas palavras como entrada,
depois ordena as letras através do método
sorted, aí compara as duas se forem iguais
Retorna True caso contrário retorna False
'''
def anagrama (s1,s2):
  s1=sorted (s1)
  s2=sorted (s2)
  if s1 == s2:
    return True
  else:
    return False

s1='marrocos'
s2='socorram'
anagrama(s1,s2)
