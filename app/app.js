(() => {
  "use strict";

  const DATA = window.HCR_DATA;
  if (!DATA) {
    document.body.innerHTML = '<main class="main"><section class="panel"><h1>Registry data unavailable</h1><p>Generate the bundle with <code>python -m hcr generate</code>, then reload this page.</p></section></main>';
    return;
  }

  const ACTORS = {
    human_operator: "Human operator",
    in_harness_agent: "In-harness agent",
    external_orchestrator: "External orchestrator",
    ci_runner: "CI runner",
    administrator: "Administrator"
  };
  const ACCESS_ORDER = ["native", "supported", "configurable", "experimental", "mediated", "unavailable", "unknown", "deprecated"];
  const ACCESS_LABELS = {
    native: "Native",
    supported: "Supported",
    configurable: "Configurable",
    experimental: "Experimental",
    mediated: "Mediated",
    unavailable: "Unavailable",
    unknown: "Unknown",
    deprecated: "Deprecated"
  };
  const FAMILY_LABELS = {
    agentic_harness: "Agentic harness",
    general_agent_harness: "General agent harness",
    agent_sdk: "Agent SDK",
    provider_sdk: "Provider SDK"
  };
  const PURPOSE_LABELS = {
    release_history: "Release history",
    capability_reference: "Capability reference",
    lifecycle_reference: "Lifecycle reference",
    comparison_reference: "Comparison reference"
  };
  const AUTHORITY_LABELS = {
    official_primary: "Official primary",
    official_secondary: "Official secondary"
  };

  const byId = (id) => document.getElementById(id);
  const harnessById = new Map(DATA.harnesses.map((item) => [item.id, item]));
  const taxonomyById = new Map(DATA.taxonomy.map((item) => [item.id, item]));
  const sourceById = new Map(DATA.sources.map((item) => [item.id, item]));
  const guideByHarness = new Map(DATA.agent_guides.map((item) => [item.harness.id, item]));
  const releasesByHarness = groupBy(DATA.releases, (item) => item.harness_id);
  const capabilitiesByHarness = groupBy(DATA.capabilities, (item) => item.harness_id);

  const configuredCoreHarnesses = DATA.registry_meta?.seed_scope?.core_harnesses || [];
  const defaultHarnesses = configuredCoreHarnesses.filter((id) => harnessById.has(id));
  if (defaultHarnesses.length === 0) {
    defaultHarnesses.push(...DATA.harnesses
      .filter((item) => item.tracking_priority === "core" && ["agentic_harness", "general_agent_harness"].includes(item.family))
      .map((item) => item.id));
  }

  const state = {
    activeTab: readTabFromHash(),
    selectedHarnesses: loadStoredHarnesses(defaultHarnesses),
    matrixActor: "external_orchestrator",
    releaseLimit: 40
  };

  function groupBy(items, fn) {
    const result = new Map();
    for (const item of items) {
      const key = fn(item);
      if (!result.has(key)) result.set(key, []);
      result.get(key).push(item);
    }
    return result;
  }

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function safeUrl(value) {
    try {
      const url = new URL(String(value));
      return ["http:", "https:"].includes(url.protocol) ? url.href : "#";
    } catch {
      return "#";
    }
  }

  function humanize(value) {
    return String(value ?? "")
      .replaceAll("_", " ")
      .replaceAll("-", " ")
      .replace(/\b\w/g, (match) => match.toUpperCase());
  }

  function formatNumber(value) {
    return new Intl.NumberFormat().format(Number(value || 0));
  }

  function formatDate(value, fallback = "Date not published") {
    if (!value) return fallback;
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return fallback;
    return new Intl.DateTimeFormat(undefined, { year: "numeric", month: "short", day: "numeric" }).format(date);
  }

  function formatDateTime(value, fallback = "Unknown") {
    if (!value) return fallback;
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return fallback;
    return new Intl.DateTimeFormat(undefined, {
      year: "numeric", month: "short", day: "numeric", hour: "numeric", minute: "2-digit"
    }).format(date);
  }

  function truncate(value, limit = 150) {
    const text = String(value ?? "");
    return text.length > limit ? `${text.slice(0, limit - 1)}…` : text;
  }

  function accessPill(access) {
    const normalized = ACCESS_LABELS[access] ? access : "unknown";
    return `<span class="access-pill ${escapeHtml(normalized)}">${escapeHtml(ACCESS_LABELS[normalized])}</span>`;
  }

  function lifecycleBadge(value) {
    const normalized = value || "unknown";
    return `<span class="badge ${escapeHtml(normalized)}">${escapeHtml(humanize(normalized))}</span>`;
  }

  function tags(items, max = items?.length ?? 0) {
    return (items || []).slice(0, max).map((item) => `<span class="tag">${escapeHtml(item)}</span>`).join("");
  }

  function list(items, empty = "None recorded") {
    if (!items || items.length === 0) return `<span class="card-subtitle">${escapeHtml(empty)}</span>`;
    return `<ul>${items.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>`;
  }

  function readTabFromHash() {
    const candidate = window.location.hash.replace(/^#\/?/, "");
    const valid = ["overview", "harnesses", "matrix", "actors", "releases", "sources", "guide"];
    return valid.includes(candidate) ? candidate : "overview";
  }

  function loadStoredHarnesses(fallback) {
    try {
      const parsed = JSON.parse(window.localStorage.getItem("hcr.matrixHarnesses") || "[]");
      const valid = parsed.filter((id) => harnessById.has(id));
      return valid.length > 0 ? valid : fallback;
    } catch {
      return fallback;
    }
  }

  function showToast(message) {
    const toast = byId("toast");
    toast.textContent = message;
    toast.classList.add("show");
    window.clearTimeout(showToast.timeout);
    showToast.timeout = window.setTimeout(() => toast.classList.remove("show"), 2300);
  }

  function openDialog(dialog) {
    if (typeof dialog.showModal === "function") dialog.showModal();
    else dialog.setAttribute("open", "");
  }

  function closeDialog(dialog) {
    if (typeof dialog.close === "function") dialog.close();
    else dialog.removeAttribute("open");
  }

  function switchTab(tab, { updateHash = true } = {}) {
    const validTab = byId(`view-${tab}`) ? tab : "overview";
    state.activeTab = validTab;
    document.querySelectorAll(".view").forEach((view) => view.classList.toggle("active", view.id === `view-${validTab}`));
    document.querySelectorAll(".nav-item").forEach((item) => item.classList.toggle("active", item.dataset.tab === validTab));
    if (updateHash) history.replaceState(null, "", `#${validTab}`);
    renderTab(validTab);
    window.scrollTo({ top: 0, behavior: "instant" });
  }

  function renderTab(tab) {
    if (tab === "overview") renderOverview();
    if (tab === "harnesses") renderHarnesses();
    if (tab === "matrix") renderMatrix();
    if (tab === "actors") renderActorView();
    if (tab === "releases") renderReleases();
    if (tab === "sources") renderSources();
    if (tab === "guide") renderGuide();
  }

  function populateSelect(select, options, labelFn = humanize) {
    const current = select.value;
    select.insertAdjacentHTML("beforeend", options.map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(labelFn(value))}</option>`).join(""));
    if ([...select.options].some((option) => option.value === current)) select.value = current;
  }

  function initializeFilters() {
    populateSelect(byId("harnessFamily"), [...new Set(DATA.harnesses.map((item) => item.family))].sort(), (value) => FAMILY_LABELS[value] || humanize(value));
    populateSelect(byId("harnessLifecycle"), [...new Set(DATA.harnesses.map((item) => item.lifecycle))].sort());

    for (const id of ["matrixActor", "actorSelect"]) {
      const select = byId(id);
      select.innerHTML = Object.entries(ACTORS).map(([value, label]) => `<option value="${value}">${escapeHtml(label)}</option>`).join("");
    }
    byId("matrixActor").value = state.matrixActor;
    byId("actorSelect").value = "external_orchestrator";

    populateSelect(byId("matrixCategory"), [...new Set(DATA.taxonomy.map((item) => item.category))].sort());
    populateHarnessOptions(byId("actorHarness"));
    populateSelect(byId("actorAccess"), ACCESS_ORDER, (value) => ACCESS_LABELS[value] || humanize(value));
    populateHarnessOptions(byId("releaseHarness"));

    populateSelect(byId("sourcePurpose"), [...new Set(DATA.sources.map((item) => item.purpose))].sort(), (value) => PURPOSE_LABELS[value] || humanize(value));
    populateSelect(byId("sourceAuthority"), [...new Set(DATA.sources.map((item) => item.authority))].sort(), (value) => AUTHORITY_LABELS[value] || humanize(value));

    const guideSelect = byId("guideHarness");
    guideSelect.innerHTML = sortedHarnesses().map((item) => `<option value="${escapeHtml(item.id)}">${escapeHtml(item.name)}</option>`).join("");
    guideSelect.value = defaultHarnesses[0] || DATA.harnesses[0]?.id || "";
  }

  function sortedHarnesses() {
    const priority = { core: 0, secondary: 1, historical: 2 };
    return [...DATA.harnesses].sort((a, b) =>
      (priority[a.tracking_priority] ?? 3) - (priority[b.tracking_priority] ?? 3) ||
      a.name.localeCompare(b.name)
    );
  }

  function populateHarnessOptions(select) {
    select.insertAdjacentHTML("beforeend", sortedHarnesses().map((item) => `<option value="${escapeHtml(item.id)}">${escapeHtml(item.name)}</option>`).join(""));
  }

  function renderFreshness() {
    const updated = DATA.registry_meta.updated_at || DATA.generated_at;
    byId("freshnessBadge").textContent = `Verified ${formatDate(updated)}`;
  }

  function renderOverview() {
    const statCards = [
      [DATA.stats.harness_count, "Tracked harness / SDK tracks"],
      [DATA.stats.source_count, "Official evidence sources"],
      [DATA.stats.capability_implementation_count, "Capability implementations"],
      [DATA.stats.release_count, "Historical releases"],
      [DATA.stats.release_change_count, "Normalized release changes"]
    ];
    byId("statsGrid").innerHTML = statCards.map(([value, label]) => `
      <article class="stat-card"><span class="stat-value">${formatNumber(value)}</span><span class="stat-label">${escapeHtml(label)}</span></article>
    `).join("");

    const core = defaultHarnesses.map((id) => harnessById.get(id)).filter(Boolean);
    byId("coreHarnesses").innerHTML = core.map((item) => {
      const count = capabilitiesByHarness.get(item.id)?.length || 0;
      return `<article class="mini-card" data-harness-id="${escapeHtml(item.id)}" tabindex="0" role="button">
        <div class="mini-card-head"><div><strong>${escapeHtml(item.name)}</strong><span>${escapeHtml(item.vendor)}</span></div>${lifecycleBadge(item.lifecycle)}</div>
        <div class="card-footer"><span>${formatNumber(count)} mapped capabilities</span><span>${escapeHtml(item.current_version || "version unknown")}</span></div>
      </article>`;
    }).join("");
    byId("coreHarnesses").querySelectorAll("[data-harness-id]").forEach(bindHarnessOpen);

    const impact = [];
    for (const release of DATA.releases) {
      const harness = harnessById.get(release.harness_id);
      for (const change of release.changes || []) {
        if (change.security_relevant || change.breaking_or_deprecated || ["added", "deprecated", "removed", "security"].includes(change.kind)) {
          impact.push({ release, change, harness });
        }
      }
      if (impact.length >= 28) break;
    }
    byId("impactChanges").innerHTML = impact.slice(0, 8).map(({ release, change, harness }) => `
      <article class="timeline-item">
        <div><div class="timeline-version">${escapeHtml(release.version)}</div><div class="timeline-product">${escapeHtml(harness?.name || release.harness_id)}</div></div>
        <div><div class="timeline-text">${escapeHtml(truncate(change.summary, 180))}</div><div class="change-meta">${escapeHtml(humanize(change.kind))} · ${escapeHtml(formatDate(release.published_at))}</div></div>
      </article>
    `).join("") || '<p class="card-subtitle">No impact-tagged changes are available yet.</p>';

    const sourcesOfficial = DATA.sources.filter((item) => item.official).length;
    const tracksWithReleases = new Set(DATA.releases.map((item) => item.harness_id)).size;
    const actorAssessments = DATA.capabilities.reduce((sum, item) => sum + Object.keys(item.actor_access || {}).length, 0);
    const verifiedPct = DATA.stats.capability_implementation_count
      ? Math.round((DATA.stats.verified_capability_count / DATA.stats.capability_implementation_count) * 100)
      : 0;
    const coverage = [
      [`${verifiedPct}%`, "Capabilities backed by verified official evidence"],
      [sourcesOfficial, "Official sources in the evidence inventory"],
      [`${tracksWithReleases}/${DATA.stats.harness_count}`, "Tracks with ingested release history"],
      [actorAssessments, "Explicit actor-access assessments"]
    ];
    byId("coverageSummary").innerHTML = coverage.map(([value, label]) => `
      <article class="coverage-card"><strong>${escapeHtml(formatNumberMaybe(value))}</strong><span>${escapeHtml(label)}</span></article>
    `).join("");
  }

  function formatNumberMaybe(value) {
    return typeof value === "number" ? formatNumber(value) : value;
  }

  function bindHarnessOpen(element) {
    const open = () => showHarness(element.dataset.harnessId);
    element.addEventListener("click", open);
    element.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        open();
      }
    });
  }

  function renderHarnesses() {
    const query = byId("harnessSearch").value.trim().toLowerCase();
    const family = byId("harnessFamily").value;
    const lifecycle = byId("harnessLifecycle").value;
    const records = sortedHarnesses().filter((item) => {
      const haystack = [item.name, item.vendor, item.family, ...(item.surfaces || []), ...(item.recommended_when || [])].join(" ").toLowerCase();
      return (!query || haystack.includes(query)) && (family === "all" || item.family === family) && (lifecycle === "all" || item.lifecycle === lifecycle);
    });

    byId("harnessGrid").innerHTML = records.map((item) => {
      const capCount = capabilitiesByHarness.get(item.id)?.length || 0;
      const releaseCount = releasesByHarness.get(item.id)?.length || 0;
      return `<article class="harness-card" data-harness-id="${escapeHtml(item.id)}" tabindex="0" role="button">
        <div class="card-top">
          <div><h3 class="card-title">${escapeHtml(item.name)}</h3><div class="card-subtitle">${escapeHtml(item.vendor)} · ${escapeHtml(FAMILY_LABELS[item.family] || humanize(item.family))}</div></div>
          <div class="card-version">${escapeHtml(item.current_version || "unverified")}</div>
        </div>
        <div class="card-section"><div class="card-section-label">Surfaces</div><div class="tag-row">${tags(item.surfaces, 6)}</div></div>
        <div class="card-section"><div class="card-section-label">Best fit</div><div class="tag-row">${tags(item.recommended_when, 3)}</div></div>
        <div class="card-footer"><span>${formatNumber(capCount)} capabilities · ${formatNumber(releaseCount)} releases</span>${lifecycleBadge(item.lifecycle)}</div>
      </article>`;
    }).join("");
    byId("harnessEmpty").classList.toggle("hidden", records.length > 0);
    byId("harnessGrid").querySelectorAll("[data-harness-id]").forEach(bindHarnessOpen);
  }

  function showHarness(harnessId) {
    const item = harnessById.get(harnessId);
    if (!item) return;
    const capabilities = capabilitiesByHarness.get(item.id) || [];
    const releases = releasesByHarness.get(item.id) || [];
    const sources = (item.source_ids || []).map((id) => sourceById.get(id)).filter(Boolean);
    const predecessor = item.predecessor ? harnessById.get(item.predecessor) : null;
    const successor = item.successor ? harnessById.get(item.successor) : null;

    byId("dialogEyebrow").textContent = `${item.vendor} · ${FAMILY_LABELS[item.family] || humanize(item.family)}`;
    byId("dialogTitle").textContent = item.name;
    byId("dialogBody").innerHTML = `
      <dl class="detail-grid">
        <dt>Current version</dt><dd><code>${escapeHtml(item.current_version || "Not verified")}</code> <span class="card-subtitle">as of ${escapeHtml(item.version_as_of || "unknown")}</span></dd>
        <dt>Lifecycle</dt><dd>${lifecycleBadge(item.lifecycle)} ${lifecycleBadge(item.maturity)}</dd>
        <dt>Mapped capabilities</dt><dd>${formatNumber(capabilities.length)}</dd>
        <dt>Historical releases</dt><dd>${formatNumber(releases.length)}</dd>
        <dt>Surfaces</dt><dd><div class="tag-row">${tags(item.surfaces)}</div></dd>
        <dt>Authentication</dt><dd><div class="tag-row">${tags(item.auth_modes)}</div></dd>
        ${predecessor ? `<dt>Predecessor</dt><dd>${escapeHtml(predecessor.name)}</dd>` : ""}
        ${successor ? `<dt>Successor</dt><dd>${escapeHtml(successor.name)}</dd>` : ""}
        <dt>Official links</dt><dd>${item.docs_url ? `<a href="${escapeHtml(safeUrl(item.docs_url))}" target="_blank" rel="noopener">Documentation</a>` : ""}${item.docs_url && item.repo_url ? " · " : ""}${item.repo_url ? `<a href="${escapeHtml(safeUrl(item.repo_url))}" target="_blank" rel="noopener">Repository</a>` : ""}</dd>
      </dl>
      <section class="card-section"><h3>Recommended when</h3>${list(item.recommended_when)}</section>
      <section class="card-section"><h3>Avoid or qualify when</h3>${list(item.avoid_when)}</section>
      <section class="card-section"><h3>Control-plane routing dimensions</h3><div class="tag-row">${Object.entries(item.control_plane_dimensions || {}).map(([key, value]) => `<span class="tag">${escapeHtml(humanize(key))}: ${escapeHtml(humanize(value))}</span>`).join("")}</div></section>
      <section class="card-section"><h3>Official evidence sources</h3><div class="evidence-list">${sources.map((source) => `
        <article class="evidence-card"><strong>${escapeHtml(source.name)}</strong><div class="card-subtitle">${escapeHtml(PURPOSE_LABELS[source.purpose] || humanize(source.purpose))} · ${escapeHtml(AUTHORITY_LABELS[source.authority] || humanize(source.authority))}</div><a href="${escapeHtml(safeUrl(source.url))}" target="_blank" rel="noopener">${escapeHtml(source.url)}</a></article>
      `).join("") || '<p class="card-subtitle">No source records attached.</p>'}</div></section>
      <section class="card-section"><h3>Recent registry releases</h3>${releases.slice(0, 8).map((release) => `<div class="guide-capability"><strong>${escapeHtml(release.version)}</strong><p>${escapeHtml(formatDate(release.published_at))} · ${formatNumber(release.change_count)} normalized changes</p></div>`).join("") || '<p class="card-subtitle">No release history ingested yet.</p>'}</section>
    `;
    openDialog(byId("detailDialog"));
  }

  function renderMatrix() {
    state.matrixActor = byId("matrixActor").value;
    const category = byId("matrixCategory").value;
    const query = byId("matrixSearch").value.trim().toLowerCase();
    const selected = state.selectedHarnesses.map((id) => harnessById.get(id)).filter(Boolean);
    const rows = DATA.matrix.filter((row) => {
      const capability = row.capability;
      const haystack = [capability.name, capability.category, capability.definition, capability.comparison_question].join(" ").toLowerCase();
      return (category === "all" || capability.category === category) && (!query || haystack.includes(query));
    });

    byId("selectedHarnessChips").innerHTML = selected.map((item) => `<span class="chip">${escapeHtml(item.name)}</span>`).join("");
    byId("matrixHead").innerHTML = `<tr><th>Capability</th>${selected.map((item) => `<th>${escapeHtml(item.name)}<span class="capability-category">${escapeHtml(item.vendor)}</span></th>`).join("")}</tr>`;
    byId("matrixBody").innerHTML = rows.map((row) => {
      const cells = selected.map((harness) => {
        const impl = row.implementations[harness.id];
        const access = impl?.actor_access?.[state.matrixActor] || "unknown";
        const summary = impl ? truncate(impl.summary, 110) : "No reviewed implementation record for this capability.";
        return `<td class="matrix-cell" data-capability-id="${escapeHtml(row.capability.id)}" data-harness-id="${escapeHtml(harness.id)}" tabindex="0">
          ${accessPill(access)}
          <div class="matrix-summary">${escapeHtml(summary)}</div>
        </td>`;
      }).join("");
      return `<tr><td><span class="capability-name">${escapeHtml(row.capability.name)}</span><span class="capability-category">${escapeHtml(humanize(row.capability.category))}</span></td>${cells}</tr>`;
    }).join("");

    byId("matrixBody").querySelectorAll(".matrix-cell").forEach((cell) => {
      const open = () => showCapability(cell.dataset.harnessId, cell.dataset.capabilityId, state.matrixActor);
      cell.addEventListener("click", open);
      cell.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          open();
        }
      });
    });
  }

  function renderColumnChoices() {
    byId("columnChoices").innerHTML = sortedHarnesses().map((item) => {
      const checked = state.selectedHarnesses.includes(item.id) ? "checked" : "";
      return `<label class="choice"><input type="checkbox" value="${escapeHtml(item.id)}" ${checked}><span><strong>${escapeHtml(item.name)}</strong><span>${escapeHtml(item.vendor)} · ${escapeHtml(FAMILY_LABELS[item.family] || humanize(item.family))}</span></span></label>`;
    }).join("");
  }

  function showCapability(harnessId, capabilityId, actor) {
    const harness = harnessById.get(harnessId);
    const taxonomy = taxonomyById.get(capabilityId);
    const impl = (capabilitiesByHarness.get(harnessId) || []).find((item) => item.capability_id === capabilityId);
    byId("dialogEyebrow").textContent = `${harness?.name || harnessId} · ${ACTORS[actor] || humanize(actor)}`;
    byId("dialogTitle").textContent = taxonomy?.name || capabilityId;

    if (!impl) {
      byId("dialogBody").innerHTML = `
        <div class="guide-warning"><strong>Unknown / unmodeled.</strong> The registry has no reviewed implementation claim for this harness-capability pair. This is not evidence that the capability is unavailable.</div>
        <section class="card-section"><h3>Comparison question</h3><p>${escapeHtml(taxonomy?.comparison_question || "No comparison question recorded.")}</p></section>
        <section class="card-section"><h3>Definition</h3><p>${escapeHtml(taxonomy?.definition || "No definition recorded.")}</p></section>
      `;
      openDialog(byId("detailDialog"));
      return;
    }

    const evidence = impl.evidence || [];
    const actorRows = Object.entries(ACTORS).map(([key, label]) => `<dt>${escapeHtml(label)}</dt><dd>${accessPill(impl.actor_access?.[key] || "unknown")}</dd>`).join("");
    byId("dialogBody").innerHTML = `
      ${impl.requires_human_mediation ? '<div class="guide-warning"><strong>Human mediation required.</strong> This capability cannot be treated as directly agent-callable without the documented mediation step.</div>' : ""}
      <p>${escapeHtml(impl.summary)}</p>
      <dl class="detail-grid">
        <dt>Status</dt><dd>${lifecycleBadge(impl.status)}</dd>
        <dt>Confidence</dt><dd>${escapeHtml(humanize(impl.confidence))}</dd>
        <dt>Verified version</dt><dd><code>${escapeHtml(impl.current_version_verified || "Unpinned")}</code></dd>
        <dt>Minimum version</dt><dd><code>${escapeHtml(impl.minimum_version || "Not recorded")}</code></dd>
        <dt>Verified at</dt><dd>${escapeHtml(formatDateTime(impl.verified_at))}</dd>
        <dt>Surfaces</dt><dd><div class="tag-row">${tags(impl.surfaces)}</div></dd>
        <dt>Invocation</dt><dd>${(impl.invocation || []).length ? impl.invocation.map((value) => `<code>${escapeHtml(value)}</code>`).join(" · ") : "Not recorded"}</dd>
        ${actorRows}
      </dl>
      <section class="card-section"><h3>Definition</h3><p>${escapeHtml(taxonomy?.definition || "Not recorded")}</p><p class="card-subtitle">${escapeHtml(taxonomy?.comparison_question || "")}</p></section>
      <section class="card-section"><h3>Limitations</h3>${list(impl.limitations, "No explicit limitations recorded; this does not imply none exist.")}</section>
      <section class="card-section"><h3>Evidence</h3><div class="evidence-list">${evidence.map((item) => {
        const source = sourceById.get(item.source_id);
        return `<article class="evidence-card"><strong>${escapeHtml(source?.name || item.source_id)}</strong><p>${escapeHtml(item.claim)}</p><div class="card-subtitle">Version ${escapeHtml(item.version || "current docs")} · checked ${escapeHtml(formatDate(item.verified_at))}</div><a href="${escapeHtml(safeUrl(item.url))}" target="_blank" rel="noopener">${escapeHtml(item.url)}</a></article>`;
      }).join("") || '<p class="card-subtitle">No evidence records attached.</p>'}</div></section>
    `;
    openDialog(byId("detailDialog"));
  }

  function actorFilteredCapabilities() {
    const actor = byId("actorSelect").value;
    const harnessFilter = byId("actorHarness").value;
    const accessFilter = byId("actorAccess").value;
    const query = byId("actorSearch").value.trim().toLowerCase();
    return DATA.capabilities.filter((impl) => {
      const harness = harnessById.get(impl.harness_id);
      const taxonomy = taxonomyById.get(impl.capability_id);
      const access = impl.actor_access?.[actor] || "unknown";
      const haystack = [harness?.name, harness?.vendor, taxonomy?.name, taxonomy?.category, impl.summary].join(" ").toLowerCase();
      return (harnessFilter === "all" || impl.harness_id === harnessFilter) &&
        (accessFilter === "all" || access === accessFilter) &&
        (!query || haystack.includes(query));
    });
  }

  function renderActorView() {
    const actor = byId("actorSelect").value;
    const records = actorFilteredCapabilities();
    const counts = Object.fromEntries(ACCESS_ORDER.map((value) => [value, 0]));
    records.forEach((item) => counts[item.actor_access?.[actor] || "unknown"] += 1);
    const direct = counts.native + counts.supported + counts.configurable + counts.experimental;
    const summaries = [
      [records.length, "Matching implementation records"],
      [direct, "Direct or configurable"],
      [counts.mediated, "Require mediation"],
      [counts.unavailable + counts.unknown, "Unavailable or unknown"]
    ];
    byId("actorSummary").innerHTML = summaries.map(([value, label]) => `<article class="stat-card"><span class="stat-value">${formatNumber(value)}</span><span class="stat-label">${escapeHtml(label)}</span></article>`).join("");

    byId("actorResults").innerHTML = records
      .sort((a, b) => {
        const accessA = ACCESS_ORDER.indexOf(a.actor_access?.[actor] || "unknown");
        const accessB = ACCESS_ORDER.indexOf(b.actor_access?.[actor] || "unknown");
        return accessA - accessB || (harnessById.get(a.harness_id)?.name || "").localeCompare(harnessById.get(b.harness_id)?.name || "") || (taxonomyById.get(a.capability_id)?.name || "").localeCompare(taxonomyById.get(b.capability_id)?.name || "");
      })
      .map((impl) => {
        const harness = harnessById.get(impl.harness_id);
        const taxonomy = taxonomyById.get(impl.capability_id);
        const access = impl.actor_access?.[actor] || "unknown";
        return `<article class="result-card" data-harness-id="${escapeHtml(impl.harness_id)}" data-capability-id="${escapeHtml(impl.capability_id)}" tabindex="0" role="button">
          <div><strong>${escapeHtml(taxonomy?.name || impl.capability_id)}</strong><div class="result-product">${escapeHtml(harness?.name || impl.harness_id)} · ${escapeHtml(humanize(taxonomy?.category || "other"))}</div></div>
          <div class="result-summary">${escapeHtml(impl.summary)}${impl.requires_human_mediation ? " Human mediation is required." : ""}</div>
          <div>${accessPill(access)}</div>
        </article>`;
      }).join("") || '<div class="empty-state">No capability records match these filters.</div>';

    byId("actorResults").querySelectorAll("[data-capability-id]").forEach((element) => {
      const open = () => showCapability(element.dataset.harnessId, element.dataset.capabilityId, actor);
      element.addEventListener("click", open);
      element.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          open();
        }
      });
    });
  }

  function releaseMatchesFlag(release, flag) {
    if (flag === "all") return true;
    if (flag === "security") return release.flags?.security || (release.changes || []).some((item) => item.security_relevant);
    if (flag === "breaking") return release.flags?.breaking || release.flags?.deprecation || (release.changes || []).some((item) => item.breaking_or_deprecated);
    if (flag === "added") return (release.changes || []).some((item) => item.kind === "added");
    return true;
  }

  function renderReleases() {
    const harnessFilter = byId("releaseHarness").value;
    const flag = byId("releaseFlag").value;
    const query = byId("releaseSearch").value.trim().toLowerCase();
    const records = DATA.releases.filter((release) => {
      const harness = harnessById.get(release.harness_id);
      const haystack = [release.version, release.title, release.notes_excerpt, harness?.name, ...(release.changes || []).map((item) => item.summary)].join(" ").toLowerCase();
      return (harnessFilter === "all" || release.harness_id === harnessFilter) && releaseMatchesFlag(release, flag) && (!query || haystack.includes(query));
    });
    const visible = records.slice(0, state.releaseLimit);

    byId("releaseResults").innerHTML = visible.map((release) => {
      const harness = harnessById.get(release.harness_id);
      const flags = [
        release.flags?.security ? '<span class="flag security">security</span>' : "",
        (release.flags?.breaking || release.flags?.deprecation) ? '<span class="flag breaking">breaking / deprecated</span>' : "",
        `<span class="flag">${formatNumber(release.change_count)} changes</span>`
      ].join("");
      return `<article class="release-card">
        <div class="release-head" tabindex="0" role="button" aria-expanded="false">
          <div><div class="release-product">${escapeHtml(harness?.name || release.harness_id)} · ${escapeHtml(release.version)}</div><div class="release-meta">${escapeHtml(formatDate(release.published_at))} · ${escapeHtml(humanize(release.channel))} · ${escapeHtml(humanize(release.provenance?.ingestion || "unknown ingestion"))}</div></div>
          <div><div class="release-title">${escapeHtml(release.title || `Release ${release.version}`)}</div><div class="release-excerpt">${escapeHtml(release.notes_excerpt || release.changes?.[0]?.summary || "No release excerpt captured.")}</div></div>
          <div class="flag-row">${flags}</div>
        </div>
        <div class="release-body">
          <ol class="change-list">${(release.changes || []).map((change) => `<li><div>${escapeHtml(change.summary)}</div><div class="change-meta">${escapeHtml(humanize(change.kind))} · ${escapeHtml(humanize(change.category))} · ${escapeHtml(humanize(change.normalization?.review_status || "unreviewed"))}${change.security_relevant ? " · security" : ""}${change.breaking_or_deprecated ? " · breaking/deprecated" : ""}</div></li>`).join("") || "<li>No normalized changes captured.</li>"}</ol>
          <p class="card-subtitle">Source: <a href="${escapeHtml(safeUrl(release.source_url))}" target="_blank" rel="noopener">${escapeHtml(release.source_url)}</a></p>
        </div>
      </article>`;
    }).join("") || '<div class="empty-state">No releases match these filters.</div>';

    byId("releaseResults").querySelectorAll(".release-card").forEach((card) => {
      const head = card.querySelector(".release-head");
      const toggle = () => {
        card.classList.toggle("open");
        head.setAttribute("aria-expanded", String(card.classList.contains("open")));
      };
      head.addEventListener("click", toggle);
      head.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          toggle();
        }
      });
    });
    byId("loadMoreReleases").classList.toggle("hidden", visible.length >= records.length);
  }

  function renderSources() {
    const purpose = byId("sourcePurpose").value;
    const authority = byId("sourceAuthority").value;
    const query = byId("sourceSearch").value.trim().toLowerCase();
    const records = DATA.sources.filter((source) => {
      const names = (source.harness_ids || []).map((id) => harnessById.get(id)?.name || id);
      const haystack = [source.name, source.url, source.source_type, source.purpose, source.authority, ...names].join(" ").toLowerCase();
      return (purpose === "all" || source.purpose === purpose) && (authority === "all" || source.authority === authority) && (!query || haystack.includes(query));
    });

    byId("sourceBody").innerHTML = records.map((source) => {
      const tracks = (source.harness_ids || []).map((id) => harnessById.get(id)?.name || id);
      return `<tr>
        <td><span class="source-name">${escapeHtml(source.name)}</span><a class="source-url" href="${escapeHtml(safeUrl(source.url))}" target="_blank" rel="noopener">${escapeHtml(source.url)}</a></td>
        <td>${escapeHtml(PURPOSE_LABELS[source.purpose] || humanize(source.purpose))}</td>
        <td>${escapeHtml(AUTHORITY_LABELS[source.authority] || humanize(source.authority))}</td>
        <td><div class="tag-row">${tags(tracks, 5)}</div></td>
        <td>${escapeHtml(humanize(source.collector?.kind || "manual"))}</td>
        <td>${escapeHtml(humanize(source.refresh?.cadence || "manual"))}<div class="card-subtitle">SLA ${escapeHtml(source.refresh?.staleness_sla_hours ?? "—")}h</div></td>
      </tr>`;
    }).join("") || '<tr><td colspan="6" class="empty-state">No sources match these filters.</td></tr>';
  }

  function renderGuide() {
    const harnessId = byId("guideHarness").value;
    const guide = guideByHarness.get(harnessId);
    if (!guide) {
      byId("guideContent").innerHTML = '<div class="empty-state">No generated guide is available for this harness.</div>';
      return;
    }
    const routing = guide.routing_hint || {};
    const mediationCount = guide.human_mediation_required?.length || 0;
    const lowConfidenceCount = guide.unverified_or_low_confidence?.length || 0;
    const actorPanels = Object.entries(guide.capabilities_by_actor || {}).map(([actor, capabilities]) => {
      const sorted = [...capabilities].sort((a, b) => ACCESS_ORDER.indexOf(a.access) - ACCESS_ORDER.indexOf(b.access) || a.name.localeCompare(b.name));
      return `<section class="actor-panel">
        <h3>${escapeHtml(ACTORS[actor] || humanize(actor))} <span class="badge">${formatNumber(capabilities.length)}</span></h3>
        ${sorted.slice(0, 12).map((capability) => `<article class="guide-capability"><div>${accessPill(capability.access)} <strong>${escapeHtml(capability.name)}</strong></div><p>${escapeHtml(truncate(capability.summary, 170))}</p></article>`).join("") || '<p class="card-subtitle">No callable capabilities recorded for this actor.</p>'}
        ${sorted.length > 12 ? `<p class="card-subtitle">${formatNumber(sorted.length - 12)} additional entries are included in the downloadable JSON guide.</p>` : ""}
      </section>`;
    }).join("");

    byId("guideContent").innerHTML = `
      <section class="guide-hero">
        <div><p class="eyebrow">${escapeHtml(guide.harness.vendor)} · ${escapeHtml(FAMILY_LABELS[guide.harness.family] || humanize(guide.harness.family))}</p><h2>${escapeHtml(guide.harness.name)} HarnessBOM</h2><p class="card-subtitle">Version ${escapeHtml(guide.harness.current_version || "unverified")} · generated ${escapeHtml(formatDateTime(guide.generated_at))}</p></div>
        ${lifecycleBadge(guide.harness.lifecycle)}
      </section>
      <div class="guide-warning"><strong>Agent routing warning:</strong> ${escapeHtml(guide.freshness.warning)} ${mediationCount ? `${formatNumber(mediationCount)} capability entries require human mediation.` : ""} ${lowConfidenceCount ? `${formatNumber(lowConfidenceCount)} entries remain low-confidence or unverified.` : ""}</div>
      <section class="panel card-section"><div class="panel-heading"><div><p class="eyebrow">Routing hint</p><h2>Control-plane fit</h2></div></div>
        <div class="two-column"><div><h3>Recommended when</h3>${list(routing.recommended_when)}</div><div><h3>Avoid or qualify when</h3>${list(routing.avoid_when)}</div></div>
        <div class="tag-row">${Object.entries(routing.control_plane_dimensions || {}).map(([key, value]) => `<span class="tag">${escapeHtml(humanize(key))}: ${escapeHtml(humanize(value))}</span>`).join("")}</div>
      </section>
      <div class="actor-sections">${actorPanels}</div>
    `;
  }

  async function copyGuide() {
    const guide = guideByHarness.get(byId("guideHarness").value);
    if (!guide) return;
    const text = JSON.stringify(guide, null, 2);
    try {
      await navigator.clipboard.writeText(text);
      showToast("Agent guide JSON copied");
    } catch {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed";
      textarea.style.opacity = "0";
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      textarea.remove();
      showToast("Agent guide JSON copied");
    }
  }

  function downloadBundle(event) {
    if (!window.Blob || !window.URL?.createObjectURL) return;
    event.preventDefault();
    const blob = new Blob([JSON.stringify(DATA, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = "harness-capability-registry.bundle.json";
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    URL.revokeObjectURL(url);
  }

  function bindEvents() {
    document.querySelectorAll(".nav-item").forEach((button) => button.addEventListener("click", () => switchTab(button.dataset.tab)));
    window.addEventListener("hashchange", () => switchTab(readTabFromHash(), { updateHash: false }));

    ["harnessSearch", "harnessFamily", "harnessLifecycle"].forEach((id) => byId(id).addEventListener(id === "harnessSearch" ? "input" : "change", renderHarnesses));
    ["matrixActor", "matrixCategory"].forEach((id) => byId(id).addEventListener("change", renderMatrix));
    byId("matrixSearch").addEventListener("input", renderMatrix);
    byId("chooseHarnesses").addEventListener("click", () => { renderColumnChoices(); openDialog(byId("columnDialog")); });
    byId("applyColumns").addEventListener("click", () => {
      const selected = [...byId("columnChoices").querySelectorAll('input[type="checkbox"]:checked')].map((input) => input.value);
      if (selected.length === 0) {
        showToast("Select at least one harness column");
        return;
      }
      state.selectedHarnesses = selected;
      window.localStorage.setItem("hcr.matrixHarnesses", JSON.stringify(selected));
      closeDialog(byId("columnDialog"));
      renderMatrix();
    });

    ["actorSelect", "actorHarness", "actorAccess"].forEach((id) => byId(id).addEventListener("change", renderActorView));
    byId("actorSearch").addEventListener("input", renderActorView);

    ["releaseHarness", "releaseFlag"].forEach((id) => byId(id).addEventListener("change", () => { state.releaseLimit = 40; renderReleases(); }));
    byId("releaseSearch").addEventListener("input", () => { state.releaseLimit = 40; renderReleases(); });
    byId("loadMoreReleases").addEventListener("click", () => { state.releaseLimit += 40; renderReleases(); });

    ["sourcePurpose", "sourceAuthority"].forEach((id) => byId(id).addEventListener("change", renderSources));
    byId("sourceSearch").addEventListener("input", renderSources);
    byId("guideHarness").addEventListener("change", renderGuide);
    byId("copyGuide").addEventListener("click", copyGuide);
    byId("downloadBundle").addEventListener("click", downloadBundle);

    byId("openAbout").addEventListener("click", () => openDialog(byId("aboutDialog")));
    byId("closeAbout").addEventListener("click", () => closeDialog(byId("aboutDialog")));
    byId("closeDialog").addEventListener("click", () => closeDialog(byId("detailDialog")));
    byId("closeColumns").addEventListener("click", () => closeDialog(byId("columnDialog")));

    for (const dialog of document.querySelectorAll("dialog")) {
      dialog.addEventListener("click", (event) => {
        if (event.target === dialog) closeDialog(dialog);
      });
    }
  }

  initializeFilters();
  bindEvents();
  renderFreshness();
  switchTab(state.activeTab, { updateHash: false });
})();
