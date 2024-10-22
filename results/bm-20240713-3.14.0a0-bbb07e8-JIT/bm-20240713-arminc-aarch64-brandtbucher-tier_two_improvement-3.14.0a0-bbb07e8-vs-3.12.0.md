# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-aarch64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 362 ms: 1.18x slower                                                          |
| docutils       | 2.98 sec                                                              | 3.59 sec: 1.20x slower                                                        |
| html5lib       | 65.1 ms                                                               | 70.8 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                                          |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                          |
| async_tree_memoization_tg  | 740 ms                                                                | 547 ms: 1.35x faster                                                          |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 594 ms: 1.31x faster                                                          |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 734 ms: 1.24x faster                                                          |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                          |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                          |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                          |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                         |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                         |
| regex_compile  | 137 ms                                                                | 178 ms: 1.30x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                          |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                        |
| unpickle_pure_python | 260 us                                                                | 272 us: 1.05x slower                                                          |
| json_loads           | 30.7 us                                                               | 33.2 us: 1.08x slower                                                         |
| pickle_pure_python   | 365 us                                                                | 400 us: 1.10x slower                                                          |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                         |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                                  |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                                         |
| python_startup         | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                         |
| django_template | 40.7 ms                                                               | 50.6 ms: 1.25x slower                                                         |
| genshi_text     | 27.4 ms                                                               | 34.5 ms: 1.26x slower                                                         |
| genshi_xml      | 60.6 ms                                                               | 78.7 ms: 1.30x slower                                                         |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                                          |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                          |
| async_tree_memoization_tg  | 740 ms                                                                | 547 ms: 1.35x faster                                                          |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 594 ms: 1.31x faster                                                          |
| deepcopy_memo              | 49.6 us                                                               | 38.8 us: 1.28x faster                                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 734 ms: 1.24x faster                                                          |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                          |
| generators                 | 43.5 ms                                                               | 37.3 ms: 1.17x faster                                                         |
| deepcopy                   | 446 us                                                                | 383 us: 1.16x faster                                                          |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.12x faster                                                         |
| comprehensions             | 25.4 us                                                               | 23.4 us: 1.08x faster                                                         |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                                          |
| logging_simple             | 7.63 us                                                               | 7.22 us: 1.06x faster                                                         |
| logging_format             | 8.34 us                                                               | 8.06 us: 1.03x faster                                                         |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                          |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                          |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                        |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                          |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                         |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                                        |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.02x slower                                                         |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                        |
| thrift                     | 937 us                                                                | 967 us: 1.03x slower                                                          |
| crypto_pyaes               | 86.6 ms                                                               | 89.5 ms: 1.03x slower                                                         |
| richards_super             | 58.5 ms                                                               | 60.5 ms: 1.03x slower                                                         |
| async_generators           | 491 ms                                                                | 509 ms: 1.04x slower                                                          |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                          |
| python_startup_no_site     | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                                         |
| deepcopy_reduce            | 4.10 us                                                               | 4.28 us: 1.04x slower                                                         |
| dask                       | 376 ms                                                                | 393 ms: 1.05x slower                                                          |
| unpickle_pure_python       | 260 us                                                                | 272 us: 1.05x slower                                                          |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.0 ms: 1.05x slower                                                         |
| richards                   | 50.9 ms                                                               | 53.6 ms: 1.05x slower                                                         |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                         |
| json                       | 5.54 ms                                                               | 5.90 ms: 1.06x slower                                                         |
| fannkuch                   | 443 ms                                                                | 473 ms: 1.07x slower                                                          |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                         |
| deltablue                  | 4.12 ms                                                               | 4.44 ms: 1.08x slower                                                         |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                                         |
| html5lib                   | 65.1 ms                                                               | 70.8 ms: 1.09x slower                                                         |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                          |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.09x slower                                                          |
| pickle_pure_python         | 365 us                                                                | 400 us: 1.10x slower                                                          |
| asyncio_tcp                | 566 ms                                                                | 621 ms: 1.10x slower                                                          |
| scimark_fft                | 418 ms                                                                | 460 ms: 1.10x slower                                                          |
| logging_silent             | 127 ns                                                                | 139 ns: 1.10x slower                                                          |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                         |
| pyflate                    | 559 ms                                                                | 616 ms: 1.10x slower                                                          |
| pycparser                  | 1.26 sec                                                              | 1.38 sec: 1.10x slower                                                        |
| sqlglot_parse              | 1.46 ms                                                               | 1.62 ms: 1.10x slower                                                         |
| sqlglot_transpile          | 1.83 ms                                                               | 2.03 ms: 1.11x slower                                                         |
| bench_mp_pool              | 7.05 ms                                                               | 7.91 ms: 1.12x slower                                                         |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.99 ms: 1.13x slower                                                         |
| python_startup             | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                         |
| pylint                     | 355 ms                                                                | 404 ms: 1.14x slower                                                          |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                          |
| gc_traversal               | 4.40 ms                                                               | 5.02 ms: 1.14x slower                                                         |
| sqlglot_optimize           | 61.3 ms                                                               | 70.2 ms: 1.14x slower                                                         |
| sqlglot_normalize          | 126 ms                                                                | 144 ms: 1.15x slower                                                          |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                          |
| typing_runtime_protocols   | 181 us                                                                | 210 us: 1.16x slower                                                          |
| 2to3                       | 308 ms                                                                | 362 ms: 1.18x slower                                                          |
| nqueens                    | 99.2 ms                                                               | 118 ms: 1.18x slower                                                          |
| dulwich_log                | 62.0 ms                                                               | 74.2 ms: 1.20x slower                                                         |
| docutils                   | 2.98 sec                                                              | 3.59 sec: 1.20x slower                                                        |
| scimark_sor                | 150 ms                                                                | 181 ms: 1.21x slower                                                          |
| sympy_str                  | 280 ms                                                                | 339 ms: 1.21x slower                                                          |
| create_gc_cycles           | 1.92 ms                                                               | 2.34 ms: 1.22x slower                                                         |
| sympy_integrate            | 21.6 ms                                                               | 26.6 ms: 1.23x slower                                                         |
| django_template            | 40.7 ms                                                               | 50.6 ms: 1.25x slower                                                         |
| sympy_expand               | 454 ms                                                                | 565 ms: 1.25x slower                                                          |
| telco                      | 8.51 ms                                                               | 10.6 ms: 1.25x slower                                                         |
| genshi_text                | 27.4 ms                                                               | 34.5 ms: 1.26x slower                                                         |
| chaos                      | 71.4 ms                                                               | 89.9 ms: 1.26x slower                                                         |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.26x slower                                                        |
| sympy_sum                  | 154 ms                                                                | 195 ms: 1.26x slower                                                          |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.26x slower                                                          |
| pprint_pformat             | 1.88 sec                                                              | 2.38 sec: 1.27x slower                                                        |
| regex_compile              | 137 ms                                                                | 178 ms: 1.30x slower                                                          |
| genshi_xml                 | 60.6 ms                                                               | 78.7 ms: 1.30x slower                                                         |
| hexiom                     | 6.98 ms                                                               | 9.16 ms: 1.31x slower                                                         |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                                  |

Benchmark hidden because not significant (7): xml_etree_parse, float, coroutines, xml_etree_generate, asyncio_websockets, xml_etree_process, tornado_http
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x