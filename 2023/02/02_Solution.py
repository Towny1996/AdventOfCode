import string
import re
import math

class Part_One:
    def DoWork(self):
        input_file = open('input.txt', 'r')
        return self.GetIdSums(input_file.read().splitlines())

    def GetIdSums(self, lines: [string]) -> int:
        game_summary = []
        for index, line in enumerate(lines):
            game = { 'game': index + 1}
            cubes = re.findall('([0-9]{1,2}\s{1}[a-z]*[^,;])', line)
            for res in cubes:
                colour = res.split(' ')[1]
                amount = int(res.split(' ')[0])
    
                if(colour in game): game[colour].append(amount)
                else: game[colour] = [amount]
            
            game_summary.append(game)
        
        return sum([int(x['game']) for x in game_summary if max(x.get('red', 0)) <= 12 and max(x.get('green', 0)) <= 13 and max(x.get('blue', 0)) <= 14])

class Part_Two:
    def DoWork(self):
        input_file = open('input.txt', 'r')
        return self.GetCubePowers(input_file.read().splitlines())

    def GetCubePowers(self, lines: [string]) -> int:
        game_summary = []
        for index, line in enumerate(lines):
            game = {}
            cubes = re.findall('([0-9]{1,2}\s{1}[a-z]*[^,;])', line)
            for res in cubes:
                colour = res.split(' ')[1]
                amount = int(res.split(' ')[0])

                if((colour in game and game[colour] < amount) or (colour not in game)): game[colour] = amount

            game_summary.append(game)
        
        return sum([math.prod(x.values()) for x in game_summary])

print(Part_One().DoWork())
print(Part_Two().DoWork())
