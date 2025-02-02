# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.086x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 398 ms: 1.29x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.76 sec: 1.26x slower                                                   |
| html5lib       | 65.1 ms                                                               | 74.6 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.23x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                     |
| async_tree_none            | 624 ms                                                                | 471 ms: 1.32x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 618 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 461 ms: 1.25x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 773 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 766 ms: 1.15x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.29 sec: 1.09x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.22x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 96.2 ms: 1.05x slower                                                    |
| pidigits       | 233 ms                                                                | 249 ms: 1.07x slower                                                     |
| nbody          | 105 ms                                                                | 118 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 5.08 ms: 1.10x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                    |
| regex_compile  | 137 ms                                                                | 183 ms: 1.33x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.15x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 82.3 ms: 1.04x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 273 us: 1.05x slower                                                     |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.06x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 422 us: 1.16x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.14 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 34.0 ms: 1.24x slower                                                    |
| django_template | 40.7 ms                                                               | 51.2 ms: 1.26x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 81.4 ms: 1.34x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                     |
| async_tree_none            | 624 ms                                                                | 471 ms: 1.32x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 618 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 461 ms: 1.25x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.7 us: 1.22x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 773 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 766 ms: 1.15x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.29 sec: 1.09x faster                                                   |
| deepcopy                   | 446 us                                                                | 412 us: 1.08x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 87.8 ms: 1.01x slower                                                    |
| raytrace                   | 353 ms                                                                | 362 ms: 1.02x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 677 ms: 1.03x slower                                                     |
| json                       | 5.54 ms                                                               | 5.75 ms: 1.04x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 82.3 ms: 1.04x slower                                                    |
| float                      | 92.1 ms                                                               | 96.2 ms: 1.05x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.58 sec: 1.05x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.4 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                     |
| thrift                     | 937 us                                                                | 984 us: 1.05x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 273 us: 1.05x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                    |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.38 ms: 1.06x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.40 ms: 1.07x slower                                                    |
| pidigits                   | 233 ms                                                                | 249 ms: 1.07x slower                                                     |
| scimark_fft                | 418 ms                                                                | 449 ms: 1.07x slower                                                     |
| async_generators           | 491 ms                                                                | 532 ms: 1.08x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.10 us: 1.09x slower                                                    |
| pyflate                    | 559 ms                                                                | 609 ms: 1.09x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.14 ms: 1.09x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 5.08 ms: 1.10x slower                                                    |
| nbody                      | 105 ms                                                                | 118 ms: 1.13x slower                                                     |
| meteor_contest             | 112 ms                                                                | 127 ms: 1.13x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.66 ms: 1.13x slower                                                    |
| generators                 | 43.5 ms                                                               | 49.3 ms: 1.13x slower                                                    |
| spectral_norm              | 131 ms                                                                | 149 ms: 1.14x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 74.6 ms: 1.15x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 422 us: 1.16x slower                                                     |
| fannkuch                   | 443 ms                                                                | 513 ms: 1.16x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.88 ms: 1.16x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.16x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                    |
| chaos                      | 71.4 ms                                                               | 83.8 ms: 1.17x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| go                         | 157 ms                                                                | 187 ms: 1.19x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.18 ms: 1.19x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.38 ms: 1.19x slower                                                    |
| richards_super             | 58.5 ms                                                               | 69.9 ms: 1.19x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.50 sec: 1.20x slower                                                   |
| sqlalchemy_imperative      | 16.7 ms                                                               | 20.6 ms: 1.24x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.0 ms: 1.24x slower                                                    |
| richards                   | 50.9 ms                                                               | 63.3 ms: 1.24x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 224 us: 1.24x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 198 ms: 1.26x slower                                                     |
| django_template            | 40.7 ms                                                               | 51.2 ms: 1.26x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.76 sec: 1.26x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 127 ms: 1.28x slower                                                     |
| 2to3                       | 308 ms                                                                | 398 ms: 1.29x slower                                                     |
| sympy_str                  | 280 ms                                                                | 363 ms: 1.30x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 82.2 ms: 1.33x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 167 ms: 1.33x slower                                                     |
| regex_compile              | 137 ms                                                                | 183 ms: 1.33x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 81.4 ms: 1.34x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 29.3 ms: 1.36x slower                                                    |
| sympy_expand               | 454 ms                                                                | 616 ms: 1.36x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 83.6 ms: 1.36x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 212 ms: 1.38x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.26 sec: 1.38x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.63 sec: 1.40x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| pylint                     | 355 ms                                                                | 509 ms: 1.44x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 10.1 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.42 ms: 1.46x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.75 ms: 1.95x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.91 sec: 270.56x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.19x slower                                                             |

Benchmark hidden because not significant (10): comprehensions, coroutines, xml_etree_parse, logging_format, regex_dna, deepcopy_reduce, logging_simple, xml_etree_generate, xml_etree_iterparse, mako
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.086x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x