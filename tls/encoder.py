import re, itertools

def camel_to_snake(name):
  name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

signs = [
    "Dilithium2",
    "Dilithium3",
    "Dilithium4",
    "Falcon512",
    "Falcon1024",
    "MQDSS3148",
    "MQDSS3164",
    "RainbowIaClassic",
    "RainbowIaCyclic",
    "RainbowIaCyclicCompressed",
    "RainbowIIIcclassic",
    "RainbowIIIcCyclic",
    "RainbowIIIcCyclicCompressed",
    "RainbowVcClassic",
    "RainbowVcCyclic",
    "RainbowVcCyclicCompressed",
    "SphincsHaraka128fRobust",
    "SphincsHaraka128fSimple",
    "SphincsHaraka128sRobust",
    "SphincsHaraka128sSimple",
    "SphincsHaraka192fRobust",
    "SphincsHaraka192fSimple",
    "SphincsHaraka192sRobust",
    "SphincsHaraka192sSimple",
    "SphincsHaraka256fRobust",
    "SphincsHaraka256fSimple",
    "SphincsHaraka256sRobust",
    "SphincsHaraka256sSimple",
    "SphincsSha256128fRobust",
    "SphincsSha256128fSimple",
    "SphincsSha256128sRobust",
    "SphincsSha256128sSimple",
    "SphincsSha256192fRobust",
    "SphincsSha256192fSimple",
    "SphincsSha256192sRobust",
    "SphincsSha256192sSimple",
    "SphincsSha256256fRobust",
    "SphincsSha256256fSimple",
    "SphincsSha256256sRobust",
    "SphincsSha256256sSimple",
    "SphincsShake256128fRobust",
    "SphincsShake256128fSimple",
    "SphincsShake256128sRobust",
    "SphincsShake256128sSimple",
    "SphincsShake256192fRobust",
    "SphincsShake256192fSimple",
    "SphincsShake256192sRobust",
    "SphincsShake256192sSimple",
    "SphincsShake256256fRobust",
    "SphincsShake256256fSimple",
    "SphincsShake256256sRobust",
    "SphincsShake256256sSimple",
    "PicnicL1Fs",
    "PicnicL1Ur",
    "PicnicL3Fs",
    "PicnicL3Ur",
    "PicnicL5Fs",
    "PicnicL5Ur",
    "Picnic2L1Fs",
    "Picnic2L3Fs",
    "Picnic2L5Fs",
    "QTeslaPI",
    "QTeslaPIII",
]

kems = [
    # CSIDH
    "csidh",
    # kyber
    "kyber512",
    "kyber768",
    "kyber1024",
    # kyber90s
    "kyber51290s",
    "kyber76890s",
    "kyber102490s",
    # threebears
    "babybear",
    "babybearephem",
    "mamabear",
    "mamabearephem",
    "papabear",
    "papabearephem",
    # SABER
    "lightsaber",
    "saber",
    "firesaber",
    # leda
    "ledakemlt12",
    "ledakemlt32",
    "ledakemlt52",
    # newhope
    "newhope512cpa",
    "newhope512cca",
    "newhope1024cpa",
    "newhope1024cca",
    # NTRU
    "ntruhps2048509",
    "ntruhps2048677",
    "ntruhps4096821",
    "ntruhrss701",
    # Frodo
    "frodokem640aes",
    "frodokem640shake",
    "frodokem976aes",
    "frodokem976shake",
    "frodokem1344aes",
    "frodokem1344shake",
    # McEliece
    "mceliece348864",
    "mceliece348864f",
    "mceliece460896",
    "mceliece460896f",
    "mceliece6688128",
    "mceliece6688128f",
    "mceliece6960119",
    "mceliece6960119f",
    "mceliece8192128",
    "mceliece8192128f",
    # hqc
    "hqc1281cca2",
    "hqc1921cca2",
    "hqc1922cca2",
    "hqc2561cca2",
    "hqc2562cca2",
    "hqc2563cca2",
]

OQS_KEMS = [
    ("bikel1fo", "BikeL1Fo"),
    ("sikep434compressed", "SikeP434Compressed"),
]

kems.extend((kem for (kem, _) in OQS_KEMS))


def is_oqs_algorithm(algorithm):
    for (kem, _) in OQS_KEMS:
        if kem == algorithm:
            return True
    return False


def get_oqs_algorithm(algorithm):
    for (kem, alg) in OQS_KEMS:
        if kem == algorithm:
            return alg
    return False


oids = {
    var: i
    for (i, var) in [
        *enumerate(itertools.chain(signs)),
        *[(i + 100, var) for (i, var) in enumerate(kems)],
    ]
}

