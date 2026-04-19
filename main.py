import textwrap

matn = "Bu matn uzunligi 80 belgiga mos ravishda qatorlarga bo'lishi kerak."
qatorlar = textwrap.wrap(matn, 80)

for qator in qatorlar:
    print(qator)
