# Minimal frame-driven component

This is a six-second silent example of a sensor signal becoming a visible
response. It illustrates deterministic animation; it is not a complete video
production, factual measurement, or standalone application.

1. Create a TypeScript Remotion project using the current official setup.
2. Copy `Demo.tsx` into its `src/` directory.
3. Import `Demo` into the root file that declares compositions and add:

```tsx
<Composition
  id="FahrezDemo"
  component={Demo}
  width={1080}
  height={1920}
  fps={30}
  durationInFrames={180}
/>
```

Keep existing imports/registration and import `Composition` from `remotion` if
needed. In a conventional project whose registered entry is `src/index.ts`:

```powershell
npx remotion studio src/index.ts
npx remotion render src/index.ts FahrezDemo out/demo.mp4
```

Use your actual entry path if it differs. Adapt the typography, imagery,
story, narration, and captions to your own brief. Inspect the exported result.

Reference: [Remotion's frame model](https://www.remotion.dev/docs/idea).
