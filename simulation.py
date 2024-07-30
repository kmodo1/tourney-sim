from simulators import round_robin_tournament

def main():
    round_robin_results = round_robin_tournament()
    for p in round_robin_results:
        print(p)

if __name__ == "__main__": main()