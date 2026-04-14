# AxiomCore Physical Audit Ledger (Incident 001)

## Node: Ottawa-POS-01 (L05B3TF9E0PJK)
**Audit Window:** 2026-04-11 to 2026-04-13
**Digital Variance:** $700.00

### Hardware Telemetry
- [ ] **Offline Sync Status:** [PENDING]
- [ ] **Tender Type Verification:** [PENDING]
- [ ] **Manual Drawer Count:** [PENDING]

### Logic Notes
If Cloud API returns $1.00 but Drawer Report shows $701.00, the error is a "Tender-Type Mismatch" at the human-interaction layer.
