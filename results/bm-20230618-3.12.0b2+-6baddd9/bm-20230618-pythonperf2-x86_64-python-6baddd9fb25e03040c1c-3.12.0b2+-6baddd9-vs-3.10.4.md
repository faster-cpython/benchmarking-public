
# Results vs. 3.10.4

- fork: python
- ref: 6baddd9fb25e03040c1c
- machine: linux-x86_64
- commit hash: 6baddd9
- commit date: 2023-06-18
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                         |
| docutils       | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                                       |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                                         |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 84.8 ms: 1.62x faster                                                        |
| float          | 110 ms                                                       | 79.1 ms: 1.39x faster                                                        |
| pidigits       | 271 ms                                                       | 259 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.35x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                                        |
| regex_dna      | 259 ms                                                       | 241 ms: 1.08x faster                                                         |
| regex_effbot   | 2.99 ms                                                      | 3.53 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 209 us: 1.54x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 324 us: 1.41x faster                                                         |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.39x faster                                                        |
| tomli_loads          | 2.97 sec                                                     | 2.18 sec: 1.36x faster                                                       |
| xml_etree_process    | 76.0 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.3 us: 1.23x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 86.4 ms: 1.10x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 151 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                         |
| pickle               | 9.94 us                                                      | 10.3 us: 1.03x slower                                                        |
| unpickle             | 14.2 us                                                      | 14.7 us: 1.04x slower                                                        |
| unpickle_list        | 4.49 us                                                      | 4.75 us: 1.06x slower                                                        |
| pickle_list          | 4.11 us                                                      | 4.42 us: 1.08x slower                                                        |
| pickle_dict          | 30.0 us                                                      | 33.0 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.49 ms: 1.16x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.46x faster                                                         |
| deltablue                | 7.47 ms                                                      | 3.26 ms: 2.29x faster                                                        |
| asyncio_tcp              | 782 ms                                                       | 377 ms: 2.07x faster                                                         |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.56 sec: 1.98x faster                                                       |
| richards_super           | 90.8 ms                                                      | 51.5 ms: 1.76x faster                                                        |
| go                       | 259 ms                                                       | 147 ms: 1.76x faster                                                         |
| logging_silent           | 166 ns                                                       | 96.7 ns: 1.71x faster                                                        |
| chaos                    | 107 ms                                                       | 63.2 ms: 1.69x faster                                                        |
| scimark_lu               | 164 ms                                                       | 98.9 ms: 1.65x faster                                                        |
| raytrace                 | 488 ms                                                       | 297 ms: 1.64x faster                                                         |
| richards                 | 74.1 ms                                                      | 45.1 ms: 1.64x faster                                                        |
| hexiom                   | 9.52 ms                                                      | 5.81 ms: 1.64x faster                                                        |
| nbody                    | 137 ms                                                       | 84.8 ms: 1.62x faster                                                        |
| generators               | 58.0 ms                                                      | 35.9 ms: 1.62x faster                                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.40 ms: 1.61x faster                                                        |
| unpickle_pure_python     | 321 us                                                       | 209 us: 1.54x faster                                                         |
| pyflate                  | 697 ms                                                       | 458 ms: 1.52x faster                                                         |
| async_tree_none          | 700 ms                                                       | 460 ms: 1.52x faster                                                         |
| scimark_monte_carlo      | 109 ms                                                       | 72.0 ms: 1.52x faster                                                        |
| async_tree_io            | 1.61 sec                                                     | 1.06 sec: 1.51x faster                                                       |
| scimark_sor              | 177 ms                                                       | 117 ms: 1.51x faster                                                         |
| sqlglot_transpile        | 2.71 ms                                                      | 1.81 ms: 1.50x faster                                                        |
| spectral_norm            | 136 ms                                                       | 91.2 ms: 1.49x faster                                                        |
| async_tree_memoization   | 824 ms                                                       | 555 ms: 1.48x faster                                                         |
| mako                     | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                                        |
| fannkuch                 | 496 ms                                                       | 339 ms: 1.46x faster                                                         |
| crypto_pyaes             | 118 ms                                                       | 81.9 ms: 1.44x faster                                                        |
| pickle_pure_python       | 457 us                                                       | 324 us: 1.41x faster                                                         |
| float                    | 110 ms                                                       | 79.1 ms: 1.39x faster                                                        |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.39x faster                                                        |
| tomli_loads              | 2.97 sec                                                     | 2.18 sec: 1.36x faster                                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 705 ms: 1.35x faster                                                         |
| regex_compile            | 194 ms                                                       | 144 ms: 1.35x faster                                                         |
| coroutines               | 30.4 ms                                                      | 22.7 ms: 1.34x faster                                                        |
| pycparser                | 1.66 sec                                                     | 1.27 sec: 1.31x faster                                                       |
| logging_simple           | 8.90 us                                                      | 6.81 us: 1.31x faster                                                        |
| xml_etree_process        | 76.0 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.29x faster                                                       |
| deepcopy_memo            | 48.9 us                                                      | 37.8 us: 1.29x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 815 ms: 1.29x faster                                                         |
| logging_format           | 9.57 us                                                      | 7.51 us: 1.27x faster                                                        |
| tornado_http             | 152 ms                                                       | 121 ms: 1.26x faster                                                         |
| nqueens                  | 112 ms                                                       | 89.9 ms: 1.25x faster                                                        |
| json_loads               | 30.0 us                                                      | 24.3 us: 1.23x faster                                                        |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                         |
| comprehensions           | 26.9 us                                                      | 22.0 us: 1.22x faster                                                        |
| dulwich_log              | 80.1 ms                                                      | 65.9 ms: 1.21x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                         |
| mdp                      | 3.03 sec                                                     | 2.50 sec: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.30 ms: 1.21x faster                                                        |
| deepcopy                 | 454 us                                                       | 379 us: 1.20x faster                                                         |
| sqlglot_optimize         | 70.3 ms                                                      | 58.6 ms: 1.20x faster                                                        |
| unpack_sequence          | 59.5 ns                                                      | 49.8 ns: 1.20x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 952 us: 1.19x faster                                                         |
| scimark_fft              | 359 ms                                                       | 305 ms: 1.18x faster                                                         |
| docutils                 | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.44 us: 1.17x faster                                                        |
| json                     | 5.96 ms                                                      | 5.12 ms: 1.16x faster                                                        |
| regex_v8                 | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                                        |
| pathlib                  | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                                        |
| xml_etree_generate       | 94.6 ms                                                      | 86.4 ms: 1.10x faster                                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.67 ms: 1.09x faster                                                        |
| meteor_contest           | 137 ms                                                       | 125 ms: 1.09x faster                                                         |
| sqlite_synth             | 2.97 us                                                      | 2.73 us: 1.09x faster                                                        |
| async_generators         | 422 ms                                                       | 389 ms: 1.09x faster                                                         |
| regex_dna                | 259 ms                                                       | 241 ms: 1.08x faster                                                         |
| xml_etree_parse          | 162 ms                                                       | 151 ms: 1.07x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                         |
| pidigits                 | 271 ms                                                       | 259 ms: 1.04x faster                                                         |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                                        |
| telco                    | 7.14 ms                                                      | 7.26 ms: 1.02x slower                                                        |
| pickle                   | 9.94 us                                                      | 10.3 us: 1.03x slower                                                        |
| unpickle                 | 14.2 us                                                      | 14.7 us: 1.04x slower                                                        |
| unpickle_list            | 4.49 us                                                      | 4.75 us: 1.06x slower                                                        |
| pickle_list              | 4.11 us                                                      | 4.42 us: 1.08x slower                                                        |
| pickle_dict              | 30.0 us                                                      | 33.0 us: 1.10x slower                                                        |
| python_startup_no_site   | 7.32 ms                                                      | 8.49 ms: 1.16x slower                                                        |
| gc_traversal             | 3.45 ms                                                      | 4.00 ms: 1.16x slower                                                        |
| regex_effbot             | 2.99 ms                                                      | 3.53 ms: 1.18x slower                                                        |
| dask                     | 463 ms                                                       | 569 ms: 1.23x slower                                                         |
| bench_mp_pool            | 7.18 ms                                                      | 10.1 ms: 1.41x slower                                                        |
| coverage                 | 64.0 ms                                                      | 90.5 ms: 1.42x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x
