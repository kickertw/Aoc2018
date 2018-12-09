from datetime import datetime

class TimeLog:
    def __init__(self, time, message):
        self.timestamp = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        self.message = message.rstrip()

    def get_id(self):
        tmp = self.message.split()
        return int(tmp[1][1:])

class GuardLog:
    def __init__(self, id):
        self.id = id
        self.sleepy_time = 0
        self.sleep_tracker = [0] * 60
    
    def most_sleepy_min(self):
        max_min = 0
        max_min_val = self.sleep_tracker[0]
        for ii in range(1,60):
            if self.sleep_tracker[ii] > max_min_val:
                max_min = ii
                max_min_val = self.sleep_tracker[ii]
        return max_min, max_min_val

    def pprint(self):
        print("{} - slept {} - most sleepy at {} minute mark".format(self.id, self.sleepy_time, self.most_sleepy_min()))
        # print(self.sleep_tracker)

guard_list = {}
time_log = list()

with open("./inputs/day4.txt", "r") as f:
    for line in f:
        time_log.append(TimeLog(line[1:17]+":00" , line[19:]))

time_log.sort(key=lambda x: x.timestamp)

current_guard = "#?"
current_sleep_min = 0

for log in time_log:
    if log.message.startswith("Guard"):
        current_guard = log.get_id()
        if current_guard not in guard_list:
            guard_list[current_guard] = GuardLog(current_guard)
    elif log.message == "falls asleep":
        current_sleep_min = log.timestamp.minute
    elif log.message == "wakes up":
        guard_list[current_guard].sleepy_time += log.timestamp.minute - current_sleep_min
        for ii in range(current_sleep_min, log.timestamp.minute):
            guard_list[current_guard].sleep_tracker[ii] += 1 

#part 1
max_sleepy_time = 0
max_min = 0
max_msm_count = 0

for key, guard in guard_list.items():
    if guard.sleepy_time > max_sleepy_time:
        sleepiest_guard = guard
        max_sleepy_time = guard.sleepy_time
    
    msm, msm_count = guard.most_sleepy_min()
    if msm_count > max_msm_count:
        sleepiest_min_guard = guard
        max_msm_count = msm_count
        max_min = msm

msm, msm_count = sleepiest_guard.most_sleepy_min()
print("part 1 answer = {}".format(sleepiest_guard.id * msm))
print("part 2 answer = {}".format(sleepiest_min_guard.id * max_min))