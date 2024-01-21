from shiny import App, render, ui, reactive
import asyncio
from pathlib import Path
from engine import process

# set image directory
www_dir = Path(__file__).parent / "www"

app_ui = ui.page_fillable(
    {"style": "background-color: rgba(0, 128, 255, 0.1)"},
    ui.row(
        ui.column(12,
            # outer perimiter
            ui.card(
                ui.row(
                    ui.column(3, 
                        # navigation bar
                        ui.card({"style": "background-color: #c1c6fc"},
                            ui.row(
                                ui.column(12, ui.card(
                                    ui.img(src="logo.png", )
                                )),
                                ui.column(12, ui.card(
                                    # description or instructions
                                    ui.markdown("""
                                                <h4>Make memorizing diagrams or maps a breeze!</h4>
                                                
                                                <h6>Simply upload an image in .png, .jpeg, or .jpg format and start quizzing yourself</h6>
                                                """),
                                    # lets user upload files
                                    ui.input_file("inputImage", "Choose your diagram!", accept=[".png", ".jpeg", ".jpg"], multiple=False,
                                                  button_label='Browse...', placeholder='None chosen', capture=None),
                                    # used to submit, if not functions will run regardless
                                    ui.input_action_button("submit", "Submit", class_="btn-primary")
                                    )
                                    
                                    )
                            )
                        )
                    ),
                    ui.column(9,
                              ui.card(ui.card(
                                        ui.output_text_verbatim("printout", placeholder=True))
                                      )
                                      
                              )
                                
                )
            )
        )
    )
)


def server(input, output, session):
    # will need to eventually replace with the matlab stuff
    @reactive.Calc
    @reactive.event(input.submit)
    def pathToMathlab():
        path = input.inputImage()[0].get("datapath")        
        dict = {}
        dict.update({"path": path})
        dict.update({"export": "static\images"})

        process(dict)
    
    
    @output
    @render.text
    @reactive.event(input.submit)
    async def printout():
        input.submit()
        await asyncio.sleep(1)

        with reactive.isolate():
            return input.inputImage()[0].get("datapath")
        


app = App(app_ui, server, static_assets=www_dir)
