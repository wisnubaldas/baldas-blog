export const modul1 = [
  {
    key: "fa",
    name: "Finance & Accounting",
    description:
      "General Ledger (GL), Accounts Payable (AP), Accounts Receivable (AR) and other financial modules.",
    icon: "solar:document-add-broken",
    path: "https://app.wisnubaldas.net",
  },
  {
    key: "wms",
    name: "Inventory / Warehouse Management (WMS)",
    description:
      "Stock In / Stock Out and other warehouse management features.",
    icon: "mdi:radar",
    path: "/wms",
  },
  {
    key: "sales",
    name: "Sales Management",
    description: "Quotation, Sales Order, Invoicing and other sales features.",
    icon: "ph:air-traffic-control-duotone",
    path: "/sales",
  },
  {
    key: "purchase",
    name: "Purchasing / Procurement",
    description:
      "Purchase Order, Goods Receipt, Invoice Matching and other procurement features.",
    icon: "mdi:lan",
    path: "/purchase",
  },
  {
    key: "manufacturing",
    name: "Manufacturing",
    description:
      "Production Planning, Work Order, and other manufacturing features.",
    icon: "mdi:factory",
    path: "/manufacturing",
  },
  {
    key: "suplay-chain",
    name: "Supply Chain Management",
    description:
      "End-to-end supply chain management features including logistics and distribution.",
    icon: "mdi:truck-delivery",
    path: "/supply-chain",
  },
  {
    key: "hrm",
    name: "Human Resource Management (HRM)",
    description:
      "Employee records, payroll, attendance, and other HR management features.",
    icon: "mdi:account-group",
    path: "/hrm",
  },
];

export const apps = [
  {
    key: "finance",
    name: "Finance & Accounting",
    description:
      "General Ledger, Accounts Payable, Accounts Receivable, budgeting, tax management, and financial reporting.",
    icon: "mdi:finance",
    path: "https://app.wisnubaldas.net",
  },
  {
    key: "wms",
    name: "Inventory / Warehouse Management (WMS)",
    description:
      "Stock In / Stock Out, multi warehouse, barcode scanning, batch tracking, and real-time inventory reporting.",
    icon: "mdi:warehouse",
    path: "/wms",
  },
  {
    key: "sales",
    name: "Sales Management",
    description:
      "Quotation, Sales Order, Delivery Order, invoicing, customer management, and sales reporting.",
    icon: "mdi:cart-outline",
    path: "/sales",
  },
  {
    key: "purchasing",
    name: "Purchasing / Procurement",
    description:
      "Purchase Request, Purchase Order, vendor management, approval workflow, and goods receipt integration.",
    icon: "mdi:cart-arrow-down",
    path: "/purchasing",
  },
  {
    key: "manufacturing",
    name: "Manufacturing",
    description:
      "Bill of Material (BOM), production planning, work orders, MRP, and quality control.",
    icon: "mdi:factory",
    path: "/manufacturing",
  },
  {
    key: "logistics",
    name: "Logistics & Supply Chain",
    description:
      "Shipment management, tracking, fleet management, delivery scheduling, and EDI integration.",
    icon: "mdi:truck-outline",
    path: "/logistics",
  },
  {
    key: "hris",
    name: "Human Resource (HRIS)",
    description:
      "Employee management, attendance, payroll, leave management, recruitment, and performance evaluation.",
    icon: "mdi:account-group-outline",
    path: "/hris",
  },
  {
    key: "bi",
    name: "Business Intelligence (BI)",
    description:
      "KPI dashboards, financial analytics, sales analysis, inventory insights, and forecasting tools.",
    icon: "mdi:chart-line",
    path: "/bi",
  },
  {
    key: "dms",
    name: "Document Management System (DMS)",
    description:
      "Digital document storage, version control, approval workflow, audit trail, and secure access control.",
    icon: "mdi:file-document-outline",
    path: "/dms",
  },
  {
    key: "system",
    name: "System & Administration",
    description:
      "User management, RBAC, multi-company support, audit logs, notifications, and API integration.",
    icon: "mdi:cog-outline",
    path: "/system",
  },
];

export function getApp(keyOrPath) {
  return apps.find((app) => app.key === keyOrPath || app.path === keyOrPath);
}
