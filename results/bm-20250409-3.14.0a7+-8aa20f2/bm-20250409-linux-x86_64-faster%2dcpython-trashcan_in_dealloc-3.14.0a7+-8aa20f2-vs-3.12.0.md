# Results vs. 3.12.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-x86_64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                            |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                            |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.7 ms: 1.22x faster                                                           |
| nbody          | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                           |
| regex_v8       | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                           |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 84.3 ms: 1.06x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.05x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                            |
| json_loads           | 28.5 us                                                | 30.3 us: 1.06x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.19x slower                                                           |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.09x faster                                                           |
| mako            | 11.9 ms                                                | 11.1 ms: 1.08x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                            |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                            |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                           |
| go                         | 139 ms                                                 | 108 ms: 1.29x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                           |
| float                      | 84.7 ms                                                | 69.7 ms: 1.22x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                          |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                            |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                            |
| logging_format             | 7.23 us                                                | 6.21 us: 1.17x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                           |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.15x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 59.9 ms: 1.14x faster                                                           |
| async_generators           | 463 ms                                                 | 405 ms: 1.14x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 66.7 ms: 1.13x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                                           |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                            |
| pyflate                    | 482 ms                                                 | 437 ms: 1.10x faster                                                            |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                           |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                            |
| nbody                      | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                           |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.09x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                           |
| richards                   | 45.8 ms                                                | 42.5 ms: 1.08x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 76.0 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 721 ms: 1.08x faster                                                            |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.08x faster                                                           |
| scimark_fft                | 382 ms                                                 | 356 ms: 1.07x faster                                                            |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                            |
| logging_silent             | 104 ns                                                 | 97.6 ns: 1.07x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                          |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                           |
| richards_super             | 51.5 ms                                                | 48.6 ms: 1.06x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 84.3 ms: 1.06x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.05x faster                                                           |
| regex_v8                   | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.12 ms: 1.05x faster                                                           |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                          |
| nqueens                    | 83.3 ms                                                | 81.6 ms: 1.02x faster                                                           |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                           |
| fannkuch                   | 417 ms                                                 | 415 ms: 1.01x faster                                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                            |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                           |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                                            |
| json_loads                 | 28.5 us                                                | 30.3 us: 1.06x slower                                                           |
| json                       | 5.26 ms                                                | 5.63 ms: 1.07x slower                                                           |
| telco                      | 7.10 ms                                                | 7.99 ms: 1.12x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                           |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.19x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 4.79 ms: 1.26x slower                                                           |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 82.4 ms: 3.43x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                    |

Benchmark hidden because not significant (2): scimark_lu, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.123x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x