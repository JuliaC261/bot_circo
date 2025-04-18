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

     # Defina os pesos: [Recém-Chegada, Experiente, Corrompida]
    pesos = [60, 30, 10]  # ou qualquer outra proporção que você quiser

    escolha = random.choices(opcoes, weights=pesos, k=1)[0]

    embed = discord.Embed(
        title=" ",
        description=escolha["mensagem"],
        color=0x7e0e01
    )
    embed.set_image(url=escolha["imagem"])
    await ctx.send(embed=embed)

# Ative esta função depois se quiser usá-la (remova os três aspas):
"""
@bot.command()
async def função(ctx):
    opcoes = [
        {
            "mensagem": "A alma sussurra verdades antigas...",
            "imagem": "https://exemplo.com/imagem-alma1.jpg"
        },
        {
            "mensagem": "Você escuta o eco da alma.",
            "imagem": "https://exemplo.com/imagem-alma2.jpg"
        },
        {
            "mensagem": "A alma responde em silêncio profundo.",
            "imagem": "https://exemplo.com/imagem-alma3.jpg"
        },
        {
            "mensagem": "Fragmentos de alma se manifestam.",
            "imagem": "https://exemplo.com/imagem-alma4.jpg"
        },
    ]

    escolha = random.choice(opcoes)

    embed = discord.Embed(
        title="⚙️ Função Executada",
        description=escolha["mensagem"],
        color=0x3498db
    )
    embed.set_image(url=escolha["imagem"])
    await ctx.send(embed=embed)
"""

# Inicia o bot
bot.run(TOKEN)
