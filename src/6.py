import random 

def generate_random_code(): 
     num = random.randint(100,1000) 
     return f'{num} {num+1} {num+2}'