# Results vs. 3.12.0

- fork: mdboom
- ref: tuple_hash
- machine: linux-x86_64
- commit hash: 0a71905
- commit date: 2025-03-18
- overall geometric mean: 1.019x faster
- HPT reliability: 66.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 650 ms: 1.60x faster                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 657 ms: 1.60x faster                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 342 ms: 1.58x faster                                               |
| async_tree_none_tg         | 431 ms                                                       | 276 ms: 1.56x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                               |
| async_tree_none            | 452 ms                                                       | 291 ms: 1.55x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                               |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 72.5 ms: 1.06x faster                                              |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                               |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                               |
| Geometric mean | (ref)                                                        | 1.02x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.17 ms: 1.13x faster                                              |
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                               |
| regex_v8       | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                              |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                               |
| xml_etree_iterparse  | 103 ms                                                       | 98.9 ms: 1.04x faster                                              |
| tomli_loads          | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                             |
| xml_etree_generate   | 86.1 ms                                                      | 85.7 ms: 1.01x faster                                              |
| xml_etree_process    | 58.4 ms                                                      | 60.5 ms: 1.04x slower                                              |
| pickle_pure_python   | 318 us                                                       | 338 us: 1.06x slower                                               |
| json_loads           | 24.4 us                                                      | 26.1 us: 1.07x slower                                              |
| unpickle_pure_python | 210 us                                                       | 225 us: 1.07x slower                                               |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                              |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                              |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                              |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.4 ms: 1.05x faster                                              |
| mako            | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                              |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 650 ms: 1.60x faster                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 657 ms: 1.60x faster                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 342 ms: 1.58x faster                                               |
| async_tree_none_tg         | 431 ms                                                       | 276 ms: 1.56x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                               |
| async_tree_none            | 452 ms                                                       | 291 ms: 1.55x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                               |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                              |
| deepcopy                   | 368 us                                                       | 296 us: 1.25x faster                                               |
| comprehensions             | 21.9 us                                                      | 17.6 us: 1.25x faster                                              |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                              |
| regex_effbot               | 3.57 ms                                                      | 3.17 ms: 1.13x faster                                              |
| go                         | 150 ms                                                       | 134 ms: 1.12x faster                                               |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                              |
| pathlib                    | 18.9 ms                                                      | 17.2 ms: 1.10x faster                                              |
| deepcopy_reduce            | 3.37 us                                                      | 3.08 us: 1.10x faster                                              |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                               |
| float                      | 76.6 ms                                                      | 72.5 ms: 1.06x faster                                              |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                               |
| django_template            | 38.2 ms                                                      | 36.4 ms: 1.05x faster                                              |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                               |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.2 ms: 1.04x faster                                              |
| dulwich_log                | 65.4 ms                                                      | 62.8 ms: 1.04x faster                                              |
| xml_etree_iterparse        | 103 ms                                                       | 98.9 ms: 1.04x faster                                              |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                              |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                               |
| logging_format             | 7.48 us                                                      | 7.21 us: 1.04x faster                                              |
| logging_simple             | 6.71 us                                                      | 6.49 us: 1.03x faster                                              |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.03x faster                                             |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                              |
| spectral_norm              | 91.6 ms                                                      | 90.2 ms: 1.02x faster                                              |
| sympy_str                  | 302 ms                                                       | 297 ms: 1.02x faster                                               |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.01x faster                                               |
| tomli_loads                | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                             |
| xml_etree_generate         | 86.1 ms                                                      | 85.7 ms: 1.01x faster                                              |
| logging_silent             | 94.4 ns                                                      | 95.1 ns: 1.01x slower                                              |
| regex_v8                   | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                              |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                             |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                               |
| chaos                      | 64.0 ms                                                      | 65.2 ms: 1.02x slower                                              |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                              |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                             |
| scimark_lu                 | 98.8 ms                                                      | 101 ms: 1.03x slower                                               |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                               |
| pprint_safe_repr           | 807 ms                                                       | 835 ms: 1.03x slower                                               |
| xml_etree_process          | 58.4 ms                                                      | 60.5 ms: 1.04x slower                                              |
| deltablue                  | 3.24 ms                                                      | 3.36 ms: 1.04x slower                                              |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.04x slower                                             |
| scimark_fft                | 301 ms                                                       | 314 ms: 1.04x slower                                               |
| sympy_expand               | 484 ms                                                       | 505 ms: 1.04x slower                                               |
| crypto_pyaes               | 80.3 ms                                                      | 84.7 ms: 1.05x slower                                              |
| json                       | 5.12 ms                                                      | 5.42 ms: 1.06x slower                                              |
| pyflate                    | 439 ms                                                       | 464 ms: 1.06x slower                                               |
| pickle_pure_python         | 318 us                                                       | 338 us: 1.06x slower                                               |
| nqueens                    | 89.9 ms                                                      | 96.1 ms: 1.07x slower                                              |
| json_loads                 | 24.4 us                                                      | 26.1 us: 1.07x slower                                              |
| unpickle_pure_python       | 210 us                                                       | 225 us: 1.07x slower                                               |
| async_generators           | 390 ms                                                       | 421 ms: 1.08x slower                                               |
| richards                   | 45.7 ms                                                      | 49.5 ms: 1.08x slower                                              |
| richards_super             | 51.3 ms                                                      | 55.8 ms: 1.09x slower                                              |
| hexiom                     | 5.96 ms                                                      | 6.51 ms: 1.09x slower                                              |
| fannkuch                   | 350 ms                                                       | 388 ms: 1.11x slower                                               |
| mako                       | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                              |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.12x slower                                               |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                              |
| telco                      | 6.96 ms                                                      | 8.02 ms: 1.15x slower                                              |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.85 ms: 1.15x slower                                              |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                               |
| coverage                   | 66.7 ms                                                      | 80.6 ms: 1.21x slower                                              |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                              |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                              |
| create_gc_cycles           | 1.59 ms                                                      | 2.81 ms: 1.77x slower                                              |
| gc_traversal               | 3.48 ms                                                      | 6.61 ms: 1.90x slower                                              |
| bench_mp_pool              | 4.76 ms                                                      | 1.22 sec: 256.93x slower                                           |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                       |

Benchmark hidden because not significant (4): asyncio_websockets, raytrace, 2to3, bench_thread_pool
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250318-3.14.0a6+-0a71905/bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.019x faster

# HPT report

- Reliability score: 66.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x