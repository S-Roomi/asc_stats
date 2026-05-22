import pdfplumber
import argparse

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
    courses_tutored = []
    for page in pdf.pages:
        for row in page.extract_table()[1:] or []: 
            # for getting unique names
            if row[1] not in unique and row[1] != '':
                # print(row)
                unique.append(row[1])

            # for getting courses tutored
            if row[4] not in courses_tutored and row[4] != '':
                courses_tutored.append(row[4])
            
            # for getting time tutored worked
            if row[0] == '\uf192':
                time_worked += parse_duration(row[7])

    courses_tutored.sort()
    return {
        "unique_students": len(unique), 
        "time_worked": time_worked, 
        "courses_tutored": courses_tutored
    }


if __name__ == "__main__": 
    

    parser = argparse.ArgumentParser(
        prog="asc_stats",
        description="Simple scripts used to gather information for tutors who worked at the Academic Success Center",
        epilog="HELPPPPPPPPPPP"
    )

    parser.add_argument("filename", default="listing.php.pdf", type=str, help="Please provide the file or file path to the TracCloud pdf")




    args = parser.parse_args()

    stats = None
    with pdfplumber.open(args.filename) as pdf:
        stats = get_stats(pdf)
    print(f'Number of unique students {stats.get("unique_students")}')
    print(f'Number of hours worked {stats.get("time_worked")/60} hours or {stats.get("time_worked")} minutes')
    print(f'Courses tutored: ', end='')

    course_list = stats.get("courses_tutored")
    course_list_len = len(course_list)
    for i, course in enumerate(course_list):
        if i < course_list_len - 1:
            print(course, end=", ")
        else:
            print(course)