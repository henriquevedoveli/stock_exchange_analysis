def convert_to_float(cell):
    try:
        cell = cell.replace(',', '').replace('%', '')
        cell = cell.replace('.', '').replace(',', '.')
        return float(cell)
    except ValueError:
        return cell
