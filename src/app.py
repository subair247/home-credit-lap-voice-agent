import streamlit as st
from src.agent.system_prompt import get_system_prompt
from src.services.validation import validate_eligibility

st.set_page_config(page_title="Home Credit LAP Voice Agent Dashboard", layout="wide")

st.title("📞 Home Credit LAP Voice Agent - Testing Dashboard")
st.markdown("Test the conversational state, checklist extraction, and validation rules locally.")

st.sidebar.header("Agent Configurations")
customer_name = st.sidebar.text_input("Customer Name", value="Rahul Sharma")
agent_name = st.sidebar.text_input("Agent Name", value="Sharukh")
agent_gender = st.sidebar.selectbox("Agent Gender", ["Female", "Male"])
language = st.sidebar.selectbox("Language", ["English", "Hindi"])

st.subheader("Internal Qualification State Simulator")
col1, col2 = st.columns(2)

with col1:
    prop_type = st.selectbox("Property Type", [None, "Residential", "Commercial", "Industrial", "Agricultural"])
    ownership = st.selectbox("Ownership Status", [None, "Sole", "Joint"])
    docs = st.selectbox("Original Documents Available?", [None, True, False])
    loan_amt = st.number_input("Desired Loan Amount (₹)", value=5000000, step=100000)

with col2:
    occupation = st.selectbox("Occupation", [None, "Salaried", "Self-Employed"])
    income_mode = st.selectbox("Income Mode", [None, "Bank", "Cash"])
    market_val = st.number_input("Estimated Market Value (₹)", value=10000000, step=500000)
    tenure = st.slider("Tenure (Years)", 1, 20, 10)
    
    existing_loan = st.checkbox("Existing Property Loan / EMI Reduction Intent")

current_state = {
    "property_type": prop_type,
    "ownership_status": ownership,
    "documents_available": docs,
    "loan_amount": loan_amt,
    "occupation": occupation,
    "income_mode": income_mode,
    "market_value": market_val,
    "tenure": tenure,
    "existing_property_loan": existing_loan
}

if st.button("Evaluate Agent Status & Validation"):
    result = validate_eligibility(current_state)
    st.markdown("---")
    st.subheader("Evaluation Results")
    st.json(result)

st.markdown("---")
st.subheader("Generated System Prompt Preview")
with st.expander("View Full System Prompt"):
    prompt_text = get_system_prompt(
        customer_name=customer_name,
        agent_name=agent_name,
        agent_gender=agent_gender,
        language_to_speak=language
    )
    st.text_area("System Prompt", prompt_text, height=300)