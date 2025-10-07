import asyncio
from datetime import datetime, timedelta

@nightyScript(
    name="Update Countdown",
    author="Kirby631",
    description="Displays a live countdown to the next update (5 years from now).",
    usage="<p>update"
)
def update_countdown_script():
    """
    UPDATE COUNTDOWN
    ----------------
    Shows a live countdown timer to the next update (5 years from now).

    COMMANDS:
    <p>update — Displays a real-time countdown (updates every second for 30 seconds)

    NOTES:
    - Automatically stops after 30 seconds to prevent rate limits
    - Displays years, days, hours, minutes, and seconds remaining
    - Stops early if the target date has passed
    """

    def format_countdown(target_date: datetime) -> str:
      
        now = datetime.now()
        remaining = target_date - now

        if remaining.total_seconds() <= 0:
            return "🎉 The update is here!"

        years = remaining.days // 365
        days = remaining.days % 365
        hours = remaining.seconds // 3600
        minutes = (remaining.seconds % 3600) // 60
        seconds = remaining.seconds % 60

        parts = []
        if years:
            parts.append(f"{years} year{'s' if years != 1 else ''}")
        if days:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")

        return ", ".join(parts)

    @bot.command(name="update", description="Show countdown to next update")
    async def update_countdown(ctx, *, args: str = ""):
        await ctx.message.delete()

       
        target_date = datetime.now() + timedelta(days=365 * 5)

    
        countdown_text = format_countdown(target_date)
        msg = await ctx.send(f"**⏳ Next Update Countdown**\n\n{countdown_text}")

        try:
          
            for _ in range(30):
                await asyncio.sleep(1)
                countdown_text = format_countdown(target_date)
                await msg.edit(content=f"**⏳ Next Update Countdown**\n\n{countdown_text}")

        except Exception as e:
            print(f"❌ Error updating countdown: {e}", type_="ERROR")

    print("✅ Update Countdown script loaded successfully.", type_="SUCCESS")

update_countdown_script()
