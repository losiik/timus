pos = 1
prev_pos = 1
counter = 0
mailbox_1 = ['Alice', 'Ariel', 'Aurora', 'Phil', 'Peter', 'Olaf', 'Phoebus', 'Ralph', 'Robin']
mailbox_2 = ['Bambi', 'Belle', 'Bolt', 'Mulan', 'Mowgli', 'Mickey', 'Silver', 'Simba', 'Stitch']
mailbox_3 = ['Dumbo', 'Genie', 'Jiminy', 'Kuzko', 'Kida', 'Kenai', 'Tarzan', 'Tiana', 'Winnie']

n = int(input())

for i in range(n):
    name = input()
    if name in mailbox_1:
        pos = 1
    elif name in mailbox_2:
        pos = 2
    else:
        pos = 3

    counter += abs(pos - prev_pos)
    prev_pos = pos

print(counter)
