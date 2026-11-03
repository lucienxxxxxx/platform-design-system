# Interaction, motion and components

Prioritize controls and platform-specific patterns by frequency, complexity and impact. Specify purpose and non-use, anatomy and semantic element, variants and content, tokens, public API, states and transitions, keyboard, pointer, touch, focus and screen readers, responsive behavior, localization, overflow, dependencies, tests and owner. Use the component specification and state matrix templates.

Record default, hover, focus-visible, active, disabled, loading, selected, expanded, success, error and empty as applicable. Define trigger → transition → feedback → cancellation/recovery. Hover is enhancement only; touch and keyboard need equivalent access to essential content. Maintain visible focus and accessible names. For overlays specify focus entry, containment if modal, Escape, dismissal and return; verify behavior in the actual library.

Define motion role, properties, duration, easing and interruption. Prefer transform/opacity for simple effects, avoid layout jumps, offer reduced-motion alternatives and avoid auto-playing sound. Distinguish input received, request pending, server/device acknowledgment, success and failure. A button click does not prove that a hardware operation succeeded. Specify timeout and recovery as appropriate.

Use semantic tokens and reusable primitives. Match design and code names, variants and states; avoid inventing values from inaccessible sources. Verify current component APIs from the installed version.
