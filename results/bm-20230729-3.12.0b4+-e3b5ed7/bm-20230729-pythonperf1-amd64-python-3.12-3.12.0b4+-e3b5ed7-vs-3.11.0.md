
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: e3b5ed7
- commit date: 2023-07-29
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 215 ms: 1.03x slower                                        |
| docutils       | 1.60 sec                                                    | 1.66 sec: 1.03x slower                                      |
| tornado_http   | 91.8 ms                                                     | 87.8 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 66.6 ms: 1.05x faster                                       |
| float          | 54.6 ms                                                     | 53.6 ms: 1.02x faster                                       |
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 88.2 ms: 1.03x faster                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.76 ms: 1.31x faster                                       |
| unpickle_pure_python | 152 us                                                      | 134 us: 1.13x faster                                        |
| tomli_loads          | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                      |
| xml_etree_parse      | 95.9 ms                                                     | 93.7 ms: 1.02x faster                                       |
| pickle_pure_python   | 200 us                                                      | 195 us: 1.02x faster                                        |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.5 ms: 1.03x slower                                       |
| xml_etree_process    | 37.1 ms                                                     | 38.6 ms: 1.04x slower                                       |
| unpickle             | 8.09 us                                                     | 8.48 us: 1.05x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.06x slower                                       |
| json_loads           | 12.9 us                                                     | 13.8 us: 1.07x slower                                       |
| pickle               | 6.61 us                                                     | 7.13 us: 1.08x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 56.5 ms: 1.08x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.81 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.90 ms: 1.05x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.3 us: 3.38x faster                                       |
| generators               | 33.8 ms                                                     | 22.4 ms: 1.51x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 488 ms: 1.43x faster                                        |
| json_dumps               | 7.56 ms                                                     | 5.76 ms: 1.31x faster                                       |
| richards_super           | 37.5 ms                                                     | 29.2 ms: 1.28x faster                                       |
| deltablue                | 2.61 ms                                                     | 2.13 ms: 1.22x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 38.0 ns: 1.21x faster                                       |
| sqlglot_parse            | 952 us                                                      | 798 us: 1.19x faster                                        |
| richards                 | 30.6 ms                                                     | 25.7 ms: 1.19x faster                                       |
| logging_silent           | 69.8 ns                                                     | 60.8 ns: 1.15x faster                                       |
| go                       | 97.3 ms                                                     | 85.3 ms: 1.14x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.02 ms: 1.14x faster                                       |
| comprehensions           | 15.9 us                                                     | 14.0 us: 1.13x faster                                       |
| hexiom                   | 4.55 ms                                                     | 4.02 ms: 1.13x faster                                       |
| unpickle_pure_python     | 152 us                                                      | 134 us: 1.13x faster                                        |
| mdp                      | 1.67 sec                                                    | 1.48 sec: 1.13x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 56.7 ms: 1.12x faster                                       |
| raytrace                 | 211 ms                                                      | 188 ms: 1.12x faster                                        |
| chaos                    | 47.1 ms                                                     | 43.0 ms: 1.10x faster                                       |
| json                     | 3.25 ms                                                     | 2.99 ms: 1.09x faster                                       |
| async_tree_none          | 320 ms                                                      | 296 ms: 1.08x faster                                        |
| async_tree_memoization   | 371 ms                                                      | 345 ms: 1.08x faster                                        |
| nqueens                  | 64.9 ms                                                     | 60.5 ms: 1.07x faster                                       |
| coverage                 | 55.9 ms                                                     | 52.1 ms: 1.07x faster                                       |
| mypy2                    | 229 ms                                                      | 214 ms: 1.07x faster                                        |
| deepcopy_memo            | 25.2 us                                                     | 23.6 us: 1.07x faster                                       |
| async_tree_io            | 779 ms                                                      | 734 ms: 1.06x faster                                        |
| spectral_norm            | 67.9 ms                                                     | 64.2 ms: 1.06x faster                                       |
| mako                     | 7.26 ms                                                     | 6.90 ms: 1.05x faster                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.4 ms: 1.05x faster                                       |
| nbody                    | 70.0 ms                                                     | 66.6 ms: 1.05x faster                                       |
| tornado_http             | 91.8 ms                                                     | 87.8 ms: 1.05x faster                                       |
| deepcopy                 | 246 us                                                      | 237 us: 1.04x faster                                        |
| sqlglot_normalize        | 190 ms                                                      | 184 ms: 1.04x faster                                        |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 484 ms: 1.03x faster                                        |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.49 ms: 1.03x faster                                       |
| tomli_loads              | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                      |
| bench_thread_pool        | 852 us                                                      | 828 us: 1.03x faster                                        |
| aiohttp                  | 899 us                                                      | 874 us: 1.03x faster                                        |
| coroutines               | 14.6 ms                                                     | 14.2 ms: 1.03x faster                                       |
| regex_compile            | 90.6 ms                                                     | 88.2 ms: 1.03x faster                                       |
| pyflate                  | 304 ms                                                      | 297 ms: 1.02x faster                                        |
| xml_etree_parse          | 95.9 ms                                                     | 93.7 ms: 1.02x faster                                       |
| pickle_pure_python       | 200 us                                                      | 195 us: 1.02x faster                                        |
| fannkuch                 | 252 ms                                                      | 247 ms: 1.02x faster                                        |
| meteor_contest           | 74.7 ms                                                     | 73.4 ms: 1.02x faster                                       |
| float                    | 54.6 ms                                                     | 53.6 ms: 1.02x faster                                       |
| logging_simple           | 6.61 us                                                     | 6.50 us: 1.02x faster                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 34.4 ms: 1.01x faster                                       |
| dulwich_log              | 44.5 ms                                                     | 44.0 ms: 1.01x faster                                       |
| scimark_fft              | 178 ms                                                      | 180 ms: 1.01x slower                                        |
| logging_format           | 7.01 us                                                     | 7.07 us: 1.01x slower                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.05 sec: 1.01x slower                                      |
| crypto_pyaes             | 47.6 ms                                                     | 48.2 ms: 1.01x slower                                       |
| python_startup           | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                       |
| pidigits                 | 148 ms                                                      | 153 ms: 1.03x slower                                        |
| telco                    | 3.90 ms                                                     | 4.02 ms: 1.03x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.5 ms: 1.03x slower                                       |
| 2to3                     | 209 ms                                                      | 215 ms: 1.03x slower                                        |
| docutils                 | 1.60 sec                                                    | 1.66 sec: 1.03x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 78.3 ms: 1.04x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 38.6 ms: 1.04x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.48 us: 1.05x slower                                       |
| sqlite_synth             | 1.68 us                                                     | 1.76 us: 1.05x slower                                       |
| gc_traversal             | 1.46 ms                                                     | 1.54 ms: 1.05x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.83 us: 1.06x slower                                       |
| regex_dna                | 115 ms                                                      | 123 ms: 1.07x slower                                        |
| json_loads               | 12.9 us                                                     | 13.8 us: 1.07x slower                                       |
| regex_effbot             | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                       |
| pickle                   | 6.61 us                                                     | 7.13 us: 1.08x slower                                       |
| create_gc_cycles         | 693 us                                                      | 748 us: 1.08x slower                                        |
| xml_etree_generate       | 52.2 ms                                                     | 56.5 ms: 1.08x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 67.8 ms: 1.08x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.81 us: 1.11x slower                                       |
| pathlib                  | 71.4 ms                                                     | 82.9 ms: 1.16x slower                                       |
| async_generators         | 178 ms                                                      | 235 ms: 1.32x slower                                        |
| dask                     | 264 ms                                                      | 365 ms: 1.38x slower                                        |
| Geometric mean           | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, pycparser, regex_v8, pprint_safe_repr, deepcopy_reduce, python_startup_no_site, pickle_dict
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
