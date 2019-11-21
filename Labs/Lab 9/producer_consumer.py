"""
Producers make API calls, stores it into a buffer, and Consumer uses it and
removes it from the buffer.
"""

import city_processor as cp
import threading
import time
import logging


class CityOverheadTimeQueue:
    """
    Buffer where CityOverheadTimes are stored prior to consumption.
    """
    def __init__(self):
        """
        Initialises Queue with an empty list and lock for threadsafe access.
        """
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: cp.CityOverheadTimes) -> None:
        """
        Append CityOverheadTimes to the data_queue list.
        :param overhead_time: CityOverheadTimes
        :return: None
        """
        with self.access_queue_lock:
            logging.info(f"{threading.current_thread().name}"
                         f" acquired lock and added "
                         f"{overhead_time.city.city_name} to the queue.")
            self.data_queue.append(overhead_time)
            logging.info(f"{threading.current_thread().name}"
                         f" released lock!")

    def get(self) -> cp.CityOverheadTimes:
        """
        Remove an element from data_queue. Pops the first element
        off as queues are FIFO.
        :return:
        """
        with self.access_queue_lock:
            item = self.data_queue[0]
            del self.data_queue[0]
            return item
            # return self.data_queue.pop(0)

    def __len__(self) -> int:
        """
        Return the length of the data_queue
        :return:
        """
        return len(self.data_queue)


class ProducerThread(threading.Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        """
        Initialise the thread with a list of City objects and
        CityOverheadTimeQueue.
        :param cities:
        :param queue:
        """
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        """
        Executes when thread starts.  Loops over each city and passes it
        to ISSDataRequest, and adds each city to the queue.
        :return:
        """
        count = 0
        for city in self.cities:
            logging.info(f"{threading.current_thread().name}"
                         f" is downloading info on {city.city_name}")
            city_overhead_times = cp.ISSDataRequest.get_overhead_pass(city)
            self.queue.put(city_overhead_times)
            count += 1
            if count % 5 == 0:
                time.sleep(1)


class ConsumerThread(threading.Thread):
    """
    Consumer thread prints information out.
    """

    def __init__(self, queue: CityOverheadTimeQueue):
        """
        Initialises with the same queue that the ProducerThread has.
        :param queue: CityOverheadQueue
        """
        super().__init__()
        self.data_incoming = True
        self.queue = queue

    def run(self) -> None:
        """
        Called when thread is started.
        :return: None
        """
        while self.data_incoming or len(self.queue) > 0:
            if len(self.queue) > 0:
                print(f"======================\n"
                      f"{self.queue.data_queue.pop(0)}\n"
                      f"======================\n")
                time.sleep(0.5)
            else:
                time.sleep(0.75)


def main():
    q = CityOverheadTimeQueue()
    db = cp.CityDatabase("city_locations.xlsx")
    # db = cp.CityDatabase("city_locations_test.xlsx")
    items_to_process = len(db.city_db)
    threads = 3
    cities_per_thread = round(items_to_process / threads)
    logging.info("Main: Before creating threads")
    start_time = time.time()

    p_thread = ProducerThread(db.city_db[0:cities_per_thread:], q)
    p2_thread = ProducerThread(db.city_db[cities_per_thread:(
            cities_per_thread*2):], q)
    p3_thread = ProducerThread(db.city_db[(cities_per_thread*2)::], q)
    c_thread = ConsumerThread(q)
    p_thread.start()
    p2_thread.start()
    p3_thread.start()
    c_thread.start()
    p_thread.join()
    p2_thread.join()
    p3_thread.join()
    c_thread.data_incoming = False
    c_thread.join()

    duration = time.time() - start_time
    print(f"Downloaded data on {items_to_process} cities {duration} seconds")


if __name__ == "__main__":
    _format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=_format, level=logging.INFO, datefmt="%H:%M:%S")
    main()
