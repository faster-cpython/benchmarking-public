# Results vs. 3.12.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-aarch64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.057x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 298 ms: 1.03x faster                                                              |
| docutils       | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 460 ms: 1.69x faster                                                              |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 877 ms: 1.61x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 892 ms: 1.57x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.54x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.8 ms: 1.07x faster                                                             |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.00 ms: 1.16x faster                                                             |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| regex_dna      | 254 ms                                                                | 242 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 180 ms: 1.08x faster                                                              |
| xml_etree_iterparse  | 150 ms                                                                | 142 ms: 1.06x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.50 sec: 1.04x faster                                                            |
| xml_etree_process    | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                                             |
| unpickle_pure_python | 260 us                                                                | 268 us: 1.03x slower                                                              |
| pickle_pure_python   | 365 us                                                                | 384 us: 1.05x slower                                                              |
| json_loads           | 30.7 us                                                               | 34.9 us: 1.14x slower                                                             |
| json_dumps           | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                             |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 60.9 ms: 1.01x slower                                                             |
| mako           | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 460 ms: 1.69x faster                                                              |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 877 ms: 1.61x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 892 ms: 1.57x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.54x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                                              |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 37.5 us: 1.32x faster                                                             |
| go                         | 157 ms                                                                | 132 ms: 1.19x faster                                                              |
| generators                 | 43.5 ms                                                               | 36.7 ms: 1.19x faster                                                             |
| comprehensions             | 25.4 us                                                               | 21.6 us: 1.17x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 52.9 ms: 1.17x faster                                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.52 us: 1.17x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 4.00 ms: 1.16x faster                                                             |
| pylint                     | 355 ms                                                                | 315 ms: 1.13x faster                                                              |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                             |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                              |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                              |
| sympy_integrate            | 21.6 ms                                                               | 20.0 ms: 1.08x faster                                                             |
| deltablue                  | 4.12 ms                                                               | 3.83 ms: 1.08x faster                                                             |
| float                      | 92.1 ms                                                               | 85.8 ms: 1.07x faster                                                             |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.06x faster                                                              |
| async_generators           | 491 ms                                                                | 462 ms: 1.06x faster                                                              |
| chaos                      | 71.4 ms                                                               | 67.3 ms: 1.06x faster                                                             |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                              |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                              |
| sqlalchemy_declarative     | 157 ms                                                                | 149 ms: 1.06x faster                                                              |
| logging_simple             | 7.63 us                                                               | 7.28 us: 1.05x faster                                                             |
| regex_dna                  | 254 ms                                                                | 242 ms: 1.05x faster                                                              |
| logging_format             | 8.34 us                                                               | 7.96 us: 1.05x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.50 sec: 1.04x faster                                                            |
| 2to3                       | 308 ms                                                                | 298 ms: 1.03x faster                                                              |
| pyflate                    | 559 ms                                                                | 543 ms: 1.03x faster                                                              |
| spectral_norm              | 131 ms                                                                | 127 ms: 1.03x faster                                                              |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.01x faster                                                            |
| docutils                   | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                            |
| genshi_xml                 | 60.6 ms                                                               | 60.9 ms: 1.01x slower                                                             |
| richards                   | 50.9 ms                                                               | 51.2 ms: 1.01x slower                                                             |
| hexiom                     | 6.98 ms                                                               | 7.02 ms: 1.01x slower                                                             |
| xml_etree_process          | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                                             |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                                            |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                              |
| sqlite_synth               | 3.77 us                                                               | 3.84 us: 1.02x slower                                                             |
| pprint_safe_repr           | 916 ms                                                                | 936 ms: 1.02x slower                                                              |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.03x slower                                                             |
| unpickle_pure_python       | 260 us                                                                | 268 us: 1.03x slower                                                              |
| sympy_expand               | 454 ms                                                                | 470 ms: 1.04x slower                                                              |
| coroutines                 | 29.0 ms                                                               | 30.2 ms: 1.04x slower                                                             |
| scimark_fft                | 418 ms                                                                | 435 ms: 1.04x slower                                                              |
| pickle_pure_python         | 365 us                                                                | 384 us: 1.05x slower                                                              |
| fannkuch                   | 443 ms                                                                | 487 ms: 1.10x slower                                                              |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                             |
| json                       | 5.54 ms                                                               | 6.09 ms: 1.10x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.85 ms: 1.11x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.48 ms: 1.11x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 203 us: 1.12x slower                                                              |
| json_loads                 | 30.7 us                                                               | 34.9 us: 1.14x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                             |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                              |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                              |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                             |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.62 ms: 1.51x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.54 ms: 1.85x slower                                                             |
| bench_mp_pool              | 7.05 ms                                                               | 2.04 sec: 288.97x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (15): scimark_monte_carlo, scimark_sor, scimark_lu, sqlalchemy_imperative, regex_v8, nqueens, html5lib, meteor_contest, crypto_pyaes, richards_super, genshi_text, logging_silent, django_template, xml_etree_generate, pidigits
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250409-3.14.0a7+-3514aa1/bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x