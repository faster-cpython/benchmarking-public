# Results vs. 3.12.0

- fork: python
- ref: 44e4c479fbf2c28605bd
- machine: linux-aarch64
- commit hash: 44e4c47
- commit date: 2025-04-30
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 298 ms: 1.03x faster                                                     |
| html5lib       | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 466 ms: 1.67x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 878 ms: 1.60x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                     |
| async_tree_none            | 624 ms                                                                | 393 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 676 ms: 1.35x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.9 ms: 1.07x faster                                                    |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| nbody          | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                    |
| regex_compile  | 137 ms                                                                | 124 ms: 1.10x faster                                                     |
| regex_dna      | 254 ms                                                                | 236 ms: 1.08x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 27.4 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 176 ms: 1.11x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.06x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                   |
| pickle_pure_python  | 365 us                                                                | 383 us: 1.05x slower                                                     |
| json_loads          | 30.7 us                                                               | 35.5 us: 1.16x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                                    |
| genshi_text     | 27.4 ms                                                               | 26.5 ms: 1.03x faster                                                    |
| mako            | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 466 ms: 1.67x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 878 ms: 1.60x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                     |
| async_tree_none            | 624 ms                                                                | 393 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                     |
| deepcopy                   | 446 us                                                                | 326 us: 1.37x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 676 ms: 1.35x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 38.1 us: 1.30x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.8 us: 1.22x faster                                                    |
| go                         | 157 ms                                                                | 129 ms: 1.21x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.7 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.53 us: 1.16x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 176 ms: 1.11x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 56.0 ms: 1.11x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                    |
| regex_compile              | 137 ms                                                                | 124 ms: 1.10x faster                                                     |
| pylint                     | 355 ms                                                                | 323 ms: 1.10x faster                                                     |
| raytrace                   | 353 ms                                                                | 322 ms: 1.10x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.97 us: 1.09x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.77 ms: 1.09x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                     |
| async_generators           | 491 ms                                                                | 454 ms: 1.08x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.72 us: 1.08x faster                                                    |
| regex_dna                  | 254 ms                                                                | 236 ms: 1.08x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 20.1 ms: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 85.9 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.06x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.06x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.4 ms: 1.06x faster                                                    |
| chaos                      | 71.4 ms                                                               | 67.5 ms: 1.06x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.0 ms: 1.04x faster                                                    |
| sympy_str                  | 280 ms                                                                | 270 ms: 1.04x faster                                                     |
| regex_v8                   | 28.3 ms                                                               | 27.4 ms: 1.03x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.5 ms: 1.03x faster                                                    |
| 2to3                       | 308 ms                                                                | 298 ms: 1.03x faster                                                     |
| richards_super             | 58.5 ms                                                               | 57.1 ms: 1.02x faster                                                    |
| pyflate                    | 559 ms                                                                | 548 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.85 sec: 1.02x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 85.7 ms: 1.01x faster                                                    |
| richards                   | 50.9 ms                                                               | 50.8 ms: 1.00x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.02x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 29.6 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 383 us: 1.05x slower                                                     |
| scimark_fft                | 418 ms                                                                | 442 ms: 1.06x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| fannkuch                   | 443 ms                                                                | 483 ms: 1.09x slower                                                     |
| json                       | 5.54 ms                                                               | 6.10 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 199 us: 1.10x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.51 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.02 ms: 1.13x slower                                                    |
| json_loads                 | 30.7 us                                                               | 35.5 us: 1.16x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                                    |
| nbody                      | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| coverage                   | 87.3 ms                                                               | 111 ms: 1.28x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.66 ms: 1.52x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.71 ms: 1.93x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.81 sec: 398.83x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (15): scimark_sor, scimark_lu, pprint_safe_repr, nqueens, pycparser, hexiom, docutils, meteor_contest, xml_etree_generate, xml_etree_process, spectral_norm, sympy_expand, unpickle_pure_python, genshi_xml, logging_silent
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x