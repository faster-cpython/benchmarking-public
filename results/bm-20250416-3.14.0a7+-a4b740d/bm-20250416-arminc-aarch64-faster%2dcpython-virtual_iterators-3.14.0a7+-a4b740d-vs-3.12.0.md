# Results vs. 3.12.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-aarch64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.077x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 290 ms: 1.06x faster                                                            |
| docutils       | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                                          |
| html5lib       | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                            |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 886 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.0 ms: 1.11x faster                                                           |
| nbody          | 105 ms                                                                | 119 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                           |
| regex_compile  | 137 ms                                                                | 121 ms: 1.14x faster                                                            |
| regex_dna      | 254 ms                                                                | 241 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                            |
| tomli_loads         | 2.59 sec                                                              | 2.41 sec: 1.08x faster                                                          |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                            |
| pickle_pure_python  | 365 us                                                                | 374 us: 1.02x slower                                                            |
| json_loads          | 30.7 us                                                               | 34.8 us: 1.14x slower                                                           |
| json_dumps          | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                           |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 26.3 ms: 1.04x faster                                                           |
| django_template | 40.7 ms                                                               | 39.5 ms: 1.03x faster                                                           |
| genshi_xml      | 60.6 ms                                                               | 59.2 ms: 1.02x faster                                                           |
| mako            | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.60 sec: 2.13x faster                                                          |
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                            |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 886 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                            |
| deepcopy                   | 446 us                                                                | 326 us: 1.37x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 36.6 us: 1.36x faster                                                           |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.25x faster                                                           |
| regex_effbot               | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                           |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                            |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                           |
| dulwich_log                | 62.0 ms                                                               | 52.7 ms: 1.18x faster                                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.58 us: 1.14x faster                                                           |
| regex_compile              | 137 ms                                                                | 121 ms: 1.14x faster                                                            |
| raytrace                   | 353 ms                                                                | 315 ms: 1.12x faster                                                            |
| logging_simple             | 7.63 us                                                               | 6.82 us: 1.12x faster                                                           |
| float                      | 92.1 ms                                                               | 83.0 ms: 1.11x faster                                                           |
| logging_format             | 8.34 us                                                               | 7.53 us: 1.11x faster                                                           |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                           |
| scimark_monte_carlo        | 85.1 ms                                                               | 77.6 ms: 1.10x faster                                                           |
| async_generators           | 491 ms                                                                | 450 ms: 1.09x faster                                                            |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                            |
| chaos                      | 71.4 ms                                                               | 66.3 ms: 1.08x faster                                                           |
| tomli_loads                | 2.59 sec                                                              | 2.41 sec: 1.08x faster                                                          |
| deltablue                  | 4.12 ms                                                               | 3.84 ms: 1.07x faster                                                           |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.6 ms: 1.07x faster                                                           |
| 2to3                       | 308 ms                                                                | 290 ms: 1.06x faster                                                            |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                            |
| sqlalchemy_declarative     | 157 ms                                                                | 149 ms: 1.06x faster                                                            |
| regex_dna                  | 254 ms                                                                | 241 ms: 1.06x faster                                                            |
| html5lib                   | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                                           |
| crypto_pyaes               | 86.6 ms                                                               | 83.0 ms: 1.04x faster                                                           |
| pyflate                    | 559 ms                                                                | 536 ms: 1.04x faster                                                            |
| genshi_text                | 27.4 ms                                                               | 26.3 ms: 1.04x faster                                                           |
| pprint_pformat             | 1.88 sec                                                              | 1.82 sec: 1.04x faster                                                          |
| docutils                   | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                                          |
| pprint_safe_repr           | 916 ms                                                                | 888 ms: 1.03x faster                                                            |
| django_template            | 40.7 ms                                                               | 39.5 ms: 1.03x faster                                                           |
| meteor_contest             | 112 ms                                                                | 109 ms: 1.03x faster                                                            |
| genshi_xml                 | 60.6 ms                                                               | 59.2 ms: 1.02x faster                                                           |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.02x faster                                                          |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                            |
| pickle_pure_python         | 365 us                                                                | 374 us: 1.02x slower                                                            |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 181 us                                                                | 186 us: 1.03x slower                                                            |
| fannkuch                   | 443 ms                                                                | 471 ms: 1.06x slower                                                            |
| json                       | 5.54 ms                                                               | 5.89 ms: 1.06x slower                                                           |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.79 ms: 1.10x slower                                                           |
| telco                      | 8.51 ms                                                               | 9.44 ms: 1.11x slower                                                           |
| nbody                      | 105 ms                                                                | 119 ms: 1.13x slower                                                            |
| json_loads                 | 30.7 us                                                               | 34.8 us: 1.14x slower                                                           |
| json_dumps                 | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                           |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                            |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                           |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                           |
| gc_traversal               | 4.40 ms                                                               | 6.54 ms: 1.49x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.59 ms: 1.87x slower                                                           |
| bench_mp_pool              | 7.05 ms                                                               | 6.60 sec: 935.46x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (16): spectral_norm, scimark_sor, nqueens, scimark_fft, regex_v8, hexiom, sqlite_synth, logging_silent, xml_etree_process, richards_super, scimark_lu, unpickle_pure_python, xml_etree_generate, pidigits, richards, coroutines
Ignored benchmarks (23) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x