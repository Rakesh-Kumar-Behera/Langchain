from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template= """Please summarize the research paper titled "{selected_paper}" with the following 
specifications: 
Explanation Style: {selected_style} 
Explanation Length: {selected_input_length} 
1. Mathematical Details: 
- Include relevant mathematical equations if present in the paper. 
- Explain the mathematical concepts using simple, intuitive code snippets where applicable. 
2. Analogies: 
-Use relatable analogies to simplify complex ideas. 
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing. 
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
    input_variables=["selected_paper", "selected_style", "selected_input_length"],
    validate_template=True, # Ensure the template is valid, or the variables are correctly set
)

template.save("prompt_template.json") # Save the template to a file
# template.save("prompt_template.yaml") # Save the template to a file
