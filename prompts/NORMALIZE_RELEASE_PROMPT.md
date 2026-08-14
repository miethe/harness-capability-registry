# Release Normalization Prompt

Given one official release record, the current canonical capability taxonomy, and the existing HarnessBOM:

1. Preserve each distinct upstream change as a source-faithful statement.
2. Classify `kind`, `category`, `surfaces`, affected `actors`, and candidate `capability_refs`.
3. Do not infer a capability introduction from a bug fix unless the text explicitly establishes introduction.
4. Flag security, breaking, deprecation, lifecycle, and actor-reachability changes.
5. Compare against current capability implementations and propose—not apply—semantic patches.
6. Treat missing evidence as `unknown`.
7. Output valid JSON matching the release and capability schemas.
8. Include a `review_reason` for every proposed capability-graph change.
