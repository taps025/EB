import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Employee Benefits", layout="wide")

st.markdown(
    """
    <style>
      .stApp { background: #efefef; }
      h1 { color: #111111 !important; text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="minet-banner">
      <div class="minet-hero">
        <div class="minet-hero-title">EMPLOYEE BENEFITS</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

revenue_distribution = [
    ("Healthcare", 1_000_000),
    ("BOMAID", 625_000),
    ("Dread Disease (BPOPF)", 380_000),
    ("Tardiue", 195_000),
    ("Northside Primary", 120_000),
    ("Winners Chapel", 100_000),
    ("Hospital Cash Plan", 85_500),
    ("KFC", 48_000),
    ("Woolworths", 40_000),
    ("Livingstone Kolobeng", 26_000),
    ("AFSV", 25_000),
    ("Oxy Gas", 25_000),
    ("Nandos", 23_000),
    ("Legal Guard", 20_000),
]

client_notes = {
    "BOMAID": "Embedded GFS.",
    "Legal Guard": "Embedded GFS. Embedded funeral to the existing policy holders.",
    "AFSV": "Embedded GFS. Embedded funeral to the free standing fund.",
    "Healthcare": "Sharing Minet target lists with all OracleMed for joint presentations. Converting OracleMed's business written on non-admitted basis to brokered portfolios through Minet.",
    "Hospital Cash Plan": "Embed hospital cash plan to BPOPF fund members.",
    "Dread Disease (BPOPF)": "Optional DD to BPOPF fund members.",
    "Northside Primary": "Proposal shared with client.",
    "Tardiue": "Proposal shared with client.",
    "Oxy Gas": "Contacts for a key personnel.",
    "Winners Chapel": "Contacts for a key personnel.",
    "Woolworths": "Contacts for a key personnel.",
    "Nandos": "Contacts for a key personnel.",
    "KFC": "Lost in 2023, pursuing client, renews in November.",
    "Livingstone Kolobeng": "Proposal shared with client.",
}

high_value_progress = [
    {"name": "Healthcare", "progress": 86, "prob": 80, "value": 195_000},
    {"name": "BOMAID", "progress": 86, "prob": 50, "value": 625_000},
    {"name": "Dread Disease (BPOPF)", "progress": 71, "prob": 50, "value": 380_000},
    {"name": "Hospital Cash Plan (BPOPF)", "progress": 71, "prob": 50, "value": 85_500},
]

early_stage = [
    "Oxy Gas",
    "Livingstone Kolobeng",
    "MP Mining",
    "Winners Chapel",
    "Woolworths",
    "Nandos",
    "KFC",
]

max_revenue = max(value for _, value in revenue_distribution)
total_revenue = sum(value for _, value in revenue_distribution)
def _escape_attr(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

revenue_rows = "\n".join(
    f"""
    <button class="row stat-row" data-name="{_escape_attr(name)}" data-value="{value}" data-share="{value / total_revenue * 100:.1f}" data-note="{_escape_attr(client_notes.get(name, ''))}">
      <div class="label">{name}</div>
      <div class="bar"><span style="width:{int(value / max_revenue * 100)}%"></span></div>
      <div class="value">{value:,.0f}</div>
    </button>
    """
    for name, value in revenue_distribution
)

max_value = max(item["value"] for item in high_value_progress)
high_value_rows = "\n".join(
    f"""
    <div class="row">
      <div class="label">{item['name']}</div>
      <div class="bar"><span style="width:{int(item['progress'])}%"></span></div>
      <div class="value">{item['progress']}% | {item['prob']}% | {item['value']:,.0f}</div>
    </div>
    """
    for item in high_value_progress
)

early_rows = "\n".join(
    f"""
    <div class="row compact">
      <div class="label">{name}</div>
      <div class="bar"><span style="width:40%"></span></div>
      <div class="value">40%</div>
    </div>
    """
    for name in early_stage
)

html = f"""
<div class="journey-board">
  <div class="journey-tabs" role="tablist">
    <button class="journey-tab active" data-target="tab-prospects" role="tab" aria-selected="true">Prospects</button>
    <button class="journey-tab" data-target="tab-pipeline" role="tab" aria-selected="false">Pipeline Progress</button>
  </div>

  <div class="journey-panel active" id="tab-prospects" role="tabpanel">
    <div class="journey-title">Prospects</div>
    <div class="tree-map">
      <button class="tree-root-box" id="prospects-toggle" type="button" aria-expanded="false" onclick="toggleProspects()">Prospects</button>
      <div class="tree-branches is-collapsed" id="prospects-branches">
        <div class="connector-col">
          <div class="v-line"></div>
          <div class="h-line-row"><span class="h-line"></span></div>
          <div class="h-line-row"><span class="h-line"></span></div>
          <div class="h-line-row"><span class="h-line"></span></div>
        </div>
        <div class="branches-col">
        <div class="tree-branch-card">
          <button class="branch-title" type="button" data-target="all-prospects-panel" aria-expanded="false" onclick="toggleBranch('all-prospects-panel', this)">All Prospects</button>
          <div class="branch-panel is-collapsed" id="all-prospects-panel">
            <table class="prospects-table">
              <thead>
                <tr>
                  <th>Prospect</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                <tr onclick="selectProspect('Healthcare')" data-name="Healthcare"><td>Healthcare</td><td>1,000,000</td></tr>
                <tr onclick="selectProspect('BOMAID')" data-name="BOMAID"><td>BOMAID</td><td>625,000</td></tr>
                <tr onclick="selectProspect('Dread Disease (BPOPF)')" data-name="Dread Disease (BPOPF)"><td>Dread Disease (BPOPF)</td><td>380,000</td></tr>
                <tr onclick="selectProspect('Tardiue')" data-name="Tardiue"><td>Tardiue</td><td>195,000</td></tr>
                <tr onclick="selectProspect('Northside Primary')" data-name="Northside Primary"><td>Northside Primary</td><td>120,000</td></tr>
                <tr onclick="selectProspect('Winners Chapel')" data-name="Winners Chapel"><td>Winners Chapel</td><td>100,000</td></tr>
                <tr onclick="selectProspect('Hospital Cash Plan')" data-name="Hospital Cash Plan"><td>Hospital Cash Plan</td><td>85,500</td></tr>
                <tr onclick="selectProspect('KFC')" data-name="KFC"><td>KFC</td><td>48,000</td></tr>
                <tr onclick="selectProspect('Woolworths')" data-name="Woolworths"><td>Woolworths</td><td>40,000</td></tr>
                <tr onclick="selectProspect('Livingstone Kolobeng')" data-name="Livingstone Kolobeng"><td>Livingstone Kolobeng</td><td>26,000</td></tr>
                <tr onclick="selectProspect('AFSV')" data-name="AFSV"><td>AFSV</td><td>25,000</td></tr>
                <tr onclick="selectProspect('Oxy Gas')" data-name="Oxy Gas"><td>Oxy Gas</td><td>25,000</td></tr>
                <tr onclick="selectProspect('Nandos')" data-name="Nandos"><td>Nandos</td><td>23,000</td></tr>
                <tr onclick="selectProspect('Legal Guard')" data-name="Legal Guard"><td>Legal Guard</td><td>20,000</td></tr>
                <tr onclick="selectProspect('Medical Aid Scheme')" data-name="Medical Aid Scheme"><td>Medical Aid Scheme</td><td>—</td></tr>
              </tbody>
            </table>
            <div class="prospect-detail" id="prospect-detail">
              <div class="stat-detail-title">Select a prospect</div>
              <div class="stat-detail-line">Click a client to see more information.</div>
            </div>
          </div>
        </div>
        <div class="tree-branch-card">
          <button class="branch-title" type="button" data-target="high-value-panel" aria-expanded="false" onclick="toggleBranch('high-value-panel', this)">High Value Prospects</button>
          <div class="branch-panel is-collapsed" id="high-value-panel">
            <div class="branch-body">
              <div class="journey-sub">Progress | Probability | Value</div>
              {high_value_rows}
            </div>
          </div>
        </div>
        <div class="tree-branch-card">
          <button class="branch-title" type="button" data-target="early-stage-panel" aria-expanded="false" onclick="toggleBranch('early-stage-panel', this)">Early Stage Prospects</button>
          <div class="branch-panel is-collapsed" id="early-stage-panel">
            <div class="branch-body">
              <div class="journey-sub">All currently at 40% progress</div>
              {early_rows}
            </div>
          </div>
        </div>
        </div>
      </div>
    </div>
  </div>

  <div class="journey-panel" id="tab-pipeline" role="tabpanel">
    <div class="journey-title">Overall Pipeline Progress</div>
    <div class="journey-tree">
      <div class="tree-root">Pipeline Progress</div>
      <div class="tree-branch">
        <div class="pipeline-summary">
          <div class="pipeline-card total">
            <div class="pipeline-label">Total Potential</div>
            <div class="pipeline-value">3,412,500</div>
          </div>
          <div class="pipeline-card adjusted">
            <div class="pipeline-label">Probability Adjusted</div>
            <div class="pipeline-value">1,823,750</div>
          </div>
          <div class="pipeline-card progress">
            <div class="pipeline-label">Progress</div>
            <div class="pipeline-value">53%</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  
</div>

<style>
  .journey-board {{
    width: 100%;
    max-width: 1200px;
    margin: 10px auto 0;
    background: #f5f5f5;
    border: 1px solid #d0d0d0;
    border-radius: 16px;
    padding: 20px 22px 26px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.12);
  }}

  .minet-banner {{
    max-width: 1200px;
    margin: 8px auto 18px;
    background: #efefef;
    border-radius: 24px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 10px 24px rgba(0,0,0,0.12);
    padding: 26px 34px 14px;
  }}

  .minet-hero {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0;
    width: 100%;
  }}

  .minet-hero-title {{
    font-size: 2px;
    font-weight: 900;
    color: #000000;
    line-height: 1.1;
    margin: 0;
    text-align: center;
  }}

  .journey-tabs {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 18px;
  }}

  .journey-tab {{
    padding: 8px 14px;
    border-radius: 999px;
    background: #ffffff;
    border: 1px solid #d0d0d0;
    font-size: 12px;
    font-weight: 700;
    color: #4a4a4a;
    cursor: pointer;
  }}

  .journey-tab.active {{
    background: #111111;
    color: #ffffff;
    border-color: #111111;
  }}

  .journey-panel {{
    display: none;
    background: #ffffff;
    border: 1px solid #d9d9d9;
    border-radius: 12px;
    padding: 14px 16px 18px;
    min-height: 520px;
  }}

  .journey-panel.active {{
    display: block;
  }}

  .journey-title {{
    font-size: 16px;
    font-weight: 800;
    color: #111111;
    margin-bottom: 4px;
  }}

  .journey-sub {{
    font-size: 12px;
    color: #6a6a6a;
    margin-bottom: 12px;
  }}

  .journey-sub.muted {{
    margin-top: -6px;
    margin-bottom: 8px;
    color: #8a8a8a;
  }}

  .journey-tree {{
    position: relative;
    margin-top: 18px;
  }}

  .tree-map {{
    position: relative;
    margin-top: 18px;
    padding-left: 10px;
    display: flex;
    align-items: flex-start;
    gap: 24px;
  }}

  .tree-root-box {{
    display: inline-flex;
    align-items: center;
    padding: 10px 16px;
    border-radius: 10px;
    border: 2px solid #e14b4b;
    font-size: 14px;
    font-weight: 800;
    color: #111111;
    background: #ffffff;
    cursor: pointer;
  }}

  .tree-branches {{
    position: relative;
    margin-top: 0;
    padding-top: 6px;
    display: grid;
    grid-template-columns: 36px 1fr;
    gap: 18px;
  }}

  .tree-branches.is-collapsed {{
    display: none;
  }}

  .connector-col {{
    position: relative;
    display: grid;
    grid-template-rows: repeat(3, auto);
  }}

  .v-line {{
    position: absolute;
    left: 16px;
    top: 6px;
    bottom: 6px;
    width: 2px;
    background: #e14b4b;
  }}

  .h-line-row {{
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding: 18px 0;
  }}

  .h-line {{
    display: inline-block;
    width: 18px;
    height: 2px;
    background: #e14b4b;
  }}

  .branches-col {{
    display: grid;
    grid-template-rows: repeat(3, auto);
    gap: 20px;
  }}

  .tree-branch-card {{
    position: relative;
    padding: 12px 14px;
    border-radius: 10px;
    border: 1px solid #e6e6e6;
    background: #ffffff;
  }}

  .branch-title {{
    display: inline-flex;
    align-items: center;
    padding: 6px 10px;
    border-radius: 8px;
    border: 2px solid #e14b4b;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 10px;
    background: #ffffff;
    cursor: pointer;
  }}

  .tree-branch {{
    position: relative;
    margin-top: 14px;
    padding-left: 24px;
  }}

  .tree-branch::before {{
    content: "";
    position: absolute;
    left: 6px;
    top: -10px;
    bottom: 6px;
    width: 2px;
    background: #d0d0d0;
  }}

  .row {{
    display: grid;
    grid-template-columns: 1.1fr 1.4fr 0.7fr;
    gap: 8px;
    align-items: center;
    position: relative;
    padding-left: 12px;
  }}

  .row::before {{
    content: "";
    position: absolute;
    left: -10px;
    top: 50%;
    width: 12px;
    height: 2px;
    background: #d0d0d0;
  }}

  .row.compact {{
    grid-template-columns: 1.1fr 1.2fr 0.6fr;
  }}

  .branch-body {{
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}

  .branch-panel {{
    margin-top: 8px;
  }}

  .branch-panel.is-collapsed {{
    display: none;
  }}

  .prospects-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
  }}

  .prospects-table thead th {{
    text-align: left;
    background: #111111;
    color: #ffffff;
    padding: 6px 8px;
    font-weight: 800;
  }}

  .prospects-table tbody td {{
    padding: 6px 8px;
    border-bottom: 1px solid #e6e6e6;
  }}

  .prospects-table tbody tr:nth-child(odd) {{
    background: #f0f0f0;
  }}

  .prospects-table tbody tr {{
    cursor: pointer;
  }}

  .prospects-table tbody tr.active {{
    background: #e9f0ff;
  }}

  .prospect-detail {{
    margin-top: 10px;
    padding: 10px 12px;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
    background: #fafafa;
  }}

  .stat-row {{
    width: 100%;
    text-align: left;
    background: transparent;
    border: none;
    padding: 2px 0;
    cursor: pointer;
  }}

  .stat-row:hover .label {{
    color: #2b74ff;
  }}

  .stat-row.active .label {{
    color: #2b74ff;
  }}

  .label {{
    font-size: 12px;
    font-weight: 700;
    color: #1f1f1f;
  }}

  .bar {{
    position: relative;
    height: 8px;
    background: #ececec;
    border-radius: 999px;
    overflow: hidden;
  }}

  .bar span {{
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    background: #2b74ff;
    border-radius: 999px;
  }}

  .value {{
    font-size: 11px;
    color: #4a4a4a;
    text-align: right;
    white-space: nowrap;
  }}

  .pipeline-summary {{
    display: grid;
    gap: 14px;
    margin-top: 6px;
  }}

  .pipeline-card {{
    border-radius: 18px;
    padding: 20px 22px;
    color: #ffffff;
    box-shadow: 0 12px 20px rgba(0,0,0,0.16);
    border: 1px solid #111111;
  }}

  .pipeline-card.total {{
    background: #e10600;
  }}

  .pipeline-card.adjusted {{
    background: #111111;
  }}

  .pipeline-card.progress {{
    background: #ffffff;
    color: #111111;
  }}

  .pipeline-label {{
    font-size: 14px;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    opacity: 0.85;
    margin-bottom: 6px;
  }}

  .pipeline-value {{
    font-size: 34px;
    font-weight: 800;
    letter-spacing: 0.3px;
  }}

  .stat-detail {{
    margin-top: 16px;
    padding: 14px;
    border-radius: 12px;
    border: 1px solid #d9d9d9;
    background: #fafafa;
  }}

  .stat-detail-title {{
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 6px;
  }}

  .stat-detail-line {{
    font-size: 12px;
    color: #4a4a4a;
    margin-bottom: 4px;
  }}

  @media (max-width: 720px) {{
    .minet-banner {{
      padding: 16px 18px 12px;
    }}
    .minet-hero-title {{
      font-size: 28px;
    }}
    .tree-branches {{
      grid-template-columns: 24px 1fr;
    }}
    .row, .row.compact {{
      grid-template-columns: 1fr;
      gap: 4px;
    }}
    .value {{
      text-align: left;
    }}
  }}
</style>

<script>
  const tabs = document.querySelectorAll('.journey-tab');
  const panels = document.querySelectorAll('.journey-panel');
  tabs.forEach((tab) => {{
    tab.addEventListener('click', () => {{
      tabs.forEach((t) => {{ t.classList.remove('active'); t.setAttribute('aria-selected', 'false'); }});
      panels.forEach((p) => p.classList.remove('active'));
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');
      const panel = document.getElementById(tab.dataset.target);
      if (panel) panel.classList.add('active');
    }});
  }});
</script>

<script>
  const statRows = document.querySelectorAll('.stat-row');
  const statDetail = document.getElementById('stat-detail');
  statRows.forEach((row) => {{
    row.addEventListener('click', () => {{
      statRows.forEach((r) => r.classList.remove('active'));
      row.classList.add('active');
      const name = row.dataset.name;
      const value = Number(row.dataset.value || 0).toLocaleString();
      const share = row.dataset.share || '0.0';
      const note = row.dataset.note || 'No notes provided.';
      statDetail.innerHTML = `
        <div class="stat-detail-title">${{name}}</div>
        <div class="stat-detail-line">Estimated Converted Income: ${{value}}</div>
        <div class="stat-detail-line">Share of total: ${{share}}%</div>
        <div class="stat-detail-line">Notes: ${{note}}</div>
      `;
    }});
  }});
</script>

<script>
  function toggleProspects() {{
    const prospectsToggle = document.getElementById('prospects-toggle');
    const prospectsBranches = document.getElementById('prospects-branches');
    if (!prospectsToggle || !prospectsBranches) return;
    const isCollapsed = prospectsBranches.classList.toggle('is-collapsed');
    prospectsToggle.setAttribute('aria-expanded', (!isCollapsed).toString());
  }}
</script>

<script>
  function toggleBranch(panelId, btn) {{
    const panel = document.getElementById(panelId);
    if (!panel) return;
    const isCollapsed = panel.classList.toggle('is-collapsed');
    if (btn) btn.setAttribute('aria-expanded', (!isCollapsed).toString());
  }}
</script>

<script>
  const prospectNotes = {{
    "BOMAID": "Embedded GFS.",
    "Legal Guard": "Embedded GFS. Embedded funeral to the existing policy holders.",
    "AFSV": "Embedded GFS. Embedded funeral to the free standing fund.",
    "Medical Aid Scheme": "Application letter sent to NBFIRA.",
    "Healthcare": "Sharing Minet target lists with all OracleMed for joint presentations. Converting OracleMed's business written on non-admitted basis to brokered portfolios through Minet.",
    "Hospital Cash Plan": "Embed hospital cash plan to BPOPF fund members.",
    "Dread Disease (BPOPF)": "Optional DD to BPOPF fund members.",
    "Northside Primary": "Proposal shared with client.",
    "Tardiue": "Proposal shared with client.",
    "Oxy Gas": "Contacts for a key personnel.",
    "Winners Chapel": "Contacts for a key personnel.",
    "Woolworths": "Contacts for a key personnel.",
    "Nandos": "Contacts for a key personnel.",
    "KFC": "Lost in 2023, pursuing client, renews in November.",
    "Livingstone Kolobeng": "Proposal shared with client."
  }};

  function selectProspect(name) {{
    const detail = document.getElementById('prospect-detail');
    if (!detail) return;
    const rows = document.querySelectorAll('.prospects-table tbody tr');
    rows.forEach((r) => r.classList.remove('active'));
    const row = Array.from(rows).find((r) => r.dataset.name === name);
    if (row) row.classList.add('active');
    const note = prospectNotes[name] || "No notes provided.";
    detail.innerHTML = `
      <div class="stat-detail-title">${{name}}</div>
      <div class="stat-detail-line">${{note}}</div>
    `;
  }}
</script>
"""

components.html(html, height=900, scrolling=False)
