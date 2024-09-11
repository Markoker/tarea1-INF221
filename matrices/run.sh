mkdir -p dataset
mkdir -p dataset/resultados
mkdir -p dataset/resultados/cuadradas
mkdir -p dataset/resultados/rectangulares

echo "Ejecutando programas..."
echo "Strassen para matrices cuadradas"
./programas/strassen "dataset/matrices_cuadradas.txt" > "dataset/resultados/cuadradas/strassen.csv"

echo "Algoritmo simple para matrices cuadradas"
./programas/simple "dataset/matrices_cuadradas.txt" > "dataset/resultados/cuadradas/simple.csv"
echo "Algoritmo simple para matrices rectangulares"
./programas/simple "dataset/matrices_rectangulares.txt" > "dataset/resultados/rectangulares/simple.csv"

echo "Algoritmo simple optimizado para matrices cuadradas"
./programas/transpuesta "dataset/matrices_cuadradas.txt" > "dataset/resultados/cuadradas/transpuesta.csv"
echo "Algoritmo simple optimizado para matrices rectangulares"
./programas/transpuesta "dataset/matrices_rectangulares.txt" > "dataset/resultados/rectangulares/transpuesta.csv"


