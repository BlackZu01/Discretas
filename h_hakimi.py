# Estare implementando el algoritmo de Havel - Hakimi.
from graphic import ploting

class Problem:

    def __init__(self, sec_sec2: list()):
        self.sec_sec2 = sec_sec2
    
    def havel_hakimi(self):
        if sum(self.sec_sec2) % 2 != 0:
            return ('The sequence doesn\'t satisfy Handshaking Theorem', False)
        
        while True:
            print(self.sec_sec2)
            self.sec_sec2.sort(reverse=True)
            

            deleted = self.sec_sec2.pop(0)

            
            if deleted >= len(self.sec_sec2):
                return ('The first grade is bigger than the number of vertex of the graph', False)
            
            for i in range(0, deleted):
                self.sec_sec2[i] -= 1

            if set(self.sec_sec2) == {0}:
                return ('The graph is graphic', True)

            breakable = len(list(filter(lambda grade: grade  < 0, self.sec_sec2[:deleted])))
            if breakable > 0:
                return ('Contradiction ↯', False)



sec = [6, 6, 6, 6, 4, 3, 3, 0] # Clase
sec2 = [1, 4, 2, 4, 3, 2]      # Clase


problema = Problem(sec2)
solution = problema.havel_hakimi()

print(f'{problema.sec_sec2} - {solution}')

answer = int(input('[+] Do you want to see it in a graph?  (press 0: yes - press 1: otherwise): '))

if answer == 0:
    ploting(sec2, solution)
elif answer == 1:
    print('Thanks')
else:
    print('Enter a valid option')
