from bs4 import BeautifulSoup
import requests





def login(email,password):

    # email = input("Email: ")
    # password = getpass.getpass("Password: ")

    login_data = {
        "role_id": "3",
        "email": email,
        "password": password
    }

    session = requests.Session()

    response = session.post(
        "https://erp.mmumullana.org/login/validate_login",
        data=login_data
    )

    print("Status:", response.status_code)
    print("Final URL:", response.url)

# todo validate login later
    
    return session


def fetch_data(session):
    attendance_response = session.get(
        "https://erp.mmumullana.org/student/attendance_record"
    )


    print("Attendance status:", attendance_response.status_code)
    print("Length:", len(attendance_response.text))
    # print(attendance_response.text())



    
    # subject=""
    # attended=0
    # total=0
    
    return attendance_response


def parse_data(attendance_response):

    soup = BeautifulSoup(attendance_response.text, 'html.parser')

    # ---------------- FIND ATTENDANCE TABLE ----------------

    attendance_table = soup.find(
        "table",
        id="table_export"
    )

    if attendance_table is None:
        print("Attendance table not found.")
        exit()


    # ---------------- GET SUBJECTS ----------------

    thead = attendance_table.find("thead")

    headers = thead.find_all("th")

    subjects = []

    # Skip first heading because it is "Description"
    for header in headers[1:]:

        subject_name = header.get_text(
            " ",
            strip=True
        )

        subjects.append(subject_name)



   


    # ---------------- GET ATTENDANCE DATA ----------------

    tbody = attendance_table.find("tbody")

    rows = tbody.find_all("tr")


   


    for row in rows:

        cells = row.find_all("td")

        # Skip empty rows
        if len(cells) == 0:
            continue


        # First column contains things like:
        # Percentage
        # Suggestion to attend...
        description = cells[0].get_text(
            " ",
            strip=True
        )

        if "Percentage" not in description:
            continue


        # Remaining columns correspond to subjects
        values = []

        for cell in cells[1:]:

            value = cell.get_text(
                " ",
                strip=True
            )

            values.append(value)


   



    ateen_data = []


    for a,v in zip(subjects,values):
        atten = {"subject": a,
                "Percentage":v}
        ateen_data.append(atten)
        
    return ateen_data


    # rows = soup.find_all('tr')

    # for row in rows:
    #     cells = row.find_all("td")  
    #     # if len(cells)==3:
    #     subject = cells[0].get_text() 
    #     attended = cells[1].get_text()
    #     total= cells[2].get_text()
    #     print(subject + " " + str(attended) + " " + str(total))











# call login → save returned session

# call fetch_data using that session → save returned response

# call parse_data using that response → save returned data

# session = login(11252689,9671701790)
# response = fetch_data(session)
# data = parse_data(response)

# print(data)