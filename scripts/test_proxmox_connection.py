from proxmoxer import ProxmoxAPI

# Remplace ces valeurs par les tiennes
PROXMOX_HOST = "10.0.0.100"  # ← IP de ton serveur Proxmox
API_USER = "root@pam"
API_TOKEN = "37a09cc0-af90-4fa7-9774-2a10e131875d"  # ← Ton vrai token ici

# Connexion sécurisée à l'API Proxmox
proxmox = ProxmoxAPI(
    PROXMOX_HOST,
    user=API_USER,
    token_name="python-automation",
    token_value=API_TOKEN,
    verify_ssl=False  # ← Tu peux mettre True si ton certificat est valide
)

# Afficher les nœuds du cluster
print("Liste des nœuds dans le cluster Proxmox :")
for node in proxmox.nodes.get():
    print(f"- {node['node']}")

