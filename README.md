# Financial Data Extractor

Extractor de datos financieros desde documentos PDF. Esta herramienta está diseñada para procesar estados financieros y extraer información específica basada en códigos contables predefinidos.

## 🔍 Funcionalidades Detalladas

### Extracción de Datos
- Lectura automática de PDFs
- Identificación de códigos contables
- Extracción de montos financieros
- Validación de datos extraídos

### Procesamiento
- Conversión de texto a valores numéricos
- Categorización automática
- Limpieza de datos extraídos

## ⚙️ Dependencias Principales

- PyMuPDF (fitz) para procesamiento de PDFs
- PyPDF2 para extracción de texto
- pandas para manejo de datos
- numpy para operaciones numéricas

## 🔒 Manejo de Errores

El extractor incluye manejo de errores para:
- Archivos PDF no encontrados
- Errores de lectura de PDF
- Formatos de archivo inválidos
- Datos malformados o faltantes

### Categorías Soportadas

El extractor busca las siguientes categorías financieras:
- INGRESOS OPERACIONALES (51000)
- COSTOS (41000)
- Gastos de Comercialización (42200)
- Gastos Administrativos (42100)
- Otros Ingresos (52200)
- Y otras categorías definidas en `CATEGORIES`

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo `LICENSE` para más detalles.

## ✨ Agradecimientos

- PyMuPDF por su excelente biblioteca de procesamiento de PDFs
- Pandas por el manejo eficiente de datos
- La comunidad de Python por sus contribuciones


