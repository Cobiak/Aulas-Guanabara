   ## FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELA

# toda função 'input' é classe 'string' independente do tipo, é necessário especificar ##

a = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(a))     ## 'a' é considerado o OBJETO: todo o objeto tem características e realiza funcionalidades, atributos e métodos
print('Só tem espaços? ', a.isspace())                         
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculo? ', a.isupper())
print('Está em minúsculo? ', a.islower())
print('Está capitalizada? ', a.istitle())               ## não está nem maiúscula e nem minúscula ##