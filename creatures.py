import creature_class


class Orc(creature_class):
    def __init__(self, weapon, max_hit_points, current_hit_points):
        self.__weapon = weapon
        self.__max_hit_points = max_hit_points
        self.__current_hit_points = current_hit_points

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def set_max_hit_points(self, max_hit_points):
        self.__max_hit_points = max_hit_points

    def set_current_hit_points(self, current_hit_points):
        self.__current_hit_points = current_hit_points

    def get_weapon(self):
        return self.__weapon

    def get_max_hit_points(self):
        return self.__max_hit_points

    def get_current_hit_points(self):
        return self.__current_hit_points

    def __str__(self):
        return "\nWeapon: " + self.__weapon + "\nMax Hit Points: " + self.__max_hit_points + "\nCurrent Hit Points: "+ \
            self.__current_hit_points


class OrcBoss(creature_class, Orc):
    def __init__(self, weapon, max_hit_points, current_hit_points, name, special_move):
        Orc.__init__(self, weapon, max_hit_points, current_hit_points)
        self.__name = name
        self.__special_move = special_move

    def set_name(self, name):
        self.__name = name

    def set_special_move(self, special_move):
        self.__special_move = special_move

    def get_name(self):
        return self.__name

    def get_special_move(self):
        return self.__special_move

    def __str__(self):
        return "\nWeapon: " + self.get_weapon() + "\nMax Hit Points: " + self.get_max_hit_points() + \
            "\nCurrent Hit Points: " + self.get_current_hit_points() + "\nName: " + self.get_name() + \
            "\nSpecial Move: " + self.get_special_move()
