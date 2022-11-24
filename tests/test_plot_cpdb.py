#!/usr/bin/env python
import pandas as pd
import pytest

from plotnine import ggplot
from unittest.mock import patch

from ktplotspy.plot import plot_cpdb


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb(mock_show, adata, means, pvals):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes=["CXCL13", "CD274", "CXCR5"],
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_title(mock_show, adata, means, pvals):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2=".",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes=["PTPRC", "TNFSF13"],
        title="interacting interactions!",
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_spec_character(mock_show, adata, means, pvals):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes=["CXCL13", "CD274", "CXCR5"],
        special_character_regex_pattern="\\+",
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_deg(mock_show, adata, means, pvals):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes=["CXCL13", "CD274", "CXCR5"],
        degs_analysis=True,
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_noscale(mock_show, adata, means, pvals):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes=["CXCL13", "CD274", "CXCR5"],
        standard_scale=False,
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_one(mock_show, adata, means, pvals):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes="HLA-DPA1",
    )
    g


@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_df(adata, means, pvals):
    df = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes=["CXCL13", "CD274", "CXCR5"],
        return_table=True,
    )
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_family(mock_show, adata, means, pvals):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        gene_family="chemokines",
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_two_families(mock_show, adata, means, pvals):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        gene_family=["chemokines", "Th1"],
    )
    g


@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_wrong_family(adata, means, pvals):
    with pytest.raises(KeyError):
        plot_cpdb(
            adata=adata,
            cell_type1="B cell",
            cell_type2="CD4T cell",
            means=means,
            pvals=pvals,
            celltype_key="celltype",
            gene_family="haha",
        )


@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_two_families_but_wrong(adata, means, pvals):
    with pytest.raises(KeyError):
        plot_cpdb(
            adata=adata,
            cell_type1="B cell",
            cell_type2="CD4T cell",
            means=means,
            pvals=pvals,
            celltype_key="celltype",
            gene_family=["chemokines", "custombad!"],
            custom_gene_family={"custom_family": ["CXCL13", "CD274", "CXCR5"]},
        )


@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_both_gene_and_family(adata, means, pvals):
    with pytest.raises(KeyError):
        plot_cpdb(
            adata=adata,
            cell_type1="B cell",
            cell_type2="CD4T cell",
            means=means,
            pvals=pvals,
            celltype_key="celltype",
            gene_family="chemokines",
            genes=["CXCL13", "CD274", "CXCR5"],
        )


@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_custom_family(adata, means, pvals):
    plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        gene_family="custom_family",
        custom_gene_family={"custom_family": ["CXCL13", "CD274", "CXCR5"]},
    )


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
def test_plot_cpdb_all(mock_show, adata, means, pvals):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means_split", "pvals_split")
def test_plot_cpdb_split(mock_show, adata, means_split, pvals_split):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means_split,
        pvals=pvals_split,
        celltype_key="celltype",
        splitby_key="Experiment",
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
@pytest.mark.parametrize(
    "style,size",
    [
        pytest.param(True, None),
        pytest.param(True, 2),
        pytest.param(False, None),
        pytest.param(False, 2),
    ],
)
def test_plot_not_default(mock_show, adata, means, pvals, style, size):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes=["CXCL13", "CD274", "CXCR5"],
        default_style=style,
        highlight_size=size,
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
@pytest.mark.parametrize(
    "style,size",
    [
        pytest.param(True, None),
        pytest.param(True, 2),
        pytest.param(False, None),
        pytest.param(False, 2),
    ],
)
def test_plot_not_default_v2(mock_show, adata, means, pvals, style, size):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2=".",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes=["PTPRC", "CD40", "CLEC2D"],
        default_style=style,
        highlight_size=size,
    )
    g


@patch("matplotlib.pyplot.show")
@pytest.mark.usefixtures("adata", "means", "pvals")
@pytest.mark.parametrize(
    "exclude",
    [
        "CXCL13-CXCR5",
        ["CXCL13-CXCR5"],
    ],
)
def test_plot_exclude(mock_show, adata, means, pvals, exclude):
    g = plot_cpdb(
        adata=adata,
        cell_type1="B cell",
        cell_type2="CD4T cell",
        means=means,
        pvals=pvals,
        celltype_key="celltype",
        genes=["CXCL13", "CD274", "CXCR5"],
        exclude_interactions=exclude,
    )
    g
