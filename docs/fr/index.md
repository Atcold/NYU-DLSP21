---
layout: default
title: APPRENTISSAGE PROFOND
author: Alfredo Canziani
lang-ref: home
lang: fr
translation-date: 19 Jun 2021
translator: Loïck Bourdois
---

<!--
**DS-GA 1008 · SPRING 2021 · [NYU CENTER FOR DATA SCIENCE](http://cds.nyu.edu/)**

| INSTRUCTORS | Yann LeCun & Alfredo Canziani |
| LECTURES    | Wednesday 9:30 – 11:30, Zoom |
| PRACTICA    | Tuesdays 9:30 – 10:30, Zoom |
| FORUM       | [r/NYU_DeepLearning](https://www.reddit.com/r/NYU_DeepLearning/) |
| DISCORD     | [NYU DL](https://discord.gg/CthuqsX8Pb) |
| MATERIAL    | [2021 repo](https://github.com/Atcold/NYU-DLSP21) |
-->

**DS-GA 1008 · PRINTEMPS 2021 · [NYU CENTER FOR DATA SCIENCE](http://cds.nyu.edu/)**

| INSTRUCTEURS | Yann Le Cun & Alfredo Canziani |
| COURS MAGISTRAUX  | Mercredi 9:30 – 11:30, Zoom |
| TRAVAUX DIRIGÉS   | Jeudi 9:30 – 10:30, Zoom |
| FORUM       | [r/NYU_DeepLearning](https://www.reddit.com/r/NYU_DeepLearning/) |
| DISCORD     | [NYU DL](https://discord.gg/CthuqsX8Pb) |
| MATERIEL    | [2021 repo](https://github.com/Atcold/NYU-DLSP21) |


<!--
## 2021 edition disclaimer

Check the repo's [`README.md`](https://github.com/Atcold/NYU-DLSP21/blob/master/README.md) and learn about:

- Content new organisation
- The semester's second half intellectual dilemma
- This semester repository
- Previous releases
-->

## Informations liées à l'édition 2021

Consultez le fichier [`README.md`](https://github.com/Atcold/NYU-DLSP21/blob/master/docs/fr/README-FR.md) du dépôt pour en savoir plus sur  :

- La nouvelle organisation du contenu
- Le dilemme intellectuel de la seconde moitié du semestre
- Le référentiel de ce semestre
- Les éditions précédentes


<!--
## Lectures

Most of the lectures, labs, and notebooks are similar to the previous edition, nevertheless, some are brand new.
I will try to make clear which is which.

**Legend**: 🖥 slides, 📓 Jupyter notebook, 🎥 YouTube video.

### Theme 1 : Introduction

 * History and resources [🎥](https://youtu.be/mTtDfKgLm54) [🖥 ](https://drive.google.com/file/d/1vVNUye-1JNJnqP4A0704sjtF7gs_MpCI/)
 * Gradient descent and the backpropagation algorithm [🎥](https://youtu.be/nTlCqaL7fCY) [🖥 ](https://drive.google.com/file/d/1tYPYGYFDQw5IBs9wx4egCcBTTX2h9d9g/)
 * [Neural nets inference](https://atcold.github.io/NYU-DLSP21/en/week02/02-3/) [🎥](https://youtu.be/0TdAmZUMj2k) [📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb)
 * Modules and architectures [🎥](https://youtu.be/IYQN3i7dJIQ)
 * [Neural nets training](https://atcold.github.io/NYU-DLSP21/en/week03/03-3/) [🎥](https://youtu.be/EyKiYVwrdjE) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf) [📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb)[📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb)
* [Homework 1](https://drive.google.com/drive/folders/1g-uQNEi_NJyELGRMrJGXXxmARDabcXFd)

### Theme 2: Parameters sharing

 * Recurrent and convolutional nets [🎥](https://youtu.be/7dU3TFBJl-0) [🖥 ](https://drive.google.com/file/d/1GtI4ywzI84oamyr_W5k_wzgfRN139aFD/) [📝 ](https://drive.google.com/file/d/12jP4ssUIoGURAU8jGj6QwKXyZVdXW0o6/)
 * ConvNets in practice [🎥](https://youtu.be/-wz_vADGbtE) [🖥 ](https://drive.google.com/file/d/1WX3HoZhekL4MVvi_7VuLRYJtBGnF9JJY/) [📝 ](https://drive.google.com/file/d/1ToWP7e71diAeMtQ0D9pU-f0BXF4bAg46/)
 * Natural signals properties and the convolution [🎥](https://youtu.be/KvvNkE2vQVk) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf) [📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb)
 * Recurrent neural networks, vanilla and gated (LSTM) [🎥](https://youtu.be/5KSGNomPJTE) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/04%20-%20RNN.pdf) [📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/08-seq_classification.ipynb)[📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/09-echo_data.ipynb)
 * [Homework 2](https://drive.google.com/drive/folders/1or1YiW0fFiZGEYy6b4EOEDgRPr0GQX0i)

### Theme 3: Energy based models, foundations

 * Energy based models (I) [🎥](https://youtu.be/xIn-Czj1g2Q) [🖥 ](https://drive.google.com/file/d/1kLUgZdRYFO5ksYHzbsRS8m8IocNiGu2J/)
 * Inference for LV-EBMs [🎥](https://youtu.be/xA_OPjRby5g) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf)
 * What are EBMs good for? [🎥](https://youtu.be/eJeJWWEo7cE)
 * Energy based models (II) [🎥](https://youtu.be/8u2s64ZtmiA) [🖥 ](https://drive.google.com/file/d/1czfiEE6IPqE7q1fTm-SWOiC3VNEtpNrj/) [📝 ](https://drive.google.com/file/d/1IB5dkcAQ6GsHEz8Eg2hjaeQeVtT2i4Z5/)
 * Training LV-EBMs [🎥](https://youtu.be/XIMaWj5YjOQ) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf)
 * [Homework 3: structured prediction](https://drive.google.com/drive/folders/1zGy_SnMBqaoS7_dHRmKiOFtqNV1jJJb6)
-->

## Cours magistraux

La plupart des cours, des travaux dirigés et des notebooks sont similaires à l’édition précédente, néanmoins, certains sont nouveaux. Nous essayerons d’indiquer clairement lesquels.

**Légende**: 🖥 diapositives, 📓 notebook Jupyter , 🎥 vidéos YouTube

### Thème 1 : Introduction

 * Historique et ressources [🎥](https://youtu.be/mTtDfKgLm54) [🖥 ](https://drive.google.com/file/d/1vVNUye-1JNJnqP4A0704sjtF7gs_MpCI/)
 * Descente de gradient et algorithme de rétropropagation [🎥](https://youtu.be/nTlCqaL7fCY) [🖥 ](https://drive.google.com/file/d/1tYPYGYFDQw5IBs9wx4egCcBTTX2h9d9g/)
 * [Inférence des réseaux de neurones](https://atcold.github.io/NYU-DLSP21/fr/week02/02-3/) [🎥](https://youtu.be/0TdAmZUMj2k) [📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb)
 * Modules et architectures [🎥](https://youtu.be/IYQN3i7dJIQ)
 * [Entraînement des réseaux neuronaux](https://atcold.github.io/NYU-DLSP21/fr/week03/03-3/) [🎥](https://youtu.be/EyKiYVwrdjE) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf) [📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb)[📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb)
* [Devoir 1](https://drive.google.com/drive/folders/1g-uQNEi_NJyELGRMrJGXXxmARDabcXFd)


### Thème 2 : Partage des paramètres

 * Réseaux convolutifs et récurrents [🎥](https://youtu.be/7dU3TFBJl-0) [🖥 ](https://drive.google.com/file/d/1GtI4ywzI84oamyr_W5k_wzgfRN139aFD/) [📝 ](https://drive.google.com/file/d/12jP4ssUIoGURAU8jGj6QwKXyZVdXW0o6/)
 * ConvNets en pratique [🎥](https://youtu.be/-wz_vADGbtE) [🖥 ](https://drive.google.com/file/d/1WX3HoZhekL4MVvi_7VuLRYJtBGnF9JJY/) [📝 ](https://drive.google.com/file/d/1ToWP7e71diAeMtQ0D9pU-f0BXF4bAg46/)
 * Les propriétés des signaux naturels et la convolution [🎥](https://youtu.be/KvvNkE2vQVk) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf) [📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb)
 * Réseaux neuronaux récurrents, de base et à portes (LSTM) [🎥](https://youtu.be/5KSGNomPJTE) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/04%20-%20RNN.pdf) [📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/08-seq_classification.ipynb)[📓](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/09-echo_data.ipynb)
 * [Devoir 2](https://drive.google.com/drive/folders/1or1YiW0fFiZGEYy6b4EOEDgRPr0GQX0i)


### Thème 3 : Modèles à base d'énergie (EBMs), fondations

 * Modèles à base d'énergie (I) [🎥](https://youtu.be/xIn-Czj1g2Q) [🖥 ](https://drive.google.com/file/d/1kLUgZdRYFO5ksYHzbsRS8m8IocNiGu2J/)
 * Inférence pour les modèles à base d'énergie à variable latente (LV-EBMs) [🎥](https://youtu.be/xA_OPjRby5g) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf)
 * A quoi servent les EBMs ? [🎥](https://youtu.be/eJeJWWEo7cE)
 * Modèles à base d'énergie (II) [🎥](https://youtu.be/8u2s64ZtmiA) [🖥 ](https://drive.google.com/file/d/1czfiEE6IPqE7q1fTm-SWOiC3VNEtpNrj/) [📝 ](https://drive.google.com/file/d/1IB5dkcAQ6GsHEz8Eg2hjaeQeVtT2i4Z5/)
 * Entraînement des LV-EBMs [🎥](https://youtu.be/XIMaWj5YjOQ) [🖥 ](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/12%20-%20EBM.pdf)
 * [Devoir 3](https://drive.google.com/drive/folders/1zGy_SnMBqaoS7_dHRmKiOFtqNV1jJJb6)
