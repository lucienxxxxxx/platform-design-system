# Platform Design System Skill

An agent skill for researching, designing, documenting, and implementing a platform-specific design system. It covers visual tokens, reusable components, interaction states, motion, accessibility, an interactive component gallery, verification, and handoff.

## Use

Install the `platform-design-system` directory in your agent's skill location, or use the skills CLI:

```bash
npx skills add lucienxxxxxx/platform-design-system
```

Then ask your assistant, for example:

> Use the platform-design-system skill to study our website and build a design system for the marketing site and dashboard, including an interactive component gallery.

The skill adapts its outputs to the requested scope. It distinguishes observed behavior from inferred or proposed behavior, respects existing project conventions, and records validation limitations.

## What's included

- `SKILL.md`: the workflow and routing instructions.
- `references/`: discovery, component and interaction specifications, preview, verification, shadcn integration, and an illustrative example.
- `assets/templates/`: editable briefs, evidence and state inventories, component specification, and handoff checklist.
- `assets/starter/`: neutral HTML/CSS/JavaScript component gallery and example tokens. Open `assets/starter/index.html` in a browser. It is a starting point, not a production library or a representation of any platform's branding.
- `scripts/`: a non-overwriting scaffolder and a solid-color contrast calculator.

Create a new editable starting directory with Python 3:

```bash
python scripts/scaffold.py ./my-design-system
```

Check an opaque color pair:

```bash
python scripts/contrast.py '#000000' '#ffffff'
```

The contrast script checks only opaque sRGB hexadecimal pairs; it does not certify accessibility or assess the actual rendered interface. Adapt and verify the gallery against the intended project, browser, input devices, accessibility requirements, and real components before production use.

## shadcn/ui and Base UI

The official [shadcn skill](https://ui.shadcn.com/docs/skills) is a separate upstream project and is **not bundled**. This skill includes integration guidance and can be used alongside it. Base UI and shadcn/ui are optional; use the stack appropriate to the project.

## License

MIT. Third-party product names and linked sites belong to their respective owners; no third-party brand assets are included.
