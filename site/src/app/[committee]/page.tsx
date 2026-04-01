import Link from "next/link";
import { notFound } from "next/navigation";
import { getCommitteeData, getAllCommitteeIds } from "@/lib/data";
import {
  ALL_REPORT_SLUGS,
  REPORT_TITLES,
  REPORT_DESCRIPTIONS,
  REPORT_NUMBERS,
  REPORT_TAGS,
  REPORT_SLUG_MAP,
} from "@/lib/constants";
import { formatPeriod } from "@/lib/markdown";
import type { CommitteeData } from "@/lib/types";

function DeliveryRateRing({ data }: { data: CommitteeData }) {
  const rate = data.stats.delivery_rate;
  const radius = 42;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (rate / 100) * circumference;

  return (
    <div className="progress-ring-wrap">
      <svg className="progress-ring" viewBox="0 0 100 100">
        <circle className="ring-bg" cx="50" cy="50" r={radius} />
        <circle
          className="ring-fg"
          cx="50"
          cy="50"
          r={radius}
          strokeDasharray={circumference}
          strokeDashoffset={offset}
        />
        <text className="progress-ring-label" x="50" y="50">
          ~{rate}%
        </text>
      </svg>
      <div className="progress-ring-meta">
        <div className="progress-ring-title">Promise Delivery Rate</div>
        <p style={{ fontSize: "14px", lineHeight: 1.7, color: "var(--color-ink-muted)" }}>
          Of {data.stats.total_promises} commitments tracked across{" "}
          {data.meetings_count} meetings, {data.stats.delivered} were fully
          delivered. {data.stats.partial} were partially delivered and{" "}
          {data.stats.failed} were not delivered. The committee&apos;s delivery
          rate is{" "}
          <strong style={{ color: "var(--color-accent)" }}>~{rate}%</strong>.
        </p>
      </div>
    </div>
  );
}

function ReportCard({
  slug,
  committee,
  available,
}: {
  slug: string;
  committee: string;
  available: boolean;
}) {
  const title = REPORT_TITLES[slug];
  const desc = REPORT_DESCRIPTIONS[slug];
  const num = REPORT_NUMBERS[slug];
  const tag = REPORT_TAGS[slug];
  const href = `/${committee}/${slug}`;

  if (!available) {
    return (
      <div
        className="report-card"
        style={{ opacity: 0.5, pointerEvents: "none" }}
      >
        <span className="report-card-num">Report {num}</span>
        <h3 className="report-card-title">{title}</h3>
        <p className="report-card-desc">{desc}</p>
        <span className={`report-card-tag tag-${tag.color}`}>{tag.label}</span>
      </div>
    );
  }

  return (
    <Link className="report-card" href={href}>
      <span className="report-card-num">Report {num}</span>
      <h3 className="report-card-title">{title}</h3>
      <p className="report-card-desc">{desc}</p>
      <span className={`report-card-tag tag-${tag.color}`}>{tag.label}</span>
      <span className="report-card-arrow">&rarr;</span>
    </Link>
  );
}

export default async function CommitteeOverviewPage({
  params,
}: {
  params: Promise<{ committee: string }>;
}) {
  const { committee } = await params;
  const data = getCommitteeData(committee);

  if (!data) {
    notFound();
  }

  const periodStr = formatPeriod(data.period.start, data.period.end);

  // Determine which reports are available
  const reportAvailability: Record<string, boolean> = {};
  for (const slug of ALL_REPORT_SLUGS) {
    if (slug === "meetings") {
      // Meetings page is always available if committee has data
      reportAvailability[slug] = true;
    } else {
      const key = REPORT_SLUG_MAP[slug];
      if (key) {
        const report = data.reports[key as keyof typeof data.reports];
        reportAvailability[slug] = report?.available ?? false;
      } else {
        reportAvailability[slug] = false;
      }
    }
  }

  const availableReportCount = Object.values(reportAvailability).filter(Boolean).length;

  return (
    <main className="page-wrap">
      <Link href="/" className="back-link">
        &larr; All committees
      </Link>

      {/* Intro block */}
      <div className="intro-block">
        <div>
          <p className="intro-lede">
            This section publishes independent analysis of the{" "}
            <strong>
              Intersect {data.full_name} ({data.committee})
            </strong>{" "}
            — covering {data.meetings_count} public meetings from{" "}
            {periodStr.replace(" \u2192 ", " to ")}. All findings are grounded in
            the official meeting{" "}
            {data.has_transcripts ? "transcripts" : "summaries"}.
          </p>
          <br />
          <p
            style={{
              fontSize: "14px",
              color: "var(--color-ink-muted)",
              lineHeight: 1.8,
            }}
          >
            The reports examine whether official summaries accurately reflect what
            was discussed, how elected members participated, whether leadership
            fulfilled its responsibilities, whether commitments made in meetings
            were followed through, and whether governance structures served the
            community or entrenched institutional control.
          </p>
        </div>
        <div className="intro-meta">
          <div className="intro-meta-item">
            <span className="intro-meta-label">Committee</span>
            <span className="intro-meta-value">{data.full_name}</span>
          </div>
          <div className="intro-meta-item">
            <span className="intro-meta-label">Period covered</span>
            <span className="intro-meta-value">{periodStr}</span>
          </div>
          <div className="intro-meta-item">
            <span className="intro-meta-label">Meetings analysed</span>
            <span className="intro-meta-value">
              {data.meetings_count} public meetings
            </span>
          </div>
          <div className="intro-meta-item">
            <span className="intro-meta-label">Source material</span>
            <span className="intro-meta-value">
              Official {data.has_transcripts ? "transcripts & meeting summaries" : "meeting summaries"}
            </span>
          </div>
        </div>
      </div>

      {/* Stat strip */}
      <div className="stat-strip">
        <div className="stat-item">
          <span className="stat-num">{data.meetings_count}</span>
          <span className="stat-label">Meetings analysed</span>
        </div>
        <div className="stat-item">
          <span className="stat-num" style={{ color: "var(--color-teal)" }}>
            {data.has_transcripts ? data.transcript_count : data.summary_count}
          </span>
          <span className="stat-label">
            {data.has_transcripts ? "Transcripts processed" : "Summaries processed"}
          </span>
        </div>
        <div className="stat-item">
          <span className="stat-num" style={{ color: "var(--color-amber)" }}>
            {data.stats.delivery_rate > 0 ? `~${data.stats.delivery_rate}%` : "N/A"}
          </span>
          <span className="stat-label">Promise delivery rate</span>
        </div>
        <div className="stat-item">
          <span className="stat-num" style={{ color: "var(--color-accent)" }}>
            {availableReportCount}
          </span>
          <span className="stat-label">Reports published</span>
        </div>
      </div>

      {/* Delivery rate ring (only if stats exist) */}
      {data.stats.delivery_rate > 0 && <DeliveryRateRing data={data} />}

      {/* Reports section */}
      <div className="section-header">
        <span className="section-number">01</span>
        <h2 className="section-title">Reports</h2>
      </div>

      <div className="reports-grid">
        {ALL_REPORT_SLUGS.map((slug) => (
          <ReportCard
            key={slug}
            slug={slug}
            committee={committee}
            available={reportAvailability[slug]}
          />
        ))}
      </div>
    </main>
  );
}

export function generateStaticParams() {
  const ids = getAllCommitteeIds();
  return ids.map((id) => ({ committee: id }));
}
