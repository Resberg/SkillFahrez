---
name: fahrez-ui-build
description: Build or substantially redesign a responsive interface from a product brief, with working interactions and visual verification. Use for pages, dashboards, portfolios, and app screens.
---

# Build a UI

Identify the audience, the main task, the content, and what working completion means. Inspect existing project instructions, components, tokens, and package scripts before choosing a stack. Preserve an established system unless the user asks to change it.

Create a compact direction: a layout concept, type roles, semantic color tokens, spacing, and one distinctive element tied to the product. Match the amount of expression to the task: a portfolio can persuade; a working dashboard needs clear operations and legible data. Avoid inventing stats, testimonials, or product capabilities to fill space.

Implement the primary user journey first, including its result. Give buttons real actions. Label demo data and simulations. Include the empty, loading, error, success, and disabled states that the actual flow needs. Keep business logic outside presentation when doing so improves clarity; do not expand a small task into a framework.

Use semantic controls, visible labels and focus, useful error text, keyboard operation, and layouts that tolerate long text. Check narrow screens and zoom. Use meaningful images with appropriate alternatives. Respect reduced-motion preferences. Scope CSS so shared selectors do not silently override components.

Render representative desktop and mobile views with the tools available. Inspect hierarchy, spacing, overflow, text wrapping, image cropping, contrast, and focus. Exercise the primary journey and its failure/recovery path. Run the project's relevant build, lint, or type checks. Report tool limits instead of claiming a browser check that did not run.

Deliver the working files, instructions to preview, a concise description of the design decisions, and actual verification results. Deploy only within the user's authorized scope.
