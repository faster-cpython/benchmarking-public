# Results vs. 3.12.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-aarch64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 370 ms: 1.20x slower                                                              |
| docutils       | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                            |
| html5lib       | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                             |
| tornado_http   | 136 ms                                                                | 139 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 754 ms: 1.21x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                              |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 258 ms: 1.01x slower                                                              |
| regex_v8       | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                             |
| regex_effbot   | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                             |
| regex_compile  | 137 ms                                                                | 182 ms: 1.33x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                                            |
| unpickle_pure_python | 260 us                                                                | 277 us: 1.06x slower                                                              |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                             |
| json_loads           | 30.7 us                                                               | 32.9 us: 1.07x slower                                                             |
| pickle_pure_python   | 365 us                                                                | 398 us: 1.09x slower                                                              |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                                      |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.88 ms: 1.06x slower                                                             |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 33.2 ms: 1.21x slower                                                             |
| genshi_xml      | 60.6 ms                                                               | 75.3 ms: 1.24x slower                                                             |
| django_template | 40.7 ms                                                               | 50.6 ms: 1.24x slower                                                             |
| Geometric mean  | (ref)                                                                 | 1.17x slower                                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 38.9 us: 1.27x faster                                                             |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 754 ms: 1.21x faster                                                              |
| deepcopy                   | 446 us                                                                | 382 us: 1.17x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.11x faster                                                             |
| raytrace                   | 353 ms                                                                | 332 ms: 1.07x faster                                                              |
| comprehensions             | 25.4 us                                                               | 24.1 us: 1.05x faster                                                             |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                              |
| logging_format             | 8.34 us                                                               | 8.05 us: 1.04x faster                                                             |
| logging_simple             | 7.63 us                                                               | 7.37 us: 1.04x faster                                                             |
| coroutines                 | 29.0 ms                                                               | 28.2 ms: 1.03x faster                                                             |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                              |
| regex_dna                  | 254 ms                                                                | 258 ms: 1.01x slower                                                              |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                             |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                                            |
| tornado_http               | 136 ms                                                                | 139 ms: 1.03x slower                                                              |
| tomli_loads                | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                                            |
| deepcopy_reduce            | 4.10 us                                                               | 4.22 us: 1.03x slower                                                             |
| thrift                     | 937 us                                                                | 964 us: 1.03x slower                                                              |
| dask                       | 376 ms                                                                | 391 ms: 1.04x slower                                                              |
| async_generators           | 491 ms                                                                | 511 ms: 1.04x slower                                                              |
| json                       | 5.54 ms                                                               | 5.77 ms: 1.04x slower                                                             |
| crypto_pyaes               | 86.6 ms                                                               | 90.3 ms: 1.04x slower                                                             |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.29 sec: 1.05x slower                                                            |
| richards_super             | 58.5 ms                                                               | 61.6 ms: 1.05x slower                                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.8 ms: 1.06x slower                                                             |
| regex_v8                   | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                             |
| meteor_contest             | 112 ms                                                                | 119 ms: 1.06x slower                                                              |
| python_startup_no_site     | 8.37 ms                                                               | 8.88 ms: 1.06x slower                                                             |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                              |
| unpickle_pure_python       | 260 us                                                                | 277 us: 1.06x slower                                                              |
| regex_effbot               | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                             |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                             |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.08x slower                                                              |
| richards                   | 50.9 ms                                                               | 55.0 ms: 1.08x slower                                                             |
| deltablue                  | 4.12 ms                                                               | 4.44 ms: 1.08x slower                                                             |
| html5lib                   | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 398 us: 1.09x slower                                                              |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.10x slower                                                              |
| pyflate                    | 559 ms                                                                | 616 ms: 1.10x slower                                                              |
| scimark_fft                | 418 ms                                                                | 462 ms: 1.10x slower                                                              |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.87 ms: 1.11x slower                                                             |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                              |
| bench_mp_pool              | 7.05 ms                                                               | 7.89 ms: 1.12x slower                                                             |
| sqlglot_parse              | 1.46 ms                                                               | 1.67 ms: 1.14x slower                                                             |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                             |
| asyncio_tcp                | 566 ms                                                                | 653 ms: 1.15x slower                                                              |
| go                         | 157 ms                                                                | 182 ms: 1.16x slower                                                              |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                              |
| gc_traversal               | 4.40 ms                                                               | 5.09 ms: 1.16x slower                                                             |
| scimark_sor                | 150 ms                                                                | 173 ms: 1.16x slower                                                              |
| pycparser                  | 1.26 sec                                                              | 1.45 sec: 1.16x slower                                                            |
| sqlglot_transpile          | 1.83 ms                                                               | 2.13 ms: 1.17x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.17x slower                                                              |
| sqlglot_optimize           | 61.3 ms                                                               | 72.0 ms: 1.17x slower                                                             |
| sqlglot_normalize          | 126 ms                                                                | 149 ms: 1.19x slower                                                              |
| 2to3                       | 308 ms                                                                | 370 ms: 1.20x slower                                                              |
| genshi_text                | 27.4 ms                                                               | 33.2 ms: 1.21x slower                                                             |
| chaos                      | 71.4 ms                                                               | 87.7 ms: 1.23x slower                                                             |
| scimark_lu                 | 146 ms                                                                | 180 ms: 1.23x slower                                                              |
| genshi_xml                 | 60.6 ms                                                               | 75.3 ms: 1.24x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 2.39 ms: 1.24x slower                                                             |
| django_template            | 40.7 ms                                                               | 50.6 ms: 1.24x slower                                                             |
| pylint                     | 355 ms                                                                | 442 ms: 1.25x slower                                                              |
| sympy_str                  | 280 ms                                                                | 350 ms: 1.25x slower                                                              |
| telco                      | 8.51 ms                                                               | 10.7 ms: 1.25x slower                                                             |
| docutils                   | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                            |
| nqueens                    | 99.2 ms                                                               | 124 ms: 1.25x slower                                                              |
| sympy_integrate            | 21.6 ms                                                               | 27.7 ms: 1.28x slower                                                             |
| pprint_safe_repr           | 916 ms                                                                | 1.18 sec: 1.29x slower                                                            |
| pprint_pformat             | 1.88 sec                                                              | 2.43 sec: 1.29x slower                                                            |
| sympy_sum                  | 154 ms                                                                | 203 ms: 1.31x slower                                                              |
| sympy_expand               | 454 ms                                                                | 595 ms: 1.31x slower                                                              |
| generators                 | 43.5 ms                                                               | 57.4 ms: 1.32x slower                                                             |
| regex_compile              | 137 ms                                                                | 182 ms: 1.33x slower                                                              |
| hexiom                     | 6.98 ms                                                               | 9.78 ms: 1.40x slower                                                             |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                                      |

Benchmark hidden because not significant (6): xml_etree_iterparse, float, mako, asyncio_websockets, xml_etree_process, xml_etree_generate
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.01x