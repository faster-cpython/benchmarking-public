# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.039x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 309 ms: 1.13x slower                                             |
| docutils       | 2.77 sec                                               | 2.83 sec: 1.02x slower                                           |
| Geometric mean | (ref)                                                  | 1.07x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 551 ms: 2.15x faster                                             |
| async_tree_io              | 1.16 sec                                               | 596 ms: 1.94x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 239 ms: 1.88x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                             |
| async_tree_none            | 472 ms                                                 | 287 ms: 1.64x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 366 ms: 1.58x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 528 ms: 1.38x faster                                             |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.1 ms: 1.07x faster                                            |
| pidigits       | 187 ms                                                 | 181 ms: 1.03x faster                                             |
| nbody          | 97.0 ms                                                | 140 ms: 1.44x slower                                             |
| Geometric mean | (ref)                                                  | 1.09x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.48 ms: 1.04x faster                                            |
| regex_compile  | 148 ms                                                 | 150 ms: 1.01x slower                                             |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                             |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                  | 1.03x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 95.2 ms: 1.12x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                             |
| tomli_loads          | 2.33 sec                                               | 2.41 sec: 1.03x slower                                           |
| xml_etree_generate   | 89.2 ms                                                | 96.3 ms: 1.08x slower                                            |
| json_loads           | 28.5 us                                                | 31.8 us: 1.12x slower                                            |
| xml_etree_process    | 61.7 ms                                                | 72.1 ms: 1.17x slower                                            |
| pickle_pure_python   | 324 us                                                 | 380 us: 1.17x slower                                             |
| unpickle_pure_python | 230 us                                                 | 270 us: 1.17x slower                                             |
| json_dumps           | 10.4 ms                                                | 12.9 ms: 1.24x slower                                            |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.34 ms: 1.35x slower                                            |
| python_startup         | 9.55 ms                                                | 15.0 ms: 1.57x slower                                            |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 41.7 ms: 1.21x slower                                            |
| mako            | 11.9 ms                                                | 16.5 ms: 1.39x slower                                            |
| Geometric mean  | (ref)                                                  | 1.29x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 551 ms: 2.15x faster                                             |
| async_tree_io              | 1.16 sec                                               | 596 ms: 1.94x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 239 ms: 1.88x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                             |
| async_tree_none            | 472 ms                                                 | 287 ms: 1.64x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 366 ms: 1.58x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 528 ms: 1.38x faster                                             |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                            |
| deepcopy                   | 371 us                                                 | 318 us: 1.17x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 95.2 ms: 1.12x faster                                            |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                             |
| float                      | 84.7 ms                                                | 79.1 ms: 1.07x faster                                            |
| async_generators           | 463 ms                                                 | 438 ms: 1.06x faster                                             |
| comprehensions             | 21.8 us                                                | 20.9 us: 1.04x faster                                            |
| regex_effbot               | 3.61 ms                                                | 3.48 ms: 1.04x faster                                            |
| pidigits                   | 187 ms                                                 | 181 ms: 1.03x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                            |
| deepcopy_memo              | 40.7 us                                                | 39.9 us: 1.02x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 3.30 us: 1.01x faster                                            |
| generators                 | 31.2 ms                                                | 30.8 ms: 1.01x faster                                            |
| regex_compile              | 148 ms                                                 | 150 ms: 1.01x slower                                             |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                             |
| docutils                   | 2.77 sec                                               | 2.83 sec: 1.02x slower                                           |
| dulwich_log                | 68.5 ms                                                | 70.1 ms: 1.02x slower                                            |
| tomli_loads                | 2.33 sec                                               | 2.41 sec: 1.03x slower                                           |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.04x slower                                             |
| pycparser                  | 1.18 sec                                               | 1.23 sec: 1.04x slower                                           |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                           |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                             |
| sympy_sum                  | 169 ms                                                 | 178 ms: 1.05x slower                                             |
| logging_simple             | 6.46 us                                                | 6.90 us: 1.07x slower                                            |
| logging_format             | 7.23 us                                                | 7.74 us: 1.07x slower                                            |
| sympy_str                  | 300 ms                                                 | 321 ms: 1.07x slower                                             |
| json                       | 5.26 ms                                                | 5.65 ms: 1.07x slower                                            |
| xml_etree_generate         | 89.2 ms                                                | 96.3 ms: 1.08x slower                                            |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                            |
| pyflate                    | 482 ms                                                 | 528 ms: 1.10x slower                                             |
| sqlglot_normalize          | 110 ms                                                 | 121 ms: 1.10x slower                                             |
| gc_traversal               | 3.79 ms                                                | 4.17 ms: 1.10x slower                                            |
| chaos                      | 67.0 ms                                                | 74.0 ms: 1.11x slower                                            |
| sqlglot_optimize           | 54.8 ms                                                | 60.7 ms: 1.11x slower                                            |
| scimark_sor                | 129 ms                                                 | 143 ms: 1.11x slower                                             |
| crypto_pyaes               | 81.9 ms                                                | 90.8 ms: 1.11x slower                                            |
| sympy_integrate            | 21.4 ms                                                | 23.8 ms: 1.11x slower                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 163 ms: 1.11x slower                                             |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.8 ms: 1.11x slower                                            |
| json_loads                 | 28.5 us                                                | 31.8 us: 1.12x slower                                            |
| pprint_safe_repr           | 776 ms                                                 | 865 ms: 1.12x slower                                             |
| sympy_expand               | 478 ms                                                 | 536 ms: 1.12x slower                                             |
| scimark_fft                | 382 ms                                                 | 429 ms: 1.12x slower                                             |
| 2to3                       | 274 ms                                                 | 309 ms: 1.13x slower                                             |
| pprint_pformat             | 1.57 sec                                               | 1.78 sec: 1.14x slower                                           |
| raytrace                   | 312 ms                                                 | 356 ms: 1.14x slower                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.56 ms: 1.14x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.70 ms: 1.15x slower                                            |
| coroutines                 | 23.2 ms                                                | 26.7 ms: 1.15x slower                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.95 ms: 1.16x slower                                            |
| logging_silent             | 104 ns                                                 | 121 ns: 1.16x slower                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 87.3 ms: 1.16x slower                                            |
| xml_etree_process          | 61.7 ms                                                | 72.1 ms: 1.17x slower                                            |
| pickle_pure_python         | 324 us                                                 | 380 us: 1.17x slower                                             |
| unpickle_pure_python       | 230 us                                                 | 270 us: 1.17x slower                                             |
| richards                   | 45.8 ms                                                | 53.8 ms: 1.17x slower                                            |
| meteor_contest             | 112 ms                                                 | 133 ms: 1.18x slower                                             |
| nqueens                    | 83.3 ms                                                | 99.3 ms: 1.19x slower                                            |
| django_template            | 34.6 ms                                                | 41.7 ms: 1.21x slower                                            |
| scimark_lu                 | 118 ms                                                 | 143 ms: 1.21x slower                                             |
| richards_super             | 51.5 ms                                                | 62.3 ms: 1.21x slower                                            |
| hexiom                     | 6.41 ms                                                | 7.78 ms: 1.21x slower                                            |
| fannkuch                   | 417 ms                                                 | 514 ms: 1.23x slower                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.24 ms: 1.23x slower                                            |
| json_dumps                 | 10.4 ms                                                | 12.9 ms: 1.24x slower                                            |
| deltablue                  | 3.72 ms                                                | 4.68 ms: 1.26x slower                                            |
| telco                      | 7.10 ms                                                | 9.10 ms: 1.28x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 9.34 ms: 1.35x slower                                            |
| typing_runtime_protocols   | 158 us                                                 | 215 us: 1.36x slower                                             |
| mako                       | 11.9 ms                                                | 16.5 ms: 1.39x slower                                            |
| nbody                      | 97.0 ms                                                | 140 ms: 1.44x slower                                             |
| coverage                   | 72.7 ms                                                | 108 ms: 1.49x slower                                             |
| python_startup             | 9.55 ms                                                | 15.0 ms: 1.57x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 89.3 ms: 3.72x slower                                            |
| bench_thread_pool          | 842 us                                                 | 3.50 ms: 4.16x slower                                            |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250123-3.14.0a4+-8ffb2c1-NOGIL/bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.31x