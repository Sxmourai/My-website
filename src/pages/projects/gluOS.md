---
layout: "@/layouts/DefaultProject.astro"
title: Mon système d'exploitation GluOS
date: 1/12/2023
desc: GluOS est mon premier système d'exploitation que j'ai fais lorsque j'avais 14 ans
img: /gluOS.png
categories: [["Rust", "#5f0d06"], ["Operating System", "#060f5a"]]
---
## Introduction

En début 2023, alors agé de 14 ans, j'ai commencé à m'intéresser au low-level, d'abord en apprenant le C++ puis le Rust. Lorsque j'ai compris que le Rust était un langage "memory safe", c'est-à-dire qu'il possède un grand nombre de règles stricte pour éviter de faire des bugs dans notre code qui pourrait créer des "memory leaks". Je me suis donc dis que c'était le meilleur langage pour faire un système d'exploitation. Voila pourquoi j'ai commencé ce projet.

## Le setup

Pour faire mon système d'exploitation, j'ai suivi le tuto de Phill Opp. Il était très bien fait, et il proposait un bootloader préfait, ce qui m'a fait gagner un temps considérable. J'ai aussi du installer WSL2, qemu pour tester mon os plus facilement.

## Début du développement

Au départ, j'ai commencé par implementer la fonction print sur le buffer VGA, qui est une fonctionnalité disponible sur la quasi totalité des cartes graphiques. En effet, ce standart qui date des années 80 permet d'afficher du texte en couleur à l'écran. J'ai aussi ajouter le terminal scrolling, c'est-à-dire de déplacer tout le texte vers le haut lorsqu'il n'y a plus de place à l'écran (pour faire de la place au prochain print). J'ai ensuite écris des tests pour vérifier que mon print s'affichait bien, que le terminal scrolling marchait etc. J'étais perdu au départ mais j'ai finis par m'y retrouver et comprendre ce qui se passait.

## Le travail d'équipe c'est mieux

Au bout d'un moment, j'ai fini par ajouter pas mal de fonctionnalités (input du clavier, print sur la console de mon IDE grâce au fonctions de débogage de Qemu, ...). Je me suis dit que j'aimerais bien travailler avec d'autres et qu'on s'entraide. C'est comme ça que j'ai rencontré Grey et Yasser Cherfaoui.

## Ce que j'en ai tiré

J'ai appris beaucoup de choses grâce à ce projet, notamment sur le fonctionnement d'un ordinateur, les différents pointeurs en Rust et les bonnes pratiques. J'ai d'ailleurs réussi le quizz en Rust de Linkedin et je pense que d'avoir développé un OS m'a grandement aider à la réussite de ce quizz.
