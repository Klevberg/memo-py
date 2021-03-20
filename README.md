# memo-py

Flash cards for studying.

## How to use:

Run game.py in your terminal of choice.

```
> python game.py
```

*(Note: Colors may not show up in your terminal. I recommend using VSCode)*


The game will ask which file you wish to use. This file will contain the cards used in the game. All files should end with .json and be located in the packs/ directory. Press enter to use the example pack, which is included with the game.

Next, the game will ask which side you want to see when shown a card. A card can store multiple categories, and therefore have multiple sides. The cards from the example.json file will contain categories `country` and `capital`. Enter one of these categories.

Finally, you will be asked which side you want to guess. This side will not be shown to you, but will be used to track if you guessed the word correctly.
