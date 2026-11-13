# Prompts that produce concrete deliverables

Replace bracketed values with the actual project. State the result, constraints, and verification; let the agent inspect the implementation details.

## New UI

```text
Use $fahrez-ui-build to build [surface] for [audience]. The primary task is
[action and result]. Work in this repository's existing stack. Use [content
or data source], and label sample data. Follow [brand direction]. Implement
the primary journey and necessary failure/empty states. Inspect desktop
and phone layouts and report the checks that actually ran.
```

## UI repair

```text
Use $fahrez-ui-review on [page/URL]. Focus on [observed problem]. Reproduce
it, fix the cause, and inspect the affected journey at [viewports]. Preserve
the established design system. Report user impact and remaining limits.
```

## Product video

```text
Use $fahrez-video-production. Make a [duration] [aspect ratio] film for
[product], showing [specific real action]. Use [assets] and [language].
The visual direction is [direction]. Deliver editable source, final MP4,
requested captions, thumbnail, and a verification note. Inspect the exact
final file and clearly identify illustrative or generated material.
```

## Indonesian educational explainer

```text
Gunakan $fahrez-video-production untuk membuat video vertikal berbahasa
Indonesia tentang [topik] untuk [audiens], sekitar [durasi]. Jelaskan lewat
satu contoh konkret. Periksa klaim penting melalui sumber utama, lalu buat
naskah, storyboard, narasi, visual, dan subtitle. Gunakan aset yang tersedia
secara sah. Serahkan proyek yang bisa diedit dan MP4 final yang sudah
ditonton serta didengarkan, dengan catatan pemeriksaan yang sebenarnya.
```

## Continue a saved project

```text
Use $fahrez-creative-tools and continue the saved project at [path]. First
inspect its actual state and available commands. Complete [remaining work],
save the editable project, export [format], and verify the resulting file.
If the GUI has unsaved changes that the integration cannot read, reconcile
that state before editing the disk project.
```
