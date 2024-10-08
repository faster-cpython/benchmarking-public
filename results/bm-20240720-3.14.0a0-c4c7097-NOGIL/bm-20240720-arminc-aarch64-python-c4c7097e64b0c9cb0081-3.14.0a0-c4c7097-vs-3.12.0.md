# Results vs. 3.12.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.55x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 513 ms: 1.66x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.11 sec: 1.38x slower                                                  |
| html5lib       | 65.1 ms                                                               | 121 ms: 1.86x slower                                                    |
| tornado_http   | 136 ms                                                                | 207 ms: 1.53x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 688 ms: 1.08x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 739 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.36 sec: 1.03x faster                                                  |
| async_tree_none            | 624 ms                                                                | 604 ms: 1.03x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 560 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 859 ms: 1.03x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.39 sec: 1.01x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 209 ms: 2.27x slower                                                    |
| nbody          | 105 ms                                                                | 290 ms: 2.77x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.85x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.43 ms: 1.05x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 32.6 ms: 1.15x slower                                                   |
| regex_compile  | 137 ms                                                                | 254 ms: 1.85x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| json_loads           | 30.7 us                                                               | 38.8 us: 1.26x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 157 ms: 1.40x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.7 ms: 1.45x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.20 sec: 1.62x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 130 ms: 1.64x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 538 us: 2.07x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 773 us: 2.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.45x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.8 ms: 1.42x slower                                                   |
| python_startup         | 11.4 ms                                                               | 17.6 ms: 1.55x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.48x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 104 ms: 1.71x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 52.2 ms: 1.90x slower                                                   |
| django_template | 40.7 ms                                                               | 81.3 ms: 2.00x slower                                                   |
| mako            | 12.9 ms                                                               | 28.9 ms: 2.24x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.95x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.45 ms: 1.27x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.60 ms: 1.20x faster                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 6.23 ms: 1.13x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 688 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 739 ms: 1.05x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.43 ms: 1.05x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.36 sec: 1.03x faster                                                  |
| async_tree_none            | 624 ms                                                                | 604 ms: 1.03x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 560 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 859 ms: 1.03x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.39 sec: 1.01x faster                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 26.6 ms: 1.08x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.46 sec: 1.12x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 32.6 ms: 1.15x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 671 ms: 1.19x slower                                                    |
| deepcopy                   | 446 us                                                                | 553 us: 1.24x slower                                                    |
| json                       | 5.54 ms                                                               | 6.97 ms: 1.26x slower                                                   |
| json_loads                 | 30.7 us                                                               | 38.8 us: 1.26x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.38 sec: 1.28x slower                                                  |
| coroutines                 | 29.0 ms                                                               | 38.5 ms: 1.33x slower                                                   |
| generators                 | 43.5 ms                                                               | 57.7 ms: 1.33x slower                                                   |
| docutils                   | 2.98 sec                                                              | 4.11 sec: 1.38x slower                                                  |
| async_generators           | 491 ms                                                                | 686 ms: 1.40x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 157 ms: 1.40x slower                                                    |
| pylint                     | 355 ms                                                                | 502 ms: 1.41x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 11.8 ms: 1.42x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.87 ms: 1.43x slower                                                   |
| scimark_fft                | 418 ms                                                                | 599 ms: 1.43x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.92 ms: 1.44x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 17.7 ms: 1.45x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 5.99 us: 1.46x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 72.8 us: 1.47x slower                                                   |
| telco                      | 8.51 ms                                                               | 12.5 ms: 1.47x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 149 ms: 1.51x slower                                                    |
| coverage                   | 87.3 ms                                                               | 132 ms: 1.51x slower                                                    |
| tornado_http               | 136 ms                                                                | 207 ms: 1.53x slower                                                    |
| meteor_contest             | 112 ms                                                                | 172 ms: 1.53x slower                                                    |
| python_startup             | 11.4 ms                                                               | 17.6 ms: 1.55x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 98.3 ms: 1.58x slower                                                   |
| comprehensions             | 25.4 us                                                               | 40.5 us: 1.60x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 140 ms: 1.61x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 4.20 sec: 1.62x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 35.1 ms: 1.62x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 2.06 sec: 1.64x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 130 ms: 1.64x slower                                                    |
| 2to3                       | 308 ms                                                                | 513 ms: 1.66x slower                                                    |
| fannkuch                   | 443 ms                                                                | 740 ms: 1.67x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 104 ms: 1.71x slower                                                    |
| thrift                     | 937 us                                                                | 1.65 ms: 1.76x slower                                                   |
| pyflate                    | 559 ms                                                                | 1.01 sec: 1.81x slower                                                  |
| spectral_norm              | 131 ms                                                                | 239 ms: 1.83x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 231 ms: 1.84x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 332 us: 1.84x slower                                                    |
| regex_compile              | 137 ms                                                                | 254 ms: 1.85x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 121 ms: 1.86x slower                                                    |
| sympy_str                  | 280 ms                                                                | 520 ms: 1.86x slower                                                    |
| logging_format             | 8.34 us                                                               | 15.7 us: 1.88x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.74 sec: 1.90x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 52.2 ms: 1.90x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 3.59 sec: 1.91x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 117 ms: 1.91x slower                                                    |
| logging_simple             | 7.63 us                                                               | 14.7 us: 1.92x slower                                                   |
| django_template            | 40.7 ms                                                               | 81.3 ms: 2.00x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 172 ms: 2.02x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 317 ms: 2.05x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 538 us: 2.07x slower                                                    |
| sympy_expand               | 454 ms                                                                | 953 ms: 2.10x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 773 us: 2.12x slower                                                    |
| logging_silent             | 127 ns                                                                | 281 ns: 2.22x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 15.6 ms: 2.23x slower                                                   |
| mako                       | 12.9 ms                                                               | 28.9 ms: 2.24x slower                                                   |
| chaos                      | 71.4 ms                                                               | 161 ms: 2.25x slower                                                    |
| float                      | 92.1 ms                                                               | 209 ms: 2.27x slower                                                    |
| scimark_sor                | 150 ms                                                                | 341 ms: 2.28x slower                                                    |
| richards                   | 50.9 ms                                                               | 117 ms: 2.29x slower                                                    |
| richards_super             | 58.5 ms                                                               | 137 ms: 2.34x slower                                                    |
| raytrace                   | 353 ms                                                                | 829 ms: 2.35x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 348 ms: 2.39x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.41 ms: 2.41x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 3.83 ms: 2.62x slower                                                   |
| nbody                      | 105 ms                                                                | 290 ms: 2.77x slower                                                    |
| go                         | 157 ms                                                                | 446 ms: 2.83x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.7 ms: 3.09x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.55x slower                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, regex_dna
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.43x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.37x

# Memory
- memory change: 1.07x