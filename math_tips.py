from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import Color, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.platypus.tableofcontents import TableOfContents
import os

class HomeschoolMathGuide:
    def __init__(self):
        # Define your color scheme
        self.purple = Color(0.463, 0.294, 0.635)  # #764ba2
        self.blue = Color(0.4, 0.494, 0.918)     # #667eea
        self.dark_gray = Color(0.2, 0.2, 0.2)
        
    def create_custom_styles(self):
        """Create custom paragraph styles"""
        styles = getSampleStyleSheet()
        
        # Title style
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=self.purple,
            fontName='Helvetica-Bold'
        )
        
        # Section header style
        section_style = ParagraphStyle(
            'SectionHeader',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=self.blue,
            fontName='Helvetica-Bold'
        )
        
        # Body text style
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=12,
            alignment=TA_JUSTIFY,
            textColor=self.dark_gray,
            fontName='Helvetica'
        )
        
        # Tip content style
        tip_style = ParagraphStyle(
            'TipContent',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=8,
            leftIndent=20,
            textColor=self.dark_gray,
            fontName='Helvetica'
        )
        
        return {
            'title': title_style,
            'section': section_style,
            'body': body_style,
            'tip': tip_style
        }
    
    def get_enhanced_content(self):
        """Return enhanced and expanded content"""
        tips = [
            {
                "title": "1. Real-World Applications",
                "content": "Connect math concepts to everyday situations that your child encounters. Use cooking to teach fractions and measurements, grocery shopping for addition and budgeting, home improvement projects for geometry, and sports statistics for data analysis. This approach helps children understand why math matters and makes abstract concepts concrete.",
                "activities": [
                    "• Recipe scaling (doubling or halving ingredients)",
                    "• Calculating tips at restaurants",
                    "• Measuring rooms for furniture placement",
                    "• Planning garden layouts using area and perimeter"
                ]
            },
            {
                "title": "2. Short, Frequent Sessions",
                "content": "Research shows that shorter, more frequent math sessions are more effective than lengthy ones. Aim for 15-20 minute focused sessions for elementary students, and 25-30 minutes for middle schoolers. This prevents mental fatigue and maintains engagement throughout the lesson.",
                "activities": [
                    "• Morning math warm-ups (5-10 minutes)",
                    "• Afternoon skill practice sessions",
                    "• Evening math games or puzzles",
                    "• Weekend project-based applications"
                ]
            },
            {
                "title": "3. Hands-On Learning with Manipulatives",
                "content": "Physical objects help students visualize abstract mathematical concepts. Manipulatives bridge the gap between concrete understanding and abstract thinking, making math more accessible for kinesthetic learners and visual processors.",
                "activities": [
                    "• Base-ten blocks for place value and operations",
                    "• Fraction bars and circles for fraction concepts",
                    "• Geometric solids for 3D shape exploration",
                    "• Algebra tiles for equation solving"
                ]
            },
            {
                "title": "4. Gamification and Math Games",
                "content": "Transform routine practice into engaging games. Games naturally incorporate repetition, immediate feedback, and motivation through challenge and achievement. They also reduce math anxiety by creating a playful learning environment.",
                "activities": [
                    "• Dice games for probability and number operations",
                    "• Card games for mental math practice",
                    "• Board games with mathematical strategy",
                    "• Online math platforms with game elements"
                ]
            },
            {
                "title": "5. Growth Mindset and Positive Reinforcement",
                "content": "Focus on effort, strategy, and improvement rather than just correct answers. Praise the problem-solving process, celebrate mistakes as learning opportunities, and emphasize that mathematical ability grows with practice and persistence.",
                "activities": [
                    "• Process-focused praise ('I like how you tried multiple strategies')",
                    "• Error analysis discussions",
                    "• Progress celebrations for effort and improvement",
                    "• Mathematical reflection journals"
                ]
            },
            {
                "title": "6. Multi-Sensory Learning Approaches",
                "content": "Engage multiple senses to accommodate different learning styles and strengthen neural pathways. Combine visual representations, auditory explanations, and kinesthetic activities to create rich learning experiences.",
                "activities": [
                    "• Visual: Charts, graphs, and colorful diagrams",
                    "• Auditory: Math songs, verbal explanations, and discussions",
                    "• Kinesthetic: Movement games and hands-on activities",
                    "• Tactile: Textured materials and building activities"
                ]
            },
            {
                "title": "7. Progress Tracking and Assessment",
                "content": "Regular assessment helps identify strengths and areas for improvement. Use a variety of assessment methods including formal tests, informal observations, portfolio work, and self-assessment to get a complete picture of your child's mathematical understanding.",
                "activities": [
                    "• Weekly progress charts and goal setting",
                    "• Portfolio collections of best work",
                    "• Peer teaching opportunities",
                    "• Self-reflection and goal-setting sessions"
                ]
            },
            {
                "title": "8. Individualized Pacing and Expectations",
                "content": "Every child learns at their own pace. Adjust your expectations and timeline based on your child's individual needs, learning style, and developmental readiness. Focus on deep understanding rather than rushing through curriculum.",
                "activities": [
                    "• Regular learning style assessments",
                    "• Flexible scheduling based on child's energy and focus",
                    "• Mastery-based progression rather than time-based",
                    "• Regular parent-child conferences about math goals"
                ]
            }
        ]
        
        resources = {
            "Books and Literature": [
                "• 'The Number Devil' by Hans Magnus Enzensberger",
                "• 'Math Curse' by Jon Scieszka",
                "• 'Sir Cumference' series by Cindy Neuschwander",
                "• 'Bedtime Math' series by Laura Overdeck"
            ],
            "Online Resources": [
                "• Khan Academy (free comprehensive math courses)",
                "• IXL Math (adaptive practice platform)",
                "• Prodigy Math (game-based learning)",
                "• Numberphile (engaging math videos)"
            ],
            "Apps and Software": [
                "• DragonBox (algebra concepts for young learners)",
                "• Photomath (step-by-step problem solving)",
                "• GeoGebra (interactive geometry and graphing)",
                "• Math Playground (games and problem-solving)"
            ],
            "Physical Materials": [
                "• Cuisenaire rods for number relationships",
                "• Pattern blocks for geometry exploration",
                "• Tangrams for spatial reasoning",
                "• Math journals for reflection and problem-solving"
            ]
        }
        
        return tips, resources
    
    def create_pdf(self, filename="homeschool_math_guide.pdf"):
        """Generate the PDF document"""
        doc = SimpleDocTemplate(filename, pagesize=letter, 
                              rightMargin=72, leftMargin=72,
                              topMargin=72, bottomMargin=18)
        
        # Get styles and content
        styles = self.create_custom_styles()
        tips, resources = self.get_enhanced_content()
        
        # Build the document
        story = []
        
        # Title
        story.append(Paragraph("Homeschool Math Success Guide", styles['title']))
        story.append(Spacer(1, 12))
        
        # Subtitle
        subtitle = Paragraph(
            "<i>Essential strategies and activities to make math engaging and effective for homeschool students</i>",
            styles['body']
        )
        story.append(subtitle)
        story.append(Spacer(1, 30))
        
        # Introduction
        intro_text = """
        Mathematics is one of the most important subjects in your child's education, yet it can also be one of the most challenging to teach at home. This guide provides research-based strategies and practical activities to help you create a positive, effective math learning environment for your homeschooled child.
        
        Whether you're just starting your homeschool journey or looking to improve your current math instruction, these eight essential strategies will help you build your child's mathematical confidence and competence.
        """
        story.append(Paragraph(intro_text, styles['body']))
        story.append(Spacer(1, 20))
        
        # Main content - Tips
        story.append(Paragraph("Eight Essential Strategies", styles['section']))
        
        for tip in tips:
            # Tip title
            story.append(Paragraph(tip['title'], styles['section']))
            
            # Tip content
            story.append(Paragraph(tip['content'], styles['body']))
            story.append(Spacer(1, 8))
            
            # Activities
            story.append(Paragraph("<b>Practical Activities:</b>", styles['tip']))
            for activity in tip['activities']:
                story.append(Paragraph(activity, styles['tip']))
            
            story.append(Spacer(1, 15))
        
        # Resources section
        story.append(Spacer(1, 20))
        story.append(Paragraph("Additional Resources", styles['section']))
        
        for category, items in resources.items():
            story.append(Paragraph(f"<b>{category}</b>", styles['body']))
            for item in items:
                story.append(Paragraph(item, styles['tip']))
            story.append(Spacer(1, 10))
        
        # Footer
        story.append(Spacer(1, 30))
        footer_text = """
        <i>Remember: The goal is not perfection, but progress. Every child learns differently, and your patience, 
        encouragement, and adaptability are the most important tools in your homeschool math toolkit.</i>
        """
        story.append(Paragraph(footer_text, styles['body']))
        
        # Build PDF
        doc.build(story)
        print(f"PDF created successfully: {filename}")
        return filename

def main():
    """Main function to generate the PDF"""
    guide = HomeschoolMathGuide()
    filename = guide.create_pdf()
    
    # Check if file was created successfully
    if os.path.exists(filename):
        print(f"\n✅ Success! Your enhanced Homeschool Math Guide has been created as '{filename}'")
        print(f"📄 File size: {os.path.getsize(filename)} bytes")
        print("\n📋 What's included in your guide:")
        print("   • 8 comprehensive teaching strategies")
        print("   • Practical activities for each strategy") 
        print("   • Extensive resource recommendations")
        print("   • Professional formatting with your color scheme")
    else:
        print("❌ Error: PDF file was not created successfully")

if __name__ == "__main__":
    main()
