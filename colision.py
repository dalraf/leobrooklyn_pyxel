from player import Player
from rock import Rock
from enemies import Enemy_1, Enemy_2



def verify_colision(pyxel, objects, enemies, player):
    lista_kill = []
    lista_all = objects.lista_objects.copy() + enemies.lista_enemies.copy()
    lista_all.append(player)
    for sprite1 in lista_all:
        for sprite2 in lista_all:
            if isinstance(sprite1, Rock)  and sprite1.shoot_enemy:
                if isinstance(sprite2, Player):
                    distance = sprite1.calculate_distance_damage(sprite2)
                    if distance < 10:
                        sprite2.life -= sprite1.sprint
                        if sprite2.life <= 0:
                            pyxel.quit()
                        lista_kill.append(sprite1)
            if isinstance(sprite1, Rock) and sprite1.shoot_player:
                if any([isinstance(sprite2, enemy) for enemy in [Enemy_1, Enemy_2]]):
                    distance = sprite1.calculate_distance_damage(sprite2)
                    if distance < 10:
                        sprite2.life -= sprite1.sprint
                        if sprite2.life <= 0:
                            lista_kill.append(sprite2)
                        lista_kill.append(sprite1)
    
    for sprite in lista_kill:
        if sprite in objects.lista_objects:
            objects.lista_objects.remove(sprite)
        if sprite in enemies.lista_enemies:
            enemies.lista_enemies.remove(sprite)
        del sprite