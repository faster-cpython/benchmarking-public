
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 60ade0c
- commit date: 2023-07-08
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 215 ms: 1.10x faster                                        |
| docutils       | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                      |
| tornado_http   | 109 ms                                                      | 96.2 ms: 1.13x faster                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.0 ms: 1.13x faster                                       |
| nbody          | 69.3 ms                                                     | 69.8 ms: 1.01x slower                                       |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.6 ms: 1.21x faster                                       |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                       |
| regex_dna      | 132 ms                                                      | 124 ms: 1.07x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.63 ms: 1.51x faster                                       |
| pickle_pure_python   | 257 us                                                      | 190 us: 1.35x faster                                        |
| unpickle_pure_python | 171 us                                                      | 131 us: 1.31x faster                                        |
| tomli_loads          | 1.62 sec                                                    | 1.37 sec: 1.19x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 37.7 ms: 1.15x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 89.7 ms: 1.13x faster                                       |
| unpickle             | 9.17 us                                                     | 8.42 us: 1.09x faster                                       |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.6 ms: 1.01x faster                                       |
| xml_etree_generate   | 54.5 ms                                                     | 55.0 ms: 1.01x slower                                       |
| pickle               | 6.80 us                                                     | 7.13 us: 1.05x slower                                       |
| unpickle_list        | 2.81 us                                                     | 2.96 us: 1.05x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.1 us: 1.07x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 20.4 ms: 1.02x slower                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.86 ms: 1.28x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 93.4 us: 3.48x faster                                       |
| deltablue                | 4.17 ms                                                     | 2.07 ms: 2.02x faster                                       |
| richards_super           | 51.7 ms                                                     | 29.6 ms: 1.75x faster                                       |
| mypy2                    | 352 ms                                                      | 209 ms: 1.68x faster                                        |
| logging_silent           | 96.4 ns                                                     | 58.7 ns: 1.64x faster                                       |
| richards                 | 41.2 ms                                                     | 25.6 ms: 1.61x faster                                       |
| go                       | 136 ms                                                      | 86.9 ms: 1.57x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 787 us: 1.55x faster                                        |
| scimark_lu               | 85.4 ms                                                     | 56.0 ms: 1.52x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 700 ms: 1.52x faster                                        |
| json_dumps               | 8.50 ms                                                     | 5.63 ms: 1.51x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 334 ms: 1.49x faster                                        |
| raytrace                 | 271 ms                                                      | 185 ms: 1.47x faster                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 998 us: 1.47x faster                                        |
| generators               | 31.6 ms                                                     | 21.6 ms: 1.46x faster                                       |
| async_tree_none          | 420 ms                                                      | 288 ms: 1.46x faster                                        |
| chaos                    | 58.9 ms                                                     | 42.4 ms: 1.39x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.01 ms: 1.38x faster                                       |
| pickle_pure_python       | 257 us                                                      | 190 us: 1.35x faster                                        |
| crypto_pyaes             | 62.3 ms                                                     | 46.4 ms: 1.34x faster                                       |
| pyflate                  | 387 ms                                                      | 291 ms: 1.33x faster                                        |
| scimark_sor              | 105 ms                                                      | 79.2 ms: 1.32x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.5 ms: 1.32x faster                                       |
| asyncio_tcp              | 712 ms                                                      | 542 ms: 1.32x faster                                        |
| unpickle_pure_python     | 171 us                                                      | 131 us: 1.31x faster                                        |
| mako                     | 8.80 ms                                                     | 6.86 ms: 1.28x faster                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 475 ms: 1.28x faster                                        |
| pycparser                | 868 ms                                                      | 678 ms: 1.28x faster                                        |
| spectral_norm            | 78.0 ms                                                     | 63.7 ms: 1.22x faster                                       |
| deepcopy_memo            | 28.5 us                                                     | 23.3 us: 1.22x faster                                       |
| regex_compile            | 103 ms                                                      | 85.6 ms: 1.21x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.42 sec: 1.21x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.02 sec: 1.19x faster                                      |
| tomli_loads              | 1.62 sec                                                    | 1.37 sec: 1.19x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 498 ms: 1.18x faster                                        |
| docutils                 | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 33.4 ms: 1.17x faster                                       |
| coroutines               | 15.9 ms                                                     | 13.8 ms: 1.16x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 37.7 ms: 1.15x faster                                       |
| comprehensions           | 16.0 us                                                     | 14.0 us: 1.14x faster                                       |
| float                    | 60.2 ms                                                     | 53.0 ms: 1.13x faster                                       |
| xml_etree_parse          | 102 ms                                                      | 89.7 ms: 1.13x faster                                       |
| tornado_http             | 109 ms                                                      | 96.2 ms: 1.13x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 179 ms: 1.13x faster                                        |
| aiohttp                  | 1.01 ms                                                     | 895 us: 1.13x faster                                        |
| dulwich_log              | 47.6 ms                                                     | 42.9 ms: 1.11x faster                                       |
| bench_thread_pool        | 946 us                                                      | 855 us: 1.11x faster                                        |
| 2to3                     | 237 ms                                                      | 215 ms: 1.10x faster                                        |
| nqueens                  | 67.0 ms                                                     | 61.0 ms: 1.10x faster                                       |
| deepcopy                 | 255 us                                                      | 234 us: 1.09x faster                                        |
| unpickle                 | 9.17 us                                                     | 8.42 us: 1.09x faster                                       |
| create_gc_cycles         | 782 us                                                      | 722 us: 1.08x faster                                        |
| regex_v8                 | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.48 ms: 1.07x faster                                       |
| regex_dna                | 132 ms                                                      | 124 ms: 1.07x faster                                        |
| fannkuch                 | 258 ms                                                      | 243 ms: 1.06x faster                                        |
| scimark_fft              | 193 ms                                                      | 183 ms: 1.05x faster                                        |
| sqlite_synth             | 1.84 us                                                     | 1.75 us: 1.05x faster                                       |
| json_loads               | 14.2 us                                                     | 13.5 us: 1.05x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.09 us: 1.03x faster                                       |
| json                     | 3.05 ms                                                     | 2.97 ms: 1.02x faster                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 62.6 ms: 1.01x faster                                       |
| meteor_contest           | 72.5 ms                                                     | 72.2 ms: 1.01x faster                                       |
| nbody                    | 69.3 ms                                                     | 69.8 ms: 1.01x slower                                       |
| xml_etree_generate       | 54.5 ms                                                     | 55.0 ms: 1.01x slower                                       |
| logging_format           | 6.66 us                                                     | 6.75 us: 1.01x slower                                       |
| python_startup           | 20.0 ms                                                     | 20.4 ms: 1.02x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.32 us: 1.02x slower                                       |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                        |
| unpack_sequence          | 37.8 ns                                                     | 39.2 ns: 1.04x slower                                       |
| async_generators         | 224 ms                                                      | 233 ms: 1.04x slower                                        |
| pickle                   | 6.80 us                                                     | 7.13 us: 1.05x slower                                       |
| unpickle_list            | 2.81 us                                                     | 2.96 us: 1.05x slower                                       |
| pathlib                  | 77.4 ms                                                     | 81.5 ms: 1.05x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.1 us: 1.07x slower                                       |
| telco                    | 3.78 ms                                                     | 4.06 ms: 1.07x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.83 us: 1.09x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 70.5 ms: 1.16x slower                                       |
| dask                     | 305 ms                                                      | 366 ms: 1.20x slower                                        |
| coverage                 | 40.0 ms                                                     | 51.1 ms: 1.28x slower                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x
