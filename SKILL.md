---
name: platform-design-system
description: Design, audit, or extend a platform-specific design system from a website, product, brand, or codebase, including visual tokens, reusable components, interaction and motion, an interactive component gallery, documentation, and implementation handoff. Use for a coherent UI/UX system across a product, not a one-off generic styling change.
---

# Platform design system

Turn platform evidence and user goals into an implementable, reusable system. Match the requested scope and medium; an audit, pilot, full library, Figma artifact, or implementation are different outputs. Separate observed evidence, assumptions, and proposals. Never claim a screenshot, hover, device behavior, asset right, or implementation was verified unless observed. Respect existing project conventions and the requested fidelity.

## Workflow

1. **Scope and discover.** Inspect the supplied site, assets and relevant repository before deciding a stack. Identify audiences, journeys, platforms, languages, accessibility needs, constraints, owners and desired outputs. Distinguish faithful reproduction, brand extension, and inspiration. Ask only consequential missing questions; proceed with labelled assumptions otherwise. Read [discovery](references/discovery.md). Use `assets/templates/` to record evidence and decisions.
2. **Audit.** Examine representative pages, breakpoints, interaction states, responsive behavior, loading/error/empty states and existing components. Inspect rendered views and interactions when possible; static HTML is not proof of behavior. Record source, date, viewport, state, evidence, confidence and gaps. Never represent unobserved states as facts.
3. **Set direction.** Derive principles and semantic tokens from evidence; test on expressive brand pages and functional workflows. Define typography, color pairs, spacing, layout, elevation, radii, iconography, imagery, motion and themes as applicable. Bundled tokens and preview are generic examples, not extracted brand facts. Check provenance and rights.
4. **Design behavior and components.** Prioritize components based on actual journeys. Specify semantics, variants, anatomy, content, states, responsive behavior, keyboard, pointer, touch, focus, motion and error recovery. Document transitions, including real device/server confirmations where relevant. Read [interaction and components](references/interaction-components.md).
5. **Build requested outputs.** A complete system deliverable includes an interactive component gallery/documentation page: see [preview](references/preview.md) and the runnable starter in `assets/starter/`. An audit-only request need not build one. Map existing tokens and components before code changes. Choose Base UI, shadcn/ui or another stack based on the actual project. Invoke applicable Figma, Sites and other skills. For shadcn read [integration](references/shadcn-integration.md); its official skill is separate, not bundled. Keep existing dependencies and primitive library unless migration is requested.
6. **Verify and hand off.** Inspect actual outputs at representative sizes and interaction states; test keyboard, focus, reduced motion, touch alternatives, contrast, long text, loading/error and applicable workflows. Automated checks supplement manual validation. Report evidence, limitations, ownership and next steps. Read [verification and governance](references/verification-governance.md).

## Resources

- [Discovery](references/discovery.md); [interaction and components](references/interaction-components.md); [preview](references/preview.md); [verification and governance](references/verification-governance.md).
- [shadcn integration](references/shadcn-integration.md) and [illustrative Microduck example](references/example-microduck.md).
- `assets/templates/`: project brief, evidence inventory, decisions, component specification, state matrix and checklist.
- `assets/starter/`: editable sample tokens, CSS and a standalone interactive gallery. Redesign these neutral examples for each platform.
- `scripts/scaffold.py`: copies starter assets without overwriting. `scripts/contrast.py`: calculates contrast of opaque sRGB hex pairs; it cannot validate the rendered UI.

Use the available installation workflow if the user requests installation. Do not silently install third-party dependencies, configure a server, publish, or modify a live platform merely because this skill is invoked.
