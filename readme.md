# Nighty Selfbot Scripts Collection

A collection of custom NightyScripts for the Nighty Selfbot platform, featuring utility fixes, entertainment commands, and countdown timers.

## 📋 Scripts Included

### 1. CMD Error Fix (`cmderror.py`)
**Author:** YourName

A utility script that provides instructions to fix CMD prompt errors when the Nighty configuration becomes corrupted.

#### Features
- Displays step-by-step instructions to reset Nighty
- Explains why CMD prompt errors occur
- Provides multiple command aliases for convenience

#### Commands
- `.cmderror` - Show fix instructions
- `.cmdfix` - Alias for cmderror
- `.fixerror` - Alias for cmderror

#### Usage
```
<p>cmderror
```

When your Nighty config file gets corrupted or has invalid JSON format, use this command to get reset instructions.

---

### 2. Dexter Roll (`dexter.py`)
**Author:** Kirby631

A fun entertainment script that randomly sends Dexter-themed edits and GIFs with weighted rarity chances.

#### Features
- 10 different Dexter-themed media items
- Weighted random selection system
- Rarity tiers from common to mythical
- Displays chance percentage with each roll

#### Media Pool
| Title | Rarity | Chance |
|-------|--------|--------|
| Bay Harbor Butcher edits | Common | 50% |
| Brian Dexter edit | Common | 50% |
| Doakes hot daddy edit | Common | 50% |
| Joey Quinn edit | Common | 50% |
| Uncommon Doakes Suspicion | Common | 50% |
| Tonight's the night 🌙 | Uncommon | 15% |
| Legendary sussy Doakes 👀 | Legendary | 5% |
| ❤️ Mythical long-haired Doakes ❤️ | Mythical | 3% |

#### Commands
- `.dexter` - Roll a random Dexter-themed media

#### Usage
```
<p>dexter
```

---

### 3. Update Countdown (`update.py`)
**Author:** Kirby631

A live countdown timer that displays time remaining until the next update (set 5 years from activation).

#### Features
- Real-time countdown display
- Updates every second for 30 seconds
- Displays years, days, hours, minutes, and seconds
- Automatic stop to prevent rate limits
- Handles expired countdowns gracefully

#### Commands
- `.update` - Display live countdown timer

#### Usage
```
<p>update
```

The countdown will automatically update every second for 30 seconds, showing the time remaining in a human-readable format.

---

## 🚀 Installation

1. Place the script files in your Nighty Selfbot scripts directory
2. Restart Nighty or reload scripts
3. Scripts will automatically register their commands

## ⚙️ Configuration

Each script uses the `@nightyScript` decorator with metadata:
- **name** - Display name of the script
- **author** - Script creator
- **description** - What the script does
- **usage** - Command usage syntax

## 📝 Notes

- All scripts temporarily disable private mode when sending embeds to ensure visibility
- Scripts include error handling and logging
- Commands automatically delete the trigger message for clean chat appearance
- The Dexter Roll script uses a weighted random system for fair distribution

## 🐛 Troubleshooting

### CMD Error Issues
If Nighty opens a CMD prompt instead of running normally:
1. Press `Windows key + R`
2. Type `%appdata%/Nighty Selfbot` and click OK
3. Delete `nighty.config` and the `data` folder
4. Restart Nighty

### Script Not Loading
- Ensure scripts are in the correct directory
- Check for syntax errors in the console
- Verify Nighty Selfbot is up to date

## 📄 License

These scripts are provided as-is for use with Nighty Selfbot. Modify and distribute freely.

## 🤝 Contributing

Feel free to fork, modify, and improve these scripts. Pull requests are welcome!

---

**Disclaimer:** These scripts are for educational purposes. Using selfbots may violate Discord's Terms of Service. Use at your own risk.