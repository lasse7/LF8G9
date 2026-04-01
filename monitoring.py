import psutil
import argparse
from alarm import check_value


def check_memory(soft, hard):
    memory = psutil.virtual_memory().percent
    return check_value(memory, soft, hard, "Memory usage (%)")


def check_processes(soft, hard):
    processes = len(psutil.pids())
    return check_value(processes, soft, hard, "Process count")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mem-soft", type=int, default=70)
    parser.add_argument("--mem-hard", type=int, default=90)
    parser.add_argument("--proc-soft", type=int, default=150)
    parser.add_argument("--proc-hard", type=int, default=300)

    args = parser.parse_args()

    print("Memory:", check_memory(args.mem_soft, args.mem_hard))
    print("Processes:", check_processes(args.proc_soft, args.proc_hard))


if __name__ == "__main__":
    main()