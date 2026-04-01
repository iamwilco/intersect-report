import Link from "next/link";
import { getIndexData } from "@/lib/data";
import type { IndexCommittee } from "@/lib/types";
import MastheadNav from "@/components/layout/MastheadNav";

function CommitteeCard({ committee }: { committee: IndexCommittee }) {
  const hasReports = committee.report_count > 0;
  const href = `/${committee.id.toLowerCase()}`;
  const totalReports = 5;

  const inner = (
    <>
      <span className="committee-card-code">{committee.id}</span>
      <span className="committee-card-name">{committee.name}</span>
      <div className="committee-card-meta">
        {hasReports ? (
          <>
            <span className="committee-card-stat">
              <strong>{committee.meetings_count}</strong> meetings
            </span>
            {committee.stats.delivery_rate > 0 && (
              <span className="committee-card-stat">
                <strong>{committee.stats.delivery_rate}%</strong> delivery rate
              </span>
            )}
          </>
        ) : (
          <span className="committee-card-stat">Awaiting analysis</span>
        )}
      </div>
      <div className="committee-card-reports">
        {Array.from({ length: totalReports }).map((_, i) => (
          <span
            key={i}
            className={`committee-card-pip${i < committee.report_count ? "" : " empty"}`}
          />
        ))}
      </div>
      {hasReports && <span className="committee-card-arrow">&rarr;</span>}
    </>
  );

  if (hasReports) {
    return (
      <Link className="committee-card" href={href}>
        {inner}
      </Link>
    );
  }

  return <div className="committee-card no-data">{inner}</div>;
}

export default function HomePage() {
  const data = getIndexData();
  const committeesWithReports = data.committees.filter(
    (c) => c.report_count > 0
  );

  const navLinks = [
    { href: "/", label: "All Committees" },
    ...committeesWithReports.map((c) => ({
      href: `/${c.id.toLowerCase()}`,
      label: `${c.id} Reports`,
    })),
  ];

  return (
    <>
      <header className="masthead">
        <div className="masthead-top">
          <span className="masthead-kicker">
            Intersect MBO — Committee Governance Analysis
          </span>
          <span className="masthead-date">2025–2026 Season</span>
        </div>
        <div className="masthead-main">
          <h1 className="masthead-title">Intersect Committee Reports</h1>
          <p className="masthead-subtitle">
            Independent, evidence-based analysis of committee performance &amp;
            accountability
          </p>
        </div>
        <MastheadNav links={navLinks} />
      </header>

      <main className="page-wrap">
        {/* Intro block */}
        <div className="intro-block">
          <div>
            <p className="intro-lede">
              This site publishes independent analysis of{" "}
              <strong>Intersect MBO committee governance</strong> — examining
              whether official records accurately reflect what was discussed, how
              elected members participated, whether commitments were followed
              through, and whether non-elected staff stayed within their defined
              roles.
            </p>
            <br />
            <p
              style={{
                fontSize: "14px",
                color: "var(--color-ink-muted)",
                lineHeight: 1.8,
              }}
            >
              Every finding is grounded in the official meeting transcripts and
              summaries. The analysis pipeline processes raw committee records
              through five structured prompts, producing evidence-based reports on
              each committee&apos;s performance. Reports cover: truth audits of
              official summaries, member participation analysis, leadership
              assessment, promise tracking, and critical observations.
            </p>
          </div>
          <div className="intro-meta">
            <div className="intro-meta-item">
              <span className="intro-meta-label">Scope</span>
              <span className="intro-meta-value">8 Intersect committees</span>
            </div>
            <div className="intro-meta-item">
              <span className="intro-meta-label">Analysis types</span>
              <span className="intro-meta-value">
                5 structured report prompts per committee
              </span>
            </div>
            <div className="intro-meta-item">
              <span className="intro-meta-label">Source material</span>
              <span className="intro-meta-value">
                Official transcripts &amp; meeting summaries
              </span>
            </div>
            <div className="intro-meta-item">
              <span className="intro-meta-label">Method</span>
              <span className="intro-meta-value">
                Systematic evidence-based analysis via Anthropic API
              </span>
            </div>
          </div>
        </div>

        {/* Section 01: The Five Reports */}
        <div className="section-header">
          <span className="section-number">01</span>
          <h2 className="section-title">The Five Reports</h2>
        </div>

        <div className="findings-grid" style={{ marginBottom: "56px" }}>
          <div className="finding-box">
            <h4 className="finding-title">01 — Summaries vs. Transcripts</h4>
            <ul className="finding-list">
              <li>
                Forensic comparison of official summaries against raw transcripts
              </li>
              <li>
                Identifies fabricated decisions, invented action items, tone
                laundering
              </li>
              <li>
                Flags omitted conflicts and sanitised accountability failures
              </li>
              <li>
                Requires transcripts — skipped for summaries-only committees
              </li>
            </ul>
          </div>
          <div className="finding-box">
            <h4 className="finding-title">02 — Member Participation</h4>
            <ul className="finding-list">
              <li>
                Attendance grid for every elected member across all meetings
              </li>
              <li>
                Speaking frequency, substantive contributions, between-meeting work
              </li>
              <li>Power dynamics — who dominates, who is sidelined</li>
              <li>
                Ranked from most to least effective with transcript evidence
              </li>
            </ul>
          </div>
          <div className="finding-box">
            <h4 className="finding-title">03 — Leadership Assessment</h4>
            <ul className="finding-list">
              <li>
                Chair: facilitation, decision-making, preparation, conflict
                management
              </li>
              <li>
                Vice Chair: support role, independent contributions,
                accountability
              </li>
              <li>
                Secretary: minutes accuracy, boundary respect, tool management
              </li>
              <li>Overall verdict on whether the committee is well-led</li>
            </ul>
          </div>
          <div className="finding-box">
            <h4 className="finding-title">04 — Promises vs. Reality</h4>
            <ul className="finding-list">
              <li>
                Every commitment and action item tracked from source to outcome
              </li>
              <li>
                Delivery rate calculated — delivered, partial, failed, recurring
              </li>
              <li>Most and least reliable promise-keepers identified</li>
              <li>
                Assessment of whether the committee delivers value to Cardano
              </li>
            </ul>
          </div>
        </div>

        {/* Section 02: Committees */}
        <div className="section-header">
          <span className="section-number">02</span>
          <h2 className="section-title">Committees</h2>
        </div>

        <div className="committee-grid">
          {data.committees.map((committee) => (
            <CommitteeCard key={committee.id} committee={committee} />
          ))}
        </div>

        {/* Section 03: How It Works */}
        <div className="section-header">
          <span className="section-number">03</span>
          <h2 className="section-title">How It Works</h2>
        </div>

        <div className="methodology-box">
          <h3>Analysis Pipeline</h3>
          <p>
            Committee meeting transcripts and summaries are processed through a
            structured Python pipeline using the Anthropic API. Each
            committee&apos;s source material is fed through five analysis prompts,
            producing independent reports with full audit trails.
          </p>
          <p>
            For committees with both transcripts and summaries, a forensic truth
            audit (Prompt 1) compares every summary against its corresponding
            transcript, identifying fabrications, omissions, and systematic biases.
            Prompts 2-5 analyse participation, leadership, promise delivery, and
            governance dynamics.
          </p>
          <p>
            Every API call is logged with its exact input, output, and token
            counts. Any finding can be verified by checking what the model actually
            received. The pipeline supports automatic chunking for large datasets
            and synthesis passes for multi-part analyses.
          </p>
        </div>

        <div className="methodology-box">
          <h3>Methodology &amp; Source Notes</h3>
          <p>
            All reports are based on official meeting transcripts and summaries
            sourced from Intersect&apos;s public documentation channels. Every
            factual claim is traceable to a specific transcript passage.
            Participation data is derived from transcript evidence — attendance
            lists in summaries are cross-referenced against actual speaking
            records.
          </p>
          <p>
            These reports represent independent community analysis and are not
            affiliated with Intersect or any official body.
          </p>
        </div>
      </main>
    </>
  );
}
