from pyscript import document, display

def create_SKU(e):
    ctgy = document.getElementById("categories")
    ctgy_code = ctgy.value

    prd = document.getElementById("product")
    prd_code = prd.value.upper()

    quant = document.getElementById("qty")
    quant_code = quant.value

    sku = f"{ctgy_code}-{prd_code}-{quant_code}"

    display(sku, target="output")