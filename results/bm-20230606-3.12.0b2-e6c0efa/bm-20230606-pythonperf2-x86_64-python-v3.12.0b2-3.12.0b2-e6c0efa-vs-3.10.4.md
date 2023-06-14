
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b2
- machine: linux-x86_64
- commit hash: e6c0efa
- commit date: 2023-06-06
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                             |
| docutils       | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                           |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                             |
| Geometric mean | (ref)                                                        | 1.22x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 83.7 ms: 1.64x faster                                            |
| float          | 110 ms                                                       | 77.3 ms: 1.43x faster                                            |
| pidigits       | 271 ms                                                       | 259 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                        | 1.35x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.34x faster                                             |
| regex_v8       | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                            |
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                             |
| regex_effbot   | 2.99 ms                                                      | 3.55 ms: 1.19x slower                                            |
| Geometric mean | (ref)                                                        | 1.08x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 205 us: 1.57x faster                                             |
| pickle_pure_python   | 457 us                                                       | 324 us: 1.41x faster                                             |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                            |
| tomli_loads          | 2.97 sec                                                     | 2.19 sec: 1.36x faster                                           |
| xml_etree_process    | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                            |
| json_loads           | 30.0 us                                                      | 24.5 us: 1.23x faster                                            |
| xml_etree_generate   | 94.6 ms                                                      | 85.6 ms: 1.10x faster                                            |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.07x faster                                             |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                            |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                            |
| pickle_dict          | 30.0 us                                                      | 31.2 us: 1.04x slower                                            |
| pickle_list          | 4.11 us                                                      | 4.27 us: 1.04x slower                                            |
| unpickle_list        | 4.49 us                                                      | 4.71 us: 1.05x slower                                            |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                            |
| python_startup_no_site | 7.32 ms                                                      | 8.45 ms: 1.15x slower                                            |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.93 ms: 1.48x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 150 us: 3.48x faster                                             |
| deltablue                | 7.47 ms                                                      | 3.25 ms: 2.30x faster                                            |
| asyncio_tcp              | 782 ms                                                       | 379 ms: 2.06x faster                                             |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.98x faster                                           |
| richards_super           | 90.8 ms                                                      | 51.0 ms: 1.78x faster                                            |
| logging_silent           | 166 ns                                                       | 93.8 ns: 1.77x faster                                            |
| go                       | 259 ms                                                       | 147 ms: 1.77x faster                                             |
| scimark_lu               | 164 ms                                                       | 96.3 ms: 1.70x faster                                            |
| chaos                    | 107 ms                                                       | 63.6 ms: 1.68x faster                                            |
| scimark_sor              | 177 ms                                                       | 107 ms: 1.66x faster                                             |
| nbody                    | 137 ms                                                       | 83.7 ms: 1.64x faster                                            |
| generators               | 58.0 ms                                                      | 35.5 ms: 1.64x faster                                            |
| richards                 | 74.1 ms                                                      | 45.5 ms: 1.63x faster                                            |
| sqlglot_parse            | 2.26 ms                                                      | 1.40 ms: 1.62x faster                                            |
| hexiom                   | 9.52 ms                                                      | 5.95 ms: 1.60x faster                                            |
| raytrace                 | 488 ms                                                       | 307 ms: 1.59x faster                                             |
| scimark_monte_carlo      | 109 ms                                                       | 69.2 ms: 1.58x faster                                            |
| pyflate                  | 697 ms                                                       | 441 ms: 1.58x faster                                             |
| unpickle_pure_python     | 321 us                                                       | 205 us: 1.57x faster                                             |
| async_tree_none          | 700 ms                                                       | 452 ms: 1.55x faster                                             |
| async_tree_io            | 1.61 sec                                                     | 1.04 sec: 1.54x faster                                           |
| async_tree_memoization   | 824 ms                                                       | 546 ms: 1.51x faster                                             |
| sqlglot_transpile        | 2.71 ms                                                      | 1.80 ms: 1.51x faster                                            |
| spectral_norm            | 136 ms                                                       | 91.6 ms: 1.49x faster                                            |
| mako                     | 14.7 ms                                                      | 9.93 ms: 1.48x faster                                            |
| crypto_pyaes             | 118 ms                                                       | 81.2 ms: 1.46x faster                                            |
| fannkuch                 | 496 ms                                                       | 343 ms: 1.45x faster                                             |
| float                    | 110 ms                                                       | 77.3 ms: 1.43x faster                                            |
| pickle_pure_python       | 457 us                                                       | 324 us: 1.41x faster                                             |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                            |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 697 ms: 1.37x faster                                             |
| coroutines               | 30.4 ms                                                      | 22.3 ms: 1.36x faster                                            |
| deepcopy_memo            | 48.9 us                                                      | 36.0 us: 1.36x faster                                            |
| tomli_loads              | 2.97 sec                                                     | 2.19 sec: 1.36x faster                                           |
| regex_compile            | 194 ms                                                       | 144 ms: 1.34x faster                                             |
| pycparser                | 1.66 sec                                                     | 1.24 sec: 1.34x faster                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                           |
| bench_mp_pool            | 7.18 ms                                                      | 5.41 ms: 1.33x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.33x faster                                             |
| logging_simple           | 8.90 us                                                      | 6.73 us: 1.32x faster                                            |
| logging_format           | 9.57 us                                                      | 7.35 us: 1.30x faster                                            |
| xml_etree_process        | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                            |
| tornado_http             | 152 ms                                                       | 121 ms: 1.26x faster                                             |
| nqueens                  | 112 ms                                                       | 89.5 ms: 1.26x faster                                            |
| comprehensions           | 26.9 us                                                      | 21.6 us: 1.25x faster                                            |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                             |
| deepcopy                 | 454 us                                                       | 369 us: 1.23x faster                                             |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                             |
| json_loads               | 30.0 us                                                      | 24.5 us: 1.23x faster                                            |
| sqlglot_optimize         | 70.3 ms                                                      | 57.5 ms: 1.22x faster                                            |
| dulwich_log              | 80.1 ms                                                      | 65.9 ms: 1.21x faster                                            |
| scimark_fft              | 359 ms                                                       | 296 ms: 1.21x faster                                             |
| mdp                      | 3.03 sec                                                     | 2.51 sec: 1.21x faster                                           |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.29 ms: 1.21x faster                                            |
| unpack_sequence          | 59.5 ns                                                      | 49.8 ns: 1.19x faster                                            |
| docutils                 | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                           |
| deepcopy_reduce          | 4.03 us                                                      | 3.40 us: 1.18x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 960 us: 1.18x faster                                             |
| json                     | 5.96 ms                                                      | 5.19 ms: 1.15x faster                                            |
| regex_v8                 | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                            |
| pathlib                  | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                            |
| create_gc_cycles         | 1.82 ms                                                      | 1.62 ms: 1.12x faster                                            |
| xml_etree_generate       | 94.6 ms                                                      | 85.6 ms: 1.10x faster                                            |
| sqlite_synth             | 2.97 us                                                      | 2.71 us: 1.09x faster                                            |
| xml_etree_parse          | 162 ms                                                       | 148 ms: 1.09x faster                                             |
| async_generators         | 422 ms                                                       | 389 ms: 1.08x faster                                             |
| meteor_contest           | 137 ms                                                       | 127 ms: 1.07x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.07x faster                                             |
| regex_dna                | 259 ms                                                       | 245 ms: 1.06x faster                                             |
| pidigits                 | 271 ms                                                       | 259 ms: 1.04x faster                                             |
| telco                    | 7.14 ms                                                      | 7.08 ms: 1.01x faster                                            |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                            |
| pickle                   | 9.94 us                                                      | 10.0 us: 1.01x slower                                            |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                            |
| pickle_dict              | 30.0 us                                                      | 31.2 us: 1.04x slower                                            |
| pickle_list              | 4.11 us                                                      | 4.27 us: 1.04x slower                                            |
| unpickle_list            | 4.49 us                                                      | 4.71 us: 1.05x slower                                            |
| gc_traversal             | 3.45 ms                                                      | 3.79 ms: 1.10x slower                                            |
| python_startup_no_site   | 7.32 ms                                                      | 8.45 ms: 1.15x slower                                            |
| regex_effbot             | 2.99 ms                                                      | 3.55 ms: 1.19x slower                                            |
| dask                     | 463 ms                                                       | 563 ms: 1.21x slower                                             |
| coverage                 | 64.0 ms                                                      | 88.5 ms: 1.38x slower                                            |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                     |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
