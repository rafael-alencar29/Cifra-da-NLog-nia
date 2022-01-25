'''
Para solucionar o problema, o dividi em algumas etapas. Primeiro, eh feito a leitura da palabra a ser cifrada,
posteriomente cada letra da palavra eh tradada indiviualmente. Ser for vogal, o valor eh guardado, caso seja consoante,
eh feito o calculo da vogal mais proxima. Tambem eh calculado a consoante mais proxima. Todos esses valores sao concatenos 
formando a palavra cifrada. O processo eh possivel ser feito atraves do uso de dicionarios em python. Cada letra tem seu 
respectivo indice.
Dado a leitura de uma letra, sabemos seu indice, entao podemos calcular qual a vogal mais proxima.
Como a funcao que calcula a vogal mais proxima retorna um indice, o uso de listas eh necessario para sabermos a letra 
correspondente, e posteriormente ser feita a concatenacao.
'''

def closer_vowel(num, vowels):  # funcao calcula a variavel mais proxima da consoante e a retorna
	smallest = 50               
	aux = []
	for i in range(0,len(vowels)):
		result = abs(num - vowels[i])
		if (result < smallest):
			smallest = result
			closer = vowels[i]

	return closer	

vowels = [0,4,8,14,20]

# Os dicionarios armazenam as letras do alfabeto e seus respectivos indices
alphabet = { "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i" : 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
			 "o": 14, "p": 15, "q": 16, "r" : 17, "s" : 18, "t": 19, "u": 20, "v": 21, "x": 22, "z": 23  	
			 }

consonants = { "b": 0, "c": 1, "d": 2,  "f": 3, "g": 4, "h": 5, "j": 6, "k": 7, "l": 8, "m": 9, "n": 10,
			  "p": 11, "q": 12, "r" : 13, "s" : 14, "t": 15,  "v": 16, "x": 17, "z": 18  	
			 }

alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z']	
consonants_list = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']		 

word = input() # leitura da palavra
cypher = ''    # variavel que armazena o resultado final, a palvra jah cifrada

'''
 Apos a leiura da palavra, a mesma é divido na quantidade de letras que a compoem, exemplo:
 a palavra "ter" eh dividida em t-e-r, e cada letra eh processada individualmente no loop for
'''
for i in range(0,len(word)):
	if (word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == "u"): # vogais permanecem inalteradas
		cypher = cypher + word[i]
		
	else:
		letter = word[i]
		num = alphabet[letter]	
		closer = closer_vowel(num,vowels)
		cypher = cypher + letter + alphabet_list[closer] + consonants_list[consonants[letter] + 1] # primeira consoante permanece a mesma, entao eh acrescido a vogal mais proxima eh proxima consoante

print(cypher)