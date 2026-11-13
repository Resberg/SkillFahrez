# Make a UI from brief to working product

## 1. Define the job

Use the [UI brief](../templates/ui-brief.md). Identify who visits, what they need to do, what information supports that action, and how you will know it works. For a portfolio, the main task might be opening a relevant project and contacting its author. For a simulator, it might be changing an input and understanding the computed output.

Inspect an existing repository before selecting libraries. Reuse its routing, components, design tokens, and checks. For a new project, choose a stack appropriate to the interaction and hosting requirements; a static page often needs less than an application with accounts and stored data.

## 2. Make a design direction concrete

Write a small token table: background, surface, text, muted text, accent, border, type families, type scale, spacing, and container width. Choose one memorable feature grounded in the product: a real circuit diagram for an engineering project, for example. Give primary actions more emphasis than secondary details.

Sketch the order of information using real or explicitly marked sample content. Do not use fabricated testimonials or metrics as visual filler. Decide what simplifies or rearranges on small screens before implementing a wide layout.

### Use Framer University as a reference

Browse [Framer University Resources](https://framer.university/resources) for components, animations, effects, interactions, and websites. Its category and tag filters help narrow a search to the behavior you need. Examples on the page include text reveals, hover tooltips, scroll animations, and form submission states.

1. Choose a reference that supports the primary user task, and save its specific resource link in the UI brief.
2. Describe what you want to learn from it: trigger, initial state, movement, timing, final state, and feedback. Separate that behavior from the reference's branding and content.
3. Adapt the behavior to the project's stack and design system. A Framer component or override may require a new implementation in another framework.
4. Provide keyboard and touch behavior where relevant, and a reduced-motion alternative. Verify the result on a narrow screen as well as desktop.

Check the selected resource's terms before copying code or assets. This repository links to the library; it does not redistribute its components.

Example reference brief:

```text
Reference: https://framer.university/resources
Select a relevant form submission example and record its specific link.
Study its pending-to-success feedback, then implement that behavior in this
project's existing form using our typography and colors. Keep errors
recoverable, announce the result accessibly, and respect reduced motion.
```

## 3. Build the task and its states

Implement the central action all the way to its result. A contact control should open an actual contact route; a filter should change results. Add the states needed to make that action understandable: pending, success, error, empty, selected, disabled. Explain how to recover from errors beside the relevant field or action.

Use native elements where possible. Provide labels, accessible names, visible focus, sensible tab order, and text alternatives. Handle long titles, large values, missing images, and reduced motion. Keep sample data distinguishable from live data.

## 4. Inspect the rendered interface

Run the repository's preview command. At representative wide and narrow widths, check hierarchy, alignment, wrapping, clipping, image crops, and horizontal overflow. Try the primary task with keyboard and pointer. Inspect focus and validation feedback, not only the initial screen.

Use the [review checklist](../templates/ui-review.md) to record evidence. Fix related findings together and inspect again. Run the relevant build/type/lint checks. Automated accessibility tools can assist, but do not replace keyboard and screen-reader checks when those are in scope.

## 5. Deliver

Provide source changes, a preview command, required environment-variable names without values, and an accurate verification note. If deployment is requested, confirm the actual deployed result after the deployment finishes.

Example prompt:

```text
Use $fahrez-ui-build. Build an Indonesian circuit-learning interface in
this repository's existing stack. The primary task is solving an unknown
resistance from supplied measurements. Show the formula and calculation,
handle invalid inputs, and inspect a narrow phone viewport and desktop.
Use illustrative examples and label them. Deliver a working preview.
```
