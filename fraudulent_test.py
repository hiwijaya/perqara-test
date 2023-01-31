import statistics


def get_n_and_d():

    while True:
        try:
            n, d = input().split()

            n = int(n)
            d = int(d)

            if not (1 <= n & n <= 2 * 10 ** 5):
                raise Exception('1 <= n <= 2*10^5')
            if not (1 <= d & d <= n):
                raise Exception('1 <= d <= n')

            return n, d
        except Exception as e:
            print(e)
            print('Invalid input. try again.')


def get_expenditures(given_n):

    while True:
        try:
            input_arr = input().split()

            if not len(input_arr) == given_n:
                raise Exception('n == expenditures length')

            expenditure = []
            for i in input_arr:
                i = int(i)

                if not (0 <= i & i <= 200):
                    raise Exception('0 <= expenditure[i] <= 200')

                expenditure.append(i)

            return expenditure
        except Exception as e:
            print(e)
            print('Invalid input expenditure. try again.')


def find_fraudulent_activity(expenditures, d):

    n_times = 0

    for i in range(len(expenditures)):

        if i < d:
            continue

        amount = expenditures[i]
        trailing_expenditures = expenditures[(i-d):i]

        trailing_expenditures.sort()
        median = statistics.median(trailing_expenditures)

        if amount >= (2 * median):
            n_times += 1

    return n_times


if __name__ == '__main__':

    n, d = get_n_and_d()
    expenditures = get_expenditures(n)
    n_times = find_fraudulent_activity(expenditures, d)
    print(n_times)
