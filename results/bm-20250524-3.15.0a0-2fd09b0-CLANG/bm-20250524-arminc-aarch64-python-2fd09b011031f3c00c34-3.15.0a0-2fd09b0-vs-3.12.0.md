# Results vs. 3.12.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: linux-aarch64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.029x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| html5lib       | 65.1 ms                                                               | 62.1 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 450 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 867 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.61x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 364 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 893 ms: 1.57x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 713 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.6 ms: 1.05x faster                                                   |
| nbody          | 105 ms                                                                | 129 ms: 1.23x slower                                                    |
| pidigits       | 233 ms                                                                | 293 ms: 1.26x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 120 ms: 1.14x faster                                                    |
| regex_dna      | 254 ms                                                                | 240 ms: 1.06x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.37 sec: 1.10x faster                                                  |
| xml_etree_generate   | 112 ms                                                                | 107 ms: 1.05x faster                                                    |
| unpickle             | 18.5 us                                                               | 17.6 us: 1.05x faster                                                   |
| unpickle_list        | 6.17 us                                                               | 5.90 us: 1.05x faster                                                   |
| unpickle_pure_python | 260 us                                                                | 249 us: 1.04x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 76.1 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 382 us: 1.05x slower                                                    |
| xml_etree_parse      | 195 ms                                                                | 209 ms: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| json_loads           | 30.7 us                                                               | 34.4 us: 1.12x slower                                                   |
| pickle               | 13.4 us                                                               | 15.4 us: 1.14x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.82 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.1 ms: 1.04x faster                                                   |
| genshi_text     | 27.4 ms                                                               | 26.9 ms: 1.02x faster                                                   |
| mako            | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.67 sec: 2.05x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 450 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 867 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.61x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 364 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 893 ms: 1.57x faster                                                    |
| deepcopy                   | 446 us                                                                | 318 us: 1.40x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 35.8 us: 1.39x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 713 ms: 1.24x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.37 us: 1.21x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.8 ms: 1.21x faster                                                   |
| go                         | 157 ms                                                                | 132 ms: 1.19x faster                                                    |
| async_generators           | 491 ms                                                                | 417 ms: 1.18x faster                                                    |
| regex_compile              | 137 ms                                                                | 120 ms: 1.14x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 54.3 ms: 1.14x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.13x faster                                                   |
| raytrace                   | 353 ms                                                                | 317 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 76.6 ms: 1.11x faster                                                   |
| pylint                     | 355 ms                                                                | 324 ms: 1.10x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.37 sec: 1.10x faster                                                  |
| spectral_norm              | 131 ms                                                                | 120 ms: 1.09x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.09x faster                                                    |
| pyflate                    | 559 ms                                                                | 515 ms: 1.09x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.0 ms: 1.08x faster                                                   |
| sympy_str                  | 280 ms                                                                | 259 ms: 1.08x faster                                                    |
| richards_super             | 58.5 ms                                                               | 54.7 ms: 1.07x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.3 ms: 1.06x faster                                                   |
| regex_dna                  | 254 ms                                                                | 240 ms: 1.06x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.90 ms: 1.06x faster                                                   |
| float                      | 92.1 ms                                                               | 87.6 ms: 1.05x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 107 ms: 1.05x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.1 ms: 1.05x faster                                                   |
| unpickle                   | 18.5 us                                                               | 17.6 us: 1.05x faster                                                   |
| unpickle_list              | 6.17 us                                                               | 5.90 us: 1.05x faster                                                   |
| richards                   | 50.9 ms                                                               | 48.8 ms: 1.04x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 543 ms: 1.04x faster                                                    |
| scimark_fft                | 418 ms                                                                | 402 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 249 us: 1.04x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.1 ms: 1.04x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 76.1 ms: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 84.6 ms: 1.02x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.18 us: 1.02x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 26.9 ms: 1.02x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.50 us: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.17 sec: 1.01x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 674 ms: 1.02x slower                                                    |
| sympy_expand               | 454 ms                                                                | 465 ms: 1.02x slower                                                    |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.90 us: 1.03x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 382 us: 1.05x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.82 ms: 1.05x slower                                                   |
| json                       | 5.54 ms                                                               | 5.86 ms: 1.06x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.9 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 209 ms: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.66 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| fannkuch                   | 443 ms                                                                | 480 ms: 1.08x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.46 ms: 1.11x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.10 sec: 1.11x slower                                                  |
| json_loads                 | 30.7 us                                                               | 34.4 us: 1.12x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.03 sec: 1.12x slower                                                  |
| pickle                     | 13.4 us                                                               | 15.4 us: 1.14x slower                                                   |
| nbody                      | 105 ms                                                                | 129 ms: 1.23x slower                                                    |
| pidigits                   | 233 ms                                                                | 293 ms: 1.26x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.81 ms: 1.55x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.82 ms: 1.99x slower                                                   |
| logging_silent             | 127 ns                                                                | 596 ns: 4.70x slower                                                    |
| coverage                   | 87.3 ms                                                               | 526 ms: 6.03x slower                                                    |
| thrift                     | 937 us                                                                | 194 ms: 207.03x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 3.87 sec: 548.69x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (10): scimark_sor, regex_effbot, pickle_dict, pycparser, genshi_xml, hexiom, docutils, bench_thread_pool, pickle_list, nqueens
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.029x slower

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.13x