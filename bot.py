#!/usr/bin/env python
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import random
import glob
import mydown
import os
import youtube_downloader 

client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def enes(ctx):
    await ctx.send(f"print(\"enes\")")

@client.command()
async def faruk(ctx):
    await ctx.send("ADAM GIBI ADAM Brad Pitt yaninda bok yemis")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency *1000)}ms")

@client.command(aliases = ["8ball","test"] )
async def _8balls(ctx, *, question):
    responce = ["Kesinlikle","Kesinlikle öyle","Kuşkusuz"," Evet - elbette","Bana güvenebilirsin","Gördüğüm kadarıyla, evet","Çoğunlukla","Dışarıdan iyi görünüyor","Evet","Belirtiler olduğu yönünde","Biraz belirsiz, tekrar dene","Daha Sonra tekrar dene","Şimdi söylemesem daha iyi","Şimdi kehanette bulunamam","Konsantre ol ve tekrar sor","Bana öyle bakma","Yanıtım hayır","Kaynaklarım hayır diyor","Pek iyi görünmüyor","Çok şüpheli"]
    if 'özgür' in question.lower():
        await ctx.send("Yaraticim hakkinda soru cevaplamiyorum kendisi mükemmel bir insandir")    
    else:
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responce)}")

@client.command()
async def uf(ctx):
    await ctx.send("ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜFFFFFFFFFFf")

@client.command()
async def kisiselgelisim(ctx):
    await ctx.send("EAT\nSIKIS\nDERS\nSPOR\nSIKIS\nREPEAT")

@client.command()
async def nofap(ctx):
    file = open("nofap.txt","r")
    content = file.read()
    content_list = content.splitlines()
    await ctx.send(random.choice(content_list))
    f.close()
    
@client.command()
async def clear(ctx,amount = 200):
    await ctx.channel.purge(limit=amount)


@client.command()
async def motivasyon(ctx):
    file = open("turkmotivasyon.txt","r")
    content = file.read()
    content_list = content.splitlines()
    await ctx.send(random.choice(content_list))
    f.close()

@client.command()
async def atasozu(ctx):
    file = open("atasozu.txt","r")
    content = file.read()
    content_list = content.splitlines()
    await ctx.send(random.choice(content_list))
    f.close()

@client.command()
async def twittervideo(ctx,*,theurl):
    twitter_dl = mydown.TwitterDownloader(theurl,"videos",500)
    twitter_dl.download()
    videos = [f for f in glob.glob("videos/*.mp4")]
    videonamearr = [discord.File(videos[0])]
    await ctx.send(files=videonamearr)
    os.remove(videos[0])

@client.command()
async def youtubevideo(ctx,*,theurl):
    try:
        youtube_downloader.download_video(theurl,"high")
    except:
        youtube_downloader.download_video(theurl,"medium")
    else:
        youtube_downloader.download_video(theurl,"low")
    await ctx.send("Downloaded")

@client.command()
async def image(ctx):
    images= [f for f in glob.glob("images/*.jpeg")]
    arr = [discord.File(random.choice(images))]
    await ctx.send(files=arr)

client.run("NzUzNjkxNjE2OTQ1ODk3NDgy.X1p4BA.bV9hvzqcJU-VdtZeiwZyu6jf1IU") //Here goes your discord token


