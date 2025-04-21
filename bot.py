import discord
from discord.ext import commands
import random
import os  
import json # <--- Adicionado

# Configuração do bot
TOKEN = os.getenv("TOKEN")  # COnfigurar variável TOKEN em variaveis globais no railway
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
                "> -# - *São aqueles que já acabaram de morrer e se despertaram nesse circo sem entender o que está acontecendo, [Saiba mais…](https://discordapp.com/channels/1352404572114653244/1354250241322516550)*"
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
                "> -# - *São aqueles que já passaram tempo suficiente no circo para compreender suas regras e horrores, [Saiba mais…](https://discordapp.com/channels/1352404572114653244/1354250241322516550)*"
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
                "> -# - *Foram tomadas pelo medo, ganância ou desespero, [Saiba mais…](https://discordapp.com/channels/1352404572114653244/1354250241322516550)*"
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

pesos_raridade = {
    "comum": 60,
    "incomum": 30,
    "rara": 10
}

# Carregar funções do JSON
def carregar_funcoes():
    if not os.path.exists("funcoes.json"):
        with open("funcoes.json", "w") as f:
            json.dump({"comum": [], "incomum": [], "rara": []}, f)
    with open("funcoes.json", "r") as f:
        return json.load(f)

# Salvar funções no JSON
def salvar_funcoes(dados):
    with open("funcoes.json", "w") as f:
        json.dump(dados, f, indent=4)

@bot.command()
async def adicionar(ctx, *, args):
    try:
        partes = args.rsplit(" ", 1)
        nome = partes[0].strip()
        raridade = partes[1].strip().lower()
        
        if raridade not in pesos_raridade:
            await ctx.send("Raridade inválida. Use: `comum`, `incomum`, ou `rara`.")
            return
        
        dados = carregar_funcoes()
        if nome in dados[raridade]:
            await ctx.send(f"A função **{nome}** já existe na categoria **{raridade}**!")
            return
        
        dados[raridade].append(nome)
        salvar_funcoes(dados)
        await ctx.send(f"Função **{nome}** adicionada com sucesso como **{raridade}**!")
    except Exception as e:
        await ctx.send("Erro ao adicionar função. Use o formato: `!adicionar Nome Da Função raridade`")

@bot.command()
async def remover(ctx, *, args):
    try:
        partes = args.rsplit(" ", 1)
        nome = partes[0].strip()
        raridade = partes[1].strip().lower()

        if raridade not in pesos_raridade:
            await ctx.send("Raridade inválida. Use: `comum`, `incomum`, ou `rara`.")
            return

        dados = carregar_funcoes()

        if nome not in dados[raridade]:
            await ctx.send(f"A função **{nome}** não existe na categoria **{raridade}**.")
            return

        dados[raridade].remove(nome)
        salvar_funcoes(dados)
        await ctx.send(f"Função **{nome}** removida com sucesso da categoria **{raridade}**!")
    except Exception as e:
        await ctx.send("Erro ao remover função. Use o formato: `!remover Nome Da Função raridade`")

@bot.command()
async def função(ctx):
    categorias = carregar_funcoes()

    # Garantir que tem funções em pelo menos uma categoria
    todas_vazias = all(len(funcoes) == 0 for funcoes in categorias.values())
    if todas_vazias:
        await ctx.send("Nenhuma função cadastrada ainda!")
        return

    nomes_categorias = list(categorias.keys())
    pesos_categorias = [pesos_raridade[cat] for cat in nomes_categorias]

    # Escolher uma categoria com base no peso
    categoria_escolhida = random.choices(nomes_categorias, weights=pesos_categorias, k=1)[0]

    # Se a categoria estiver vazia, escolher uma com funções
    while not categorias[categoria_escolhida]:
        categoria_escolhida = random.choice([
            cat for cat in nomes_categorias if categorias[cat]
        ])

    funcao_escolhida = random.choice(categorias[categoria_escolhida])

    # Mensagem padrão com a função escolhida
    mensagem = (
                "ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ౨ৎㅤㅤㅤㅤㅤㅤㅤㅤ₊ㅤㅤㅤㅤㅤㅤㅤㅤ𓈒 ◌\n"
                "┄\n"
                "⠀⠀⠀⠀⠀**₊˚ ‿︵‿︵‿︵୨୧ · · :casinha: · · ୨୧‿︵‿︵‿︵ ˚₊**\n"
                "\n"
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀***MEUS PARABÉNS!!!***\n"
                "\n"
                f"⠀⠀⠀⠀**◎** *Sua Função é **__{funcao_escolhida}__***!*\n"
                "\n"
        "> -# - ***[Saiba mais…](https://discord.com/channels/1352404572114653244/1353079696325349478)***"
    )

    imagem = "https://media.discordapp.net/attachments/1149801910895910912/1363672072471056475/A4H1Wk1U4BCeAAAAAElFTkSuQmCC.png"

    # Criar embed
    embed = discord.Embed(title=" ", description=mensagem, color=0x7e0e01)
    embed.set_image(url=imagem)
    await ctx.send(embed=embed)

# Inicia o bot
bot.run(TOKEN)
