import redis
from datetime import datetime
from json import dumps,loads


class queue():
    def __init__(self):
        self.connection = redis.StrictRedis(host='localhost',port=6379, db=0)


    def currentTime(self):
        datetimeOBJ = datetime.now()
        timestamp = datetimeOBJ.strftime("%d-%b-%Y %H:%M:%S")
        return timestamp


    def setExpire(self):
        self.connection.expire("dataLidar",86400)


    def pushQueue(self, data):
        try:
            push_to_queue = self.connection.rpush("dataLidar", dumps({"timestamp":self.currentTime(),"data":data}))
            self.setExpire()
            return True
        except:
            return False


    
    def FifoPopQueue(self):
        try:
            pop_from_queue = self.connection.rpop("dataLidar")
            pop_from_queue = loads(pop_from_queue)
            return pop_from_queue
        except:
            return None



    def LifoPopQueue(self):
        try:
            pop_from_queue = self.connection.lpop("dataLidar")
            pop_from_queue = loads(pop_from_queue)
            return pop_from_queue
        except:
            return None