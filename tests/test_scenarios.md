# Home Credit LAP Voice Agent - Test Scenarios

1. **Perfect Eligible Customer:** Residential, Sole owner, Original docs available, 50 Lakhs, Salaried, Bank income, 10-year tenure -> **Result: QUALIFIED (Handoff to Expert)**
2. **Agricultural Property:** Property type is Agricultural -> **Result: IMMEDIATE DISQUALIFICATION**
3. **Cash Income:** Self-employed with Cash income -> **Result: IMMEDIATE DISQUALIFICATION**
4. **Missing Original Docs:** Photocopies only -> **Result: IMMEDIATE DISQUALIFICATION**
5. **Tenure Too Short:** Tenure = 2 years -> **Result: DISQUALIFIED (< 3 years)**
6. **Tenure Too Long:** Tenure = 18 years -> **Result: DISQUALIFIED (> 15 years)**
7. **Loan Amount > 75 Lakhs:** Requested 90 Lakhs -> **Result: Explain 75L limit, offer max 75L alternative**
8. **Joint Ownership:** Joint property with spouse -> **Result: ELIGIBLE (Continue flow)**
9. **Existing Property Loan:** Customer wants to reduce EMI -> **Result: Transfer specialist flow & End**
10. **Out-of-Order Answers:** Customer gives residential property, joint ownership, and market value in first sentence -> **Result: State updated, skip asked questions, ask earliest missing question**
11. **Busy Customer:** Customer says "I am in a meeting" -> **Result: Ask preferred callback time & End**
12. **Diversion Handling:** Customer asks for exact interest rates -> **Result: State expert will provide rates post-qualification, return to checklist**