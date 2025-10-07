@nightyScript(
    name="CMD Error Fix",
    author="Kirby631",
    description="Shows instructions to fix CMD prompt error when Nighty config is corrupted.",
    usage="<p>cmderror"
)
def cmd_error_script():
    """
    CMD ERROR FIX (NightyScript)
    ----------------------------
    Provides the `.cmderror` command which shows reset instructions
    when Nighty opens a CMD prompt due to corrupted config.
    """

    from datetime import datetime

    async def send_embed(ctx, title, content):

        current_private = getConfigData().get("private")
        updateConfigData("private", False)
        try:
            await forwardEmbedMethod(
                channel_id=ctx.channel.id,
                title=title,
                content=content
            )
        finally:
            updateConfigData("private", current_private)

    @bot.command(
        name="cmderror",
        aliases=["cmdfix", "fixerror"],
        usage="",
        description="Shows how to fix CMD prompt error by resetting Nighty."
    )
    async def cmderror_cmd(ctx, *, args: str = ""):
        await ctx.message.delete()

        lines = []
        lines.append("# 🖥️ CMD prompt fix (Reset Nighty)")
        lines.append("**1**・`Windows key + R`")
        lines.append("**2**・Type `%appdata%/Nighty Selfbot` → Click OK")
        lines.append("**3**・Delete `nighty.config` and the `data` folder")
        lines.append("**4**・Restart Nighty\n")
        lines.append("⚠️ Nighty opens a CMD prompt when your config file gets corrupted or has an invalid JSON format.")
        lines.append("Deleting `nighty.config` fixes this issue.")
        lines.append(f"\n_Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC_")

        await send_embed(ctx, "CMD Error Fix", "\n".join(lines))

cmd_error_script()
