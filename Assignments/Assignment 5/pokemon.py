class Pokemon:
    """
    Represent a Pokemon through its main attributes from PokeAPI call.
    """
    def __init__(self, name=None, id_=None, height=None, weight=None,
                 stats=None, types=None, abilities=None, moves=None):
        self._name = name
        self._id = id_
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves

    def __str__(self):
        """
        Formatted string for Pokemon object.
        :return: str
        """
        newline = '\n'
        base_stats = [(stat["stat"]["name"], stat["base_stat"]) for stat in
                      self._stats]
        types = [type["type"]["name"].upper() for type in self._types]
        abilities = [ability["ability"]["name"].upper()
                     for ability in self._abilities]

        moves = [f"\n=== {move['move']['name'].upper().replace('-', ' ')} " 
                 f"===\nLEARNABLE AT LEVEL "
                 f"{move['version_group_details'][0]['level_learned_at']}" for
                 move in self._moves]

        base_stats_str = ""
        for stat in base_stats:
            base_stats_str += f"{stat[0].upper()} : {stat[1]}\n"

        return f"{'*' * 150}\n" \
               f"*** POKEMON NAME ***\n{self._name.title()} " \
               f"(ID: {self._id})\n\n" \
               f"*** HEIGHT / WEIGHT ***\n{self._height} decimeters, " \
               f"{self._weight} hectograms\n\n" \
               f"*** STATS ***\n{base_stats_str}\n" \
               f"*** TYPES ***\n{'/'.join(types)}\n\n" \
               f"*** ABILITIES ***\n{newline.join(abilities)}\n\n" \
               f"*** MOVES ***\n{newline.join(moves)}\n" \
               f"{'*' * 150}\n"


class Move:
    """
    Represent the main attributes of a Pokemon Move.
    """
    def __init__(self, name=None, id_=None, generation=None, accuracy=None,
                 pp=None, power=None, type_=None, damage_class=None,
                 effect_short=None):
        self._name = name
        self._id = id_
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type_
        self._damage_class = damage_class
        self._effect_short = effect_short

    def __str__(self):
        """
        Formatted string for Move object.
        :return: str
        """
        return f"{'*' * 150}\n" \
               f"*** MOVE NAME ***\n{self._name.title()}\t" \
               f"(ID: {self._id})\n\n" \
               f"*** GENERATION ***\n{self._generation.upper()}\n\n" \
               f"*** MOVE STATS ***\n" \
               f"ACCURACY: {self._accuracy}\t|\t" \
               f"PP: {self._pp}\t|\t" \
               f"POWER: {self._power}\n\n" \
               f"*** TYPE  ***\n{self._type['name'].upper()}\t" \
               f"{self._type['url']}\n\n" \
               f"*** DAMAGE CLASS ***\n" \
               f"{self._damage_class['name'].upper()}\t" \
               f"{self._damage_class['url']}\n\n" \
               f"*** EFFECT (SHORT) ***\n{self._effect_short}\n" \
               f"{'*' * 150}\n"


class Ability:
    """
    Represent the main attributes of a Pokemon's innate Ability.
    """
    def __init__(self, name=None, id_=None, generation=None,
                 effect=None, effect_short=None, pokemon=None):
        self._name = name
        self._id = id_
        self._generation = generation
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon

    def __str__(self):
        """
        Formatted string for Ability object.
        :return: str
        """
        pokemon_list = [pokemon["pokemon"]["name"].title() for pokemon in
                        self._pokemon]
        return f"{'*' * 150}\n" \
               f"*** ABILITY ***\n{self._name.title()} " \
               f"(ID: {self._id})\n\n" \
               f"*** GENERATION INTRODUCED ***" \
               f"\n{self._generation['name'].upper()}\n\n" \
               f"*** ABILITY EFFECT ***\n{self._effect}\n\n" \
               f"*** ABILITY EFFECT (SHORT) ***\n{self._effect_short}\n\n" \
               f"*** POKEMON WITH THIS ABILITY***" \
               f"\n{', '.join(pokemon_list)}\n\n" \
               f"{'*' * 150}\n"