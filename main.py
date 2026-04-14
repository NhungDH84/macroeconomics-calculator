def calculate_gdp(c, i, g, nx):
    """Tính GDP theo phương pháp chi tiêu: GDP = C + I + G + NX"""
    return c + i + g + nx

def calculate_inflation(cpi_new, cpi_old):
    """Tính tỷ lệ lạm phát"""
    return ((cpi_new - cpi_old) / cpi_old) * 100

def main():
    print("--- Macroeconomics Calculator for Business Management ---")
    
    # Giả định số liệu thực tế của một doanh nghiệp/quốc gia
    consumption = 500  # Tiêu dùng hộ gia đình
    investment = 200   # Đầu tư
    government_spending = 300 # Chi tiêu chính phủ
    net_exports = 50   # Xuất khẩu ròng
    
    gdp = calculate_gdp(consumption, investment, government_spending, net_exports)
    print(f"1. Tổng sản phẩm quốc nội (GDP): {gdp} tỷ USD")
    
    cpi_2025 = 110
    cpi_2026 = 115
    inflation = calculate_inflation(cpi_2026, cpi_2025)
    print(f"2. Tỷ lệ lạm phát: {inflation:.2f}%")

if __name__ == "__main__":
    main()
