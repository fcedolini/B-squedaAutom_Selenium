import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ----------------- Ventana Buscar Mercado Libre ------------------


# Configurar opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# Ejecutar sin abrir la ventana del navegador
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.89 Safari/537.36")


# Función para abrir enlaces en el navegador
def abrir_link(event):
    index = resultados_text.index(tk.CURRENT)
    for tag in resultados_text.tag_names(index):
        if tag.startswith("link_"):
            webbrowser.open(tag.split("_")[1])


# Función para buscar en Mercado Libre
def buscar_producto():
    producto = entrada_producto.get()
    if not producto:
        messagebox.showerror("Error", "Por favor, ingrese un producto.")
        return

    # Configurar Selenium
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    try:
        # Ir a Mercado Libre
        driver.get("https://www.mercadolibre.com.ar/")

        # Esperar el campo de búsqueda e ingresar el producto
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[name='as_word']"))
        )
        search_box.send_keys(producto)

        # Hacer clic en el botón de búsqueda
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.nav-search-btn"))
        )
        search_button.click()

        try:
            # Esperar hasta que los productos estén cargados
            WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, './/div[@class="ui-search-result__wrapper"]'))
            )

            # Limpiar resultados anteriores
            resultados_text.config(state=tk.NORMAL)
            resultados_text.delete(1.0, tk.END)

            # Obtener todos los productos
            productos = driver.find_elements(
                By.XPATH, './/div[@class="ui-search-result__wrapper"]')

            # Extraer los últimos 10 productos
            for i, producto in enumerate(productos[-10:]):
                try:
                    # Extraer título
                    titulo_element = producto.find_element(
                        By.XPATH, './/h3[@class="poly-component__title-wrapper"]')
                    titulo = titulo_element.text

                    # Extraer precio
                    entero_element = producto.find_element(
                        By.XPATH,
                        './/div[@class="poly-price__current"]//span[@class="andes-money-amount andes-money-amount--cents-superscript"]//span[@class="andes-money-amount__fraction"]'
                    )
                    entero = entero_element.text
                    precio = f"$ {entero}"

                    # Extraer link
                    link_element = producto.find_element(
                        By.XPATH, './/div[@class="poly-card__content"]//h3[@class="poly-component__title-wrapper"]//a'
                    )
                    link_url = link_element.get_attribute("href")

                    # Insertar resultados en el ScrolledText
                    resultados_text.insert(
                        tk.END, f"{i+1}. Artículo: ", "titulo")
                    resultados_text.insert(tk.END, f"{titulo}\n", "titulo")
                    resultados_text.insert(tk.END, "    Precio: ", "normal")
                    resultados_text.insert(tk.END, f"{precio}\n", "precio")
                    resultados_text.insert(tk.END, "    ", "normal")

                    # Insertar link con una etiqueta única
                    link_tag = f"link_{link_url}"
                    resultados_text.insert(
                        tk.END, "Compralo ya mismo haciendo click acá!!\n\n", link_tag)

                    # Configurar la etiqueta para que sea clickeable
                    resultados_text.tag_configure(link_tag, font=(
                        "Arial", 11, "italic"), foreground="green")
                    resultados_text.tag_bind(
                        link_tag, "<Button-1>", abrir_link)

                except Exception as e:
                    print(f"Error al procesar el producto {i+1}: {e}")

            resultados_text.config(state=tk.DISABLED)

        except Exception as e:
            print(f"Error al obtener los productos: {e}")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener los datos: {e}")

    finally:
        driver.quit()  # Cerrar el navegador


# Func para poder llamarla desde main
def buscar_mercado():
    global entrada_producto, resultados_text
    # Crear la interfaz gráfica con Tkinter
    ventana = tk.Tk()
    ventana.title("Buscador de Mercado Libre")
    ventana.geometry("700x650")
    ventana.config(bg="#3498db")

    tk.Label(ventana, text="Ingrese el producto a buscar:",
             font=("Arial", 12)).pack(pady=5)
    entrada_producto = tk.Entry(ventana, width=50, font=("Arial", 12))
    entrada_producto.pack(pady=5)

    tk.Button(ventana, text="Buscar", command=buscar_producto,
              font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

    # Crear ScrolledText con estilos
    resultados_text = scrolledtext.ScrolledText(
        ventana, width=80, height=30, font=("Arial", 11))
    resultados_text.pack(pady=5)

    # Configurar estilos en ScrolledText
    resultados_text.tag_configure("titulo", font=(
        "Arial", 12, "bold"), foreground="blue")
    resultados_text.tag_configure("precio", font=("Arial", 11))
    resultados_text.tag_configure("normal", font=("Arial", 11))

    ventana.mainloop()
