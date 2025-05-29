# Results vs. 3.12.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-aarch64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.078x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 285 ms: 1.08x faster                                                        |
| docutils       | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                      |
| html5lib       | 65.1 ms                                                               | 60.0 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 872 ms: 1.62x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 875 ms: 1.61x faster                                                        |
| async_tree_none            | 624 ms                                                                | 391 ms: 1.60x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 724 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.1 ms: 1.12x faster                                                       |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                        |
| pidigits       | 233 ms                                                                | 291 ms: 1.25x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 123 ms: 1.12x faster                                                        |
| regex_effbot   | 4.64 ms                                                               | 4.16 ms: 1.12x faster                                                       |
| regex_dna      | 254 ms                                                                | 238 ms: 1.07x faster                                                        |
| regex_v8       | 28.3 ms                                                               | 29.8 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                                      |
| pickle_pure_python | 365 us                                                                | 378 us: 1.04x slower                                                        |
| xml_etree_parse    | 195 ms                                                                | 207 ms: 1.06x slower                                                        |
| json_loads         | 30.7 us                                                               | 33.1 us: 1.08x slower                                                       |
| json_dumps         | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                       |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                       |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                       |
| mako            | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.60 sec: 2.13x faster                                                      |
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 872 ms: 1.62x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 875 ms: 1.61x faster                                                        |
| async_tree_none            | 624 ms                                                                | 391 ms: 1.60x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                        |
| deepcopy                   | 446 us                                                                | 312 us: 1.43x faster                                                        |
| deepcopy_memo              | 49.6 us                                                               | 36.6 us: 1.36x faster                                                       |
| comprehensions             | 25.4 us                                                               | 19.7 us: 1.29x faster                                                       |
| generators                 | 43.5 ms                                                               | 34.3 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 724 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                        |
| async_generators           | 491 ms                                                                | 408 ms: 1.20x faster                                                        |
| go                         | 157 ms                                                                | 132 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 4.10 us                                                               | 3.45 us: 1.19x faster                                                       |
| dulwich_log                | 62.0 ms                                                               | 52.3 ms: 1.19x faster                                                       |
| pylint                     | 355 ms                                                                | 301 ms: 1.18x faster                                                        |
| pathlib                    | 24.5 ms                                                               | 21.0 ms: 1.17x faster                                                       |
| raytrace                   | 353 ms                                                                | 312 ms: 1.13x faster                                                        |
| float                      | 92.1 ms                                                               | 82.1 ms: 1.12x faster                                                       |
| regex_compile              | 137 ms                                                                | 123 ms: 1.12x faster                                                        |
| deltablue                  | 4.12 ms                                                               | 3.69 ms: 1.12x faster                                                       |
| regex_effbot               | 4.64 ms                                                               | 4.16 ms: 1.12x faster                                                       |
| spectral_norm              | 131 ms                                                                | 117 ms: 1.12x faster                                                        |
| tomli_loads                | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                                      |
| sympy_integrate            | 21.6 ms                                                               | 19.5 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 85.1 ms                                                               | 76.9 ms: 1.11x faster                                                       |
| logging_simple             | 7.63 us                                                               | 6.90 us: 1.11x faster                                                       |
| scimark_sor                | 150 ms                                                                | 135 ms: 1.10x faster                                                        |
| sqlalchemy_declarative     | 157 ms                                                                | 143 ms: 1.10x faster                                                        |
| logging_format             | 8.34 us                                                               | 7.57 us: 1.10x faster                                                       |
| chaos                      | 71.4 ms                                                               | 65.4 ms: 1.09x faster                                                       |
| sympy_str                  | 280 ms                                                                | 257 ms: 1.09x faster                                                        |
| scimark_fft                | 418 ms                                                                | 385 ms: 1.09x faster                                                        |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                        |
| pyflate                    | 559 ms                                                                | 515 ms: 1.08x faster                                                        |
| html5lib                   | 65.1 ms                                                               | 60.0 ms: 1.08x faster                                                       |
| 2to3                       | 308 ms                                                                | 285 ms: 1.08x faster                                                        |
| logging_silent             | 127 ns                                                                | 118 ns: 1.08x faster                                                        |
| regex_dna                  | 254 ms                                                                | 238 ms: 1.07x faster                                                        |
| django_template            | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                       |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                                       |
| crypto_pyaes               | 86.6 ms                                                               | 83.1 ms: 1.04x faster                                                       |
| docutils                   | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                      |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.01x faster                                                      |
| meteor_contest             | 112 ms                                                                | 111 ms: 1.01x faster                                                        |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                        |
| sqlite_synth               | 3.77 us                                                               | 3.84 us: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.36 ms: 1.03x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 378 us: 1.04x slower                                                        |
| typing_runtime_protocols   | 181 us                                                                | 189 us: 1.05x slower                                                        |
| regex_v8                   | 28.3 ms                                                               | 29.8 ms: 1.05x slower                                                       |
| json                       | 5.54 ms                                                               | 5.86 ms: 1.06x slower                                                       |
| xml_etree_parse            | 195 ms                                                                | 207 ms: 1.06x slower                                                        |
| telco                      | 8.51 ms                                                               | 9.12 ms: 1.07x slower                                                       |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                       |
| coverage                   | 87.3 ms                                                               | 94.6 ms: 1.08x slower                                                       |
| fannkuch                   | 443 ms                                                                | 484 ms: 1.09x slower                                                        |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                       |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                       |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                        |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                       |
| pidigits                   | 233 ms                                                                | 291 ms: 1.25x slower                                                        |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                       |
| gc_traversal               | 4.40 ms                                                               | 6.53 ms: 1.49x slower                                                       |
| create_gc_cycles           | 1.92 ms                                                               | 3.66 ms: 1.91x slower                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 2.97 sec: 420.89x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (16): genshi_text, genshi_xml, xml_etree_generate, xml_etree_process, unpickle_pure_python, scimark_lu, bench_thread_pool, richards_super, xml_etree_iterparse, richards, pprint_pformat, sympy_expand, pprint_safe_repr, nqueens, coroutines, hexiom
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x