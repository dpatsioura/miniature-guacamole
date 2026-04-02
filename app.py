import streamlit as st
import datetime

st.set_page_config(page_title="Ο Φάκελος Υγείας Μου", page_icon="favicon144.png", layout="centered")

def clear_shopping_list():
    for key in st.session_state.keys():
        if key.startswith("shop_"):
            st.session_state[key] = False

st.image("favicon144.png", width=80)
st.title("Το Πρόγραμμα Μου")

# Τα γεύματα πλέον είναι ανεξάρτητα μενού
diet_plan = {
    "Μενού 1 (Φακές & Σνίτσελ)": {
        "Πρωινό": "* Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 1 φλ. φακές/ρεβίθια/φασόλια μαγειρεμένα\n* 90γρ τυρί λευκό χαμηλών λιπαρών\n* 4 κγ ελαιόλαδο",
        "Απογευματινό": "* 3 φρούτα\n* 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ",
        "Βραδινό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 180γρ σνίτσελ κοτόπουλο φούρνου\n* 60γρ τυρί λευκό χαμηλών λιπαρών\n* 4 κγ ελαιόλαδο"
    },
    "Μενού 2 (Κοτόπουλο 1)": {
        "Πρωινό": "* Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 150γρ κοτόπουλο χωρίς δέρμα\n* 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες\n* 30γρ τυρί λευκό χαμηλών λιπαρών\n* 4 κγ ελαιόλαδο",
        "Απογευματινό": "* 3 φρούτα\n* 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ",
        "Βραδινό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 150γρ κοτόπουλο χωρίς δέρμα\n* 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες\n* 30γρ τυρί λευκό χαμηλών λιπαρών\n* 4 κγ ελαιόλαδο"
    },
    "Μενού 3 (Μακαρόνια & Τόνος)": {
        "Πρωινό": "* Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 1,5 φλ. μακαρόνια μαγειρεμένα\n* 8 κομματάκια τυρί χαμηλών λιπαρών ή 1 μεγάλο κεσεδάκι κονσέρβα τόνο σε νερό\n* 4 κγ ελαιόλαδο",
        "Απογευματινό": "* 3 φρούτα\n* 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ",
        "Βραδινό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 1,5 φλ. μακαρόνια μαγειρεμένα\n* 8 κομματάκια τυρί χαμηλών λιπαρών ή 1 μεγάλο κεσεδάκι κονσέρβα τόνο σε νερό\n* 4 κγ ελαιόλαδο"
    },
    "Μενού 4 (Κοτόπουλο 2)": {
        "Πρωινό": "* Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 150γρ κοτόπουλο χωρίς δέρμα\n* 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες\n* 30γρ τυρί λευκό χαμηλών λιπαρών\n* 4 κγ ελαιόλαδο",
        "Απογευματινό": "* 3 φρούτα\n* 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ",
        "Βραδινό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 150γρ κοτόπουλο χωρίς δέρμα\n* 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες\n* 30γρ τυρί λευκό χαμηλών λιπαρών\n* 4 κγ ελαιόλαδο"
    },
    "Μενού 5 (Φασολάκια & Ομελέτα)": {
        "Πρωινό": "* Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 1,5 φλ. φασολάκια ή αρακά μαγειρεμένο\n* 90γρ τυρί λευκό χαμηλών λιπαρών\n* 4 κγ ελαιόλαδο",
        "Απογευματινό": "* 3 φρούτα\n* 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ",
        "Βραδινό": "Ομελέτα:\n* 4 αυγά (τον ένα κρόκο)\n* 90γρ τυρί λευκό χαμηλών λιπαρών\n* 1 τμχ πιπεριά\n* 1 ντομάτα\n* 3 μανιτάρια μεγάλα\n* 1 κσ ελαιόλαδο"
    },
    "Μενού 6 (Ψάρι & Τυλιχτό)": {
        "Πρωινό": "* Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 300γρ σαρδέλες/γαύρο φούρνου ή 330γρ τσιπούρα χωρίς δέρμα\n* 4 κγ ελαιόλαδο",
        "Απογευματινό": "* 3 φρούτα\n* 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ",
        "Βραδινό": "Τυλιχτό:\n* 1 τορτίγια μετρίου μεγέθους\n* 3 φέτες κίτρινο τυρί χαμηλών λιπαρών\n* 4 κγ τυρί κρέμα light\n* 2 φλ. λαχανικά νωπά"
    },
    "Μενού 7 (Μπιφτέκια)": {
        "Πρωινό": "* Σταθερό πρωινό (σύμφωνα με τις γενικές οδηγίες)",
        "Μεσημεριανό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 150γρ κιμά σε μπιφτέκια (χοιρινό ή μοσχαρίσιο)\n* 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες\n* 4 κγ ελαιόλαδο",
        "Απογευματινό": "* 3 φρούτα\n* 1 κεσεδάκι γιαούρτι 2% ή 1 φλ. κεφίρ",
        "Βραδινό": "* 2 φλ. λαχανικά σαλάτα νωπή-φρέσκια\n* 150γρ κιμά σε μπιφτέκια (χοιρινό ή μοσχαρίσιο)\n* 1 φλ. ρύζι μαγειρεμένο ή 3 μικρές πατάτες\n* 4 κγ ελαιόλαδο"
    }
}

if "menu_assignments" not in st.session_state:
    st.session_state.menu_assignments = {}
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

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Ημέρα", "Εβδομάδα & Ψώνια", "Μετρήσεις", "Δραστηριότητα", "Φάρμακα & Συνταγές"])

with tab1:
    selected_date = st.date_input("Επίλεξε ημερομηνία:", datetime.date.today())
    date_str = str(selected_date)
    
    # Βρίσκουμε τις ημέρες της εβδομάδας για να κρύψουμε τα μενού που ήδη έκανες
    start_of_week = selected_date - datetime.timedelta(days=selected_date.weekday())
    week_dates_str = [str(start_of_week + datetime.timedelta(days=i)) for i in range(7)]
    
    used_menus = [st.session_state.menu_assignments[d] for d in week_dates_str if d in st.session_state.menu_assignments and d != date_str]
    all_menus = list(diet_plan.keys())
    available_menus = [m for m in all_menus if m not in used_menus]
    
    current_menu = st.session_state.menu_assignments.get(date_str, "Κανένα μενού")
    
    options = ["Κανένα μενού"] + available_menus
    if current_menu in options:
        default_idx = options.index(current_menu)
    elif current_menu != "Κανένα μενού":
        options = ["Κανένα μενού", current_menu] + available_menus
        default_idx = 1
    else:
        default_idx = 0
        
    selected_menu = st.selectbox("Επίλεξε τι θα φας αυτή τη μέρα:", options, index=default_idx)
    
    if selected_menu != "Κανένα μενού":
        st.session_state.menu_assignments[date_str] = selected_menu
        st.subheader(f"Πρόγραμμα: {selected_menu}")
        
        for meal_time, meal_desc in diet_plan[selected_menu].items():
            st.write(f"### {meal_time}")
            st.write(meal_desc)
            status_key = f"status_{date_str}_{meal_time}"
            if status_key not in st.session_state.meal_status:
                st.session_state.meal_status[status_key] = "Δεν καταγράφηκε"
            choice = st.radio(f"Κατάσταση για το {meal_time.lower()}:", ["Δεν καταγράφηκε", "Κατά γράμμα", "Εναλλακτική επιλογή", "Παρασπονδία"], key=f"radio_{status_key}")
            st.session_state.meal_status[status_key] = choice
            details_key = f"details_{date_str}_{meal_time}"
            if choice in ["Εναλλακτική επιλογή", "Παρασπονδία"]:
                label = "Τι έφαγες ακριβώς;" if choice == "Παρασπονδία" else "Ποια εναλλακτική διάλεξες;"
                current_val = st.session_state.meal_details.get(details_key, "")
                detail_input = st.text_input(label, value=current_val, key=f"input_{details_key}")
                st.session_state.meal_details[details_key] = detail_input
            st.divider()
            
        st.subheader("Σημειώσεις και Διάθεση")
        mood_key = f"mood_{date_str}"
        current_mood = st.session_state.daily_mood.get(mood_key, "")
        new_mood = st.text_area("Πώς ένιωσες σήμερα; Πώς πήγε η διατροφή γενικά;", value=current_mood, key=f"area_{mood_key}")
        if st.button("Αποθήκευση Σημειώσεων", key=f"btn_mood_{mood_key}"):
            st.session_state.daily_mood[mood_key] = new_mood
            st.success("Οι πληροφορίες της ημέρας καταγράφηκαν.")
    else:
        if date_str in st.session_state.menu_assignments:
            del st.session_state.menu_assignments[date_str]
        st.info("Επίλεξε ένα μενού από τη λίστα για να δεις τα γεύματα. Τα μενού που έχεις ήδη κάνει αυτή την εβδομάδα αποκρύπτονται.")

with tab2:
    st.subheader("Πρόγραμμα Τρέχουσας Εβδομάδας")
    days_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]
    view_date = datetime.date.today()
    week_start = view_date - datetime.timedelta(days=view_date.weekday())
    
    for i in range(7):
        curr_d = week_start + datetime.timedelta(days=i)
        curr_d_str = str(curr_d)
        d_name = days_gr[i]
        assigned = st.session_state.menu_assignments.get(curr_d_str, "Κενό")
        
        with st.expander(f"{d_name} ({curr_d.strftime('%d/%m')}) : {assigned}"):
            if assigned != "Κενό":
                for meal_time, meal_desc in diet_plan[assigned].items():
                    st.write(f"{meal_time}:\n{meal_desc}")
            else:
                st.write("Δεν έχεις ορίσει μενού για αυτή τη μέρα.")
                
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
    med_dose = st.text_input("Δοσολογία π.χ. 1 χάπι το βράδυ:")
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
