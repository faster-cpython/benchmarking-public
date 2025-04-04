# Results vs. 3.12.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-x86_64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.124x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 248 ms: 1.11x faster                                                      |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                      |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 481 ms: 1.51x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.4 ms: 1.26x faster                                                     |
| nbody          | 97.0 ms                                                | 91.6 ms: 1.06x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                     |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                     |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.03x faster                                                      |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                     |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                     |
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                      |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 481 ms: 1.51x faster                                                      |
| deepcopy                   | 371 us                                                 | 253 us: 1.47x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                     |
| float                      | 84.7 ms                                                | 67.4 ms: 1.26x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                     |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                    |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                      |
| chaos                      | 67.0 ms                                                | 56.8 ms: 1.18x faster                                                     |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                      |
| async_generators           | 463 ms                                                 | 395 ms: 1.17x faster                                                      |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 59.1 ms: 1.16x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 65.1 ms: 1.15x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 72.5 ms: 1.13x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                                     |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                      |
| scimark_fft                | 382 ms                                                 | 344 ms: 1.11x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                     |
| 2to3                       | 274 ms                                                 | 248 ms: 1.11x faster                                                      |
| pyflate                    | 482 ms                                                 | 437 ms: 1.10x faster                                                      |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                      |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.67 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                                     |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                                      |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                    |
| nbody                      | 97.0 ms                                                | 91.6 ms: 1.06x faster                                                     |
| logging_silent             | 104 ns                                                 | 99.0 ns: 1.06x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                     |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                      |
| richards                   | 45.8 ms                                                | 44.0 ms: 1.04x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                      |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                     |
| richards_super             | 51.5 ms                                                | 50.0 ms: 1.03x faster                                                     |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.03x faster                                                      |
| generators                 | 31.2 ms                                                | 30.5 ms: 1.02x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                      |
| nqueens                    | 83.3 ms                                                | 82.4 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                      |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                     |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                                      |
| telco                      | 7.10 ms                                                | 7.75 ms: 1.09x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.76 ms: 1.26x slower                                                     |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (3): sqlite_synth, asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250404-3.14.0a6+-492df4e/bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.124x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x