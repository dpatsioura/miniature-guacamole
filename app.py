import streamlit as st
import datetime

st.set_page_config(page_title="Ο Φάκελος Υγείας Μου", page_icon="favicon144.png", layout="centered")

def clear_shopping_list():
    for key in st.session_state.keys():
        if key.startswith("shop_"):
            st.session_state[key] = False

st.image("favicon144.png", width=80)
st.title("Το Πρόγραμμα Μου")

diet_plan = {
    "Monday": {
        "Πρωινό": "Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 1 φλ. φακές/ρεβίθια/φασόλια μαγειρεμένα (ζουμί όσο θέλετε), 90γρ τυρί λευκό χαμηλών λιπαρών, 4 κγ ελαιόλαδο.",
        "Απογευματινό": "3 φρούτα, 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ (ακόμη και με γεύσεις).",
        "Βραδινό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 180γρ σνίτσελ κοτόπουλο φούρνου, 60γρ τυρί λευκό χαμηλών λιπαρών, 4 κγ ελαιόλαδο."
    },
    "Tuesday": {
        "Πρωινό": "Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 150γρ κοτόπουλο χωρίς δέρμα, 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες μεγέθους αυγού η κάθε μία, 30γρ τυρί λευκό χαμηλών λιπαρών, 4 κγ ελαιόλαδο.",
        "Απογευματινό": "3 φρούτα, 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ (ακόμη και με γεύσεις).",
        "Βραδινό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 150γρ κοτόπουλο χωρίς δέρμα, 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες μεγέθους αυγού η κάθε μία, 30γρ τυρί λευκό χαμηλών λιπαρών, 4 κγ ελαιόλαδο."
    },
    "Wednesday": {
        "Πρωινό": "Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 1,5 φλ. μακαρόνια μαγειρεμένα, 8 κομματάκια τυρί χαμηλών λιπαρών ή 1 μεγάλο κεσεδάκι κονσέρβα τόνο σε νερό, 4 κγ ελαιόλαδο.",
        "Απογευματινό": "3 φρούτα, 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ (ακόμη και με γεύσεις).",
        "Βραδινό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 1,5 φλ. μακαρόνια μαγειρεμένα, 8 κομματάκια τυρί χαμηλών λιπαρών ή 1 μεγάλο κεσεδάκι κονσέρβα τόνο σε νερό, 4 κγ ελαιόλαδο."
    },
    "Thursday": {
        "Πρωινό": "Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 150γρ κοτόπουλο χωρίς δέρμα, 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες μεγέθους αυγού η κάθε μία, 30γρ τυρί λευκό χαμηλών λιπαρών, 4 κγ ελαιόλαδο.",
        "Απογευματινό": "3 φρούτα, 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ (ακόμη και με γεύσεις).",
        "Βραδινό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 150γρ κοτόπουλο χωρίς δέρμα, 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες μεγέθους αυγού η κάθε μία, 30γρ τυρί λευκό χαμηλών λιπαρών, 4 κγ ελαιόλαδο."
    },
    "Friday": {
        "Πρωινό": "Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 1,5 φλ. φασολάκια ή αρακά μαγειρεμένο, 90γρ τυρί λευκό χαμηλών λιπαρών, 4 κγ ελαιόλαδο.",
        "Απογευματινό": "3 φρούτα, 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ (ακόμη και με γεύσεις).",
        "Βραδινό": "Ομελέτα: 4 αυγά (τον ένα κρόκο), 90γρ τυρί λευκό χαμηλών λιπαρών, 1 τμχ πιπεριά, 1 ντομάτα, 3 μανιτάρια μεγάλα, 1 κσ ελαιόλαδο."
    },
    "Saturday": {
        "Πρωινό": "Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 300γρ σαρδέλες/γαύρο φούρνου ή 330γρ τσιπούρα χωρίς δέρμα, 4 κγ ελαιόλαδο.",
        "Απογευματινό": "3 φρούτα, 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ (ακόμη και με γεύσεις).",
        "Βραδινό": "Τυλιχτό: 1 τορτίγια μετρίου μεγέθους, 3 φέτες κίτρινο τυρί χαμηλών λιπαρών, 4 κγ τυρί κρέμα light, 2 φλ. λαχανικά νωπά."
    },
    "Sunday": {
        "Πρωινό": "Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 150γρ κιμά σε μπιφτέκια (χοιρινό ή μοσχαρίσιο), 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες μεγέθους αυγού η κάθε μία, 4 κγ ελαιόλαδο.",
        "Απογευματινό": "3 φρούτα, 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ (ακόμη και με γεύσεις).",
        "Βραδινό": "2 φλ. λαχανικά σαλάτα νωπή-φρέσκια, 150γρ κιμά σε μπιφτέκια (χοιρινό ή μοσχαρίσιο), 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες μεγέθους αυγού η κάθε μία, 4 κγ ελαιόλαδο."
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
if "medications" not in st.session_state:
    st.session_state.medications = []
if "prescriptions" not in st.session_state:
    st.session_state.prescriptions = []

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Ημέρα", "Ψώνια", "Μετρήσεις", "Δραστηριότητα", "Φάρμακα & Συνταγές"])

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
        choice = st.radio(f"Κατάσταση για το {meal_time.lower()}:", ["Δεν καταγράφηκε", "Κατά γράμμα", "Εναλλακτική επιλογή", "Παρασπονδία"], key=f"radio_{status_key}")
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
    
    base_shopping_items = [
        "Λαχανικά για σαλάτα (νωπά/φρέσκα)", "Πιπεριές", "Ντομάτες", "Μανιτάρια", "Φρούτα", 
        "Στήθος κοτόπουλο / Σνίτσελ", "Κιμάς (χοιρινό ή μοσχάρι)", "Σαρδέλες / Γαύρος / Τσιπούρα",
        "Τόνος σε νερό", "Αυγά", "Τυρί λευκό χαμηλών λιπαρών", "Κίτρινο τυρί χαμηλών λιπαρών", 
        "Τυρί κρέμα light", "Γιαούρτι 2% ή Κεφίρ", "Φακές / Ρεβίθια", "Φασολάκια / Αρακάς", 
        "Ρύζι", "Μακαρόνια", "Πατάτες", "Τορτίγιες", "Ελαιόλαδο"
    ]
    all_shopping_items = base_shopping_items + st.session_state.custom_items
    
    for item in all_shopping_items:
        key_name = f"shop_{item}"
        if key_name not in st.session_state:
            st.session_state[key_name] = False
        st.checkbox(item, key=key_name)
        
    new_item = st.text_input("Πρόσθεσε νέο προϊόν στη λίστα:")
    if st.button("Προσθήκη στη λίστα"):
        if new_item and new_item not in all_shopping_items:
            st.session_state.custom_items.append(new_item)
            st.rerun()
    st.button("Καθαρισμός τικ (για νέα αγορά)", on_click=clear_shopping_list)

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
    water = st.slider("Ποτήρια νερό", 0, 15, 0)
    walking = st.number_input("Λεπτά περπάτημα", 0, 500, 0, step=10)
    if st.button("Καταγραφή Δραστηριότητας"):
        st.success("Τα δεδομένα αποθηκεύτηκαν.")
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

with tab5:
    st.subheader("Φαρμακευτική Αγωγή")
    med_name = st.text_input("Όνομα Φαρμάκου:")
    med_dose = st.text_input("Δοσολογία (π.χ. 1 χάπι το βράδυ):")
    if st.button("Προσθήκη Φαρμάκου"):
        if med_name and med_dose:
            st.session_state.medications.append({"name": med_name, "dose": med_dose})
            st.success("Το φάρμακο προστέθηκε.")
    
    if st.session_state.medications:
        st.write("Η τρέχουσα αγωγή σου:")
        for m in st.session_state.medications:
            st.write(f"- {m['name']}: {m['dose']}")
            
    st.divider()
    st.subheader("Πλάνο Συνταγών (6 μήνες)")
    presc_name = st.text_input("Για ποιο φάρμακο είναι η συνταγή;")
    start_presc = st.date_input("Ημερομηνία πρώτης εκτέλεσης συνταγής:", datetime.date.today())
    
    if st.button("Δημιουργία Πλάνου Συνταγών"):
        if presc_name:
            new_plan = []
            for i in range(6):
                next_date = start_presc + datetime.timedelta(days=i*30)
                new_plan.append(next_date)
            st.session_state.prescriptions.append({"name": presc_name, "dates": new_plan})
            st.success("Το εξάμηνο πλάνο δημιουργήθηκε.")

    if st.session_state.prescriptions:
        today = datetime.date.today()
        for p in st.session_state.prescriptions:
            st.write(f"### Συνταγές για: {p['name']}")
            for d in p['dates']:
                diff = (d - today).days
                if 0 <= diff <= 5:
                    st.warning(f"ΠΡΟΣΟΧΗ: Εκτέλεση συνταγής στις {d.strftime('%d/%m/%Y')} (σε {diff} μέρες)")
                else:
                    st.write(f"- Ημερομηνία: {d.strftime('%d/%m/%Y')}")
