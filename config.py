import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
from langchain_community.chat_models import BedrockChat
import boto3

# load_dotenv()

# Get the GROQ API key from the environment variables
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")

# Initialize the Bedrock client
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-west-2'  # replace with your preferred region
)

llm = BedrockChat(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        client=bedrock_client,
        model_kwargs={
            "temperature": 0,
            "max_tokens": 4096
        }
    )


prompt_template = """
    Input Symptoms: {input}
    ------------------
    Based on the given input symptoms, classify the department related to the symptoms in which the patient should enquire. Given below is the list of departments:
    - General Physician: Primary care for various general health concerns. Simple symptoms like headache, fever, pain, injury, cough, dizziness, etc.
    - Cardiology: Heart and blood vessel conditions
    - Oncology: Cancer treatment
    - Neurology: Nervous system disorders
    - Gynecology: Female reproductive health
    - Obstetrics: Pregnancy and childbirth
    - Orthopedics: Bones, joints, and bone muscles
    - Pediatrics: Children's health
    - Gastroenterology: Digestive system disorders
    - Dermatology: Skin conditions
    - Endocrinology: Hormonal disorders
    - Nephrology: Kidney health
    - Pulmonology: Lung and respiratory conditions
    - Hematology: Blood disorders
    - Rheumatology: Autoimmune and musculoskeletal diseases, inflammation in the muscles and internal organs
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
    ------------------

    Give priority to "General Physician" for one/ two symptoms.
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