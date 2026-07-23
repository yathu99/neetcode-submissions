class TimeMap:

    def __init__(self):
        self.store=dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[(timestamp,value)]
        else:
            self.store[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.store):
            return ""
        curr=len(self.store[key])-1
        while(curr>=0 and self.store[key][curr][0]>timestamp):
                curr-=1
        return self.store[key][curr][1] if curr>=0 else ""

