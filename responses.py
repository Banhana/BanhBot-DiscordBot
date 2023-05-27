import random
import json
import re
import random_responses

def get_response(message: str) -> str:
    """
    Args:
        message: A string message
    Returns:
        A string response
    """
    
    p_message = message.lower() # Lowercase the message

    if p_message == 'hello':
        return 'Hey there!'

    if p_message.startswith('!') and p_message[1:] not in ['roll', 'choose', 'help']:
        return "Invalid command. Try `!help`"

    # Rolling a dice
    if p_message.startswith('!roll '):
        dice_notation = p_message[5:]  # Extract the dice notation part
        try:
            rolls = roll_dice(dice_notation)
            return ', '.join(rolls)  # Return the rolls as a comma-separated string
        except ValueError:
            return "Invalid dice notation. Please use the format '!roll <num_rolls>d<dice_sides>' Ex. !roll 1d20."
        
    # Choosing between 2 or more options
    if p_message.startswith('!choose '):
        choose_notation = p_message[8:] # Extract the choose notation
        try:
            choice = choose_option(choose_notation)
            return choice
        except ValueError:
            return "Invalid notation. Please use the format '!choose <choice1> | <choice2>' Ex. !choose This | That"

    # Help prompts
    if p_message == '!help':
        return "```" + "\n".join([
            "Help:",
            "\t!roll to roll a dice. (Ex. !roll 1d20)",
            "\t!choose to choose between options. (Ex. !choose This | That)"
        ]) + "```"


def roll_dice(dice_notation):
    try:
        # Extract the values from the dice notation string
        num_rolls, dice_sides = map(int, dice_notation.split('d'))

        # Roll the dice and return the results
        rolls = [str(random.randint(1, dice_sides)) for _ in range(num_rolls)]
        return rolls
    except ValueError:
        raise ValueError("Invalid dice notation.")
    
def choose_option(choose_notation):
    try:
        options = choose_notation.split(" | ")
        if len(options) < 2:
            raise ValueError("Invalid notation.")
        choice = random.choice(options)
        return choice
    except ValueError:
        raise ValueError("Invalid notation.")

