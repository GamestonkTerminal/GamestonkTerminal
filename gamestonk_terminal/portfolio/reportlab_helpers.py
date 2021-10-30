"""Reportlab Helpers"""
__docformat__ = "numpy"

from datetime import datetime

from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph


def base_format(report: canvas.Canvas, header: str) -> None:
    """Applies a base page format to each page

    Parameters
    ----------
    report : canvas.Canvas
        The report to be formatted
    header : str
        The header for the page
    """
    report.setLineWidth(0.3)
    report.setFont("Helvetica", 12)
    report.drawString(30, 750, "Gamestonk Terminal")
    report.drawString(500, 750, datetime.now().strftime("%Y/%m/%d"))
    report.drawString(275, 725, "Annual Report")
    report.setFillColorRGB(255, 0, 0)
    report.drawString(200, 710, "Warning: currently only analyzes stocks")
    report.setFillColorRGB(0, 0, 0)
    report.line(50, 700, 580, 700)
    report.setFont("Helvetica", 20)
    report.drawString(50, 670, header)
    report.setFont("Helvetica", 12)


def draw_paragraph(
    report: canvas.Canvas, msg: str, x: int, y: int, max_width: int, max_height: int
) -> None:
    message_style = ParagraphStyle("Normal")
    message = msg.replace("\n", "<br />")
    message = Paragraph(message, style=message_style)
    _, h = message.wrap(max_width, max_height)
    message.drawOn(report, x, y - h)
