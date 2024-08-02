# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.02x slower
- HPT reliability: 83.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                                    |
| chameleon      | 8.81 ms                                                               | 9.03 ms: 1.02x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| html5lib       | 65.1 ms                                                               | 68.3 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 486 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 465 ms: 1.24x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 642 ms: 1.21x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 628 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 785 ms: 1.16x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.16x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 792 ms: 1.12x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.19x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.6 ms: 1.02x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 131 ms: 1.05x faster                                                    |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 358 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| pickle_list          | 5.25 us                                                               | 5.19 us: 1.01x faster                                                   |
| xml_etree_process    | 79.0 ms                                                               | 80.3 ms: 1.02x slower                                                   |
| pickle               | 13.4 us                                                               | 13.8 us: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.63 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.48 ms: 1.01x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.3 ms: 1.09x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.05x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 61.2 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 28.6 ms: 1.04x slower                                                   |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 486 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 465 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 642 ms: 1.21x faster                                                    |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 628 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 785 ms: 1.16x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.16x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 792 ms: 1.12x faster                                                    |
| generators                 | 43.5 ms                                                               | 39.0 ms: 1.11x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.00 us: 1.09x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 81.5 ms: 1.06x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 58.3 ms: 1.06x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.85 us: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.6 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.05x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                                    |
| regex_compile              | 137 ms                                                                | 131 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.05x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.04x faster                                                   |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.0 ms: 1.02x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 358 us: 1.02x faster                                                    |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                                    |
| float                      | 92.1 ms                                                               | 90.6 ms: 1.02x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.37 sec: 1.01x faster                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| pickle_list                | 5.25 us                                                               | 5.19 us: 1.01x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.07 us: 1.01x faster                                                   |
| hexiom                     | 6.98 ms                                                               | 7.03 ms: 1.01x slower                                                   |
| deepcopy                   | 446 us                                                                | 450 us: 1.01x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 61.2 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.01x slower                                                  |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.48 ms: 1.01x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.3 ms: 1.02x slower                                                   |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.02x slower                                                  |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 935 ms: 1.02x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 9.03 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.02x slower                                                   |
| json                       | 5.54 ms                                                               | 5.68 ms: 1.03x slower                                                   |
| django_template            | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 63.0 ms: 1.03x slower                                                   |
| go                         | 157 ms                                                                | 161 ms: 1.03x slower                                                    |
| richards_super             | 58.5 ms                                                               | 60.1 ms: 1.03x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 51.3 us: 1.03x slower                                                   |
| pyflate                    | 559 ms                                                                | 578 ms: 1.03x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.90 us: 1.03x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 28.6 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 463 ms: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.3 ms: 1.05x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 68.3 ms: 1.05x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.41 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.53 ms: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 443 ms: 1.06x slower                                                    |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.63 us: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| python_startup             | 11.4 ms                                                               | 12.3 ms: 1.09x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.5 ms: 1.14x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.29 ms: 1.20x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.42 ms: 1.26x slower                                                   |
| telco                      | 8.51 ms                                                               | 166 ms: 19.46x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (14): pylint, tornado_http, bench_thread_pool, xml_etree_parse, dask, nqueens, xml_etree_generate, coroutines, pickle_dict, asyncio_websockets, thrift, async_generators, xml_etree_iterparse, asyncio_tcp
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging

# HPT report

- Reliability score: 83.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x