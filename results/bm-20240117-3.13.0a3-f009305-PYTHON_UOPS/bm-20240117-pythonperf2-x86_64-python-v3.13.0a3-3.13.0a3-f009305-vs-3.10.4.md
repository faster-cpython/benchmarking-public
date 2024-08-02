
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 308 ms: 1.14x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.89 ms: 1.20x faster                                            |
| docutils       | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                           |
| tornado_http   | 157 ms                                                       | 123 ms: 1.27x faster                                             |
| Geometric mean | (ref)                                                        | 1.19x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 446 ms: 1.55x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 558 ms: 1.47x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 1.10 sec: 1.46x faster                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 710 ms: 1.32x faster                                             |
| Geometric mean          | (ref)                                                        | 1.45x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 111 ms                                                       | 103 ms: 1.08x faster                                             |
| nbody          | 134 ms                                                       | 125 ms: 1.07x faster                                             |
| pidigits       | 271 ms                                                       | 265 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                        | 1.06x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 170 ms: 1.12x faster                                             |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                             |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                            |
| regex_effbot   | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 311 us: 1.46x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                            |
| unpickle_pure_python | 312 us                                                       | 245 us: 1.28x faster                                             |
| xml_etree_process    | 75.9 ms                                                      | 62.3 ms: 1.22x faster                                            |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                             |
| tomli_loads          | 2.92 sec                                                     | 2.82 sec: 1.03x faster                                           |
| xml_etree_generate   | 92.3 ms                                                      | 90.9 ms: 1.02x faster                                            |
| unpickle_list        | 4.65 us                                                      | 4.74 us: 1.02x slower                                            |
| pickle_dict          | 29.5 us                                                      | 30.7 us: 1.04x slower                                            |
| pickle               | 9.89 us                                                      | 10.3 us: 1.05x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.32 us: 1.05x slower                                            |
| xml_etree_iterparse  | 110 ms                                                       | 117 ms: 1.06x slower                                             |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                            |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.5 ms: 1.09x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 11.0 ms: 1.50x slower                                            |
| Geometric mean         | (ref)                                                        | 1.28x slower                                                     |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 124 us: 4.33x faster                                             |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                           |
| logging_silent           | 167 ns                                                       | 98.9 ns: 1.69x faster                                            |
| generators               | 57.3 ms                                                      | 34.3 ms: 1.67x faster                                            |
| raytrace                 | 489 ms                                                       | 305 ms: 1.60x faster                                             |
| scimark_lu               | 167 ms                                                       | 104 ms: 1.60x faster                                             |
| async_tree_none          | 692 ms                                                       | 446 ms: 1.55x faster                                             |
| sqlglot_parse            | 2.24 ms                                                      | 1.45 ms: 1.54x faster                                            |
| richards_super           | 90.6 ms                                                      | 60.0 ms: 1.51x faster                                            |
| async_tree_memoization   | 819 ms                                                       | 558 ms: 1.47x faster                                             |
| pickle_pure_python       | 455 us                                                       | 311 us: 1.46x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 1.10 sec: 1.46x faster                                           |
| go                       | 262 ms                                                       | 180 ms: 1.45x faster                                             |
| sqlglot_transpile        | 2.68 ms                                                      | 1.87 ms: 1.43x faster                                            |
| chaos                    | 109 ms                                                       | 77.4 ms: 1.40x faster                                            |
| deltablue                | 7.50 ms                                                      | 5.40 ms: 1.39x faster                                            |
| richards                 | 75.1 ms                                                      | 54.5 ms: 1.38x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 86.6 ms: 1.38x faster                                            |
| unpack_sequence          | 59.9 ns                                                      | 44.2 ns: 1.36x faster                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.73 ms: 1.35x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.34x faster                                            |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 710 ms: 1.32x faster                                             |
| logging_format           | 9.64 us                                                      | 7.38 us: 1.31x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.88 us: 1.29x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 245 us: 1.28x faster                                             |
| tornado_http             | 157 ms                                                       | 123 ms: 1.27x faster                                             |
| pyflate                  | 733 ms                                                       | 582 ms: 1.26x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 40.3 us: 1.23x faster                                            |
| deepcopy                 | 468 us                                                       | 379 us: 1.23x faster                                             |
| scimark_sor              | 180 ms                                                       | 147 ms: 1.23x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.36 sec: 1.23x faster                                           |
| xml_etree_process        | 75.9 ms                                                      | 62.3 ms: 1.22x faster                                            |
| scimark_monte_carlo      | 107 ms                                                       | 88.7 ms: 1.21x faster                                            |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                            |
| chameleon                | 9.44 ms                                                      | 7.89 ms: 1.20x faster                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.41 us: 1.18x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 969 us: 1.18x faster                                             |
| docutils                 | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                           |
| dask                     | 472 ms                                                       | 407 ms: 1.16x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 124 ms: 1.16x faster                                             |
| sympy_sum                | 193 ms                                                       | 166 ms: 1.16x faster                                             |
| pprint_safe_repr         | 1.05 sec                                                     | 921 ms: 1.14x faster                                             |
| mdp                      | 3.01 sec                                                     | 2.64 sec: 1.14x faster                                           |
| 2to3                     | 350 ms                                                       | 308 ms: 1.14x faster                                             |
| sympy_integrate          | 28.2 ms                                                      | 24.8 ms: 1.13x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.90 sec: 1.13x faster                                           |
| async_generators         | 421 ms                                                       | 372 ms: 1.13x faster                                             |
| dulwich_log              | 81.1 ms                                                      | 72.1 ms: 1.13x faster                                            |
| sympy_expand             | 600 ms                                                       | 534 ms: 1.12x faster                                             |
| sympy_str                | 360 ms                                                       | 322 ms: 1.12x faster                                             |
| pathlib                  | 21.4 ms                                                      | 19.1 ms: 1.12x faster                                            |
| regex_compile            | 190 ms                                                       | 170 ms: 1.12x faster                                             |
| create_gc_cycles         | 1.76 ms                                                      | 1.59 ms: 1.11x faster                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 63.6 ms: 1.10x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                             |
| json                     | 5.86 ms                                                      | 5.35 ms: 1.10x faster                                            |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                             |
| float                    | 111 ms                                                       | 103 ms: 1.08x faster                                             |
| nbody                    | 134 ms                                                       | 125 ms: 1.07x faster                                             |
| comprehensions           | 26.7 us                                                      | 25.0 us: 1.07x faster                                            |
| nqueens                  | 115 ms                                                       | 108 ms: 1.07x faster                                             |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                            |
| tomli_loads              | 2.92 sec                                                     | 2.82 sec: 1.03x faster                                           |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                            |
| pidigits                 | 271 ms                                                       | 265 ms: 1.02x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 90.9 ms: 1.02x faster                                            |
| meteor_contest           | 138 ms                                                       | 139 ms: 1.00x slower                                             |
| unpickle_list            | 4.65 us                                                      | 4.74 us: 1.02x slower                                            |
| pickle_dict              | 29.5 us                                                      | 30.7 us: 1.04x slower                                            |
| hexiom                   | 9.42 ms                                                      | 9.82 ms: 1.04x slower                                            |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.05x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.32 us: 1.05x slower                                            |
| xml_etree_iterparse      | 110 ms                                                       | 117 ms: 1.06x slower                                             |
| python_startup           | 11.5 ms                                                      | 12.5 ms: 1.09x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 3.74 ms: 1.09x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                            |
| telco                    | 7.23 ms                                                      | 8.28 ms: 1.15x slower                                            |
| spectral_norm            | 139 ms                                                       | 161 ms: 1.16x slower                                             |
| scimark_fft              | 361 ms                                                       | 429 ms: 1.19x slower                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.49 ms: 1.28x slower                                            |
| coverage                 | 63.3 ms                                                      | 81.8 ms: 1.29x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 11.0 ms: 1.50x slower                                            |
| Geometric mean           | (ref)                                                        | 1.18x faster                                                     |

Benchmark hidden because not significant (4): mypy2, fannkuch, asyncio_websockets, mako
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x


# Memory

- memory change: 1.07x