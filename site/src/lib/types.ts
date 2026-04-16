export interface Period {
  start: string;
  end: string;
}

export interface CommitteeStats {
  total_promises: number;
  delivered: number;
  partial: number;
  failed: number;
  recurring: number;
  delivery_rate: number;
}

export interface ReportHeader {
  committee: string;
  period: string;
  meetings_count: number;
  has_transcripts: boolean;
  generated: string;
}

export interface ReportSection {
  title: string;
  body: string;
}

export interface MemberData {
  name: string;
  attended: number;
  total: number;
  rate: number;
}

export type AiStatus = "delivered" | "partial" | "failed" | "recurring";
export type VerifiedStatus = "verified-delivered" | "disputed";

export interface EvidenceSubmission {
  url: string;
  type: "recording" | "doc" | "pr" | "screenshot" | "other";
  submitted_by: string;
  submitted_at: string;
  note?: string;
  accepted: boolean;
}

export interface PromiseData {
  num: number;
  promise: string;
  made_by: string;
  first_promised: string;
  repeated: string;
  status: AiStatus;
  evidence: string;
  verified_status?: VerifiedStatus;
  evidence_submissions?: EvidenceSubmission[];
}

export interface ReportData {
  available: boolean;
  header?: ReportHeader;
  sections?: ReportSection[];
  members?: MemberData[];
  promises?: PromiseData[];
}

export interface CommitteeData {
  committee: string;
  full_name: string;
  period: Period;
  meetings_count: number;
  summary_count: number;
  transcript_count: number;
  has_transcripts: boolean;
  dates: string[];
  reports: {
    summaries_vs_transcripts: ReportData;
    member_participation: ReportData;
    leadership_assessment: ReportData;
    promises_vs_reality: ReportData;
    critical_observations: ReportData;
  };
  stats: CommitteeStats;
  generated: string;
  needs_rerun?: boolean;
  report_period_inferred?: number;
}

export interface IndexCommittee {
  id: string;
  name: string;
  period: Period;
  meetings_count: number;
  has_transcripts: boolean;
  report_count: number;
  stats: CommitteeStats;
}

export interface IndexData {
  generated: string;
  committees: IndexCommittee[];
}
