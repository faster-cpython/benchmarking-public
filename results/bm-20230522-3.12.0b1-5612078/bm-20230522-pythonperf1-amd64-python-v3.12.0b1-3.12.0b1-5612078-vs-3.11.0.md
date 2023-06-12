
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b1
- machine: windows-amd64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 218 ms: 1.05x slower                                            |
| docutils       | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                          |
| tornado_http   | 91.8 ms                                                     | 98.2 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                       | 1.05x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 69.0 ms: 1.01x faster                                           |
| float          | 54.6 ms                                                     | 56.5 ms: 1.03x slower                                           |
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 89.3 ms: 1.02x faster                                           |
| regex_v8       | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                           |
| regex_effbot   | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                           |
| regex_dna      | 115 ms                                                      | 126 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.68 ms: 1.33x faster                                           |
| unpickle_pure_python | 152 us                                                      | 137 us: 1.11x faster                                            |
| xml_etree_parse      | 95.9 ms                                                     | 93.8 ms: 1.02x faster                                           |
| pickle_pure_python   | 200 us                                                      | 196 us: 1.02x faster                                            |
| tomli_loads          | 1.41 sec                                                    | 1.39 sec: 1.02x faster                                          |
| pickle_dict          | 18.5 us                                                     | 19.2 us: 1.04x slower                                           |
| xml_etree_process    | 37.1 ms                                                     | 38.6 ms: 1.04x slower                                           |
| unpickle             | 8.09 us                                                     | 8.47 us: 1.05x slower                                           |
| xml_etree_iterparse  | 62.6 ms                                                     | 66.2 ms: 1.06x slower                                           |
| pickle               | 6.61 us                                                     | 7.00 us: 1.06x slower                                           |
| pickle_list          | 2.68 us                                                     | 2.86 us: 1.07x slower                                           |
| json_loads           | 12.9 us                                                     | 13.8 us: 1.07x slower                                           |
| xml_etree_generate   | 52.2 ms                                                     | 56.6 ms: 1.08x slower                                           |
| unpickle_list        | 2.55 us                                                     | 2.92 us: 1.15x slower                                           |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 20.8 ms: 1.12x slower                                           |
| python_startup_no_site | 15.9 ms                                                     | 17.8 ms: 1.12x slower                                           |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                    |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 94.7 us: 3.40x faster                                           |
| generators               | 33.8 ms                                                     | 23.0 ms: 1.47x faster                                           |
| json_dumps               | 7.56 ms                                                     | 5.68 ms: 1.33x faster                                           |
| richards_super           | 37.5 ms                                                     | 29.1 ms: 1.29x faster                                           |
| richards                 | 30.6 ms                                                     | 25.5 ms: 1.20x faster                                           |
| mdp                      | 1.67 sec                                                    | 1.40 sec: 1.20x faster                                          |
| sqlglot_parse            | 952 us                                                      | 800 us: 1.19x faster                                            |
| unpack_sequence          | 46.1 ns                                                     | 38.7 ns: 1.19x faster                                           |
| deltablue                | 2.61 ms                                                     | 2.20 ms: 1.19x faster                                           |
| logging_silent           | 69.8 ns                                                     | 60.1 ns: 1.16x faster                                           |
| sqlglot_transpile        | 1.16 ms                                                     | 1.02 ms: 1.14x faster                                           |
| hexiom                   | 4.55 ms                                                     | 4.09 ms: 1.11x faster                                           |
| unpickle_pure_python     | 152 us                                                      | 137 us: 1.11x faster                                            |
| comprehensions           | 15.9 us                                                     | 14.4 us: 1.10x faster                                           |
| go                       | 97.3 ms                                                     | 88.2 ms: 1.10x faster                                           |
| coverage                 | 55.9 ms                                                     | 50.9 ms: 1.10x faster                                           |
| raytrace                 | 211 ms                                                      | 192 ms: 1.10x faster                                            |
| json                     | 3.25 ms                                                     | 2.98 ms: 1.09x faster                                           |
| chaos                    | 47.1 ms                                                     | 44.3 ms: 1.06x faster                                           |
| deepcopy_memo            | 25.2 us                                                     | 23.7 us: 1.06x faster                                           |
| scimark_lu               | 63.5 ms                                                     | 60.0 ms: 1.06x faster                                           |
| async_tree_memoization   | 371 ms                                                      | 351 ms: 1.06x faster                                            |
| nqueens                  | 64.9 ms                                                     | 61.6 ms: 1.05x faster                                           |
| deepcopy                 | 246 us                                                      | 236 us: 1.04x faster                                            |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.9 ms: 1.04x faster                                           |
| mypy2                    | 229 ms                                                      | 221 ms: 1.04x faster                                            |
| async_tree_none          | 320 ms                                                      | 309 ms: 1.04x faster                                            |
| fannkuch                 | 252 ms                                                      | 246 ms: 1.03x faster                                            |
| spectral_norm            | 67.9 ms                                                     | 66.3 ms: 1.03x faster                                           |
| xml_etree_parse          | 95.9 ms                                                     | 93.8 ms: 1.02x faster                                           |
| pickle_pure_python       | 200 us                                                      | 196 us: 1.02x faster                                            |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.52 ms: 1.02x faster                                           |
| pyflate                  | 304 ms                                                      | 298 ms: 1.02x faster                                            |
| tomli_loads              | 1.41 sec                                                    | 1.39 sec: 1.02x faster                                          |
| sqlglot_normalize        | 190 ms                                                      | 187 ms: 1.02x faster                                            |
| async_tree_io            | 779 ms                                                      | 765 ms: 1.02x faster                                            |
| regex_compile            | 90.6 ms                                                     | 89.3 ms: 1.02x faster                                           |
| nbody                    | 70.0 ms                                                     | 69.0 ms: 1.01x faster                                           |
| coroutines               | 14.6 ms                                                     | 14.4 ms: 1.01x faster                                           |
| regex_v8                 | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                           |
| meteor_contest           | 74.7 ms                                                     | 75.2 ms: 1.01x slower                                           |
| pprint_safe_repr         | 512 ms                                                      | 517 ms: 1.01x slower                                            |
| pycparser                | 691 ms                                                      | 700 ms: 1.01x slower                                            |
| deepcopy_reduce          | 2.07 us                                                     | 2.10 us: 1.01x slower                                           |
| pprint_pformat           | 1.04 sec                                                    | 1.06 sec: 1.02x slower                                          |
| dulwich_log              | 44.5 ms                                                     | 45.3 ms: 1.02x slower                                           |
| logging_simple           | 6.61 us                                                     | 6.77 us: 1.02x slower                                           |
| aiohttp                  | 899 us                                                      | 928 us: 1.03x slower                                            |
| float                    | 54.6 ms                                                     | 56.5 ms: 1.03x slower                                           |
| pidigits                 | 148 ms                                                      | 153 ms: 1.03x slower                                            |
| logging_format           | 7.01 us                                                     | 7.28 us: 1.04x slower                                           |
| pickle_dict              | 18.5 us                                                     | 19.2 us: 1.04x slower                                           |
| xml_etree_process        | 37.1 ms                                                     | 38.6 ms: 1.04x slower                                           |
| docutils                 | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                          |
| 2to3                     | 209 ms                                                      | 218 ms: 1.05x slower                                            |
| unpickle                 | 8.09 us                                                     | 8.47 us: 1.05x slower                                           |
| bench_thread_pool        | 852 us                                                      | 895 us: 1.05x slower                                            |
| gc_traversal             | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                           |
| xml_etree_iterparse      | 62.6 ms                                                     | 66.2 ms: 1.06x slower                                           |
| pickle                   | 6.61 us                                                     | 7.00 us: 1.06x slower                                           |
| sqlite_synth             | 1.68 us                                                     | 1.78 us: 1.06x slower                                           |
| pickle_list              | 2.68 us                                                     | 2.86 us: 1.07x slower                                           |
| scimark_sor              | 75.6 ms                                                     | 80.6 ms: 1.07x slower                                           |
| tornado_http             | 91.8 ms                                                     | 98.2 ms: 1.07x slower                                           |
| json_loads               | 12.9 us                                                     | 13.8 us: 1.07x slower                                           |
| xml_etree_generate       | 52.2 ms                                                     | 56.6 ms: 1.08x slower                                           |
| telco                    | 3.90 ms                                                     | 4.23 ms: 1.08x slower                                           |
| regex_effbot             | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                           |
| regex_dna                | 115 ms                                                      | 126 ms: 1.09x slower                                            |
| create_gc_cycles         | 693 us                                                      | 766 us: 1.11x slower                                            |
| python_startup           | 18.7 ms                                                     | 20.8 ms: 1.12x slower                                           |
| bench_mp_pool            | 62.5 ms                                                     | 70.0 ms: 1.12x slower                                           |
| python_startup_no_site   | 15.9 ms                                                     | 17.8 ms: 1.12x slower                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.39 sec: 1.13x slower                                          |
| unpickle_list            | 2.55 us                                                     | 2.92 us: 1.15x slower                                           |
| pathlib                  | 71.4 ms                                                     | 85.4 ms: 1.20x slower                                           |
| async_generators         | 178 ms                                                      | 237 ms: 1.34x slower                                            |
| dask                     | 264 ms                                                      | 382 ms: 1.45x slower                                            |
| Geometric mean           | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (6): asyncio_tcp, async_tree_cpu_io_mixed, mako, crypto_pyaes, scimark_fft, sqlglot_optimize
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
