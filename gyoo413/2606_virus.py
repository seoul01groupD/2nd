node = int(input())
count = int(input())
link_list = [list(map(int, input().split())) for _ in range(link)]

output = [1]

for link in link_list:
    for i in range(2):
        if link[i] in output:
            output.append(link[i])