# Палатка
# 30 человек подходят к палатке
# если очередь 3 человека, тогда остальные уходят
# если нет, тогда встают в очередь
# время обслуживания константа или рандом. ВЫбрано Константа

import random
import collections
import queue
import argparse
import time

DEFAULT_NUMBER_OF_QUENE = 3     # Размер очереди
WAIT_DURATION = 20              # продолжительность ожидания
SERVICE_DURATION = 5            # продолжительность обслуживания клиента
ARRIVAL_INTERVAL = 8            # интервал появления людей
flag = True

Event = collections.namedtuple('Событие', 'Время Участники Действие')

# Время начала симуляции работы палатки
def tent_process(ident, trips, start=30, flag):  
    time = yield Event(start, ident, 'Прибытие очереди людей')  
    while flag: 
        time = yield Event(time, ident, 'Люди встали в очередь') 
        time = yield Event(time, ident, 'Люди ушли')

class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self):  # <1>
        """Планирование и отображение событий до истечения времени"""
        # запланируйте первое событие для каждой машины
        for _, proc in sorted(self.procs.items()):  
            first_event = next(proc)  # <3>
            self.events.put(first_event)  # <4>

        # главный цикл работы симуляции
        sim_time = 0  # <5>
        while True:
            if self.events.empty(): 
                print('*** end of events ***')
                break

            if (queue_people > 3):
                flag = False

            else:
                queue += 1

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event 
            print('taxi:', proc_id, proc_id * '   ', current_event) 
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id] 
            else:
                self.events.put(next_event)
        else: 
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))
# Завершение симуляции работы палатки


def compute_duration(previous_action):
    """Вычисление длительность действия с использованием экспоненциального распределения"""
    if previous_action in ['Люди ушли', 'Человек обслужен']:
        # Время интервала - поиск клиента
        interval = WAIT_DURATION
    elif previous_action == 'Люди встали в очередь':
        # Время интервала - время поездки
        interval = SERVICE_DURATION
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1


def main(num_queue=DEFAULT_NUMBER_OF_QUENE, seed=None):
    """Initialize random generator, build procs and run simulation"""
    if seed is not None:
        random.seed(seed)  # получить воспроизводимые результаты

    i = 1
    queue_people = 30
    flager = True
    taxis = {i: tent_process(i, (i+1)*2, i*ARRIVAL_INTERVAL, flager)}
    sim = Simulator(taxis)
    sim.run()

main()