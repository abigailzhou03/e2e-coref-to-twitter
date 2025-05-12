import os
import sys
import random

def main():
    parent_dir = sys.argv[1]
    file_ids = []
    test = [6, 7, 14, 29, 98, 138, 144, 35, 64, 81, 91, 92, 95, 96, 117, 137, 140, 150, 153, 172]
    for conll in os.listdir(parent_dir):
        with open(parent_dir + conll, "r", encoding="utf-8") as c:
            conll2 = list(c)
            temp=[]
            for e in conll2:
                if '#end' not in e:
                    temp.append(e)
                else:
                    temp.append(e)
                    i = temp[0].split('; part')[-1].strip()
                    if int(i) not in test:
                        file_ids.append(int(i))
    # dev_ids = random.sample(file_ids, 20)
    dev_ids = [8, 21, 26, 33, 46, 50, 54, 57, 63, 78, 83, 89, 90, 110, 125, 130, 136, 158, 159, 177]
    dev_ids_sorted = sorted(dev_ids)
    print(dev_ids_sorted)
    return

if __name__ == "__main__":
    main()