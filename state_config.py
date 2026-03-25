"""
State configuration for this LouisianaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "LA"
STATE_NAME = "Louisiana"
APP_NAME = "LouisianaDischargeWatch"
APP_TAGLINE = "Louisiana Discharge Monitoring"
DOMAIN = "louisianadischargewatch.org"
DATA_FILE = "la_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@louisianadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 6
