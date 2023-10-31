
<<<<<<< HEAD
# Sudação 

  Bem-vindo ao nosso projeto! 
  Neste repositório, encontrará o código-fonte e recursos relacionados ao nosso software. 
  Vamos desbruçar nas principais tarefas deste trabalho.

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

  O desenvolvimento deste tópico deu origem ao código "detection.py"e ao vídeo deteção.mp4 presente na pasta docs.

   <video src="docs/dete%C3%A7%C3%A3o.mp4" controls title="Title"></video>
  
  
# Seguimento ou traking
  O traking teve como base a implementação de código desenvolvido em aula, tendo dado origem ao ficheiro main.py e ao vídeo traking.mp4 presente na pasta docs.

  <video src="docs/traking.mp4" controls title="Title"></video>

# Reconhecimento
  
  O desenvolvimento deste tópico passou pela implementação de duas formas deiferente de fazer reconhecimento.
   A primeira forma passou por implementar deap learning com um ficheiro de treino criado uma única vez, que teve como base o vídeo "https://www.youtube.com/watch?v=lH01BgsIPuE&t=818s" e o site "https://teachablemachine.withgoogle.com/". O desenvolvimento deste tópico deu origem ao código recognition.py, o seu desempenho mostrou-se pouco eficaz e o seu uso foi abandonado por decisão do grupo.

   A segunda forma explorada e bem socedida teve como base o vídeo "https://www.youtube.com/watch?v=tl2eEBFEHqM&t=971s" onde analiza os nomes das imagens presentes numa pasta e assucias devidamente para posteriormente fazer o reconhecimento com base nessa informação. O resultado deste tópico deu origem ao código tenstativa_recognition.py e ao vídeo de demontração "reconhecimento.mp4" presente na pasta docs.
   

<video src="docs/reconhecimento.mp4" controls title="Title"></video>

# Base de dados Caras
  

  A pasta onde está guardada a base de dados é denominda de "faces" e contem as imagens com os elementos do grupo e o nome de identificação.
  Exemplo de configuração inicial da base de dados:
  

  A pasta onde está guardada a base de dados é denominada de "faces", onde se guarda as imagens com o nome da pessoa.


![Alt text](<docs/base de dados nomes.jpeg>)

![Alt text](docs/Emanuel.jpeg)

![Alt text](<docs/joao valinho.jpg>)

![Alt text](docs/Figueiredo.jpeg)


# Deteção de desconhecidos
  Sempre que o programa deteta alguem desconhecido, é atribuido a este um id e é automaticamente guardado na base de dados com esse id, uma vez a base de dados alterada é executada a atualização do reconhecimento tendo em conta as novas entradas.
  A deteção de desconhecidos está implementada só na versão final do código que é maincopy_3.py.
  
  Exemplo da deteção de um desconhecido:

![Alt text](<docs/deteção desconhecidos.jpeg>)

# Aprendizagem de novas caras

![Alt text](<docs/deteção de movas caras.jpeg>)

![Alt text](<docs/registo base de dados desconhecido.jpeg>)

# Cumprimentar pessoas

  Usou-se o exemplo de disponibilizado no enunciado do trabalho:
  https:/https://pypi.org/project/pyttsx3//pypi.org/project/pyttsx3/ ;
  Quando a pessoa é reconhecida, cumprimenta-a dizendo "Hello" juntamente com nome associado tal como os desconhecidos (unknow) após serem detetados
=======
Usou-se o exemplo de referência disponibilizado no enunciado do trabalho:
https:/https://pypi.org/project/pyttsx3//pypi.org/project/pyttsx3/ ;
Quando a pessoa é reconhecida, cumprimenta-a dizendo "Hello" e o seu nome
>>>>>>> adc18ba66484ba700d1708d4943bd32c1b357dfb


# Vizualização da informação
  
  Pode-se visualizar no terminal mensagens após determinadas ações para fazer o debug do programa, como se pode verificar no vídeo a seguir:

  <video src="docs/resultado_final.mp4" controls title="Title"></video>



# Extras

 Foram feitos dois extras, sendo eles:
 - O programa é iníciado com um dialogo de brincadeira "welcome noobs!".
 - Atualização da base de dados sempre que encontra alguem desconhecido.
 

# main

 O resultado do trabalho desenvolvidp

 |programa principal | funções e classes|
 | -------------    |------------- |
 | maincopy_3.py   | classescopy_3.py |

O arquivo `maincopy_3.py` é o coração deste projeto. 
Este é o arquivo principal que contém a lógica central do programa. Aqui, você encontrará todas as funcionalidades principais e os principais algoritmos que fazem este programa funcionar.

`classescopy_3.py` é um arquivo auxiliar que contém funções e classes úteis para auxiliar o funcionamento do `maincopy_3'. Ele fornece funcionalidades extras e facilita a organização do código principal.

Consulte a documentação completa e os recursos fornecidos para obter mais detalhes sobre como usar, modificar e contribuir para este projeto.

Se tiver alguma dúvida, sinta-se à vontade para entrar em contacto.

Aproveite o projeto!




=======
>>>>>>> 22a4c1d0fdb35fd2f21c3f87125dc20a817c7682
