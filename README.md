# Proxmox Automation avec Python

Ce projet permet d’automatiser la gestion de machines virtuelles dans un cluster Proxmox via son API, en utilisant Python.

## 🎯 Objectifs

- Apprendre Python progressivement à travers un projet concret
- Automatiser les actions sur les VMs Proxmox : création, démarrage, arrêt, suppression
- Structurer un projet Python prêt pour GitHub

## 📁 Organisation du projet

- `scripts/` : scripts Python exécutables
- `docs/` : documentation de chaque étape (en Markdown)
- `requirements.txt` : dépendances Python à installer avec `pip install -r requirements.txt`
- `.gitignore` : fichiers à exclure du versionnement (comme `venv/`)
- `venv/` : environnement Python virtuel (non versionné)

## 🧪 Première étape réalisée

- Connexion sécurisée à l’API Proxmox avec un token
- Script Python pour afficher les nœuds du cluster

## 🛠️ Prochaine étape

Cloner une VM à partir d’un template, automatiser sa configuration.
