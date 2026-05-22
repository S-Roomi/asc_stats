import pdfplumber

FILE = "listing.pdf"

def parse_duration(duration: str):
    time = 0
    # some strings might have \n in them, just replace it with a space and split it
    for elem in duration.replace('\n', " ").split(" "):
        if elem[-1] == 'h':
            time = int(elem[:-1]) * 60
        elif elem[-1] == 'm':
            time += int(elem[:-1]) 
    return time

def get_stats(pdf: pdfplumber.pdf.PDF) -> dict:
    unique = []
    time_worked = 0
    for page in pdf.pages:
        for row in page.extract_table()[1:] or []: 
            #for getting unique names
            if row[1] not in unique and row[1] != '':
                # print(row)
                unique.append(row[1])
            # for getting time tutored worked
            if row[0] == '\uf192':
                time_worked += parse_duration(row[7])
    return {"unique students": len(unique), "time worked": time_worked}


if __name__ == "__main__":
    # print(f'Hours Worked: {total_time()/60}')
    stats = None
    with pdfplumber.open(FILE) as pdf:
        stats = get_stats(pdf)
    print(f'Number of unique students {stats.get("unique students")}')
    print(f'Number of hours worked {stats.get("time worked")/60} hours or {stats.get("time worked")} minutes')
