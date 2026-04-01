import fs from "fs";
import path from "path";
import type { IndexData, CommitteeData, ReportData } from "./types";
import { REPORT_SLUG_MAP } from "./constants";

const DATA_DIR = path.join(process.cwd(), "data");

export function getIndexData(): IndexData {
  const raw = fs.readFileSync(path.join(DATA_DIR, "index.json"), "utf-8");
  return JSON.parse(raw);
}

export function getCommitteeData(id: string): CommitteeData | null {
  const filePath = path.join(DATA_DIR, `${id.toLowerCase()}.json`);
  if (!fs.existsSync(filePath)) return null;
  const raw = fs.readFileSync(filePath, "utf-8");
  return JSON.parse(raw);
}

export function getReportData(
  committeeId: string,
  reportSlug: string
): ReportData | null {
  const data = getCommitteeData(committeeId);
  if (!data) return null;

  const key = REPORT_SLUG_MAP[reportSlug];
  if (!key) return null;

  const report = data.reports[key as keyof typeof data.reports];
  if (!report || !report.available) return null;

  return report;
}

export function getAllCommitteeIds(): string[] {
  const index = getIndexData();
  return index.committees
    .filter((c) => c.report_count > 0)
    .map((c) => c.id.toLowerCase());
}
