# SAVI_TP1_G4

# Trabalho prático 1- Enunciado

Pretende-se desenvolver um sistema inteligente que recebe um stream de vídeo da câmara a bordo do computador.

 1. O sistema deverá detetar caras sempre que alguém chegar perto;

 2. Para além de detetar as caras o sistema deverá ser capaz de reconhecer as várias pessoas da turma (ou do grupo). Para isso pode funcionar com uma base de dados pré-gravada. Deve também ser possível iniciar o sistema sem ter ainda informação sobre nenhuma pessoa;

 3. Deve ser possível visualizar a base de dados das pessoas em tempo real;

 4. O sistema deverá identificar as pessoas que reconhece, e perguntar sobre as pessoas desconhecidas;

 5. O sistema deve cumprimentar as pessoas que já conhece, dizendo "Hello <nome da pessoa>". Poderá utilizar uma ferramenta de \emph{text to speech}, por exemplo https://pypi.org/project/pyttsx3/ ;

 6. O sistema deverá fazer o seguimento das pessoas na sala e manter a identificação em cima das pessoas que reconheceu anteriormente, ainda que atualmente não seja possível reconhecê-las.

 # Tópicos e percentages-para avaliação

  | Percentagem  | Tarefa |
| ------------- | ------------- |
  |15%| Deteção|
  |15%| Seguimento|
  |10%| Reconhecimento|
  |5%| Base de dados Caras|
  |5%| Deteção de desconhecidos|
  |5%| Aprendizagem de novas caras|
  |10%| Comprimentar pessoas|
  |5%| Interface|
  |10%| Vizualização da informação|
  |10%| Extras|
  |10%| Código e Github|

# Deteção
  A deteção é baseada no site : https://www.datacamp.com/tutorial/face-detection-python-opencv
  
  Haar Cascade para deteção de caras usando OpenCV e Python

