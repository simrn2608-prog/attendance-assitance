import streamlit as st
import math
import pandas as pd

st.title("Attendance Calculator")
st.write("Enter your attendance details below.")

# ---------------- FORM ----------------

with st.form("attendance_form"):

    subject = st.text_input("Subject name")

    attended_classes = st.number_input(
        "Classes attended",
        min_value=0,
        step=1
    )

    total_classes = st.number_input(
        "Total classes held",
        min_value=0,
        step=1
    )

    required_attendance = st.slider(
        "Required attendance (%)",
        min_value=1,
        max_value=100,
        value=75
    )

    submitted = st.form_submit_button("Calculate")




# ---------------- CALCULATION ----------------

safe=True
current_attendance=0
data=0

if submitted:

    # Validation
    if total_classes == 0:
        st.error("Total classes cannot be zero.")

    elif attended_classes > total_classes:
        st.error("Attended classes cannot be greater than total classes.")

    else:

        current_attendance = (
            attended_classes / total_classes
        ) * 100

        st.write(f"### {subject}")
        st.write(
            f"Current attendance: **{current_attendance:.2f}%**"
        )

        # ---------------- SAFE ----------------

        if current_attendance >= required_attendance:


            st.success("You are safe ✅")

            target = required_attendance / 100

            # Special case: 100%
            if required_attendance == 100:
                st.write(
                    "You cannot miss any class if you want to maintain 100% attendance."
                )

            else:

                allowed_misses = (
                    attended_classes / target
                ) - total_classes

                allowed_misses = math.floor(allowed_misses)

                st.write(
                    f"You can safely miss **{allowed_misses} classes** "
                    f"and still maintain at least {required_attendance}% attendance."
                )
                allowed_misses=data
                st.write(f"-----------------{data}---------------")

        # ---------------- SHORT ----------------

        else:
            safe=False

            st.error("You are short in attendance ❌")

            target = required_attendance / 100

            # Special case: target = 100%
            if required_attendance == 100:

                st.write(
                    "You cannot reach exactly 100% attendance because "
                    "you have already missed one or more classes."
                )

            else:

                required_classes = (
                    (target * total_classes) - attended_classes
                ) / (1 - target)

                required_classes = math.ceil(required_classes)

                st.write(
                    f"You need to attend the next "
                    f"**{required_classes} classes continuously** "
                    f"to reach at least {required_attendance}% attendance."
                )
                required_classes=data
                st.write(f"-----------------{data}---------------")


#---------------------df------------------------
df = pd.DataFrame({' ':['Attended classes','Total classes',"Current attendance","Safe"], f'{subject}': [f'{attended_classes}',f'{total_classes}',f'{(current_attendance):.2f}',f'{safe}']})
df
