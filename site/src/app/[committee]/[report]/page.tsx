import Link from "next/link";
import type { Metadata } from "next";
import { getCommitteeData, getIndexData } from "@/lib/data";
import {
  REPORT_SLUG_MAP,
  REPORT_TITLES,
  REPORT_NUMBERS,
  ALL_REPORT_SLUGS,
} from "@/lib/constants";
import { renderMarkdown, formatDate } from "@/lib/markdown";
import type { ReportData, ReportSection, PromiseData } from "@/lib/types";

/* ── Static params ── */

export async function generateStaticParams() {
  const index = getIndexData();
  const reports = ALL_REPORT_SLUGS;
  return index.committees
    .filter((c) => c.report_count > 0)
    .flatMap((c) =>
      reports.map((report) => ({
        committee: c.id.toLowerCase(),
        report,
      }))
    );
}

/* ── Metadata ── */

export async function generateMetadata({
  params,
}: {
  params: Promise<{ committee: string; report: string }>;
}): Promise<Metadata> {
  const { committee, report } = await params;
  const data = getCommitteeData(committee);
  const title = REPORT_TITLES[report] || report;
  return {
    title: `${title} — ${data?.committee || committee.toUpperCase()} Reports`,
  };
}

/* ── Helpers ── */

function SectionBlock({ section }: { section: ReportSection }) {
  return (
    <section className="mb-12">
      <h3
        className="font-serif font-bold text-xl mt-10 mb-4"
        style={{ borderBottom: "1px solid var(--color-rule)", paddingBottom: 6 }}
      >
        {section.title}
      </h3>
      <div dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }} />
    </section>
  );
}

function PromiseStatStrip({ promises }: { promises: PromiseData[] }) {
  const effective = (p: PromiseData) =>
    p.verified_status === "verified-delivered" ? "delivered" : p.status;
  const delivered = promises.filter((p) => effective(p) === "delivered").length;
  const partial = promises.filter((p) => effective(p) === "partial").length;
  const failed = promises.filter((p) => effective(p) === "failed").length;
  const recurring = promises.filter((p) => effective(p) === "recurring").length;
  const verifiedCount = promises.filter((p) => p.verified_status === "verified-delivered").length;

  return (
    <div className="stat-strip">
      <div className="stat-item">
        <span className="stat-num" style={{ color: "var(--color-teal)" }}>
          {delivered}
        </span>
        <span className="stat-label">Delivered</span>
      </div>
      <div className="stat-item">
        <span className="stat-num" style={{ color: "var(--color-amber)" }}>
          {partial}
        </span>
        <span className="stat-label">Partial</span>
      </div>
      <div className="stat-item">
        <span className="stat-num" style={{ color: "var(--color-accent)" }}>
          {failed}
        </span>
        <span className="stat-label">Failed</span>
      </div>
      <div className="stat-item">
        <span className="stat-num" style={{ color: "var(--color-purple)" }}>
          {recurring}
        </span>
        <span className="stat-label">Recurring</span>
      </div>
      {verifiedCount > 0 && (
        <div className="stat-item">
          <span className="stat-num" style={{ color: "var(--color-teal)" }}>
            {verifiedCount}
          </span>
          <span className="stat-label">✓ Verified by evidence</span>
        </div>
      )}
    </div>
  );
}

const REPO_ISSUES = "https://github.com/iamwilco/intersect-report/issues/new";

function evidenceIssueUrl(committee: string, p: PromiseData) {
  const params = new URLSearchParams({
    template: "evidence-submission.yml",
    title: `[Evidence] ${committee} #${p.num}: ${p.promise.slice(0, 60)}`,
    "promise-id": `${committee}#${p.num}`,
    "promise-quote": p.promise,
  });
  return `${REPO_ISSUES}?${params.toString()}`;
}

function StatusCell({ p }: { p: PromiseData }) {
  const verified = p.verified_status === "verified-delivered";
  const disputed = p.verified_status === "disputed";
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
      <span className={`status-pill s-${p.status}`}>{p.status}</span>
      {verified && (
        <span className="status-pill s-delivered" title="Evidence reviewed and accepted">
          ✓ verified
        </span>
      )}
      {disputed && (
        <span className="status-pill s-partial" title="Conflicting claims under review">
          ⚠ disputed
        </span>
      )}
    </div>
  );
}

function EvidenceCell({ committee, p }: { committee: string; p: PromiseData }) {
  const subs = p.evidence_submissions ?? [];
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
      <span>{p.evidence}</span>
      {subs.length > 0 && (
        <ul style={{ margin: 0, paddingLeft: 16, fontSize: "0.85em" }}>
          {subs.map((s, i) => (
            <li key={i}>
              <a href={s.url} target="_blank" rel="noopener noreferrer">
                {s.type}
              </a>{" "}
              — {s.submitted_by}
            </li>
          ))}
        </ul>
      )}
      <a
        href={evidenceIssueUrl(committee, p)}
        target="_blank"
        rel="noopener noreferrer"
        style={{ fontSize: "0.8em", textDecoration: "underline" }}
      >
        Submit evidence
      </a>
    </div>
  );
}

function EvidenceDisclaimer() {
  return (
    <div
      className="verdict-box"
      style={{
        background: "var(--color-surface, #f8f8f5)",
        border: "1px solid var(--color-rule)",
        padding: "12px 16px",
        marginBottom: 16,
        fontSize: "0.9em",
      }}
    >
      <strong>Note on delivery status:</strong> AI status reflects what is
      findable in the public meeting transcripts only. Off-transcript work
      (workshops, async deliveries, side-channels) won&rsquo;t be captured here.
      Committee members and the public can submit evidence via the{" "}
      <em>Submit evidence</em> link on each row, or email{" "}
      <a href="mailto:chat@wilco.space">chat@wilco.space</a>. Verified items
      get a ✓ badge with a link to the artifact.
    </div>
  );
}

function PromiseTable({ committee, promises }: { committee: string; promises: PromiseData[] }) {
  return (
    <div className="overflow-x-auto mb-12">
      <EvidenceDisclaimer />
      <table className="data-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Promise</th>
            <th>Made by</th>
            <th>Date</th>
            <th>Status</th>
            <th>Evidence</th>
          </tr>
        </thead>
        <tbody>
          {promises.map((p) => (
            <tr key={p.num}>
              <td>{p.num}</td>
              <td>{p.promise}</td>
              <td>{p.made_by}</td>
              <td style={{ whiteSpace: "nowrap" }}>{p.first_promised}</td>
              <td><StatusCell p={p} /></td>
              <td><EvidenceCell committee={committee} p={p} /></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

/* ── Renderers per report type ── */

function renderSummariesVsTranscripts(sections: ReportSection[]) {
  const lastSection = sections[sections.length - 1];
  const isOverallPatterns =
    lastSection && lastSection.title.toLowerCase().includes("overall pattern");

  const regularSections = isOverallPatterns
    ? sections.slice(0, -1)
    : sections;

  return (
    <>
      {regularSections.map((section, i) => (
        <SectionBlock key={i} section={section} />
      ))}
      {isOverallPatterns && lastSection && (
        <div className="verdict-box verdict-negative">
          <h4>{lastSection.title}</h4>
          <div
            dangerouslySetInnerHTML={{
              __html: renderMarkdown(lastSection.body),
            }}
          />
        </div>
      )}
    </>
  );
}

function renderMemberAnalysis(sections: ReportSection[]) {
  return (
    <>
      {sections.map((section, i) => (
        <SectionBlock key={i} section={section} />
      ))}
    </>
  );
}

function renderLeadership(sections: ReportSection[]) {
  return (
    <>
      {sections.map((section, i) => (
        <SectionBlock key={i} section={section} />
      ))}
    </>
  );
}

function renderPromises(report: ReportData, committee: string) {
  return (
    <>
      {report.promises && report.promises.length > 0 && (
        <>
          <PromiseStatStrip promises={report.promises} />
          <PromiseTable committee={committee} promises={report.promises} />
        </>
      )}
      {report.sections &&
        report.sections.map((section, i) => (
          <SectionBlock key={i} section={section} />
        ))}
    </>
  );
}

function renderCriticalObservations(sections: ReportSection[]) {
  return (
    <>
      {sections.map((section, i) => (
        <SectionBlock key={i} section={section} />
      ))}
    </>
  );
}

function renderMeetings(dates: string[]) {
  return (
    <div className="overflow-x-auto">
      <table className="data-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {dates.map((date, i) => (
            <tr key={date}>
              <td>{i + 1}</td>
              <td>{formatDate(date)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

/* ── Page ── */

export default async function ReportPage({
  params,
}: {
  params: Promise<{ committee: string; report: string }>;
}) {
  const { committee, report } = await params;
  const data = getCommitteeData(committee);

  if (!data) {
    return (
      <div className="page-wrap">
        <Link href="/" className="back-link">
          &larr; Back to committees
        </Link>
        <p>Committee not found.</p>
      </div>
    );
  }

  const reportTitle = REPORT_TITLES[report] || report;
  const reportNumber = REPORT_NUMBERS[report] || "00";

  /* Resolve report data */
  const reportKey = REPORT_SLUG_MAP[report];
  const reportData = reportKey
    ? (data.reports[reportKey as keyof typeof data.reports] as ReportData)
    : null;

  const isMeetings = report === "meetings";

  if (!isMeetings && (!reportData || !reportData.available)) {
    return (
      <div className="page-wrap">
        <Link href={`/${committee}`} className="back-link">
          &larr; Back to {data.committee}
        </Link>
        <div className="section-header">
          <span className="section-number">Report {reportNumber}</span>
          <h1 className="section-title">{reportTitle}</h1>
        </div>
        <p>This report is not yet available for {data.committee}.</p>
      </div>
    );
  }

  return (
    <div className="page-wrap">
      <Link href={`/${committee}`} className="back-link">
        &larr; Back to {data.committee}
      </Link>

      <div className="section-header">
        <span className="section-number">Report {reportNumber}</span>
        <h1 className="section-title">{reportTitle}</h1>
      </div>

      {/* Render by report type */}
      {report === "summaries-vs-transcripts" &&
        reportData?.sections &&
        renderSummariesVsTranscripts(reportData.sections)}

      {report === "member-analysis" &&
        reportData?.sections &&
        renderMemberAnalysis(reportData.sections)}

      {report === "leadership" &&
        reportData?.sections &&
        renderLeadership(reportData.sections)}

      {report === "promises" && reportData && renderPromises(reportData, data.committee)}

      {report === "critical-observations" &&
        reportData?.sections &&
        renderCriticalObservations(reportData.sections)}

      {report === "meetings" && renderMeetings(data.dates)}
    </div>
  );
}
