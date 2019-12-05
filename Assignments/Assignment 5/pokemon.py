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
        # base_stats = [(stat["stat"]["name"], stat["base_stat"]) for stat in
        #               self._stats]
        types = [type["type"]["name"].upper() for type in self._types]
        # abilities = [ability["ability"]["name"].upper()
        #              for ability in self._abilities]

        moves = [f"\n=== {move['move']['name'].upper().replace('-', ' ')} "
                 f"===\nLEARNABLE AT LEVEL "
                 f"{move['version_group_details'][0]['level_learned_at']}" for
                 move in self._moves]

        # base_stats_str = ""
        # for stat in base_stats:
        #     base_stats_str += f"{stat[0].upper()} : {stat[1]}\n"

        abilities = ""
        for ability in self._abilities:
            abilities += f"{ability}"

        return f"{'*' * 150}\n" \
               f"*** POKEMON NAME ***\n{self._name.title()} " \
               f"(ID: {self._id})\n\n" \
               f"*** HEIGHT / WEIGHT ***\n{self._height} decimeters, " \
               f"{self._weight} hectograms\n\n" \
               f"*** STATS ***\n{self._stats}\n" \
               f"*** TYPES ***\n{'/'.join(types)}\n\n" \
               f"*** ABILITIES ***\n{abilities}\n\n" \
               f"*** MOVES ***\n{newline.join(moves)}\n" \
               f"{'*' * 150}\n"


class Stats:
    def __init__(self, speed=None, sp_def=None, sp_atk=None, defense=None,
                 attack=None, hp=None, id_=None, is_battle_only=None):
        # (name, base_stat, url)
        self._speed = speed
        self._sp_def = sp_def
        self._sp_atk = sp_atk
        self._defense = defense
        self._attack = attack
        self._hp = hp
        self._id = id_
        self._is_battle_only = is_battle_only

    def __str__(self):
        # Non expanded stats
        if self._id is None:
            return f"{self._speed['stat']['name'].upper()} : " \
                   f"{self._speed['base_stat']} " \
                   f"({self._speed['stat']['url']})\n" \
                   f"{self._sp_def['stat']['name'].upper()} : " \
                   f"{self._sp_def['base_stat']} " \
                   f"({self._sp_def['stat']['url']})\n" \
                   f"{self._sp_atk['stat']['name'].upper()} : " \
                   f"{self._sp_atk['base_stat']} " \
                   f"({self._sp_atk['stat']['url']})\n" \
                   f"{self._defense['stat']['name'].upper()} : " \
                   f"{self._defense['base_stat']} " \
                   f"({self._defense['stat']['url']})\n" \
                   f"{self._attack['stat']['name'].upper()} : " \
                   f"{self._attack['base_stat']} " \
                   f"({self._attack['stat']['url']})\n" \
                   f"{self._hp['stat']['name'].upper()} : " \
                   f"{self._hp['base_stat']} " \
                   f"({self._hp['stat']['url']})\n"
        else:
            return f"Undefined expanded stats"


class Move:
    """
    Represent the main attributes of a Pokemon Move.
    """

    def __init__(self, name=None, id_=None, generation=None, accuracy=None,
                 pp=None, power=None, type_=None, damage_class=None,
                 effect_short=None, move_url=None, level=None):
        self._name = name
        self._id = id_
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type_
        self._damage_class = damage_class
        self._effect_short = effect_short
        self._move_url = move_url
        self._level = level

    def __str__(self):
        """
        Formatted string for Move object.
        :return: str
        """
        if self._move_url is None:
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
        else:
            return f"{'*' * 150}\n" \
                   f"*** MOVE NAME ***\n{self._name.title()}" \
                   f"*** LEVEL LEARNED AT ***\n{self._level}\n" \
                   f"*** URL ***\n{self._move_url}\n" \
                   f"{'*' * 150}\n"


class Ability:
    """
    Represent the main attributes of a Pokemon's innate Ability.
    """

    def __init__(self, name=None, id_=None, generation=None,
                 effect=None, effect_short=None, pokemon=None, url=None):
        self._name = name
        self._url = url
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
        # Unexpanded ability formatting
        if self._id is None:
            return f"{self._name.upper().replace('-', ' ')} " \
                   f"({self._url})\n"
        else:
            # Expanded ability formatting
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
