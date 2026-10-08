# subject_tracking_data_qa

subject_tracking_data_qa

## What it does

| Step | What it does |
|---|---|
| **Set Workflow Details** | Add information that will help to differentiate this workflow from another. |
| **Set Groupers** |  |
| **Set Er Connection** |  |
| **Get Subjects** | Fetch subjects from EarthRanger with filtering options. |
| **Get Subjectsources** | Fetch subject-source assignments (which device was on which subject, and when) from EarthRanger. |
| **Get Sources** | Fetch sources (tracking devices) from EarthRanger. |
| **Draw Subject Source Diagram** | Draw subjects and sources in two columns, linked by their assignments. |
| **Persist Text** | Persist text to a file or cloud storage object. |
| **Create Plot Widget Single View** | Create a plot widget with a single view. |
| **Gather Dashboard** |  |

## Requirements

- Access to a **EarthRanger** data source, set up as a connection

---

## 1. Load the Workflow

In the workflow runner, add a new template using this repository's URL. Once added, select
**subject_tracking_data_qa** from the available templates list to load it.

---

## 2. Configure the Workflow

You'll be prompted to fill in the following parameters before running.

### Set Workflow Details

| Field | Description | Default |
|---|---|---|
| Workflow Name *(required)* |  | — |

### Get Subjects

| Field | Description | Default |
|---|---|---|
| Include Inactive | Include inactive subjects in the list. | — |
| Subject Group Name | Subject group name to filter subjects by. | — |

---

## Developing

```bash
# recompile spec.yaml (first time: --install; after that: --update, which bumps VERSION.yaml)
./dev/recompile.sh --update

# run the test cases in test-cases.yaml
pixi run --manifest-path pixi.toml -e default bash dev/pytest-cli.sh subject_tracking_data_qa --all
```

Documentation: [docs/index.html](docs/index.html).
