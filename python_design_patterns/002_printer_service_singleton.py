import threading

class Printer:
    _instance_lock = threading.Lock()
    _unique_instance = None # assign the first instance created

    def __new__(cls):
        with cls._instance_lock:
            if cls._unique_instance is None:
                # if not instance exists, create new instance
                cls._unique_instance = super(Printer, cls).__new__(cls)
                cls._unique_instance._init_printer()
        return cls._unique_instance

    def _init_printer(self):
        self.mode = "GrayScale"
    
    def get_printer_status(self):
        return self.mode
    
    def set_mode(self, mode):
        self.mode = mode
        print(f"Mode changed to {mode}")

if __name__ == "__main__":
    worker1 = Printer()
    worker2 = Printer()

    worker1.set_mode("Color")
    worker2.set_mode("Grayscale")

    worker1_mode = worker1.get_printer_status()
    worker2_mode = worker2.get_printer_status()