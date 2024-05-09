Voici un exemple de script permettant la mise en place d'un système de RAG minimaliste fourni en accompagnement au magazine ActuIA n°15.

Ce script se base sur Ollama et llamaIndex.

# Installation préalable
*  Installez et lancez l'application Ollama ( https://ollama.com/ ) qui permet de faire tourner des LLM open source en local.

# Modules python : 

Vous pouvez installer l'ensemble des modules python nécessaires en lançant la commande : 
```
pip install -r requirements.txt
```
ou un par un  :

#### LlamaIndex : framework de conception d'applications basées sur les LLM
```
pip install llama-index
```

#### Ollama : module Ollama pour Python 
```
pip install ollama
```
#### Interfaçage entre LlamaIndex et Ollama
```
pip install llama-index-llms-ollama
```
#### Accès aux modèles dep longement d'Hugging Face permettant de transformer le corpus documentaire en vecteurs
```
pip install llama-index-embeddings-huggingface
```


## Avant le premier lancement du script, insérez des documents texte dans un nouveau dossier nommé data afin de constituer votre corpus à interroger.

#### Exécution du script : 
```
python script.py
```

Au premier lancement, les différents modèles seront téléchargés et l'index sera généré, ce qui peut prendre du temps selon les ressources matérielles de votre PC/serveur et la taille du corpus que vous utilisez.

Ce script, inspiré de la documentation officielle de LlamaIndex est créé dans un but pédagogique. L'emploi d'un framework web comme flask ou django pour interroger votre RAG via une API, la possibilité de réindexer votre corpus sont des évolutions qui rendront votre RAG plus opérationnel.


Retrouvez le magazine de l'intelligence artificielle sur https://boutique.actuia.com
