import streamlit as st
import datetime

st.set_page_config(page_title="Ο Φάκελος Υγείας Μου", layout="centered")

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

tab1, tab2, tab3, tab4 = st.tabs(["Ημέρα", "Ψώνια", "Μετρήσεις", "Δραστηριότητα & Ραντεβού"])

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

    st.subheader("Σημειώσεις και Διάθεση")
    mood_key = f"mood_{selected_date}"
    current_mood = st.session_state.daily_mood.get(mood_key, "")
    new_mood = st.text_area("Πώς ένιωσες σήμερα; Πώς πήγε η διατροφή γενικά;", value=current_mood, key=f"area_{mood_key}")
    
    if st.button("Αποθήκευση Σημειώσεων", key=f"btn_mood_{mood_key}"):
        st.session_state.daily_mood[mood_key] = new_mood
        st.success("Οι πληροφορίες της ημέρας καταγράφηκαν.")

with tab2:
    st.subheader("Σύνοψη Εβδομάδας")
    for eng_day, gr_day in days_map.items():
        with st.expander(f"Πρόγραμμα για {gr_day}"):
            for meal_time, meal_desc in diet_plan[eng_day].items():
                st.write(f"{meal_time}: {meal_desc}")
                
    st.divider()
    
    st.subheader("Λίστα για Ψώνια")
    st.write("Τσέκαρε όσα χρειάζεται να αγοράσεις:")
    
    base_shopping_items = [
        "Γάλα αμυγδάλου", "Βρώμη", "Στήθος κοτόπουλο", "Φρέσκια σαλάτα", 
        "Λαχανικά", "Μήλα", "Πορτοκάλια", "Αυγά", "Φρυγανιές ολικής", 
        "Μέλι", "Ψάρι", "Χόρτα", "Αμύγδαλα", "Καρύδια", 
        "Γιαούρτι χαμηλών λιπαρών", "Φακές", "Μακαρόνια ολικής", 
        "Σάλτσα ντομάτας", "Κοτόπουλο ολόκληρο", "Πατάτες"
    ]
    
    all_shopping_items = base_shopping_items + st.session_state.custom_items
    
    for item in all_shopping_items:
        key_name = f"shop_{item}"
        if key_name not in st.session_state:
            st.session_state[key_name] = False
        
        is_checked = st.checkbox(item, value=st.session_state[key_name], key=key_name)
        st.session_state[key_name] = is_checked

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
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Βάρος σε κιλά", min_value=40.0, max_value=150.0, value=80.0, step=0.1)
        systolic = st.number_input("Συστολική Πίεση", 80, 200, 120)
    with col2:
        diastolic = st.number_input("Διαστολική Πίεση", 40, 130, 80)
        cholesterol = st.number_input("Ολική Χοληστερίνη", 100, 500, 240)

    if st.button("Αποθήκευση Μετρήσεων"):
        st.success("Οι μετρήσεις αποθηκεύτηκαν.")

    st.divider()
    st.subheader("Αρχείο Εξετάσεων")
    uploaded_file = st.file_uploader("Φόρτωσε τις εξετάσεις σου εδώ", type=["pdf", "png", "jpg"])
    if uploaded_file:
        st.success("Το αρχείο ανέβηκε.")

with tab4:
    st.subheader("Γυμναστήριο και Άσκηση")
    workout_type = st.selectbox("Τι είδους προπόνηση έκανες;", ["Καμία", "Βάρη", "Cardio", "Yoga", "Crossfit", "Άλλο"])
    if workout_type != "Καμία":
        muscle_group = st.text_input("Τι γύμνασες σήμερα; παράδειγμα Πόδια, Στήθος")
        gym_time = st.number_input("Διάρκεια προπόνησης σε λεπτά", 0, 300, 60, step=5)
    
    st.write("")
    water = st.slider("Ποτήρια νερό", 0, 15, 0)
    walking = st.number_input("Λεπτά περπάτημα", 0, 500, 0, step=10)
    
    if st.button("Καταγραφή Δραστηριότητας"):
        st.success("Όλα τα δεδομένα άσκησης και ενυδάτωσης αποθηκεύτηκαν.")
    
    st.divider()
    st.subheader("Επόμενο Ραντεβού")
    appointment = st.date_input("Ημερομηνία επανεξέτασης:", datetime.date.today() + datetime.timedelta(days=60))
    days_to_go = (appointment - datetime.date.today()).days
    
    if days_to_go > 0:
        st.info(f"Σε {days_to_go} ημέρες θα ελέγξουμε ξανά την πρόοδό σου.")
    elif days_to_go == 0:
        st.warning("Το ραντεβού στον γιατρό είναι σήμερα.")
    else:
        st.write("Η ημερομηνία του ραντεβού έχει περάσει.")
