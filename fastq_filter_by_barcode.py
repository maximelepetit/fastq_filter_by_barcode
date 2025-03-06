import argparse
import os
import gzip

def filter_fastq_by_barcodes(r1_file, r2_file, barcode_file, output_dir, filtered_r1, filtered_r2, barcode_length):
    # Charger la liste des barcodes valides dans un set pour un accès rapide
    with open(barcode_file, 'r') as f:
        barcodes = set(line.strip() for line in f)

    # Assurer que le dossier de sortie existe, sinon le créer
    os.makedirs(output_dir, exist_ok=True)

    # Chemins complets pour les fichiers de sortie
    output_r1 = os.path.join(output_dir, filtered_r1)
    output_r2 = os.path.join(output_dir, filtered_r2)

    # Ouvrir les fichiers d'entrée et de sortie (gzip)
    with gzip.open(r1_file, 'rt') as r1, gzip.open(r2_file, 'rt') as r2, \
         gzip.open(output_r1, 'wt') as out_r1, gzip.open(output_r2, 'wt') as out_r2:


        while True:
            # Lire un bloc de 4 lignes pour chaque read (R1 et R2)
            r1_lines = [r1.readline().strip() for _ in range(4)]
            r2_lines = [r2.readline().strip() for _ in range(4)]

            # Si nous avons atteint la fin de l'un des fichiers, sortir
            if not r1_lines[0] or not r2_lines[0]:
                break


            # Extraire le barcode de R1
            r1_barcode = r1_lines[1][:barcode_length]
            r2_barcode = r2_lines[1][:barcode_length]	
            # Filtrer les reads en fonction du barcode
            if r1_barcode in barcodes:
                out_r1.write("\n".join(r1_lines) + "\n")
                out_r2.write("\n".join(r2_lines) + "\n")


def main():
    # Initialisation du parser d'arguments
    parser = argparse.ArgumentParser(description="Filtrer les reads FASTQ en fonction d'une liste de barcodes.")

    # Définition des arguments
    parser.add_argument('r1_file', type=str, help="Fichier d'entrée R1 (fastq.gz)")
    parser.add_argument('r2_file', type=str, help="Fichier d'entrée R2 (fastq.gz)")
    parser.add_argument('barcode_file', type=str, help="Fichier contenant les barcodes valides (un par ligne)")
    parser.add_argument('output_dir', type=str, help="Dossier de sortie pour les fichiers filtrés")
    parser.add_argument('filtered_r1', type=str, help="Nom du fichier de sortie R1 (fastq.gz)")
    parser.add_argument('filtered_r2', type=str, help="Nom du fichier de sortie R2 (fastq.gz)")
    parser.add_argument('--barcode_length', type=int, required=True, help="Longueur du barcode")

    # Analyse des arguments
    args = parser.parse_args()

    # Appel de la fonction principale
    filter_fastq_by_barcodes(
        args.r1_file,
        args.r2_file,
        args.barcode_file,
        args.output_dir,
        args.filtered_r1,
        args.filtered_r2,
        args.barcode_length
    )

if __name__ == '__main__':
    main()
