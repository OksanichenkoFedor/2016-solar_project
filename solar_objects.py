# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""

    def move(self, dt):
        """Перемещает тело в соответствии с действующей на него силой.

        Параметры:

        **body** — тело, которое нужно переместить.
        """
        ax = self.Fx / self.m
        self.Vx += ax * dt
        self.x += self.Vx * dt

        ay = self.Fy / self.m
        self.Vy += ay * dt
        self.y += self.Vy * dt

    def Force_Count(self, space_objects):
        self.Fx = self.Fy = 0
        for obj in space_objects:
            if self == obj:
                continue  # тело не действует гравитационной силой на само себя!
            r = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
            modul_F = (gravitational_constant * self.m * obj.m) / r ** 2
            self.Fx += modul_F * (obj.x - self.x) / r
            self.Fy += modul_F * (obj.y - self.y) / r

class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""

    def move(self, dt):
        """Перемещает тело в соответствии с действующей на него силой.

        Параметры:

        **body** — тело, которое нужно переместить.
        """
        ax = self.Fx / self.m
        self.Vx += ax * dt
        self.x += self.Vx * dt

        ay = self.Fy / self.m
        self.Vy += ay * dt
        self.y += self.Vy * dt

    def Force_Count(self, space_objects):
        self.Fx = self.Fy = 0
        for obj in space_objects:
            if self == obj:
                continue  # тело не действует гравитационной силой на само себя!
            r = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
            modul_F = (gravitational_constant * self.m * obj.m) / r ** 2
            self.Fx += modul_F * (obj.x - self.x) / r
            self.Fy += modul_F * (obj.y - self.y) / r
