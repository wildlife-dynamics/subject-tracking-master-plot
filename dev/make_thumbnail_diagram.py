"""Synthetic thumbnail data for subject-tracking-master-plot.

Made-up subjects, collars and assignments run through the workflow's own
draw_subject_source_diagram task with the spec's style settings. No real data.

Usage (from the repo root):
  pixi run --manifest-path ecoscope-workflows-subject-tracking-master-plot-workflow/pixi.toml \
    python dev/make_thumbnail_diagram.py spec.yaml diagram.html
Then screenshot the 746x630 figure with headless Chrome
(--window-size=760,662 --force-device-scale-factor=2.15) and pad it to 2560x1440
on white (sips --padToHeightWidth 1440 2560 --padColor FFFFFF) as resources/thumbnail.png.
"""

import sys

import pandas as pd
import yaml
from ecoscope_workflows_ext_custom.tasks.results._subject_source import (
    DiagramLayoutStyle,
    LinkStyle,
    NodeStyle,
    draw_subject_source_diagram,
)

spec_path, out_path = sys.argv[1], sys.argv[2]
OPEN = "9999-12-31T23:59:59+00:00"

subjects = pd.DataFrame(
    [
        {"id": "sub-01", "name": "Amani", "subject_type": "wildlife", "subject_subtype": "elephant", "is_active": True},
        {"id": "sub-02", "name": "Baraka", "subject_type": "wildlife", "subject_subtype": "elephant", "is_active": True},
        {"id": "sub-03", "name": "Chausiku", "subject_type": "wildlife", "subject_subtype": "elephant", "is_active": True},
        {"id": "sub-04", "name": "Dalila", "subject_type": "wildlife", "subject_subtype": "lion", "is_active": True},
        {"id": "sub-05", "name": "Etana", "subject_type": "wildlife", "subject_subtype": "lion", "is_active": True},
        {"id": "sub-06", "name": "Faraji", "subject_type": "wildlife", "subject_subtype": "giraffe", "is_active": False},
        {"id": "sub-07", "name": "Hodari", "subject_type": "wildlife", "subject_subtype": "rhino", "is_active": True},
        {"id": "sub-08", "name": "Imani", "subject_type": "wildlife", "subject_subtype": "elephant", "is_active": True},
        {"id": "sub-09", "name": "Jabari", "subject_type": "wildlife", "subject_subtype": "elephant", "is_active": True},
    ]
)

sources = pd.DataFrame(
    [
        {"id": "src-01", "manufacturer_id": "ST-2104", "provider": "savannah", "source_type": "tracking-device", "model_name": "SAT-GPS"},
        {"id": "src-02", "manufacturer_id": "ST-1877", "provider": "savannah", "source_type": "tracking-device", "model_name": "SAT-GPS"},
        {"id": "src-03", "manufacturer_id": "ST-2251", "provider": "savannah", "source_type": "tracking-device", "model_name": "SAT-GPS"},
        {"id": "src-04", "manufacturer_id": "AWT-3310", "provider": "awt", "source_type": "tracking-device", "model_name": "Iridium"},
        {"id": "src-05", "manufacturer_id": "AWT-3342", "provider": "awt", "source_type": "tracking-device", "model_name": "Iridium"},
        {"id": "src-06", "manufacturer_id": "VEC-0921", "provider": "vectronic", "source_type": "tracking-device", "model_name": "Vertex Lite"},
        {"id": "src-07", "manufacturer_id": "ST-1650", "provider": "savannah", "source_type": "tracking-device", "model_name": "SAT-GPS"},
        {"id": "src-08", "manufacturer_id": "ST-2290", "provider": "savannah", "source_type": "tracking-device", "model_name": "SAT-GPS"},
        {"id": "src-09", "manufacturer_id": "ST-9001", "provider": "savannah", "source_type": "tracking-device", "model_name": "SAT-GPS"},
        {"id": "src-10", "manufacturer_id": "AWT-3999", "provider": "awt", "source_type": "tracking-device", "model_name": "Iridium"},
    ]
)


def ss(subject, source, lower, upper=OPEN):
    return {"subject": subject, "source": source, "assigned_range": {"lower": lower, "upper": upper}}


subjectsources = pd.DataFrame(
    [
        ss("sub-01", "src-07", "2023-02-14T00:00:00+00:00", "2024-08-30T00:00:00+00:00"),  # collar swap
        ss("sub-01", "src-01", "2024-09-02T00:00:00+00:00"),
        ss("sub-02", "src-02", "2023-06-10T00:00:00+00:00"),
        ss("sub-03", "src-03", "2025-01-21T00:00:00+00:00"),
        ss("sub-04", "src-04", "2024-03-05T00:00:00+00:00"),
        ss("sub-05", "src-05", "2024-03-05T00:00:00+00:00"),
        ss("sub-06", "src-06", "2022-11-01T00:00:00+00:00", "2025-04-18T00:00:00+00:00"),  # inactive, ended
        {**ss("sub-07", "src-08", None), "invalid_assigned_range_lower": "2025-13-40"},  # unreadable date
        ss("sub-08", "src-0b7e1f2a-missing", "2025-06-01T00:00:00+00:00"),  # source not in list
        # sub-09 (Jabari) has no collar; src-09 and src-10 are spares
    ]
)

spec = yaml.safe_load(open(spec_path))
step = next(s for s in spec["workflow"] if s["id"] == "subject_source_diagram")
kw = {k: v for k, v in step["partial"].items() if k not in ("subjectsources", "sources")}

kw["node_style"] = NodeStyle(**kw["node_style"])
kw["link_style"] = LinkStyle(**kw["link_style"])
kw["layout_style"] = DiagramLayoutStyle(**kw["layout_style"])
html = draw_subject_source_diagram(
    subjects=subjects, subjectsources=subjectsources, sources=sources, **kw
)
open(out_path, "w").write(html)
print("wrote", out_path, len(html))
