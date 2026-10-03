(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Grease pencil circles the problem frame once, when the strip is on screen.
  const ring = $(".pencil-ring");
  if (ring) {
    const draw = () => { ring.classList.add("drawn"); ring.closest(".film")?.classList.add("inked"); };
    if (reduced || !("IntersectionObserver" in window)) draw();
    else {
      const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { draw(); io.disconnect(); } }, { threshold: 0.4 });
      io.observe(ring);
    }
  }

  // Loupe: drag (or arrow keys) to see Auto WB through the glass.
  const box = $(".loupe-box");
  if (box) {
    const frames = {
      dog: { before: "assets/img/dog-incandescent.jpg", after: "assets/img/dog-awb.jpg", alt: "Golden retriever on grey pavers" },
      lake: { before: "assets/img/lake-incandescent.jpg", after: "assets/img/lake-fixed.jpg", alt: "Pond with swans below mountains at dusk" },
    };
    const before = $(".before", box);
    const after = $(".fixed", box);
    let x = 46, y = 52;
    const place = () => { box.style.setProperty("--x", `${x}%`); box.style.setProperty("--y", `${y}%`); };
    const fromEvent = (e) => {
      const r = box.getBoundingClientRect();
      x = Math.min(100, Math.max(0, ((e.clientX - r.left) / r.width) * 100));
      y = Math.min(100, Math.max(0, ((e.clientY - r.top) / r.height) * 100));
      place();
    };
    box.addEventListener("pointerdown", (e) => {
      box.setPointerCapture(e.pointerId);
      box.classList.add("dragging");
      // A touch might be the start of a page scroll, so wait for a drag or a tap before moving the glass.
      if (e.pointerType !== "touch") fromEvent(e);
    });
    box.addEventListener("pointermove", (e) => { if (box.classList.contains("dragging") || e.pointerType === "mouse") fromEvent(e); });
    const stop = (e) => {
      if (e.type === "pointerup" && box.classList.contains("dragging")) fromEvent(e);
      box.classList.remove("dragging");
    };
    box.addEventListener("pointerup", stop);
    box.addEventListener("pointercancel", stop);
    box.addEventListener("keydown", (e) => {
      const step = e.shiftKey ? 10 : 3;
      const moves = { ArrowLeft: [-step, 0], ArrowRight: [step, 0], ArrowUp: [0, -step], ArrowDown: [0, step] };
      if (!moves[e.key]) return;
      e.preventDefault();
      x = Math.min(100, Math.max(0, x + moves[e.key][0]));
      y = Math.min(100, Math.max(0, y + moves[e.key][1]));
      place();
    });

    const fullBtn = $("[data-loupe-full]");
    fullBtn?.addEventListener("click", () => {
      const on = !box.classList.contains("full");
      box.classList.toggle("full", on);
      fullBtn.setAttribute("aria-pressed", String(on));
      fullBtn.textContent = on ? "Back to the loupe" : "Fix the whole frame";
    });

    $$("[data-frame]").forEach((btn) => btn.addEventListener("click", () => {
      const f = frames[btn.dataset.frame];
      before.src = f.before;
      after.src = f.after;
      before.alt = `${f.alt}, shot on Incandescent white balance: everything is tinted blue`;
      after.alt = `${f.alt}, corrected to daylight white balance`;
      $$("[data-frame]").forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
    }));
  }

  // Fix checklist, remembered on this device.
  const KEY = "s5ii-fixes";
  const saved = new Set(JSON.parse(localStorage.getItem(KEY) || "[]"));
  const boxes = $$(".fix input[type=checkbox]");
  const progress = $(".progress");
  const sync = () => {
    boxes.forEach((b) => b.closest(".fix").classList.toggle("is-done", b.checked));
    const n = boxes.filter((b) => b.checked).length;
    if (progress) progress.textContent = n === boxes.length ? "All five done. Go shoot." : `${n} of ${boxes.length} done on the camera`;
  };
  boxes.forEach((b) => {
    b.checked = saved.has(b.name);
    b.addEventListener("change", () => {
      b.checked ? saved.add(b.name) : saved.delete(b.name);
      localStorage.setItem(KEY, JSON.stringify([...saved]));
      sync();
    });
  });
  sync();

  // Mode dial.
  const dial = $(".dial-svg");
  if (dial) {
    const data = JSON.parse($("#dial-data").textContent);
    const rotor = $(".dial-rotor", dial);
    const positions = $$(".dial-pos", dial);
    const out = $(".readout");
    const step = 360 / data.length;
    const select = (id, focus = false) => {
      const i = data.findIndex((d) => d.id === id);
      const d = data[i];
      rotor.style.transform = `rotate(${-i * step}deg)`;
      positions.forEach((p) => p.classList.toggle("is-on", p.dataset.id === id));
      $$("[data-dial]").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.dial === id)));
      out.innerHTML = `
        <div class="label">${d.label}</div>
        <div class="name">${d.name}</div>
        ${d.note ? `<span class="marker">${d.note}</span>` : ""}
        <p>${d.what}</p>
        <dl>${d.rows.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join("")}</dl>`;
      if (focus) out.focus({ preventScroll: true });
    };
    positions.forEach((p) => {
      p.addEventListener("click", () => select(p.dataset.id));
      p.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); select(p.dataset.id); } });
    });
    $$("[data-dial]").forEach((b) => b.addEventListener("click", () => select(b.dataset.dial)));
    select("A");
  }

  // Looks: flip between LUT prints.
  const lookImg = $("#look-img");
  $$(".look-btn").forEach((btn) => btn.addEventListener("click", () => {
    lookImg.src = `assets/img/look-${btn.dataset.look}.jpg`;
    lookImg.alt = `Lisbon rooftops with the ${btn.querySelector(".n").textContent} look`;
    $("#look-cap").textContent = btn.dataset.cap;
    $$(".look-btn").forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
  }));

  // Edge nav: mark the section in view.
  const links = $$(".edge-nav a[href^='#']:not(.home)");
  const map = new Map(links.map((a) => [a.getAttribute("href").slice(1), a]));
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        links.forEach((a) => a.removeAttribute("aria-current"));
        const a = map.get(e.target.id);
        if (!a) return;
        a.setAttribute("aria-current", "true");
        // scrollIntoView would also scroll the page (the sticky bar sits inside scroll-padding), so only slide the bar.
        const bar = a.closest("ol");
        const dx = a.getBoundingClientRect().left - bar.getBoundingClientRect().left - (bar.clientWidth - a.offsetWidth) / 2;
        bar.scrollBy({ left: dx, behavior: reduced ? "auto" : "smooth" });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    map.forEach((_, id) => { const s = document.getElementById(id); if (s) io.observe(s); });
  }

  // Print only the field card.
  $("[data-print-card]")?.addEventListener("click", () => {
    document.body.classList.add("print-card");
    window.print();
  });
  addEventListener("afterprint", () => document.body.classList.remove("print-card"));
})();
