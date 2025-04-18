import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def alma(ctx):
    opcoes = [
        {
            "mensagem": "-#               _ _                                                               ౨ৎ ‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ ‎ ₊ ‎ ‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ 𓈒 ◌
_ _ 
-# _ _                      ┄          
_ _ _ _ **₊˚ ‿︵‿︵‿︵୨୧ · · :casinha: · · ୨୧‿︵‿︵‿︵ ˚₊**
_ _ 
_ _ 
_ _ _ _                   ***MEUS PARABÉNS!!!***
_ _ 
_ _ _ _        **◎** *Sua Alma é uma **__Experiente__**!*
_ _ 
> -#  - *São aqueles que já passaram tempo suficiente no circo para compreender suas regras e horrores, [Sabia mais…](https://discordapp.com/channels/1352404572114653244/1354250241322516550)*",
            "imagem": "https://media.discordapp.net/attachments/1149801910895910912/1362921665071288420/729_Sem_Titulo_20250325150216.jpg?ex=68042736&is=6802d5b6&hm=5c764f3fb95c6fe692225934e73a8cd4d6256454ea7c70ba1a11705e822bee74&=&format=webp&width=1860&height=620"
        },
        {
            "mensagem": "-#               _ _                                                               ౨ৎ ‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ ‎ ₊ ‎ ‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ 𓈒 ◌
_ _ 
-# _ _                      ┄          
_ _ _ _ **₊˚ ‿︵‿︵‿︵୨୧ · · :casinha: · · ୨୧‿︵‿︵‿︵ ˚₊**
_ _ 
_ _ 
_ _ _ _                   ***MEUS PARABÉNS!!!***
_ _ 
_ _ _ _        **◎** *Sua Alma é uma **__Recém - Chegada__**!*
_ _ 
> -#  - *São aqueles que já acabaram de morrer e se despertaram nesse circo sem entender o que está acontecendo, [Sabia mais…](https://discordapp.com/channels/1352404572114653244/1354250241322516550)*",
            "imagem": "https://media.discordapp.net/attachments/1149801910895910912/1362921665071288420/729_Sem_Titulo_20250325150216.jpg?ex=68042736&is=6802d5b6&hm=5c764f3fb95c6fe692225934e73a8cd4d6256454ea7c70ba1a11705e822bee74&=&format=webp&width=1860&height=620"
        },
        {
            "mensagem": "-#               _ _                                                               ౨ৎ ‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ ‎ ₊ ‎ ‎ ‎ ‎ ‎ ‎ ‎   ‎ ‎ ‎ 𓈒 ◌
_ _ 
-# _ _                      ┄          
_ _ _ _ **₊˚ ‿︵‿︵‿︵୨୧ · · :casinha: · · ୨୧‿︵‿︵‿︵ ˚₊**
_ _ 
_ _ 
_ _ _ _                   ***MEUS PARABÉNS!!!***
_ _ 
_ _ _ _        **◎** *Sua Alma é uma **__Corrompida__**!*
_ _ 
> -#  - *Foram tomadas pelo medo, ganância ou desespero, [Sabia mais…](https://discordapp.com/channels/1352404572114653244/1354250241322516550)*",
            "imagem": "https://media.discordapp.net/attachments/1149801910895910912/1362922657175175219/729_Sem_Titulo3_20250418194750.jpg?ex=68042823&is=6802d6a3&hm=9431444d67d24d66324ea05d4279af6dec6c6560fcac7a6eec7f29eae3ed1011&=&format=webp&width=1860&height=620"
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

"""

    escolha = random.choice(opcoes)

    embed = discord.Embed(
        title="🕊️ Voz da Alma",
        description=escolha["mensagem"],
        color=0x9b59b6
    )
    embed.set_image(url=escolha["imagem"])
    await ctx.send(embed=embed)

# Coloque o token do seu bot aqui
bot.run("SEU_TOKEN_AQUI")
