# Kordebalet67
# Testing module is made to check resources of PC 
# using to run any programm.
# ----------------------------------------------------
# To check program import main.py of your programm as
# other module like "math" and run this code.

import time
import psutil
import os
import main as check

# Testing function
def test_function():
    
    start_time = time.time()
    check.main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time} секунд")

    # Измерение использования процессора и памяти
    process = psutil.Process(os.getpid())
    cpu_usage = process.cpu_percent(interval=1)
    memory_info = process.memory_info()
    print(f"Использование процессора: {cpu_usage}%")
    print(f"Использование памяти: {memory_info.rss / (1024 * 1024)} MB")


if __name__ == '__main__':
    test_function()