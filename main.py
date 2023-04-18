from system.lib import *
import random
Lib = Lib_UsOS()

card_ref = {
    '+2 bleu':"https://i.ibb.co/Ht8SBzq/2bleu.png",
    '+2 jaune':"https://i.ibb.co/pzQq06n/2jaune.png",
    '+2 rouge':"https://i.ibb.co/b270SJ3/2rouge.png",
    '+2 vert':"https://i.ibb.co/MkWhFjs/2vert.png",
    '+4 couleur':"https://i.ibb.co/Pzc24xx/4changement-de-couleur.png",
    '+4 bleu':"https://i.ibb.co/Pzc24xx/4changement-de-couleur.png",
    '+4 jaune':"https://i.ibb.co/Pzc24xx/4changement-de-couleur.png",
    '+4 rouge':"https://i.ibb.co/Pzc24xx/4changement-de-couleur.png",
    '+4 vert':"https://i.ibb.co/Pzc24xx/4changement-de-couleur.png",
    '0 bleu':"https://i.ibb.co/nf9BNpk/0bleu.png",
    '0 jaune':"https://i.ibb.co/yPYg5x8/0jaune.png",
    '0 rouge':"https://i.ibb.co/qYFDdvD/0rouge.png",
    '0 vert':"https://i.ibb.co/wdH48xY/0vert.png",
    '1 bleu':"https://i.ibb.co/LpWP4tX/1bleu.png",
    '1 jaune':"https://i.ibb.co/vXbVwxq/1jaune.png",
    '1 rouge':"https://i.ibb.co/wzDG0Dr/1rouge.png",
    '1 vert':"https://i.ibb.co/vqYNNcn/1vert.png",
    '2 bleu':"https://i.ibb.co/Lkkby8R/2bleu.png",
    '2 jaune':"https://i.ibb.co/WBnZvH3/2jaune.png",
    '2 rouge':"https://i.ibb.co/TTWbkhD/2rouge.png",
    '2 vert':"https://i.ibb.co/b3PbvQv/2vert.png",
    '3 bleu':"https://i.ibb.co/vvRys3c/3bleu.png",
    '3 jaune':"https://i.ibb.co/GWYNNG5/3jaune.png",
    '3 rouge':"https://i.ibb.co/vPftD9C/3rouge.png",
    '3 vert':"https://i.ibb.co/QFRYCcs/3vert.png",
    '4 bleu':"https://i.ibb.co/zVNFQGN/4bleu.png",
    '4 jaune':"https://i.ibb.co/tC1c5fF/4jaune.png",
    '4 rouge':"https://i.ibb.co/9NkYmbj/4rouge.png",
    '4 vert':"https://i.ibb.co/TL6YK4v/4vert.png",
    '5 bleu':"https://i.ibb.co/PtqmYqb/5bleu.png",
    '5 jaune':"https://i.ibb.co/wQr05X3/5jaune.png",
    '5 rouge':"https://i.ibb.co/DVSCKSc/5rouge.png",
    '5 vert':"https://i.ibb.co/fd8hBcP/5vert.png",
    '6 bleu':"https://i.ibb.co/HhBnRkN/6bleu.png",
    '6 jaune':"https://i.ibb.co/TT1T1SG/6jaune.png",
    '6 rouge':"https://i.ibb.co/87T92Mg/6rouge.png",
    '6 vert':"https://i.ibb.co/BP0pDPs/6vert.png",
    '7 bleu':"https://i.ibb.co/s2f1Ntj/7bleu.png",
    '7 jaune':"https://i.ibb.co/R7Lf1bG/7jaune.png",
    '7 rouge':"https://i.ibb.co/w45nQfT/7rouge.png",
    '7 vert':"https://i.ibb.co/grS8HL0/7vert.png",
    '8 bleu':"https://i.ibb.co/xF2rSYc/8bleu.png",
    '8 jaune':"https://i.ibb.co/8czGKDP/8jaune.png",
    '8 rouge':"https://i.ibb.co/TTdN2wp/8rouge.png",
    '8 vert':"https://i.ibb.co/rftH5mF/8vert.png",
    '9 bleu':"https://i.ibb.co/6PNXHdr/9bleu.png",
    '9 jaune':"https://i.ibb.co/pvj5Mnh/9jaune.png",
    '9 rouge':"https://i.ibb.co/3BBdjVL/9rouge.png",
    '9 vert':"https://i.ibb.co/ZJpKHch/9vert.png",
    'ch couleur':"https://i.ibb.co/rm80hJq/changement-de-couleur.png",
    'ch bleu':"https://i.ibb.co/rm80hJq/changement-de-couleur.png",
    'ch jaune':"https://i.ibb.co/rm80hJq/changement-de-couleur.png",
    'ch rouge':"https://i.ibb.co/rm80hJq/changement-de-couleur.png",
    'ch vert':"https://i.ibb.co/rm80hJq/changement-de-couleur.png",
    'inv bleu':"https://i.ibb.co/pdb8Bq5/inversement-de-sensbleu.png",
    'inv jaune':"https://i.ibb.co/bQT6w9H/inversement-de-sensjaune.png",
    'inv rouge':"https://i.ibb.co/3yNgrQx/inversement-de-sensrouge.png",
    'inv vert':"https://i.ibb.co/x2X0fs4/inversement-de-sensvert.png",
    'pass bleu':"https://i.ibb.co/0jNX5yv/passe-ton-tourbleu.png",
    'pass jaune':"https://i.ibb.co/nBBcnrV/passe-ton-tourjaune.png",
    'pass rouge':"https://i.ibb.co/zGwbHKj/passe-ton-tourrouge.png",
    'pass vert':"https://i.ibb.co/1KTYtsg/passe-ton-tourvert.png"
}

emotes = {
    "couleur": "",
    "+4": "🔳 +4",
    "ch": "⬛️ couleur",
    "+2": "+2 ",
    "pass": "🚫",
    "inv": "🔃",
    "rouge": "🟥",
    "bleu": "🟦",
    "jaune": "🟨",
    "vert": "🟩",
    "0": "0️⃣",
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣",
    "6": "6️⃣",
    "7": "7️⃣",
    "8": "8️⃣",
    "9": "9️⃣"
}

bot_name = [
    "Amino",
    "Alcatraz",
    "Rose Blanche",
    "Boo"
]

# f'{emotes[valeur]}{emotes[couleur]}' -> carte normale / action
# f'{emotes[valeur]}' -> +4 / ch couleur

async def valide_intaraction(interaction:discord.Interaction):
    try:
        await interaction.response.send_message()
    except Exception as error:
        pass
        #print(error)


class Carte:
    def __init__(self, couleur: str, valeur: str) -> None:
        self.couleur = couleur
        self.valeur = str(valeur)
        self.url = card_ref[f"{self.valeur} {self.couleur}"]

    def build_str(self):
        res = ""
        for key, value in self.__dict__.items():
            res += f"{key} : {value}\n"

        return res

    def __str__(self):
        return self.build_str()


class Player:
    def __init__(self, ctx: discord.Interaction, bot: bool = False) -> None:
        self.ctx = ctx
        self.cartes = []
        self.id = ctx.user.id if self.ctx!=None else None
        self.nom = ctx.user.name if self.ctx!=None else random.choice(bot_name)
        self.pioche = False
        self.bot = bot
    
    def get_carte(self, couleur: str, valeur: str) -> Carte:
        for carte in self.cartes:
            if carte.valeur == valeur and carte.couleur == couleur:
                return carte
    
    def got_carte_valeur(self, valeur: list):
        if isinstance(valeur, str):
            valeur = [valeur]
        
        for carte in self.cartes:
            if carte.valeur in valeur:
                return True
        
        return False
    
    def got_carte_couleur(self, couleur: list):
        if isinstance(couleur, str):
            couleur = [couleur]

        for carte in self.cartes:
            if carte.couleur == couleur:
                return True

        return False
    
    def has_cartes(self):
        return len(self.cartes)

    def add_carte(self, carte: Carte):
        self.cartes.append(carte)
    
    def delete_carte(self, carte: Carte):
        if carte in self.cartes:
            self.cartes.remove(carte)
    
    def tri_cartes(self):
        ordo = []
        for coul in ["couleur", "bleu", "rouge", "jaune", "vert"]:
            for carte in self.cartes:
                if carte.couleur == coul:
                    ordo.append(carte)

        self.cartes = ordo

    def count_cartes_color(self):
        ordo = {}
        for coul in ["couleur", "bleu", "rouge", "jaune", "vert"]:
            ordo[coul] = 0
            for carte in self.cartes:
                if carte.couleur == coul:
                    ordo[coul] += 1

        return ordo

    def get_embed(self, joueur):
        if self == joueur:
            embed = discord.Embed(title="Choisi une carte :", description=f"Il vous reste {len(self.cartes)} carte{'s' if len(self.cartes)>1 else ''}")
        else:
            embed = discord.Embed(title=f"{joueur.nom} joue...", description=f"Il vous reste {len(self.cartes)} carte{'s' if len(self.cartes)>1 else ''}")
        return embed

    def build_str(self):
        res = ""
        for key, value in self.__dict__.items():
            res += f"{key} : {value}\n"

        return res

    def __str__(self):
        return self.build_str()
    

class Game:
    rules = {
        "noir_cumul": {"label": "Cumule changement de couleur", "description": "permet de cumuler les cartes changement de couleur", "value": True},
        "+4_pass": {"label": "Passe +4", "description": "passe apres un +4", "value": True},
        "+2_pass": {"label": "Passe +2", "description": "passe apres un +2", "value": True},
        "pioche_rejoue": {"label": "Rejouer", "description": "Rejouer après avoir pioché", "value": False},
        "complet_by_bot": {"label": "Complété avec des bot", "description": "Ajoute des bot si il manque des joueurs", "value": True}
    }

    def __init__(self, ctx: discord.Interaction, nom, max_joueur=4) -> None:
        self.ctx = ctx
        self.host = ctx.user
        self.nom = nom
        self.end = False
        self.joueurs = []
        self.joueur_actuel = 0
        self.carte_actuelle = None
        self.somme_plus = 0
        self.started = False
        self.pioche = self.gen_pioche()
        self.max_joueur = max_joueur

    def get_joueur(self, user_id: int) -> Player:
        for joueur in self.joueurs:
            if user_id == joueur.id:
                return joueur
    
    def get_current_joueur(self) -> Player:
        return self.joueurs[self.joueur_actuel]
    
    def get_next_joueur(self) -> Player:
        next_joueur = self.joueur_actuel + 1
        
        if next_joueur >= len(self.joueurs):
            next_joueur = 0
        
        return self.joueurs[next_joueur]

    def get_previous_joueur(self) -> Player:
        next_joueur = self.joueur_actuel - 1

        if next_joueur < 0:
            next_joueur = len(self.joueurs)-1
        
        return self.joueurs[next_joueur]

    def gen_pioche(self):
        pioche = [Carte("bleu", 0), Carte("rouge", 0), Carte("jaune", 0), Carte("vert", 0)]

        for color in ["bleu", "rouge", "jaune", "vert"]:
            for i in range(1, 10):
                pioche.append(Carte(couleur=color, valeur=i))
                pioche.append(Carte(couleur=color, valeur=i))
            
            for action in ["pass", "inv", "+2"]:
                pioche.append(Carte(couleur=color, valeur=action))
                pioche.append(Carte(couleur=color, valeur=action))
            
        for i in range(4):
            pioche.append(Carte(couleur="couleur", valeur="ch"))
            pioche.append(Carte(couleur="couleur", valeur="+4"))
        
        random.shuffle(pioche)

        return pioche

    def add_joueur(self, ctx_joueur: discord.Interaction):
        if len(self.joueurs)>=self.max_joueur:
            return False

        if ctx_joueur==None:
            self.joueurs.append(Player(ctx_joueur, bot=True))
            return True

        if not self.is_in_game(ctx_joueur):
            self.joueurs.append(Player(ctx_joueur))
            return True
        
        return False

    def remove_joueur(self, ctx_joueur: discord.Interaction):
        if self.is_in_game(ctx_joueur):
            self.joueurs.remove(self.get_joueur(ctx_joueur.user.id))
            return True
        
        return False
    
    def is_in_game(self, ctx_joueur: discord.Interaction):
        if self.get_joueur(ctx_joueur.user.id):
            return True

        return False

    def embed_stat(self) -> discord.Embed:
        embed = discord.Embed()
        embed.set_author(name=f"Game : {self.nom}  | Host par : {self.host.name}", icon_url=self.host.avatar.url)
        if not self.started and len(self.joueurs) < 4:
            embed.title = "En attente de joueurs"
            embed.description = f"Nombre de Joueurs : ` {len(self.joueurs)}/{self.max_joueur} `"
            for joueur in self.joueurs:
                embed.add_field(name=f"{joueur.nom}", value='\u200b')
        else:
            embed.title = f"{self.get_current_joueur().nom} joue..."
            if self.carte_actuelle!=None:
                embed.set_image(url=self.carte_actuelle.url)
                if self.carte_actuelle.couleur == "bleu":
                    embed.color=discord.Color.blue()
                elif  self.carte_actuelle.couleur == "rouge":
                    embed.color=discord.Color.red()
                elif  self.carte_actuelle.couleur == "jaune":
                    embed.color=discord.Color.gold()
                elif  self.carte_actuelle.couleur == "vert":
                    embed.color=discord.Color.green()
                else:
                    embed.color=discord.Color.light_grey()
            if not self.end:
                embed.description = f"Prochain joueur : {self.get_next_joueur().nom}"
                for joueur in self.joueurs:
                    embed.add_field(name=f"{joueur.nom} :", value=f"{len(joueur.cartes)} cartes")
        if self.end:
            for joueur in self.joueurs:
                if len(joueur.cartes)==0:
                    embed.title = f"{joueur.nom} a gagné"
                    break

        return embed
    
    def pioche_carte(self) -> Carte:
        return self.pioche.pop()

    def joueur_pioche(self, joueur: Player):
        joueur.add_carte(self.pioche_carte())
    
    def pose_carte(self, carte: Carte):
        self.carte_actuelle = carte

    def deffause_carte(self, joueur: Player, carte: Carte):
        joueur.delete_carte(carte)
    
    def check_rule(self, rule: str):
        return self.rules[rule]
    
    def bot_joue(self, bot: Player):
        jouable = ["pioche"]
        for carte in bot.cartes:
            if self.est_jouable(carte):
                jouable.append(carte)

        if len(jouable) > 1:
            jouable.remove("pioche")
        choix = random.choice(jouable)
        if choix!="pioche" and choix.valeur in ["ch", "+4"]:
            couleur = random.choice(["rouge", "bleu", "jaune", "vert"])
        else:
            couleur = None
        return choix, couleur
    
    def est_jouable(self, carte: Carte) -> bool:
        car = self.carte_actuelle
        
        if not car:
            return True
        
        elif carte == "pioche":
            return True
        
        elif car.valeur == "+2" and self.somme_plus and carte.valeur not in ["+2", "+4", "ch"]:
            return False

        if car.valeur in ["+4", "ch"] and carte.valeur in ["+4", "ch"]:
            return self.check_rule("noir_cumul")

        elif carte.couleur == car.couleur:
            return True

        elif carte.valeur == car.valeur:
            return True
        
        elif carte.couleur == "couleur" and car.valeur == "+2":
            return True
        
        elif carte.couleur == "couleur":
            return True

        return False
    
    def saute_tour(self):
        self.prochain_joueur()
    
    def change_sens(self):
        self.joueurs.reverse()
    
    def plus_2(self):
        self.somme_plus += 2
        next_joueur = self.get_next_joueur()

        if not next_joueur.got_carte_valeur(["+2", "+4", "ch"]):
            for i in range(self.somme_plus):
                self.joueur_pioche(next_joueur)
            
            if self.check_rule("+2_pass"):
                self.saute_tour()
    
            self.somme_plus = 0
    
    def plus_4(self, couleur: str):
        self.somme_plus += 4
        next_joueur = self.get_next_joueur()

        if not next_joueur.got_carte_valeur(["+4"]):
            for _ in range(self.somme_plus):
                self.joueur_pioche(next_joueur)

            if self.check_rule("+4_pass"):
                self.saute_tour()

            self.somme_plus = 0
            self.carte_actuelle.couleur = couleur

    def change_couleur(self, couleur: str):
        self.somme_plus = 0
        self.carte_actuelle.couleur = couleur

    def joue_tour(self, carte: Carte, couleur: str = None) -> Player:
        joueur = self.get_current_joueur()
        joueur.tri_cartes()
        
        if len(self.pioche) <= 0:
            self.pioche = self.gen_pioche()

        if carte == "pioche":
            if self.somme_plus:
                for _ in range(self.somme_plus):
                    self.joueur_pioche(joueur)

                self.somme_plus = 0
            else:
                self.joueur_pioche(joueur)
            
            if not self.rules["pioche_rejoue"]["value"]:
                self.prochain_joueur()
            
            elif self.rules["pioche_rejoue"]["value"] and joueur.pioche:
                self.prochain_joueur()
                
            else:
                joueur.pioche = True

            return self.get_current_joueur()
        
        self.pose_carte(carte)

        if carte.valeur == "ch":
            self.change_couleur(couleur)
        
        elif carte.valeur == "pass":
            self.saute_tour()
        
        elif carte.valeur == "inv":
            self.change_sens()
        
        elif carte.valeur == "+2":
            self.plus_2()
        
        elif carte.valeur == "+4":
            self.plus_4(couleur)
        
        self.deffause_carte(joueur, carte)

        if not joueur.has_cartes():
            self.end = True

        joueur.pioche = False
        self.prochain_joueur()
        self.get_current_joueur().tri_cartes()
        return self.get_current_joueur()

    def start(self):
        if self.rules["complet_by_bot"]["value"]:
            for i in range(self.max_joueur-len(self.joueurs)):
                self.add_joueur(None)
        for joueur in self.joueurs:
            for i in range(7):
                self.joueur_pioche(joueur)

            joueur.tri_cartes()
            # joueur.cartes.append(Carte("couleur", "+4"))

        while self.pioche[-1].valeur in ["+4", "ch", "pass", "inv", "+2"]:
            random.shuffle(self.pioche)
        
        self.pose_carte(self.pioche_carte())
        random.shuffle(self.joueurs)
        self.started = True
        
    def prochain_joueur(self):
        self.joueur_actuel += 1
        if self.joueur_actuel >= len(self.joueurs):
            self.joueur_actuel = 0

    async def update_embed(self):
        await self.ctx.edit_original_response(embed=self.embed_stat())
        if self.end:
            await self.ctx.edit_original_response(view=None)

    async def update_player_embed(self):
        for player in self.joueurs:
            if not player.bot:
                if not self.end and self.started:
                    await player.ctx.edit_original_response(embeds=[self.embed_stat(), player.get_embed(self.get_current_joueur())])
                elif not self.started:
                    await player.ctx.edit_original_response(embed=self.embed_stat())
                else:
                    await player.ctx.edit_original_response(embeds=[self.embed_stat(), discord.Embed(title="Partie terminé")], view=None)
     
    def build_str(self):
        res = ""
        for key, value in self.__dict__.items():
            if key != "pioche":
                res += f"{key} : {value}\n"

        return res

    def __str__(self):
        return self.build_str()


class Games:
    def __init__(self) -> None:
        self.games = []
    
    def create_game(self, ctx: discord.Interaction, nom: str, max_joueur):
        game = Game(ctx, nom, max_joueur)
        self.games.append(game)
        return game

    def end_game(self, ctx: discord.Interaction):
        self.games.remove(self.get_game(ctx))
    
    def get_game(self, ctx: discord.Interaction):
        for game in self.games:
            if game.ctx == ctx:
                return game

    def get_game_by_name(self, nom: discord.Interaction) -> Game:
        for game in self.games:
            if game.nom == nom:
                return game


games = Games()

#------------------------------ View --------------------------------
class Game_view(discord.ui.View):
    def __init__(self, game: Game, timeout=None):
        super().__init__(timeout=timeout)
        self.game = game

    @discord.ui.button(emoji="\u23EF", style=discord.ButtonStyle.primary)
    async def get_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id in [joueur.id  for joueur in self.game.joueurs]:
            try:
                await self.game.get_joueur(interaction.user.id).ctx.delete_original_response()
            except:
                pass
            self.game.get_joueur(interaction.user.id).ctx = interaction
            await interaction.response.send_message(embeds=[self.game.embed_stat(), self.game.get_joueur(interaction.user.id).get_embed(self.game.get_current_joueur())], view=Player_view(self.game) if self.game.get_joueur(interaction.user.id)==self.game.get_current_joueur() else None, ephemeral=True)
        else:
            await valide_intaraction(interaction)

class Uno_view(discord.ui.View):
    def __init__(self, game: Game, timeout=None):
        super().__init__(timeout=timeout)
        self.game = game

    @discord.ui.button(label="Rejoindre", style=discord.ButtonStyle.green)
    async def join_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.game.add_joueur(interaction):
            await interaction.response.send_message(embed=discord.Embed(title="Vous avez bien rejoint, merci de ne pas fermer ce message et d'attendre la debut de la partie"), ephemeral=True)
            await self.game.update_player_embed()
            await self.game.update_embed()
        else:
            pass
        await valide_intaraction(interaction)

    @discord.ui.button(label="Commencer", style=discord.ButtonStyle.grey)
    async def start_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await valide_intaraction(interaction)
        if interaction.user == self.game.host:
            self.game.start()
            await self.game.update_embed()
            await self.game.ctx.edit_original_response(view=Game_view(self.game))
            await self.game.update_player_embed()
            joueur_next = self.game.get_current_joueur()
            while joueur_next.bot and not self.game.end:
                joueur_next = self.game.joue_tour(*self.game.bot_joue(joueur_next))
                await self.game.update_player_embed()
                await self.game.update_embed()
            if not self.game.end:
                await joueur_next.ctx.edit_original_response(view=Player_view(self.game))
    
    @discord.ui.button(label="Règle", style=discord.ButtonStyle.blurple)
    async def rule_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user == self.game.host:
            await interaction.response.send_message(embed=discord.Embed(title="Règle de la game") ,view=Rule_select_view(interaction, self.game), ephemeral=True)
        await valide_intaraction(interaction)

    @discord.ui.button(label="Quitter", style=discord.ButtonStyle.red)
    async def leave_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.game.remove_joueur(interaction):
            await interaction.response.send_message(embed=discord.Embed(title="Vous avez bien quitté"), ephemeral=True)
            await self.game.update_player_embed()
            await self.game.update_embed()
        await valide_intaraction(interaction)

class Cartes_select(discord.ui.Select):
    def __init__(self, game: Game, joueur: Player, options, enable=True) -> None:
        super().__init__(placeholder=f"Choisi une carte", max_values=1, min_values=1, options=options)
        self.game = game
        self.joueur = joueur
        self.enable = enable

    async def callback(self, interaction: discord.Interaction):
        carte_ref = self.values[0]
        couleur = carte_ref.split(" ")[2]
        valeur = carte_ref.split(" ")[1]
        carte = self.joueur.get_carte(couleur=couleur, valeur=valeur)
        if self.game.est_jouable(carte) and self.enable:
            if carte.valeur == "ch" or carte.valeur == "+4":
                await valide_intaraction(interaction)
                #embed = discord.Embed(title="Choisi une carte :", description=f"Il vous reste {len(self.cartes)} carte{'s' if len(self.cartes)>1 else ''}")

                await self.joueur.ctx.edit_original_response(view=Color_view(self.game, carte))
            else:
                await self.joueur.ctx.edit_original_response(view=None)
                await valide_intaraction(interaction) 
                joueur_next = self.game.joue_tour(carte)
                await self.game.update_embed()
                await self.game.update_player_embed()
                #await self.joueur.ctx.edit_original_response(embed=self.joueur.get_embed())
                while joueur_next.bot and not self.game.end:
                    joueur_next = self.game.joue_tour(*self.game.bot_joue(joueur_next))
                    await self.game.update_player_embed()
                    await self.game.update_embed()

                if not self.game.end:
                    await joueur_next.ctx.edit_original_response(view=Player_view(self.game))
        else:
            await valide_intaraction(interaction) 
            pass #ici le joueur choisi une mauvaise carte
        
class Color_view(discord.ui.View):
    def __init__(self, game: Game, carte: Carte, enable=True, timeout=None):
        super().__init__(timeout=timeout)
        self.game = game
        self.player = game.get_current_joueur()
        self.carte = carte
        self.enable = enable

        i=0
        options=[]
        for carte in list(self.player.cartes):
            options.append(discord.SelectOption(label=f"{emotes[carte.valeur]}{emotes[carte.couleur]}", value=f"{i+1} {carte.valeur} {carte.couleur}"))
            i+=1
            if i==25:
                i=0
                self.add_item(Cartes_select(self.game, self.player, options, False))
                options=[]
        if options!=[]:
            self.add_item(Cartes_select(self.game, self.player, options, False))
        
    @discord.ui.button(label="Bleu", style=discord.ButtonStyle.primary)
    async def blue_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await valide_intaraction(interaction)
        await self.send("bleu")
        
    @discord.ui.button(label="Rouge", style=discord.ButtonStyle.red)
    async def red_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await valide_intaraction(interaction)
        await self.send("rouge")

    @discord.ui.button(label="Jaune", style=discord.ButtonStyle.gray)
    async def yellow_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await valide_intaraction(interaction)
        await self.send("jaune")

    @discord.ui.button(label="Vert", style=discord.ButtonStyle.green)
    async def green_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await valide_intaraction(interaction)
        await self.send("vert")

    async def send(self, couleur):
        await self.player.ctx.edit_original_response(view=None)
        joueur_next = self.game.joue_tour(self.carte, couleur)
        await self.game.update_embed()
        #await self.player.ctx.edit_original_response(embed=self.player.get_embed())
        await self.game.update_player_embed()
        if not self.game.end:
            while joueur_next.bot and not self.game.end:
                joueur_next = self.game.joue_tour(*self.game.bot_joue(joueur_next))
                await self.game.update_player_embed()
                await self.game.update_embed()
            if not self.game.end:
                await joueur_next.ctx.edit_original_response(view=Player_view(self.game)) #embed=joueur_next.get_embed()

class Player_view(discord.ui.View):
    def __init__(self, game: Game, timeout=None):
        super().__init__(timeout=timeout)
        self.game = game
        self.player = game.get_current_joueur()
        # print([f"{cart.couleur} {cart.valeur}" for cart in self.player.cartes])
        i=0
        options=[]
        for carte in list(self.player.cartes):
            options.append(discord.SelectOption(label=f"{emotes[carte.valeur]}{emotes[carte.couleur]}", value=f"{i+1} {carte.valeur} {carte.couleur}"))
            i+=1
            if i==25:
                i=0
                self.add_item(Cartes_select(self.game, self.player, options))
                options=[]
        if options!=[]:
            self.add_item(Cartes_select(self.game, self.player, options))

    @discord.ui.button(label="Piocher", style=discord.ButtonStyle.red)
    async def pioche_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await self.player.ctx.edit_original_response(view=None)
        await valide_intaraction(interaction)
        joueur_next = self.game.joue_tour("pioche")
        await self.game.update_player_embed()
        await self.game.update_embed()

        if not self.game.end:
            while joueur_next.bot and not self.game.end:
                joueur_next = self.game.joue_tour(*self.game.bot_joue(joueur_next))
                await self.game.update_player_embed()
                await self.game.update_embed()
            if not self.game.end:
                await joueur_next.ctx.edit_original_response(view=Player_view(self.game))

class Game_select(discord.ui.Select):
    def __init__(self, game: Game, options) -> None:
        super().__init__(placeholder=f"Choisi une game", max_values=1, min_values=0, options=options)
        self.game = game
        

    async def callback(self, interaction: discord.Interaction):
        if not self.game.started:
            if self.values==[]:
                if self.game.remove_joueur(interaction):
                    await interaction.response.send_message(embed=discord.Embed(title="Vous avez bien quitté"), ephemeral=True)
                    await self.game.update_player_embed()
                    await self.game.update_embed()
            else:
                #game_ref = self.values[0]
                #nom = game_ref[len(game_ref.split(" ")[0])+1:]
                if self.game.add_joueur(interaction):
                    await interaction.response.send_message(embed=discord.Embed(title="Vous avez bien rejoint, merci de ne pas fermer ce message et d'attendre la debut de la partie"), ephemeral=False if interaction.guild==None else True)
                    await self.game.update_player_embed()
                    await self.game.update_embed()
        else:
            await interaction.delete_original_response()

        await valide_intaraction(interaction)

class Game_select_view(discord.ui.View):
    def __init__(self, games: Games, timeout=None):
        super().__init__(timeout=timeout)
        self.games = games
        i=0
        options=[]
        for game in list(self.games.games):
            if not game.started:
                options.append(discord.SelectOption(label=f"{game.nom}", description=f"Joueurs : {len(game.joueurs)}/4", value=f"{i+1} {game.nom}"))
                i+=1
                if i==25:
                    i=0
                    self.add_item(Game_select(game, options))
                    options=[]
        if options!=[]:
            self.add_item(Game_select(game, options))

class Rule_select_view(discord.ui.View):
    def __init__(self, ctx: discord.Interaction, game: Game, timeout=None):
        super().__init__(timeout=timeout)
        options=[discord.SelectOption(label=f"{stat['label']} : {'Oui' if stat['value'] else 'Non'}", description=f"{stat['description']}", value=rule) for rule, stat in game.rules.items()]
        self.add_item(Rule_select(ctx, game, options))

class Rule_select(discord.ui.Select):
    def __init__(self,ctx: discord.Interaction, game: Game, options) -> None:
        super().__init__(placeholder=f"Liste des règle", max_values=len(options), min_values=1, options=options)
        self.ctx = ctx
        self.game = game
        
    async def callback(self, interaction: discord.Interaction):
        for regle in self.values:
            self.game.rules[regle]["value"] = not self.game.rules[regle]["value"]
        await valide_intaraction(interaction)
        await self.ctx.delete_original_response()

@Lib.event.event()
async def on_app_command_error(ctx: discord.Interaction, error: discord.app_commands.AppCommandError):
    print(ctx.data, error)
        

@Lib.app.slash(name="host", description="créé une nouvelle partie de uno", force_name=True)
async def uno(ctx: discord.Interaction, nom: str="player's game", max_joueur: int=4):
    try:
        game = games.create_game(ctx, nom, max_joueur)
        await ctx.response.send_message(embed=game.embed_stat(), view=Uno_view(game))
    except Exception as error:
        print(error)
    
@Lib.app.slash(name="join", description="rejoingnez une partie de uno")
async def join(ctx: discord.Interaction):
    try:
        await ctx.response.send_message(embed=discord.Embed(title="Salon"), view=Game_select_view(games), ephemeral=True)
    except Exception as error:
        print(error)