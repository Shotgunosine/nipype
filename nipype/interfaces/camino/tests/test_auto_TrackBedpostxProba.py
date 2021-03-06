# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..dti import TrackBedpostxProba


def test_TrackBedpostxProba_inputs():
    input_map = dict(
        anisfile=dict(argstr='-anisfile %s', ),
        anisthresh=dict(argstr='-anisthresh %f', ),
        args=dict(argstr='%s', ),
        bedpostxdir=dict(
            argstr='-bedpostxdir %s',
            mandatory=True,
        ),
        curveinterval=dict(
            argstr='-curveinterval %f',
            requires=['curvethresh'],
        ),
        curvethresh=dict(argstr='-curvethresh %f', ),
        data_dims=dict(
            argstr='-datadims %s',
            units='voxels',
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        gzip=dict(argstr='-gzip', ),
        in_file=dict(
            argstr='-inputfile %s',
            position=1,
        ),
        inputdatatype=dict(argstr='-inputdatatype %s', ),
        inputmodel=dict(
            argstr='-inputmodel %s',
            usedefault=True,
        ),
        interpolator=dict(argstr='-interpolator %s', ),
        ipthresh=dict(argstr='-ipthresh %f', ),
        iterations=dict(
            argstr='-iterations %d',
            units='NA',
        ),
        maxcomponents=dict(
            argstr='-maxcomponents %d',
            units='NA',
        ),
        min_vol_frac=dict(
            argstr='-bedpostxminf %d',
            units='NA',
        ),
        numpds=dict(
            argstr='-numpds %d',
            units='NA',
        ),
        out_file=dict(
            argstr='-outputfile %s',
            genfile=True,
            position=-1,
        ),
        output_root=dict(
            argstr='-outputroot %s',
            position=-1,
        ),
        outputtracts=dict(argstr='-outputtracts %s', ),
        seed_file=dict(
            argstr='-seedfile %s',
            position=2,
        ),
        stepsize=dict(
            argstr='-stepsize %f',
            requires=['tracker'],
        ),
        tracker=dict(
            argstr='-tracker %s',
            usedefault=True,
        ),
        voxel_dims=dict(
            argstr='-voxeldims %s',
            units='mm',
        ),
    )
    inputs = TrackBedpostxProba.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_TrackBedpostxProba_outputs():
    output_map = dict(tracked=dict(), )
    outputs = TrackBedpostxProba.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
