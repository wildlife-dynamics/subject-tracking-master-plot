# subject_tracking_master_plot

A data-quality check for EarthRanger tracking setups. It fetches every subject, tracking
device (source) and assignment between them, and draws them as a single interactive
diagram so you can see at a glance which animal wears which collar, since when, and what
looks wrong.

## What the diagram shows

Subjects are listed on the left and sources on the right. Each assignment is a line
between them, labelled with its date range (e.g. `2024-03-01 → present`).

| You see | It means |
|---|---|
| Solid dark line | A current assignment (no end date) |
| Grey dashed line | An ended assignment |
| Red line and label marked `⚠` | An assignment whose start or end date can't be read |
| Pill with an amber outline, listed at the bottom | A subject with no source, or a source with no subject |
| Grey-filled subject pill | An inactive subject |
| Source pill with a red outline | An assignment points at a source that isn't in the sources list |

Assignment date labels are coloured to match their line: dark for current, grey for ended,
red for a date that can't be read.

### Using the diagram

- **Hover** a subject or source to fade everything else and trace its links. Hover a line
  or pill for its details as a tooltip.
- **Click** a subject or source to open a details card: the full name, its EarthRanger
  ID, its type (subjects) or provider, type and model (sources), and every assignment
  with its dates. **Copy** copies the whole card; you can also select just one value in
  it, such as the ID. Close it with ×, Esc or a click elsewhere.
- **Select and copy** any text in the diagram, like ordinary text: drag down a column to
  pick several names, or double-click one. Copying gives one value per line, and names
  cut short with `…` copy in full.

## What it does

| Step | What it does |
|---|---|
| **Set Workflow Details** | Names the run, so its dashboard can be told apart from others. |
| **Set Groupers** | No grouping: the dashboard has a single view. |
| **Set Er Connection** | Connects to the EarthRanger site you pick. |
| **Get Subjects** | Fetches subjects, optionally only one subject group. Stops the run if none are found. |
| **Get Subjectsources** | Fetches all subject–source assignments on the site. |
| **Get Sources** | Fetches all sources (tracking devices) on the site. |
| **Draw Subject Source Diagram** | Draws the diagram as a self-contained HTML page, including sources not assigned to any subject. |
| **Persist Text** | Saves the HTML page to the results folder. |
| **Create Plot Widget Single View** | Wraps the page in a dashboard widget titled **Subject Tracking Master**. |
| **Gather Dashboard** | Builds the dashboard from that widget. |

## Requirements

- Access to an **EarthRanger** site, set up as a data source connection. The account
  needs read access to subjects, sources and subject sources.

---

## 1. Load the Workflow

In the workflow runner, add a new template using this repository's URL. Once added, select
**subject_tracking_master_plot** from the available templates list to load it.

---

## 2. Configure the Workflow

You'll be prompted to fill in the following parameters before running.

### Set Workflow Details

| Field | Description | Default |
|---|---|---|
| Workflow Name *(required)* | A name for this run. | — |
| Workflow Description | A description for this run. | empty |

### Set Er Connection

| Field | Description | Default |
|---|---|---|
| Data Source *(required)* | The EarthRanger connection to check. | — |

### Get Subjects

| Field | Description | Default |
|---|---|---|
| Subject Group Name | Only check subjects in this group. Pick from the drop-down, which lists the subject groups on the chosen EarthRanger site once a Data Source is selected. Leave empty for all subjects. | All subject groups |
| Include Inactive *(advanced)* | Include inactive subjects. | On |

Filtering by subject group limits the **subjects** and their assignments. Sources are
always fetched for the whole site, so every source not assigned to one of the chosen
subjects appears under **Sources with no subject**.

---

## 3. Results

The run produces one dashboard with the diagram, and saves the diagram's HTML file to the
results folder (`ECOSCOPE_WORKFLOWS_RESULTS`).

---

## Developing

```bash
# recompile spec.yaml (first time: --install; after that: --update, which bumps VERSION.yaml)
./dev/recompile.sh --update

# run the test cases in test-cases.yaml
pixi run --manifest-path pixi.toml -e default bash dev/pytest-cli.sh subject_tracking_master_plot --all
```

Documentation: [docs/index.html](docs/index.html).
