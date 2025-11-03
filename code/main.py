for i in range(1,6):
    with open(f'file{i}.txt','w') as f:
        f.write(f'This is file number {i}')