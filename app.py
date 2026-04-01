import streamlit as st
import datetime

st.set_page_config(page_title="My Diet Plan", layout="centered")

st.title("Το Πρόγραμμα Μου")

diet_plan = {
    "Monday": {
        "Πρωινό": "Βρώμη με γάλα αμυγδάλου",
        "Μεσημεριανό": "Στήθος κοτόπουλο με σαλάτα",
        "Απογευματινό": "1 μήλο",
        "Βραδινό": "Σαλάτα με 1 αυγό βραστό"
    },
    "Tuesday": {
        "Πρωινό": "2 φρυγανιές ολικής με μέλι",
        "Μεσημεριανό": "Ψάρι ψητό με χόρτα",
        "Απογευματινό": "Λίγα αμύγδαλα",
        "Βραδινό": "Γιαούρτι με χαμηλά λιπαρά"
    },
    "Wednesday": {
        "Πρωινό": "Βρώμη με γάλα αμυγδάλου",
        "Μεσημεριανό": "Φακές με σαλάτα",
        "Απογευματινό": "1 πορτοκάλι",
        "Βραδινό": "Σαλάτα εποχής"
    },
    "Thursday": {
        "Πρωινό": "2 φρυγανιές ολικής με μέλι",
        "Μεσημεριανό": "Μακαρόνια ολικής με σάλτσα ντομάτας",
        "Απογευματινό": "Λίγα αμύγδαλα",
        "Βραδινό": "Γιαούρτι με χαμηλά λιπαρά"
    },
    "Friday": {
        "Πρωινό": "Βρώμη με γάλα αμυγδάλου",
        "Μεσημεριανό": "Μπιφτέκια μοσχαρίσια με σαλάτα",
        "Απογευματινό": "1 μήλο",
        "Βραδινό": "Σαλάτα με 1 αυγό βραστό"
    },
    "Saturday": {
        "Πρωινό": "2 φρυγανιές ολικής με μέλι",
        "Μεσημεριανό": "Ψάρι ψητό με χόρτα",
        "Απογευματινό": "Λίγα αμύγδαλα",
        "Βραδινό": "Γιαούρτι με χαμηλά λιπαρά"
    },
    "Sunday": {
        "Πρωινό": "Βρώμη με γάλα αμυγδάλου",
        "Μεσημεριανό": "Κοτόπουλο στον φούρνο με πατάτες",
        "Απογευματινό": "1 πορτοκάλι",
        "Βραδινό": "Σαλάτα εποχής"
    }
}

days_map = {
    "Monday": "Δευτέρα", "Tuesday": "Τρίτη", "Wednesday": "Τετάρτη",
    "Thursday": "Πέμπτη", "Friday": "Παρασκευή", "Saturday": "Σάββατο", "Sunday": "Κυριακή"
}

if "meal_status" not in st.session_state:
    st.session_state.meal_status = {}
if "meal_details" not in st.session_state:
    st.session_state.meal_details = {}
if "custom_items" not in st.session_state:
    st.session_state.custom_items = []
if "daily_mood" not in st.session_state:
    st.session_state.daily_mood = {}

tab1, tab2, tab3, tab4 = st.tabs(["Ημέρα", "Ψώνια", "Μετρήσεις", "Ραντεβού & Δραστηριότητα"])

with tab1:
    selected_date = st.date_input("Επίλεξε ημερομηνία:", datetime.date.today())
    day_name = selected_date.strftime("%A")
    
    st.subheader(f"Πρόγραμμα για {days_map[day_name]} {selected_date.strftime('%d/%m/%Y')}")
    current_plan = diet_plan[day_name]
    
    for meal_time, meal_desc in current_plan.items():
        st.write(f"### {meal_time}")
        st.write(meal_desc)
        
        status_key = f"status_{selected_date}_{meal_time}"
        if status_key not in st.session_state.meal_status:
            st.session_state.meal_status[status_key] = "Δεν καταγράφηκε"
            
        choice = st.radio(
            f"Κατάσταση για το {meal_time.lower()}:",
            ["Δεν καταγράφηκε", "Κατά γράμμα", "Εναλλακτική επιλογή", "Παρασπονδία"],
            key=f"radio_{status_key}"
        )
        st.session_state.meal_status[status_key] = choice
        
        details_key = f"details_{selected_date}_{meal_time}"
        if choice in ["Εναλλακτική επιλογή", "Παρασπονδία"]:
            label = "Τι έφαγες ακριβώς;" if choice == "Παρασπονδία" else "Ποια εναλλακτική διάλεξες;"
            current_val = st.session_state.meal_details.get(details_key, "")
            detail_input = st.text_input(label, value=current_val, key=f"input_{details_key}")
            st.session_state.meal_details[details_key] = detail_input

        st.divider()

    st.subheader("Ημερολόγιο Διάθεσης")
    mood_key = f"mood_{selected_date}"
    current_mood = st.session_state.daily_mood.get(mood_key, "")
    new_mood = st.text_area("Πώς ένιωσες σήμερα; Είχες καθόλου κόπωση ή πείνα;", value=current_mood, key=f"area_{mood_key}")
    
    if st.button("Αποθήκευση Διάθεσης", key=f"btn_mood_{mood_key}"):
        st.session_state.daily_mood[mood_key] = new_mood
        st.success("Οι σημειώσεις της ημέρας καταγράφηκαν.")

with tab2:
    st.subheader("Σύνοψη Εβδομάδας")
    for eng_day, gr_day in days_map.items():
        with st.expander(f"Πρόγραμμα για {gr_day}"):
            for meal_time, meal_desc in diet_plan[eng_day].items():
                st.write(f"{meal_time}: {meal_desc}")
                
    st.divider()
    
    st.subheader("Λίστα για Ψώνια")
    base_shopping_items = [
        "Γάλα αμυγδάλου", "Βρώμη", "Στήθος κοτόπουλο", "Φρέσκια σαλάτα / Λαχανικά",
        "Μήλα", "Πορτοκάλια", "Αυγά", "Φρυγανιές ολικής", "Μέλι", "Ψάρι", 
        "Χόρτα", "Αμύγδαλα / Καρύδια", "Γιαούρτι χαμηλών λιπαρών", "Φακές", 
        "Μακαρόνια ολικής", "Σάλτσα ντομάτας", "Κοτόπουλο ολόκληρο", "Πατάτες"
    ]
    
    all_shopping_items = base_shopping_items + st.session_state.custom_items
    
    for item in all_shopping_items:
        key_name = f"shop_{item}"
        if key_name not in st.session_state:
            st.session_state[key_name] = False
        st.checkbox(item, key=key_name)

    st.write("")
    new_item = st.text_input("Πρόσθεσε νέο προϊόν στη λίστα:")
    if st.button("Προσθήκη στη λίστα"):
        if new_item and new_item not in all_shopping_items:
            st.session_state.custom_items.append(new_item)
            st.rerun()

    st.write("")
if st.button("Καθαρισμός τικ (για νέα αγορά)"):
    for key in st.session_state.keys():
        if key.startswith("shop_"):
            st.session_state[key] = False
    st.rerun()

with tab3:
    st.subheader("Ζωτικές Μετρήσεις")
    st.write("Κατάγραψε τα νούμερα σου για να τα έχεις συγκεντρωμένα.")
    
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Βάρος (κιλά)", min_value=40.0, max_value=150.0, value=80.0, step=0.1)
        systolic = st.number_input("Συστολική Πίεση (Μεγάλη)", 80, 200, 120)
    with col2:
        diastolic = st.number_input("Διαστολική Πίεση (Μικρή)", 40, 130, 80)
        sugar = st.number_input("Σάκχαρο", 50, 300, 90)

    if st.button("Αποθήκευση Μετρήσεων"):
        st.success("Οι μετρήσεις αποθηκεύτηκαν.")

    st.divider()
    
    st.subheader("Εξετάσεις Αίματος")
    st.write("Ανέβασε τις τελευταίες σου εξετάσεις για να τις βρίσκεις εύκολα.")
    uploaded_file = st.file_uploader("Επίλεξε αρχείο (PDF ή Εικόνα)", type=["pdf", "png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.success(f"Το αρχείο {uploaded_file.name} φορτώθηκε με επιτυχία.")

with tab4:
    st.subheader("Ιατρικά Ραντεβού")
    appointment_date = st.date_input("Πότε είναι η επανεξέταση στον καρδιολόγο;", datetime.date.today() + datetime.timedelta(days=60))
    
    days_left = (appointment_date - datetime.date.today()).days
    if days_left > 0:
        st.info(f"Απομένουν {days_left} ημέρες μέχρι να δούμε τα αποτελέσματα της προσπάθειάς σου.")
    elif days_left == 0:
        st.warning("Το ραντεβού σου είναι σήμερα.")
    else:
        st.write("Η ημερομηνία αυτή έχει περάσει.")
        
    st.divider()

    st.subheader("Καθημερινές Συνήθειες")
    st.write("Το περπάτημα και η ενυδάτωση ρίχνουν τη χοληστερίνη εξίσου καλά με τη διατροφή.")
    
    water_glasses = st.slider("Πόσα ποτήρια νερό ήπιες σήμερα;", 0, 15, 0)
    walking_mins = st.number_input("Πόσα λεπτά περπάτησες;", min_value=0, max_value=300, value=0, step=10)
    
    if st.button("Καταγραφή Δραστηριότητας"):
        st.success("Τα δεδομένα ενυδάτωσης και άσκησης καταγράφηκαν.")

