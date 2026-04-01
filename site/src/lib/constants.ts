export const REPORT_SLUG_MAP: Record<string, string> = {
  "summaries-vs-transcripts": "summaries_vs_transcripts",
  "member-analysis": "member_participation",
  "leadership": "leadership_assessment",
  "promises": "promises_vs_reality",
  "critical-observations": "critical_observations",
};

export const REPORT_TITLES: Record<string, string> = {
  "summaries-vs-transcripts": "Summaries vs. Transcripts",
  "member-analysis": "Member Participation",
  "leadership": "Leadership Assessment",
  "promises": "Promises vs. Reality",
  "critical-observations": "Critical Observations",
  "meetings": "Meeting Index",
};

export const REPORT_NUMBERS: Record<string, string> = {
  "summaries-vs-transcripts": "01",
  "member-analysis": "02",
  "leadership": "03",
  "promises": "04",
  "critical-observations": "05",
  "meetings": "06",
};

export const REPORT_TAGS: Record<string, { label: string; color: string }> = {
  "summaries-vs-transcripts": { label: "Truth Audit", color: "accent" },
  "member-analysis": { label: "Analysis", color: "teal" },
  "leadership": { label: "Analysis", color: "teal" },
  "promises": { label: "Accountability", color: "amber" },
  "critical-observations": { label: "Observations", color: "purple" },
  "meetings": { label: "Reference", color: "ink-muted" },
};

export const REPORT_DESCRIPTIONS: Record<string, string> = {
  "summaries-vs-transcripts":
    "Forensic comparison of official summaries against raw transcripts. Identifies fabricated decisions, invented action items, and omitted conflicts.",
  "member-analysis":
    "Attendance records and qualitative analysis for all elected members. Speaking frequency, contributions, and effectiveness rankings.",
  "leadership":
    "Chair, Vice Chair, and Secretary evaluated on facilitation, decision-making, preparation, and boundary respect.",
  "promises":
    "Every commitment tracked from source to outcome. Delivery rate calculated with most and least reliable promise-keepers identified.",
  "critical-observations":
    "Free-form governance report covering red flags, cultural dynamics, information asymmetry, and recurring failures.",
  "meetings":
    "Complete index of all meetings with dates, key topics, and attendance.",
};

export const COMMITTEE_NAV_LINKS = [
  { href: "", label: "Overview" },
  { href: "/summaries-vs-transcripts", label: "Summaries vs. Transcripts" },
  { href: "/member-analysis", label: "Member Participation" },
  { href: "/leadership", label: "Leadership Assessment" },
  { href: "/promises", label: "Promises vs. Reality" },
  { href: "/critical-observations", label: "Critical Observations" },
  { href: "/meetings", label: "Meeting Index" },
];

export const ALL_REPORT_SLUGS = [
  "summaries-vs-transcripts",
  "member-analysis",
  "leadership",
  "promises",
  "critical-observations",
  "meetings",
];
