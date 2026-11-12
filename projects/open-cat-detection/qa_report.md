# QA Report — Open Cat Detection Mini-Project v1

**Date:** 12 November 2026  
**Scope:** 30 images, single class (`cat`), 2D bounding boxes  
**Status:** Structural QA passed; visual labels remain provisional

## Summary

| Metric | Result |
|---|---:|
| Source images | 30 |
| Classes | 1 (`cat`) |
| Bounding boxes | 41 |
| Images with more than one box | 6 |
| Unique source file pages recorded | 30 |
| Licence types recorded | 4 |

## Automated validation

- All image records have a unique integer ID.
- All annotation IDs are unique.
- Every annotation references an image ID present in the COCO `images` array.
- Every annotation references the defined `cat` category.
- Every box has positive width and height.
- Every box stays within the declared image dimensions.
- The CSV manifest has one source page, creator, licence and direct image URL per image.
- All source file page URLs are unique.

**Result:** PASS for structural checks.

## Visual review and limitations

The boxes were drafted from visual review of the linked Commons image previews and then converted to pixel coordinates using the declared dimensions. The annotation tool itself was not launched in this session, and the original image files were not downloaded into the build environment. Therefore, this release has not had a complete full-resolution box-tightness review, an independent second-annotator review, or adjudication of disagreements. Some difficult multi-cat scenes and edge-touching boxes may need adjustment.

This is a transparent portfolio pilot, not a validated training benchmark. The annotations should not be used to train, benchmark or make production claims until the human review checklist below is completed.

## Risks found / cases to inspect

1. **Small/distant cats:** confirm that the object is identifiable as a cat and that the box encloses the complete visible animal.
2. **Overlapping cats:** verify that each distinguishable animal has its own box and that no cat was merged or double-counted.
3. **Partial occlusion:** ensure boxes stop at the visible contour rather than extending behind a fence, box or another animal.
4. **Image-edge truncation:** allow a box to meet an image boundary when the animal is visibly cut off; do not invent unseen extent.
5. **Nearly full-frame animals:** tighten boxes to the visible cat contour; a full-frame box should remain only if the cat genuinely touches all relevant image edges.
6. **Multi-cat scene:** re-check the count and instance separation; crowded scenes carry the highest omission/duplication risk.

## Final human QA checklist

For each of the 30 images, a reviewer should mark: **Pass / Fix / Unclear** for each item.

- [ ] Every visible, distinguishable cat is labelled.
- [ ] No non-cat object is labelled.
- [ ] One instance has one box; no merged group boxes.
- [ ] Box is tight to the visible animal boundary.
- [ ] Occlusion and truncation are represented using visible extent only.
- [ ] Boxes remain inside image dimensions.
- [ ] Source attribution and licence are retained.
- [ ] Corrected annotations are exported again and re-run through structural validation.

## Release decision

**Current release:** suitable as a reproducible portfolio sample demonstrating annotation schema design, dataset documentation, provenance handling and preliminary QA.  
**Not yet suitable:** production model training, benchmark reporting, or claims of adjudicated annotation accuracy.

**Recommended next revision:** perform a full-resolution review in CVAT or Label Studio, document the reviewer/date, record per-image fixes, and issue `v1.1 — human-reviewed` only after all 30 images pass.