from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import Color, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
import os

class QuickMathGames:
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
            fontSize=10,
            spaceAfter=8,
            alignment=TA_JUSTIFY,
            textColor=self.dark_gray,
            fontName='Helvetica'
        )
        
        # Game detail style
        game_style = ParagraphStyle(
            'GameDetail',
            parent=styles['Normal'],
            fontSize=9,
            spaceAfter=4,
            leftIndent=15,
            textColor=self.dark_gray,
            fontName='Helvetica'
        )
        
        return {
            'title': title_style,
            'section': section_style,
            'body': body_style,
            'game': game_style
        }
    
    def get_enhanced_content(self):
        """Return enhanced and expanded content"""
        games = [
            {
                "title": "1. Number Line Leap",
                "description": "Transform your hallway or living room into a giant number line using masking tape. Mark numbers 0-20 (or higher for older kids) on the floor. Call out math problems and have your child physically jump to the correct answer. This kinesthetic approach helps children visualize number relationships and makes abstract concepts concrete.",
                "skills": "Addition, subtraction, number recognition, skip counting, inequalities",
                "ages": "Ages 5-8 (beginners), 9-12 (advanced problems)",
                "materials": ["Masking tape", "Marker", "Index cards for problems"],
                "variations": [
                    "• Use negative numbers for advanced students",
                    "• Create multiplication tables on the floor",
                    "• Add decimal points for fraction work",
                    "• Time challenges for speed practice"
                ],
                "learning_benefits": "Develops number sense, spatial awareness, and provides physical activity while learning"
            },
            {
                "title": "2. Grocery Store Math",
                "description": "Turn every shopping trip into a math adventure. Before entering the store, give your child a budget and shopping list. Have them estimate costs, compare unit prices, calculate discounts, and figure out tax. This real-world application shows how math is essential in daily life and builds practical financial literacy skills.",
                "skills": "Estimation, money math, percentages, ratios, data analysis, budgeting",
                "ages": "Ages 8+ (basic), 10+ (advanced calculations)",
                "materials": ["Calculator (for checking)", "Notebook", "Shopping list"],
                "variations": [
                    "• Compare prices per ounce/pound between brands",
                    "• Calculate savings with coupons and sales",
                    "• Estimate total before checkout",
                    "• Track spending across multiple store visits"
                ],
                "learning_benefits": "Builds practical life skills, reinforces decimal operations, and develops estimation abilities"
            },
            {
                "title": "3. Dice War Champions",
                "description": "Each player rolls two dice and performs the specified operation (addition, subtraction, multiplication, or division). The player with the highest correct answer wins both sets of dice. Continue until one player has all the dice. This fast-paced game builds automaticity with math facts while maintaining high engagement.",
                "skills": "Basic operations, quick mental math, strategic thinking, number comparisons",
                "ages": "Ages 6-12 (adjust operations by age)",
                "materials": ["4-6 dice per player", "Paper for scorekeeping", "Timer (optional)"],
                "variations": [
                    "• Use three dice for more complex operations",
                    "• Include parentheses for order of operations",
                    "• Play with fractions using fraction dice",
                    "• Tournament style with multiple rounds"
                ],
                "learning_benefits": "Improves computational fluency, builds competitive motivation, and develops quick thinking skills"
            },
            {
                "title": "4. Fraction Pizza Party",
                "description": "Create paper plate 'pizzas' with different toppings drawn on them. Cut the pizzas into various fractional pieces (halves, thirds, quarters, eighths). Practice serving different portions to family members, comparing sizes, and adding fractions together when someone wants multiple slices.",
                "skills": "Fractions, equivalent fractions, addition/subtraction of fractions, visual representation",
                "ages": "Ages 7-10 (basic), 11+ (complex operations)",
                "materials": ["Paper plates", "Colored markers", "Scissors", "Brad fasteners"],
                "variations": [
                    "• Create fraction circles with different denominators",
                    "• Use real pizza for a delicious lesson",
                    "• Compare fractions across different 'restaurants'",
                    "• Practice decimal equivalents"
                ],
                "learning_benefits": "Makes abstract fraction concepts concrete, develops part-whole understanding, and connects to real-world situations"
            },
            {
                "title": "5. Mathematical Scavenger Hunt",
                "description": "Create targeted lists of mathematical concepts to find throughout your home and neighborhood. Look for geometric shapes, patterns, symmetry, angles, and number sequences. This activity helps children recognize that math exists everywhere and develops observational skills while reinforcing classroom learning.",
                "skills": "Geometry, pattern recognition, measurement, data collection, spatial reasoning",
                "ages": "All ages (adjust complexity of items)",
                "materials": ["Scavenger hunt lists", "Camera or smartphone", "Measuring tools"],
                "variations": [
                    "• Seasonal themes (holiday shapes, nature patterns)",
                    "• Photo documentation with explanations",
                    "• Neighborhood walks for larger measurements",
                    "• Time-based challenges"
                ],
                "learning_benefits": "Connects classroom learning to real world, develops observation skills, and builds mathematical vocabulary"
            },
            {
                "title": "6. Kitchen Chemistry Calculator",
                "description": "Transform cooking and baking into intensive math practice. Double or halve recipes, convert between measurement units, calculate cooking times for different quantities, and explore ratios in ingredient proportions. This delicious approach to math makes learning memorable and practical.",
                "skills": "Ratios, proportions, unit conversions, multiplication, division, fractions",
                "ages": "Ages 8+ (with supervision), 10+ (independent work)",
                "materials": ["Recipes", "Measuring cups", "Calculator", "Kitchen scale"],
                "variations": [
                    "• Scale recipes for different family sizes",
                    "• Convert between metric and imperial units",
                    "• Calculate nutritional information",
                    "• Cost analysis of homemade vs. store-bought"
                ],
                "learning_benefits": "Develops practical life skills, reinforces ratio concepts, and provides immediate, tangible results"
            },
            {
                "title": "7. Time Detective Challenge",
                "description": "Create scenarios where children must calculate elapsed time, plan schedules, and work with different time zones. Use real-world situations like planning a family trip, calculating movie times, or figuring out when relatives in different time zones might be available to call.",
                "skills": "Time calculations, elapsed time, time zones, scheduling, problem-solving",
                "ages": "Ages 9+ (basic), 11+ (complex scenarios)",
                "materials": ["Clocks", "World map", "Calendar", "Schedule templates"],
                "variations": [
                    "• Plan imaginary vacations with flight times",
                    "• Calculate age differences in days/hours",
                    "• Work with 24-hour military time",
                    "• Historical timeline projects"
                ],
                "learning_benefits": "Builds practical time management skills, develops logical thinking, and connects to geography"
            },
            {
                "title": "8. Probability Prediction Station",
                "description": "Set up experiments using coins, dice, cards, and spinners to explore probability concepts. Make predictions, conduct trials, record results, and compare actual outcomes to theoretical probabilities. This hands-on approach makes abstract probability concepts concrete and engaging.",
                "skills": "Probability, statistics, data collection, graphing, predictions, fractions",
                "ages": "Ages 10+ (basic concepts), 12+ (advanced calculations)",
                "materials": ["Coins", "Dice", "Playing cards", "Spinners", "Data recording sheets"],
                "variations": [
                    "• Create probability trees for complex events",
                    "• Use colored marbles in bags for sampling",
                    "• Analyze real sports statistics",
                    "• Compare different probability scenarios"
                ],
                "learning_benefits": "Develops statistical thinking, builds prediction skills, and introduces concepts of chance and uncertainty"
            }
        ]
        
        quick_tips = {
            "Setup Success": [
                "• Keep materials in a designated 'math games' container",
                "• Rotate games weekly to maintain interest",
                "• Adjust difficulty based on your child's current skill level",
                "• Set a positive, encouraging tone before starting"
            ],
            "Engagement Strategies": [
                "• Let children choose which game to play",
                "• Create friendly competition with siblings or parents",
                "• Celebrate effort and improvement, not just correct answers",
                "• Take breaks if frustration levels rise"
            ],
            "Learning Extensions": [
                "• Connect games to current curriculum topics",
                "• Have children explain their thinking process",
                "• Create variations or new rules together",
                "• Document progress and favorite strategies"
            ],
            "Troubleshooting": [
                "• If a game is too easy, add complexity or time pressure",
                "• If too difficult, simplify rules or provide more support",
                "• Use games as rewards for completing other work",
                "• Make losing fun by focusing on learning from mistakes"
            ]
        }
        
        return games, quick_tips
    
    def create_pdf(self, filename="quick_math_games_guide.pdf"):
        """Generate the PDF document"""
        doc = SimpleDocTemplate(filename, pagesize=letter, 
                              rightMargin=72, leftMargin=72,
                              topMargin=72, bottomMargin=72)
        
        # Get styles and content
        styles = self.create_custom_styles()
        games, quick_tips = self.get_enhanced_content()
        
        # Build the document
        story = []
        
        # Title
        story.append(Paragraph("Quick Math Games for Kids", styles['title']))
        story.append(Spacer(1, 8))
        
        # Subtitle
        subtitle = Paragraph(
            "<i>Fun, no-prep math games for homeschool families using purple and blue themes</i>",
            styles['body']
        )
        story.append(subtitle)
        story.append(Spacer(1, 20))
        
        # Introduction
        intro_text = """
        Learning math doesn't have to be a struggle filled with worksheets and textbooks. These eight engaging games transform mathematical concepts into fun, interactive experiences that children actually enjoy. Each game requires minimal preparation, uses common household items, and can be adapted for different skill levels and ages.
        
        These activities are designed to build mathematical confidence while developing critical thinking skills. Whether you need a quick brain break, want to reinforce specific concepts, or simply make math more enjoyable, these games provide practical solutions for homeschooling families.
        """
        story.append(Paragraph(intro_text, styles['body']))
        story.append(Spacer(1, 15))
        
        # Main content - Games
        story.append(Paragraph("Eight Engaging Math Games", styles['section']))
        story.append(Spacer(1, 8))
        
        for i, game in enumerate(games):
            # Add page break before games 2, 4, and 6 for better distribution
            if i in [1, 3, 5]:
                story.append(PageBreak())
            
            # Game title
            story.append(Paragraph(game['title'], styles['section']))
            
            # Game description - truncate if too long
            description = game['description']
            if len(description) > 400:
                description = description[:400] + "..."
            story.append(Paragraph(description, styles['body']))
            story.append(Spacer(1, 3))
            
            # Skills and ages on same line to save space
            skills_ages = f"<b>Skills:</b> {game['skills'][:60]}{'...' if len(game['skills']) > 60 else ''} | <b>Ages:</b> {game['ages']}"
            story.append(Paragraph(skills_ages, styles['game']))
            
            # Materials
            materials_text = "<b>Materials:</b> " + ", ".join(game['materials'][:3])  # Limit materials
            if len(game['materials']) > 3:
                materials_text += ", etc."
            story.append(Paragraph(materials_text, styles['game']))
            story.append(Spacer(1, 2))
            
            # Variations - limit to 2 for space
            story.append(Paragraph("<b>Variations:</b>", styles['game']))
            for variation in game['variations'][:2]:  # Limit to first 2 variations
                story.append(Paragraph(variation, styles['game']))
            story.append(Spacer(1, 2))
            
            # Learning benefits - truncate if too long
            benefits = game['learning_benefits']
            if len(benefits) > 150:
                benefits = benefits[:150] + "..."
            story.append(Paragraph(f"<b>Benefits:</b> {benefits}", styles['game']))
            
            story.append(Spacer(1, 8))
        
        # Quick Tips section
        story.append(Spacer(1, 15))
        story.append(Paragraph("Quick Tips for Success", styles['section']))
        story.append(Spacer(1, 8))
        
        for category, tips in quick_tips.items():
            story.append(Paragraph(f"<b>{category}</b>", styles['body']))
            story.append(Spacer(1, 2))
            for tip in tips:
                story.append(Paragraph(tip, styles['game']))
            story.append(Spacer(1, 6))
        
        # Footer
        story.append(Spacer(1, 15))
        footer_text = """
        <i>Remember: The best math game is one that your child enjoys and wants to play again. Don't worry about perfection – focus on engagement, exploration, and building positive associations with mathematics.</i>
        """
        story.append(Paragraph(footer_text, styles['body']))
        
        # Build PDF
        doc.build(story)
        print(f"PDF created successfully: {filename}")
        return filename

def main():
    """Main function to generate the PDF"""
    games = QuickMathGames()
    filename = games.create_pdf()
    
    # Check if file was created successfully
    if os.path.exists(filename):
        print(f"\n✅ Success! Your Quick Math Games Guide has been created as '{filename}'")
        print(f"📄 File size: {os.path.getsize(filename)} bytes")
        print("\n📋 What's included in your guide:")
        print("   • 8 detailed math games with variations")
        print("   • Materials lists and setup instructions") 
        print("   • Age-appropriate skill development focus")
        print("   • Quick tips for successful implementation")
        print("   • Professional formatting with purple and blue theme")
    else:
        print("❌ Error: PDF file was not created successfully")

if __name__ == "__main__":
    main()