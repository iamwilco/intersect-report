export function renderMarkdown(md: string): string {
  if (!md) return "";

  const esc = md
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

  const lines = esc.split("\n");
  const out: string[] = [];

  type Block =
    | { kind: "para"; lines: string[] }
    | { kind: "ul"; items: string[] }
    | { kind: "ol"; items: string[] }
    | { kind: "table"; header: string[]; rows: string[][] }
    | { kind: "quote"; lines: string[] };

  let cur: Block | null = null;

  const flush = () => {
    if (!cur) return;
    if (cur.kind === "para") {
      const text = cur.lines.join(" ").trim();
      if (text) out.push(`<p class="prose-p">${inline(text)}</p>`);
    } else if (cur.kind === "ul") {
      out.push(
        `<ul class="prose-ul">${cur.items
          .map((i) => `<li>${inline(i)}</li>`)
          .join("")}</ul>`
      );
    } else if (cur.kind === "ol") {
      out.push(
        `<ol class="prose-ol">${cur.items
          .map((i) => `<li>${inline(i)}</li>`)
          .join("")}</ol>`
      );
    } else if (cur.kind === "table") {
      const thead = `<thead><tr>${cur.header
        .map((h) => `<th>${inline(h)}</th>`)
        .join("")}</tr></thead>`;
      const tbody = `<tbody>${cur.rows
        .map(
          (r) =>
            `<tr>${r.map((c) => `<td>${inline(c)}</td>`).join("")}</tr>`
        )
        .join("")}</tbody>`;
      out.push(
        `<div class="prose-table-wrap"><table class="prose-table">${thead}${tbody}</table></div>`
      );
    } else if (cur.kind === "quote") {
      out.push(
        `<blockquote class="prose-quote">${cur.lines
          .map((l) => inline(l))
          .join("<br/>")}</blockquote>`
      );
    }
    cur = null;
  };

  const splitRow = (line: string): string[] =>
    line
      .trim()
      .replace(/^\|/, "")
      .replace(/\|$/, "")
      .split("|")
      .map((c) => c.trim());

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();

    if (trimmed === "") {
      flush();
      continue;
    }

    // Horizontal rule
    if (/^---+$/.test(trimmed)) {
      flush();
      out.push(`<hr class="prose-hr" />`);
      continue;
    }

    // Headers
    let h = /^(#{1,4})\s+(.+)$/.exec(trimmed);
    if (h) {
      flush();
      const level = h[1].length;
      out.push(
        `<h${level} class="prose-h${level}">${inline(h[2])}</h${level}>`
      );
      continue;
    }

    // Blockquote
    if (trimmed.startsWith("&gt;")) {
      const content = trimmed.replace(/^&gt;\s?/, "");
      if (cur?.kind === "quote") cur.lines.push(content);
      else {
        flush();
        cur = { kind: "quote", lines: [content] };
      }
      continue;
    }

    // Table
    if (trimmed.startsWith("|") && trimmed.includes("|", 1)) {
      const cells = splitRow(trimmed);
      const next = (lines[i + 1] || "").trim();
      const isHeader =
        next.startsWith("|") &&
        splitRow(next).every((c) => /^:?-+:?$/.test(c));
      const existing = cur as Block | null;
      if (existing && existing.kind === "table") {
        existing.rows.push(cells);
      } else if (isHeader) {
        flush();
        cur = { kind: "table", header: cells, rows: [] };
        i++; // skip separator row
      } else {
        flush();
        cur = { kind: "table", header: cells, rows: [] };
      }
      continue;
    }

    // Unordered list
    let ulm = /^[-*+]\s+(.+)$/.exec(trimmed);
    if (ulm) {
      if (cur?.kind === "ul") cur.items.push(ulm[1]);
      else {
        flush();
        cur = { kind: "ul", items: [ulm[1]] };
      }
      continue;
    }

    // Ordered list
    let olm = /^\d+\.\s+(.+)$/.exec(trimmed);
    if (olm) {
      if (cur?.kind === "ol") cur.items.push(olm[1]);
      else {
        flush();
        cur = { kind: "ol", items: [olm[1]] };
      }
      continue;
    }

    // Paragraph
    if (cur?.kind === "para") cur.lines.push(trimmed);
    else {
      flush();
      cur = { kind: "para", lines: [trimmed] };
    }
  }
  flush();

  return out.join("\n");
}

function inline(text: string): string {
  return text
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/(^|[^*])\*([^*]+)\*/g, "$1<em>$2</em>")
    .replace(/`([^`]+)`/g, "<code class=\"prose-code\">$1</code>")
    .replace(
      /\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g,
      '<a href="$2" target="_blank" rel="noopener noreferrer" class="prose-link">$1</a>'
    );
}

export function formatDate(dateStr: string): string {
  if (!dateStr || dateStr === "unknown") return dateStr;
  const y = dateStr.slice(0, 4);
  const m = dateStr.slice(4, 6);
  const d = dateStr.slice(6, 8);
  const months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
  ];
  return `${months[parseInt(m) - 1]} ${parseInt(d)}, ${y}`;
}

export function formatPeriod(start: string, end: string): string {
  return `${formatDate(start)} \u2192 ${formatDate(end)}`;
}
