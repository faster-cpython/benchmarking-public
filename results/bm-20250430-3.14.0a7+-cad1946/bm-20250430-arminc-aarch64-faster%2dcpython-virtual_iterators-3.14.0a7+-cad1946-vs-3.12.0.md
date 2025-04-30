# Results vs. 3.12.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-aarch64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                            |
| docutils       | 2.98 sec                                                              | 2.91 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 459 ms: 1.69x faster                                                            |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 882 ms: 1.60x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 886 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.9 ms: 1.07x faster                                                           |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                            |
| nbody          | 105 ms                                                                | 124 ms: 1.18x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.81 ms: 1.22x faster                                                           |
| regex_compile  | 137 ms                                                                | 120 ms: 1.14x faster                                                            |
| regex_dna      | 254 ms                                                                | 241 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 182 ms: 1.07x faster                                                            |
| tomli_loads         | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                          |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.05x faster                                                            |
| pickle_pure_python  | 365 us                                                                | 382 us: 1.05x slower                                                            |
| json_loads          | 30.7 us                                                               | 35.4 us: 1.15x slower                                                           |
| json_dumps          | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                           |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 61.4 ms: 1.01x slower                                                           |
| mako           | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.64 sec: 2.09x faster                                                          |
| async_tree_memoization     | 777 ms                                                                | 459 ms: 1.69x faster                                                            |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 882 ms: 1.60x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 886 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                            |
| deepcopy                   | 446 us                                                                | 325 us: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                           |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                           |
| go                         | 157 ms                                                                | 128 ms: 1.23x faster                                                            |
| regex_effbot               | 4.64 ms                                                               | 3.81 ms: 1.22x faster                                                           |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.54 us: 1.16x faster                                                           |
| regex_compile              | 137 ms                                                                | 120 ms: 1.14x faster                                                            |
| dulwich_log                | 62.0 ms                                                               | 54.9 ms: 1.13x faster                                                           |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.12x faster                                                           |
| logging_simple             | 7.63 us                                                               | 6.92 us: 1.10x faster                                                           |
| logging_format             | 8.34 us                                                               | 7.62 us: 1.10x faster                                                           |
| async_generators           | 491 ms                                                                | 450 ms: 1.09x faster                                                            |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                            |
| float                      | 92.1 ms                                                               | 85.9 ms: 1.07x faster                                                           |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                            |
| tomli_loads                | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                          |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.0 ms: 1.06x faster                                                           |
| regex_dna                  | 254 ms                                                                | 241 ms: 1.05x faster                                                            |
| deltablue                  | 4.12 ms                                                               | 3.92 ms: 1.05x faster                                                           |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                            |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                            |
| docutils                   | 2.98 sec                                                              | 2.91 sec: 1.02x faster                                                          |
| pprint_pformat             | 1.88 sec                                                              | 1.84 sec: 1.02x faster                                                          |
| crypto_pyaes               | 86.6 ms                                                               | 85.0 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 916 ms                                                                | 899 ms: 1.02x faster                                                            |
| pyflate                    | 559 ms                                                                | 549 ms: 1.02x faster                                                            |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.02x faster                                                          |
| hexiom                     | 6.98 ms                                                               | 6.87 ms: 1.02x faster                                                           |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                            |
| genshi_xml                 | 60.6 ms                                                               | 61.4 ms: 1.01x slower                                                           |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                            |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                            |
| python_startup_no_site     | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                           |
| coroutines                 | 29.0 ms                                                               | 30.2 ms: 1.04x slower                                                           |
| sqlite_synth               | 3.77 us                                                               | 3.94 us: 1.05x slower                                                           |
| pickle_pure_python         | 365 us                                                                | 382 us: 1.05x slower                                                            |
| bench_thread_pool          | 1.31 ms                                                               | 1.39 ms: 1.06x slower                                                           |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                            |
| json                       | 5.54 ms                                                               | 6.00 ms: 1.08x slower                                                           |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                            |
| fannkuch                   | 443 ms                                                                | 488 ms: 1.10x slower                                                            |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.99 ms: 1.13x slower                                                           |
| telco                      | 8.51 ms                                                               | 9.73 ms: 1.14x slower                                                           |
| json_loads                 | 30.7 us                                                               | 35.4 us: 1.15x slower                                                           |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                           |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                            |
| nbody                      | 105 ms                                                                | 124 ms: 1.18x slower                                                            |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                           |
| gc_traversal               | 4.40 ms                                                               | 6.53 ms: 1.49x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.59 ms: 1.87x slower                                                           |
| bench_mp_pool              | 7.05 ms                                                               | 1.87 sec: 264.40x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (17): sqlalchemy_declarative, chaos, html5lib, sqlalchemy_imperative, scimark_sor, django_template, spectral_norm, xml_etree_generate, nqueens, regex_v8, richards_super, scimark_lu, xml_etree_process, meteor_contest, genshi_text, richards, unpickle_pure_python
Ignored benchmarks (23) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x