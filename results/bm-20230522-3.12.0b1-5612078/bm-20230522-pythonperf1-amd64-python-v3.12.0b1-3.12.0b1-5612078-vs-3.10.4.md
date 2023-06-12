
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b1
- machine: windows-amd64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 218 ms: 1.09x faster                                            |
| docutils       | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                          |
| tornado_http   | 109 ms                                                      | 99.2 ms: 1.10x faster                                           |
| Geometric mean | (ref)                                                       | 1.11x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.5 ms: 1.08x faster                                           |
| pidigits       | 145 ms                                                      | 153 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 88.7 ms: 1.17x faster                                           |
| regex_v8       | 15.0 ms                                                     | 13.3 ms: 1.13x faster                                           |
| regex_dna      | 132 ms                                                      | 119 ms: 1.11x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                       | 1.11x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.67 ms: 1.50x faster                                           |
| pickle_pure_python   | 257 us                                                      | 195 us: 1.32x faster                                            |
| unpickle_pure_python | 171 us                                                      | 134 us: 1.28x faster                                            |
| tomli_loads          | 1.62 sec                                                    | 1.38 sec: 1.17x faster                                          |
| xml_etree_process    | 43.4 ms                                                     | 38.6 ms: 1.13x faster                                           |
| xml_etree_parse      | 102 ms                                                      | 92.8 ms: 1.10x faster                                           |
| unpickle             | 9.17 us                                                     | 8.56 us: 1.07x faster                                           |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.04x faster                                           |
| unpickle_list        | 2.81 us                                                     | 2.90 us: 1.03x slower                                           |
| xml_etree_generate   | 54.5 ms                                                     | 56.6 ms: 1.04x slower                                           |
| xml_etree_iterparse  | 63.5 ms                                                     | 66.1 ms: 1.04x slower                                           |
| pickle               | 6.80 us                                                     | 7.42 us: 1.09x slower                                           |
| pickle_list          | 2.59 us                                                     | 2.91 us: 1.12x slower                                           |
| pickle_dict          | 16.9 us                                                     | 19.2 us: 1.13x slower                                           |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 21.0 ms: 1.05x slower                                           |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                           |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.91 ms: 1.27x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 97.4 us: 3.33x faster                                           |
| deltablue                | 4.17 ms                                                     | 2.19 ms: 1.90x faster                                           |
| richards_super           | 51.7 ms                                                     | 29.4 ms: 1.76x faster                                           |
| logging_silent           | 96.4 ns                                                     | 59.9 ns: 1.61x faster                                           |
| richards                 | 41.2 ms                                                     | 25.8 ms: 1.60x faster                                           |
| mypy2                    | 352 ms                                                      | 220 ms: 1.60x faster                                            |
| go                       | 136 ms                                                      | 88.1 ms: 1.55x faster                                           |
| json_dumps               | 8.50 ms                                                     | 5.67 ms: 1.50x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 814 us: 1.50x faster                                            |
| generators               | 31.6 ms                                                     | 21.8 ms: 1.45x faster                                           |
| scimark_lu               | 85.4 ms                                                     | 60.0 ms: 1.42x faster                                           |
| sqlglot_transpile        | 1.46 ms                                                     | 1.03 ms: 1.42x faster                                           |
| async_tree_none          | 420 ms                                                      | 297 ms: 1.41x faster                                            |
| async_tree_memoization   | 497 ms                                                      | 355 ms: 1.40x faster                                            |
| raytrace                 | 271 ms                                                      | 194 ms: 1.40x faster                                            |
| async_tree_io            | 1.07 sec                                                    | 766 ms: 1.39x faster                                            |
| hexiom                   | 5.52 ms                                                     | 4.03 ms: 1.37x faster                                           |
| scimark_sor              | 105 ms                                                      | 77.3 ms: 1.36x faster                                           |
| chaos                    | 58.9 ms                                                     | 44.4 ms: 1.33x faster                                           |
| pickle_pure_python       | 257 us                                                      | 195 us: 1.32x faster                                            |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.8 ms: 1.30x faster                                           |
| crypto_pyaes             | 62.3 ms                                                     | 48.1 ms: 1.30x faster                                           |
| pyflate                  | 387 ms                                                      | 299 ms: 1.30x faster                                            |
| unpickle_pure_python     | 171 us                                                      | 134 us: 1.28x faster                                            |
| mako                     | 8.80 ms                                                     | 6.91 ms: 1.27x faster                                           |
| pycparser                | 868 ms                                                      | 694 ms: 1.25x faster                                            |
| deepcopy_memo            | 28.5 us                                                     | 23.4 us: 1.22x faster                                           |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 501 ms: 1.21x faster                                            |
| tomli_loads              | 1.62 sec                                                    | 1.38 sec: 1.17x faster                                          |
| regex_compile            | 103 ms                                                      | 88.7 ms: 1.17x faster                                           |
| pprint_pformat           | 1.21 sec                                                    | 1.04 sec: 1.16x faster                                          |
| pprint_safe_repr         | 589 ms                                                      | 507 ms: 1.16x faster                                            |
| spectral_norm            | 78.0 ms                                                     | 67.2 ms: 1.16x faster                                           |
| docutils                 | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                          |
| coroutines               | 15.9 ms                                                     | 14.1 ms: 1.13x faster                                           |
| regex_v8                 | 15.0 ms                                                     | 13.3 ms: 1.13x faster                                           |
| xml_etree_process        | 43.4 ms                                                     | 38.6 ms: 1.13x faster                                           |
| mdp                      | 1.71 sec                                                    | 1.53 sec: 1.12x faster                                          |
| regex_dna                | 132 ms                                                      | 119 ms: 1.11x faster                                            |
| sqlglot_optimize         | 39.0 ms                                                     | 35.3 ms: 1.10x faster                                           |
| tornado_http             | 109 ms                                                      | 99.2 ms: 1.10x faster                                           |
| nqueens                  | 67.0 ms                                                     | 61.1 ms: 1.10x faster                                           |
| xml_etree_parse          | 102 ms                                                      | 92.8 ms: 1.10x faster                                           |
| scimark_fft              | 193 ms                                                      | 177 ms: 1.09x faster                                            |
| 2to3                     | 237 ms                                                      | 218 ms: 1.09x faster                                            |
| comprehensions           | 16.0 us                                                     | 14.7 us: 1.09x faster                                           |
| float                    | 60.2 ms                                                     | 55.5 ms: 1.08x faster                                           |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.45 ms: 1.08x faster                                           |
| bench_thread_pool        | 946 us                                                      | 875 us: 1.08x faster                                            |
| aiohttp                  | 1.01 ms                                                     | 936 us: 1.08x faster                                            |
| unpickle                 | 9.17 us                                                     | 8.56 us: 1.07x faster                                           |
| sqlglot_normalize        | 202 ms                                                      | 189 ms: 1.07x faster                                            |
| asyncio_tcp              | 712 ms                                                      | 668 ms: 1.07x faster                                            |
| fannkuch                 | 258 ms                                                      | 242 ms: 1.07x faster                                            |
| sqlite_synth             | 1.84 us                                                     | 1.73 us: 1.06x faster                                           |
| deepcopy                 | 255 us                                                      | 241 us: 1.06x faster                                            |
| dulwich_log              | 47.6 ms                                                     | 45.3 ms: 1.05x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                           |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.04x faster                                           |
| deepcopy_reduce          | 2.16 us                                                     | 2.11 us: 1.02x faster                                           |
| create_gc_cycles         | 782 us                                                      | 765 us: 1.02x faster                                            |
| json                     | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                           |
| meteor_contest           | 72.5 ms                                                     | 74.4 ms: 1.03x slower                                           |
| unpickle_list            | 2.81 us                                                     | 2.90 us: 1.03x slower                                           |
| xml_etree_generate       | 54.5 ms                                                     | 56.6 ms: 1.04x slower                                           |
| xml_etree_iterparse      | 63.5 ms                                                     | 66.1 ms: 1.04x slower                                           |
| python_startup           | 20.0 ms                                                     | 21.0 ms: 1.05x slower                                           |
| pidigits                 | 145 ms                                                      | 153 ms: 1.05x slower                                            |
| logging_format           | 6.66 us                                                     | 7.07 us: 1.06x slower                                           |
| logging_simple           | 6.20 us                                                     | 6.61 us: 1.07x slower                                           |
| async_generators         | 224 ms                                                      | 240 ms: 1.07x slower                                            |
| pickle                   | 6.80 us                                                     | 7.42 us: 1.09x slower                                           |
| telco                    | 3.78 ms                                                     | 4.14 ms: 1.09x slower                                           |
| pickle_list              | 2.59 us                                                     | 2.91 us: 1.12x slower                                           |
| pathlib                  | 77.4 ms                                                     | 87.5 ms: 1.13x slower                                           |
| pickle_dict              | 16.9 us                                                     | 19.2 us: 1.13x slower                                           |
| bench_mp_pool            | 60.7 ms                                                     | 69.6 ms: 1.15x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                           |
| gc_traversal             | 1.34 ms                                                     | 1.55 ms: 1.15x slower                                           |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 2.35 sec: 1.15x slower                                          |
| dask                     | 305 ms                                                      | 381 ms: 1.25x slower                                            |
| coverage                 | 40.0 ms                                                     | 52.4 ms: 1.31x slower                                           |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                    |

Benchmark hidden because not significant (2): nbody, unpack_sequence
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
