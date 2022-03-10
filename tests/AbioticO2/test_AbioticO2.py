import astropy.units as u
import pytest
from benchmark import Benchmark, benchmark


@benchmark(
    {
        "log.initial.system.Age": {"value": 3.155760e14, "unit": u.sec},
        "log.initial.system.Time": {"value": 0.000000, "unit": u.sec},
        "log.initial.system.TotAngMom": {
            "value": 2.202965e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.system.TotEnergy": {"value": -4.452384e39, "unit": u.Joule},
        "log.initial.system.PotEnergy": {"value": -4.460297e39, "unit": u.Joule},
        "log.initial.system.KinEnergy": {"value": 7.940530e36, "unit": u.Joule},
        "log.initial.system.DeltaTime": {"value": 0.000000, "unit": u.sec},
        "log.initial.star.Mass": {"value": 1.769690e29, "unit": u.kg},
        "log.initial.star.Radius": {"value": 2.811813e08, "unit": u.m},
        "log.initial.star.RadGyra": {"value": 0.463275},
        "log.initial.star.RotAngMom": {
            "value": 2.183803e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.star.RotVel": {"value": 2.044808e04, "unit": u.m / u.sec},
        "log.initial.star.BodyType": {"value": 0.000000},
        "log.initial.star.RotRate": {"value": 7.272205e-05, "unit": 1 / u.sec},
        "log.initial.star.RotPer": {"value": 8.640000e04, "unit": u.sec},
        "log.initial.star.Density": {"value": 1900.419733, "unit": u.kg / u.m ** 3},
        "log.initial.star.HZLimitDryRunaway": {"value": 1.496223e10, "unit": u.m},
        "log.initial.star.HZLimRecVenus": {"value": 1.345177e10, "unit": u.m},
        "log.initial.star.HZLimRunaway": {"value": 1.771185e10, "unit": u.m},
        "log.initial.star.HZLimMoistGreenhouse": {"value": 1.779891e10, "unit": u.m},
        "log.initial.star.HZLimMaxGreenhouse": {"value": 3.407433e10, "unit": u.m},
        "log.initial.star.HZLimEarlyMars": {"value": 3.716153e10, "unit": u.m},
        "log.initial.star.Instellation": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.star.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.initial.star.LXUVTot": {"value": 4.669934e21, "unit": u.kg / u.sec ** 3},
        "log.initial.star.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule},
        "log.initial.star.LostAngMom": {
            "value": 5.562685e-309,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.star.Luminosity": {"value": 4.669934e24, "unit": u.W},
        "log.initial.star.LXUVStellar": {"value": 4.669934e21, "unit": u.W},
        "log.initial.star.Temperature": {"value": 3017.748141, "unit": u.K},
        "log.initial.star.LXUVFrac": {"value": 0.001000},
        "log.initial.star.RossbyNumber": {"value": 0.014927},
        "log.initial.star.DRotPerDtStellar": {"value": -9.167364e-11},
        "log.initial.b.Mass": {"value": 6.073713e24, "unit": u.kg},
        "log.initial.b.Radius": {"value": 7.149850e06, "unit": u.m},
        "log.initial.b.RadGyra": {"value": 0.500000},
        "log.initial.b.BodyType": {"value": 0.000000},
        "log.initial.b.Density": {"value": 3967.115625, "unit": u.kg / u.m ** 3},
        "log.initial.b.HZLimitDryRunaway": {"value": 1.496252e10, "unit": u.m},
        "log.initial.b.HZLimRecVenus": {"value": 1.345177e10, "unit": u.m},
        "log.initial.b.HZLimRunaway": {"value": 1.771185e10, "unit": u.m},
        "log.initial.b.HZLimMoistGreenhouse": {"value": 1.779891e10, "unit": u.m},
        "log.initial.b.HZLimMaxGreenhouse": {"value": 3.407433e10, "unit": u.m},
        "log.initial.b.HZLimEarlyMars": {"value": 3.716153e10, "unit": u.m},
        "log.initial.b.Instellation": {"value": 1.245271e05, "unit": u.kg / u.sec ** 3},
        "log.initial.b.MeanMotion": {"value": 4.786567e-05, "unit": 1 / u.sec},
        "log.initial.b.OrbPeriod": {"value": 1.312671e05, "unit": u.sec},
        "log.initial.b.SemiMajorAxis": {"value": 1.727519e09, "unit": u.m},
        "log.initial.b.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.initial.b.SurfWaterMass": {"value": 10.000000, "unit": u.TO},
        "log.initial.b.EnvelopeMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.b.OxygenMass": {"value": 0.000000, "unit": u.bar},
        "log.initial.b.RGLimit": {"value": 1.717177e10, "unit": u.m},
        "log.initial.b.XO": {"value": 0.333333},
        "log.initial.b.EtaO": {"value": 0.828235},
        "log.initial.b.PlanetRadius": {"value": 7.149850e06, "unit": u.m},
        "log.initial.b.OxygenMantleMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.b.RadXUV": {"value": -1.000000, "unit": u.m},
        "log.initial.b.RadSolid": {"value": -1.000000, "unit": u.m},
        "log.initial.b.PresXUV": {"value": 5.000000},
        "log.initial.b.ScaleHeight": {"value": -1.000000, "unit": u.m},
        "log.initial.b.ThermTemp": {"value": 400.000000, "unit": u.K},
        "log.initial.b.AtmGasConst": {"value": 4124.000000},
        "log.initial.b.PresSurf": {"value": -1.000000, "unit": u.Pa},
        "log.initial.b.DEnvMassDt": {"value": 0.000000, "unit": u.kg / u.sec},
        "log.initial.b.FXUV": {"value": 124.527050, "unit": u.W / u.m ** 2},
        "log.initial.b.AtmXAbsEffH2O": {"value": 0.010000},
        "log.initial.b.RocheRadius": {"value": 3.892555e07, "unit": u.m},
        "log.initial.b.BondiRadius": {"value": 3.408687e08, "unit": u.m},
        "log.initial.b.HEscapeRegime": {"value": 8.000000},
        "log.initial.b.RRCriticalFlux": {"value": 20.874806, "unit": u.W / u.m ** 2},
        "log.initial.b.KTide": {"value": 0.727578},
        "log.initial.b.RGDuration": {"value": 0.00000e00, "unit": u.yr},
        "log.initial.e.Mass": {"value": 4.610528e24, "unit": u.kg},
        "log.initial.e.Radius": {"value": 5.804071e06, "unit": u.m},
        "log.initial.e.RadGyra": {"value": 0.500000},
        "log.initial.e.BodyType": {"value": 0.000000},
        "log.initial.e.Density": {"value": 5629.422788, "unit": u.kg / u.m ** 3},
        "log.initial.e.HZLimitDryRunaway": {"value": 1.496243e10, "unit": u.m},
        "log.initial.e.HZLimRecVenus": {"value": 1.345177e10, "unit": u.m},
        "log.initial.e.HZLimRunaway": {"value": 1.771185e10, "unit": u.m},
        "log.initial.e.HZLimMoistGreenhouse": {"value": 1.779891e10, "unit": u.m},
        "log.initial.e.HZLimMaxGreenhouse": {"value": 3.407433e10, "unit": u.m},
        "log.initial.e.HZLimEarlyMars": {"value": 3.716153e10, "unit": u.m},
        "log.initial.e.Instellation": {"value": 1.936552e04, "unit": u.kg / u.sec ** 3},
        "log.initial.e.MeanMotion": {"value": 1.185355e-05, "unit": 1 / u.sec},
        "log.initial.e.OrbPeriod": {"value": 5.300679e05, "unit": u.sec},
        "log.initial.e.SemiMajorAxis": {"value": 4.380652e09, "unit": u.m},
        "log.initial.e.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.initial.e.SurfWaterMass": {"value": 10.000000, "unit": u.TO},
        "log.initial.e.EnvelopeMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.e.OxygenMass": {"value": 0.000000, "unit": u.bar},
        "log.initial.e.RGLimit": {"value": 1.728490e10, "unit": u.m},
        "log.initial.e.XO": {"value": 0.333333},
        "log.initial.e.EtaO": {"value": 0.571632},
        "log.initial.e.PlanetRadius": {"value": 5.804071e06, "unit": u.m},
        "log.initial.e.OxygenMantleMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.e.RadXUV": {"value": -1.000000, "unit": u.m},
        "log.initial.e.RadSolid": {"value": -1.000000, "unit": u.m},
        "log.initial.e.PresXUV": {"value": 5.000000},
        "log.initial.e.ScaleHeight": {"value": -1.000000, "unit": u.m},
        "log.initial.e.ThermTemp": {"value": 400.000000, "unit": u.K},
        "log.initial.e.AtmGasConst": {"value": 4124.000000},
        "log.initial.e.PresSurf": {"value": -1.000000, "unit": u.Pa},
        "log.initial.e.DEnvMassDt": {"value": 0.000000, "unit": u.kg / u.sec},
        "log.initial.e.FXUV": {"value": 19.365515, "unit": u.W / u.m ** 2},
        "log.initial.e.AtmXAbsEffH2O": {"value": 0.025204},
        "log.initial.e.RocheRadius": {"value": 9.004290e07, "unit": u.m},
        "log.initial.e.BondiRadius": {"value": 1.624896e08, "unit": u.m},
        "log.initial.e.HEscapeRegime": {"value": 8.000000},
        "log.initial.e.RRCriticalFlux": {"value": 34.669871, "unit": u.W / u.m ** 2},
        "log.initial.e.KTide": {"value": 0.903445},
        "log.initial.e.RGDuration": {"value": 0.00000e00, "unit": u.yr},
        "log.final.system.Age": {"value": 3.471336e15, "unit": u.sec, "rtol": 1e-4},
        "log.final.system.Time": {"value": 3.155760e15, "unit": u.sec, "rtol": 1e-4},
        "log.final.system.TotAngMom": {
            "value": 2.196283e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.system.TotEnergy": {
            "value": -4.460407e39,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.PotEnergy": {
            "value": -1.057009e40,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.KinEnergy": {
            "value": 8.299131e36,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        # "log.final.system.DeltaTime": {"value": 4.378318e+09, "unit": u.sec, "rtol": 1e-4},
        "log.final.star.Mass": {"value": 1.769690e29, "unit": u.kg, "rtol": 1e-4},
        "log.final.star.Radius": {"value": 1.186510e08, "unit": u.m, "rtol": 1e-4},
        "log.final.star.RadGyra": {"value": 0.466090, "rtol": 1e-4},
        "log.final.star.RotAngMom": {
            "value": 9.478094e40,
            "unit": (u.kg * u.m ** 2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.RotVel": {
            "value": 2.077844e04,
            "unit": u.m / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.star.RotRate": {"value": 0.000175, "unit": 1 / u.sec, "rtol": 1e-4},
        "log.final.star.RotPer": {"value": 3.587883e04, "unit": u.sec, "rtol": 1e-4},
        "log.final.star.Density": {
            "value": 2.529265e04,
            "unit": u.kg / u.m ** 3,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimitDryRunaway": {
            "value": 5.941096e09,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimRecVenus": {
            "value": 5.349684e09,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimRunaway": {
            "value": 7.039052e09,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimMoistGreenhouse": {
            "value": 7.078520e09,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimMaxGreenhouse": {
            "value": 1.359778e10,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimEarlyMars": {
            "value": 1.482979e10,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.Instellation": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.star.CriticalSemiMajorAxis": {
            "value": -1.000000,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.LXUVTot": {
            "value": 7.362936e20,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.star.LostEnergy": {
            "value": 6.101413e39,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.star.LostAngMom": {
            "value": 1.229310e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.Luminosity": {"value": 7.362936e23, "unit": u.W, "rtol": 1e-4},
        "log.final.star.LXUVStellar": {"value": 7.362936e20, "unit": u.W, "rtol": 1e-4},
        "log.final.star.Temperature": {"value": 2926.559033, "unit": u.K, "rtol": 1e-4},
        "log.final.star.LXUVFrac": {"value": 0.001000, "rtol": 1e-4},
        "log.final.star.RossbyNumber": {"value": 0.005916, "rtol": 1e-4},
        "log.final.star.DRotPerDtStellar": {"value": -4.367201e-12, "rtol": 1e-4},
        "log.final.b.Mass": {"value": 6.073713e24, "unit": u.kg, "rtol": 1e-4},
        "log.final.b.Radius": {"value": 7.149850e06, "unit": u.m, "rtol": 1e-4},
        "log.final.b.RadGyra": {"value": 0.500000, "rtol": 1e-4},
        "log.final.b.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.b.Density": {
            "value": 3967.115625,
            "unit": u.kg / u.m ** 3,
            "rtol": 1e-4,
        },
        "log.final.b.HZLimitDryRunaway": {
            "value": 5.941210e09,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.b.HZLimRecVenus": {"value": 5.349684e09, "unit": u.m, "rtol": 1e-4},
        "log.final.b.HZLimRunaway": {"value": 7.039052e09, "unit": u.m, "rtol": 1e-4},
        "log.final.b.HZLimMoistGreenhouse": {
            "value": 7.078520e09,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.b.HZLimMaxGreenhouse": {
            "value": 1.359778e10,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.b.HZLimEarlyMars": {"value": 1.482979e10, "unit": u.m, "rtol": 1e-4},
        "log.final.b.Instellation": {
            "value": 1.963378e04,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.b.MeanMotion": {
            "value": 4.786567e-05,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.b.OrbPeriod": {"value": 1.312671e05, "unit": u.sec, "rtol": 1e-4},
        "log.final.b.SemiMajorAxis": {"value": 1.727519e09, "unit": u.m, "rtol": 1e-4},
        "log.final.b.LXUVTot": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.b.SurfWaterMass": {"value": 2.800778, "unit": u.TO, "rtol": 1e-4},
        "log.final.b.EnvelopeMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.b.OxygenMass": {"value": 209.804676, "unit": u.bar, "rtol": 1e-4},
        "log.final.b.RGLimit": {"value": 6.824916e09, "unit": u.m, "rtol": 1e-4},
        "log.final.b.XO": {"value": 0.427123, "rtol": 1e-4},
        "log.final.b.EtaO": {"value": 0.894840, "rtol": 1e-4},
        "log.final.b.PlanetRadius": {"value": 7.149850e06, "unit": u.m, "rtol": 1e-4},
        "log.final.b.OxygenMantleMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.b.RadXUV": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.b.RadSolid": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.b.PresXUV": {"value": 5.000000, "rtol": 1e-4},
        "log.final.b.ScaleHeight": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.b.ThermTemp": {"value": 400.000000, "unit": u.K, "rtol": 1e-4},
        "log.final.b.AtmGasConst": {"value": 4124.000000, "rtol": 1e-4},
        "log.final.b.PresSurf": {"value": -1.000000, "unit": u.Pa, "rtol": 1e-4},
        "log.final.b.DEnvMassDt": {
            "value": 0.000000,
            "unit": u.kg / u.sec,
            "rtol": 1e-4,
        },
        "log.final.b.FXUV": {"value": 19.633781, "unit": u.W / u.m ** 2, "rtol": 1e-4},
        "log.final.b.AtmXAbsEffH2O": {"value": 0.025045, "rtol": 1e-4},
        "log.final.b.RocheRadius": {"value": 3.892555e07, "unit": u.m, "rtol": 1e-4},
        "log.final.b.BondiRadius": {"value": 5.410910e08, "unit": u.m, "rtol": 1e-4},
        "log.final.b.HEscapeRegime": {"value": 8.000000, "rtol": 1e-4},
        "log.final.b.RRCriticalFlux": {
            "value": 20.874806,
            "unit": u.W / u.m ** 2,
            "rtol": 1e-4,
        },
        "log.final.b.KTide": {"value": 0.727578, "rtol": 1e-4},
        "log.final.b.RGDuration": {"value": 0.00000e00, "unit": u.yr, "rtol": 1e-4},
        "log.final.e.Mass": {"value": 4.610528e24, "unit": u.kg, "rtol": 1e-4},
        "log.final.e.Radius": {"value": 5.804071e06, "unit": u.m, "rtol": 1e-4},
        "log.final.e.RadGyra": {"value": 0.500000, "rtol": 1e-4},
        "log.final.e.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.e.Density": {
            "value": 5629.422788,
            "unit": u.kg / u.m ** 3,
            "rtol": 1e-4,
        },
        "log.final.e.HZLimitDryRunaway": {
            "value": 5.941173e09,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.e.HZLimRecVenus": {"value": 5.349684e09, "unit": u.m, "rtol": 1e-4},
        "log.final.e.HZLimRunaway": {"value": 7.039052e09, "unit": u.m, "rtol": 1e-4},
        "log.final.e.HZLimMoistGreenhouse": {
            "value": 7.078520e09,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.e.HZLimMaxGreenhouse": {
            "value": 1.359778e10,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.e.HZLimEarlyMars": {"value": 1.482979e10, "unit": u.m, "rtol": 1e-4},
        "log.final.e.Instellation": {
            "value": 3053.298722,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.e.MeanMotion": {
            "value": 1.185355e-05,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.e.OrbPeriod": {"value": 5.300679e05, "unit": u.sec, "rtol": 1e-4},
        "log.final.e.SemiMajorAxis": {"value": 4.380652e09, "unit": u.m, "rtol": 1e-4},
        "log.final.e.LXUVTot": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.e.SurfWaterMass": {"value": 7.403333, "unit": u.TO, "rtol": 1e-4},
        "log.final.e.EnvelopeMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.e.OxygenMass": {"value": 418.194192, "unit": u.bar, "rtol": 1e-4},
        "log.final.e.RGLimit": {"value": 6.869930e09, "unit": u.m, "rtol": 1e-4},
        "log.final.e.XO": {"value": 0.377310, "rtol": 1e-4},
        "log.final.e.EtaO": {"value": 0.299543, "rtol": 1e-4},
        "log.final.e.PlanetRadius": {"value": 5.804071e06, "unit": u.m, "rtol": 1e-4},
        "log.final.e.OxygenMantleMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.e.RadXUV": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.e.RadSolid": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.e.PresXUV": {"value": 5.000000, "rtol": 1e-4},
        "log.final.e.ScaleHeight": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.e.ThermTemp": {"value": 400.000000, "unit": u.K, "rtol": 1e-4},
        "log.final.e.AtmGasConst": {"value": 4124.000000, "rtol": 1e-4},
        "log.final.e.PresSurf": {"value": -1.000000, "unit": u.Pa, "rtol": 1e-4},
        "log.final.e.DEnvMassDt": {
            "value": 0.000000,
            "unit": u.kg / u.sec,
            "rtol": 1e-4,
        },
        "log.final.e.FXUV": {"value": 3.053299, "unit": u.W / u.m ** 2, "rtol": 1e-4},
        "log.final.e.AtmXAbsEffH2O": {"value": 0.051776, "rtol": 1e-4},
        "log.final.e.RocheRadius": {"value": 9.004290e07, "unit": u.m, "rtol": 1e-4},
        "log.final.e.BondiRadius": {"value": 2.579341e08, "unit": u.m, "rtol": 1e-4},
        "log.final.e.HEscapeRegime": {"value": 8.000000, "rtol": 1e-4},
        "log.final.e.RRCriticalFlux": {
            "value": 34.669871,
            "unit": u.W / u.m ** 2,
            "rtol": 1e-4,
        },
        "log.final.e.KTide": {"value": 0.903445, "rtol": 1e-4},
        "log.final.e.RGDuration": {"value": 0.00000e00, "unit": u.yr, "rtol": 1e-4},
    }
)
class TestAbioticO2(Benchmark):
    pass
