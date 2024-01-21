from shiny import App, render, ui, reactive

app_ui = ui.page_fillable(
    ui.row(
        ui.column(12, 
            ui.card("Width 12",
                ui.row(
                    ui.column(3,
                        ui.card("Width 3",
                            ui.row(
                                ui.column(12, ui.card("Width 12")),
                                ui.column(12, ui.card(
                                    ui.input_file("inputImage", "Choose your diagram!", accept=[".png", ".jpeg", ".jpg"], multiple=False,
                                                  button_label='Browse...', placeholder='None chosen', capture=None))
                                    )
                            )
                        )
                    ),
                    ui.column(9,
                              ui.card("width 9"),
                              ui.card("width 9"),
                              ui.card("width 9")
                              )
                                
                )
            )
        )
    )
)


def server(input, output, session):
    @reactive.Calc
    def pathToMathlab():
        path = input.inputImage()[0].get("datapath")
        return path
        


app = App(app_ui, server)
