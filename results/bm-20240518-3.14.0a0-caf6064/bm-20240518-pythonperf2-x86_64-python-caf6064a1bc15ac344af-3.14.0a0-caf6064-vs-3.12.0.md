# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.03x slower
- HPT reliability: 69.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                        |
| chameleon      | 7.23 ms                                                      | 7.29 ms: 1.01x slower                                                       |
| docutils       | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 339 ms: 1.27x faster                                                        |
| async_tree_none            | 452 ms                                                       | 366 ms: 1.23x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 441 ms: 1.22x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 865 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 885 ms: 1.19x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 465 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 615 ms: 1.13x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.70 ms: 1.04x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.7 us: 1.06x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 84.6 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| unpickle             | 14.8 us                                                      | 14.7 us: 1.01x faster                                                       |
| json_loads           | 24.4 us                                                      | 24.5 us: 1.00x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 105 ms: 1.02x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.77 us: 1.02x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 59.8 ms: 1.02x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.35 sec: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 12.8 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                       |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 339 ms: 1.27x faster                                                        |
| async_tree_none            | 452 ms                                                       | 366 ms: 1.23x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 441 ms: 1.22x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 865 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 885 ms: 1.19x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 465 ms: 1.17x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 615 ms: 1.13x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.1 ms: 1.11x faster                                                       |
| generators                 | 37.4 ms                                                      | 33.7 ms: 1.11x faster                                                       |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.2 ms: 1.08x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.97 us: 1.07x faster                                                       |
| chaos                      | 64.0 ms                                                      | 59.8 ms: 1.07x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 30.7 us: 1.06x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.37 us: 1.05x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 902 us: 1.05x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.53 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| async_generators           | 390 ms                                                       | 373 ms: 1.05x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.04x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                      |
| scimark_fft                | 301 ms                                                       | 295 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                                       |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 84.6 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 298 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| unpickle                   | 14.8 us                                                      | 14.7 us: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.00x slower                                                       |
| chameleon                  | 7.23 ms                                                      | 7.29 ms: 1.01x slower                                                       |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 105 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.44 us: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.77 us: 1.02x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.8 ms: 1.02x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 92.2 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                        |
| django_template            | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.6 ns: 1.03x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.70 ms: 1.04x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 38.2 us: 1.04x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 67.9 ms: 1.04x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                      |
| deepcopy                   | 368 us                                                       | 384 us: 1.04x slower                                                        |
| float                      | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 60.1 ms: 1.05x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                       |
| sympy_expand               | 484 ms                                                       | 507 ms: 1.05x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 96.4 ms: 1.05x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.41 ms: 1.06x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                                        |
| json                       | 5.12 ms                                                      | 5.42 ms: 1.06x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 123 ms: 1.06x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.33 ms: 1.06x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.35 sec: 1.09x slower                                                      |
| pyflate                    | 439 ms                                                       | 483 ms: 1.10x slower                                                        |
| python_startup             | 11.6 ms                                                      | 12.8 ms: 1.10x slower                                                       |
| richards                   | 45.7 ms                                                      | 51.6 ms: 1.13x slower                                                       |
| go                         | 150 ms                                                       | 170 ms: 1.14x slower                                                        |
| richards_super             | 51.3 ms                                                      | 59.2 ms: 1.15x slower                                                       |
| coverage                   | 66.7 ms                                                      | 77.7 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 177 us: 1.17x slower                                                        |
| scimark_sor                | 109 ms                                                       | 138 ms: 1.26x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.40 ms: 1.26x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.03 ms: 1.27x slower                                                       |
| telco                      | 6.96 ms                                                      | 170 ms: 24.39x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (8): pickle, nbody, pprint_pformat, pprint_safe_repr, pickle_list, scimark_lu, dask, asyncio_websockets
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 69.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.92x