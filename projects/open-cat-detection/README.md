# Open Cat Detection Mini-Project v1

**Task:** 2D object detection using bounding boxes  
**Class:** `cat` (single class)  
**Images:** 30 Wikimedia Commons files  
**Format:** COCO JSON + Label Studio task JSON + CSV  
**Status:** Draft annotation package — full-resolution human QA still required

## Scope
This is an independently created portfolio exercise. It is not an Innodata or client dataset, and it does not reproduce any employer's proprietary task guide. The images are sourced individually from Wikimedia Commons. The `images_manifest.csv` records the original file page, creator/attribution, licence, licence URL, direct image URL and dimensions for every image.

The annotations in this release are **draft boxes** estimated during visual review of the source images. They have been checked for structural validity (image bounds, positive dimensions, unique IDs and valid category references), but have **not** received a full-resolution correction pass inside a live CVAT/Label Studio session. Do not describe this release as fully adjudicated gold-standard data.

## Annotation policy
1. Label every visually distinguishable domestic cat. Use one rectangle per cat.
2. Draw a tight axis-aligned box around the visible extent of the cat. Include ears, tail and paws when visible and clearly part of the same animal.
3. For partial occlusion or truncation, box only the visible portion. Do not extend a box behind an obstruction or beyond the image boundary.
4. For overlapping cats, use separate boxes when individual animals can be distinguished. Boxes may overlap.
5. Do not label toys, people, furniture, other animals, shadows or cat-shaped objects.
6. If the image is too ambiguous to establish that an object is a cat, flag it for review rather than guessing.
7. One class only: `cat`. Do not infer breed, age, colour, pose or identity.

## Package contents
- `images_manifest.csv` — image-by-image attribution and licence record.
- `annotations_coco.json` — COCO object-detection annotations and source metadata.
- `annotations_boxes.csv` — flat, human-readable annotation table in pixel coordinates.
- `label_studio_tasks.json` — Label Studio tasks with draft predictions and remote image URLs.
- `label_config.xml` — Label Studio interface config.
- `download_images.py` — downloads originals into `images/` using the manifest.
- `preview.html` — visual review page with image overlays (requires an internet connection).
- `qa_report.md` — structural QA results, limitations and human review checklist.

## Use in Label Studio
1. Install and start Label Studio on your computer.
2. Create a project and use the XML in `label_config.xml` as the labeling interface.
3. Import `label_studio_tasks.json`. It contains remote `data.image` URLs and pre-annotation predictions. If remote images are blocked by your setup, run `python download_images.py` and change the task image references to local storage URLs or upload the images to the project.
4. Review every prediction at full resolution. Correct boxes, add missed cats, remove false positives, then convert the reviewed predictions to final annotations in the project.

## Use in CVAT
1. Download the originals with `python download_images.py`.
2. Create a CVAT task with label `cat` and upload the files in `images/`.
3. Import `annotations_coco.json` as COCO 1.0 annotations. If the CVAT version expects an archive, zip the `images/` directory and the COCO JSON in its required import layout.
4. Inspect and correct every box before using the dataset.

## Download the images
Run from this folder: `python download_images.py`. The script uses the direct Wikimedia Commons upload URLs from the manifest and preserves filenames. It does not change the source images. Network access is required.

## Reuse and attribution
Image copyright and reuse terms are determined by each individual Commons file page, not by this project. Check the file page before redistribution. Preserve attribution and comply with each listed licence. Several images use CC BY-SA, which can require attribution and share-alike terms for adaptations; two images use CC BY 2.0; one is marked public domain. Do not replace the per-image licence with a blanket dataset licence. The original images are not bundled in this ZIP; only metadata and links are included.

## Suggested public repository title
`open-cat-detection-mini-project`