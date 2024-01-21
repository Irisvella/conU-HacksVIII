from shiny import App, render, ui, reactive

app_ui = ui.page_fillable(
    ui.row(
        ui.column(12, 
            ui.card("Outer",
                ui.row(
                    ui.column(3,
                        ui.card("Navbar",
                            ui.row(
                                ui.column(12, ui.card("probably logo")),
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
                              ui.card("top display", 
                                      ui.output_text_verbatim("printout")),
                              ui.card("main image"),
                              ui.card("navigation buttons")
                              )
                                
                )
            )
        )
    )
)


def server(input, output, session):
    @reactive.Calc
    def pathToMathlab():
        while type(input.inputImage) != 'NoneType':
            path = input.inputImage()[0].get("datapath")
            return path
        else:
            return "not done yet"
    
    @output
    @render.text
    def printout():
        return input.inputImage()[0].get("datapath")
        #return f'the temp path of the image is {pathToMathlab()}'
        


app = App(app_ui, server)
