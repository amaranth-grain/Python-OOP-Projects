import city_processor as cp
import threading
import time


class CityOverheadTimeQueue:
    def __init__(self):
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: cp.CityOverheadTimes) -> None:
        """
        Append CityOverheadTimes to the data_queue list.
        :param overhead_time: CityOverheadTimes
        :return: None
        """
        with self.access_queue_lock:
            self.data_queue.append(overhead_time)

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
            json = cp.ISSDataRequest.get_overhead_pass(city)
            self.queue.put(cp.CityOverheadTimes(city, json["response"]))
            count += 1
            if count % 5 == 0:
                time.sleep(1)


class ProducerThread2(threading.Thread):
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
            json = cp.ISSDataRequest.get_overhead_pass(city)
            self.queue.put(cp.CityOverheadTimes(city, json["response"]))
            count += 1
            if count % 5 == 0:
                time.sleep(1)


class ConsumerThread(threading.Thread):

    def __init__(self, queue: CityOverheadTimeQueue):
        """
        Initialises with the same queue that the ProducerThread has.
        :param queue: CityOverheadQueue
        """
        super().__init__()
        self.data_incoming = True
        self.queue = queue

    def run(self) -> None:
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
    db = cp.CityDatabase("city_locations_test.xlsx")
    p_thread = ProducerThread(db.city_db, q)
    c_thread = ConsumerThread(q)
    p_thread.start()
    c_thread.start()
    p_thread.join()
    c_thread.data_incoming = False
    c_thread.join()
    # change consumer attribute data_incoming to false after producer
    # thread joins main


    # print([city.city_name for city in p_thread.cities])
    # print([item for item in p_thread.queue.data_queue])
    # q = CityOverheadTimeQueue()
    # db = cp.CityDatabase("city_locations_test.xlsx")
    #
    # for city in db.city_db:
    #     json = cp.ISSDataRequest.get_overhead_pass(city)
    #     # print(json["response"])
    #     q.put(cp.CityOverheadTimes(city, json["response"]))
    #
    #
    # for city in db.city_db:
    #     json = cp.ISSDataRequest.get_overhead_pass(city)
    #     q.put(cp.CityOverheadTimes(city, json["response"]))
    # #     q.put(cp.CityOverheadTimes(city, json))
    # # print(len(q))
    # print(q.data_queue)


if __name__ == "__main__":
    main()
