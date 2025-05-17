# FHE-based Biological Age Predictor

This app securely estimates biological age from DNA methylation data using Fully Homomorphic Encryption (FHE). It integrates R (Horvath Clock) with Concrete ML for privacy-preserving inference.

## Upload Format
- CSV file with samples as rows and CpG sites as columns (beta matrix).

## Outputs
- Predicted biological ages via encrypted (FHE) inference.

## Credits
- Horvath Clock via `dnaMethyAge` R package
- FHE via `concrete-ml`