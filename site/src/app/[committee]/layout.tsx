import { notFound } from "next/navigation";
import { getCommitteeData } from "@/lib/data";
import { COMMITTEE_NAV_LINKS } from "@/lib/constants";
import { formatPeriod } from "@/lib/markdown";
import MastheadNav from "@/components/layout/MastheadNav";

export default async function CommitteeLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ committee: string }>;
}) {
  const { committee } = await params;
  const data = getCommitteeData(committee);

  if (!data) {
    notFound();
  }

  const navLinks = COMMITTEE_NAV_LINKS.map((link) => ({
    href: `/${committee}${link.href}`,
    label: link.label,
  }));

  const periodStr = formatPeriod(data.period.start, data.period.end);

  return (
    <>
      <header className="masthead">
        <div className="masthead-top">
          <span className="masthead-kicker">
            Intersect — {data.full_name}
          </span>
          <span className="masthead-date">
            Season {periodStr} &middot; {data.meetings_count} Meetings
          </span>
        </div>
        <div className="masthead-main">
          <h1 className="masthead-title">
            {committee.toUpperCase()} Public Reports
          </h1>
          <p className="masthead-subtitle">
            Independent analysis of committee meetings, governance &amp;
            accountability
          </p>
        </div>
        <MastheadNav links={navLinks} />
      </header>
      {children}
    </>
  );
}
