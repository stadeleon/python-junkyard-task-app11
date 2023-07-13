from fpdf import FPDF


class ReceiptGenerator:
    def __init__(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font(family='Times', size=18, style="B")
        self.pdf = pdf

    def generate(self, order):
        self.pdf.cell(w=100, h=10, txt=f"Item# {order.article.id}", ln=1)
        self.pdf.cell(w=100, h=10, txt=f"Article: {order.article.name} X {order.quantity}", ln=1)
        self.pdf.cell(w=100, h=10, txt=f"Price: {order.article.price}", ln=1)
        self.pdf.cell(w=100, h=10, txt=f"Total: {order.article.price * order.quantity}", ln=1)

        self.pdf.output(str(order.article.id) + '.pdf')
