# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.05x slower
- HPT reliability: 76.55%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 306 ms: 1.07x slower                                                        |
| chameleon      | 7.23 ms                                                      | 8.00 ms: 1.11x slower                                                       |
| docutils       | 2.87 sec                                                     | 3.15 sec: 1.10x slower                                                      |
| tornado_http   | 121 ms                                                       | 124 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 344 ms: 1.25x faster                                                        |
| async_tree_none            | 452 ms                                                       | 374 ms: 1.21x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 453 ms: 1.19x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 874 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 586 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 890 ms: 1.18x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 468 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 621 ms: 1.12x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 82.6 ms: 1.07x faster                                                       |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 73.6 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_dna      | 239 ms                                                       | 239 ms: 1.00x slower                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.6 ms: 1.03x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.13 sec: 1.01x faster                                                      |
| pickle_dict          | 32.5 us                                                      | 32.2 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 24.5 us: 1.01x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 321 us: 1.01x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                       |
| pickle               | 10.5 us                                                      | 10.9 us: 1.04x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.88 us: 1.05x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.68 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.43 ms: 1.09x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.11 ms: 1.10x faster                                                       |
| django_template | 38.2 ms                                                      | 43.4 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 344 ms: 1.25x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.9 us: 1.23x faster                                                       |
| async_tree_none            | 452 ms                                                       | 374 ms: 1.21x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 453 ms: 1.19x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 874 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 586 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 890 ms: 1.18x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.16x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 468 ms: 1.16x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 70.6 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 621 ms: 1.12x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 83.0 ms: 1.10x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.11 ms: 1.10x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                       |
| generators                 | 37.4 ms                                                      | 34.9 ms: 1.07x faster                                                       |
| nbody                      | 88.0 ms                                                      | 82.6 ms: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.4 ms: 1.06x faster                                                       |
| raytrace                   | 298 ms                                                       | 284 ms: 1.05x faster                                                        |
| scimark_fft                | 301 ms                                                       | 289 ms: 1.04x faster                                                        |
| float                      | 76.6 ms                                                      | 73.6 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.06 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 99.6 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 790 ms: 1.02x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.13 sec: 1.01x faster                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                      |
| pickle_dict                | 32.5 us                                                      | 32.2 us: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 36.6 us: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| regex_dna                  | 239 ms                                                       | 239 ms: 1.00x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.01x slower                                                       |
| logging_simple             | 6.71 us                                                      | 6.76 us: 1.01x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 321 us: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                       |
| json                       | 5.12 ms                                                      | 5.18 ms: 1.01x slower                                                       |
| async_generators           | 390 ms                                                       | 396 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                                        |
| tornado_http               | 121 ms                                                       | 124 ms: 1.03x slower                                                        |
| richards_super             | 51.3 ms                                                      | 52.7 ms: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| dulwich_log                | 65.4 ms                                                      | 67.5 ms: 1.03x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.1 ms: 1.03x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 168 ms: 1.04x slower                                                        |
| pickle                     | 10.5 us                                                      | 10.9 us: 1.04x slower                                                       |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.44 ms: 1.04x slower                                                       |
| sympy_str                  | 302 ms                                                       | 315 ms: 1.04x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.85 ms: 1.04x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.88 us: 1.05x slower                                                       |
| dask                       | 392 ms                                                       | 411 ms: 1.05x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.68 us: 1.06x slower                                                       |
| pyflate                    | 439 ms                                                       | 470 ms: 1.07x slower                                                        |
| 2to3                       | 285 ms                                                       | 306 ms: 1.07x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 97.4 ms: 1.08x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 26.0 ms: 1.08x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.67 us: 1.09x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.43 ms: 1.09x slower                                                       |
| go                         | 150 ms                                                       | 164 ms: 1.09x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.15 sec: 1.10x slower                                                      |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| sympy_expand               | 484 ms                                                       | 535 ms: 1.10x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 8.00 ms: 1.11x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 105 ns: 1.11x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 64.4 ms: 1.12x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.68 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 130 ms: 1.12x slower                                                        |
| django_template            | 38.2 ms                                                      | 43.4 ms: 1.14x slower                                                       |
| deepcopy                   | 368 us                                                       | 424 us: 1.15x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 115 ms: 1.16x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.79 ms: 1.17x slower                                                       |
| scimark_sor                | 109 ms                                                       | 130 ms: 1.19x slower                                                        |
| coverage                   | 66.7 ms                                                      | 80.6 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 186 us: 1.23x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.96 ms: 1.23x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.45 ms: 1.28x slower                                                       |
| telco                      | 6.96 ms                                                      | 174 ms: 24.93x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (8): xml_etree_process, logging_format, fannkuch, unpickle, richards, asyncio_websockets, bench_mp_pool, bench_thread_pool
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 76.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x