import discord
from discord.ext import commands
import requests

# Yapay Zeka kısmı
from ai_model import classify_image  # Basitleştirilmiş modelin bulunduğu dosya

# Discord Botu ayarları
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot giriş yaptı: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.lower().endswith(("jpg", "jpeg", "png")):
                # Görselin URL'sini al
                image_url = attachment.url

                # Yapay zeka modelini çağır
                label, score = classify_image(image_url)

                # Sonucu Discord kanalına gönder
                await message.channel.send(f"📷 Bu görseldeki hayvan: **{label}** (%{score:.1f} güvenle)")

    await bot.process_commands(message)

# Botu çalıştır
bot.run("cf84f31f8ad540369afec653419db4ec31aa993563e22c802e182d7ba1ac3fa8")