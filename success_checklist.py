"""
Enhanced Math Success Checklist
===============================

Comprehensive grade-by-grade math milestones for homeschool students.
Uses purple/blue color scheme and generates professional PDF reports.
"""

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

class EnhancedMathSuccessChecklist:
    def __init__(self):
        # Define your color scheme (keeping original colors)
        self.purple = Color(0.463, 0.294, 0.635)  # #764ba2
        self.blue = Color(0.4, 0.494, 0.918)     # #667eea
        self.light_purple = Color(0.463, 0.294, 0.635, alpha=0.2)
        self.light_blue = Color(0.4, 0.494, 0.918, alpha=0.2)
        self.dark_gray = Color(0.2, 0.2, 0.2)
        self.light_gray = Color(0.9, 0.9, 0.9)
    
    def get_enhanced_grade_data(self):
        """Comprehensive math skills by grade with detailed breakdowns"""
        return {
            "Pre-K (Ages 3-4)": {
                "skills": [
                    "Count objects 1-10",
                    "Recognize numbers 1-5",
                    "Sort objects by size, color, shape",
                    "Basic shape recognition (circle, square, triangle)",
                    "Simple patterns (AB, ABC)",
                    "More/less comparison with objects",
                    "One-to-one correspondence",
                    "Basic spatial concepts (in/out, up/down)"
                ],
                "activities": [
                    "Counting songs and finger plays",
                    "Shape sorting games",
                    "Pattern blocks activities",
                    "Number books and stories"
                ],
                "assessments": [
                    "Can count 5 objects accurately",
                    "Identifies basic shapes in environment",
                    "Creates simple AB patterns"
                ]
            },
            "Kindergarten (Ages 5-6)": {
                "skills": [
                    "Count to 100 by ones and tens",
                    "Write numbers 0-20",
                    "Basic addition/subtraction with objects (within 10)",
                    "Identify and describe 2D and 3D shapes",
                    "Compare numbers using greater/less than",
                    "Understand addition as putting together",
                    "Understand subtraction as taking apart",
                    "Classify objects and count by categories"
                ],
                "activities": [
                    "Number line activities",
                    "Manipulative-based math (blocks, counters)",
                    "Shape scavenger hunts",
                    "Measurement with non-standard units"
                ],
                "assessments": [
                    "Counts to 100 without assistance",
                    "Solves addition/subtraction problems within 10",
                    "Writes numbers 0-20 legibly"
                ]
            },
            "1st Grade (Ages 6-7)": {
                "skills": [
                    "Add and subtract within 20 fluently",
                    "Understand place value (tens and ones)",
                    "Tell and write time to hour and half-hour",
                    "Measure lengths with non-standard units",
                    "Organize and interpret data with graphs",
                    "Partition circles and rectangles into halves/fourths",
                    "Count by 2s, 5s, and 10s",
                    "Word problem strategies for addition/subtraction"
                ],
                "activities": [
                    "Base-10 blocks for place value",
                    "Clock practice with daily routines",
                    "Measurement stations with rulers",
                    "Graphing family data (pets, favorite foods)"
                ],
                "assessments": [
                    "Addition/subtraction facts within 20 in 3 minutes",
                    "Tells time to nearest half-hour",
                    "Explains place value of 2-digit numbers"
                ]
            },
            "2nd Grade (Ages 7-8)": {
                "skills": [
                    "Add and subtract within 100 using strategies",
                    "Understand place value to hundreds",
                    "Measure and estimate lengths in standard units",
                    "Work with time and money",
                    "Represent and interpret data",
                    "Recognize and draw shapes with attributes",
                    "Partition rectangles into equal parts",
                    "Skip counting patterns and odd/even numbers"
                ],
                "activities": [
                    "Money counting games and store play",
                    "Measurement comparison activities",
                    "Data collection projects",
                    "Geometric shape building"
                ],
                "assessments": [
                    "Solves 2-digit addition/subtraction within 5 minutes",
                    "Counts money combinations up to $1.00",
                    "Measures objects to nearest inch/centimeter"
                ]
            },
            "3rd Grade (Ages 8-9)": {
                "skills": [
                    "Multiply and divide within 100 fluently",
                    "Understand fractions as numbers on number line",
                    "Solve word problems using all four operations",
                    "Find area and perimeter of rectangles",
                    "Tell time to nearest minute",
                    "Measure mass and volume",
                    "Understand properties of multiplication",
                    "Round numbers to nearest 10 or 100"
                ],
                "activities": [
                    "Multiplication arrays and skip counting",
                    "Fraction circles and bars",
                    "Area and perimeter with grid paper",
                    "Multi-step word problem solving"
                ],
                "assessments": [
                    "Multiplication facts 0-12 in 5 minutes",
                    "Identifies equivalent fractions with models",
                    "Solves multi-step word problems independently"
                ]
            },
            "4th Grade (Ages 9-10)": {
                "skills": [
                    "Multi-digit multiplication and division",
                    "Generate equivalent fractions",
                    "Add and subtract fractions with like denominators",
                    "Understand decimal notation for fractions",
                    "Convert measurements within single systems",
                    "Classify geometric figures by properties",
                    "Analyze and create patterns",
                    "Solve multi-step word problems with remainders"
                ],
                "activities": [
                    "Long multiplication and division algorithms",
                    "Fraction equivalence with manipulatives",
                    "Decimal place value activities",
                    "Geometry classification charts"
                ],
                "assessments": [
                    "Multiplies 4-digit by 1-digit numbers accurately",
                    "Adds/subtracts fractions with like denominators",
                    "Converts between fractions and decimals"
                ]
            },
            "5th Grade (Ages 10-11)": {
                "skills": [
                    "Add, subtract, multiply, and divide fractions",
                    "Understand volume as attribute of 3D figures",
                    "Graph points on coordinate plane",
                    "Perform operations with decimals to hundredths",
                    "Convert measurements within and between systems",
                    "Classify 2D figures in hierarchy",
                    "Analyze numerical patterns and relationships",
                    "Apply order of operations"
                ],
                "activities": [
                    "Fraction operations with visual models",
                    "Volume experiments with unit cubes",
                    "Coordinate graphing activities",
                    "Decimal computation practice"
                ],
                "assessments": [
                    "Solves fraction word problems accurately",
                    "Calculates volume of rectangular prisms",
                    "Graphs coordinate pairs correctly"
                ]
            },
            "6th Grade (Ages 11-12)": {
                "skills": [
                    "Understand ratios and rates",
                    "Solve unit rate problems",
                    "Understand and use percent",
                    "Work with positive and negative integers",
                    "Write and evaluate algebraic expressions",
                    "Solve one-variable equations and inequalities",
                    "Find area of triangles and quadrilaterals",
                    "Display and analyze statistical data"
                ],
                "activities": [
                    "Ratio and proportion real-world problems",
                    "Integer operations with number lines",
                    "Algebraic expression modeling",
                    "Statistical data collection projects"
                ],
                "assessments": [
                    "Solves ratio and rate problems",
                    "Evaluates algebraic expressions",
                    "Analyzes statistical displays"
                ]
            },
            "7th Grade (Ages 12-13)": {
                "skills": [
                    "Add, subtract, multiply, and divide rational numbers",
                    "Solve multi-step real-life mathematical problems",
                    "Use properties of operations for equivalent expressions",
                    "Solve real-life problems using linear equations",
                    "Draw geometric shapes with given conditions",
                    "Describe relationships between angles",
                    "Solve problems involving scale drawings",
                    "Use random sampling to draw inferences"
                ],
                "activities": [
                    "Rational number operations practice",
                    "Multi-step equation solving",
                    "Geometric construction activities",
                    "Statistical inference projects"
                ],
                "assessments": [
                    "Operates with rational numbers fluently",
                    "Solves linear equations in one variable",
                    "Constructs geometric figures accurately"
                ]
            },
            "8th Grade (Ages 13-14)": {
                "skills": [
                    "Work with radicals and integer exponents",
                    "Understand and apply linear functions",
                    "Analyze and solve systems of linear equations",
                    "Understand congruence and similarity",
                    "Apply Pythagorean Theorem",
                    "Solve problems involving volume of cylinders, cones, spheres",
                    "Investigate patterns of association in bivariate data",
                    "Understand and apply scientific notation"
                ],
                "activities": [
                    "Exponent rules exploration",
                    "Linear function graphing",
                    "Pythagorean Theorem applications",
                    "Volume calculations with real objects"
                ],
                "assessments": [
                    "Graphs linear functions accurately",
                    "Applies Pythagorean Theorem to solve problems",
                    "Uses scientific notation appropriately"
                ]
            }
        }
    
    def print_enhanced_checklist(self):
        """Print enhanced console version with colors"""
        print("\n\033[1;35m🧮 Enhanced Homeschool Math Success Checklist 🧮\033[0m")
        print("\033[34m" + "="*60 + "\033[0m\n")
        
        grade_data = self.get_enhanced_grade_data()
        
        for grade, content in grade_data.items():
            print(f"\033[1;34m📚 {grade}\033[0m")
            print(f"\033[35m{'─' * (len(grade) + 4)}\033[0m")
            
            print(f"\033[1;33m  ✨ Core Skills:\033[0m")
            for skill in content["skills"]:
                print(f"    □ {skill}")
            
            print(f"\n\033[1;33m  🎯 Recommended Activities:\033[0m")
            for activity in content["activities"]:
                print(f"    • {activity}")
            
            print(f"\n\033[1;33m  📋 Assessment Milestones:\033[0m")
            for assessment in content["assessments"]:
                print(f"    ✓ {assessment}")
            
            print("\n" + "\033[36m" + "─" * 60 + "\033[0m\n")
    
    def create_custom_styles(self):
        """Create custom paragraph styles for PDF"""
        styles = getSampleStyleSheet()
        
        # Title style
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=self.purple,
            fontName='Helvetica-Bold'
        )
        
        # Grade header style
        grade_style = ParagraphStyle(
            'GradeHeader',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=10,
            spaceBefore=15,
            textColor=self.blue,
            fontName='Helvetica-Bold'
        )
        
        # Section header style
        section_style = ParagraphStyle(
            'SectionHeader',
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
            'grade': grade_style,
            'section': section_style,
            'body': body_style,
            'small': small_style
        }
    
    def create_progress_tracking_table(self, grade, skills):
        """Create a progress tracking table for each grade"""
        # Create table data
        headers = ["Skill", "Not Started", "Learning", "Practicing", "Mastered", "Date Achieved"]
        data = [headers]
        
        for skill in skills:
            row = [skill, "□", "□", "□", "□", "___/___/___"]
            data.append(row)
        
        # Create table
        table = Table(data, colWidths=[3*inch, 0.7*inch, 0.7*inch, 0.7*inch, 0.7*inch, 0.9*inch])
        
        # Style the table
        table.setStyle(TableStyle([
            # Header row styling
            ('BACKGROUND', (0, 0), (-1, 0), self.purple),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            
            # Data rows styling
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, self.dark_gray),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, self.light_gray]),
            
            # Skill column styling
            ('ALIGN', (0, 1), (0, -1), 'LEFT'),
            ('LEFTPADDING', (0, 1), (0, -1), 8),
            
            # Checkbox columns styling
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
        ]))
        
        return table
    
    def create_activities_table(self, activities):
        """Create activities suggestion table"""
        headers = ["Recommended Activity", "Materials Needed", "Completed", "Notes"]
        data = [headers]
        
        for activity in activities:
            row = [activity, "", "□", ""]
            data.append(row)
        
        table = Table(data, colWidths=[2.5*inch, 1.8*inch, 0.8*inch, 1.4*inch])
        
        table.setStyle(TableStyle([
            # Header styling
            ('BACKGROUND', (0, 0), (-1, 0), self.blue),
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
            ('TOPPADDING', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ]))
        
        return table
    
    def create_assessment_checklist(self, assessments):
        """Create assessment milestone checklist"""
        headers = ["Assessment Milestone", "Date Tested", "Passed", "Needs Review", "Notes"]
        data = [headers]
        
        for assessment in assessments:
            row = [assessment, "___/___/___", "□", "□", ""]
            data.append(row)
        
        table = Table(data, colWidths=[2.8*inch, 1*inch, 0.6*inch, 0.8*inch, 1.3*inch])
        
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
            ('TOPPADDING', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ]))
        
        return table
    
    def create_pdf(self, filename="enhanced_math_success_checklist.pdf"):
        """Generate the comprehensive PDF checklist"""
        doc = SimpleDocTemplate(filename, pagesize=letter,
                              rightMargin=36, leftMargin=36,
                              topMargin=36, bottomMargin=36)
        
        styles = self.create_custom_styles()
        story = []
        grade_data = self.get_enhanced_grade_data()
        
        # Cover Page
        story.append(Spacer(1, 1*inch))
        story.append(Paragraph("Enhanced Homeschool Math Success Checklist", styles['title']))
        story.append(Spacer(1, 0.5*inch))
        
        # Student info section
        student_info = """
        <b>Student Name:</b> _________________________________<br/><br/>
        <b>Current Grade Level:</b> ____________________________<br/><br/>
        <b>School Year:</b> ___________________________________<br/><br/>
        <b>Parent/Teacher:</b> ________________________________<br/><br/>
        <b>Start Date:</b> ____________________________________<br/><br/>
        <b>Target Completion Date:</b> __________________________
        """
        story.append(Paragraph(student_info, styles['body']))
        story.append(Spacer(1, 0.8*inch))
        
        # Instructions
        instructions = """
        <b>How to Use This Enhanced Checklist:</b><br/>
        • This comprehensive guide covers Pre-K through 8th grade math skills<br/>
        • Each grade includes: Core Skills, Recommended Activities, and Assessment Milestones<br/>
        • Use the progress tracking tables to monitor skill development<br/>
        • Check off skills as they are mastered and record dates<br/>
        • Use the activity suggestions to reinforce learning<br/>
        • Regular assessments help identify areas needing extra attention<br/>
        • Celebrate achievements and adjust pace as needed for your child's learning style
        """
        story.append(Paragraph(instructions, styles['body']))
        story.append(PageBreak())
        
        # Table of Contents
        story.append(Paragraph("Table of Contents", styles['grade']))
        story.append(Spacer(1, 10))
        
        toc_content = ""
        page_num = 3
        for grade in grade_data.keys():
            toc_content += f"<b>{grade}</b> ................................. Page {page_num}<br/>"
            page_num += 2
        
        story.append(Paragraph(toc_content, styles['body']))
        story.append(PageBreak())
        
        # Generate pages for each grade
        for grade, content in grade_data.items():
            # Grade title page
            story.append(Paragraph(grade, styles['grade']))
            story.append(Spacer(1, 15))
            
            # Core Skills Section
            story.append(Paragraph("Core Skills Progress Tracking", styles['section']))
            story.append(Spacer(1, 10))
            story.append(self.create_progress_tracking_table(grade, content['skills']))
            story.append(Spacer(1, 20))
            
            # Progress legend
            legend = """
            <b>Progress Legend:</b> Not Started = Concept not yet introduced | Learning = Being taught, needs support | 
            Practicing = Can do with minimal help | Mastered = Demonstrates understanding independently
            """
            story.append(Paragraph(legend, styles['small']))
            story.append(PageBreak())
            
            # Activities and Assessment page
            story.append(Paragraph(f"{grade} - Activities & Assessments", styles['grade']))
            story.append(Spacer(1, 15))
            
            # Recommended Activities
            story.append(Paragraph("Recommended Learning Activities", styles['section']))
            story.append(Spacer(1, 10))
            story.append(self.create_activities_table(content['activities']))
            story.append(Spacer(1, 20))
            
            # Assessment Milestones
            story.append(Paragraph("Assessment Milestones", styles['section']))
            story.append(Spacer(1, 10))
            story.append(self.create_assessment_checklist(content['assessments']))
            story.append(Spacer(1, 15))
            
            # Grade completion notes
            notes_section = f"""
            <b>{grade} Completion Notes:</b><br/>
            Overall Progress: ________________________<br/>
            Strengths: ______________________________<br/>
            Areas for Improvement: ____________________<br/>
            Date Grade Completed: ____________________<br/>
            Parent Signature: ________________________
            """
            story.append(Paragraph(notes_section, styles['body']))
            story.append(PageBreak())
        
        # Resources and Tips Page
        story.append(Paragraph("Homeschool Math Resources & Tips", styles['grade']))
        story.append(Spacer(1, 15))
        
        resources_content = """
        <b>Recommended Math Curricula:</b><br/>
        □ Saxon Math □ Math-U-See □ Teaching Textbooks □ Beast Academy □ Singapore Math<br/>
        □ Khan Academy □ IXL Math □ Other: ___________________________<br/><br/>
        
        <b>Essential Math Manipulatives by Grade:</b><br/>
        <b>Pre-K - 2nd Grade:</b> Counting bears, pattern blocks, base-10 blocks, fraction circles<br/>
        <b>3rd - 5th Grade:</b> Multiplication charts, geometric solids, measuring tools, calculators<br/>
        <b>6th - 8th Grade:</b> Algebra tiles, graphing paper, protractors, scientific calculators<br/><br/>
        
        <b>Online Resources:</b><br/>
        • Khan Academy (free video lessons and practice)<br/>
        • IXL Math (comprehensive practice platform)<br/>
        • Prodigy Math (game-based learning)<br/>
        • DragonBox (algebra apps for younger learners)<br/>
        • GeoGebra (interactive geometry, algebra, and calculus)<br/><br/>
        
        <b>Assessment and Testing Options:</b><br/>
        • Weekly skill quizzes • Monthly progress tests • Quarterly comprehensive reviews<br/>
        • Standardized tests (CAT, Iowa, Stanford) • Portfolio assessments<br/>
        • State-required testing • College entrance exam prep (SAT, ACT)<br/><br/>
        
        <b>Tips for Math Success:</b><br/>
        • Practice mental math daily (5-10 minutes)<br/>
        • Connect math to real-life situations<br/>
        • Use visual and hands-on approaches<br/>
        • Celebrate small victories and progress<br/>
        • Don't rush - mastery is more important than speed<br/>
        • Seek help when needed - tutoring, co-ops, online support<br/><br/>
        
        <b>Record Keeping Notes:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        """
        
        story.append(Paragraph(resources_content, styles['body']))
        story.append(PageBreak())
        
        # Final Summary Page
        story.append(Paragraph("Multi-Year Progress Summary", styles['grade']))
        story.append(Spacer(1, 15))
        
        summary_content = """
        <b>Overall Math Journey Summary:</b><br/><br/>
        
        <b>Grades Completed:</b><br/>
        Pre-K: □ Started ___/___ Completed ___/___<br/>
        Kindergarten: □ Started ___/___ Completed ___/___<br/>
        1st Grade: □ Started ___/___ Completed ___/___<br/>
        2nd Grade: □ Started ___/___ Completed ___/___<br/>
        3rd Grade: □ Started ___/___ Completed ___/___<br/>
        4th Grade: □ Started ___/___ Completed ___/___<br/>
        5th Grade: □ Started ___/___ Completed ___/___<br/>
        6th Grade: □ Started ___/___ Completed ___/___<br/>
        7th Grade: □ Started ___/___ Completed ___/___<br/>
        8th Grade: □ Started ___/___ Completed ___/___<br/><br/>
        
        <b>Student's Math Strengths:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Areas of Continued Growth:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Favorite Math Topics/Activities:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>High School Math Readiness:</b><br/>
        □ Ready for Algebra I □ Needs Pre-Algebra review □ Advanced/Ready for Geometry<br/><br/>
        
        <b>Parent/Teacher Final Comments:</b><br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/>
        ________________________________________________________________<br/><br/>
        
        <b>Date Completed:</b> _________________ <b>Parent Signature:</b> _____________________
        """
        
        story.append(Paragraph(summary_content, styles['body']))
        
        # Build the PDF
        doc.build(story)
        print(f"Enhanced PDF created successfully: {filename}")
        return filename

def main():
    """Main function with enhanced options"""
    checker = EnhancedMathSuccessChecklist()
    
    print("\n\033[1;35m🧮 Enhanced Math Success Checklist Generator 🧮\033[0m")
    print("\033[34m" + "="*50 + "\033[0m")
    print("\n\033[1;33mChoose an option:\033[0m")
    print("1. 📺 Display checklist in console")
    print("2. 📄 Generate comprehensive PDF")
    print("3. 🚀 Both (display and generate PDF)")
    
    choice = input("\n\033[36mEnter your choice (1, 2, or 3): \033[0m").strip()
    
    if choice in ['1', '3']:
        checker.print_enhanced_checklist()
    
    if choice in ['2', '3']:
        filename = checker.create_pdf()
        
        # Check if file was created successfully
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
            print(f"\n✅ Success! Enhanced Math Checklist created as '{filename}'")
            print(f"📄 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
            print("\n📋 Your enhanced checklist includes:")
            print("   • Comprehensive skills for Pre-K through 8th Grade")
            print("   • Progress tracking tables with 4-level mastery system")
            print("   • Recommended activities for each grade level")
            print("   • Assessment milestones and testing guidance")
            print("   • Homeschool math resources and curriculum suggestions")
            print("   • Multi-year progress summary pages")
            print("   • Professional formatting with your purple/blue color scheme")
            print("\n\033[1;32mYou can now print this professional PDF to track your homeschool math progress!\033[0m")
        else:
            print("\n❌ Error: PDF file was not created successfully.")
    
    if choice not in ['1', '2', '3']:
        print("\n\033[31mInvalid choice. Please select 1, 2, or 3.\033[0m")

if __name__ == "__main__":
    main()