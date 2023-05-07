
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 207 ms: 1.02x slower                                        |
| docutils       | 1.59 sec                                                                 | 1.58 sec: 1.01x faster                                      |
| tornado_http   | 91.8 ms                                                                  | 88.3 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 53.3 ms                                                                  | 51.7 ms: 1.03x faster                                       |
| nbody          | 70.9 ms                                                                  | 69.4 ms: 1.02x faster                                       |
| pidigits       | 147 ms                                                                   | 151 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 84.5 ms: 1.06x faster                                       |
| regex_effbot   | 1.63 ms                                                                  | 1.62 ms: 1.01x faster                                       |
| regex_v8       | 13.5 ms                                                                  | 14.0 ms: 1.04x slower                                       |
| regex_dna      | 115 ms                                                                   | 119 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.63 ms: 1.37x faster                                       |
| unpickle_pure_python | 150 us                                                                   | 134 us: 1.12x faster                                        |
| pickle_pure_python   | 203 us                                                                   | 190 us: 1.07x faster                                        |
| pickle_dict          | 18.6 us                                                                  | 18.1 us: 1.03x faster                                       |
| xml_etree_iterparse  | 61.8 ms                                                                  | 63.1 ms: 1.02x slower                                       |
| unpickle_list        | 2.80 us                                                                  | 2.86 us: 1.02x slower                                       |
| json_loads           | 13.5 us                                                                  | 13.9 us: 1.03x slower                                       |
| unpickle             | 8.01 us                                                                  | 8.29 us: 1.03x slower                                       |
| xml_etree_process    | 36.6 ms                                                                  | 38.2 ms: 1.04x slower                                       |
| pickle_list          | 2.70 us                                                                  | 2.83 us: 1.05x slower                                       |
| xml_etree_generate   | 52.3 ms                                                                  | 55.9 ms: 1.07x slower                                       |
| pickle               | 6.47 us                                                                  | 7.04 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                                    | 1.01x faster                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.4 ms                                                                  | 15.6 ms: 1.02x slower                                       |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|-----------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.20 ms                                                                  | 6.48 ms: 1.11x faster                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 20.3 ms: 1.66x faster                                       |
| asyncio_tcp             | 674 ms                                                                   | 454 ms: 1.48x faster                                        |
| json_dumps              | 7.71 ms                                                                  | 5.63 ms: 1.37x faster                                       |
| deltablue               | 2.68 ms                                                                  | 2.04 ms: 1.31x faster                                       |
| richards                | 32.1 ms                                                                  | 25.1 ms: 1.28x faster                                       |
| mypy2                   | 276 ms                                                                   | 217 ms: 1.27x faster                                        |
| logging_silent          | 71.0 ns                                                                  | 58.0 ns: 1.22x faster                                       |
| sqlglot_parse           | 929 us                                                                   | 787 us: 1.18x faster                                        |
| mdp                     | 1.67 sec                                                                 | 1.42 sec: 1.18x faster                                      |
| spectral_norm           | 71.8 ms                                                                  | 61.7 ms: 1.16x faster                                       |
| unpack_sequence         | 43.1 ns                                                                  | 37.8 ns: 1.14x faster                                       |
| sqlglot_transpile       | 1.13 ms                                                                  | 996 us: 1.14x faster                                        |
| go                      | 97.5 ms                                                                  | 86.0 ms: 1.13x faster                                       |
| hexiom                  | 4.46 ms                                                                  | 3.95 ms: 1.13x faster                                       |
| nqueens                 | 65.1 ms                                                                  | 57.9 ms: 1.12x faster                                       |
| json                    | 3.20 ms                                                                  | 2.85 ms: 1.12x faster                                       |
| unpickle_pure_python    | 150 us                                                                   | 134 us: 1.12x faster                                        |
| raytrace                | 206 ms                                                                   | 184 ms: 1.12x faster                                        |
| scimark_lu              | 62.8 ms                                                                  | 56.4 ms: 1.11x faster                                       |
| mako                    | 7.20 ms                                                                  | 6.48 ms: 1.11x faster                                       |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.39 ms: 1.10x faster                                       |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 468 ms: 1.10x faster                                        |
| chaos                   | 47.3 ms                                                                  | 43.8 ms: 1.08x faster                                       |
| pickle_pure_python      | 203 us                                                                   | 190 us: 1.07x faster                                        |
| async_tree_memoization  | 374 ms                                                                   | 351 ms: 1.07x faster                                        |
| pyflate                 | 302 ms                                                                   | 284 ms: 1.07x faster                                        |
| coroutines              | 14.8 ms                                                                  | 13.9 ms: 1.07x faster                                       |
| scimark_monte_carlo     | 45.8 ms                                                                  | 43.1 ms: 1.06x faster                                       |
| regex_compile           | 89.7 ms                                                                  | 84.5 ms: 1.06x faster                                       |
| deepcopy_memo           | 25.3 us                                                                  | 23.9 us: 1.06x faster                                       |
| fannkuch                | 255 ms                                                                   | 242 ms: 1.05x faster                                        |
| async_tree_none         | 313 ms                                                                   | 300 ms: 1.04x faster                                        |
| crypto_pyaes            | 48.3 ms                                                                  | 46.3 ms: 1.04x faster                                       |
| scimark_fft             | 183 ms                                                                   | 175 ms: 1.04x faster                                        |
| tornado_http            | 91.8 ms                                                                  | 88.3 ms: 1.04x faster                                       |
| async_tree_io           | 744 ms                                                                   | 716 ms: 1.04x faster                                        |
| dulwich_log             | 43.4 ms                                                                  | 42.0 ms: 1.04x faster                                       |
| logging_simple          | 6.60 us                                                                  | 6.39 us: 1.03x faster                                       |
| pycparser               | 686 ms                                                                   | 664 ms: 1.03x faster                                        |
| pickle_dict             | 18.6 us                                                                  | 18.1 us: 1.03x faster                                       |
| float                   | 53.3 ms                                                                  | 51.7 ms: 1.03x faster                                       |
| deepcopy                | 240 us                                                                   | 233 us: 1.03x faster                                        |
| coverage                | 55.3 ms                                                                  | 53.8 ms: 1.03x faster                                       |
| logging_format          | 7.13 us                                                                  | 6.94 us: 1.03x faster                                       |
| meteor_contest          | 74.4 ms                                                                  | 72.6 ms: 1.02x faster                                       |
| bench_thread_pool       | 856 us                                                                   | 837 us: 1.02x faster                                        |
| nbody                   | 70.9 ms                                                                  | 69.4 ms: 1.02x faster                                       |
| pprint_pformat          | 1.05 sec                                                                 | 1.03 sec: 1.02x faster                                      |
| regex_effbot            | 1.63 ms                                                                  | 1.62 ms: 1.01x faster                                       |
| docutils                | 1.59 sec                                                                 | 1.58 sec: 1.01x faster                                      |
| pprint_safe_repr        | 512 ms                                                                   | 509 ms: 1.00x faster                                        |
| deepcopy_reduce         | 2.06 us                                                                  | 2.08 us: 1.01x slower                                       |
| comprehensions          | 15.4 us                                                                  | 15.5 us: 1.01x slower                                       |
| sqlglot_optimize        | 34.5 ms                                                                  | 34.9 ms: 1.01x slower                                       |
| sqlglot_normalize       | 189 ms                                                                   | 191 ms: 1.01x slower                                        |
| scimark_sor             | 77.7 ms                                                                  | 78.7 ms: 1.01x slower                                       |
| python_startup_no_site  | 15.4 ms                                                                  | 15.6 ms: 1.02x slower                                       |
| 2to3                    | 204 ms                                                                   | 207 ms: 1.02x slower                                        |
| telco                   | 3.93 ms                                                                  | 4.00 ms: 1.02x slower                                       |
| xml_etree_iterparse     | 61.8 ms                                                                  | 63.1 ms: 1.02x slower                                       |
| unpickle_list           | 2.80 us                                                                  | 2.86 us: 1.02x slower                                       |
| sqlite_synth            | 1.67 us                                                                  | 1.71 us: 1.02x slower                                       |
| json_loads              | 13.5 us                                                                  | 13.9 us: 1.03x slower                                       |
| pidigits                | 147 ms                                                                   | 151 ms: 1.03x slower                                        |
| unpickle                | 8.01 us                                                                  | 8.29 us: 1.03x slower                                       |
| regex_v8                | 13.5 ms                                                                  | 14.0 ms: 1.04x slower                                       |
| regex_dna               | 115 ms                                                                   | 119 ms: 1.04x slower                                        |
| gc_traversal            | 1.40 ms                                                                  | 1.46 ms: 1.04x slower                                       |
| create_gc_cycles        | 666 us                                                                   | 693 us: 1.04x slower                                        |
| xml_etree_process       | 36.6 ms                                                                  | 38.2 ms: 1.04x slower                                       |
| pickle_list             | 2.70 us                                                                  | 2.83 us: 1.05x slower                                       |
| xml_etree_generate      | 52.3 ms                                                                  | 55.9 ms: 1.07x slower                                       |
| bench_mp_pool           | 61.2 ms                                                                  | 66.3 ms: 1.08x slower                                       |
| pickle                  | 6.47 us                                                                  | 7.04 us: 1.09x slower                                       |
| pathlib                 | 72.9 ms                                                                  | 81.2 ms: 1.11x slower                                       |
| async_generators        | 180 ms                                                                   | 235 ms: 1.31x slower                                        |
| dask                    | 267 ms                                                                   | 360 ms: 1.35x slower                                        |
| Geometric mean          | (ref)                                                                    | 1.05x faster                                                |

Benchmark hidden because not significant (2): xml_etree_parse, python_startup
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
