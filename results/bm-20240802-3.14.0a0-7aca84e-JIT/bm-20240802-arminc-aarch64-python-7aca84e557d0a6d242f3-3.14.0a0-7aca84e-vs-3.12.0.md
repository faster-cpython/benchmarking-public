# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.06x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 367 ms: 1.19x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.67 sec: 1.23x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.6 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 435 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 538 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 574 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 696 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 744 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.20x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.3 ms: 1.01x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| regex_compile  | 137 ms                                                                | 174 ms: 1.27x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| xml_etree_generate   | 112 ms                                                                | 114 ms: 1.01x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 275 us: 1.06x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.7 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 396 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.83 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 72.7 ms: 1.20x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 32.9 ms: 1.20x slower                                                   |
| django_template | 40.7 ms                                                               | 52.1 ms: 1.28x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.17x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 435 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 538 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 574 ms: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.4 us: 1.29x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 696 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 744 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.20x faster                                                  |
| deepcopy                   | 446 us                                                                | 376 us: 1.19x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                   |
| raytrace                   | 353 ms                                                                | 332 ms: 1.06x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.1 us: 1.05x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.00 us: 1.04x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.35 us: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| float                      | 92.1 ms                                                               | 91.3 ms: 1.01x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| xml_etree_generate         | 112 ms                                                                | 114 ms: 1.01x slower                                                    |
| scimark_sor                | 150 ms                                                                | 152 ms: 1.02x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 148 ms: 1.02x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 4.22 us: 1.03x slower                                                   |
| async_generators           | 491 ms                                                                | 506 ms: 1.03x slower                                                    |
| dask                       | 376 ms                                                                | 391 ms: 1.04x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                  |
| crypto_pyaes               | 86.6 ms                                                               | 90.2 ms: 1.04x slower                                                   |
| thrift                     | 937 us                                                                | 979 us: 1.04x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.1 ms: 1.05x slower                                                   |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.83 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 134 ns: 1.06x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 275 us: 1.06x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.1 ms: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.06x slower                                                   |
| meteor_contest             | 112 ms                                                                | 120 ms: 1.07x slower                                                    |
| richards                   | 50.9 ms                                                               | 54.9 ms: 1.08x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.44 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.08x slower                                                    |
| fannkuch                   | 443 ms                                                                | 481 ms: 1.08x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 70.6 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| pyflate                    | 559 ms                                                                | 612 ms: 1.09x slower                                                    |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.90 ms: 1.11x slower                                                   |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 4.91 ms: 1.12x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.3 ms: 1.13x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.65 ms: 1.13x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 641 ms: 1.13x slower                                                    |
| scimark_fft                | 418 ms                                                                | 476 ms: 1.14x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.11 ms: 1.16x slower                                                   |
| go                         | 157 ms                                                                | 182 ms: 1.16x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 8.23 ms: 1.17x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 147 ms: 1.17x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.47 sec: 1.17x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 72.5 ms: 1.18x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 213 us: 1.18x slower                                                    |
| 2to3                       | 308 ms                                                                | 367 ms: 1.19x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 72.7 ms: 1.20x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 32.9 ms: 1.20x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| pylint                     | 355 ms                                                                | 429 ms: 1.21x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.35 ms: 1.23x slower                                                   |
| chaos                      | 71.4 ms                                                               | 87.7 ms: 1.23x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.67 sec: 1.23x slower                                                  |
| nqueens                    | 99.2 ms                                                               | 123 ms: 1.24x slower                                                    |
| sympy_str                  | 280 ms                                                                | 350 ms: 1.25x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.26x slower                                                  |
| regex_compile              | 137 ms                                                                | 174 ms: 1.27x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.39 sec: 1.27x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 27.5 ms: 1.27x slower                                                   |
| django_template            | 40.7 ms                                                               | 52.1 ms: 1.28x slower                                                   |
| sympy_expand               | 454 ms                                                                | 589 ms: 1.30x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 201 ms: 1.30x slower                                                    |
| generators                 | 43.5 ms                                                               | 57.3 ms: 1.32x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 9.24 ms: 1.32x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                            |

Benchmark hidden because not significant (5): bench_thread_pool, mako, xml_etree_iterparse, xml_etree_process, tornado_http
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.01x