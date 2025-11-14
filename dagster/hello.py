from time import sleep
SECONDS_IN_MINUTES = 60
INTERVAL_IN_MINUTES = 5
TIME_INTERVAL = SECONDS_IN_MINUTES * INTERVAL_IN_MINUTES


def main():
    for i in range(60):
        sleep(TIME_INTERVAL)
        print(f'elapsed time is {i*INTERVAL_IN_MINUTES} minutes')

if __name__ == "__main__":
    main()
