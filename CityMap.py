from LoggerConfig import *

logger = logging.getLogger(__name__)


class CityMap:
    def __init__(self, node_number, edge_number, data_begin, data_end):
        logger.info("CityMap 初始化")
        self.node_number = node_number
        self.edge_number = edge_number
        self.data_begin = data_begin
        self.data_length = data_end - data_begin
        self.city_map = {}
        if edge_number < node_number - 1:
            logger.warning("设定边数为{0}小于{1}-1,默认设置为{2}-1".format(edge_number, node_number, node_number))
            self.edge_number = node_number - 1
        elif edge_number > node_number * (node_number - 1) // 2:
            logger.warning("设定边数为{0}大于{1}*({2}-1)/2,默认设置为{3}-1".format(edge_number, node_number, node_number,
                                                                       node_number))
            self.edge_number = node_number * (node_number - 1) // 2

    def add_edge(self, node_begin, node_end, data_temp):
        if node_begin in self.city_map.keys():
            self.city_map[node_begin][node_end] = data_temp
        else:
            self.city_map[node_begin] = {node_end: data_temp}
        if node_end in self.city_map.keys():
            self.city_map[node_end][node_begin] = data_temp
        else:
            self.city_map[node_end] = {node_begin: data_temp}

    def build(self):
        logger.info("生成图")
        node_set = set()
        edge_number = 0
        available_edge = {}
        normal_list = Normal(self.data_begin + self.data_length // 2, self.data_length / 4, self.edge_number)
        self.city_map = {}
        for i in range(self.node_number):
            set_temp = set(range(self.node_number))
            set_temp.remove(i)
            available_edge[i] = set_temp
        node_set.add(0)
        for node_end in range(1, self.node_number):
            list_temp = list(node_set)
            node_begin = list_temp[int(len(list_temp) * np.random.rand())]
            data_temp = normal_list.randn()
            self.add_edge(node_begin, node_end, data_temp)
            node_set.add(node_end)
            edge_number += 1
            available_edge[node_begin].remove(node_end)
            available_edge[node_end].remove(node_begin)
        for i in range(edge_number, self.edge_number):
            while True:
                node_begin = int(self.node_number * np.random.rand())
                node_end = int(self.node_number * np.random.rand())
                if node_end in available_edge[node_begin]:
                    break
            data_temp = normal_list.randn()
            self.add_edge(node_begin, node_end, data_temp)
            available_edge[node_begin].remove(node_end)
            available_edge[node_end].remove(node_begin)

    def get_map(self):
        logger.info("返回city_map邻接表")
        logger.debug(self.city_map)
        return self.city_map

    def save(self, file_path):
        np.save(file_path, self.city_map)
