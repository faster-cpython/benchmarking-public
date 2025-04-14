# Results vs. 3.12.0

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: a31e8be
- commit date: 2025-03-20
- overall geometric mean: 1.024x faster
- HPT reliability: 60.18%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 288 ms: 1.01x slower                                                      |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 660 ms: 1.58x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 668 ms: 1.58x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 284 ms: 1.52x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 359 ms: 1.52x faster                                                      |
| async_tree_none            | 452 ms                                                       | 299 ms: 1.51x faster                                                      |
| async_tree_memoization_tg  | 540 ms                                                       | 359 ms: 1.50x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 521 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 528 ms: 1.32x faster                                                      |
| Geometric mean             | (ref)                                                        | 1.48x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.9 ms: 1.07x faster                                                     |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                      |
| nbody          | 88.0 ms                                                      | 103 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                        | 1.02x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.01 ms: 1.19x faster                                                     |
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                      |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                                      |
| regex_v8       | 23.6 ms                                                      | 24.0 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                        | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 98.8 ms: 1.04x faster                                                     |
| xml_etree_generate   | 86.1 ms                                                      | 86.7 ms: 1.01x slower                                                     |
| tomli_loads          | 2.16 sec                                                     | 2.19 sec: 1.01x slower                                                    |
| xml_etree_process    | 58.4 ms                                                      | 61.4 ms: 1.05x slower                                                     |
| unpickle_pure_python | 210 us                                                       | 224 us: 1.07x slower                                                      |
| pickle_pure_python   | 318 us                                                       | 340 us: 1.07x slower                                                      |
| json_loads           | 24.4 us                                                      | 26.3 us: 1.08x slower                                                     |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                     |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.5 ms: 1.02x faster                                                     |
| mako            | 10.0 ms                                                      | 11.2 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.34 sec: 1.92x faster                                                    |
| async_tree_io              | 1.04 sec                                                     | 660 ms: 1.58x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 668 ms: 1.58x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 284 ms: 1.52x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 359 ms: 1.52x faster                                                      |
| async_tree_none            | 452 ms                                                       | 299 ms: 1.51x faster                                                      |
| async_tree_memoization_tg  | 540 ms                                                       | 359 ms: 1.50x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 521 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 528 ms: 1.32x faster                                                      |
| generators                 | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                     |
| deepcopy                   | 368 us                                                       | 289 us: 1.28x faster                                                      |
| comprehensions             | 21.9 us                                                      | 17.9 us: 1.22x faster                                                     |
| deepcopy_memo              | 36.8 us                                                      | 30.4 us: 1.21x faster                                                     |
| regex_effbot               | 3.57 ms                                                      | 3.01 ms: 1.19x faster                                                     |
| deepcopy_reduce            | 3.37 us                                                      | 3.00 us: 1.12x faster                                                     |
| go                         | 150 ms                                                       | 133 ms: 1.12x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                     |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 159 ms                                                       | 148 ms: 1.08x faster                                                      |
| float                      | 76.6 ms                                                      | 71.9 ms: 1.07x faster                                                     |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.6 ms: 1.05x faster                                                     |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                      |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 98.8 ms: 1.04x faster                                                     |
| dulwich_log                | 65.4 ms                                                      | 63.2 ms: 1.03x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.03x faster                                                     |
| logging_format             | 7.48 us                                                      | 7.31 us: 1.02x faster                                                     |
| logging_simple             | 6.71 us                                                      | 6.56 us: 1.02x faster                                                     |
| django_template            | 38.2 ms                                                      | 37.5 ms: 1.02x faster                                                     |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                                      |
| logging_silent             | 94.4 ns                                                      | 94.9 ns: 1.01x slower                                                     |
| xml_etree_generate         | 86.1 ms                                                      | 86.7 ms: 1.01x slower                                                     |
| raytrace                   | 298 ms                                                       | 301 ms: 1.01x slower                                                      |
| 2to3                       | 285 ms                                                       | 288 ms: 1.01x slower                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.19 sec: 1.01x slower                                                    |
| regex_v8                   | 23.6 ms                                                      | 24.0 ms: 1.01x slower                                                     |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                    |
| crypto_pyaes               | 80.3 ms                                                      | 81.5 ms: 1.01x slower                                                     |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                                    |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.86 us: 1.03x slower                                                     |
| chaos                      | 64.0 ms                                                      | 65.9 ms: 1.03x slower                                                     |
| richards                   | 45.7 ms                                                      | 47.2 ms: 1.03x slower                                                     |
| pprint_safe_repr           | 807 ms                                                       | 838 ms: 1.04x slower                                                      |
| richards_super             | 51.3 ms                                                      | 53.4 ms: 1.04x slower                                                     |
| scimark_lu                 | 98.8 ms                                                      | 103 ms: 1.04x slower                                                      |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.04x slower                                                     |
| pycparser                  | 1.23 sec                                                     | 1.30 sec: 1.05x slower                                                    |
| xml_etree_process          | 58.4 ms                                                      | 61.4 ms: 1.05x slower                                                     |
| pyflate                    | 439 ms                                                       | 464 ms: 1.06x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 224 us: 1.07x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 340 us: 1.07x slower                                                      |
| json                       | 5.12 ms                                                      | 5.50 ms: 1.07x slower                                                     |
| scimark_fft                | 301 ms                                                       | 324 ms: 1.08x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 96.7 ms: 1.08x slower                                                     |
| json_loads                 | 24.4 us                                                      | 26.3 us: 1.08x slower                                                     |
| hexiom                     | 5.96 ms                                                      | 6.45 ms: 1.08x slower                                                     |
| async_generators           | 390 ms                                                       | 424 ms: 1.09x slower                                                      |
| fannkuch                   | 350 ms                                                       | 388 ms: 1.11x slower                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.72 ms: 1.12x slower                                                     |
| mako                       | 10.0 ms                                                      | 11.2 ms: 1.12x slower                                                     |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                     |
| telco                      | 6.96 ms                                                      | 7.94 ms: 1.14x slower                                                     |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                      |
| nbody                      | 88.0 ms                                                      | 103 ms: 1.17x slower                                                      |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                                     |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                     |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                     |
| create_gc_cycles           | 1.59 ms                                                      | 2.83 ms: 1.78x slower                                                     |
| gc_traversal               | 3.48 ms                                                      | 6.38 ms: 1.83x slower                                                     |
| bench_mp_pool              | 4.76 ms                                                      | 1.07 sec: 225.15x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                              |

Benchmark hidden because not significant (3): spectral_norm, asyncio_websockets, bench_thread_pool
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250320-3.14.0a6+-a31e8be/bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 60.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x