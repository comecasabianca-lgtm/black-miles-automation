
import os
from pathlib import Path

link = os.environ.get("TRC_LINK", "").strip()

if not link.startswith(
    "https://app.therunningcollective.fr/links/"
):
    raise ValueError("Lien TRC invalide")

output = Path("output")
output.mkdir(exist_ok=True)

posts = {
    "reddit.txt": f"""
Je participe au Black Miles Challenge !

Pour découvrir The Running Collective
et comparer des chaussures de running :

{link}

C'est mon lien de parrainage.
""",

    "discord.txt": f"""
🏃 Je participe au Black Miles Challenge !

Pour découvrir The Running Collective :
{link}

Lien de parrainage personnel !
""",

    "forums.txt": f"""
Bonjour à tous !

Je participe au Black Miles Challenge.
Voici mon lien pour découvrir
The Running Collective :

{link}

Bonne course !
"""
}

for filename, content in posts.items():
    (output / filename).write_text(
        content.strip() + "\n",
        encoding="utf-8"
    )

print("Publications générées avec succès !")
