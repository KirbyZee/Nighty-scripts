import random

@nightyScript(
    name="Dexter Roll",
    author="Kirby631",
    description="Randomly sends Dexter-themed edits or GIFs with weighted chances. Avoids repeating the same roll twice in a row.",
    usage="<p>dexter"
)
def dexter_roll_script():
    """
    DEXTER ROLL (No Repeat)
    -----------------------
    Sends a random Dexter-themed edit or GIF with rarity chances.
    Prevents rolling the same clip twice in a row.
    """

    MEDIA_POOL = [
         {"title": "who's number one now", "url": "https://getsharex.co/usZ4H", "chance": 50},
          {"title": "Peak friendship", "url": "https://getsharex.co/c45PP", "chance": 50},
         {"title": "Dexter is funny!", "url": "https://getsharex.co/WpjAE", "chance": 50},
         {"title": "I own you!!", "url": "https://getsharex.co/ihHt7", "chance": 50},
        {"title": "Court!", "url": "https://getsharex.co/CWzMW", "chance": 50},
        {"title": "That one dexter edit!", "url": "https://getsharex.co/04lmL", "chance": 50},
        {"title": "Bay Harbor Butcher x doakes edit!", "url": "https://getsharex.co/lr4Sr", "chance": 50},
        {"title": "Brian Dexter edit!", "url": "https://getsharex.co/D3FHk", "chance": 50},
        {"title": "Doakes hot daddy edit!", "url": "https://getsharex.co/OuJLq", "chance": 50},
        {"title": "Joey Quinn edit!", "url": "https://getsharex.co/a26Is", "chance": 50},
        {"title": "Uncommon Doakes Suspicion", "url": "https://getsharex.co/IGq2D", "chance": 50},
        {"title": "Tonight's the night 🌙", "url": "https://getsharex.co/j6AOF", "chance": 15},
        {"title": "Legendary sussy Doakes 💀", "url": "https://getsharex.co/knBw3", "chance": 5},
        {"title": "❤️ Mythical long-haired Doakes ❤️", "url": "https://getsharex.co/eo0v8", "chance": 3}
    ]

    # Store the last rolled title globally (per session)
    last_roll = {"title": None}

    def weighted_choice(pool):
        total = sum(item["chance"] for item in pool)
        r = random.uniform(0, total)
        upto = 0
        for item in pool:
            if upto + item["chance"] >= r:
                return item
            upto += item["chance"]
        return pool[-1]

    @bot.command(name="dexter", description="Rolls a random Dexter edit or GIF (no repeats).")
    async def dexter_command(ctx, *, args: str = ""):
        await ctx.message.delete()


        # Reroll if it’s the same as the last one
        roll = weighted_choice(MEDIA_POOL)
        reroll_count = 0
        while last_roll["title"] == roll["title"] and reroll_count < 5:
            roll = weighted_choice(MEDIA_POOL)
            reroll_count += 1

        last_roll["title"] = roll["title"]

        current_private = getConfigData().get("private")
        updateConfigData("private", False)

        try:
            await forwardEmbedMethod(
                channel_id=ctx.channel.id,
                title=roll["title"],
                content=(
                    f"# 🔪 Dexter Roll Result!\n\n"
                    f"**{roll['title']}**\n\n"
                    f"*Chance:* {roll['chance']}"
                )
            )
            await ctx.send(roll["url"])

            print(f"✅ Sent Dexter roll: {roll['title']} ({roll['url']})", type_="SUCCESS")

        except Exception as e:
            await ctx.send(f"Error sending Dexter roll: {e}", delete_after=5)
            print(f"❌ Error sending roll: {e}", type_="ERROR")

        finally:
            updateConfigData("private", current_private)

    print("🎯 Dexter Roll (No Repeat) loaded successfully.", type_="SUCCESS")

dexter_roll_script()
