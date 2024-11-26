# Results vs. 3.12.0

- fork: faster-cpython
- ref: mark_first_2
- machine: linux-x86_64
- commit hash: 79ab26c
- commit date: 2024-11-22
- overall geometric mean: 1.016x faster
- HPT reliability: 86.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 657 ms: 1.60x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 666 ms: 1.56x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                           |
| async_tree_none            | 452 ms                                                       | 296 ms: 1.53x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 363 ms: 1.50x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.36x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 527 ms: 1.32x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.50x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                           |
| nbody          | 88.0 ms                                                      | 89.7 ms: 1.02x slower                                                          |
| float          | 76.6 ms                                                      | 79.3 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.36 ms: 1.06x faster                                                          |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                           |
| regex_dna      | 239 ms                                                       | 250 ms: 1.05x slower                                                           |
| regex_v8       | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.7 ms: 1.06x faster                                                          |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                           |
| xml_etree_generate   | 86.1 ms                                                      | 83.7 ms: 1.03x faster                                                          |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.01x slower                                                           |
| xml_etree_process    | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                                          |
| json_loads           | 24.4 us                                                      | 25.6 us: 1.05x slower                                                          |
| pickle_pure_python   | 318 us                                                       | 336 us: 1.06x slower                                                           |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                          |
| tomli_loads          | 2.16 sec                                                     | 2.52 sec: 1.17x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                          |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.9 ms: 1.01x faster                                                          |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 657 ms: 1.60x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 666 ms: 1.56x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                           |
| async_tree_none            | 452 ms                                                       | 296 ms: 1.53x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 363 ms: 1.50x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.36x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 527 ms: 1.32x faster                                                           |
| generators                 | 37.4 ms                                                      | 29.8 ms: 1.26x faster                                                          |
| deepcopy                   | 368 us                                                       | 297 us: 1.24x faster                                                           |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                          |
| deepcopy_memo              | 36.8 us                                                      | 30.7 us: 1.20x faster                                                          |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                          |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.14x faster                                                          |
| sqlalchemy_declarative     | 159 ms                                                       | 141 ms: 1.13x faster                                                           |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                          |
| crypto_pyaes               | 80.3 ms                                                      | 73.7 ms: 1.09x faster                                                          |
| go                         | 150 ms                                                       | 138 ms: 1.09x faster                                                           |
| xml_etree_iterparse        | 103 ms                                                       | 96.7 ms: 1.06x faster                                                          |
| regex_effbot               | 3.57 ms                                                      | 3.36 ms: 1.06x faster                                                          |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.06x faster                                                           |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                           |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                          |
| raytrace                   | 298 ms                                                       | 288 ms: 1.03x faster                                                           |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                           |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                         |
| sympy_str                  | 302 ms                                                       | 293 ms: 1.03x faster                                                           |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                           |
| scimark_lu                 | 98.8 ms                                                      | 95.8 ms: 1.03x faster                                                          |
| xml_etree_generate         | 86.1 ms                                                      | 83.7 ms: 1.03x faster                                                          |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.1 ms: 1.03x faster                                                          |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                          |
| bench_thread_pool          | 950 us                                                       | 931 us: 1.02x faster                                                           |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                         |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                           |
| chaos                      | 64.0 ms                                                      | 63.2 ms: 1.01x faster                                                          |
| django_template            | 38.2 ms                                                      | 37.9 ms: 1.01x faster                                                          |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 807 ms                                                       | 802 ms: 1.01x faster                                                           |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.01x slower                                                           |
| nbody                      | 88.0 ms                                                      | 89.7 ms: 1.02x slower                                                          |
| json                       | 5.12 ms                                                      | 5.22 ms: 1.02x slower                                                          |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.02x slower                                                           |
| logging_simple             | 6.71 us                                                      | 6.88 us: 1.03x slower                                                          |
| scimark_fft                | 301 ms                                                       | 309 ms: 1.03x slower                                                           |
| sqlite_synth               | 2.77 us                                                      | 2.85 us: 1.03x slower                                                          |
| xml_etree_process          | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                                          |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                                          |
| sqlglot_optimize           | 57.5 ms                                                      | 59.4 ms: 1.03x slower                                                          |
| float                      | 76.6 ms                                                      | 79.3 ms: 1.03x slower                                                          |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.03x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                          |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                          |
| dulwich_log                | 65.4 ms                                                      | 68.5 ms: 1.05x slower                                                          |
| regex_dna                  | 239 ms                                                       | 250 ms: 1.05x slower                                                           |
| json_loads                 | 24.4 us                                                      | 25.6 us: 1.05x slower                                                          |
| pickle_pure_python         | 318 us                                                       | 336 us: 1.06x slower                                                           |
| spectral_norm              | 91.6 ms                                                      | 96.9 ms: 1.06x slower                                                          |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                          |
| hexiom                     | 5.96 ms                                                      | 6.36 ms: 1.07x slower                                                          |
| fannkuch                   | 350 ms                                                       | 374 ms: 1.07x slower                                                           |
| richards                   | 45.7 ms                                                      | 49.7 ms: 1.09x slower                                                          |
| logging_silent             | 94.4 ns                                                      | 103 ns: 1.09x slower                                                           |
| richards_super             | 51.3 ms                                                      | 56.0 ms: 1.09x slower                                                          |
| deltablue                  | 3.24 ms                                                      | 3.55 ms: 1.10x slower                                                          |
| regex_v8                   | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                          |
| pyflate                    | 439 ms                                                       | 494 ms: 1.13x slower                                                           |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                          |
| async_generators           | 390 ms                                                       | 441 ms: 1.13x slower                                                           |
| telco                      | 6.96 ms                                                      | 7.88 ms: 1.13x slower                                                          |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.79 ms: 1.14x slower                                                          |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                           |
| tomli_loads                | 2.16 sec                                                     | 2.52 sec: 1.17x slower                                                         |
| scimark_sor                | 109 ms                                                       | 128 ms: 1.18x slower                                                           |
| coverage                   | 66.7 ms                                                      | 80.9 ms: 1.21x slower                                                          |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                          |
| create_gc_cycles           | 1.59 ms                                                      | 2.66 ms: 1.67x slower                                                          |
| gc_traversal               | 3.48 ms                                                      | 6.33 ms: 1.82x slower                                                          |
| bench_mp_pool              | 4.76 ms                                                      | 1.88 sec: 395.08x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                   |

Benchmark hidden because not significant (3): logging_format, 2to3, nqueens
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241122-3.14.0a2+-79ab26c/bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 86.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x