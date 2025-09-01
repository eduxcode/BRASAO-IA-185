import re
import numpy as np

def analyze_training_logs(log_file_path):
    execution_times = []
    with open(log_file_path, 'r') as f:
        for line in f:
            match = re.search(r'Execution Time = (\d+\.\d+)s', line)
            if match:
                execution_times.append(float(match.group(1)))

    if not execution_times:
        print("No execution times found in the log file.")
        return

    mean_time = np.mean(execution_times)
    std_dev_time = np.std(execution_times)

    print(f"Mean Execution Time: {mean_time:.2f}s")
    print(f"Standard Deviation of Execution Time: {std_dev_time:.2f}s")

if __name__ == "__main__":
    log_file = "Atividade7/training_log.txt"
    analyze_training_logs(log_file)
