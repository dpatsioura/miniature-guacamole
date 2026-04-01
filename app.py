import streamlit as st

# Ρυθμίσεις σελίδας
st.set_page_config(page_title="Η Διατροφή Μου")

st.title("Εβδομαδιαίο Πρόγραμμα")

# Το πλάνο του γιατρού
diet_plan = {
    "Δευτέρα": {
        "Πρωινό": "Βρώμη με γάλα αμυγδάλου",
        "Μεσημεριανό": "Στήθος κοτόπουλο με σαλάτα",
        "Απογευματινό": "1 μήλο",
        "Βραδινό": "Σαλάτα με 1 αυγό βραστό"
    },
    "Τρίτη": {
        "Πρωινό": "2 φρυγανιές ολικής με μέλι",
        "Μεσημεριανό": "Ψάρι ψητό με χόρτα",
        "Απογευματινό": "Λίγα αμύγδαλα",
        "Βραδινό": "Γιαούρτι με χαμηλά λιπαρά"
    }
    # Συμπληρώνουμε εδώ τις υπόλοιπες μέρες
}

# Επιλογή ημέρας
days = list(diet_plan.keys())
selected_day = st.selectbox("Επίλεξε ημέρα:", days)

st.subheader(f"Γεύματα για {selected_day}")

# Αποθήκευση της προόδου ώστε να μην χάνονται τα κλικ
if "checked_meals" not in st.session_state:
    st.session_state.checked_meals = {}

# Εμφάνιση γευμάτων με κουτάκια επιλογής
for meal_time, meal_desc in diet_plan[selected_day].items():
    key = f"{selected_day}_{meal_time}"
    
    if key not in st.session_state.checked_meals:
        st.session_state.checked_meals[key] = False
    
    checked = st.checkbox(f"{meal_time}: {meal_desc}", value=st.session_state.checked_meals[key])
    st.session_state.checked_meals[key] = checked

# Μπάρα προόδου ημέρας
total_meals_today = len(diet_plan[selected_day])
completed_meals_today = sum(1 for time in diet_plan[selected_day].keys() if st.session_state.checked_meals.get(f"{selected_day}_{time}", False))

st.write("")
st.write(f"Πρόοδος ημέρας: {completed_meals_today} από {total_meals_today} γεύματα")

if total_meals_today > 0:
    st.progress(completed_meals_today / total_meals_today)
else:
    st.progress(0)
