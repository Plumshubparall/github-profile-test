# crear un circuito cuantico
q0 = cirq.GriQubit,(0,0)
q0 = cirq.GridQubit(1,0)
qc = cirq.Circuit()
# Agregar una puerta de Hadamard al primer qubit
qc. append(cirq.H(q0))
# Agregar una puerta de entrelazamiento entre los qubit
qc.append(cirq.CNOT(q0,q1))
# Agregar una puerta de rotacion al primer qubit
qc.append(cirq.rx(0.5)(q0))
#Optimizar el circuito cúantico 
optimized_qc=cirq.merge_k_qubit_unitaries(qc,k=2)
# imprimir el circuito cuántico original y optimizado
prin("Circuito cuántico original:")
print(qc)
print(qc)
print("Circuito cuántico optimizado:")
print(optimized_qc)

impot cirq
import numpy as np
from skleam.datasets import fech_20Newsgroups
from skleam.model_selection import train_test_split
# Cargar el conjunto de datos  de 20 Newsgroups(subset="al")
x = dataset.data 
y = dataset.target 
# Dividir el conjunto de datos en entrenamiento y prueba
x_train,x_test,y_train,y_test = train_test_splint(x,y,test_size=0.2,random_state=42)
# Definir el circuito cuántico 
q0 = cirq.GridQubit(0,0)
q1 = cirqGridQubit(1,0)
qc = cirq.Circuit()
# Agregar una puerta de Hadamard al primer qubit
qc.append(cirq.H(q0))
# Agregar una puerta de entrelazamiento entre los qubits
qc.append(cirq.CNOT(Q0,Q1))
# Definir el algoritmo de aprendisaje automático cuántico 
def aprender (datos): 
# Convertir los datos de texto a vectores numéricos 
vectores = []
for texto en datos:
vector = np.array([ord(c)for c texto])
vectores.append(vector)
# Entrenar el modelo cuántico 
Simulador = cirq.Simulador ()
resultados =[]
for vector in vectores:
qc_copy =qc.copy()
for i,valor in enumerate (vector):
qc_copy.append(cirq.rx(valor)(q0))
resultado = simulator.run(qc_copy,repetitions=1024)
resultados.append(resultado)
retum resultados
# Entrenar el modelo 
resultados =Aprender(x_train)
# Evaluar el modelo 
precision = 0 
for i, resultado in enumerate(resultados):
#Evaluar la precisión del modelo 
pass 
print("Precisión":precisión)





<h1 align="center">Hola 👋 , soy alejandra</h1>
<h3 align="center">Una apasionada desarrolladora de frontend de argentina</h3>

<p align="left"> <img src="https://komarev.com/ghpvc/?username=todos&label=Profile%20views&color=0e75b6&style=flat" alt="todos" /> </p>

<p align="left"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img src="https://github-profile-trophy.vercel.app/?username=todos" alt="todos" /></a> </p>

- 🔭 Actualmente estoy trabajando en [plum.io](https://www.plum.io)

- 🌱 Actualmente estoy aprendiendo **www./linkedin.com/in/alejandra-lopez-467**-

👯 Estoy buscando colaborar en [plum](https://www.plum.com.ar)

- 🤝 Estoy buscando ayuda con [https://plum.com.ar](https://plum.com.ar)

- 👨 💻 Todos mis proyectos están disponibles en [https://www.plum.io](https://www.plum.io)

- 📝 Regularmente escribo artículos sobre [https://www.plum.io](https://www.plum.io)

- 💬 Pregúntame sobre **https://wwwplum.com.ar**-

📫 Cómo contactar conmigo **al4586101@gmail.com**

- 📄 Conoce mis experiencias [https://www.plum.io](https://www.plum.io)

- ⚡ Dato curioso **si**<

h3 align="left">Conéctate conmigo:</h3>
<p align="left">
<a href="https://linkedin.com/in/todos" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="todos" height="30" width="40" /></a>
</p>

<h3 align="left">Idiomas y herramientas:</h3>
<p align="left"> <a href="https://azure.microsoft.com/en-in/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="azure" width="40" height="40"/> </a> <a href="https://www.cprogramming.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" width="40" height="40"/> </a> <a href="https://canvasjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/Hardik0307/Hardik0307/master/assets/canvasjs-charts.svg" alt="canvasjs" width="40" height="40"/> </a> <a href="https://www.w3schools.com/cs/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg" alt="csharp" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://d3js.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/d3js/d3js-original.svg" alt="d3js" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://dotnet.microsoft.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/dot-net/dot-net-original-wordmark.svg" alt="dotnet" width="40" height="40"/> </a> <a href="https://firebase.google.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/firebase/firebase-icon.svg" alt="firebase" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://jekyllrb.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/jekyllrb/jekyllrb-icon.svg" alt="jekyll" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://www.php.net" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/php/php-original.svg" alt="php" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="reaccionar" width="40" height="40"/> </a> <a href="https://reactnative.dev/" target="_blank" rel="noreferrer"> <img src="https://reactnative.dev/img/header_logo.svg" alt="reactnative" width="40" height="40"/> </a> <a href="https://www.ruby-lang.org/en/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/ruby/ruby-original.svg" alt="ruby" width="40" height="40"/> </a> <a href="https://www.sketch.com/" target="_blank" rel="noreferrer"> 
# 💫 About Me:
https://www.plum.io


## 🌐 Socials:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/www./linkedin.com/in/alejandra-lopez-467) 

# 💻 Tech Stack:
![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white) ![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white) ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white) ![.Net](https://img.shields.io/badge/.NET-5C2D91?style=for-the-badge&logo=.net&logoColor=white) ![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Adobe Acrobat Reader](https://img.shields.io/badge/Adobe%20Acrobat%20Reader-EC1C24.svg?style=for-the-badge&logo=Adobe%20Acrobat%20Reader&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Prettier](https://img.shields.io/badge/prettier-%23F7B93E.svg?style=for-the-badge&logo=prettier&logoColor=black)
# 📊 GitHub Stats: 


<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->
