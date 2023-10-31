# SAVI_TP1_G4

# Trabalho prático 1- Enunciado

Pretende-se desenvolver um sistema inteligente que recebe um stream de vídeo da câmara a bordo do computador.

 1. O sistema deverá detetar caras sempre que alguém chegar perto;

 2. Para além de detetar as caras o sistema deverá ser capaz de reconhecer as várias pessoas da turma (ou do grupo). Para isso pode funcionar com uma base de dados pré-gravada. Deve também ser possível iniciar o sistema sem ter ainda informação sobre nenhuma pessoa;

 3. Deve ser possível visualizar a base de dados das pessoas em tempo real;

 4. O sistema deverá identificar as pessoas que reconhece, e perguntar sobre as pessoas desconhecidas;

 5. O sistema deve cumprimentar as pessoas que já conhece, dizendo "Hello <nome da pessoa>". Poderá utilizar uma ferramenta de \emph{text to speech}, por exemplo https:/https://pypi.org/project/pyttsx3//pypi.org/project/pyttsx3/ ;

 6. O sistema deverá fazer o seguimento das pessoas na sala e manter a identificação em cima das pessoas que reconheceu anteriormente, ainda que atualmente não seja possível reconhecê-las.

 # Tópicos e percentagens-para avaliação

  | Percentagem  | Tarefa |
| ------------- | ------------- |
  |15%| Deteção|
  |15%| Seguimento|
  |10%| Reconhecimento|
  |5%| Base de dados Caras|
  |5%| Deteção de desconhecidos|
  |5%| Aprendizagem de novas caras|
  |10%| Cumprimentar pessoas|
  |5%| Interface|
  |10%| Vizualização da informação|
  |10%| Extras|
  |10%| Código e Github|

  # Deteção
  A deteção é baseada no site : https://www.datacamp.com/tutorial/face-detection-python-opencv
  
  Haar Cascade para deteção de caras usando OpenCV e Python

  Principio de funcionamento:
    
1. Ler a imagem;  
2. Converter para uma imgem de cinzentos;  
3. Carregar o classificador;  
4. Definir os parâmetros de deteção de caras;
5. Desenhar o retângulo envolvente;
6. Amostragem do resultado.

  # Resultados da deteção
  O desenvolvimento deste tópico deu origem ao código "detection.py", tendo obtido o seguinte resultado seguinte video:
   <video src="docs/dete%C3%A7%C3%A3o.mp4" controls title="Title"></video>
  
  
# Seguimento

  <video src="docs/traking.mp4" controls title="Title"></video>

# Reconhecimento

<video src="docs/reconhecimento.mp4" controls title="Title"></video>

# Base de dados Caras
  
  A pasta onde está guardada a base de dados é denominada de "faces", onde se guarda as imagens com o nome da pessoa.

![Alt text](<docs/base de dados nomes.jpeg>)

![Alt text](docs/Emanuel.jpeg)

![Alt text](<docs/joao valinho.jpg>)

![Alt text](docs/Figueiredo.jpeg)


# Deteção de desconhecidos

![Alt text](<docs/deteção desconhecidos.jpeg>)

# Aprendizagem de novas caras

![Alt text](<docs/deteção de movas caras.jpeg>)

![Alt text](<docs/registo base de dados desconhecido.jpeg>)

# Cumprimentar pessoas
Usou-se o exemplo de referência disponibilizado no enunciado do trabalho:
https:/https://pypi.org/project/pyttsx3//pypi.org/project/pyttsx3/ ;
Quando a pessoa é reconhecida, cumprimenta-a dizendo "Hello" e o seu nome


# Vizualização da informação

<video src="docs/resultado_final.mp4" controls title="Title"></video>


# Extras
 Atualização da base de dados sempre que encontra alguem desconhecido

# main

 Dizer o programa principal e o ficheiro auxiliar
 maincopy_3.py
 classescopy_3.py
