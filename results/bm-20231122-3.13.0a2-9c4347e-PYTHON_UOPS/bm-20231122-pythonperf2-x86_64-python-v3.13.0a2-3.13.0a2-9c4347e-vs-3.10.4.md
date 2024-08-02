
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 311 ms: 1.12x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.90 ms: 1.20x faster                                            |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                           |
| tornado_http   | 157 ms                                                       | 124 ms: 1.27x faster                                             |
| Geometric mean | (ref)                                                        | 1.19x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 447 ms: 1.55x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 561 ms: 1.46x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 1.09 sec: 1.46x faster                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 711 ms: 1.32x faster                                             |
| Geometric mean          | (ref)                                                        | 1.44x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 111 ms                                                       | 92.5 ms: 1.20x faster                                            |
| nbody          | 134 ms                                                       | 112 ms: 1.20x faster                                             |
| pidigits       | 271 ms                                                       | 267 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                        | 1.13x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 172 ms: 1.11x faster                                             |
| regex_v8       | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                            |
| regex_dna      | 261 ms                                                       | 249 ms: 1.05x faster                                             |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 312 us: 1.46x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                            |
| unpickle_pure_python | 312 us                                                       | 231 us: 1.35x faster                                             |
| xml_etree_process    | 75.9 ms                                                      | 60.9 ms: 1.25x faster                                            |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.61 sec: 1.12x faster                                           |
| xml_etree_generate   | 92.3 ms                                                      | 90.1 ms: 1.02x faster                                            |
| unpickle_list        | 4.65 us                                                      | 4.56 us: 1.02x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 157 ms: 1.02x faster                                             |
| pickle               | 9.89 us                                                      | 9.98 us: 1.01x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.27 us: 1.04x slower                                            |
| xml_etree_iterparse  | 110 ms                                                       | 117 ms: 1.06x slower                                             |
| pickle_dict          | 29.5 us                                                      | 31.8 us: 1.08x slower                                            |
| unpickle             | 13.5 us                                                      | 15.2 us: 1.13x slower                                            |
| Geometric mean       | (ref)                                                        | 1.09x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.9 ms: 1.12x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 11.3 ms: 1.55x slower                                            |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 13.6 ms: 1.08x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 133 us: 4.03x faster                                             |
| asyncio_tcp              | 779 ms                                                       | 373 ms: 2.09x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                           |
| logging_silent           | 167 ns                                                       | 98.7 ns: 1.69x faster                                            |
| generators               | 57.3 ms                                                      | 35.0 ms: 1.64x faster                                            |
| raytrace                 | 489 ms                                                       | 299 ms: 1.63x faster                                             |
| scimark_lu               | 167 ms                                                       | 105 ms: 1.59x faster                                             |
| richards_super           | 90.6 ms                                                      | 58.4 ms: 1.55x faster                                            |
| async_tree_none          | 692 ms                                                       | 447 ms: 1.55x faster                                             |
| deltablue                | 7.50 ms                                                      | 4.98 ms: 1.51x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.49 ms: 1.51x faster                                            |
| chaos                    | 109 ms                                                       | 73.3 ms: 1.48x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 80.6 ms: 1.48x faster                                            |
| go                       | 262 ms                                                       | 179 ms: 1.46x faster                                             |
| async_tree_memoization   | 819 ms                                                       | 561 ms: 1.46x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 1.09 sec: 1.46x faster                                           |
| pickle_pure_python       | 455 us                                                       | 312 us: 1.46x faster                                             |
| richards                 | 75.1 ms                                                      | 51.6 ms: 1.45x faster                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.90 ms: 1.41x faster                                            |
| unpack_sequence          | 59.9 ns                                                      | 43.3 ns: 1.38x faster                                            |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 231 us: 1.35x faster                                             |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.75 ms: 1.34x faster                                            |
| pyflate                  | 733 ms                                                       | 557 ms: 1.32x faster                                             |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 711 ms: 1.32x faster                                             |
| logging_simple           | 8.88 us                                                      | 6.80 us: 1.30x faster                                            |
| logging_format           | 9.64 us                                                      | 7.40 us: 1.30x faster                                            |
| deepcopy_memo            | 49.8 us                                                      | 38.6 us: 1.29x faster                                            |
| deepcopy                 | 468 us                                                       | 366 us: 1.28x faster                                             |
| tornado_http             | 157 ms                                                       | 124 ms: 1.27x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.33 sec: 1.26x faster                                           |
| xml_etree_process        | 75.9 ms                                                      | 60.9 ms: 1.25x faster                                            |
| scimark_monte_carlo      | 107 ms                                                       | 87.4 ms: 1.23x faster                                            |
| scimark_sor              | 180 ms                                                       | 149 ms: 1.21x faster                                             |
| float                    | 111 ms                                                       | 92.5 ms: 1.20x faster                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.35 us: 1.20x faster                                            |
| nbody                    | 134 ms                                                       | 112 ms: 1.20x faster                                             |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                            |
| chameleon                | 9.44 ms                                                      | 7.90 ms: 1.20x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 880 ms: 1.19x faster                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.81 sec: 1.19x faster                                           |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                           |
| sqlglot_normalize        | 144 ms                                                       | 124 ms: 1.16x faster                                             |
| bench_thread_pool        | 1.14 ms                                                      | 985 us: 1.16x faster                                             |
| sympy_sum                | 193 ms                                                       | 167 ms: 1.15x faster                                             |
| dask                     | 472 ms                                                       | 411 ms: 1.15x faster                                             |
| comprehensions           | 26.7 us                                                      | 23.3 us: 1.14x faster                                            |
| mdp                      | 3.01 sec                                                     | 2.63 sec: 1.14x faster                                           |
| sympy_integrate          | 28.2 ms                                                      | 24.9 ms: 1.13x faster                                            |
| dulwich_log              | 81.1 ms                                                      | 72.0 ms: 1.13x faster                                            |
| 2to3                     | 350 ms                                                       | 311 ms: 1.12x faster                                             |
| sympy_expand             | 600 ms                                                       | 535 ms: 1.12x faster                                             |
| tomli_loads              | 2.92 sec                                                     | 2.61 sec: 1.12x faster                                           |
| sympy_str                | 360 ms                                                       | 322 ms: 1.12x faster                                             |
| async_generators         | 421 ms                                                       | 377 ms: 1.12x faster                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 63.2 ms: 1.11x faster                                            |
| pathlib                  | 21.4 ms                                                      | 19.3 ms: 1.11x faster                                            |
| regex_compile            | 190 ms                                                       | 172 ms: 1.11x faster                                             |
| json                     | 5.86 ms                                                      | 5.30 ms: 1.11x faster                                            |
| nqueens                  | 115 ms                                                       | 105 ms: 1.09x faster                                             |
| create_gc_cycles         | 1.76 ms                                                      | 1.61 ms: 1.09x faster                                            |
| regex_v8                 | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                            |
| mako                     | 14.7 ms                                                      | 13.6 ms: 1.08x faster                                            |
| fannkuch                 | 483 ms                                                       | 453 ms: 1.07x faster                                             |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                            |
| regex_dna                | 261 ms                                                       | 249 ms: 1.05x faster                                             |
| hexiom                   | 9.42 ms                                                      | 9.10 ms: 1.04x faster                                            |
| xml_etree_generate       | 92.3 ms                                                      | 90.1 ms: 1.02x faster                                            |
| unpickle_list            | 4.65 us                                                      | 4.56 us: 1.02x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 157 ms: 1.02x faster                                             |
| pidigits                 | 271 ms                                                       | 267 ms: 1.01x faster                                             |
| meteor_contest           | 138 ms                                                       | 137 ms: 1.01x faster                                             |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                             |
| pickle                   | 9.89 us                                                      | 9.98 us: 1.01x slower                                            |
| spectral_norm            | 139 ms                                                       | 144 ms: 1.03x slower                                             |
| pickle_list              | 4.12 us                                                      | 4.27 us: 1.04x slower                                            |
| xml_etree_iterparse      | 110 ms                                                       | 117 ms: 1.06x slower                                             |
| pickle_dict              | 29.5 us                                                      | 31.8 us: 1.08x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 3.76 ms: 1.10x slower                                            |
| python_startup           | 11.5 ms                                                      | 12.9 ms: 1.12x slower                                            |
| scimark_fft              | 361 ms                                                       | 407 ms: 1.13x slower                                             |
| unpickle                 | 13.5 us                                                      | 15.2 us: 1.13x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                            |
| telco                    | 7.23 ms                                                      | 8.47 ms: 1.17x slower                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.01 ms: 1.18x slower                                            |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 11.3 ms: 1.55x slower                                            |
| Geometric mean           | (ref)                                                        | 1.20x faster                                                     |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x


# Memory

- memory change: 1.06x