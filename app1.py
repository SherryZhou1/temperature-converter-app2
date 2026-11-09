
# ==========================================
# TEMPERATURE CONVERTER WEB APP
# Built with Python and Streamlit
# ==========================================

# SECTION 1: Import Streamlit
# Streamlit helps us create the web interface.
import streamlit as st


# SECTION 2: Configure the web page
# This controls the browser tab title and layout.
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)


# SECTION 3: Add the application title
st.title("🌡️ Temperature Converter")

st.write(
    "Convert temperatures between Celsius and Fahrenheit easily."
)

st.divider()


# SECTION 4: Get temperature input from the user
# Users can enter positive or negative numbers.
temperature = st.number_input(
    "Enter temperature:",
    value=25.0,
    step=1.0,
    format="%.2f"
)


# SECTION 5: Let the user select conversion type
conversion_type = st.selectbox(
    "Select conversion type:",
    [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius"
    ]
)


# SECTION 6: Perform the temperature conversion
if conversion_type == "Celsius to Fahrenheit":

    # Formula: F = (C × 9/5) + 32
    converted_temperature = (temperature * 9 / 5) + 32

    formula = "°F = (°C × 9/5) + 32"

    result_unit = "°F"

else:

    # Formula: C = (F - 32) × 5/9
    converted_temperature = (temperature - 32) * 5 / 9

    formula = "°C = (°F - 32) × 5/9"

    result_unit = "°C"


# SECTION 7: Display the conversion result
st.divider()

st.subheader("Conversion Result")

st.success(
    f"{temperature:.2f} converted to "
    f"{converted_temperature:.2f} {result_unit}"
)


# SECTION 8: Display the formula used
st.subheader("Formula Used")

st.info(formula)


# SECTION 9: Add a simple footer
st.divider()

st.caption("Built with Python and Streamlit 🚀")

