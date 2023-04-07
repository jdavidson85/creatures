import creature_class
import creatures


def main():
    type_of_creature = "Orc" "OrcBoss"
    friendly = False
    position = "45, 120, 200"
    image = "Orc.pic" "OrcBoss.pic"
    weapon = "Hammer"
    max_hit_points = int("350")
    current_hit_points = int("275")
    name = "Griksnak"
    special_move = "Over head slam"

    orc_creature = creature_class.Creature(type_of_creature, friendly, position, image)
    new_creature = creatures.Orc(weapon, max_hit_points, current_hit_points)
    orc_boss = creatures.OrcBoss(name, special_move)
    print("\nType of creature: " + orc_creature.get_type_of_creature() + "\nFriendly: " + orc_creature.get_friendly()
          + "\nLocation: " + orc_creature.get_position() + "\nImage: " + orc_creature.get_image() + "\nWeapon: "
          + new_creature.get_weapon() + "\nMax Hit Points: " + new_creature.get_max_hit_points() +
          "\nCurrent Hit Points: " + new_creature.get_current_hit_points() + "\nOrc Boss Name: " + orc_boss.get_name()
          + "\nSpecial Move: " + orc_boss.get_special_move())


main()
