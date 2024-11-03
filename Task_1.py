import queue
import time
import threading

request_queue = queue.Queue()

def generate_request():
    request_id = int(time.time() * 1000)
    print(f"Generated request ID: {request_id}")
    request_queue.put(request_id)

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Processing request ID: {request_id}")
        request_queue.task_done()
    else:
        print("The queue is empty. No requests to process.")

def main():
    try:
        while True:
            generate_request()
            time.sleep(1)

            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program exited by user")

if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()
