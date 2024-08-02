# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 353 ms: 1.14x slower                                                    |
| chameleon      | 8.81 ms                                                               | 9.93 ms: 1.13x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.51 sec: 1.17x slower                                                  |
| html5lib       | 65.1 ms                                                               | 73.7 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 507 ms: 1.23x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 481 ms: 1.20x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 665 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 646 ms: 1.15x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 814 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 816 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.15x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| float          | 92.1 ms                                                               | 113 ms: 1.23x slower                                                    |
| nbody          | 105 ms                                                                | 137 ms: 1.31x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                   |
| regex_compile  | 137 ms                                                                | 166 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle               | 13.4 us                                                               | 14.0 us: 1.04x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.2 us: 1.05x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 162 ms: 1.08x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.77 us: 1.10x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 87.2 ms: 1.10x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 125 ms: 1.12x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 3.09 sec: 1.19x slower                                                  |
| pickle_pure_python   | 365 us                                                                | 440 us: 1.21x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 349 us: 1.34x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.10x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 48.9 ms: 1.20x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 76.1 ms: 1.26x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.6 ms: 1.30x slower                                                   |
| mako            | 12.9 ms                                                               | 16.8 ms: 1.30x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.26x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 507 ms: 1.23x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 481 ms: 1.20x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 665 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 646 ms: 1.15x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 814 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                  |
| generators                 | 43.5 ms                                                               | 39.5 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 816 ms: 1.08x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.38 us: 1.04x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.07 us: 1.03x faster                                                   |
| raytrace                   | 353 ms                                                                | 342 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                    |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                  |
| dask                       | 376 ms                                                                | 391 ms: 1.04x slower                                                    |
| pickle                     | 13.4 us                                                               | 14.0 us: 1.04x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 592 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| thrift                     | 937 us                                                                | 983 us: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.2 us: 1.05x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 65.2 ms: 1.05x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.59 sec: 1.05x slower                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| async_generators           | 491 ms                                                                | 517 ms: 1.05x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.98 us: 1.05x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.8 ms: 1.06x slower                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 162 ms: 1.08x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.71 ms: 1.09x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                  |
| unpickle_list              | 6.17 us                                                               | 6.77 us: 1.10x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 87.2 ms: 1.10x slower                                                   |
| python_startup             | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 125 ms: 1.12x slower                                                    |
| pylint                     | 355 ms                                                                | 396 ms: 1.12x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 9.93 ms: 1.13x slower                                                   |
| sympy_str                  | 280 ms                                                                | 317 ms: 1.13x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 73.7 ms: 1.13x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 175 ms: 1.13x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                   |
| 2to3                       | 308 ms                                                                | 353 ms: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                    |
| sympy_expand               | 454 ms                                                                | 522 ms: 1.15x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 101 ms: 1.17x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.80 us: 1.17x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.51 sec: 1.17x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 72.3 ms: 1.18x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 149 ms: 1.18x slower                                                    |
| comprehensions             | 25.4 us                                                               | 30.1 us: 1.19x slower                                                   |
| meteor_contest             | 112 ms                                                                | 133 ms: 1.19x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.09 sec: 1.19x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 5.25 ms: 1.19x slower                                                   |
| chaos                      | 71.4 ms                                                               | 85.6 ms: 1.20x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 25.9 ms: 1.20x slower                                                   |
| deepcopy                   | 446 us                                                                | 535 us: 1.20x slower                                                    |
| django_template            | 40.7 ms                                                               | 48.9 ms: 1.20x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 440 us: 1.21x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.77 ms: 1.21x slower                                                   |
| regex_compile              | 137 ms                                                                | 166 ms: 1.21x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.22 ms: 1.22x slower                                                   |
| float                      | 92.1 ms                                                               | 113 ms: 1.23x slower                                                    |
| richards_super             | 58.5 ms                                                               | 72.5 ms: 1.24x slower                                                   |
| go                         | 157 ms                                                                | 195 ms: 1.24x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 5.14 ms: 1.25x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 76.1 ms: 1.26x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 227 us: 1.26x slower                                                    |
| richards                   | 50.9 ms                                                               | 64.4 ms: 1.26x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.41 sec: 1.28x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 2.47 ms: 1.29x slower                                                   |
| scimark_fft                | 418 ms                                                                | 539 ms: 1.29x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.18 sec: 1.29x slower                                                  |
| fannkuch                   | 443 ms                                                                | 574 ms: 1.30x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.05 ms: 1.30x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 35.6 ms: 1.30x slower                                                   |
| pyflate                    | 559 ms                                                                | 727 ms: 1.30x slower                                                    |
| mako                       | 12.9 ms                                                               | 16.8 ms: 1.30x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 130 ms: 1.31x slower                                                    |
| nbody                      | 105 ms                                                                | 137 ms: 1.31x slower                                                    |
| scimark_sor                | 150 ms                                                                | 198 ms: 1.32x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 114 ms: 1.34x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 349 us: 1.34x slower                                                    |
| spectral_norm              | 131 ms                                                                | 185 ms: 1.41x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 207 ms: 1.42x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 71.9 us: 1.45x slower                                                   |
| logging_silent             | 127 ns                                                                | 189 ns: 1.49x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.5 ms: 1.51x slower                                                   |
| telco                      | 8.51 ms                                                               | 168 ms: 19.77x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.16x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_list, pickle_dict, tornado_http
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.93x