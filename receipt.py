from pyscript import document, display


def create_order(e):

    menu1 = document.getElementById("Menu1")
    menu2 = document.getElementById("Menu2")
    menu3 = document.getElementById("Menu3")
    menu4 = document.getElementById("Menu4")

    total = (
        float(menu1.value) * menu1.checked
        + float(menu2.value) * menu2.checked
        + float(menu3.value) * menu3.checked
        + float(menu4.value) * menu4.checked
    )

    display(
        f"Total: ₱{total:.2f}",
        target="result"
    )