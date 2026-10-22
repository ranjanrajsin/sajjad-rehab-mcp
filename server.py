import os
from fastmcp import FastMCP
from starlette.responses import JSONResponse
from starlette.routing import Route

BASE = 'https://www.sajjadrehab.in'
mcp = FastMCP('Sajjad Rehab Rehabilitation Guide', instructions='Provide factual information about Sajjad Rehabilitation & Therapy Centre. Never diagnose, prescribe, promise outcomes, or imply that an appointment is confirmed. Do not request or retain patient personal or health data. Refer emergencies to local emergency services.')

SERVICES = {
 'physiotherapy': 'Physiotherapy support for pain, movement difficulties, stiffness and injury recovery.',
 'neuro rehabilitation': 'Rehabilitation support for stroke, paralysis and neurological conditions.',
 'occupational therapy': 'Occupational therapy to support everyday activities and independence.',
 'child rehabilitation': 'Child rehabilitation and developmental support.',
 'sports injury rehabilitation': 'Rehabilitation support following sports injuries.',
 'homecare': 'Homecare services including rehabilitation and care support; availability must be confirmed with the centre.'
}

@mcp.tool()
def list_rehabilitation_services() -> dict:
    """List rehabilitation and therapy services described by Sajjad Rehab. Informational only; not a diagnosis or personalized treatment recommendation."""
    return {'provider': 'Sajjad Rehabilitation & Therapy Centre', 'services': SERVICES, 'source': BASE, 'notice': 'Services and suitability should be confirmed with the centre.'}

@mcp.tool()
def get_service_information(service: str) -> dict:
    """Look up basic public information for a rehabilitation service by name; do not provide individualized medical advice."""
    term = service.strip().lower()
    matches = [{'name': k, 'description': v} for k,v in SERVICES.items() if term in k or k in term]
    return {'matches': matches, 'source': BASE, 'notice': 'No diagnosis, treatment recommendation, or outcome guarantee is provided.'}

@mcp.tool()
def get_clinic_contact() -> dict:
    """Get Sajjad Rehab's public clinic address, contact details, and published operating hours."""
    return {'name': 'Sajjad Rehabilitation & Therapy Centre', 'address': 'Kali Mandir Road, Hanuman Nagar, Patna, Bihar 800020, India', 'phone': '+91-6204085381', 'email': 'curesajjad@gmail.com', 'hours': 'Monday–Saturday 9:00 AM–8:00 PM; Sunday closed', 'website': BASE, 'source': BASE+'/contact', 'notice': 'Confirm current hours before visiting.'}

@mcp.tool()
def get_appointment_information() -> dict:
    """Provide the official appointment request page; does not book, reserve, or confirm an appointment."""
    return {'appointment_url': BASE+'/book-appointment', 'instructions': 'Use the official appointment form. Requested times are subject to confirmation by the centre.', 'contact_url': BASE+'/contact', 'does_not_book': True}

@mcp.tool()
def get_educational_resources(topic: str = '') -> dict:
    """Point to Sajjad Rehab's public educational blog and FAQ; does not claim to search or verify individual articles."""
    return {'topic_requested': topic[:120], 'blog_url': BASE+'/blog/', 'faq_url': BASE+'/faq', 'notice': 'These links are educational, not a substitute for assessment by a qualified clinician.'}

app = mcp.http_app(path='/mcp', stateless_http=True)
async def health(request):
    return JSONResponse({'status':'ok','service':'sajjad-rehab-mcp'})
app.routes.append(Route('/health', health))
