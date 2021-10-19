##Anagrama  duas palavras distintas que 
#possuem as mesmas letras.
'''
A função pega duas palavras como entrada,
depois ordena as letras através do método
sorted, aí compara as duas se forem iguais
Retorna True caso contrário retorna False
'''
def anagrama(s1,s2):
  s1 = s1.replace(' ','').lower() ###retira espaços da palavra
  s2 = s2.replace(' ','').lower() ###retira espaços da palavra

  return sorted(s1) == sorted(s2) ###retorna o resultado logico se letras iguais True se não False

s1='marrocos'
s2='socorram'
anagrama(s1,s2)
