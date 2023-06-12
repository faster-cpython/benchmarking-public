
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b1
- machine: windows-amd64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 218 ms: 1.08x faster                                            |
| docutils       | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                          |
| tornado_http   | 109 ms                                                      | 98.2 ms: 1.11x faster                                           |
| Geometric mean | (ref)                                                       | 1.11x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.5 ms: 1.07x faster                                           |
| pidigits       | 145 ms                                                      | 153 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 89.3 ms: 1.16x faster                                           |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                           |
| regex_dna      | 132 ms                                                      | 126 ms: 1.05x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                       | 1.08x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.68 ms: 1.50x faster                                           |
| pickle_pure_python   | 257 us                                                      | 196 us: 1.31x faster                                            |
| unpickle_pure_python | 171 us                                                      | 137 us: 1.25x faster                                            |
| tomli_loads          | 1.62 sec                                                    | 1.39 sec: 1.17x faster                                          |
| xml_etree_process    | 43.4 ms                                                     | 38.6 ms: 1.13x faster                                           |
| xml_etree_parse      | 102 ms                                                      | 93.8 ms: 1.09x faster                                           |
| unpickle             | 9.17 us                                                     | 8.47 us: 1.08x faster                                           |
| json_loads           | 14.2 us                                                     | 13.8 us: 1.03x faster                                           |
| pickle               | 6.80 us                                                     | 7.00 us: 1.03x slower                                           |
| unpickle_list        | 2.81 us                                                     | 2.92 us: 1.04x slower                                           |
| xml_etree_generate   | 54.5 ms                                                     | 56.6 ms: 1.04x slower                                           |
| xml_etree_iterparse  | 63.5 ms                                                     | 66.2 ms: 1.04x slower                                           |
| pickle_list          | 2.59 us                                                     | 2.86 us: 1.10x slower                                           |
| pickle_dict          | 16.9 us                                                     | 19.2 us: 1.14x slower                                           |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 20.8 ms: 1.04x slower                                           |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                           |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.24 ms: 1.22x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 94.7 us: 3.43x faster                                           |
| deltablue                | 4.17 ms                                                     | 2.20 ms: 1.89x faster                                           |
| richards_super           | 51.7 ms                                                     | 29.1 ms: 1.77x faster                                           |
| richards                 | 41.2 ms                                                     | 25.5 ms: 1.61x faster                                           |
| logging_silent           | 96.4 ns                                                     | 60.1 ns: 1.60x faster                                           |
| mypy2                    | 352 ms                                                      | 221 ms: 1.59x faster                                            |
| go                       | 136 ms                                                      | 88.2 ms: 1.54x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 800 us: 1.52x faster                                            |
| json_dumps               | 8.50 ms                                                     | 5.68 ms: 1.50x faster                                           |
| sqlglot_transpile        | 1.46 ms                                                     | 1.02 ms: 1.44x faster                                           |
| scimark_lu               | 85.4 ms                                                     | 60.0 ms: 1.42x faster                                           |
| async_tree_memoization   | 497 ms                                                      | 351 ms: 1.42x faster                                            |
| raytrace                 | 271 ms                                                      | 192 ms: 1.41x faster                                            |
| async_tree_io            | 1.07 sec                                                    | 765 ms: 1.39x faster                                            |
| generators               | 31.6 ms                                                     | 23.0 ms: 1.38x faster                                           |
| async_tree_none          | 420 ms                                                      | 309 ms: 1.36x faster                                            |
| hexiom                   | 5.52 ms                                                     | 4.09 ms: 1.35x faster                                           |
| chaos                    | 58.9 ms                                                     | 44.3 ms: 1.33x faster                                           |
| crypto_pyaes             | 62.3 ms                                                     | 47.4 ms: 1.31x faster                                           |
| pickle_pure_python       | 257 us                                                      | 196 us: 1.31x faster                                            |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.9 ms: 1.30x faster                                           |
| scimark_sor              | 105 ms                                                      | 80.6 ms: 1.30x faster                                           |
| pyflate                  | 387 ms                                                      | 298 ms: 1.30x faster                                            |
| unpickle_pure_python     | 171 us                                                      | 137 us: 1.25x faster                                            |
| pycparser                | 868 ms                                                      | 700 ms: 1.24x faster                                            |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 494 ms: 1.23x faster                                            |
| mdp                      | 1.71 sec                                                    | 1.40 sec: 1.23x faster                                          |
| mako                     | 8.80 ms                                                     | 7.24 ms: 1.22x faster                                           |
| deepcopy_memo            | 28.5 us                                                     | 23.7 us: 1.20x faster                                           |
| spectral_norm            | 78.0 ms                                                     | 66.3 ms: 1.18x faster                                           |
| tomli_loads              | 1.62 sec                                                    | 1.39 sec: 1.17x faster                                          |
| regex_compile            | 103 ms                                                      | 89.3 ms: 1.16x faster                                           |
| pprint_pformat           | 1.21 sec                                                    | 1.06 sec: 1.14x faster                                          |
| pprint_safe_repr         | 589 ms                                                      | 517 ms: 1.14x faster                                            |
| docutils                 | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                          |
| xml_etree_process        | 43.4 ms                                                     | 38.6 ms: 1.13x faster                                           |
| sqlglot_optimize         | 39.0 ms                                                     | 35.0 ms: 1.11x faster                                           |
| tornado_http             | 109 ms                                                      | 98.2 ms: 1.11x faster                                           |
| comprehensions           | 16.0 us                                                     | 14.4 us: 1.11x faster                                           |
| coroutines               | 15.9 ms                                                     | 14.4 ms: 1.10x faster                                           |
| nqueens                  | 67.0 ms                                                     | 61.6 ms: 1.09x faster                                           |
| xml_etree_parse          | 102 ms                                                      | 93.8 ms: 1.09x faster                                           |
| aiohttp                  | 1.01 ms                                                     | 928 us: 1.08x faster                                            |
| 2to3                     | 237 ms                                                      | 218 ms: 1.08x faster                                            |
| unpickle                 | 9.17 us                                                     | 8.47 us: 1.08x faster                                           |
| deepcopy                 | 255 us                                                      | 236 us: 1.08x faster                                            |
| scimark_fft              | 193 ms                                                      | 178 ms: 1.08x faster                                            |
| sqlglot_normalize        | 202 ms                                                      | 187 ms: 1.08x faster                                            |
| regex_v8                 | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                           |
| float                    | 60.2 ms                                                     | 56.5 ms: 1.07x faster                                           |
| bench_thread_pool        | 946 us                                                      | 895 us: 1.06x faster                                            |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.52 ms: 1.05x faster                                           |
| dulwich_log              | 47.6 ms                                                     | 45.3 ms: 1.05x faster                                           |
| fannkuch                 | 258 ms                                                      | 246 ms: 1.05x faster                                            |
| regex_dna                | 132 ms                                                      | 126 ms: 1.05x faster                                            |
| asyncio_tcp              | 712 ms                                                      | 686 ms: 1.04x faster                                            |
| sqlite_synth             | 1.84 us                                                     | 1.78 us: 1.03x faster                                           |
| json_loads               | 14.2 us                                                     | 13.8 us: 1.03x faster                                           |
| deepcopy_reduce          | 2.16 us                                                     | 2.10 us: 1.03x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                           |
| json                     | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                           |
| create_gc_cycles         | 782 us                                                      | 766 us: 1.02x faster                                            |
| unpack_sequence          | 37.8 ns                                                     | 38.7 ns: 1.02x slower                                           |
| pickle                   | 6.80 us                                                     | 7.00 us: 1.03x slower                                           |
| meteor_contest           | 72.5 ms                                                     | 75.2 ms: 1.04x slower                                           |
| unpickle_list            | 2.81 us                                                     | 2.92 us: 1.04x slower                                           |
| xml_etree_generate       | 54.5 ms                                                     | 56.6 ms: 1.04x slower                                           |
| xml_etree_iterparse      | 63.5 ms                                                     | 66.2 ms: 1.04x slower                                           |
| python_startup           | 20.0 ms                                                     | 20.8 ms: 1.04x slower                                           |
| pidigits                 | 145 ms                                                      | 153 ms: 1.06x slower                                            |
| async_generators         | 224 ms                                                      | 237 ms: 1.06x slower                                            |
| logging_simple           | 6.20 us                                                     | 6.77 us: 1.09x slower                                           |
| logging_format           | 6.66 us                                                     | 7.28 us: 1.09x slower                                           |
| pickle_list              | 2.59 us                                                     | 2.86 us: 1.10x slower                                           |
| pathlib                  | 77.4 ms                                                     | 85.4 ms: 1.10x slower                                           |
| telco                    | 3.78 ms                                                     | 4.23 ms: 1.12x slower                                           |
| pickle_dict              | 16.9 us                                                     | 19.2 us: 1.14x slower                                           |
| gc_traversal             | 1.34 ms                                                     | 1.53 ms: 1.14x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                           |
| bench_mp_pool            | 60.7 ms                                                     | 70.0 ms: 1.15x slower                                           |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 2.39 sec: 1.17x slower                                          |
| dask                     | 305 ms                                                      | 382 ms: 1.25x slower                                            |
| coverage                 | 40.0 ms                                                     | 50.9 ms: 1.27x slower                                           |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                    |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
