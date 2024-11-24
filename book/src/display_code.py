from IPython.display import display, HTML
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def exec_and_display_code_with_line_numbers(file_path):
    """Executes a Python file and displays its code with line numbers and syntax highlighting."""
    
    # Read the code from the file
    with open(file_path, 'r') as file:
        code_content = file.read()

    # Highlight the code using Pygments
    formatter = HtmlFormatter()
    highlighted_code = highlight(code_content, PythonLexer(), formatter)

    # Create line numbers
    line_count = code_content.count('\n') + 1  # Count lines for line numbering

    # Combine line numbers and the highlighted code into a single HTML structure
    line_numbers_html = ''.join(f'<span>{i}</span><br>' 
                                 for i in range(1, line_count + 1))

    # CSS styling
    combined_code = f"""
    <style>
        .codehilite {{
            display: flex;
            font-family: monospace; /* Monospace font for code */
            font-size: 24px;
        }}
        .line-numbers {{
            flex: 0 0 40px; /* Width of the line numbers */
            padding-right: 10px;
            text-align: right;
            color: red;
            user-select: none;
            font-size: 24px;
        }}
        .highlighted-code {{
            flex-grow: 1;
            padding-top: 0;
            font-size: 24px;
        }}
    </style>
    <div class="codehilite">
        <div class="line-numbers">{line_numbers_html}</div>
        <div class="highlighted-code">{highlighted_code}</div>
    </div>
    """

    # Display the combined code with line numbers and syntax highlighting
    display(HTML(combined_code))
    
    # Execute the code
    exec(code_content)