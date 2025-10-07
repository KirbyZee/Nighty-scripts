import random

@nightyScript(
    name="Dexter Roll",
    author="Kirby631",
    description="Randomly sends Dexter-themed edits or GIFs with weighted chances. Avoids repeating the same roll twice in a row.",
    usage="<p>dexter [help]"
)
def dexter_roll_script():
    """
    DEXTER ROLL 
    -----------------------
    Sends a random Dexter-themed edit or GIF with rarity chances.
    Prevents rolling the same clip twice in a row.
    
    COMMANDS:
    <p>dexter - Roll a random Dexter edit/GIF
    <p>dexter help - Show help and statistics
    
    """

    MEDIA_POOL = [
        # Common (30% each) 
        {"title": "michael jackson x dex", "url": "https://getsharex.co/0AK84", "chance": 30},
        {"title": "doals", "url": "https://getsharex.co/Gi065", "chance": 30},
        {"title": "creaming in my panties", "url": "https://getsharex.co/HMfty", "chance": 30},
        {"title": "cutie patootie uwu", "url": "https://getsharex.co/rRNr9", "chance": 30},
        {"title": "Chruch nigga", "url": "https://getsharex.co/xA5Jk", "chance": 30},
        {"title": "who's number one now", "url": "https://getsharex.co/usZ4H", "chance": 30},
        {"title": "Peak friendship", "url": "https://getsharex.co/c45PP", "chance": 30},
        {"title": "Dexter is funny!", "url": "https://getsharex.co/WpjAE", "chance": 30},
        {"title": "I own you!!", "url": "https://getsharex.co/ihHt7", "chance": 30},
        {"title": "Court!", "url": "https://getsharex.co/CWzMW", "chance": 30},
        
        # Uncommon (15% each) 
        {"title": "That one dexter edit!", "url": "https://getsharex.co/04lmL", "chance": 15},
        {"title": "Bay Harbor Butcher x doakes edit!", "url": "https://getsharex.co/lr4Sr", "chance": 15},
        {"title": "Brian Dexter edit!", "url": "https://getsharex.co/D3FHk", "chance": 15},
        {"title": "Doakes hot daddy edit!", "url": "https://getsharex.co/OuJLq", "chance": 15},
        {"title": "Joey Quinn edit!", "url": "https://getsharex.co/a26Is", "chance": 15},
        
        # Rare (8%) 
        {"title": "Uncommon Doakes Suspicion", "url": "https://getsharex.co/IGq2D", "chance": 8},
        {"title": "Tonight's the night 🌙", "url": "https://getsharex.co/j6AOF", "chance": 8},
        
        # Legendary (3%) 
        {"title": "Legendary sussy Doakes 💀", "url": "https://getsharex.co/knBw3", "chance": 3},
        
        # Mythical (1%) 
        {"title": "❤️ Mythical long-haired Doakes ❤️", "url": "https://getsharex.co/eo0v8", "chance": 1}
    ]

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

    async def show_dexter_help(ctx):

        common_count = sum(1 for item in MEDIA_POOL if item["chance"] >= 20)
        uncommon_count = sum(1 for item in MEDIA_POOL if 10 <= item["chance"] < 20)
        rare_count = sum(1 for item in MEDIA_POOL if 5 <= item["chance"] < 10)
        legendary_count = sum(1 for item in MEDIA_POOL if 3 <= item["chance"] < 5)
        mythical_count = sum(1 for item in MEDIA_POOL if item["chance"] < 3)
        
        total_edits = len(MEDIA_POOL)
        
      
        rarity_lines = []
        if common_count > 0:
            rarity_lines.append(f"**Common** (20%+): {common_count} edits")
        if uncommon_count > 0:
            rarity_lines.append(f"**Uncommon** (10-19%): {uncommon_count} edits")
        if rare_count > 0:
            rarity_lines.append(f"**Rare** (5-9%): {rare_count} edits")
        if legendary_count > 0:
            rarity_lines.append(f"**Legendary** (3-4%): {legendary_count} edits")
        if mythical_count > 0:
            rarity_lines.append(f"**Mythical** (<3%): {mythical_count} edits")
        
        rarity_breakdown = "\n".join(rarity_lines)
        
        current_private = getConfigData().get("private")
        updateConfigData("private", False)
        
        try:
            await forwardEmbedMethod(
                channel_id=ctx.channel.id,
                title="🔪 Dexter Roll - Help",
                content=(
                    f"# Dexter Roll Command\n\n"
                    f"**Description:**\n"
                    f"Randomly sends Dexter-themed edits or GIFs with weighted rarity chances. "
                    f"The system prevents rolling the same clip twice in a row.\n\n"
                    f"**Usage:**\n"
                    f"`{getConfigData().get('prefix', '<p>')}dexter` - Roll a random edit\n"
                    f"`{getConfigData().get('prefix', '<p>')}dexter help` - Show this help\n\n"
                    f"**Available Edits:**\n"
                    f"Total: **{total_edits}** unique Dexter edits/GIFs\n\n"
                    f"**Rarity Breakdown:**\n"
                    f"{rarity_breakdown}\n\n"
                    f"> *Higher rarity = lower chance of rolling!*"
                )
            )
            print(f"✅ Displayed Dexter help (Total edits: {total_edits})", type_="SUCCESS")
        except Exception as e:
            await ctx.send(f"Error displaying help: {e}", delete_after=5)
            print(f"❌ Error showing help: {e}", type_="ERROR")
        finally:
            updateConfigData("private", current_private)

    @bot.command(name="dexter", description="Rolls a random Dexter edit or GIF (no repeats).")
    async def dexter_command(ctx, *, args: str = ""):
        await ctx.message.delete()
        
       
        if args.strip().lower() in ["help", "?"]:
            await show_dexter_help(ctx)
            return
   
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
                    f"*Chance:* {roll['chance']}%"
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