import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Get the GROQ API key from the environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")


prompt_template = """
    Input Symptoms: {input}
    ------------------
    Based on the given input symptoms, classify the department related to the symptoms in which the patient should enquire. Given below is the list of departments:
    - Cardiology: Heart and blood vessel conditions
    - Oncology: Cancer treatment
    - Neurology: Nervous system disorders
    - Gynecology: Female reproductive health
    - Obstetrics: Pregnancy and childbirth
    - Orthopedics: Bones, joints, and muscles
    - Pediatrics: Children's health
    - Gastroenterology: Digestive system disorders
    - Dermatology: Skin conditions
    - Endocrinology: Hormonal disorders
    - Nephrology: Kidney health
    - Pulmonology: Lung and respiratory conditions
    - Hematology: Blood disorders
    - Rheumatology: Autoimmune and musculoskeletal diseases
    - Urology: Urinary tract and male reproductive organs
    - Ophthalmology: Eye conditions
    - Otolaryngology (ENT): Ear, nose, and throat disorders
    - Psychiatry: Mental health
    - Emergency Medicine: Acute care for urgent conditions
    - General Surgery: Various surgical procedures
    - Plastic Surgery: Reconstructive and cosmetic surgery
    - Radiology: Imaging and diagnostics
    - Pathology: Laboratory analysis of tissue samples
    - Anesthesiology: Pain management and anesthesia during surgery
    - Palliative Care: Supportive care for serious illnesses
    - Infectious Diseases: Management of infections and contagious diseases
    - Rehabilitation: Physical and occupational therapy
    - Allergy and Immunology: Allergic and immune system disorders
    - General Physician: Primary care for various general health concerns
    ------------------

    If unable to identify any department based on the symptoms, suggest "General Physician" as the department.

    Based on the above department list, choose only one department and return in JSON format:
    {{"department": "department name"}}

    Return JSON structure only,
    JSON OUTPUT:
    """



# prompt_template = """
#     Input Symptoms:{input}
#     ------------------
#     based on the given above input symptoms classify the department related to the symptoms in which the patient should enquire. Given below is the list of departments:
#     Cardiology: Heart and blood vessel conditions
#     Oncology: Cancer treatment
#     Neurology: Nervous system disorders
#     Gynecology: Female reproductive health
#     Obstetrics: Pregnancy and childbirth
#     Orthopedics: Bones, joints, and muscles
#     Pediatrics: Children's health
#     Gastroenterology: Digestive system disorders
#     Dermatology: Skin conditions
#     Endocrinology: Hormonal disorders
#     Nephrology: Kidney health
#     Pulmonology: Lung and respiratory conditions
#     Hematology: Blood disorders
#     Rheumatology: Autoimmune and musculoskeletal diseases
#     Urology: Urinary tract and male reproductive organs
#     Ophthalmology: Eye conditions
#     Otolaryngology (ENT): Ear, nose, and throat disorders
#     Psychiatry: Mental health
#     Emergency Medicine: Acute care for urgent conditions
#     General Surgery: Various surgical procedures
#     Plastic Surgery: Reconstructive and cosmetic surgery
#     Radiology: Imaging and diagnostics
#     Pathology: Laboratory analysis of tissue samples
#     Anesthesiology: Pain management and anesthesia during surgery
#     Palliative Care: Supportive care for serious illnesses
#     Infectious Diseases: Management of infections and contagious diseases
#     Rehabilitation: Physical and occupational therapy
#     Allergy and Immunology: Allergic and immune system disorders
#     ------------------

#     Based on the above department list choose only one department and return in json format
#     {{"department": "department name"}}

#     return json structure only,
#     JSON OUTPUT:
#     """