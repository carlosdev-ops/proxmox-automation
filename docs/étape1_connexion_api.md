# 🧩 Étape 1 – Connexion à l’API Proxmox avec Python

## 🎯 Objectifs

- Créer une structure de projet Python professionnelle
- Utiliser un environnement virtuel pour l’isolation des dépendances
- Générer un token d’API sécurisé dans Proxmox
- Tester la connexion via un script Python

---

## ⚙️ Préparation de l’environnement Python

```bash
sudo apt install python3.12-venv -y
mkdir -p ~/Python/proxmox-automation/scripts ~/Python/proxmox-automation/docs
cd ~/Python/proxmox-automation
python3 -m venv venv
source venv/bin/activate
pip install proxmoxer requests
pip freeze > requirements.txt
