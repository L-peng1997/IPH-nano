class Animal(object):

    def __init__(self, lx):

        self.driver = lx

    def set_run(self):

        print(self.driver)

class dog(Animal):

    def __init__(self, xw, lx):

        super(dog, self).__init__(lx)

        self.xe = xw

    def set_r(self):

        self.set_run()

c = dog('pao1', 'zou1')

c.set_r()

