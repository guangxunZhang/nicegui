from nicegui import ui
import random

FEMINIST_WORKS = {
    'Paris is Burning': {
        'author': 'a',
        'year': 1111,
        'description': 'good',
        'themes': ['ball', 'LGBTQ+ rights', 'Social justice']
    },
        'Paris is Burning2': {
        'author': 'a',
        'year': 1111,
        'description': 'good',
        'themes': ['ball', 'LGBTQ+ rights', 'Social justice']
    },
        'Paris is Burning3': {
        'author': 'a',
        'year': 1111,
        'description': 'good',
        'themes': ['ball', 'LGBTQ+ rights', 'Social justice']
    },
    'Paris is Burning4': {
        'author': 'a',
        'year': 1111,
        'description': 'good',
        'themes': ['ball', 'LGBTQ+ rights', 'Social justice']
    }
}

def generate_fancy_patterns():
    seed1 = random.randint(1, 10000)
    seed2 = random.randint(1, 10000)
    seed3 = random.randint(1, 10000)
    return [
        f'https://picsum.photos/seed/pattern{seed1}/800/300',
        f'https://picsum.photos/seed/abstract{seed2}/800/250',
        f'https://picsum.photos/seed/art{seed3}/800/200'
    ]

@ui.page('/')
def main_page():
    ui.colors(primary='#8B4789')
    
    with ui.header().classes('items-center justify-between'):
        ui.label('Feminist Literature & Language Analysis').classes('text-2xl font-bold')
    
    with ui.column().classes('w-full max-w-6xl mx-auto p-4 gap-4'):
        
        with ui.card().classes('w-full'):
            ui.label('Feminist Literature Archive').classes('text-xl font-bold mb-2')
            ui.label('Explore key works in feminist literature and analyze their language patterns.').classes('text-gray-600')
        
        with ui.card().classes('w-full'):
            ui.label('Key Feminist Works').classes('text-lg font-bold mb-4')
            
            for title, info in FEMINIST_WORKS.items():
                with ui.expansion(title, icon='book').classes('w-full'):
                    with ui.column().classes('gap-2 p-2'):
                        ui.label(f"Author: {info['author']}").classes('font-semibold')
                        ui.label(f"Published: {info['year']}").classes('text-sm text-gray-600')
                        ui.markdown(f"**Description:** {info['description']}")
                        
                        ui.label('Key Themes:').classes('font-semibold mt-2')
                        with ui.row().classes('gap-2 flex-wrap'):
                            for theme in info['themes']:
                                ui.badge(theme, color='purple')
        
        with ui.card().classes('w-full'):
            ui.image('https://picsum.photos/800/200').classes('w-full rounded mb-4')
            
            text_input = ui.textarea(
                label='Text to Analyze',
                placeholder='Paste your text here...'
            ).classes('w-full').props('rows=6')
            
            result_container = ui.column().classes('w-full gap-2')
            
            def perform_analysis():
                result_container.clear()
                text = text_input.value
                
                if not text or not text.strip():
                    with result_container:
                        ui.label('Please enter some text to analyze.').classes('text-orange-600')
                    return
                
                patterns = generate_fancy_patterns()
                
                with result_container:
                    for pattern_url in patterns:
                        ui.image(pattern_url).classes('w-full rounded mb-2')
            
            with ui.row().classes('gap-2'):
                ui.button('Analyze Text', on_click=perform_analysis, icon='analytics').props('color=primary')
                ui.button('Clear', on_click=lambda: (text_input.set_value(''), result_container.clear()), icon='clear')
        
        with ui.card().classes('w-full'):
            ui.label('About Feminist Literary Analysis').classes('text-lg font-bold mb-2')
            ui.markdown('''
            Feminist literary analysis examines how literature reinforces or undermines the economic, political, 
            social, and psychological oppression of women. Key aspects include:
            ''')

ui.run(title='Feminist Literature Analysis', dark=None)
