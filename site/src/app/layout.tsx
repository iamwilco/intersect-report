import type { Metadata } from "next";
import { Playfair_Display, DM_Sans, DM_Mono } from "next/font/google";
import "./globals.css";

const playfair = Playfair_Display({
  subsets: ["latin"],
  variable: "--font-playfair",
  weight: ["400", "700", "900"],
  display: "swap",
});

const dmSans = DM_Sans({
  subsets: ["latin"],
  variable: "--font-dm-sans",
  weight: ["300", "400", "500"],
  style: ["normal", "italic"],
  display: "swap",
});

const dmMono = DM_Mono({
  subsets: ["latin"],
  variable: "--font-dm-mono",
  weight: ["400"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "Intersect Committee Reports — Independent Governance Analysis",
  description:
    "Independent, evidence-based analysis of Intersect MBO committee performance & accountability. All findings grounded in official meeting transcripts.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${playfair.variable} ${dmSans.variable} ${dmMono.variable}`}
    >
      <body>
        {children}
        <footer className="site-footer">
          <p>
            Intersect Committee Reports &middot; Independent governance analysis
          </p>
          <p>
            Built with the Intersect Committee Performance Analysis Pipeline
          </p>
        </footer>
      </body>
    </html>
  );
}
