# Results vs. 3.12.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.57x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 522 ms: 1.69x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.12 sec: 1.38x slower                                                  |
| html5lib       | 65.1 ms                                                               | 123 ms: 1.89x slower                                                    |
| tornado_http   | 136 ms                                                                | 209 ms: 1.54x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.62x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 695 ms: 1.06x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 743 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.35 sec: 1.04x faster                                                  |
| async_tree_none            | 624 ms                                                                | 612 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 868 ms: 1.02x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.39 sec: 1.01x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 571 ms: 1.01x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 209 ms: 2.27x slower                                                    |
| nbody          | 105 ms                                                                | 285 ms: 2.73x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.84x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.47 ms: 1.04x faster                                                   |
| regex_dna      | 254 ms                                                                | 256 ms: 1.01x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                   |
| regex_compile  | 137 ms                                                                | 258 ms: 1.88x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| json_loads           | 30.7 us                                                               | 38.9 us: 1.27x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 163 ms: 1.45x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 18.2 ms: 1.49x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.28 sec: 1.65x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 131 ms: 1.66x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 546 us: 2.10x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 787 us: 2.16x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.48x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                   |
| python_startup         | 11.4 ms                                                               | 18.1 ms: 1.59x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.52x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 109 ms: 1.80x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 55.1 ms: 2.01x slower                                                   |
| django_template | 40.7 ms                                                               | 84.1 ms: 2.07x slower                                                   |
| mako            | 12.9 ms                                                               | 28.9 ms: 2.24x slower                                                   |
| Geometric mean  | (ref)                                                                 | 2.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.51 ms: 1.25x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.62 ms: 1.18x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 695 ms: 1.06x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 743 ms: 1.05x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.47 ms: 1.04x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.35 sec: 1.04x faster                                                  |
| async_tree_none            | 624 ms                                                                | 612 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 868 ms: 1.02x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.39 sec: 1.01x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 571 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| regex_dna                  | 254 ms                                                                | 256 ms: 1.01x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.16 ms: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 26.6 ms: 1.08x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.47 sec: 1.13x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 672 ms: 1.19x slower                                                    |
| deepcopy                   | 446 us                                                                | 564 us: 1.27x slower                                                    |
| json_loads                 | 30.7 us                                                               | 38.9 us: 1.27x slower                                                   |
| json                       | 5.54 ms                                                               | 7.04 ms: 1.27x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.34 sec: 1.27x slower                                                  |
| generators                 | 43.5 ms                                                               | 57.2 ms: 1.31x slower                                                   |
| async_generators           | 491 ms                                                                | 670 ms: 1.37x slower                                                    |
| docutils                   | 2.98 sec                                                              | 4.12 sec: 1.38x slower                                                  |
| scimark_fft                | 418 ms                                                                | 582 ms: 1.39x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 41.1 ms: 1.42x slower                                                   |
| pylint                     | 355 ms                                                                | 509 ms: 1.43x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.96 ms: 1.45x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 163 ms: 1.45x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 73.0 us: 1.47x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 18.2 ms: 1.49x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 6.10 us: 1.49x slower                                                   |
| meteor_contest             | 112 ms                                                                | 168 ms: 1.50x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 152 ms: 1.53x slower                                                    |
| telco                      | 8.51 ms                                                               | 13.1 ms: 1.54x slower                                                   |
| tornado_http               | 136 ms                                                                | 209 ms: 1.54x slower                                                    |
| coverage                   | 87.3 ms                                                               | 138 ms: 1.58x slower                                                    |
| python_startup             | 11.4 ms                                                               | 18.1 ms: 1.59x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 139 ms: 1.60x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 2.11 ms: 1.62x slower                                                   |
| comprehensions             | 25.4 us                                                               | 41.2 us: 1.62x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 35.2 ms: 1.63x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 2.06 sec: 1.64x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 4.28 sec: 1.65x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 131 ms: 1.66x slower                                                    |
| fannkuch                   | 443 ms                                                                | 746 ms: 1.68x slower                                                    |
| 2to3                       | 308 ms                                                                | 522 ms: 1.69x slower                                                    |
| spectral_norm              | 131 ms                                                                | 231 ms: 1.76x slower                                                    |
| thrift                     | 937 us                                                                | 1.67 ms: 1.78x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 109 ms: 1.80x slower                                                    |
| pyflate                    | 559 ms                                                                | 1.01 sec: 1.81x slower                                                  |
| sqlglot_normalize          | 126 ms                                                                | 232 ms: 1.85x slower                                                    |
| logging_format             | 8.34 us                                                               | 15.6 us: 1.87x slower                                                   |
| sympy_str                  | 280 ms                                                                | 523 ms: 1.87x slower                                                    |
| regex_compile              | 137 ms                                                                | 258 ms: 1.88x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 123 ms: 1.89x slower                                                    |
| logging_simple             | 7.63 us                                                               | 14.5 us: 1.90x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 344 us: 1.91x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 117 ms: 1.91x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.78 sec: 1.94x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 3.66 sec: 1.95x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 55.1 ms: 2.01x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 318 ms: 2.06x slower                                                    |
| django_template            | 40.7 ms                                                               | 84.1 ms: 2.07x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 546 us: 2.10x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 180 ms: 2.12x slower                                                    |
| sympy_expand               | 454 ms                                                                | 971 ms: 2.14x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 787 us: 2.16x slower                                                    |
| chaos                      | 71.4 ms                                                               | 160 ms: 2.24x slower                                                    |
| mako                       | 12.9 ms                                                               | 28.9 ms: 2.24x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 15.7 ms: 2.25x slower                                                   |
| float                      | 92.1 ms                                                               | 209 ms: 2.27x slower                                                    |
| scimark_sor                | 150 ms                                                                | 342 ms: 2.28x slower                                                    |
| logging_silent             | 127 ns                                                                | 291 ns: 2.30x slower                                                    |
| richards                   | 50.9 ms                                                               | 117 ms: 2.30x slower                                                    |
| raytrace                   | 353 ms                                                                | 820 ms: 2.32x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.37 ms: 2.39x slower                                                   |
| richards_super             | 58.5 ms                                                               | 141 ms: 2.40x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 351 ms: 2.41x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.72 ms: 2.54x slower                                                   |
| nbody                      | 105 ms                                                                | 285 ms: 2.73x slower                                                    |
| go                         | 157 ms                                                                | 447 ms: 2.84x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.7 ms: 3.09x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.57x slower                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.07x