mkdir -p data

mkdir -p data/nearly_sorted
mkdir -p data/rev_sorted
mkdir -p data/unsorted
mkdir -p data/sorted

echo "Nearly sorted..."
echo "Merge sort..."
./programas/merge_sort data/nearly_sorted.txt > data/nearly_sorted/merge_sort.csv
echo "Quick sort..."
./programas/quick_sort data/nearly_sorted.txt > data/nearly_sorted/quick_sort.csv
echo "Funcion implementada..."
./programas/funcion_implementada data/nearly_sorted.txt > data/nearly_sorted/funcion_implementada.csv
echo "Selection sort..."
./programas/selection_sort data/nearly_sorted.txt > data/nearly_sorted/selection_sort.csv

echo "Reverse sorted..."
echo "Merge sort..."
./programas/merge_sort data/rev_sorted.txt > data/rev_sorted/merge_sort.csv
echo "Quick sort..."
./programas/quick_sort data/rev_sorted.txt > data/rev_sorted/quick_sort.csv
echo "Funcion implementada..."
./programas/funcion_implementada data/rev_sorted.txt > data/rev_sorted/funcion_implementada.csv
echo "Selection sort..."
./programas/selection_sort data/rev_sorted.txt > data/rev_sorted/selection_sort.csv

echo "Unsorted..."
echo "Merge sort..."
./programas/merge_sort data/unsorted.txt > data/unsorted/merge_sort.csv
echo "Quick sort..."
./programas/quick_sort data/unsorted.txt > data/unsorted/quick_sort.csv
echo "Funcion implementada..."
./programas/funcion_implementada data/unsorted.txt > data/unsorted/funcion_implementada.csv
echo "Selection sort..."
./programas/selection_sort data/unsorted.txt > data/unsorted/selection_sort.csv

echo "Sorted..."
echo "Merge sort..."
./programas/merge_sort data/sorted.txt > data/sorted/merge_sort.csv
echo "Quick sort..."
./programas/quick_sort data/sorted.txt > data/sorted/quick_sort.csv
echo "Funcion implementada..."
./programas/funcion_implementada data/sorted.txt > data/sorted/funcion_implementada.csv
echo "Selection sort..."
./programas/selection_sort data/sorted.txt > data/sorted/selection_sort.csv

