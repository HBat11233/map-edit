from LoggerConfig import *

logger = logging.getLogger(__name__)


class CarTrajectory:
    def __init__(self, car_number, car_speed_min, car_speed_max, fps, time_line, city_map):
        logger.info("CarTrajectory 初始化")
        self.car_number = car_number
        self.car_speed_max = car_speed_max
        self.car_speed_min = car_speed_min
        self.time_line = time_line
        self.city_map = city_map
        self.car_list = []

    def build(self):
        city_map = self.city_map.get_map()
        for i in range(self.car_number):
            speed_normal = Normal((self.car_speed_max + self.car_speed_min) // 2,
                                  (self.car_speed_max - self.car_speed_min) // 4, 100)
            node_set = set()
            time_count = 0
            car_path = []
            node_temp = int(self.city_map.node_number * np.random.rand())
            node_set.add(node_temp)
            car_path.append(node_temp)
            flag = True
            while time_count < self.time_line and flag:
                if len(city_map[node_temp]) == 0:
                    break
                remove_set = set()
                while True:
                    pos = int(len(city_map[node_temp]) * np.random.rand())
                    pos = list(city_map[node_temp].keys())[pos]
                    if pos not in remove_set:
                        if pos not in node_set:
                            node_set.add(pos)
                            break
                        else:
                            remove_set.add(pos)

                    if len(city_map[node_temp]) <= len(remove_set):
                        flag = False
                        break

                if not flag:
                    break

                if speed_normal.empty():
                    speed_normal = Normal((self.car_speed_max + self.car_speed_min) // 2,
                                          (self.car_speed_max - self.car_speed_min) // 4, 100)
                speed = speed_normal.randn()
                time_temp = int(city_map[node_temp][pos] / speed)
                time_count += time_temp
                car_path.append(time_count)
                car_path.append(pos)
                node_temp = pos
            self.car_list.append(car_path)

    def get_list(self):
        logger.info("返回car_list")
        return self.car_list

    def save(self, file_path):
        with open(file_path, 'w') as f:
            for i in self.car_list:
                for inx, val in enumerate(i):
                    if inx != 0:
                        f.write(' ')
                    f.write(str(val))
                f.write('\n')
            f.close()
        np.save(file_path,self.car_list)
