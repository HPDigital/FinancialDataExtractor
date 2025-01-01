import fitz  # PyMuPDF
import pandas as pd
import re
import PyPDF2
from typing import Dict, Optional
from pathlib import Path

class FinancialDataExtractor:
    """Clase para extraer datos financieros de documentos PDF."""
    
    CATEGORIES = {
        "INGRESOS OPERACIONALES": "51000",
        "COSTOS": "41000",
        "Gastos de Comercialización": "42200",
        "Gastos Administrativos": "42100",
        "Otros Ingresos": "52200",
        "Rendimiento por Inversiones": "52100",
        "Cargos por diferencia d ecambio": "43300",
        "Otros Egresos": "43200",
        "Ajuste por inflación y tenencia de bienes": "43100",
        "Ingresos de gestiones anteriores": "53000",
        "Gastos de gestiones anteriores": "44000",
        "Ingresos extraordianearios": "54000",
        "Gastos extraordianarios": "45000",
        "Gastos Financieros": "46000",
        "Impuesto a las Utilidades de las Empresas": "47000"
    }

    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        """
        Extrae el texto completo de un archivo PDF.
        
        Args:
            file_path: Ruta al archivo PDF.
            
        Returns:
            str: Texto extraído del PDF.
            
        Raises:
            FileNotFoundError: Si el archivo no existe.
            PyPDF2.PdfReadError: Si hay error al leer el PDF.
        """
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                return " ".join(page.extract_text() for page in reader.pages)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {file_path}")
        except PyPDF2.PdfReadError as e:
            raise PyPDF2.PdfReadError(f"Error al leer el PDF: {str(e)}")

    @classmethod
    def parse_financial_data(cls, text: str) -> Dict[str, int]:
        """
        Analiza el texto extraído para encontrar datos financieros.
        
        Args:
            text: Texto extraído del PDF.
            
        Returns:
            Dict[str, int]: Diccionario con categorías y valores encontrados.
        """
        results = {}
        lines = text.splitlines()
        
        for category, code in cls.CATEGORIES.items():
            pattern = rf"{code}.*?{re.escape(category)}.*?([\d,]+)(?=\s|$)"
            
            for line in lines:
                if match := re.search(pattern, line):
                    try:
                        results[category] = int(match.group(1).replace(',', ''))
                        break
                    except ValueError:
                        results[category] = 0
            else:
                results[category] = 0
                
        return results

    @classmethod
    def extract_financial_data(cls, file_path: str) -> pd.DataFrame:
        """
        Extrae datos financieros de un PDF y los devuelve como DataFrame.
        
        Args:
            file_path: Ruta al archivo PDF.
            
        Returns:
            pd.DataFrame: DataFrame con los datos financieros extraídos.
        """
        # Validar que el archivo existe y es un PDF
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"No se encontró el archivo: {file_path}")
        if path.suffix.lower() != '.pdf':
            raise ValueError("El archivo debe ser un PDF")

        # Extraer y procesar datos
        text = cls.extract_text_from_pdf(file_path)
        results = cls.parse_financial_data(text)
        
        return pd.DataFrame([results])

def main():
    """Función principal para ejecutar el extractor."""
    try:
        pdf_path = r"C:\Users\HP\Downloads\202312_CMI_EEFF_ER.pdf"
        extractor = FinancialDataExtractor()
        df = extractor.extract_financial_data(pdf_path)
        print("Datos extraídos exitosamente:")
        print(df)
        return df
    except Exception as e:
        print(f"Error durante la extracción: {str(e)}")
        return None

if __name__ == "__main__":
    main()
