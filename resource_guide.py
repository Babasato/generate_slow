from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import Color, white, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
from datetime import datetime
import os

class MathResourceGuide:
    def __init__(self):
        # Define your color scheme
        self.purple = Color(0.463, 0.294, 0.635)  # #764ba2
        self.blue = Color(0.4, 0.494, 0.918)     # #667eea
        self.light_purple = Color(0.463, 0.294, 0.635, alpha=0.2)
        self.light_blue = Color(0.4, 0.494, 0.918, alpha=0.2)
        self.dark_gray = Color(0.2, 0.2, 0.2)
        self.light_gray = Color(0.9, 0.9, 0.9)
        
        # Resource categories
        self.resources = {
            "Complete Curricula": [
                ("Singapore Math", "Concrete-Pictorial-Abstract approach, builds deep conceptual understanding", "singaporemath.com", "All grades", "$$$"),
                ("Math-U-See", "Multi-sensory with manipulatives, DVD lessons, self-paced progression", "mathusee.com", "K-12", "$$$"),
                ("Beast Academy", "Art of Problem Solving's challenging comic-based curriculum for advanced learners", "beastacademy.com", "2-8", "$$$$"),
                ("Saxon Math", "Incremental development with continuous review, traditional spiral approach", "saxonpublishers.harcourt.com", "K-12", "$$$"),
                ("Teaching Textbooks", "Self-teaching with built-in tutoring, automated grading and tracking", "teachingtextbooks.com", "3-12", "$$$$"),
                ("RightStart Mathematics", "Hands-on approach using AL Abacus, focuses on number sense", "rightstartmath.com", "K-12", "$$$")
            ],
            "Online Learning Platforms": [
                ("Khan Academy", "Free comprehensive lessons K-12, mastery-based with progress tracking", "khanacademy.org", "K-12", "FREE"),
                ("IXL Math", "Adaptive practice with detailed analytics, covers PreK-12", "ixl.com/math", "PreK-12", "$$"),
                ("Prodigy Math", "Game-based learning aligned to curriculum standards, engaging for K-8", "prodigygame.com", "K-8", "$"),
                ("CTC Math", "Short video lessons with practice, progress tracking for K-12", "ctcmath.com", "K-12", "$$"),
                ("Aleks Math", "AI-driven adaptive learning, comprehensive assessment and instruction", "aleks.com", "3-12", "$$$"),
                ("Time4Learning", "Self-paced online curriculum with automated record keeping", "time4learning.com", "PreK-12", "$$")
            ],
            "Supplemental Resources": [
                ("Life of Fred", "Story-based math that integrates with literature and life skills", "lifeoffredmath.com", "K-12", "$$"),
                ("Math Mammoth", "Workbooks focusing on conceptual understanding and mental math", "mathmammoth.com", "1-7", "$$"),
                ("Hands-On Equations", "Algebra made visual using manipulatives and balance concepts", "borenson.com", "3-12", "$$"),
                ("Professor B Math", "Video-based instruction with real-world applications", "professorbmath.com", "6-12", "$$$"),
                ("Number Lovin'", "Creative math activities and games for elementary ages", "numberlovin.com", "K-6", "$"),
                ("Math Games Books", "Problem-solving puzzles and critical thinking activities", "tabletopacademy.net", "K-12", "$")
            ],
            "Free Resources & Tools": [
                ("Desmos Graphing Calculator", "Free online graphing calculator with classroom activities", "desmos.com/calculator", "6-12", "FREE"),
                ("Math is Fun", "Clear explanations, examples, and interactive activities", "mathsisfun.com", "K-12", "FREE"),
                ("Coolmath Games", "Educational math games that actually teach concepts", "coolmathgames.com", "K-8", "FREE"),
                ("Math Open Reference", "Interactive geometry reference with definitions and examples", "mathopenref.com", "6-12", "FREE"),
                ("Illuminations (NCTM)", "Standards-based activities and lesson plans", "illuminations.nctm.org", "K-12", "FREE"),
                ("Homeschool Math", "Free worksheets, lessons, and curriculum guides", "homeschoolmath.net", "K-12", "FREE")
            ],
            "Advanced & Gifted Programs": [
                ("Art of Problem Solving", "Rigorous courses for mathematically gifted students", "artofproblemsolving.com", "6-12", "$$$$"),
                ("MATHCOUNTS", "National middle school mathematics competition program", "mathcounts.org", "6-8", "FREE"),
                ("AMC Competitions", "American Mathematics Competitions (AMC 8, AMC 10/12)", "maa.org/math-competitions", "8-12", "$"),
                ("Stanford EPGY", "Online courses for academically talented youth", "epgy.stanford.edu", "K-12", "$$$$"),
                ("Johns Hopkins CTY", "Advanced mathematics courses for gifted learners", "cty.jhu.edu", "K-12", "$$$$"),
                ("Russian School of Math", "After-school math program with online options", "russianschool.com", "K-12", "$$$")
            ],
            "Special Needs Support": [
                ("Touch Math", "Multisensory approach using touchpoints for counting", "touchmath.com", "K-3", "$$$"),
                ("Right Brain Math", "Visual and conceptual methods for right-brain dominant learners", "rightbrainmath.com", "K-6", "$$"),
                ("Making Math Real", "Multisensory structured approach for learning disabilities", "makingmathreal.org", "K-12", "$$$$"),
                ("ModMath Paper", "Graph paper designed to help with number alignment", "modmath.com", "K-12", "$"),
                ("Calculadder", "Systematic drill program for math fact fluency", "calculadder.com", "K-6", "$$"),
                ("Times Tales", "Memory tool for multiplication facts using visual stories", "timestales.com", "3-6", "$$")
            ]
        }
        
    def create_custom_styles(self):
        """Create custom paragraph styles"""
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
        
        # Section header style
        section_style = ParagraphStyle(
            'SectionHeader',
            parent=styles['Heading2'],
            fontSize=16,
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
    
    def create_resource_table(self, category, resources):
        """Create a table for each resource category"""
        # Headers
        headers = ["Resource", "Description", "Website", "Grades", "Cost"]
        data = [headers]
        
        # Add resource data
        for name, desc, url, grades, cost in resources:
            # Wrap long descriptions
            if len(desc) > 50:
                desc = desc[:47] + "..."
            row = [name, desc, url, grades, cost]
            data.append(row)
        
        # Create table
        table = Table(data, colWidths=[1.3*inch, 2.2*inch, 1.5*inch, 0.7*inch, 0.6*inch])
        
        # Style the table
        table.setStyle(TableStyle([
            # Header row styling
            ('BACKGROUND', (0, 0), (-1, 0), self.purple),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            
            # Data rows styling
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, self.dark_gray),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, self.light_gray]),
            ('LEFTPADDING', (0, 1), (-1, -1), 6),
            ('RIGHTPADDING', (0, 1), (-1, -1), 6),
            ('TOPPADDING', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
            
            # Cost column center alignment
            ('ALIGN', (-1, 0), (-1, -1), 'CENTER'),
            ('ALIGN', (-2, 0), (-2, -1), 'CENTER'),
        ]))
        
        return table
    
    def create_comparison_chart(self):
        """Create a curriculum comparison chart"""
        comparison_data = [
            ["Curriculum", "Teaching Style", "Grade Range", "Difficulty", "Parent Involvement", "Cost Range"],
            ["Singapore Math", "Conceptual", "K-8", "Medium-High", "Medium", "$150-300/year"],
            ["Math-U-See", "Visual/Hands-on", "K-12", "Medium", "Low-Medium", "$200-400/year"],
            ["Beast Academy", "Problem Solving", "2-8", "High", "Medium", "$100-200/year"],
            ["Saxon Math", "Traditional", "K-12", "Medium", "Low", "$100-250/year"],
            ["Teaching Textbooks", "Self-Teaching", "3-12", "Medium", "Very Low", "$300-500/year"],
            ["Khan Academy", "Video-based", "K-12", "Variable", "Low", "FREE"]
        ]
        
        table = Table(comparison_data, colWidths=[1.2*inch, 1*inch, 0.8*inch, 0.8*inch, 1*inch, 1*inch])
        
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
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, self.light_gray]),
            ('ALIGN', (0, 1), (0, -1), 'LEFT'),
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
            ('LEFTPADDING', (0, 1), (-1, -1), 4),
            ('RIGHTPADDING', (0, 1), (-1, -1), 4),
        ]))
        
        return table
    
    def create_pdf(self, filename="homeschool_math_resource_guide.pdf"):
        """Generate the comprehensive PDF resource guide"""
        doc = SimpleDocTemplate(filename, pagesize=letter,
                              rightMargin=36, leftMargin=36,
                              topMargin=36, bottomMargin=36)
        
        styles = self.create_custom_styles()
        story = []
        
        # Cover Page
        story.append(Spacer(1, 1*inch))
        story.append(Paragraph("Homeschool Math Resource Guide", styles['title']))
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph("Complete Guide to Math Resources for Homeschool Families", styles['section']))
        story.append(Spacer(1, 0.5*inch))
        
        # Cover info
        cover_info = f"""
        <b>Created:</b> {datetime.now().strftime("%B %Y")}<br/><br/>
        <b>Includes:</b><br/>
        • Complete curriculum reviews and comparisons<br/>
        • Online learning platforms and tools<br/>
        • Free resources and websites<br/>
        • Supplemental materials and games<br/>
        • Special needs accommodations<br/>
        • Advanced and gifted student options<br/>
        • Cost breakdowns and recommendations<br/><br/>
        
        <b>How to Use This Guide:</b><br/>
        • Review curriculum comparison chart first<br/>
        • Identify your child's learning style and needs<br/>
        • Start with free resources to test approaches<br/>
        • Consider your budget and time constraints<br/>
        • Mix and match resources as needed
        """
        story.append(Paragraph(cover_info, styles['body']))
        story.append(PageBreak())
        
        # Table of Contents
        story.append(Paragraph("Table of Contents", styles['section']))
        story.append(Spacer(1, 10))
        
        toc_content = """
        <b>Curriculum Comparison Chart</b> ........................... Page 3<br/>
        <b>Complete Curricula</b> ........................................ Page 4<br/>
        <b>Online Learning Platforms</b> ................................ Page 5<br/>
        <b>Supplemental Resources</b> ................................... Page 6<br/>
        <b>Free Resources & Tools</b> .................................... Page 7<br/>
        <b>Advanced & Gifted Programs</b> .............................. Page 8<br/>
        <b>Special Needs Support</b> ..................................... Page 9<br/>
        <b>Quick Reference Guide</b> ..................................... Page 10<br/>
        """
        story.append(Paragraph(toc_content, styles['body']))
        story.append(PageBreak())
        
        # Curriculum Comparison Chart
        story.append(Paragraph("Curriculum Comparison Chart", styles['section']))
        story.append(Paragraph("Quick overview of popular complete curricula", styles['body']))
        story.append(Spacer(1, 10))
        story.append(self.create_comparison_chart())
        story.append(Spacer(1, 15))
        
        comparison_notes = """
        <b>Cost Legend:</b> $ = Under $50/year | $$ = $50-150/year | $$$ = $150-300/year | $$$$ = $300+/year<br/>
        <b>Parent Involvement:</b> Very Low = child works independently | Low = minimal daily guidance | 
        Medium = regular instruction needed | High = significant daily teaching required
        """
        story.append(Paragraph(comparison_notes, styles['small']))
        story.append(PageBreak())
        
        # Resource Categories
        for category, resources in self.resources.items():
            story.append(Paragraph(category, styles['section']))
            
            # Add category-specific intro
            category_intros = {
                "Complete Curricula": "Comprehensive math programs that provide structured scope and sequence for the entire school year.",
                "Online Learning Platforms": "Interactive websites and apps that provide math instruction and practice.",
                "Supplemental Resources": "Materials to enhance your primary curriculum or provide extra practice in specific areas.",
                "Free Resources & Tools": "High-quality educational resources available at no cost.",
                "Advanced & Gifted Programs": "Challenging materials and programs for mathematically talented students.",
                "Special Needs Support": "Resources designed for students with learning differences or special needs."
            }
            
            if category in category_intros:
                story.append(Paragraph(category_intros[category], styles['body']))
                story.append(Spacer(1, 10))
            
            story.append(self.create_resource_table(category, resources))
            story.append(Spacer(1, 20))
            
            # Add page break after each major section except the last
            if category != "Special Needs Support":
                story.append(PageBreak())
        
        # Quick Reference Guide
        story.append(PageBreak())
        story.append(Paragraph("Quick Reference Guide", styles['section']))
        story.append(Spacer(1, 10))
        
        quick_ref = """
        <b>STRUGGLING STUDENTS:</b><br/>
        • Try Math-U-See or Teaching Textbooks for multi-sensory approach<br/>
        • Use Khan Academy for free video explanations<br/>
        • Consider Touch Math for early elementary<br/><br/>
        
        <b>ADVANCED STUDENTS:</b><br/>
        • Beast Academy or Art of Problem Solving for challenge<br/>
        • MATHCOUNTS competitions for middle school<br/>
        • Consider grade-level acceleration<br/><br/>
        
        <b>VISUAL LEARNERS:</b><br/>
        • Singapore Math for pictorial representations<br/>
        • Right Brain Math for creative approaches<br/>
        • Use manipulatives and visual aids<br/><br/>
        
        <b>KINESTHETIC LEARNERS:</b><br/>
        • Math-U-See with hands-on manipulatives<br/>
        • RightStart Math with AL Abacus<br/>
        • Incorporate movement and physical activities<br/><br/>
        
        <b>BUDGET-CONSCIOUS FAMILIES:</b><br/>
        • Start with Khan Academy (completely free)<br/>
        • Use library books and free printables<br/>
        • Consider used curriculum marketplaces<br/>
        • Mix free resources with affordable supplements<br/><br/>
        
        <b>BUSY PARENTS:</b><br/>
        • Teaching Textbooks for independent learning<br/>
        • Online programs like Time4Learning<br/>
        • Automated grading and progress tracking<br/><br/>
        
        <b>LITERATURE-BASED APPROACH:</b><br/>
        • Life of Fred for story-based learning<br/>
        • Living Math philosophy and resources<br/>
        • Integrate math with real-world applications<br/><br/>
        
        <b>TRADITIONAL APPROACH:</b><br/>
        • Saxon Math for systematic spiral review<br/>
        • Consistent daily practice and drill<br/>
        • Structured lesson plans and assessments
        """
        
        story.append(Paragraph(quick_ref, styles['body']))
        
        # Build the PDF
        doc.build(story)
        print(f"PDF created successfully: {filename}")
        return filename

def main():
    """Main function to generate the resource guide PDF"""
    guide = MathResourceGuide()
    filename = guide.create_pdf()
    
    # Check if file was created successfully
    if os.path.exists(filename):
        file_size = os.path.getsize(filename)
        print(f"\n✅ Success! Your Math Resource Guide has been created as '{filename}'")
        print(f"📄 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        print("\n📚 Your guide includes:")
        print("   • Comprehensive curriculum comparison chart")
        print("   • 36+ detailed resource reviews with websites and costs")
        print("   • Organized by category (curricula, online, supplements, etc.)")
        print("   • Special sections for advanced and special needs students")
        print("   • Quick reference guide for different learning styles")
        print("   • Professional formatting with purple/blue color scheme")
        print("\n💡 Perfect for:")
        print("   • New homeschool families choosing curriculum")
        print("   • Parents wanting to supplement current math program")
        print("   • Finding resources for struggling or advanced students")
        print("   • Budget-conscious families seeking free alternatives")
    else:
        print("❌ Error: PDF file was not created successfully")

if __name__ == "__main__":
    main()