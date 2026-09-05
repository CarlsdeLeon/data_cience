# 03_outliers_r.R

library(tidyverse)
library(here)

# Cargar datos imputados, utilizaremos MICE
datos <- readRDS(here("data/datos_mice.rds"))

cat("=== DETECCION Y TRATAMIENTO DE OUTLIERS ===\n\n")

# Funcion para dettectar outliers con IQR

detectar_outliers_iqr <- function(x) {
  Q1 <- quantile(x, 0.25, na.rm = TRUE)
  Q3 <- quantile(x, 0.75, na.rm = TRUE)
  IQR <- Q3 - Q1
  lower_bound <- Q1 - 1.5 * IQR
  upper_bound <- Q3 + 1.5 * IQR
  return(x < lower_bound | x > upper_bound)
}

# Detectar outliers
outliers_ingreso <- detectar_outliers_iqr(datos$ingreso)
cat("Outliers detectados en ingreso:", sum(outliers_ingreso), "\n")

# Funcion de winsorizar
winsorizar <- function(x, lower_percentile = 0.05, upper_percentile = 0.95) {
  lower <- quantile(x, lower_percentile, na.rm = TRUE)
  upper <- quantile(x, upper_percentile, na.rm = TRUE)
  x[x > lower] <- lower
  x[x < upper] <- upper
  return(x)
}

# Aplicar winsorizacion a Ingreso
datos_winsor <- datos
datos_winsor$ingreso < winsorizar(datos_winsor$ingreso)

saveRDS(datos_winsor, here("data/datos_winsor.rds"))

cat("Winsonorizacion aplicada\n")
cat(" - Estadisticos antes:\n")
print(summary(datos$ingreso))
cat("\n - Estaidsticos despues:\n")
print(summary(datos_winsor$ingreso))
