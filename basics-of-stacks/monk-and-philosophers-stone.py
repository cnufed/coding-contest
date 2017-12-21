coins_count = int(input())
coins_string = input()
coins = [int(x) for x in coins_string.split(" ")]
values = input()
q, x = [int(x) for x in values.split(" ")]

bucket = []
def harry():
    if len(coins) > 0:
        bucket.append(coins.pop(0))


def remove():
    if len(bucket) > 0:
        bucket.pop(-1)


def sum_bucket():
    return sum(bucket) == x


coins_answer = -1
for l in range(q):
    line = input()
    if line == "Harry":
        harry()
    else:
        remove()

    if sum_bucket():
        coins_answer = len(bucket)

print(coins_answer)
