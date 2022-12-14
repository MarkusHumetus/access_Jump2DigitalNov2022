
# Background
Access Project for the hackathon Jump2Digital, it will take place in 25th of Novembre 2022. At the bottom of this readme you can find the [initial information](#Initial-Info-/-Problem) shared throuhg the Nuwe platform. [Train data set](https://nuwe.io/dev/challenges/jump2digital2022-data-science#:~:text=Variables%20del%20dataset%3A,ejemplo_predicciones.csv%27%20haz%20click%20aqu%C3%AD.) and [Test data set](https://challenges-asset-files.s3.us-east-2.amazonaws.com/Events/Jump2digital+2022/test.csv) without the target/label column are shared online.
    
# Getting Started

1. Clone this [repo](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022).
2. Use [requirements.txt](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/requirements.txt) to install all required dependencies. Please note that Pycaret 2.3.0 only works properly under Python 3.6-3.8

# Methodology

0. Load libraries and data.
1. Exploratory, Analysis and manipulation of initial Data (Sweetviz library used).
2. Data Engineering
3. Study Data Engineering impact on model performance
4. Tunning of hyperparameters to optimize the Random Forest model.
5. Predict the status for the test data set (supplied without label) with the optimised model.
6. Results and conclusions

# Tools

* Python
* Git & Github
* Jupyter Notebook
* Visual Studio Code
* Libraries: Pandas, Numpy, Sweetviz, Seaborn, Matplotlib, Sklearn, Pycaret, Optuna. 

# Project Status

[Finished]

Project was completed and submitted for competition in the 11th November 2022.
Files generated in the repository:

- Python code as [app.py](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/app.py)

- [Jupyter Noebook: main.ipynb](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/main.ipynb)

- [predictions.csv](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/predictions.csv)

- [predictions.json](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/predictions.json)

- [requirements.txt](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/requirements.txt)

# Initial Info / Problem

Jorge es un ge??logo del IGME (Instituto Geol??gico y Minero de Espa??a) que est?? desarrollando un nuevo sistema de prevenci??n de erupciones para poder predecir qu?? tipo de erupci??n tendr?? un volc??n seg??n las las vibraciones detectadas por sus sensores durante los d??as previos a la erupci??n. Esto permitir?? reducir el riesgo de v??ctimas y destrozos materiales por este tipo de cat??strofe natural.
El sistema de Jorge trabaja con 5 tipos de erupciones:

![Volcanos types](https://challenges-asset-files.s3.us-east-2.amazonaws.com/data_sets/Data-Science/4+-+events/jobmadrid/images/tipos.jpeg)

__Pliniana__: Se caracteriza por su alto grado de explosividad, con manifestaciones muy violentas en las cuales se expulsan grandes vol??menes de gas volc??nico, fragmentos y cenizas.

__Peleana__: La caracter??stica m??s importante de una erupci??n peleana es la presencia de una avalancha brillante de ceniza volc??nica caliente, llamada flujo pirocl??stico.

__Vulcaniana__: Son erupciones volc??nicas de tipo explosivo. El material magm??tico liberado es m??s viscoso que en el caso de las erupciones hawaianas o estrombolianas; consecuentemente, se acumula m??s presi??n desde la c??mara magm??tica conforme el magma asciende hacia la superficie.

__Hawaiana__: Consiste en la emisi??n de material volc??nico, mayoritariamente bas??ltico, de manera efusiva o no explosiva. Ocurre de este modo debido a que la difusi??n de los gases a trav??s de magmas m??s b??sicos (bas??lticos) puede hacerse de manera lenta pero m??s o menos continua. Consecuentemente, las erupciones volc??nicas de este tipo no suelen ser muy destructivas.

__Estromboliana__: La erupci??n Estromboliana est?? caracterizada por erupciones explosivas separadas por periodos de calma de duraci??n variable. El proceso de cada explosi??n corresponde a la evoluci??n de una burbuja de gases liberados por el propio magma.

???? __Objectivo__

El objetivo del reto ser?? realizar un modelo predictivo basado en Random Forests que permita conocer el tipo de calidad del aire en funci??n de las mediciones de los sensores.

Una vez se haya hecho y entrenado el modelo predictivo, ??ste se tendr?? que emplear con los features del dataset de testing 'test.csv'. Las predicciones se tendr??n que entregar en formato csv como en el ejemplo. Donde tendr?? que aparecer tan solo una columna en la que en la primera fila habr?? un texto cualquiera y las predicciones empezar??n en la fila 2.

La calidad de la predicci??n se medir?? a partir del f1-score(macro).


???? __Dataset__

El dataset contiene 8 features en 8 columnas que son los par??metros medidos por los diferentes sensores. Estos corresponden a las diferentes interacciones que han tenido los haces de los l??seres al travesar las part??culas del aire.

Target: El target corresponde al 'label' que clasifica la calidad del aire.

*Target 0* corresponde a una calidad del aire Buena
*Target 1* corresponde a una calidad del aire Moderada
*Target 2* corresponde a una calidad del aire Peligrosa

Archivos:

[train.csv](https://nuwe.io/dev/challenges/jump2digital2022-data-science#:~:text=Variables%20del%20dataset%3A,ejemplo_predicciones.csv%27%20haz%20click%20aqu%C3%AD.): Este dataset contiene tanto las variables predictoras como el tipo de clasificaci??n de calidad del aire.

[test.csv](https://challenges-asset-files.s3.us-east-2.amazonaws.com/Events/Jump2digital+2022/test.csv): Este dataset contiene las variables predictoras con las que se tendr?? que predecir el tipo de calidad de aire.

Para descargar el dataset de 'ejemplo_predicciones.csv' haz click [aqu??](https://challenges-asset-files.s3.us-east-2.amazonaws.com/data_sets/Data-Science/4+-+events/jump2digital/dataset/ejemplo_predicciones.csv).



??? __Evaluaci??n__
La evaluaci??n se basar?? en los objetivos cumplidos (900/1200), en la calidad de c??digo (200/1200)  y en la documentaci??n (100/1200).

???? __Entrega__
Revisar que la rama principal de entrega del repositorio es main.

El c??digo se deber?? de entregar en un fichero py llamado [app.py](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/app.py). Este tendr?? todas las funciones utilizadas y el c??digo necesario junto documentaci??n para reproducir vuestra soluci??n. Para los gr??ficos os recomendamos entregarlo en un [ipynb](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/main.ipynb).

# Results & Conclusions

* No improvements observed from different scalling modification for the initial dataset (Mix-max, Standard and Robust scalers).
* Dimension reduction of features didn't improve the classification performance of Rain forest model (PCA study to 5, 6 or 7 components).
* **Maximum f1 score macro** observed in the tunning process was **0.919**.
* According to Pycaret screening with reduction of component analysis to 6 components, Extra Trees Classifier could perform better than RainForset Classifier/RFC. However, initial requirement was to use RFC and no additional trials were done.

# Analysis
Initial dataset has balanced classes and distributions can The predictions are quite accured with good metrics.be considered gaussian. There are several features with a high correlation.

# Solution
Solution includes the following files:

- Python code as [app.py](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/app.py)

- Jupyter Noebook as [main.ipynb](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/main.ipynb)

- [predictions.csv](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/predictions.csv)

- [predictions.json](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/predictions.json)

- [requirements.txt](https://github.com/MarkusHumetus/access_Jump2DigitalNov2022/blob/main/requirements.txt) in case environment of work is needed.

# License

Copyright (c) **[2022] Marc Humet Montada**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Contact

If you have any comment, doubt, proposal,... don't hesitate to contact me by email to Marc.Humet.DataScience@gmail.com or by 
 [![LinkedIn][linkedin-shield]][linkedin-url]

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://www.linkedin.com/in/marchumetmontada/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555


# Acknowledgments

Thanks to the following organisations for the set up of such event which give the junior data scientist oportunities to learn, do networking and hopefully reach a first job in the data field.

![Mobile World Capital Barcelona](https://ametic.es/sites/default/files//mobile_world_capital_barcelona.png)

![Barcelona Digital Talent](https://challenges-asset-files.s3.us-east-2.amazonaws.com/companies/BDT_card.png)

![Nuwe](https://elreferente.es/wp-content/uploads/2021/12/LOGO_LETTERS_MONO-3.png)

