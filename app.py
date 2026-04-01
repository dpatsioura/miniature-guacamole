import streamlit as st
import datetime

st.set_page_config(page_title="Η Διατροφή Μου", layout="centered")

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
if "missing_items" not in st.session_state:
    st.session_state.missing_items = {}
if "custom_items" not in st.session_state:
    st.session_state.custom_items = []

tab1, tab2 = st.tabs(["Ημερήσια Καταγραφή", "Εβδομαδιαίο Πλάνο & Ψώνια"])

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
        "Γάλα αμυγδάλου", "Βρώμη", "Στήθος κοτόπουλο", "Φρέσκια σαλάτα / Λαχανικά",
        "Μήλα", "Πορτοκάλια", "Αυγά", "Φρυγανιές ολικής", "Μέλι", "Ψάρι", 
        "Χόρτα", "Αμύγδαλα / Καρύδια", "Γιαούρτι χαμηλών λιπαρών", "Φακές", 
        "Μακαρόνια ολικής", "Σάλτσα ντομάτας", "Κοτόπουλο ολόκληρο", "Πατάτες"
    ]
    
    all_shopping_items = base_shopping_items + st.session_state.custom_items
    
    for item in all_shopping_items:
        if item not in st.session_state.missing_items:
            st.session_state.missing_items[item] = False
            
        is_missing = st.checkbox(item, value=st.session_state.missing_items[item], key=f"shop_{item}")
        st.session_state.missing_items[item] = is_missing

    st.write("")
    new_item = st.text_input("Πρόσθεσε νέο προϊόν στη λίστα:")
    if st.button("Προσθήκη στη λίστα"):
        if new_item and new_item not in all_shopping_items:
            st.session_state.custom_items.append(new_item)
            st.session_state.missing_items[new_item] = False
            st.rerun()

    st.write("")
    if st.button("Καθαρισμός τικ (για νέα αγορά)"):
        for item in all_shopping_items:
            st.session_state.missing_items[item] = False
        st.rerun()
