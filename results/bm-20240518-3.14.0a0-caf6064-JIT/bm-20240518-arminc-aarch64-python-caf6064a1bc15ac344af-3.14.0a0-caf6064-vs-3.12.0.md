# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 360 ms: 1.17x slower                                                    |
| chameleon      | 8.81 ms                                                               | 9.20 ms: 1.04x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.54 sec: 1.18x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.6 ms: 1.09x slower                                                   |
| tornado_http   | 136 ms                                                                | 145 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 497 ms: 1.25x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 473 ms: 1.22x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 617 ms: 1.20x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 655 ms: 1.19x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.23 sec: 1.14x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 807 ms: 1.13x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 813 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 171 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.32 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| pickle_dict          | 37.3 us                                                               | 38.2 us: 1.02x slower                                                   |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.1 us: 1.04x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 387 us: 1.06x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.55 us: 1.06x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 276 us: 1.06x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.8 ms: 1.29x slower                                                   |
| python_startup         | 11.4 ms                                                               | 14.9 ms: 1.31x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 49.6 ms: 1.22x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.2 ms: 1.28x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 83.5 ms: 1.38x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 497 ms: 1.25x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 473 ms: 1.22x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 617 ms: 1.20x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 655 ms: 1.19x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.23 sec: 1.14x faster                                                  |
| generators                 | 43.5 ms                                                               | 38.3 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 807 ms: 1.13x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.0 us: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 813 ms: 1.09x faster                                                    |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.79 us: 1.07x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.24 us: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 665 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.82 us: 1.01x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.32 us: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| thrift                     | 937 us                                                                | 953 us: 1.02x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.48 sec: 1.02x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| pickle_dict                | 37.3 us                                                               | 38.2 us: 1.02x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.5 ms: 1.03x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                  |
| chameleon                  | 8.81 ms                                                               | 9.20 ms: 1.04x slower                                                   |
| dask                       | 376 ms                                                                | 393 ms: 1.04x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.1 us: 1.04x slower                                                   |
| async_generators           | 491 ms                                                                | 514 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| richards_super             | 58.5 ms                                                               | 61.7 ms: 1.05x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 387 us: 1.06x slower                                                    |
| richards                   | 50.9 ms                                                               | 54.1 ms: 1.06x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.55 us: 1.06x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 276 us: 1.06x slower                                                    |
| meteor_contest             | 112 ms                                                                | 119 ms: 1.06x slower                                                    |
| tornado_http               | 136 ms                                                                | 145 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.07x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.58 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 70.6 ms: 1.09x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 615 ms: 1.09x slower                                                    |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| scimark_fft                | 418 ms                                                                | 456 ms: 1.09x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                   |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                                    |
| deepcopy                   | 446 us                                                                | 494 us: 1.11x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.88 ms: 1.11x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.58 ms: 1.11x slower                                                   |
| pyflate                    | 559 ms                                                                | 623 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.11x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 69.7 ms: 1.12x slower                                                   |
| sympy_str                  | 280 ms                                                                | 317 ms: 1.13x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 69.8 ms: 1.14x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.67 us: 1.14x slower                                                   |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 145 ms: 1.15x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 208 us: 1.15x slower                                                    |
| pylint                     | 355 ms                                                                | 411 ms: 1.16x slower                                                    |
| 2to3                       | 308 ms                                                                | 360 ms: 1.17x slower                                                    |
| scimark_sor                | 150 ms                                                                | 176 ms: 1.17x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.18 ms: 1.18x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.54 sec: 1.18x slower                                                  |
| sympy_sum                  | 154 ms                                                                | 184 ms: 1.19x slower                                                    |
| sympy_expand               | 454 ms                                                                | 541 ms: 1.19x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 119 ms: 1.20x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.0 ms: 1.20x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.10 sec: 1.20x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.28 sec: 1.21x slower                                                  |
| django_template            | 40.7 ms                                                               | 49.6 ms: 1.22x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 8.66 ms: 1.23x slower                                                   |
| chaos                      | 71.4 ms                                                               | 88.5 ms: 1.24x slower                                                   |
| regex_compile              | 137 ms                                                                | 171 ms: 1.24x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 182 ms: 1.25x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.42 ms: 1.26x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 35.2 ms: 1.28x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 10.8 ms: 1.29x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 9.07 ms: 1.30x slower                                                   |
| python_startup             | 11.4 ms                                                               | 14.9 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 83.5 ms: 1.38x slower                                                   |
| telco                      | 8.51 ms                                                               | 167 ms: 19.58x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.10x slower                                                            |

Benchmark hidden because not significant (7): float, coroutines, deepcopy_memo, crypto_pyaes, xml_etree_iterparse, xml_etree_process, xml_etree_generate
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.00x