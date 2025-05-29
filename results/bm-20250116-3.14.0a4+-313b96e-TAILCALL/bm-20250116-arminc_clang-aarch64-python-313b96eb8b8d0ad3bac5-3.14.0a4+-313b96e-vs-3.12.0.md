# Results vs. 3.12.0

- fork: python
- ref: 313b96eb8b8d0ad3bac5
- machine: linux-aarch64
- commit hash: 313b96e
- commit date: 2025-01-16
- overall geometric mean: 1.023x slower
- HPT reliability: 96.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 325 ms: 1.06x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 409 ms: 1.52x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 486 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 927 ms: 1.52x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 931 ms: 1.52x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 513 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 396 ms: 1.46x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 767 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 765 ms: 1.16x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.42x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 293 ms: 1.26x slower                                                     |
| nbody          | 105 ms                                                                | 135 ms: 1.29x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.31 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 243 ms: 1.05x faster                                                     |
| regex_compile  | 137 ms                                                                | 142 ms: 1.04x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 33.9 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                | 118 ms: 1.05x slower                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 160 ms: 1.07x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 84.3 ms: 1.07x slower                                                    |
| xml_etree_parse      | 195 ms                                                                | 212 ms: 1.09x slower                                                     |
| json_loads           | 30.7 us                                                               | 33.7 us: 1.10x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.90 sec: 1.12x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 312 us: 1.20x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 449 us: 1.23x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 15.8 ms: 1.29x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.13x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.22 ms: 1.10x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.7 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.27x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 45.3 ms: 1.11x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 31.0 ms: 1.13x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 70.0 ms: 1.16x slower                                                    |
| mako            | 12.9 ms                                                               | 15.5 ms: 1.20x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.15x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 409 ms: 1.52x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 486 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 927 ms: 1.52x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 931 ms: 1.52x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 513 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 396 ms: 1.46x faster                                                     |
| deepcopy                   | 446 us                                                                | 369 us: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 767 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 765 ms: 1.16x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                    |
| comprehensions             | 25.4 us                                                               | 23.0 us: 1.10x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 45.5 us: 1.09x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.31 ms: 1.08x faster                                                    |
| pylint                     | 355 ms                                                                | 331 ms: 1.07x faster                                                     |
| async_generators           | 491 ms                                                                | 462 ms: 1.06x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.86 us: 1.06x faster                                                    |
| scimark_fft                | 418 ms                                                                | 398 ms: 1.05x faster                                                     |
| regex_dna                  | 254 ms                                                                | 243 ms: 1.05x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.26 sec: 1.05x faster                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 152 ms: 1.04x faster                                                     |
| logging_format             | 8.34 us                                                               | 8.25 us: 1.01x faster                                                    |
| generators                 | 43.5 ms                                                               | 43.1 ms: 1.01x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 676 ms: 1.03x slower                                                     |
| regex_compile              | 137 ms                                                                | 142 ms: 1.04x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| go                         | 157 ms                                                                | 165 ms: 1.05x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 118 ms: 1.05x slower                                                     |
| sympy_str                  | 280 ms                                                                | 294 ms: 1.05x slower                                                     |
| 2to3                       | 308 ms                                                                | 325 ms: 1.06x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 154 ms: 1.06x slower                                                     |
| coroutines                 | 29.0 ms                                                               | 30.7 ms: 1.06x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 91.7 ms: 1.06x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 160 ms: 1.07x slower                                                     |
| pyflate                    | 559 ms                                                                | 596 ms: 1.07x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 84.3 ms: 1.07x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 91.0 ms: 1.07x slower                                                    |
| json                       | 5.54 ms                                                               | 5.93 ms: 1.07x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.08x slower                                                   |
| thrift                     | 937 us                                                                | 1.01 ms: 1.08x slower                                                    |
| chaos                      | 71.4 ms                                                               | 77.4 ms: 1.08x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 212 ms: 1.09x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.7 us: 1.10x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.61 ms: 1.10x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.53 ms: 1.10x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.22 ms: 1.10x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 109 ms: 1.10x slower                                                     |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.18 us: 1.11x slower                                                    |
| django_template            | 40.7 ms                                                               | 45.3 ms: 1.11x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.90 sec: 1.12x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 31.0 ms: 1.13x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 69.6 ms: 1.13x slower                                                    |
| sympy_expand               | 454 ms                                                                | 515 ms: 1.14x slower                                                     |
| logging_silent             | 127 ns                                                                | 144 ns: 1.14x slower                                                     |
| coverage                   | 87.3 ms                                                               | 99.4 ms: 1.14x slower                                                    |
| richards_super             | 58.5 ms                                                               | 66.9 ms: 1.14x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 70.0 ms: 1.16x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 145 ms: 1.16x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 33.9 ms: 1.20x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.25 sec: 1.20x slower                                                   |
| scimark_sor                | 150 ms                                                                | 179 ms: 1.20x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 312 us: 1.20x slower                                                     |
| mako                       | 12.9 ms                                                               | 15.5 ms: 1.20x slower                                                    |
| richards                   | 50.9 ms                                                               | 61.3 ms: 1.20x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 449 us: 1.23x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 8.58 ms: 1.23x slower                                                    |
| pidigits                   | 233 ms                                                                | 293 ms: 1.26x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 15.8 ms: 1.29x slower                                                    |
| nbody                      | 105 ms                                                                | 135 ms: 1.29x slower                                                     |
| fannkuch                   | 443 ms                                                                | 578 ms: 1.30x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.7 ms: 1.47x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.71 ms: 1.53x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.62 ms: 1.89x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 6.44 sec: 913.26x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                             |

Benchmark hidden because not significant (10): raytrace, scimark_sparse_mat_mult, sympy_sum, dulwich_log, spectral_norm, html5lib, logging_simple, float, sympy_integrate, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250116-3.14.0a4+-313b96e-CLANG/bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 96.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x