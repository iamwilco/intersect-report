"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

interface NavLink {
  href: string;
  label: string;
}

interface MastheadNavProps {
  links: NavLink[];
  basePath?: string;
}

export default function MastheadNav({ links, basePath = "" }: MastheadNavProps) {
  const pathname = usePathname();

  return (
    <nav className="masthead-nav">
      {links.map((link) => {
        const fullHref = `${basePath}${link.href}`;
        const isActive =
          pathname === fullHref ||
          (fullHref === "/" && pathname === "/") ||
          (fullHref !== "/" && pathname === fullHref);

        return (
          <Link
            key={fullHref}
            href={fullHref}
            className={isActive ? "active" : undefined}
          >
            {link.label}
          </Link>
        );
      })}
    </nav>
  );
}
