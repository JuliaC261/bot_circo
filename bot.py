import discord
from discord.ext import commands
import random
import os  # <--- Adicionado

# Configuração do bot
TOKEN = os.getenv("TOKEN")  # Certifique-se de ter configurado a variável de ambiente TOKEN
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def alma(ctx):
    opcoes = [
        {
            "mensagem": (
                "‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ ‎ ₊ ‎ ‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ 𓈒 ◌\n"
                "\n"
                "┄\n"
                "⠀⠀⠀⠀⠀**₊˚ ‿︵‿︵‿︵୨୧ · · :casinha: · · ୨୧‿︵‿︵‿︵ ˚₊**\n"
                "\n"
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀***MEUS PARABÉNS!!!***\n"
                "\n"
                "⠀⠀⠀⠀**◎** *Sua Alma é uma **__Recém - Chegada__***!*\n"
                "\n"
                "> -# *São aqueles que já acabaram de morrer e se despertaram nesse circo sem entender o que está acontecendo, [Saiba mais…](https://discordapp.com/channels/1352404572114653244/1354250241322516550)*"
            ),
            "imagem": "https://media.discordapp.net/attachments/1149801910895910912/1362921665071288420/729_Sem_Titulo_20250325150216.jpg"
        },
        {
            "mensagem": (
                "‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ ‎ ₊ ‎ ‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ 𓈒 ◌\n"
                "\n"
                "┄\n"
                "⠀⠀⠀⠀⠀**₊˚ ‿︵‿︵‿︵୨୧ · · :casinha: · · ୨୧‿︵‿︵‿︵ ˚₊**\n"
                "\n"
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀***MEUS PARABÉNS!!!***\n"
                "\n"
                "⠀⠀⠀⠀**◎** *Sua Alma é uma **__Experiente__***!*\n"
                "\n"
                "> -# *São aqueles que já passaram tempo suficiente no circo para compreender suas regras e horrores, [Saiba mais…](https://discordapp.com/channels/1352404572114653244/1354250241322516550)*"
            ),
            "imagem": "https://media.discordapp.net/attachments/1149801910895910912/1362921455716663417/729_Sem_Titulo_20250325170905.jpg?ex=68042704&is=6802d584&hm=5277f83cb25273eb00b9fb86fc8c9d84ebc0662cf91fe959b1ef22a36737caf2&=&format=webp&width=1860&height=620"
        },
        {
            "mensagem": (
                "‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ ‎ ₊ ‎ ‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ 𓈒 ◌\n"
                "\n"
                "┄\n"
                "⠀⠀⠀⠀⠀**₊˚ ‿︵‿︵‿︵୨୧ · · :casinha: · · ୨୧‿︵‿︵‿︵ ˚₊**\n"
                "\n"
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀***MEUS PARABÉNS!!!***\n"
                "\n"
                "⠀⠀⠀⠀**◎** *Sua Alma é uma **__Corrompida__***!*\n"
                "\n"
                "> -# *Foram tomadas pelo medo, ganância ou desespero, [Saiba mais…](https://discordapp.com/channels/1352404572114653244/1354250241322516550)*"
            ),
            "imagem": "https://media.discordapp.net/attachments/1149801910895910912/1362922657175175219/729_Sem_Titulo3_20250418194750.jpg"
        },
    ]

    
    pesos = [60, 30, 10]  

    escolha = random.choices(opcoes, weights=pesos, k=1)[0]

    embed = discord.Embed(
        title=" ",
        description=escolha["mensagem"],
        color=0x7e0e01
    )
    embed.set_image(url=escolha["imagem"])
    await ctx.send(embed=embed)

@bot.command()
async def função(ctx):
    categorias = {
        "comum": {
            "peso": 60,
            "funcoes": [
                "Palhaço", "Malabarista", "Monociclista", "Cantor", "Dançarino", "Mímico", "Ator"
            ]
        },
        "incomum": {
            "peso": 30,
            "funcoes": [
                "Equilibrista", "Acrobata", "Contorcionista", "Pernas-De-Pau", "Tapezista", "Marionetista"
            ]
        },
        "rara": {
            "peso": 10,
            "funcoes": [
                "Mágico", "Dominador de Animais", "Engolidor de Espadas", "Faquir", "Fortão"
            ]
        }
    }

    # 1. Escolher a categoria com base nos pesos
    nomes_categorias = list(categorias.keys())
    pesos_categorias = [categorias[cat]["peso"] for cat in nomes_categorias]
    categoria_escolhida = random.choices(nomes_categorias, weights=pesos_categorias, k=1)[0]

    # 2. Escolher uma função dentro da categoria sorteada
    funcao_escolhida = random.choice(categorias[categoria_escolhida]["funcoes"])

    # 3. Mensagem padrão com a função escolhida
    mensagem = (
        "‎                                    ౨ৎ   ₊ 𓈒 ◌\n"
        "                      ┄          ┄\n"
        "⠀⠀⠀⠀⠀**₊˚ ‿︵‿︵‿︵୨୧ · · ⭐ · · ୨୧‿︵‿︵‿︵ ˚₊**\n\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀***MEUS PARABÉNS!!!***\n\n"
        f"⠀⠀⠀⠀ **◎** *Sua Função é  **__{funcao_escolhida}__**!*\n"
        "> -# ****[Saiba mais…](https://discord.com/channels/1352404572114653244/1354451156071612596)****"
    )

    imagem = "https://media.discordapp.net/attachments/1149801910895910912/1363672072471056475/A4H1Wk1U4BCeAAAAAElFTkSuQmCC.png"

    # 4. Criar embed
    embed = discord.Embed(
        title=" ",
        description=mensagem,
        color=0x7e0e01
    )
    embed.set_image(url=imagem)

    # 5. Enviar
    await ctx.send(embed=embed)

# Inicia o bot
bot.run(TOKEN)
