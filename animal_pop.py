from random import randint
import time
import os
def increase_fun(actual_population: int, changes: int) -> int:
    return actual_population + changes

def decrease_fun(actual_population: int, changes: int) -> int:
    return actual_population - changes


changes_dict = {'Increase': increase_fun,
                'Decrease': decrease_fun,
                'Positive': increase_fun,
                'Negative': decrease_fun,
                '+': increase_fun,
                '-':decrease_fun}
class Carnivores:
    def __init__(self,name, habitat, weight, population, color, wild):
        self.name = name
        self.habitat = habitat
        self.weight = weight
        self.population = population
        self.color = color
        self.wild = wild
    def population_changes(self, changes: str, number: int = 0) -> int:
         if changes in changes_dict:
            self.population = changes_dict[changes](self.population, number)
         return self.population   
    def weight_change(self, changes: str , number: int = 0) -> int:
        if changes in changes_dict:
            self.weight = changes_dict[changes](self.weight, number)
        return self.weight 
    
tiger = Carnivores('Tiger', 'Sibear Forests', 308, 498, 'Orange-Black', 'Yes,tiger is wild animal')
user_chane_deciosion = input('Please write a word between Increase,Positive,+ // Decrease,Negative,-.It will effect future of animal:').capitalize().strip()
pop_change_speed = int(input('Write animal monthly population speed change:'))
success_message = 'Tiger race now is safe.'
fail_message = 'Tiger race has become extinct'
while True:            
    print(f'{tiger.population_changes(user_chane_deciosion, pop_change_speed)} ==> {tiger.name} in the world')
    time.sleep(0.5)
    os.system('cls')
    if tiger.population > 2000:
        print(f'{tiger.population} {tiger.name}:=> {success_message}')
        break
    elif tiger.population <= 0:
        print(f'0 {tiger.name}:=> {fail_message}')
        break

