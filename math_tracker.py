from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import Color, white, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta
import calendar
import os

class MathProgressTracker:
    def __init__(self):
        # Define your color scheme
        self.purple = Color(0.463, 0.294, 0.635)  # #764ba2
        self.blue = Color(0.4, 0.494, 0.918)     # #667eea
        self.light_purple = Color(0.463, 0.294, 0.635, alpha=0.2)
        self.light_blue = Color(0.4, 0.494, 0.918, alpha=0.2)
        self.dark_gray = Color(0.2, 0.2, 0.2)
        self.light_gray = Color(0.9, 0.9, 0.9)
        
    def create_custom_styles(self):
        """Create custom paragraph styles"""
        styles = getSampleStyleSheet()
        
        # Title style
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=20,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=self.purple,
            fontName='Helvetica-Bold'
        )
        
        # Section header style
        section_style = ParagraphStyle(
            'SectionHeader',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=10,
            spaceBefore=15,
            textColor=self.blue,
            fontName='Helvetica-Bold'
        )
        
        # Small header style
        small_header_style = ParagraphStyle(
            'SmallHeader',
            parent=styles['Heading3'],
            fontSize=12,
            spaceAfter=8,
            spaceBefore=10,
            textColor=self.purple,
            fontName='Helvetica-Bold'
        )
        
        # Body text style
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=6,
            textColor=self.dark_gray,
            fontName='Helvetica'
        )
        
        # Small text style
        small_style = ParagraphStyle(
            'SmallText',
            parent=styles['Normal'],
            fontSize=8,
            spaceAfter=4,
            textColor=self.dark_gray,
            fontName='Helvetica'
        )
        
        return {
            'title': title_style,
            'section': section_style,
            'small_header': small_header_style,
            'body': body_style,
            'small': small_style
        }
    
    def create_monthly_progress_table(self):
        """Create a comprehensive monthly progress tracking table"""
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        
        # Create table data
        headers = ["Month", "Week 1", "Week 2", "Week 3", "Week 4", "Goals Met", "Notes"]
        data = [headers]
        
        for month in months:
            row = [month, "□", "□", "□", "□", "___/___", ""]
            data.append(row)
        
        # Create table
        table = Table(data, colWidths=[1*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.8*inch, 1.8*inch])
        
        # Style the table
        table.setStyle(TableStyle([
            # Header row styling
            ('BACKGROUND', (0, 0), (-1, 0), self.purple),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            
            # Data rows styling
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 1, self.dark_gray),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, self.light_gray]),
            
            # Month column styling
            ('ALIGN', (0, 1), (0, -1), 'LEFT'),
            ('LEFTPADDING', (0, 1), (0, -1), 8),
            
            # Notes column styling
            ('ALIGN', (-1, 1), (-1, -1), 'LEFT'),
            ('LEFTPADDING', (-1, 1), (-1, -1), 4),
        ]))
        
        return table
    
    def create_skills_mastery_table(self):
        """Create skills mastery tracking table"""
        skills_by_grade = {
            "Elementary Skills": [
                "Number Recognition (1-100)",
                "Counting & Skip Counting",
                "Addition Facts (0-12)",
                "Subtraction Facts (0-12)",
                "Place Value (Ones, Tens, Hundreds)",
                "Basic Fractions (1/2, 1/4, 1/3)",
                "Telling Time",
                "Money Recognition & Counting",
                "Basic Shapes & Patterns",
                "Simple Measurement"
            ],
            "Intermediate Skills": [
                "Multiplication Facts (0-12)",
                "Division Facts (0-12)",
                "Multi-digit Addition/Subtraction",
                "Fraction Operations",
                "Decimal Basics",
                "Geometry (Area, Perimeter)",
                "Data & Graphing",
                "Word Problem Strategies",
                "Mental Math Strategies",
                "Estimation Skills"
            ],
            "Advanced Skills": [
                "Multi-digit Multiplication/Division",
                "Advanced Fractions & Decimals",
                "Percentage Calculations",
                "Algebraic Thinking",
                "Advanced Geometry",
                "Statistics & Probability",
                "Problem-Solving Strategies",
                "Mathematical Reasoning",
                "Pre-Algebra Concepts",
                "Mathematical Communication"
            ]
        }
        
        tables = []
        
        for grade_level, skills in skills_by_grade.items():
            # Create header
            header_data = [[grade_level, "Not Started", "Developing", "Proficient", "Mastered", "Date Mastered"]]
            
            # Create skill rows
            skill_data = []
            for skill in skills:
                row = [skill, "□", "□", "□", "□", "___/___"]
                skill_data.append(row)
            
            # Combine data
            table_data = header_data + skill_data
            
            # Create table
            table = Table(table_data, colWidths=[2.5*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch])
            
            # Style the table
            table.setStyle(TableStyle([
                # Header styling
                ('BACKGROUND', (0, 0), (-1, 0), self.blue),
                ('TEXTCOLOR', (0, 0), (-1, 0), white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                
                # Data rows styling
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, self.dark_gray),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, self.light_gray]),
                
                # Skill column styling
                ('ALIGN', (0, 1), (0, -1), 'LEFT'),
                ('LEFTPADDING', (0, 1), (0, -1), 6),
                
                # Checkbox columns styling
                ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
            ]))
            
            tables.append(table)
        
        return tables
    
    def create_goal_setting_table(self):
        """Create quarterly goal setting table"""
        quarters = ["Quarter 1 (Sep-Nov)", "Quarter 2 (Dec-Feb)", "Quarter 3 (Mar-May)", "Quarter 4 (Jun-Aug)"]
        
        data = [["Quarter", "Math Goals", "Target Skills", "Resources Needed", "Progress Notes"]]
        
        for quarter in quarters:
            row = [quarter, "", "", "", ""]
            data.append(row)
        
        table = Table(data, colWidths=[1.2*inch, 1.8*inch, 1.5*inch, 1.2*inch, 1.8*inch])
        
        table.setStyle(TableStyle([
            # Header styling
            ('BACKGROUND', (0, 0), (-1, 0), self.purple),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            
            # Data rows styling
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, self.dark_gray),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, self.light_gray]),
            ('ALIGN', (0, 1), (0, -1), 'LEFT'),
            ('LEFTPADDING', (0, 1), (-1, -1), 6),
            ('TOPPADDING', (0, 1), (-1, -1), 20),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 20),
        ]))
        
        return table
    
    def create_weekly_reflection_template(self):
        """Create weekly reflection template"""
        weeks = [f"Week {i}" for i in range(1, 37)]  # 36 weeks for school year
        
        # Create data in chunks for better page layout
        chunk_size = 12
        tables = []
        
        for i in range(0, len(weeks), chunk_size):
            week_chunk = weeks[i:i+chunk_size]
            
            data = [["Week", "Topics Covered", "Strengths", "Challenges", "Next Week Focus"]]
            
            for week in week_chunk:
                row = [week, "", "", "", ""]
                data.append(row)
            
            table = Table(data, colWidths=[0.6*inch, 1.8*inch, 1.4*inch, 1.4*inch, 1.3*inch])
            
            table.setStyle(TableStyle([
                # Header styling
                ('BACKGROUND', (0, 0), (-1, 0), self.blue),
                ('TEXTCOLOR', (0, 0), (-1, 0), white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 8),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                
                # Data rows styling
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 7),
                ('GRID', (0, 0), (-1, -1), 1, self.dark_gray),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, self.light_gray]),
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                ('LEFTPADDING', (0, 1), (-1, -1), 4),
                ('TOPPADDING', (0, 1), (-1, -1), 15),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 15),
            ]))
            
            tables.append(table)
        
        return tables
    
    def create_pdf(self, filename="math_progress_tracker.pdf"):
        """Generate the comprehensive PDF tracker"""
        doc = SimpleDocTemplate(filename, pagesize=letter,
                              rightMargin=36, leftMargin=36,
                              topMargin=36, bottomMargin=36)
        
        styles = self.create_custom_styles()
        story = []
        
        # Cover Page
        story.append(Spacer(1, 1*inch))
        story.append(Paragraph("Homeschool Math Progress Tracker", styles['title']))
        story.append(Spacer(1, 0.5*inch))
        
        # Student info section
        student_info = """
        <b>Student Name:</b> _________________________________<br/><br/>
        <b>Grade Level:</b> ___________________________________<br/><br/>
        <b>School Year:</b> ___________________________________<br/><br/>
        <b>Parent/Teacher:</b> ________________________________<br/><br/>
        <b>Start Date:</b> ____________________________________
        """
        story.append(Paragraph(student_info, styles['body']))
        story.append(Spacer(1, 1*inch))
        
        # Instructions
        instructions = """
        <b>How to Use This Tracker:</b><br/>
        • Print all pages and keep in a binder for easy reference<br/>
        • Use checkmarks, stickers, or colored pens to mark progress<br/>
        • Review weekly and monthly
        • Celebrate achievements and identify areas needing extra attention<br/>
        • Use the reflection pages to plan future lessons<br/>
        • Share progress with your child to build confidence and motivation
        """
        story.append(Paragraph(instructions, styles['body']))
        story.append(PageBreak())
        
        # Monthly Progress Overview
        story.append(Paragraph("Monthly Progress Overview", styles['section']))
        story.append(Paragraph("Track weekly completion and overall monthly goals", styles['body']))
        story.append(Spacer(1, 10))
        story.append(self.create_monthly_progress_table())
        story.append(Spacer(1, 20))
        
        # Legend
        legend = """
        <b>Legend:</b> ✓ = Week completed successfully | ◐ = Partial completion | ✗ = Needs review<br/>
        <b>Goals Met:</b> Write fraction (e.g., 3/4 means 3 out of 4 weekly goals achieved)
        """
        story.append(Paragraph(legend, styles['small']))
        story.append(PageBreak())
        
        # Quarterly Goal Setting
        story.append(Paragraph("Quarterly Goal Setting", styles['section']))
        story.append(Paragraph("Set specific, measurable goals for each quarter", styles['body']))
        story.append(Spacer(1, 10))
        story.append(self.create_goal_setting_table())
        story.append(Spacer(1, 20))
        
        # Goal setting tips
        goal_tips = """
        <b>SMART Goals Tips:</b><br/>
        • <b>Specific:</b> "Master multiplication tables 1-12" vs "Get better at math"<br/>
        • <b>Measurable:</b> Include numbers, percentages, or clear benchmarks<br/>
        • <b>Achievable:</b> Set challenging but realistic expectations<br/>
        • <b>Relevant:</b> Align with your child's grade level and needs<br/>
        • <b>Time-bound:</b> Set clear deadlines within the quarter
        """
        story.append(Paragraph(goal_tips, styles['body']))
        story.append(PageBreak())
        
        # Skills Mastery Tracking
        story.append(Paragraph("Skills Mastery Tracking", styles['section']))
        story.append(Paragraph("Monitor progress through key mathematical concepts by grade level", styles['body']))
        story.append(Spacer(1, 15))
        
        # Add all skills tables
        skills_tables = self.create_skills_mastery_table()
        for i, table in enumerate(skills_tables):
            story.append(table)
            if i < len(skills_tables) - 1:  # Don't add page break after last table
                story.append(Spacer(1, 20))
                if i == 0:  # Add page break after first table
                    story.append(PageBreak())
        
        story.append(Spacer(1, 15))
        
        # Skills tracking tips
        skills_tips = """
        <b>Skills Assessment Guide:</b><br/>
        • <b>Not Started:</b> Concept hasn't been introduced yet<br/>
        • <b>Developing:</b> Learning the concept, needs support and practice<br/>
        • <b>Proficient:</b> Can complete tasks with minimal help<br/>
        • <b>Mastered:</b> Demonstrates understanding independently and can teach others
        """
        story.append(Paragraph(skills_tips, styles['body']))
        story.append(PageBreak())
        
        # Weekly Reflection Pages
        story.append(Paragraph("Weekly Reflection & Planning", styles['section']))
        story.append(Paragraph("Document weekly progress and plan ahead", styles['body']))
        story.append(Spacer(1, 10))
        
        # Add weekly reflection tables
        weekly_tables = self.create_weekly_reflection_template()
        for i, table in enumerate(weekly_tables):
            story.append(table)
            story.append(Spacer(1, 15))
            if (i + 1) % 2 == 0:  # Page break every 2 tables
                story.append(PageBreak())
        
        # Assessment Record Page
        story.append(PageBreak())
        story.append(Paragraph("Assessment & Testing Record", styles['section']))
        story.append(Spacer(1, 10))
        
        # Create assessment table
        assessment_data = [
            ["Date", "Assessment Type", "Topic/Skill", "Score/Grade", "Strengths", "Areas to Review"]
        ]
        
        # Add 20 empty rows for assessments
        for _ in range(20):
            assessment_data.append(["", "", "", "", "", ""])
        
        assessment_table = Table(assessment_data, colWidths=[0.8*inch, 1.2*inch, 1.3*inch, 0.8*inch, 1.4*inch, 1.4*inch])
        
        assessment_table.setStyle(TableStyle([
            # Header styling
            ('BACKGROUND', (0, 0), (-1, 0), self.purple),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            
            # Data rows styling
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, self.dark_gray),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, self.light_gray]),
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
            ('LEFTPADDING', (0, 1), (-1, -1), 4),
            ('TOPPADDING', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ]))
        
        story.append(assessment_table)
        story.append(PageBreak())
        
        # Resources and Notes Page
        story.append(Paragraph("Resources & Notes", styles['section']))
        story.append(Spacer(1, 10))
        
        resources_content = """
        <b>Curriculum Resources Used:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Helpful Websites & Apps:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Manipulatives & Materials:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Areas of Strength:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Ongoing Challenges:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Parent/Teacher Notes:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        """
        
        story.append(Paragraph(resources_content, styles['body']))
        story.append(PageBreak())
        
        # Year-End Summary Page
        story.append(Paragraph("Year-End Summary & Reflection", styles['section']))
        story.append(Spacer(1, 10))
        
        summary_content = """
        <b>Biggest Achievements This Year:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Most Challenging Topics:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Favorite Math Activities:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Skills to Continue Working On:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Goals for Next Year:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>What Worked Well:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>What to Change Next Year:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Overall Grade/Progress:</b> ________________________________<br/><br/>
        <b>Parent Signature:</b> _________________________ <b>Date:</b> _____________
        """
        
        story.append(Paragraph(summary_content, styles['body']))
        
        # Build the PDF
        doc.build(story)
        print(f"PDF created successfully: {filename}")
        return filename

def main():
    """Main function to generate the progress tracker PDF"""
    tracker = MathProgressTracker()
    filename = tracker.create_pdf()
    
    # Check if file was created successfully
    if os.path.exists(filename):
        file_size = os.path.getsize(filename)
        print(f"\n✅ Success! Your Math Progress Tracker has been created as '{filename}'")
        print(f"📄 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        print("\n📋 Your tracker includes:")
        print("   • Monthly progress overview with weekly tracking")
        print("   • Quarterly goal setting templates")
        print("   • Comprehensive skills mastery checklists (Elementary, Intermediate, Advanced)")
        print("   • 36 weeks of reflection and planning pages")
        print("   • Assessment and testing record pages")
        print("   • Resources and notes sections")
        print("   • Year-end summary and reflection page")
        print("   • Professional formatting with your purple/blue color scheme")
        print("\n💡 Tips:")
        print("   • Print double-sided to save paper")
        print("   • Use a 3-ring binder for easy organization")
        print("   • Consider laminating frequently used pages")
        print("   • Make copies of blank pages for future use")
    else:
        print("❌ Error: PDF file was not created successfully")

if __name__ == "__main__":
    main()
