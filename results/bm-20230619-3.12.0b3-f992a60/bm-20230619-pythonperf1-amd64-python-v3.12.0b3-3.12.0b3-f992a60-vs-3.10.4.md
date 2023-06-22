
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b3
- machine: windows-amd64
- commit hash: f992a60
- commit date: 2023-06-19
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 217 ms: 1.09x faster                                            |
| docutils       | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                          |
| tornado_http   | 109 ms                                                      | 90.2 ms: 1.21x faster                                           |
| Geometric mean | (ref)                                                       | 1.15x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.0 ms: 1.12x faster                                           |
| nbody          | 69.3 ms                                                     | 67.6 ms: 1.03x faster                                           |
| pidigits       | 145 ms                                                      | 154 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 87.5 ms: 1.18x faster                                           |
| regex_dna      | 132 ms                                                      | 122 ms: 1.08x faster                                            |
| regex_v8       | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                           |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                       | 1.09x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.79 ms: 1.47x faster                                           |
| pickle_pure_python   | 257 us                                                      | 194 us: 1.32x faster                                            |
| unpickle_pure_python | 171 us                                                      | 132 us: 1.29x faster                                            |
| tomli_loads          | 1.62 sec                                                    | 1.38 sec: 1.17x faster                                          |
| xml_etree_process    | 43.4 ms                                                     | 38.1 ms: 1.14x faster                                           |
| unpickle             | 9.17 us                                                     | 8.28 us: 1.11x faster                                           |
| xml_etree_parse      | 102 ms                                                      | 92.7 ms: 1.10x faster                                           |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                           |
| pickle               | 6.80 us                                                     | 6.86 us: 1.01x slower                                           |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.6 ms: 1.02x slower                                           |
| xml_etree_generate   | 54.5 ms                                                     | 56.2 ms: 1.03x slower                                           |
| pickle_dict          | 16.9 us                                                     | 18.1 us: 1.07x slower                                           |
| pickle_list          | 2.59 us                                                     | 2.84 us: 1.10x slower                                           |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 20.4 ms: 1.02x slower                                           |
| python_startup_no_site | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                           |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.88 ms: 1.28x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 94.6 us: 3.43x faster                                           |
| deltablue                | 4.17 ms                                                     | 2.07 ms: 2.01x faster                                           |
| richards_super           | 51.7 ms                                                     | 29.7 ms: 1.74x faster                                           |
| mypy2                    | 352 ms                                                      | 215 ms: 1.63x faster                                            |
| logging_silent           | 96.4 ns                                                     | 59.3 ns: 1.63x faster                                           |
| richards                 | 41.2 ms                                                     | 26.1 ms: 1.58x faster                                           |
| go                       | 136 ms                                                      | 88.3 ms: 1.54x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 802 us: 1.52x faster                                            |
| scimark_lu               | 85.4 ms                                                     | 56.6 ms: 1.51x faster                                           |
| raytrace                 | 271 ms                                                      | 184 ms: 1.47x faster                                            |
| json_dumps               | 8.50 ms                                                     | 5.79 ms: 1.47x faster                                           |
| sqlglot_transpile        | 1.46 ms                                                     | 1.01 ms: 1.44x faster                                           |
| async_tree_none          | 420 ms                                                      | 292 ms: 1.44x faster                                            |
| generators               | 31.6 ms                                                     | 22.0 ms: 1.43x faster                                           |
| async_tree_io            | 1.07 sec                                                    | 744 ms: 1.43x faster                                            |
| asyncio_tcp              | 712 ms                                                      | 498 ms: 1.43x faster                                            |
| async_tree_memoization   | 497 ms                                                      | 352 ms: 1.41x faster                                            |
| hexiom                   | 5.52 ms                                                     | 3.99 ms: 1.38x faster                                           |
| chaos                    | 58.9 ms                                                     | 42.8 ms: 1.38x faster                                           |
| scimark_sor              | 105 ms                                                      | 78.1 ms: 1.34x faster                                           |
| pickle_pure_python       | 257 us                                                      | 194 us: 1.32x faster                                            |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.6 ms: 1.31x faster                                           |
| crypto_pyaes             | 62.3 ms                                                     | 47.6 ms: 1.31x faster                                           |
| pyflate                  | 387 ms                                                      | 297 ms: 1.30x faster                                            |
| unpickle_pure_python     | 171 us                                                      | 132 us: 1.29x faster                                            |
| mako                     | 8.80 ms                                                     | 6.88 ms: 1.28x faster                                           |
| pycparser                | 868 ms                                                      | 699 ms: 1.24x faster                                            |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 493 ms: 1.24x faster                                            |
| deepcopy_memo            | 28.5 us                                                     | 23.3 us: 1.22x faster                                           |
| tornado_http             | 109 ms                                                      | 90.2 ms: 1.21x faster                                           |
| spectral_norm            | 78.0 ms                                                     | 64.6 ms: 1.21x faster                                           |
| mdp                      | 1.71 sec                                                    | 1.43 sec: 1.19x faster                                          |
| regex_compile            | 103 ms                                                      | 87.5 ms: 1.18x faster                                           |
| tomli_loads              | 1.62 sec                                                    | 1.38 sec: 1.17x faster                                          |
| pprint_pformat           | 1.21 sec                                                    | 1.04 sec: 1.16x faster                                          |
| pprint_safe_repr         | 589 ms                                                      | 511 ms: 1.15x faster                                            |
| sqlglot_optimize         | 39.0 ms                                                     | 33.9 ms: 1.15x faster                                           |
| comprehensions           | 16.0 us                                                     | 14.0 us: 1.14x faster                                           |
| docutils                 | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                          |
| xml_etree_process        | 43.4 ms                                                     | 38.1 ms: 1.14x faster                                           |
| coroutines               | 15.9 ms                                                     | 14.0 ms: 1.14x faster                                           |
| aiohttp                  | 1.01 ms                                                     | 887 us: 1.14x faster                                            |
| float                    | 60.2 ms                                                     | 54.0 ms: 1.12x faster                                           |
| unpickle                 | 9.17 us                                                     | 8.28 us: 1.11x faster                                           |
| scimark_fft              | 193 ms                                                      | 175 ms: 1.11x faster                                            |
| nqueens                  | 67.0 ms                                                     | 61.1 ms: 1.10x faster                                           |
| xml_etree_parse          | 102 ms                                                      | 92.7 ms: 1.10x faster                                           |
| sqlglot_normalize        | 202 ms                                                      | 184 ms: 1.10x faster                                            |
| 2to3                     | 237 ms                                                      | 217 ms: 1.09x faster                                            |
| bench_thread_pool        | 946 us                                                      | 866 us: 1.09x faster                                            |
| deepcopy                 | 255 us                                                      | 234 us: 1.09x faster                                            |
| regex_dna                | 132 ms                                                      | 122 ms: 1.08x faster                                            |
| dulwich_log              | 47.6 ms                                                     | 44.1 ms: 1.08x faster                                           |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.47 ms: 1.08x faster                                           |
| regex_v8                 | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                           |
| fannkuch                 | 258 ms                                                      | 243 ms: 1.06x faster                                            |
| create_gc_cycles         | 782 us                                                      | 744 us: 1.05x faster                                            |
| json_loads               | 14.2 us                                                     | 13.5 us: 1.05x faster                                           |
| deepcopy_reduce          | 2.16 us                                                     | 2.08 us: 1.04x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                           |
| nbody                    | 69.3 ms                                                     | 67.6 ms: 1.03x faster                                           |
| json                     | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                           |
| pickle                   | 6.80 us                                                     | 6.86 us: 1.01x slower                                           |
| sqlite_synth             | 1.84 us                                                     | 1.86 us: 1.01x slower                                           |
| xml_etree_iterparse      | 63.5 ms                                                     | 64.6 ms: 1.02x slower                                           |
| meteor_contest           | 72.5 ms                                                     | 73.9 ms: 1.02x slower                                           |
| python_startup           | 20.0 ms                                                     | 20.4 ms: 1.02x slower                                           |
| unpack_sequence          | 37.8 ns                                                     | 38.8 ns: 1.02x slower                                           |
| xml_etree_generate       | 54.5 ms                                                     | 56.2 ms: 1.03x slower                                           |
| logging_format           | 6.66 us                                                     | 6.91 us: 1.04x slower                                           |
| logging_simple           | 6.20 us                                                     | 6.44 us: 1.04x slower                                           |
| async_generators         | 224 ms                                                      | 234 ms: 1.05x slower                                            |
| pidigits                 | 145 ms                                                      | 154 ms: 1.06x slower                                            |
| pathlib                  | 77.4 ms                                                     | 82.8 ms: 1.07x slower                                           |
| pickle_dict              | 16.9 us                                                     | 18.1 us: 1.07x slower                                           |
| telco                    | 3.78 ms                                                     | 4.11 ms: 1.09x slower                                           |
| pickle_list              | 2.59 us                                                     | 2.84 us: 1.10x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                           |
| bench_mp_pool            | 60.7 ms                                                     | 67.9 ms: 1.12x slower                                           |
| gc_traversal             | 1.34 ms                                                     | 1.53 ms: 1.14x slower                                           |
| dask                     | 305 ms                                                      | 370 ms: 1.21x slower                                            |
| coverage                 | 40.0 ms                                                     | 52.8 ms: 1.32x slower                                           |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                    |

Benchmark hidden because not significant (2): unpickle_list, asyncio_tcp_ssl
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
