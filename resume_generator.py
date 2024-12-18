import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (Paragraph, SimpleDocTemplate, Spacer, 
                                HRFlowable, Image, Table, TableStyle)
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# --------------------------------------
# CONFIGURATION & DATA
# --------------------------------------
#
# Define colors, fonts, and general parameters for the resume.
# Adjust these as needed for your own branding or preferences.
#

# Define the path to the 'assets' directory for fonts and images
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

# Register custom fonts Roboto and Poppins
pdfmetrics.registerFont(TTFont('Roboto', os.path.join(ASSETS_DIR, 'Roboto-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Roboto-Bold', os.path.join(ASSETS_DIR, 'Roboto-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Poppins', os.path.join(ASSETS_DIR, 'Poppins-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Poppins-Bold', os.path.join(ASSETS_DIR, 'Poppins-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Roboto-Italic', os.path.join(ASSETS_DIR, 'Roboto-Italic.ttf')))


#First Font Option
NAME_FONT = "Poppins-Bold"
CONTACT_FONT = "Roboto"
SECTION_TITLE_FONT = "Poppins-Bold"
SUBHEADING_FONT = "Poppins-Bold"
NORMAL_TEXT_FONT = "Roboto"
MYITALIC_FONT = "Roboto-Italic"
BOLD_FONT = "Roboto-Bold"
BULLET_ITEM_FONT = "Roboto"
LINKSTYLE_FONT = "Roboto"


#Second Font Option - Remove the comments to use
# NAME_FONT = "Helvetica-Bold"
# CONTACT_FONT = "Helvetica"
# SECTION_TITLE_FONT = "Helvetica-Bold"
# SUBHEADING_FONT = "Helvetica-Bold"
# NORMAL_TEXT_FONT = "Helvetica"
# MYITALIC_FONT = "Helvetica-Oblique"
# BOLD_FONT = "Helvetica-Bold"
# BULLET_ITEM_FONT = "Helvetica"
# LINKSTYLE_FONT = "Helvetica"


HIGHLIGHT_COLOR = colors.HexColor('#9C7A2C')  # Gold/brown highlight color
TEXT_COLOR = colors.black

# Example resume data.
# In a real scenario, this data could be loaded from JSON, YAML, or a database.
RESUME_DATA = {
    "name": "John Doe",
    "contact": "Email: lorem.ipsum@example.com ❖ Phone: (+00) 12345-6789 ❖ Location: Somewhere, Earth",
    "github_url": "https://github.com/lorem-ipsum",
    "linkedin_url": "https://www.linkedin.com/in/lorem-ipsum-12345",
    "education": [
        {
            "institution": "Lorem Ipsum University",
            "degree": "Bachelor's in Applied Sciences",
            "date": "Jan. 2010 - Dec. 2014",
            "description": (
                "Completed a thesis on the optimization of systems using advanced algorithms and AI models. "
                "Published papers demonstrating innovative solutions for data analysis and system improvements."
            )
        },
        {
            "institution": "Dolor Sit Amet Institute",
            "degree": "Master's in Computer Engineering",
            "date": "Jan. 2015 - Dec. 2017",
            "description": (
                "Specialized in embedded systems and automation. Developed projects integrating hardware and software solutions "
                "for efficient process management and technological advancements."
            )
        },
        {
            "institution": "Consectetur Academy",
            "degree": "Full-Stack Web Development Certification",
            "date": "Jan. 2023 - Dec. 2023",
            "description": (
                "Focused on web technologies including Node.js, React, and Vue.js. Built scalable applications with modern front-end "
                "frameworks and RESTful APIs, ensuring performance and usability."
            )
        }
    ],
    "experience": [
        {
            "company": "Tech Solutions Ltd.",
            "role": "Software Developer",
            "period": "Jan. 2018 – Dec. 2020\nTech City, World",
            "details": [
                "Implemented automation scripts to reduce manual workload by 40%, improving team efficiency.",
                "Developed and maintained client applications using Python and JavaScript frameworks.",
                "Collaborated with cross-functional teams to integrate new features and troubleshoot issues."
            ]
        },
        {
            "company": "InnovateX Research Lab",
            "role": "Research Assistant",
            "period": "Jan. 2021 – Dec. 2022\nInnovation Hub, Techland",
            "details": [
                "Conducted research on machine learning models for predictive analysis.",
                "Designed and simulated real-world solutions using MATLAB and Simulink.",
                "Published reports detailing findings and implementation strategies for automated systems."
            ]
        }
    ],
    "projects_volunteering": [
        {
            "year": "2019",
            "description": "Led a community project creating IoT-based devices to monitor air quality."
        },
        {
            "year": "2021",
            "description": "Participated in an open-source project enhancing accessibility tools for visually impaired individuals."
        }
    ],
    "certifications": "AWS Certified Solutions Architect; Python Programmer Professional",
    "skills": (
        "Proficiency in Python, JavaScript, React, Node.js; Experience with Docker and Kubernetes; "
        "Strong understanding of Agile methodologies; Familiarity with CI/CD pipelines and cloud technologies."
    ),
    "interests": "Open-source contributions; AI in healthcare; Mountain biking; Playing guitar."
}


# --------------------------------------
# STYLE CREATION
# --------------------------------------
#
# Define paragraph styles for various elements: headings, normal text,
# italics, bullet points, and more. These styles ensure consistency
# across the entire resume.
#

def create_styles():
    styles = getSampleStyleSheet()

    # Remove potentially conflicting styles if running multiple times.
    for s in ['Name', 'Contact', 'SectionTitle', 'SubHeading', 'NormalText', 'MyItalic', 'Bold', 'BulletItem', 'LinkStyle']:
        if s in styles.byName:
            del styles.byName[s]

        # Name style: prominent, highlighted
    styles.add(ParagraphStyle(
        name='Name',
        parent=styles['Heading1'],
        fontName=NAME_FONT,
        fontSize=16,
        leading=18,
        alignment=TA_LEFT,
        spaceAfter=4,
        textColor=HIGHLIGHT_COLOR
    ))

    # Contact style: small font, justifying if needed
    styles.add(ParagraphStyle(
        name='Contact',
        parent=styles['Normal'],
        fontName=CONTACT_FONT,
        fontSize=7,
        leading=9,
        textColor=TEXT_COLOR,
        alignment=TA_JUSTIFY,
        spaceAfter=0
    ))

    # LinkStyle: for clickable URLs (GitHub/LinkedIn)
    styles.add(ParagraphStyle(
        name='LinkStyle',
        parent=styles['Contact'],
        fontName=LINKSTYLE_FONT,
        fontSize=7,
        leading=8,
        textColor=colors.blue,
        alignment=TA_LEFT,
        spaceAfter=0
    ))

    # SectionTitle: for headings like EDUCATION, EXPERIENCE, etc.
    styles.add(ParagraphStyle(
        name='SectionTitle',
        parent=styles['Heading2'],
        fontName=SECTION_TITLE_FONT,
        fontSize=11,
        spaceBefore=6,
        spaceAfter=3,
        leading=12,
        textColor=HIGHLIGHT_COLOR,
        alignment=TA_LEFT
    ))

    # SubHeading: for institution/company names or roles
    styles.add(ParagraphStyle(
        name='SubHeading',
        parent=styles['Normal'],
        fontName=SUBHEADING_FONT,
        fontSize=9,
        spaceAfter=1,
        textColor=TEXT_COLOR,
        alignment=TA_LEFT
    ))

    # NormalText: main body text
    styles.add(ParagraphStyle(
        name='NormalText',
        parent=styles['Normal'],
        fontName=NORMAL_TEXT_FONT,
        fontSize=9,
        leading=11,
        spaceAfter=3,
        textColor=TEXT_COLOR,
        alignment=TA_JUSTIFY
    ))

    # MyItalic: italic style, often for roles or dates
    styles.add(ParagraphStyle(
        name='MyItalic',
        parent=styles['Normal'],
        fontName=MYITALIC_FONT,
        fontSize=9,
        leading=11,
        spaceAfter=2,
        textColor=TEXT_COLOR,
        alignment=TA_LEFT
    ))

    # Bold: for bold text highlights within paragraphs
    styles.add(ParagraphStyle(
        name='Bold',
        parent=styles['Normal'],
        fontName=BOLD_FONT,
        fontSize=9,
        textColor=TEXT_COLOR,
        alignment=TA_JUSTIFY
    ))

    # BulletItem: for listing responsibilities or achievements
    styles.add(ParagraphStyle(
        name='BulletItem',
        parent=styles['Normal'],
        fontName=BULLET_ITEM_FONT,
        fontSize=9,
        leading=11,
        spaceAfter=2,
        leftIndent=10,
        textColor=TEXT_COLOR,
        alignment=TA_JUSTIFY
    ))
    
    return styles

# --------------------------------------
# SECTION RENDERING FUNCTIONS
# --------------------------------------
#
# Each function below handles a specific section of the resume.
# They add styled paragraphs, tables, and separators (HRFlowable)
# to the story. You can add, remove, or modify these sections as needed.
#

def add_header(story, styles, data):
    """Add the header section with the candidate's name, contact information,
    and clickable GitHub/LinkedIn URLs in a single line below the contact info."""
    # Candidate name
    story.append(Paragraph(data["name"], styles['Name']))
    # Contact info
    story.append(Paragraph(data["contact"], styles['Contact']))

    # Icons and URLs for GitHub and LinkedIn
    github_icon = Image(os.path.join(ASSETS_DIR, "github.png"), width=5*mm, height=5*mm)
    linkedin_icon = Image(os.path.join(ASSETS_DIR, "linkedin.png"), width=5*mm, height=5*mm)

    github_link = Paragraph(f'<link href="{data["github_url"]}">{data["github_url"]}</link>', styles['LinkStyle'])
    linkedin_link = Paragraph(f'<link href="{data["linkedin_url"]}">{data["linkedin_url"]}</link>', styles['LinkStyle'])

    # Table for icons and links, all in one row, aligned left
    link_table = Table(
        [[github_icon, github_link, linkedin_icon, linkedin_link]],
        colWidths=[6*mm, None, 6*mm, None]
    )

    # Minimal padding to keep icons and text close
    link_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))

    story.append(link_table)
    # Add horizontal line after the header
    story.append(HRFlowable(width="100%", thickness=1.5, color=HIGHLIGHT_COLOR, spaceBefore=6, spaceAfter=6))


def add_education_section(story, styles, education_list):
    """Add the EDUCATION section, listing institutions, degrees, dates, and descriptions."""
    story.append(Paragraph("EDUCATION", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=HIGHLIGHT_COLOR, spaceBefore=1, spaceAfter=4))
    for edu in education_list:
        story.append(Paragraph(edu['institution'], styles['SubHeading']))
        if edu.get('degree'):
            story.append(Paragraph(edu['degree'], styles['MyItalic']))
        if edu.get('date'):
            story.append(Paragraph(edu['date'], styles['MyItalic']))
        if edu.get('description'):
            story.append(Paragraph(edu['description'], styles['NormalText']))

def add_experience_section(story, styles, experience_list):
    """Add the PROFESSIONAL EXPERIENCE section, listing roles and responsibilities."""
    story.append(Spacer(1, 6))
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=HIGHLIGHT_COLOR, spaceBefore=1, spaceAfter=4))

    for exp in experience_list:
        story.append(Paragraph(exp['company'], styles['SubHeading']))
        story.append(Paragraph(exp['role'], styles['MyItalic']))
        story.append(Paragraph(exp['period'], styles['MyItalic']))
        for detail in exp['details']:
            story.append(Paragraph("• " + detail, styles['BulletItem']))

def add_projects_volunteering_section(story, styles, projects_list):
    """Add the ADDITIONAL PROJECTS & VOLUNTEERING section."""
    if not projects_list:
        return
    story.append(Spacer(1, 6))
    story.append(Paragraph("ADDITIONAL PROJECTS & VOLUNTEERING", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=HIGHLIGHT_COLOR, spaceBefore=1, spaceAfter=4))
    for proj in projects_list:
        year_label = proj.get('year') or proj.get('year_range', '')
        prefix = f"<b>{year_label}:</b> " if year_label else ""
        story.append(Paragraph(prefix + proj['description'], styles['NormalText']))

def add_certifications_skills_interests_section(story, styles, certifications, skills, interests):
    """Add the CERTIFICATIONS, SKILLS & INTERESTS section."""
    story.append(Spacer(1, 6))
    story.append(Paragraph("CERTIFICATIONS, SKILLS & INTERESTS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=HIGHLIGHT_COLOR, spaceBefore=1, spaceAfter=4))
    story.append(Paragraph("<b>Certifications:</b> " + certifications, styles['NormalText']))
    story.append(Paragraph("<b>Skills:</b> " + skills, styles['NormalText']))
    story.append(Paragraph("<b>Interests:</b> " + interests, styles['NormalText']))

# --------------------------------------
# MAIN BUILD LOGIC
# --------------------------------------
#
# The build_resume function assembles all sections into a single PDF.
# You can choose which sections to include or exclude here.
#

def build_resume(data, output_filename):
    """Build the PDF resume from the given data dictionary."""
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        rightMargin=10*mm,
        leftMargin=10*mm,
        topMargin=10*mm,
        bottomMargin=10*mm
    )

    styles = create_styles()
    story = []

    # Header section
    add_header(story, styles, data)

    # Additional sections
    add_education_section(story, styles, data.get("education", []))
    add_experience_section(story, styles, data.get("experience", []))
    add_projects_volunteering_section(story, styles, data.get("projects_volunteering", []))
    add_certifications_skills_interests_section(
        story,
        styles,
        data.get("certifications", ""),
        data.get("skills", ""),
        data.get("interests", "")
    )

    # Build the final PDF
    doc.build(story)
    print(f"PDF file '{output_filename}' created successfully!")

# --------------------------------------
# EXECUTION
# --------------------------------------
#
# Running this script directly will generate the resume PDF from RESUME_DATA.
# Adjust RESUME_DATA and styles to your liking, then run:
# python your_script.py
#

if __name__ == "__main__":
    build_resume(RESUME_DATA, "resume.pdf")
