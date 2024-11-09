import time
import psutil
import resource


def omit_if_none(target):
    return {key: value for key, value in target.items() if value is not None}


def flatten(nested_list):
    return [item for row in nested_list for item in row]


def benchmark_start():
    process = psutil.Process()
    start_time = time.time()
    start_gmtime = time.gmtime(start_time)

    return {
        "process": process,
        "start_time": start_time,
        "start_datetime": time.strftime("%Y-%m-%d %H:%M:%S", start_gmtime),
    }


def benchmark_end(data):
    end_time = time.time()
    end_gmtime = time.gmtime(end_time)
    end_datetime = time.strftime("%Y-%m-%d %H:%M:%S", end_gmtime)
    time_usage = end_time - data["start_time"]
    cpu_usage = resource.getrusage(resource.RUSAGE_SELF).ru_utime
    memory_usage = data["process"].memory_info().rss

    with open("logs.txt", "a") as file1:
        file1.write(
            f"start: {data['start_datetime']}, end: {end_datetime}, took: {time_usage}, cpu usage: {cpu_usage}secs, ram usage: {memory_usage / (1024 ** 2)}MB\n"
        )
