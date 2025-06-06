# Results vs. 3.12.0

- fork: iritkatriel
- ref: dicts_plus
- machine: linux-x86_64
- commit hash: 3d9cf36
- commit date: 2025-04-12
- overall geometric mean: 1.136x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                              |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                              |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                              |
| async_tree_none            | 472 ms                                                 | 254 ms: 1.86x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.82x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 476 ms: 1.52x faster                                              |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.1 ms: 1.24x faster                                             |
| nbody          | 97.0 ms                                                | 90.0 ms: 1.08x faster                                             |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.11x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.19x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.16 ms: 1.14x faster                                             |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.08x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 83.2 ms: 1.07x faster                                             |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                             |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                              |
| json_loads           | 28.5 us                                                | 29.3 us: 1.03x slower                                             |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                             |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                             |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                             |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.1 ms: 1.11x faster                                             |
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                             |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.20 sec: 2.20x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                              |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                              |
| async_tree_none            | 472 ms                                                 | 254 ms: 1.86x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.82x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 476 ms: 1.52x faster                                              |
| deepcopy                   | 371 us                                                 | 248 us: 1.50x faster                                              |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.42x faster                                             |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.58 us: 1.30x faster                                             |
| go                         | 139 ms                                                 | 110 ms: 1.27x faster                                              |
| float                      | 84.7 ms                                                | 68.1 ms: 1.24x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                            |
| raytrace                   | 312 ms                                                 | 259 ms: 1.21x faster                                              |
| chaos                      | 67.0 ms                                                | 55.9 ms: 1.20x faster                                             |
| regex_compile              | 148 ms                                                 | 124 ms: 1.19x faster                                              |
| async_generators           | 463 ms                                                 | 390 ms: 1.19x faster                                              |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                             |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                             |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                             |
| dulwich_log                | 68.5 ms                                                | 59.2 ms: 1.16x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 65.2 ms: 1.15x faster                                             |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.15x faster                                              |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.16 ms: 1.14x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                              |
| sympy_str                  | 300 ms                                                 | 264 ms: 1.13x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 72.8 ms: 1.12x faster                                             |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.12x faster                                              |
| django_template            | 34.6 ms                                                | 31.1 ms: 1.11x faster                                             |
| scimark_fft                | 382 ms                                                 | 345 ms: 1.11x faster                                              |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.10x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.38 ms: 1.10x faster                                             |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                              |
| logging_silent             | 104 ns                                                 | 95.0 ns: 1.10x faster                                             |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 714 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.08x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                            |
| nbody                      | 97.0 ms                                                | 90.0 ms: 1.08x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 83.2 ms: 1.07x faster                                             |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                            |
| richards                   | 45.8 ms                                                | 42.8 ms: 1.07x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.73 ms: 1.07x faster                                             |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                             |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                             |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                              |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                            |
| richards_super             | 51.5 ms                                                | 49.2 ms: 1.05x faster                                             |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                             |
| nqueens                    | 83.3 ms                                                | 80.2 ms: 1.04x faster                                             |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                             |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                              |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                             |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                              |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                              |
| fannkuch                   | 417 ms                                                 | 412 ms: 1.01x faster                                              |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                              |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                             |
| json_loads                 | 28.5 us                                                | 29.3 us: 1.03x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                              |
| bench_thread_pool          | 842 us                                                 | 887 us: 1.05x slower                                              |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.10x slower                                             |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                             |
| coverage                   | 72.7 ms                                                | 87.6 ms: 1.21x slower                                             |
| gc_traversal               | 3.79 ms                                                | 4.72 ms: 1.24x slower                                             |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                             |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                      |

Benchmark hidden because not significant (3): asyncio_websockets, regex_v8, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250412-3.14.0a7+-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.136x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.11x