def main(s: str):
    res = {}
    s = s.replace(" ", "")
    s = s.replace("\n", "")
    s = s.replace("<sect>", "")
    s = s.replace("</sect>", "")
    s = s.replace("<data>auto#", "")
    s = s.replace("</data>", "")
    s = s.replace("=:", ",=:")
    s = s.replace(".;", "=:")
    counter = 0
    for el in s.split("=:"):
        if counter == 2:
            res[key] = value
            counter = 0
        if "," in el:
            value = int(el.replace(",", ""))
            counter += 1
        else:
            key = el
            counter += 1
    return res
