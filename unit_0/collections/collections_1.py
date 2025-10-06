import random
def create_random_list(size=10, lower_bound=1, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]  
def main():
    random_list = create_random_list()
    print("Generated list of random integers:", random_list)
if __name__ == "__main__":
    main()  
