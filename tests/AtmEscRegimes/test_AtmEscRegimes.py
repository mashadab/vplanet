import astropy.units as u
import pytest
from benchmark import Benchmark, benchmark


@benchmark(
    {
        "log.initial.system.Age": {"value": 3.155760e13, "unit": u.sec},
        "log.initial.system.Time": {"value": 0.000000, "unit": u.sec},
        "log.initial.system.TotAngMom": {
            "value": 8.302649e43,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.system.TotEnergy": {"value": -9.104511e40, "unit": u.Joule},
        "log.initial.system.PotEnergy": {"value": -9.406038e40, "unit": u.Joule},
        "log.initial.system.KinEnergy": {"value": 3.015563e39, "unit": u.Joule},
        "log.initial.system.DeltaTime": {"value": 0.000000, "unit": u.sec},
        "log.initial.star.Mass": {"value": 1.988416e30, "unit": u.kg},
        "log.initial.star.Radius": {"value": 1.683307e09, "unit": u.m},
        "log.initial.star.RadGyra": {"value": 0.449900},
        "log.initial.star.RotAngMom": {
            "value": 8.293392e43,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.star.RotVel": {"value": 1.224136e05, "unit": u.m / u.sec},
        "log.initial.star.BodyType": {"value": 0.000000},
        "log.initial.star.RotRate": {"value": 7.272205e-05, "unit": 1 / u.sec},
        "log.initial.star.RotPer": {"value": 8.640000e04, "unit": u.sec},
        "log.initial.star.Density": {"value": 99.524124, "unit": u.kg / u.m ** 3},
        "log.initial.star.HZLimitDryRunaway": {"value": 1.887931e11, "unit": u.m},
        "log.initial.star.HZLimRecVenus": {"value": 1.640992e11, "unit": u.m},
        "log.initial.star.HZLimRunaway": {"value": 2.178515e11, "unit": u.m},
        "log.initial.star.HZLimMoistGreenhouse": {"value": 2.171294e11, "unit": u.m},
        "log.initial.star.HZLimMaxGreenhouse": {"value": 3.929566e11, "unit": u.m},
        "log.initial.star.HZLimEarlyMars": {"value": 4.286401e11, "unit": u.m},
        "log.initial.star.Instellation": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.star.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.initial.star.LXUVTot": {"value": 7.435159e23, "unit": u.kg / u.sec ** 3},
        "log.initial.star.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule},
        "log.initial.star.LostAngMom": {
            "value": 5.562685e-309,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.star.Luminosity": {"value": 7.435159e26, "unit": u.W},
        "log.initial.star.LXUVStellar": {"value": 7.435159e23, "unit": u.W},
        "log.initial.star.Temperature": {"value": 4377.256537, "unit": u.K},
        "log.initial.star.LXUVFrac": {"value": 0.001000},
        "log.initial.star.RossbyNumber": {"value": 0.029996},
        "log.initial.star.DRotPerDtStellar": {"value": -4.719062e-10},
        "log.initial.bondi.Mass": {"value": 10.000000, "unit": u.Mearth},
        "log.initial.bondi.Radius": {"value": 8.356166e07, "unit": u.m},
        "log.initial.bondi.RadGyra": {"value": 0.400000},
        "log.initial.bondi.BodyType": {"value": 0.000000},
        "log.initial.bondi.Density": {"value": 24.435631, "unit": u.kg / u.m ** 3},
        "log.initial.bondi.HZLimitDryRunaway": {"value": 1.887931e11, "unit": u.m},
        "log.initial.bondi.HZLimRecVenus": {"value": 1.640992e11, "unit": u.m},
        "log.initial.bondi.HZLimRunaway": {"value": 2.178515e11, "unit": u.m},
        "log.initial.bondi.HZLimMoistGreenhouse": {"value": 2.171294e11, "unit": u.m},
        "log.initial.bondi.HZLimMaxGreenhouse": {"value": 3.929566e11, "unit": u.m},
        "log.initial.bondi.HZLimEarlyMars": {"value": 4.286401e11, "unit": u.m},
        "log.initial.bondi.Instellation": {
            "value": 2.643806e05,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.bondi.MeanMotion": {"value": 6.296138e-06, "unit": 1 / u.sec},
        "log.initial.bondi.OrbPeriod": {"value": 9.979428e05, "unit": u.sec},
        "log.initial.bondi.SemiMajorAxis": {"value": 1.495979e10, "unit": u.m},
        "log.initial.bondi.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.initial.bondi.SurfWaterMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.bondi.EnvelopeMass": {"value": 3.000000, "unit": u.Mearth},
        "log.initial.bondi.OxygenMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.bondi.RGLimit": {"value": 2.011777e11, "unit": u.m},
        "log.initial.bondi.XO": {"value": 0.000000},
        "log.initial.bondi.EtaO": {"value": 0.000000},
        "log.initial.bondi.PlanetRadius": {"value": 8.356166e07, "unit": u.m},
        "log.initial.bondi.OxygenMantleMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.bondi.RadXUV": {"value": -1.000000, "unit": u.m},
        "log.initial.bondi.RadSolid": {"value": -1.000000, "unit": u.m},
        "log.initial.bondi.PresXUV": {"value": 5.000000},
        "log.initial.bondi.ScaleHeight": {"value": -1.000000, "unit": u.m},
        "log.initial.bondi.ThermTemp": {"value": 400.000000, "unit": u.K},
        "log.initial.bondi.AtmGasConst": {"value": 4124.000000},
        "log.initial.bondi.PresSurf": {"value": -1.000000, "unit": u.Pa},
        "log.initial.bondi.DEnvMassDt": {"value": -1.753603e15, "unit": u.kg / u.sec},
        "log.initial.bondi.FXUV": {"value": 264.380605, "unit": u.W / u.m ** 2},
        "log.initial.bondi.AtmXAbsEffH2O": {"value": 0.150000},
        "log.initial.bondi.RocheRadius": {"value": 50.551692, "unit": u.Rearth},
        "log.initial.bondi.BondiRadius": {"value": 50.317150, "unit": u.Rearth},
        "log.initial.bondi.HEscapeRegime": {"value": 5.000000},
        "log.initial.bondi.RRCriticalFlux": {"value": 0.917927, "unit": u.W / u.m ** 2},
        "log.initial.bondi.KTide": {"value": 0.619953},
        "log.initial.bondi.RGDuration": {"value": 0.00000e00, "unit": u.yr},
        "log.initial.rr.Mass": {"value": 1.000000, "unit": u.Mearth},
        "log.initial.rr.Radius": {"value": 6.378853e06, "unit": u.m},
        "log.initial.rr.RadGyra": {"value": 0.400000},
        "log.initial.rr.BodyType": {"value": 0.000000},
        "log.initial.rr.Density": {"value": 5493.092238, "unit": u.kg / u.m ** 3},
        "log.initial.rr.HZLimitDryRunaway": {"value": 1.887931e11, "unit": u.m},
        "log.initial.rr.HZLimRecVenus": {"value": 1.640992e11, "unit": u.m},
        "log.initial.rr.HZLimRunaway": {"value": 2.178515e11, "unit": u.m},
        "log.initial.rr.HZLimMoistGreenhouse": {"value": 2.171294e11, "unit": u.m},
        "log.initial.rr.HZLimMaxGreenhouse": {"value": 3.929566e11, "unit": u.m},
        "log.initial.rr.HZLimEarlyMars": {"value": 4.286401e11, "unit": u.m},
        "log.initial.rr.Instellation": {
            "value": 2.643806e05,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.rr.MeanMotion": {"value": 6.296053e-06, "unit": 1 / u.sec},
        "log.initial.rr.OrbPeriod": {"value": 9.979562e05, "unit": u.sec},
        "log.initial.rr.SemiMajorAxis": {"value": 1.495979e10, "unit": u.m},
        "log.initial.rr.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.initial.rr.SurfWaterMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.rr.EnvelopeMass": {"value": 0.100000, "unit": u.Mearth},
        "log.initial.rr.OxygenMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.rr.RGLimit": {"value": 2.116686e11, "unit": u.m},
        "log.initial.rr.XO": {"value": 0.000000},
        "log.initial.rr.EtaO": {"value": 0.000000},
        "log.initial.rr.PlanetRadius": {"value": 6.378853e06, "unit": u.m},
        "log.initial.rr.OxygenMantleMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.rr.RadXUV": {"value": -1.000000, "unit": u.m},
        "log.initial.rr.RadSolid": {"value": -1.000000, "unit": u.m},
        "log.initial.rr.PresXUV": {"value": 5.000000},
        "log.initial.rr.ScaleHeight": {"value": -1.000000, "unit": u.m},
        "log.initial.rr.ThermTemp": {"value": 400.000000, "unit": u.K},
        "log.initial.rr.AtmGasConst": {"value": 4124.000000},
        "log.initial.rr.PresSurf": {"value": -1.000000, "unit": u.Pa},
        "log.initial.rr.DEnvMassDt": {"value": -7.111259e04, "unit": u.kg / u.sec},
        "log.initial.rr.FXUV": {"value": 0.001000, "unit": u.W / u.m ** 2},
        "log.initial.rr.AtmXAbsEffH2O": {"value": 0.150000},
        "log.initial.rr.RocheRadius": {"value": 23.464017, "unit": u.Rearth},
        "log.initial.rr.BondiRadius": {"value": 5.031715, "unit": u.Rearth},
        "log.initial.rr.HEscapeRegime": {"value": 6.000000},
        "log.initial.rr.RRCriticalFlux": {"value": 47.046983, "unit": u.W / u.m ** 2},
        "log.initial.rr.KTide": {"value": 0.936103},
        "log.initial.rr.RGDuration": {"value": 0.00000e00, "unit": u.yr},
        "log.final.system.Age": {"value": 3.471336e13, "unit": u.sec, "rtol": 1e-4},
        "log.final.system.Time": {"value": 3.155760e12, "unit": u.sec, "rtol": 1e-4},
        "log.final.system.TotAngMom": {
            "value": 8.300304e43,
            "unit": (u.kg * u.m ** 2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.system.TotEnergy": {
            "value": -9.104398e40,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.PotEnergy": {
            "value": -9.713685e40,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.KinEnergy": {
            "value": 3.205681e39,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.DeltaTime": {
            "value": 9.428623e08,
            "unit": u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.Mass": {"value": 1.988416e30, "unit": u.kg, "rtol": 1e-4},
        "log.final.star.Radius": {"value": 1.629995e09, "unit": u.m, "rtol": 1e-4},
        "log.final.star.RadGyra": {"value": 0.450178, "rtol": 1e-4},
        "log.final.star.RotAngMom": {
            "value": 8.285128e43,
            "unit": (u.kg * u.m ** 2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.RotVel": {
            "value": 1.261355e05,
            "unit": u.m / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.star.RotRate": {
            "value": 7.738397e-05,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.RotPer": {"value": 8.119492e04, "unit": u.sec, "rtol": 1e-4},
        "log.final.star.Density": {
            "value": 109.612533,
            "unit": u.kg / u.m ** 3,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimitDryRunaway": {
            "value": 1.825151e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimRecVenus": {
            "value": 1.586622e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimRunaway": {
            "value": 2.106345e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimMoistGreenhouse": {
            "value": 2.099354e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimMaxGreenhouse": {
            "value": 3.800038e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimEarlyMars": {
            "value": 4.145108e11,
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
            "value": 6.948891e23,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.star.LostEnergy": {
            "value": 2.887409e39,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.star.LostAngMom": {
            "value": 8.443984e40,
            "unit": (u.kg * u.m ** 2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.Luminosity": {"value": 6.948891e26, "unit": u.W, "rtol": 1e-4},
        "log.final.star.LXUVStellar": {"value": 6.948891e23, "unit": u.W, "rtol": 1e-4},
        "log.final.star.Temperature": {"value": 4373.437515, "unit": u.K, "rtol": 1e-4},
        "log.final.star.LXUVFrac": {"value": 0.001000, "rtol": 1e-4},
        "log.final.star.RossbyNumber": {"value": 0.028133, "rtol": 1e-4},
        "log.final.star.DRotPerDtStellar": {"value": -1.542974e-09, "rtol": 1e-4},
        "log.final.bondi.Mass": {"value": 7.000000, "unit": u.Mearth, "rtol": 1e-4},
        "log.final.bondi.Radius": {"value": 1.082824e07, "unit": u.m, "rtol": 1e-4},
        "log.final.bondi.RadGyra": {"value": 0.400000, "rtol": 1e-4},
        "log.final.bondi.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.bondi.Density": {
            "value": 7860.836853,
            "unit": u.kg / u.m ** 3,
            "rtol": 1e-4,
        },
        "log.final.bondi.HZLimitDryRunaway": {
            "value": 1.825151e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.bondi.HZLimRecVenus": {
            "value": 1.586622e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.bondi.HZLimRunaway": {
            "value": 2.106345e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.bondi.HZLimMoistGreenhouse": {
            "value": 2.099354e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.bondi.HZLimMaxGreenhouse": {
            "value": 3.800038e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.bondi.HZLimEarlyMars": {
            "value": 4.145108e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.bondi.Instellation": {
            "value": 2.470898e05,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.bondi.MeanMotion": {
            "value": 6.296110e-06,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.bondi.OrbPeriod": {
            "value": 9.979472e05,
            "unit": u.sec,
            "rtol": 1e-4,
        },
        "log.final.bondi.SemiMajorAxis": {
            "value": 1.495979e10,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.bondi.LXUVTot": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.bondi.SurfWaterMass": {
            "value": 0.000000,
            "unit": u.kg,
            "rtol": 1e-4,
        },
        "log.final.bondi.EnvelopeMass": {
            "value": 0.000000,
            "unit": u.Mearth,
            "rtol": 1e-4,
        },
        "log.final.bondi.OxygenMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.bondi.RGLimit": {"value": 1.959840e11, "unit": u.m, "rtol": 1e-4},
        "log.final.bondi.XO": {"value": 0.000000, "rtol": 1e-4},
        "log.final.bondi.EtaO": {"value": 0.000000, "rtol": 1e-4},
        "log.final.bondi.PlanetRadius": {
            "value": 1.082824e07,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.bondi.OxygenMantleMass": {
            "value": 0.000000,
            "unit": u.kg,
            "rtol": 1e-4,
        },
        "log.final.bondi.RadXUV": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.bondi.RadSolid": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.bondi.PresXUV": {"value": 5.000000, "rtol": 1e-4},
        "log.final.bondi.ScaleHeight": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.bondi.ThermTemp": {"value": 400.000000, "unit": u.K, "rtol": 1e-4},
        "log.final.bondi.AtmGasConst": {"value": 4124.000000, "rtol": 1e-4},
        "log.final.bondi.PresSurf": {"value": -1.000000, "unit": u.Pa, "rtol": 1e-4},
        "log.final.bondi.DEnvMassDt": {
            "value": 5.562685e-309,
            "unit": u.kg / u.sec,
            "rtol": 1e-4,
        },
        "log.final.bondi.FXUV": {
            "value": 247.089807,
            "unit": u.W / u.m ** 2,
            "rtol": 1e-4,
        },
        "log.final.bondi.AtmXAbsEffH2O": {"value": 0.150000, "rtol": 1e-4},
        "log.final.bondi.RocheRadius": {
            "value": 44.885049,
            "unit": u.Rearth,
            "rtol": 1e-4,
        },
        "log.final.bondi.BondiRadius": {
            "value": 35.824637,
            "unit": u.Rearth,
            "rtol": 1e-4,
        },
        "log.final.bondi.HEscapeRegime": {"value": 8.000000, "rtol": 1e-4},
        "log.final.bondi.RRCriticalFlux": {
            "value": 478.548229,
            "unit": u.W / u.m ** 2,
            "rtol": 1e-4,
        },
        "log.final.bondi.KTide": {"value": 0.943291, "rtol": 1e-4},
        "log.final.bondi.RGDuration": {"value": 0.00000e00, "unit": u.yr, "rtol": 1e-4},
        "log.final.rr.Mass": {"value": 1.000000, "unit": u.Mearth, "rtol": 1e-4},
        "log.final.rr.Radius": {"value": 6.378853e06, "unit": u.m, "rtol": 1e-4},
        "log.final.rr.RadGyra": {"value": 0.400000, "rtol": 1e-4},
        "log.final.rr.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.rr.Density": {
            "value": 5493.092032,
            "unit": u.kg / u.m ** 3,
            "rtol": 1e-4,
        },
        "log.final.rr.HZLimitDryRunaway": {
            "value": 1.825151e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.rr.HZLimRecVenus": {"value": 1.586622e11, "unit": u.m, "rtol": 1e-4},
        "log.final.rr.HZLimRunaway": {"value": 2.106345e11, "unit": u.m, "rtol": 1e-4},
        "log.final.rr.HZLimMoistGreenhouse": {
            "value": 2.099354e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.rr.HZLimMaxGreenhouse": {
            "value": 3.800038e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.rr.HZLimEarlyMars": {
            "value": 4.145108e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.rr.Instellation": {
            "value": 2.470898e05,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.rr.MeanMotion": {
            "value": 6.296053e-06,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.rr.OrbPeriod": {"value": 9.979562e05, "unit": u.sec, "rtol": 1e-4},
        "log.final.rr.SemiMajorAxis": {"value": 1.495979e10, "unit": u.m, "rtol": 1e-4},
        "log.final.rr.LXUVTot": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
            "rtol": 1e-4,
        },
        "log.final.rr.SurfWaterMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.rr.EnvelopeMass": {
            "value": 0.100000,
            "unit": u.Mearth,
            "rtol": 1e-4,
        },
        "log.final.rr.OxygenMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.rr.RGLimit": {"value": 2.046548e11, "unit": u.m, "rtol": 1e-4},
        "log.final.rr.XO": {"value": 0.000000, "rtol": 1e-4},
        "log.final.rr.EtaO": {"value": 0.000000, "rtol": 1e-4},
        "log.final.rr.PlanetRadius": {"value": 6.378853e06, "unit": u.m, "rtol": 1e-4},
        "log.final.rr.OxygenMantleMass": {
            "value": 0.000000,
            "unit": u.kg,
            "rtol": 1e-4,
        },
        "log.final.rr.RadXUV": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.rr.RadSolid": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.rr.PresXUV": {"value": 5.000000, "rtol": 1e-4},
        "log.final.rr.ScaleHeight": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.rr.ThermTemp": {"value": 400.000000, "unit": u.K, "rtol": 1e-4},
        "log.final.rr.AtmGasConst": {"value": 4124.000000, "rtol": 1e-4},
        "log.final.rr.PresSurf": {"value": -1.000000, "unit": u.Pa, "rtol": 1e-4},
        "log.final.rr.DEnvMassDt": {
            "value": -7.111259e04,
            "unit": u.kg / u.sec,
            "rtol": 1e-4,
        },
        "log.final.rr.FXUV": {"value": 0.001000, "unit": u.W / u.m ** 2, "rtol": 1e-4},
        "log.final.rr.AtmXAbsEffH2O": {"value": 0.150000, "rtol": 1e-4},
        "log.final.rr.RocheRadius": {
            "value": 23.464017,
            "unit": u.Rearth,
            "rtol": 1e-4,
        },
        "log.final.rr.BondiRadius": {"value": 5.117805, "unit": u.Rearth, "rtol": 1e-4},
        "log.final.rr.HEscapeRegime": {"value": 6.000000, "rtol": 1e-4},
        "log.final.rr.RRCriticalFlux": {
            "value": 47.046980,
            "unit": u.W / u.m ** 2,
            "rtol": 1e-4,
        },
        "log.final.rr.KTide": {"value": 0.936103, "rtol": 1e-4},
        "log.final.rr.RGDuration": {"value": 0.00000e00, "unit": u.yr, "rtol": 1e-4},
    }
)
class TestAtmEscRegimes(Benchmark):
    pass
