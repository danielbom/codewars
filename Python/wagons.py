from collections import deque
DEBUG = True


# TODO: Test the modification on is_in_* ...
class Coordinate(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def oriented_to(self, other):
        orientation  = 'n' if self.x > other.x else 's' if self.x < other.x else ''
        orientation += 'w' if self.y > other.y else 'e' if self.y < other.y else ''
        return orientation

    def __repr__(self):
        return f"({self.x},{self.y})"

    def is_in_horizontal(self, coord):
        return self.x == coord.x and self.y != coord.y

    def is_in_vertical(self, coord):
        return self.y == coord.y and self.x != coord.x

    def is_in_main_diagonal(self, coord):
        x = self.x - coord.x
        y = self.y - coord.y
        return x == y and self.x != coord.x

    def is_in_second_diagonal(self, coord):
        x = self.x + coord.x
        y = self.y + coord.y
        return x == y and self.x != coord.x

    def get(self):
        return (self.x, self.y)

    def add(self, x, y) -> tuple:
        return (self.x + x, self.y + y)


class Rail(object):
    def __init__(self, coord: Coordinate, symbol):
        self.symbol = symbol
        self.coord  = coord
        self.paths  = []

    def _check_initial(self, path):
        if path.symbol in "\\/":
            if self.symbol == "-":
                if self.coord.is_in_horizontal(path.coord): return True
            if self.symbol == "|":
                if self.coord.is_in_vertical(path.coord): return True
        if path.symbol == '/':
            if self.coord.is_in_second_diagonal(path.coord): return True
        if path.symbol == '\\':
            if self.coord.is_in_main_diagonal(path.coord): return True
        if path.symbol == '-':
            if self.coord.is_in_horizontal(path.coord): return True
        if path.symbol == '|':
            if self.coord.is_in_vertical(path.coord): return True

        return False

    def _check_second(self, path):
        if self.symbol == "+" and path.symbol in "-|": return True
        if self.symbol == "X" and path.symbol in "\\/": return True
        if self.symbol == "-" and path.symbol in "-\\/S+": return True
        if self.symbol == "|" and path.symbol in "|\\/S+": return True
        
        if self.symbol in "-|":
            if self.symbol + path.symbol not in "-|-": return True
        if self.symbol in "\\/":
            if self.symbol + path.symbol not in "/\\/": return True
        
        return False

    def add_path(self, path):
        if not self._check_initial(path): return
        if not self._check_second(path): return
        self.paths.append(path)

    def __repr__(self):
        return ''.join(["[", self.symbol, "]", str(self.coord), ": ", ','.join(p.symbol for p in self.paths)])


class Train(object):
    def __init__(self, shape):
        self.is_clockwise  = shape[0].islower()
        self.shape         = shape
        self.wagons        = deque()
        self.direction     = 'w' if self.is_clockwise else 'e'
        self.stop_time     = 0
        self.stop_time_max = len(shape) - 1
        self.stoped        = False

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    # Control of moves
    def _move(self, head, rail):
        self.direction = head.coord.oriented_to(rail.coord)
        if self.is_clockwise:
            self.wagons[-1] = rail
            self.wagons.appendleft(self.wagons.pop())
        else:
            self.wagons[0] = rail
            self.wagons.append(self.wagons.popleft())

    def move(self):
        head = self.wagons[0] if self.is_clockwise else self.wagons[-1]
        number_of_wagons = len(head.paths)

        for rail in head.paths:
            if rail not in self.wagons and rail.symbol == '+':
                self._move(head, rail)
                return
        
        for rail in head.paths:
            if rail not in self.wagons:
                if number_of_wagons == 2 or head.coord.oriented_to(rail.coord) == self.direction:
                    self._move(head, rail)
                    return
        
        for rail in head.paths:
            if rail not in self.wagons:
                if number_of_wagons == 2 or rail.coord.oriented_to(head.coord) == self.direction:
                    self._move(head, rail)
                    return

        raise RuntimeError

    def move_clockwise(self):
        t1 = self.is_clockwise
        self.is_clockwise = True
        self.move()
        self.is_clockwise = t1

    def move_anti_clockwise(self):
        t1 = self.is_clockwise
        self.is_clockwise = False
        self.move()
        self.is_clockwise = t1

    # Control of station stop
    def is_station_stop(self):
        head = self.wagons[0] if self.is_clockwise else self.wagons[-1]
        if self.shape[0] not in "xX" and head.symbol == 'S':
            self.stop_time = self.stop_time_max
            self.stoped = True

    def wait_station_time(self):
        self.stop_time -= 1
        self.stoped = self.stop_time > 0

    def collision_itself(self):
        head, *body = self.wagons
        return set(head.paths).issubset(body)       

class Track(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.trains = []
        self.initial_x = -1
        self.initial_y = -1
        self.lin = -1
        self.col = -1
    
    def initial_position(self) -> Train:
        if self.lin == -1:
            self.col = max(y for x, y in self.keys()) + 1
            self.lin = max(x for x, y in self.keys()) + 1
        if self.initial_y == -1:
            self.initial_x = 0
            self.initial_y = min(j for j in range(self.col) if self.get((0, j)))
        return self[self.initial_x, self.initial_y]
    
    def print(self):
        trains = {(wagon.coord.x, wagon.coord.y): train.shape[0].lower() 
            for train in self.trains for wagon in train.wagons}
        
        if self.lin == -1:
            self.initial_position()
        
        for i in range(self.lin):
            for j in range(self.col):
                if trains.get((i,j)):
                    print(trains[i,j], end='')
                elif self.get((i,j)):
                    print(self[i,j].symbol, end='')
                else:
                    print(' ', end='')
            print()
        print()

    def add_train(self, train: Train):
        self.trains.append(train)

    def move_trains(self):
        for train in self.trains:
            if train.stoped:
                train.wait_station_time()
            else:
                train.move()
                train.is_station_stop()

    def check_colision(self):
        busy_rails = [rail for train in self.trains for rail in train.wagons]
        return len(set(busy_rails)) != len(busy_rails) or any(map(Train.collision_itself, self.trains))


def build_Track(chart):
    track = Track()
    # Creating Rails
    for i in range(len(chart)):
        for j in range(len(chart[i])):
            if chart[i][j] != ' ':
                track[i,j] = Rail(Coordinate(i, j), chart[i][j])
    # Defining rails paths
    for i,j in track.keys():
        for k in range(-1,2):
            for l in range(-1, 2):
                if (k,l) != (0,0) and track.get((i+k, j+l)):
                    track[i,j].add_path(track[i+k, j+l])
    # Defining preferences paths
    for (i,j), rail in track.items():
        if rail.symbol in "-|" and len(rail.paths) > 2:
            for k in range(-1, 2, 2):
                for l in range(-1, 2, 2):
                    # Vertical check
                    if rail.symbol == "-" and track.get((i+k, j)) and track.get((i+k, j+l)):
                            if track[i+k, j] in rail.paths and track[i+k, j+l] in (rail.paths):
                                if track[i+k, j].symbol == "|":
                                    rail.paths.remove(track[i+k, j])
                                else:
                                    rail.paths.remove(track[i+k, j+l])
                    # Horizontal check
                    elif track.get((i, j+k)) and track.get((i+k, j+l)):
                        if track[i, j+k] in rail.paths and track[i+k, j+l] in (rail.paths):
                            if track[i+k, j+l].symbol == "|":
                                rail.paths.remove(track[i, j+k])
                            else:
                                rail.paths.remove(track[i+k, j+l])

    for rail in track.items():
        print(rail)

    return track


def build_Train(track, shape, pos):
    rail_initial = track.initial_position()
    train = Train(shape)
    
    orientations = ["w", "sw", "s"] if train.is_clockwise else ["e", "ne"]
    nxt = next(rail for rail in rail_initial.paths if rail_initial.coord.oriented_to(rail.coord) in orientations)

    wagons = [rail_initial]
    direction = rail_initial.coord.oriented_to(nxt.coord)
    print()
    for _ in range(len(shape)-1):
        print(nxt)
        wagons.append(nxt)
        number_of_paths = len(nxt.paths)
        for rail in nxt.paths:
            if rail not in wagons:
                new_direction = nxt.coord.oriented_to(rail.coord)
                if number_of_paths == 2 or new_direction == direction:
                    direction = new_direction
                    nxt = rail
                    break
    
    wagons = wagons if train.is_clockwise else reversed(wagons)
    for wagon in wagons:
        train.add_wagon(wagon)

    track.add_train(train)
    if DEBUG:
        track.print()
        input("----------")

    for _ in range(pos):
        if DEBUG:
            track.print()
            print(_)
            input("----------")
        train.move_clockwise()

    if DEBUG:
        track.print()
        input("----------")


def train_crash(chart, a_train, a_train_pos, b_train, b_train_pos, limit):
    track = build_Track(chart.splitlines())
    track.print()
    build_Train(track, a_train, a_train_pos)
    build_Train(track, b_train, b_train_pos)
    
    if DEBUG:
        track.print()
        input("----------")
    if track.check_colision():
        return 0
    
    colision_time = -1
    for i in range(1, limit+1):
        track.move_trains()
        if DEBUG:
            track.print()
            input("----------")
        if track.check_colision():
            colision_time = i
            break
    if DEBUG:
        print(colision_time)
    return colision_time
