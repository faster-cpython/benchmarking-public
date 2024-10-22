# Results vs. 3.12.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 362 ms: 1.18x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.63 sec: 1.22x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.39x faster                                                    |
| async_tree_none            | 624 ms                                                                | 451 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 573 ms: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 547 ms: 1.35x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.11 sec: 1.27x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 742 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.5 ms: 1.02x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 256 ms: 1.01x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| regex_compile  | 137 ms                                                                | 176 ms: 1.29x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 272 us: 1.05x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 385 us: 1.05x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 50.3 ms: 1.24x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.5 ms: 1.26x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 81.2 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.39x faster                                                    |
| async_tree_none            | 624 ms                                                                | 451 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 573 ms: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 547 ms: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.8 us: 1.31x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.11 sec: 1.27x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 742 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.5 ms: 1.19x faster                                                   |
| deepcopy                   | 446 us                                                                | 376 us: 1.19x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                   |
| raytrace                   | 353 ms                                                                | 323 ms: 1.09x faster                                                    |
| comprehensions             | 25.4 us                                                               | 23.3 us: 1.09x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.12 us: 1.07x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.84 us: 1.06x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.02 us: 1.02x faster                                                   |
| float                      | 92.1 ms                                                               | 90.5 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.29 ms: 1.01x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                  |
| regex_dna                  | 254 ms                                                                | 256 ms: 1.01x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.45 sec: 1.01x slower                                                  |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                    |
| thrift                     | 937 us                                                                | 963 us: 1.03x slower                                                    |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| async_generators           | 491 ms                                                                | 505 ms: 1.03x slower                                                    |
| richards_super             | 58.5 ms                                                               | 60.7 ms: 1.04x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 90.3 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 272 us: 1.05x slower                                                    |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.4 ms: 1.05x slower                                                   |
| dask                       | 376 ms                                                                | 396 ms: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 385 us: 1.05x slower                                                    |
| pyflate                    | 559 ms                                                                | 589 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.85 ms: 1.06x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.8 ms: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.40 ms: 1.07x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 612 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.74 ms: 1.09x slower                                                   |
| scimark_fft                | 418 ms                                                                | 456 ms: 1.09x slower                                                    |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.60 ms: 1.10x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.86 ms: 1.11x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.05 ms: 1.12x slower                                                   |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.13x slower                                                    |
| go                         | 157 ms                                                                | 177 ms: 1.13x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                    |
| pylint                     | 355 ms                                                                | 403 ms: 1.14x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 70.0 ms: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.09 ms: 1.16x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 116 ms: 1.17x slower                                                    |
| scimark_sor                | 150 ms                                                                | 175 ms: 1.17x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 72.9 ms: 1.18x slower                                                   |
| 2to3                       | 308 ms                                                                | 362 ms: 1.18x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.63 sec: 1.22x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 2.35 ms: 1.23x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.23x slower                                                   |
| sympy_str                  | 280 ms                                                                | 343 ms: 1.23x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.7 ms: 1.23x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.13 sec: 1.23x slower                                                  |
| django_template            | 40.7 ms                                                               | 50.3 ms: 1.24x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.33 sec: 1.24x slower                                                  |
| scimark_lu                 | 146 ms                                                                | 181 ms: 1.24x slower                                                    |
| chaos                      | 71.4 ms                                                               | 89.1 ms: 1.25x slower                                                   |
| sympy_expand               | 454 ms                                                                | 569 ms: 1.26x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.5 ms: 1.26x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 197 ms: 1.27x slower                                                    |
| regex_compile              | 137 ms                                                                | 176 ms: 1.29x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.12 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 81.2 ms: 1.34x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, tornado_http, xml_etree_iterparse, xml_etree_process
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x