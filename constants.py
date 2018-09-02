from entities.kingdom import Kingdom

INTENT_GET_RULER = 'INTENT_GET_RULER'
INTENT_GET_RULER_ALLIES = 'INTENT_GET_RULER_ALLIES'
INTENT_SEND_MESSAGE_TO_ALLIES = 'INTENT_SEND_MESSAGE_TO_ALLIES'

INTENTS = [
    INTENT_GET_RULER,
    INTENT_GET_RULER_ALLIES,
    INTENT_SEND_MESSAGE_TO_ALLIES
]

kingdoms = [
    Kingdom('owl', 'Kingdom Air'),
    Kingdom('octopus', 'Kingdom Water'),
    Kingdom('panda', 'Kingdom Land'),
    Kingdom('gorilla', 'Kingdom Space'),
    Kingdom('mammoth', 'Kingdom Ice'),
    Kingdom('dragon', 'Kingdom Fire'),
    Kingdom('', 'Kingdom Shan'),
]

winning_messages = {
    'panda': ["a1d22n333a4444p"],
    'dragon': ["Drag on Martin!"],
    'gorilla': ["Go, risk it all"],
    'owl': ["oaaawaala", "Let’s swing the sword together"],
    'octopus': ["Sphinx of black quartz, judge my dozen vows"],
    'mammoth': ["Ahoy! Fight for me with men and money", "zmzmzmzaztzozh"]
}

random_messages = [
    "Summer is coming",
    "a1d22n333a4444p",
    "oaaawaala",
    "zmzmzmzaztzozh",
    "Go, risk it all",
    "Let's swing the sword together",
    "Die or play the tame of thrones",
    "Ahoy! Fight for me with men and money",
    "Drag on Martin!",
    "When you play the tame of thrones, you win or you die.",
    "What could we say to the Lord of Death? Game on?",
    "Turn us away, and we will burn you first",
    "Death is so terribly final, while life is full of possibilities.",
    "You Win or You Die",
    "His watch is Ended",
    "Sphinx of black quartz, judge my dozen vows",
    "Fear cuts deeper than swords, My Lord.",
    "Different roads sometimes lead to the same castle.",
    "A DRAGON IS NOT A SLAVE.",
    "Do not waste paper",
    "Go ring all the bells",
    "Crazy Fredrick bought many very exquisite pearl, emerald and diamond jewels.",
    "The quick brown fox jumps over a lazy dog multiple times.",
    "We promptly judged antique ivory buckles for the next prize.",
    "Walar Morghulis: All men must die."
]