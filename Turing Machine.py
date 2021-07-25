class TuringMachine:
    def __init__(self, input_program, input_binary, origin_state=0):
        self.tr = {}
        self.st = str(origin_state)
        self.tape = ''.join(['_'] * 1000)
        self.h = 1000 // 2
        self.tape = self.tape[:self.h] + input + self.tape[self.h:]
        for line in input_program.splitlines():
            a, b, c, d, s1 = line.split()
            self.tr[a, b] = (c, d, s1)

    def run(self, max_iter=99999):
        i = 0
        while i < max_iter and self.st != 'half':
            self.step()
            i = i + 1

        print("Final result is : ")
        print(self.tape.replace('_', ''), self.st)

    def step(self):
        if self.st != 'halt':
            a = self.tape[self.h]
            act = self.tr.get((self.st, a))
            if act:
                r, d, s1 = act
                self.tape = self.tape[:self.h] + r + self.tape[self.h + 1:]
                if d != '*':
                    self.h = self.h + (1 if d == 'r' else -1)
                self.st = s1


input = '110110_101011'
program = open('text').read()
tm = TuringMachine(program, input)
tm.run()