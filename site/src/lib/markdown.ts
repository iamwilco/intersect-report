export function renderMarkdown(md: string): string {
  if (!md) return "";

  let html = md
    // Escape HTML
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    // Headers
    .replace(/^#### (.+)$/gm, '<h4 class="mt-6 mb-2 font-serif font-bold text-base">$1</h4>')
    .replace(/^### (.+)$/gm, '<h3 class="mt-8 mb-3 font-serif font-bold text-lg">$1</h3>')
    .replace(/^## (.+)$/gm, '<h2 class="mt-10 mb-4 font-serif font-bold text-xl">$1</h2>')
    // Horizontal rules
    .replace(/^---$/gm, '<hr class="my-8 border-rule" />')
    // Bold and italic
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\*(.+?)\*/g, "<em>$1</em>")
    // Tables
    .replace(/^\|(.+)\|$/gm, (match) => {
      const cells = match
        .split("|")
        .filter((c) => c.trim())
        .map((c) => c.trim());
      // Check if separator row
      if (cells.every((c) => /^[-:]+$/.test(c))) {
        return "<!--table-sep-->";
      }
      return `<tr>${cells.map((c) => `<td class="px-3 py-2 border-b border-rule text-sm">${c}</td>`).join("")}</tr>`;
    })
    // Wrap table rows
    .replace(
      /((?:<tr>.*<\/tr>\n?)+)/g,
      '<div class="overflow-x-auto my-4"><table class="w-full border-collapse">$1</table></div>'
    )
    .replace(/<!--table-sep-->\n?/g, "")
    // Unordered lists
    .replace(/^- (.+)$/gm, '<li class="ml-4 mb-1">$1</li>')
    .replace(/((?:<li[^>]*>.*<\/li>\n?)+)/g, '<ul class="list-disc pl-4 my-3 text-sm leading-relaxed">$1</ul>')
    // Numbered lists
    .replace(/^\d+\. (.+)$/gm, '<li class="ml-4 mb-1">$1</li>')
    // Paragraphs - wrap remaining text lines
    .replace(/^(?!<[hludtro]|<!\-\-)(.+)$/gm, '<p class="my-2 text-sm leading-relaxed text-ink-muted">$1</p>');

  return html;
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
