
import os
from pathlib import Path
from datetime import date

link = os.environ.get("TRC_LINK", "").strip()

if not link.startswith(
    "https://app.therunningcollective.fr/links/"
):
    raise ValueError("Lien TRC invalide")

today = date.today().strftime("%d/%m/%Y")

posts = {
    "reddit.txt": f"""
Bonjour !

Je participe au Black Miles Challenge de
The Running Collective.

Je partage mon lien de parrainage pour ceux
qui souhaitent découvrir la plateforme et
comparer des chaussures de running :

{link}

C'est bien un lien de parrainage personnel.
Bonne course à tous !

Date : {today}
""",

    "discord.txt": f"""
🏃 BLACK MILES

Je participe au challenge de The Running
Collective !

Si vous voulez découvrir leur plateforme
et comparer des chaussures de running :

{link}

Lien de parrainage personnel.
Merci à ceux qui passeront voir !
""",

    "forums.txt": f"""
Bonjour à tous,

Je participe actuellement au Black Miles
Challenge organisé par The Running Collective.

Pour ceux qui ne connaissent pas, la plateforme
permet notamment de découvrir et comparer
des chaussures de running.

Voici mon lien de parrainage personnel :
{link}

N'hésitez pas à me dire ce que vous pensez
de la plateforme !

Bonne journée et bonnes courses.

Date : {today}
"""
}

output = Path("output")
output.mkdir(exist_ok=True)

for filename, content in posts.items():
    (output / filename).write_text(
        content.strip() + "\n",
        encoding="utf-8"
    )

print("3 publications générées avec succès !")
