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
    def __init__(self, ctx: discord.Interaction) -> None:
        self.ctx = ctx
        self.cartes = []
        self.id = ctx.user.id
    
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

    def get_embed(self):
        emebd = discord.Embed(title="Choisi une carte :", description=f"Il vous reste {len(self.cartes)} carte{'s' if len(self.cartes)>1 else ''}")
        return emebd

    def build_str(self):
        res = ""
        for key, value in self.__dict__.items():
            res += f"{key} : {value}\n"

        return res

    def __str__(self):
        return self.build_str()
    

class Game:
    def __init__(self, ctx: discord.Interaction) -> None:
        self.ctx = ctx
        self.host = ctx.user
        self.end = False
        self.joueurs = []
        self.joueur_actuel = 0
        self.carte_actuelle = None
        self.somme_plus = 0
        self.started = False
        self.pioche = self.gen_pioche()

    def get_joueur(self, user_id: int):
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

    def embed_stat(self):
        embed = discord.Embed()
        if not self.started and len(self.joueurs) < 4:
            embed.title = "En attente de joueurs"
            embed.description = f"Nombre de Joueurs : ` {len(self.joueurs)}/4 `"
        else:
            embed.title = f"{self.joueurs[0].ctx.user.name} joue..."
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

        return embed
    
    def pioche_carte(self):
        return self.pioche.pop()

    def joueur_pioche(self, joueur: Player):
        joueur.add_carte(self.pioche_carte())
    
    def pose_carte(self, carte: Carte):
        self.carte_actuelle = carte

    def deffause_carte(self, joueur: Player, carte: Carte):
        joueur.delete_carte(carte)
    
    def est_jouable(self, carte: Carte):
        car = self.carte_actuelle
        print(carte)
        
        if not car:
            return True
        
        elif carte == "pioche":
            print("cas 1")
            return True
        
        elif car.valeur == "+2" and self.somme_plus and carte.valeur not in ["+2", "+4", "ch"]:
            print("cas 2", self.somme_plus)
            return False

        if car.valeur in ["+4", "ch"] and carte.valeur in ["+4", "ch"]:
            print("cas 3")
            return False

        elif carte.couleur == car.couleur:
            print("cas 4")
            return True

        elif carte.valeur == car.valeur:
            print("cas 5")
            return True
        
        elif carte.couleur == "couleur" and car.valeur == "+2":
            print("cas 6")
            return True
        
        elif carte.couleur == "couleur":
            print("cas 7")
            return True

        print("cas fin")
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
                
            self.saute_tour()
            self.somme_plus = 0
    
    def plus_4(self, couleur: str):
        self.somme_plus += 4

        for i in range(self.somme_plus):
            self.joueur_pioche(self.get_next_joueur())

        self.saute_tour()
        self.somme_plus = 0
        self.carte_actuelle.couleur = couleur

    def change_couleur(self, couleur: str):
        self.somme_plus = 0
        self.carte_actuelle.couleur = couleur

    def joue_tour(self, carte: Carte, couleur: str = None) -> Player:
        joueur = self.get_current_joueur()

        if len(self.pioche) <= 0:
            self.pioche = self.gen_pioche()

        if carte == "pioche":
            if self.somme_plus:
                for i in range(self.somme_plus):
                    self.joueur_pioche(joueur)

                self.somme_plus = 0
            else:
                self.joueur_pioche(joueur)

            self.prochain_joueur()
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

        self.prochain_joueur()
        return self.get_current_joueur()

    def start(self):
        for joueur in self.joueurs:
            for i in range(7):
                self.joueur_pioche(joueur)
            
            joueur.cartes.append(Carte("couleur", "+4"))

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
    
    def create_game(self, ctx: discord.Interaction):
        game = Game(ctx)
        self.games.append(game)
        return game

    def end_game(self, ctx: discord.Interaction):
        self.games.remove(self.get_game(ctx))
    
    def get_game(self, ctx: discord.Interaction):
        for game in self.games:
            if game.ctx == ctx:
                return game


games = Games()

#------------------------------ View --------------------------------

class Uno_view(discord.ui.View):
    def __init__(self, game: Game, timeout=180):
        super().__init__(timeout=timeout)
        self.game = game

    @discord.ui.button(label="Rejoindre", style=discord.ButtonStyle.primary)
    async def join_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.game.add_joueur(interaction):
            await interaction.response.send_message(embed=discord.Embed(title="Vous avez bien rejoint, merci de ne pas fermer ce message et d'attendre la debut de la partie"), ephemeral=True)
        else:
            pass

        await self.game.update_embed()
        await valide_intaraction(interaction)

    @discord.ui.button(label="Commencer", style=discord.ButtonStyle.grey)
    async def start_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        self.game.start()
        await self.game.update_embed()
        await self.game.get_current_joueur().ctx.edit_original_response(embed=self.game.get_current_joueur().get_embed(), view=Player_view(self.game))
        await valide_intaraction(interaction)

    @discord.ui.button(label="Quitter", style=discord.ButtonStyle.red)
    async def leave_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.game.remove_joueur(interaction):
            await interaction.response.send_message(embed=discord.Embed(title="Vous avez bien quitté"), ephemeral=True)
        await self.game.update_embed()
        await valide_intaraction(interaction)


class Cartes_select(discord.ui.Select):
    def __init__(self, game: Game, joueur: Player, options) -> None:
        super().__init__(placeholder=f"Choisi une carte",max_values=1,min_values=1,options=options)
        self.game = game
        self.joueur = joueur

    async def callback(self, interaction: discord.Interaction):
        carte_ref = self.values[0]
        couleur = carte_ref.split(" ")[2]
        valeur = carte_ref.split(" ")[1]
        carte = self.joueur.get_carte(couleur=couleur, valeur=valeur)
        if self.game.est_jouable(carte):
            if carte.valeur == "ch" or carte.valeur == "+4":
                await valide_intaraction(interaction)
                await self.joueur.ctx.edit_original_response(view=Color_view(self.game, carte))
            else:
                await self.joueur.ctx.edit_original_response(view=None)
                await valide_intaraction(interaction) 
                joueur_next = self.game.joue_tour(carte)
                await self.game.update_embed()
                await self.joueur.ctx.edit_original_response(embed=self.joueur.get_embed())
                await joueur_next.ctx.edit_original_response(embed=joueur_next.get_embed(), view=Player_view(self.game))
        else:
            await valide_intaraction(interaction) 
            pass #ici le joueur choisi une mauvaise carte
        
class Color_view(discord.ui.View):
    def __init__(self, game: Game, carte: Carte, timeout=180):
        super().__init__(timeout=timeout)
        self.game = game
        self.player = game.get_current_joueur()
        self.carte = carte
        
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
        await self.player.ctx.edit_original_response(embed=self.player.get_embed())
        await joueur_next.ctx.edit_original_response(embed=joueur_next.get_embed(), view=Player_view(self.game))


class Player_view(discord.ui.View):
    def __init__(self, game: Game, timeout=180):
        super().__init__(timeout=timeout)
        self.game = game
        self.player = game.get_current_joueur()
        print([f"{cart.couleur} {cart.valeur}" for cart in self.player.cartes])
        i=0
        options=[]
        for carte in list(self.player.cartes):
            options.append(discord.SelectOption(label=f"{i+1}) {carte.valeur} {carte.couleur}"))
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
        await self.game.update_embed()
        await self.player.ctx.edit_original_response(embed=self.player.get_embed())
        await joueur_next.ctx.edit_original_response(embed=joueur_next.get_embed(), view=Player_view(self.game))


@Lib.app.slash(name="uno", description="créé une nouvelle partie de uno", force_name=True)
async def uno(ctx: discord.Interaction):
    try:
        game = games.create_game(ctx)
        await ctx.response.send_message(embed=game.embed_stat(), view=Uno_view(game))
    except Exception as error:
        print(error)
    
