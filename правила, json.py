# Уно

## Правила игры
'''
1) каждому игроку раздаётся по 7 карт, оставшиеся карты кладутся в колоду
2) из колоды достают 1 карту
3) первый игрок кладёт такую же карту по цвету или по значению (от 0 до 9)
4) если такой карты нет , из колоды берётся карта. Если она подходит - игрок её кладёт.
   Если не подходит - оставляет себе , ход переходит к следующему игроку
5) побеждает тот , у кого закончились все карты
6) у оставшихся игроков подсчитываются очки( по значению карты)
'''

# Текстовый интерфейс
'''
Top: g2
Sam: r3 y5 g4 r1
Sam play: g4
-----
Top: g4
Pit: y6 y2 r8 g7 g5
Pit play: g7
----
Top: g7
Sam: r3 y5 r1
Sam : takes the card
Sam : r3 y5 r1 r4
Sam : pass
----
Top: g7
Pit: y6 y2 r8 g5
Pit play: g5
---
Top: g5
Sam: r3 y5 r1 r4
Sam play: y5
----
Top: y5
Pit: y6 y2 r8
Pit play : y2
----
Top : y2
Sam : r3 r1 r4
Sam : takes the card
Sam : r3 r1 r4 r5
Sam : pass
----
Top : y2
Pit : y6 r8
Pit play : y6 
----
Top : y6
Sam : r3 r1 r4 r5
Sam: takes the card
Sam : r3 r1 r4 r5 y8
Sam play : y8 
----
Top : y8
Pit: r8
Pit play : r8
----
Pit win!!!
'''


## Пример save-файла
'''
{
   "card" : "y7"
   "deck" : "g4 r6 r3 b0 g9"
   "player" : "Tom"
   "all_players": [{"name":"Sam", "hand": "y1 y2 y3 y4" },
                   {"name":"Bob",  "hand": "g1 g2 g3 g4" }]
}
'''
