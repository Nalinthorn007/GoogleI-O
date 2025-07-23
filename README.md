# Set up uv package, Please following step by step

1. install set up uv by following this website https://docs.astral.sh/uv/
   
   1.1 if user use windows, please use command below <strong>(Run in PowerShell)<strong>
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
   
   1.2 if user use macOS, please use command below  <strong>(Run in Terminal)<strong>
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh

   ```

2. uv python install 3.12  <strong>(Run in PowerShell / Run in Terminal) <strong>

3. check uv if it used to install ?  uv --version <strong>(Run in PowerShell / Run in Terminal) <strong>

4. create your project folder by choosing your path that you need to create

5. cd your folder path and then `uv init [name]` example: `uv init demoGoogle`

6. `cd demoGoogle`

7. `uv venv`

8. `.venv\Scripts\activate` 

9. Use Markdown Editor for Chrome™ or file run_markdown.ipynb for looking the result, How to install 


# The Libraries that you need to install in uv 
`uv add jupyter ipykernel markdown langgraph typing_extensions dotenv langchain langchain_community openai langchain_groq arxiv wikipedia`


# Until now, You’ve successfully followed the setup guide. Enjoy your experiment! 😉
