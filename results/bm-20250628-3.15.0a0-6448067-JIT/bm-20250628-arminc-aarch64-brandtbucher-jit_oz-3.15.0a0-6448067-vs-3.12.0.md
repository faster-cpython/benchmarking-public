# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_oz
- machine: linux-aarch64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.036x faster
- HPT reliability: 88.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 315 ms: 1.02x slower                                            |
| docutils       | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                          |
| html5lib       | 65.1 ms                                                               | 63.1 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 468 ms: 1.58x faster                                            |
| async_tree_none            | 624 ms                                                                | 396 ms: 1.57x faster                                            |
| async_tree_io              | 1.41 sec                                                              | 905 ms: 1.56x faster                                            |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 664 ms: 1.37x faster                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 664 ms: 1.33x faster                                            |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.4 ms: 1.09x faster                                           |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                            |
| nbody          | 105 ms                                                                | 125 ms: 1.20x slower                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                           |
| regex_dna      | 254 ms                                                                | 220 ms: 1.15x faster                                            |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                            |
| regex_v8       | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                            |
| tomli_loads          | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                          |
| xml_etree_iterparse  | 150 ms                                                                | 144 ms: 1.04x faster                                            |
| unpickle_pure_python | 260 us                                                                | 267 us: 1.03x slower                                            |
| json_loads           | 30.7 us                                                               | 33.3 us: 1.09x slower                                           |
| pickle_pure_python   | 365 us                                                                | 405 us: 1.11x slower                                            |
| json_dumps           | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                    |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                           |
| python_startup         | 11.4 ms                                                               | 15.3 ms: 1.34x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 62.0 ms: 1.02x slower                                           |
| mako           | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                    |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.70 sec: 2.00x faster                                          |
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 468 ms: 1.58x faster                                            |
| async_tree_none            | 624 ms                                                                | 396 ms: 1.57x faster                                            |
| async_tree_io              | 1.41 sec                                                              | 905 ms: 1.56x faster                                            |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 664 ms: 1.37x faster                                            |
| deepcopy_memo              | 49.6 us                                                               | 37.2 us: 1.33x faster                                           |
| deepcopy                   | 446 us                                                                | 335 us: 1.33x faster                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 664 ms: 1.33x faster                                            |
| generators                 | 43.5 ms                                                               | 36.2 ms: 1.20x faster                                           |
| regex_effbot               | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                           |
| regex_dna                  | 254 ms                                                                | 220 ms: 1.15x faster                                            |
| richards                   | 50.9 ms                                                               | 44.6 ms: 1.14x faster                                           |
| richards_super             | 58.5 ms                                                               | 51.9 ms: 1.13x faster                                           |
| comprehensions             | 25.4 us                                                               | 22.5 us: 1.13x faster                                           |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                            |
| dulwich_log                | 62.0 ms                                                               | 56.2 ms: 1.10x faster                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.75 us: 1.09x faster                                           |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                            |
| float                      | 92.1 ms                                                               | 84.4 ms: 1.09x faster                                           |
| logging_simple             | 7.63 us                                                               | 7.00 us: 1.09x faster                                           |
| pylint                     | 355 ms                                                                | 330 ms: 1.08x faster                                            |
| tomli_loads                | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                          |
| logging_format             | 8.34 us                                                               | 7.83 us: 1.07x faster                                           |
| scimark_sor                | 150 ms                                                                | 142 ms: 1.05x faster                                            |
| regex_v8                   | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                           |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                            |
| deltablue                  | 4.12 ms                                                               | 3.94 ms: 1.05x faster                                           |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                            |
| raytrace                   | 353 ms                                                                | 338 ms: 1.04x faster                                            |
| pathlib                    | 24.5 ms                                                               | 23.6 ms: 1.04x faster                                           |
| html5lib                   | 65.1 ms                                                               | 63.1 ms: 1.03x faster                                           |
| async_generators           | 491 ms                                                                | 481 ms: 1.02x faster                                            |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.4 ms: 1.02x faster                                           |
| coroutines                 | 29.0 ms                                                               | 29.1 ms: 1.00x slower                                           |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                            |
| pyflate                    | 559 ms                                                                | 569 ms: 1.02x slower                                            |
| genshi_xml                 | 60.6 ms                                                               | 62.0 ms: 1.02x slower                                           |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                            |
| 2to3                       | 308 ms                                                                | 315 ms: 1.02x slower                                            |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.03x slower                                            |
| unpickle_pure_python       | 260 us                                                                | 267 us: 1.03x slower                                            |
| go                         | 157 ms                                                                | 162 ms: 1.03x slower                                            |
| python_startup_no_site     | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                           |
| sqlite_synth               | 3.77 us                                                               | 3.95 us: 1.05x slower                                           |
| json                       | 5.54 ms                                                               | 5.83 ms: 1.05x slower                                           |
| nqueens                    | 99.2 ms                                                               | 104 ms: 1.05x slower                                            |
| docutils                   | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                          |
| scimark_fft                | 418 ms                                                                | 448 ms: 1.07x slower                                            |
| meteor_contest             | 112 ms                                                                | 120 ms: 1.07x slower                                            |
| json_loads                 | 30.7 us                                                               | 33.3 us: 1.09x slower                                           |
| sympy_expand               | 454 ms                                                                | 495 ms: 1.09x slower                                            |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                           |
| pickle_pure_python         | 365 us                                                                | 405 us: 1.11x slower                                            |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                           |
| hexiom                     | 6.98 ms                                                               | 7.77 ms: 1.11x slower                                           |
| pycparser                  | 1.26 sec                                                              | 1.40 sec: 1.12x slower                                          |
| crypto_pyaes               | 86.6 ms                                                               | 97.7 ms: 1.13x slower                                           |
| telco                      | 8.51 ms                                                               | 9.64 ms: 1.13x slower                                           |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                            |
| typing_runtime_protocols   | 181 us                                                                | 211 us: 1.17x slower                                            |
| fannkuch                   | 443 ms                                                                | 527 ms: 1.19x slower                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.37 ms: 1.19x slower                                           |
| nbody                      | 105 ms                                                                | 125 ms: 1.20x slower                                            |
| pprint_safe_repr           | 916 ms                                                                | 1.23 sec: 1.34x slower                                          |
| python_startup             | 11.4 ms                                                               | 15.3 ms: 1.34x slower                                           |
| pprint_pformat             | 1.88 sec                                                              | 2.54 sec: 1.35x slower                                          |
| gc_traversal               | 4.40 ms                                                               | 6.84 ms: 1.56x slower                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.78 ms: 1.97x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                    |

Benchmark hidden because not significant (10): chaos, django_template, sympy_str, xml_etree_generate, sympy_integrate, genshi_text, logging_silent, spectral_norm, xml_etree_process, thrift
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 88.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x