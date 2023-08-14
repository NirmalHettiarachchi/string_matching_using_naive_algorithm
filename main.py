def main():
    NUM_TESTS = 4
    
    pattern_files = [f'test_cases/pattern{i}.txt' for i in range(1, NUM_TESTS + 1)]
    text_files = [f'test_cases/text{i}.txt' for i in range(1, NUM_TESTS + 1)]

    for i in range(NUM_TESTS):
        pattern_file = pattern_files[i]
        text_file = text_files[i]
        output_file = f'out/patternmatch{i + 1}.output.txt'

        ptn_file = read_file(pattern_file)
        txt_file = read_file(text_file)

        if ptn_file and txt_file:
            pos_list = get_pattern_positions(ptn_file.read(), txt_file.read())
            write_file(pos_list, output_file)
            print(f"Completed {pattern_file} and {text_file}. Output saved to {output_file}")
        else:
            print(f"Couldn't find required file/s for {pattern_file} and {text_file}!")

def read_file(file_name):
    try:
        file = open(file_name, "r")
        return file
    except FileNotFoundError:
        return False
    
def write_file(pos_list, output_file_name):
    output_file = open(output_file_name, "w")
    for pos in pos_list:
        output_file.write(str(pos) + "\n")

def get_pattern_positions(ptn, txt):
    pos_list = []
    ptn = ptn.strip()
    txt = txt.strip()
    ptn_len = get_ptn_len(ptn)
    txt_len = len(txt)

    for i in range(txt_len - ptn_len + 1):
        ptn_index = 0
        offset = 0

        while ptn_index < ptn_len:
            if ptn[ptn_index] == "^":
                if i == 0:
                    ptn_index += 1
                    offset += 1
                else:
                    break
            elif ptn[ptn_index] == "$":
                if i + ptn_index == txt_len:
                    ptn_index += 1
                    offset += 1
                else:
                    break
            elif (ptn[ptn_index] == txt[i+ptn_index-offset]) or ptn[ptn_index] == '.':
                ptn_index += 1
            else:
                break

        if ptn_index == ptn_len:
            pos_list.append(i)
        
    return pos_list

def get_ptn_len(ptn):
    count = 0
    for char in ptn:
        if char != "$" and char != "^":
            count += 1
    return count

if __name__ == "__main__":
    main()
