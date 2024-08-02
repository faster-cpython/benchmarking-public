# Results vs. 3.12.0

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: linux-aarch64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 358 ms: 1.16x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 406 ms: 1.42x faster                                                    |
| async_tree_none            | 624 ms                                                                | 444 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 539 ms: 1.37x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.34x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 735 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 723 ms: 1.22x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.6 ms: 1.03x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 250 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| regex_compile  | 137 ms                                                                | 174 ms: 1.27x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 277 us: 1.07x slower                                                    |
| json_loads           | 30.7 us                                                               | 33.4 us: 1.09x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 398 us: 1.09x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.93 ms: 1.07x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| django_template | 40.7 ms                                                               | 49.6 ms: 1.22x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.2 ms: 1.25x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 81.7 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 406 ms: 1.42x faster                                                    |
| async_tree_none            | 624 ms                                                                | 444 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 539 ms: 1.37x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.34x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 38.8 us: 1.28x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 735 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 723 ms: 1.22x faster                                                    |
| deepcopy                   | 446 us                                                                | 376 us: 1.18x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                   |
| generators                 | 43.5 ms                                                               | 39.3 ms: 1.11x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.2 us: 1.10x faster                                                   |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.79 us: 1.07x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.20 us: 1.06x faster                                                   |
| float                      | 92.1 ms                                                               | 89.6 ms: 1.03x faster                                                   |
| regex_dna                  | 254 ms                                                                | 250 ms: 1.02x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 664 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                                  |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.21 us: 1.03x slower                                                   |
| thrift                     | 937 us                                                                | 964 us: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                  |
| richards_super             | 58.5 ms                                                               | 60.5 ms: 1.04x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.1 ms: 1.04x slower                                                   |
| dask                       | 376 ms                                                                | 391 ms: 1.04x slower                                                    |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                    |
| async_generators           | 491 ms                                                                | 512 ms: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.5 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.4 ms: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.93 ms: 1.07x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 277 us: 1.07x slower                                                    |
| json                       | 5.54 ms                                                               | 5.93 ms: 1.07x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.07x slower                                                  |
| fannkuch                   | 443 ms                                                                | 476 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 614 ms: 1.08x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.47 ms: 1.08x slower                                                   |
| logging_silent             | 127 ns                                                                | 138 ns: 1.09x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.4 us: 1.09x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 398 us: 1.09x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.60 ms: 1.09x slower                                                   |
| pyflate                    | 559 ms                                                                | 613 ms: 1.10x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                   |
| scimark_fft                | 418 ms                                                                | 461 ms: 1.10x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.86 ms: 1.11x slower                                                   |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 141 ms: 1.12x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 69.4 ms: 1.13x slower                                                   |
| spectral_norm              | 131 ms                                                                | 148 ms: 1.14x slower                                                    |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.05 ms: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 71.5 ms: 1.15x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| 2to3                       | 308 ms                                                                | 358 ms: 1.16x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                  |
| sympy_str                  | 280 ms                                                                | 331 ms: 1.18x slower                                                    |
| scimark_sor                | 150 ms                                                                | 177 ms: 1.19x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 118 ms: 1.19x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.40 ms: 1.19x slower                                                   |
| pylint                     | 355 ms                                                                | 423 ms: 1.19x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.31 ms: 1.20x slower                                                   |
| sympy_expand               | 454 ms                                                                | 547 ms: 1.21x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 186 ms: 1.21x slower                                                    |
| django_template            | 40.7 ms                                                               | 49.6 ms: 1.22x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.12 sec: 1.22x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.32 sec: 1.23x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 26.8 ms: 1.24x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.2 ms: 1.25x slower                                                   |
| chaos                      | 71.4 ms                                                               | 89.3 ms: 1.25x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 185 ms: 1.27x slower                                                    |
| regex_compile              | 137 ms                                                                | 174 ms: 1.27x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.00 ms: 1.29x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 81.7 ms: 1.35x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_iterparse, crypto_pyaes, xml_etree_process, xml_etree_generate, tornado_http
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240701-3.14.0a0-33903c5-JIT/bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x