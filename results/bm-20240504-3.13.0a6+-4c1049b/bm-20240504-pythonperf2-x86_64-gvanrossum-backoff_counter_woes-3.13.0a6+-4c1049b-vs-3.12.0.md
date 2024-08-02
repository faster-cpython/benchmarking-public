# Results vs. 3.12.0

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-x86_64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x slower
- HPT reliability: 74.68%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 288 ms: 1.01x slower                                                             |
| chameleon      | 7.23 ms                                                      | 7.86 ms: 1.09x slower                                                            |
| docutils       | 2.87 sec                                                     | 3.02 sec: 1.05x slower                                                           |
| tornado_http   | 121 ms                                                       | 120 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 342 ms: 1.26x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 431 ms: 1.25x faster                                                             |
| async_tree_none            | 452 ms                                                       | 371 ms: 1.22x faster                                                             |
| async_tree_io              | 1.04 sec                                                     | 868 ms: 1.20x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 585 ms: 1.19x faster                                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 886 ms: 1.19x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 465 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 618 ms: 1.13x faster                                                             |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 257 ms: 1.03x faster                                                             |
| nbody          | 88.0 ms                                                      | 89.9 ms: 1.02x slower                                                            |
| float          | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.42 ms: 1.04x faster                                                            |
| regex_dna      | 239 ms                                                       | 235 ms: 1.01x faster                                                             |
| regex_compile  | 144 ms                                                       | 148 ms: 1.03x slower                                                             |
| regex_v8       | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.9 us: 1.05x faster                                                            |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                            |
| json_loads           | 24.4 us                                                      | 24.8 us: 1.02x slower                                                            |
| pickle_list          | 4.43 us                                                      | 4.52 us: 1.02x slower                                                            |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.03x slower                                                             |
| xml_etree_generate   | 86.1 ms                                                      | 88.6 ms: 1.03x slower                                                            |
| xml_etree_process    | 58.4 ms                                                      | 60.3 ms: 1.03x slower                                                            |
| unpickle_list        | 4.66 us                                                      | 4.82 us: 1.04x slower                                                            |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                            |
| tomli_loads          | 2.16 sec                                                     | 2.57 sec: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                     |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                            |
| python_startup         | 11.6 ms                                                      | 12.8 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.3 ms: 1.03x slower                                                            |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 342 ms: 1.26x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 431 ms: 1.25x faster                                                             |
| async_tree_none            | 452 ms                                                       | 371 ms: 1.22x faster                                                             |
| async_tree_io              | 1.04 sec                                                     | 868 ms: 1.20x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 585 ms: 1.19x faster                                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 886 ms: 1.19x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 465 ms: 1.17x faster                                                             |
| raytrace                   | 298 ms                                                       | 262 ms: 1.14x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 618 ms: 1.13x faster                                                             |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                                            |
| generators                 | 37.4 ms                                                      | 34.1 ms: 1.10x faster                                                            |
| chaos                      | 64.0 ms                                                      | 58.8 ms: 1.09x faster                                                            |
| async_generators           | 390 ms                                                       | 360 ms: 1.08x faster                                                             |
| mypy2                      | 830 ms                                                       | 774 ms: 1.07x faster                                                             |
| crypto_pyaes               | 80.3 ms                                                      | 75.1 ms: 1.07x faster                                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.4 ms: 1.06x faster                                                            |
| pickle_dict                | 32.5 us                                                      | 30.9 us: 1.05x faster                                                            |
| regex_effbot               | 3.57 ms                                                      | 3.42 ms: 1.04x faster                                                            |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.04x faster                                                            |
| bench_mp_pool              | 4.76 ms                                                      | 4.57 ms: 1.04x faster                                                            |
| bench_thread_pool          | 950 us                                                       | 912 us: 1.04x faster                                                             |
| logging_format             | 7.48 us                                                      | 7.21 us: 1.04x faster                                                            |
| sympy_sum                  | 162 ms                                                       | 157 ms: 1.03x faster                                                             |
| pidigits                   | 265 ms                                                       | 257 ms: 1.03x faster                                                             |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                           |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                            |
| logging_simple             | 6.71 us                                                      | 6.59 us: 1.02x faster                                                            |
| scimark_lu                 | 98.8 ms                                                      | 97.1 ms: 1.02x faster                                                            |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.02x faster                                                            |
| scimark_fft                | 301 ms                                                       | 297 ms: 1.01x faster                                                             |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.01x faster                                                             |
| nqueens                    | 89.9 ms                                                      | 88.6 ms: 1.01x faster                                                            |
| tornado_http               | 121 ms                                                       | 120 ms: 1.01x faster                                                             |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                           |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                                             |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                           |
| sympy_str                  | 302 ms                                                       | 301 ms: 1.01x faster                                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                                           |
| sqlite_synth               | 2.77 us                                                      | 2.79 us: 1.01x slower                                                            |
| pprint_safe_repr           | 807 ms                                                       | 813 ms: 1.01x slower                                                             |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                             |
| 2to3                       | 285 ms                                                       | 288 ms: 1.01x slower                                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                            |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                             |
| dulwich_log                | 65.4 ms                                                      | 66.5 ms: 1.02x slower                                                            |
| json_loads                 | 24.4 us                                                      | 24.8 us: 1.02x slower                                                            |
| fannkuch                   | 350 ms                                                       | 357 ms: 1.02x slower                                                             |
| python_startup_no_site     | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                            |
| pickle_list                | 4.43 us                                                      | 4.52 us: 1.02x slower                                                            |
| deepcopy_reduce            | 3.37 us                                                      | 3.44 us: 1.02x slower                                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.30 ms: 1.02x slower                                                            |
| nbody                      | 88.0 ms                                                      | 89.9 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                            |
| regex_compile              | 144 ms                                                       | 148 ms: 1.03x slower                                                             |
| unpickle_pure_python       | 210 us                                                       | 215 us: 1.03x slower                                                             |
| logging_silent             | 94.4 ns                                                      | 97.1 ns: 1.03x slower                                                            |
| xml_etree_generate         | 86.1 ms                                                      | 88.6 ms: 1.03x slower                                                            |
| django_template            | 38.2 ms                                                      | 39.3 ms: 1.03x slower                                                            |
| xml_etree_process          | 58.4 ms                                                      | 60.3 ms: 1.03x slower                                                            |
| spectral_norm              | 91.6 ms                                                      | 94.7 ms: 1.03x slower                                                            |
| unpickle_list              | 4.66 us                                                      | 4.82 us: 1.04x slower                                                            |
| deltablue                  | 3.24 ms                                                      | 3.35 ms: 1.04x slower                                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 59.7 ms: 1.04x slower                                                            |
| scimark_sor                | 109 ms                                                       | 113 ms: 1.04x slower                                                             |
| deepcopy_memo              | 36.8 us                                                      | 38.3 us: 1.04x slower                                                            |
| deepcopy                   | 368 us                                                       | 384 us: 1.04x slower                                                             |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                            |
| gunicorn                   | 1.00 ms                                                      | 1.05 ms: 1.05x slower                                                            |
| float                      | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                            |
| sqlglot_normalize          | 116 ms                                                       | 122 ms: 1.05x slower                                                             |
| docutils                   | 2.87 sec                                                     | 3.02 sec: 1.05x slower                                                           |
| hexiom                     | 5.96 ms                                                      | 6.29 ms: 1.06x slower                                                            |
| sympy_expand               | 484 ms                                                       | 513 ms: 1.06x slower                                                             |
| pyflate                    | 439 ms                                                       | 470 ms: 1.07x slower                                                             |
| json                       | 5.12 ms                                                      | 5.51 ms: 1.08x slower                                                            |
| aiohttp                    | 1.02 ms                                                      | 1.10 ms: 1.08x slower                                                            |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                            |
| chameleon                  | 7.23 ms                                                      | 7.86 ms: 1.09x slower                                                            |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                             |
| python_startup             | 11.6 ms                                                      | 12.8 ms: 1.10x slower                                                            |
| regex_v8                   | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                            |
| typing_runtime_protocols   | 152 us                                                       | 179 us: 1.18x slower                                                             |
| richards                   | 45.7 ms                                                      | 54.4 ms: 1.19x slower                                                            |
| tomli_loads                | 2.16 sec                                                     | 2.57 sec: 1.19x slower                                                           |
| telco                      | 6.96 ms                                                      | 8.30 ms: 1.19x slower                                                            |
| richards_super             | 51.3 ms                                                      | 61.4 ms: 1.19x slower                                                            |
| coverage                   | 66.7 ms                                                      | 83.2 ms: 1.25x slower                                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                                            |
| gc_traversal               | 3.48 ms                                                      | 4.67 ms: 1.34x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                     |

Benchmark hidden because not significant (5): pickle_pure_python, unpickle, xml_etree_parse, xml_etree_iterparse, dask
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 74.68% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.92x