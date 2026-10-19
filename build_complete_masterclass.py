# build_complete_masterclass.py
# Full generator for templates/url_shortener.html
import os
import sys
from pathlib import Path

# Import from modular generators
from gen_head import get_head_css, get_header_and_modal, get_deck_controls
from gen_slides_1_8 import get_slides_1_8
from gen_slides_9_16 import get_slides_9_16
from gen_slides_17_24 import get_slides_17_24
from gen_views_and_scripts import (
    get_reader_view, get_revision_view, get_flashcards_view,
    get_quiz_view, get_drawers_and_modals, get_scripts
)

OUT_FILE = Path("d:/Learning/Backend_Notes/templates/url_shortener.html")

def main():
    print("Writing url_shortener.html with full whiteboard diagrams & comprehensive content...")
    
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        # 1. HTML Head & CSS
        f.write(get_head_css())
        
        # 2. Header & Whiteboard Lightbox Modal
        f.write(get_header_and_modal())
        
        # 3. Main container start
        f.write("""
  <main class="container">
    <!-- =========================================================================
         VIEW 1: PRESENTATION (DECK CAROUSEL MODE - 24 SLIDES)
         ========================================================================= -->
    <section id="presentationView" class="presentation-deck">
""")
        
        # 4. Slides 1 to 24
        f.write(get_slides_1_8())
        f.write(get_slides_9_16())
        f.write(get_slides_17_24())
        
        # Close Presentation Deck section
        f.write("""
    </section>
""")

        # 5. Presentation deck controls
        f.write(get_deck_controls())
        
        # 6. Reader View
        f.write(get_reader_view())
        
        # 7. Revision View (with 4 Master Interview Questions & Key Numbers)
        f.write(get_revision_view())
        
        # 8. Flashcards View (8 cards)
        f.write(get_flashcards_view())
        
        # 9. Quiz View (10 questions)
        f.write(get_quiz_view())
        
        # Close Main container
        f.write("""
  </main>
""")

        # 10. Drawers & Modals
        f.write(get_drawers_and_modals())
        
        # 11. Scripts (Navigation, Simulator, Whiteboard Modal, Search, Notes)
        f.write(get_scripts())
        
        # Close body and html
        f.write("\n</body>\n</html>\n")
        
    print(f"Successfully generated {OUT_FILE}. File size: {OUT_FILE.stat().st_size} bytes.")

if __name__ == "__main__":
    main()
