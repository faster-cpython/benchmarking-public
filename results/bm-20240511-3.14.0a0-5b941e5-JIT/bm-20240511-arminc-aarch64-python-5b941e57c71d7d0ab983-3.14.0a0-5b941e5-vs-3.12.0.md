# Results vs. 3.12.0

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 364 ms: 1.18x slower                                                    |
| chameleon      | 8.81 ms                                                               | 9.32 ms: 1.06x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.7 ms: 1.09x slower                                                   |
| tornado_http   | 136 ms                                                                | 144 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 499 ms: 1.25x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 617 ms: 1.20x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 656 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 801 ms: 1.14x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.24 sec: 1.14x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 811 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.6 ms: 1.02x faster                                                   |
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| regex_compile  | 137 ms                                                                | 171 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 80.3 ms: 1.02x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.35 us: 1.03x slower                                                   |
| pickle               | 13.4 us                                                               | 14.1 us: 1.05x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 276 us: 1.06x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 394 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_generate, pickle_dict, pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.8 ms: 1.30x slower                                                   |
| python_startup         | 11.4 ms                                                               | 14.8 ms: 1.31x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 49.8 ms: 1.22x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.4 ms: 1.26x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 81.9 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 499 ms: 1.25x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 617 ms: 1.20x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 656 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 801 ms: 1.14x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.24 sec: 1.14x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                  |
| generators                 | 43.5 ms                                                               | 38.7 ms: 1.12x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.9 us: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 811 ms: 1.09x faster                                                    |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.92 us: 1.05x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.39 us: 1.03x faster                                                   |
| float                      | 92.1 ms                                                               | 90.6 ms: 1.02x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.80 us: 1.01x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 50.1 us: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 665 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.3 ms: 1.02x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.48 sec: 1.02x slower                                                  |
| json                       | 5.54 ms                                                               | 5.69 ms: 1.03x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.4 ms: 1.03x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.35 us: 1.03x slower                                                   |
| thrift                     | 937 us                                                                | 966 us: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                  |
| async_generators           | 491 ms                                                                | 513 ms: 1.05x slower                                                    |
| pickle                     | 13.4 us                                                               | 14.1 us: 1.05x slower                                                   |
| richards_super             | 58.5 ms                                                               | 61.3 ms: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| dask                       | 376 ms                                                                | 397 ms: 1.05x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| chameleon                  | 8.81 ms                                                               | 9.32 ms: 1.06x slower                                                   |
| meteor_contest             | 112 ms                                                                | 119 ms: 1.06x slower                                                    |
| richards                   | 50.9 ms                                                               | 54.1 ms: 1.06x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 276 us: 1.06x slower                                                    |
| tornado_http               | 136 ms                                                                | 144 ms: 1.07x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 605 ms: 1.07x slower                                                    |
| fannkuch                   | 443 ms                                                                | 475 ms: 1.07x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 394 us: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 70.7 ms: 1.09x slower                                                   |
| scimark_fft                | 418 ms                                                                | 455 ms: 1.09x slower                                                    |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.60 ms: 1.09x slower                                                   |
| logging_silent             | 127 ns                                                                | 139 ns: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.84 ms: 1.10x slower                                                   |
| pyflate                    | 559 ms                                                                | 619 ms: 1.11x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.56 ms: 1.11x slower                                                   |
| deepcopy                   | 446 us                                                                | 495 us: 1.11x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.04 ms: 1.12x slower                                                   |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                    |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 69.9 ms: 1.14x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.67 us: 1.14x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 144 ms: 1.14x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 71.8 ms: 1.16x slower                                                   |
| sympy_str                  | 280 ms                                                                | 326 ms: 1.16x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.24 ms: 1.17x slower                                                   |
| scimark_sor                | 150 ms                                                                | 176 ms: 1.17x slower                                                    |
| pylint                     | 355 ms                                                                | 419 ms: 1.18x slower                                                    |
| 2to3                       | 308 ms                                                                | 364 ms: 1.18x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 118 ms: 1.19x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 5.35 ms: 1.22x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.29 sec: 1.22x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 26.4 ms: 1.22x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 189 ms: 1.22x slower                                                    |
| sympy_expand               | 454 ms                                                                | 554 ms: 1.22x slower                                                    |
| django_template            | 40.7 ms                                                               | 49.8 ms: 1.22x slower                                                   |
| chaos                      | 71.4 ms                                                               | 88.7 ms: 1.24x slower                                                   |
| regex_compile              | 137 ms                                                                | 171 ms: 1.24x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 182 ms: 1.25x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.4 ms: 1.26x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 8.99 ms: 1.29x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 10.8 ms: 1.30x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.49 ms: 1.30x slower                                                   |
| python_startup             | 11.4 ms                                                               | 14.8 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 81.9 ms: 1.35x slower                                                   |
| telco                      | 8.51 ms                                                               | 166 ms: 19.46x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.10x slower                                                            |

Benchmark hidden because not significant (8): xml_etree_parse, coroutines, crypto_pyaes, xml_etree_generate, pickle_dict, regex_dna, pickle_list, xml_etree_iterparse
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.00x