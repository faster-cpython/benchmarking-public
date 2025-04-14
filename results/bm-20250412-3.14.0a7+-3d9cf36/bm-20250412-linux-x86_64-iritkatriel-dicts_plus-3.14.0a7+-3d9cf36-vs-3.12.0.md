# Results vs. 3.12.0

- fork: iritkatriel
- ref: dicts_plus
- machine: linux-x86_64
- commit hash: 3d9cf36
- commit date: 2025-04-12
- overall geometric mean: 1.132x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                              |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                              |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.90x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                              |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.82x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 476 ms: 1.53x faster                                              |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.1 ms: 1.26x faster                                             |
| nbody          | 97.0 ms                                                | 95.2 ms: 1.02x faster                                             |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                             |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                             |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.07x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 83.4 ms: 1.07x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 58.2 ms: 1.06x faster                                             |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                              |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                              |
| json_loads           | 28.5 us                                                | 29.2 us: 1.02x slower                                             |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                             |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                             |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                             |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.10x faster                                             |
| mako            | 11.9 ms                                                | 11.2 ms: 1.07x faster                                             |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.20 sec: 2.19x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                              |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.90x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                              |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.82x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 476 ms: 1.53x faster                                              |
| deepcopy                   | 371 us                                                 | 249 us: 1.49x faster                                              |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.42x faster                                             |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                             |
| go                         | 139 ms                                                 | 110 ms: 1.26x faster                                              |
| float                      | 84.7 ms                                                | 67.1 ms: 1.26x faster                                             |
| logging_format             | 7.23 us                                                | 6.01 us: 1.20x faster                                             |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                            |
| chaos                      | 67.0 ms                                                | 56.0 ms: 1.20x faster                                             |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                              |
| logging_simple             | 6.46 us                                                | 5.44 us: 1.19x faster                                             |
| async_generators           | 463 ms                                                 | 393 ms: 1.18x faster                                              |
| spectral_norm              | 115 ms                                                 | 98.1 ms: 1.17x faster                                             |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                             |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                             |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 65.9 ms: 1.14x faster                                             |
| sympy_str                  | 300 ms                                                 | 264 ms: 1.13x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 72.3 ms: 1.13x faster                                             |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                              |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                              |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                             |
| scimark_fft                | 382 ms                                                 | 345 ms: 1.11x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                             |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.10x faster                                             |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                              |
| logging_silent             | 104 ns                                                 | 94.8 ns: 1.10x faster                                             |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.39 ms: 1.10x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                              |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.07x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                            |
| xml_etree_generate         | 89.2 ms                                                | 83.4 ms: 1.07x faster                                             |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                            |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.07x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 58.2 ms: 1.06x faster                                             |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                             |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.05x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.83 ms: 1.05x faster                                             |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                             |
| richards_super             | 51.5 ms                                                | 49.7 ms: 1.04x faster                                             |
| nqueens                    | 83.3 ms                                                | 80.8 ms: 1.03x faster                                             |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                              |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                              |
| nbody                      | 97.0 ms                                                | 95.2 ms: 1.02x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                              |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                              |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                             |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                              |
| json_loads                 | 28.5 us                                                | 29.2 us: 1.02x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                              |
| coroutines                 | 23.2 ms                                                | 24.1 ms: 1.04x slower                                             |
| bench_thread_pool          | 842 us                                                 | 884 us: 1.05x slower                                              |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                             |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                             |
| coverage                   | 72.7 ms                                                | 87.0 ms: 1.20x slower                                             |
| gc_traversal               | 3.79 ms                                                | 4.97 ms: 1.31x slower                                             |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                             |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250412-3.14.0a7+-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.132x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x