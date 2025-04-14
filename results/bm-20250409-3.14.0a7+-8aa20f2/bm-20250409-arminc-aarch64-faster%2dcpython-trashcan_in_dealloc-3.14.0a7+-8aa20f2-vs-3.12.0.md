# Results vs. 3.12.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-aarch64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                                              |
| docutils       | 2.98 sec                                                              | 2.94 sec: 1.02x faster                                                            |
| html5lib       | 65.1 ms                                                               | 63.0 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 458 ms: 1.70x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 873 ms: 1.62x faster                                                              |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.61x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 879 ms: 1.60x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 371 ms: 1.56x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                             |
| pidigits       | 233 ms                                                                | 233 ms: 1.00x slower                                                              |
| nbody          | 105 ms                                                                | 121 ms: 1.16x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                             |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| regex_dna      | 254 ms                                                                | 242 ms: 1.05x faster                                                              |
| regex_v8       | 28.3 ms                                                               | 27.8 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 175 ms: 1.11x faster                                                              |
| xml_etree_iterparse  | 150 ms                                                                | 140 ms: 1.07x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                            |
| unpickle_pure_python | 260 us                                                                | 262 us: 1.01x slower                                                              |
| pickle_pure_python   | 365 us                                                                | 387 us: 1.06x slower                                                              |
| json_loads           | 30.7 us                                                               | 34.8 us: 1.13x slower                                                             |
| json_dumps           | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                             |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.64 sec: 2.08x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 458 ms: 1.70x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 873 ms: 1.62x faster                                                              |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.61x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 879 ms: 1.60x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 371 ms: 1.56x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                                              |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                             |
| go                         | 157 ms                                                                | 131 ms: 1.20x faster                                                              |
| dulwich_log                | 62.0 ms                                                               | 52.5 ms: 1.18x faster                                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.50 us: 1.17x faster                                                             |
| comprehensions             | 25.4 us                                                               | 21.8 us: 1.17x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                             |
| generators                 | 43.5 ms                                                               | 37.8 ms: 1.15x faster                                                             |
| pylint                     | 355 ms                                                                | 309 ms: 1.15x faster                                                              |
| xml_etree_parse            | 195 ms                                                                | 175 ms: 1.11x faster                                                              |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 22.3 ms: 1.10x faster                                                             |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                              |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                              |
| deltablue                  | 4.12 ms                                                               | 3.82 ms: 1.08x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 140 ms: 1.07x faster                                                              |
| float                      | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                             |
| logging_simple             | 7.63 us                                                               | 7.17 us: 1.06x faster                                                             |
| logging_format             | 8.34 us                                                               | 7.84 us: 1.06x faster                                                             |
| async_generators           | 491 ms                                                                | 462 ms: 1.06x faster                                                              |
| sympy_integrate            | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                                             |
| sqlalchemy_declarative     | 157 ms                                                                | 149 ms: 1.06x faster                                                              |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.06x faster                                                              |
| chaos                      | 71.4 ms                                                               | 67.8 ms: 1.05x faster                                                             |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                                             |
| regex_dna                  | 254 ms                                                                | 242 ms: 1.05x faster                                                              |
| tomli_loads                | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                            |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                                              |
| html5lib                   | 65.1 ms                                                               | 63.0 ms: 1.03x faster                                                             |
| pyflate                    | 559 ms                                                                | 546 ms: 1.02x faster                                                              |
| regex_v8                   | 28.3 ms                                                               | 27.8 ms: 1.02x faster                                                             |
| docutils                   | 2.98 sec                                                              | 2.94 sec: 1.02x faster                                                            |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.02x faster                                                            |
| richards_super             | 58.5 ms                                                               | 58.1 ms: 1.01x faster                                                             |
| pidigits                   | 233 ms                                                                | 233 ms: 1.00x slower                                                              |
| unpickle_pure_python       | 260 us                                                                | 262 us: 1.01x slower                                                              |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.01x slower                                                              |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.02x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.02x slower                                                            |
| pprint_safe_repr           | 916 ms                                                                | 931 ms: 1.02x slower                                                              |
| hexiom                     | 6.98 ms                                                               | 7.09 ms: 1.02x slower                                                             |
| richards                   | 50.9 ms                                                               | 52.2 ms: 1.02x slower                                                             |
| sqlite_synth               | 3.77 us                                                               | 3.87 us: 1.03x slower                                                             |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                             |
| scimark_fft                | 418 ms                                                                | 437 ms: 1.04x slower                                                              |
| coroutines                 | 29.0 ms                                                               | 30.3 ms: 1.04x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 387 us: 1.06x slower                                                              |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                             |
| json                       | 5.54 ms                                                               | 6.03 ms: 1.09x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.82 ms: 1.10x slower                                                             |
| fannkuch                   | 443 ms                                                                | 494 ms: 1.12x slower                                                              |
| telco                      | 8.51 ms                                                               | 9.55 ms: 1.12x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 205 us: 1.13x slower                                                              |
| json_loads                 | 30.7 us                                                               | 34.8 us: 1.13x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                             |
| nbody                      | 105 ms                                                                | 121 ms: 1.16x slower                                                              |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                              |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                             |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.56 ms: 1.49x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.56 ms: 1.86x slower                                                             |
| bench_mp_pool              | 7.05 ms                                                               | 4.04 sec: 572.46x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                                      |

Benchmark hidden because not significant (13): scimark_monte_carlo, scimark_lu, spectral_norm, scimark_sor, xml_etree_generate, meteor_contest, django_template, xml_etree_process, crypto_pyaes, genshi_xml, nqueens, genshi_text, logging_silent
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x