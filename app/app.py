from shiny import App, render, ui, reactive
import asyncio
from pathlib import Path
from engine import process
from shiny.types import ImgData

# set image directory
www_dir = Path(__file__).parent / "www"

app_ui = ui.page_fillable(
    {"style": "background-color: #ef959c"},
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
                                    ui.output_image("logo", width='100%')
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
                    ui.column(9,{"style": "background-color: #8da1b9"},
                              ui.card(ui.card(
                                        ui.output_image("display", height='500px'),
                                        ui.input_action_button("toggle", "Flip!"),
                                      )
                                      
                              )
                                
                )
            )
        )
    )
))


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

    x = reactive.Value("unmasked.png")
    @reactive.Effect
    @reactive.event(input.toggle)
    def _():
        x.set("masked.png")
    
    
    @output

    @render.image
    def logo():
        img: ImgData = {"src": str(dir /"logo.png")}
        return img
    
    @render.image
    @reactive.calc
    def display():
        img: ImgData = {"src": str(dir /x())}
        return img

    @render.text
    @reactive.event(input.submit)
    async def printout():
        input.submit()
        await asyncio.sleep(1)

        with reactive.isolate():
            return input.inputImage()[0].get("datapath")
        


app = App(app_ui, server, static_assets=www_dir)
