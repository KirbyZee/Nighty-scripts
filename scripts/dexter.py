import random

@nightyScript(
    name="Dexter Roll",
    author="Kirby631",
    description="Randomly sends Dexter-themed edits or GIFs with weighted chances.",
    usage="<p>dexter"
)
def dexter_roll_script():
    """
    DEXTER ROLL
    -----------
    Sends a random Dexter-themed edit or GIF with rarity chances.
"""


  
    MEDIA_POOL = [
        {"title": "Bay Harbor Butcher edit!", "url": "https://getsharex.co/CWzMW", "chance": 50},
        {"title": "Bay Harbor Butcher edit!", "url": "https://getsharex.co/04lmL", "chance": 50},
        {"title": "Bay Harbor Butcher edit!", "url": "https://getsharex.co/lr4Sr", "chance": 50},
        {"title": "Brian Dexter edit!", "url": "https://getsharex.co/D3FHk", "chance": 50},
        {"title": "Doakes hot daddy edit!", "url": "https://getsharex.co/OuJLq", "chance": 50},
        {"title": "Joey Quinn edit!", "url": "https://getsharex.co/a26Is", "chance": 50},
        {"title": "Uncommon Doakes Suspicion", "url": "https://getsharex.co/IGq2D", "chance": 50},
        {"title": "Tonight's the night 🌙", "url": "https://getsharex.co/j6AOF", "chance": 15},
        {"title": "Legendary sussy Doakes 💀", "url": "https://getsharex.co/knBw3", "chance": 5},
        {"title": "❤️ Mythical long-haired Doakes ❤️", "url": "https://getsharex.co/eo0v8", "chance": 3}
    ]

 
    def weighted_choice(pool):
        total = sum(item["chance"] for item in pool)
        r = random.uniform(0, total)
        upto = 0
        for item in pool:
            if upto + item["chance"] >= r:
                return item
            upto += item["chance"]
        return pool[-1]

    @bot.command(name="dexter", description="Rolls a random Dexter edit or GIF.")
    async def dexter_command(ctx, *, args: str = ""):
        await ctx.message.delete()
        roll = weighted_choice(MEDIA_POOL)

        current_private = getConfigData().get("private")
        updateConfigData("private", False)

        try:
        
            await forwardEmbedMethod(
                channel_id=ctx.channel.id,
                title=roll["title"],
                content=(
                    f"# 🔪 Dexter Roll Result!\n\n"
                    f"**{roll['title']}**\n\n"
                    f"*Chance:* `{roll['chance']}`"
                )
            )

           
            await ctx.send(roll["url"])

            print(f"✅ Sent Dexter roll: {roll['title']} ({roll['url']})", type_="SUCCESS")

        except Exception as e:
            await ctx.send(f"Error sending Dexter roll: {e}", delete_after=5)
            print(f"❌ Error sending roll: {e}", type_="ERROR")

        finally:
            updateConfigData("private", current_private)

    print("🎯 Dexter Roll loaded successfully.", type_="SUCCESS")

dexter_roll_script()
