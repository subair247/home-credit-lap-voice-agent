def validate_eligibility(state: dict) -> dict:
    """
    Validates the current state against Home Credit LAP rules.
    Returns status: 'ELIGIBLE', 'DISQUALIFIED', 'TRANSFER_REQUIRED', or 'IN_PROGRESS'
    """
    
    if state.get("existing_property_loan") == True or state.get("emi_reduction_request") == True:
        return {"status": "TRANSFER_REQUIRED", "reason": "Existing loan or EMI reduction requested. Handing over to transfer specialist."}

    if state.get("property_type") and state.get("property_type").lower() == "agricultural":
        return {"status": "DISQUALIFIED", "reason": "Agricultural properties are not eligible for this LAP offer."}

    if state.get("income_mode") and state.get("income_mode").lower() == "cash":
        return {"status": "DISQUALIFIED", "reason": "Cash income mode is not eligible. Income must be received via Bank."}

    if state.get("documents_available") == False:
        return {"status": "DISQUALIFIED", "reason": "Original property documents must be available for verification."}

    tenure = state.get("tenure")
    if tenure is not None:
        if tenure < 3 or tenure > 15:
            return {"status": "DISQUALIFIED", "reason": "Repayment tenure must be between 3 and 15 years."}

    loan_amount = state.get("loan_amount")
    if loan_amount is not None and loan_amount > 7500000:
        return {"status": "LIMIT_EXCEEDED", "reason": "Requested amount exceeds ₹75 Lakhs limit. Must offer maximum ₹75 Lakhs."}

    mandatory_fields = [
        "property_type",
        "ownership_status",
        "documents_available",
        "loan_amount",
        "occupation",
        "income_mode",
        "market_value",
        "tenure"
    ]
    
    for field in mandatory_fields:
        if state.get(field) is None:
            return {"status": "IN_PROGRESS", "next_missing": field}

    return {"status": "ELIGIBLE", "reason": "All 7 eligibility criteria met successfully. Ready for senior loan expert handoff."}