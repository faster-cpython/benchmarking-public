# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.55x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.39x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 516 ms: 1.68x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.15 sec: 1.39x slower                                                  |
| html5lib       | 65.1 ms                                                               | 121 ms: 1.87x slower                                                    |
| tornado_http   | 136 ms                                                                | 200 ms: 1.48x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.59x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 696 ms: 1.06x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.35 sec: 1.04x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 566 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 871 ms: 1.01x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 767 ms: 1.01x faster                                                    |
| async_tree_none            | 624 ms                                                                | 631 ms: 1.01x slower                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.44 sec: 1.02x slower                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 942 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 207 ms: 2.25x slower                                                    |
| nbody          | 105 ms                                                                | 285 ms: 2.72x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.84x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.41 ms: 1.05x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                                   |
| regex_compile  | 137 ms                                                                | 256 ms: 1.86x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 177 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 155 ms: 1.03x slower                                                    |
| json_loads           | 30.7 us                                                               | 39.1 us: 1.27x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 162 ms: 1.45x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.9 ms: 1.46x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.19 sec: 1.62x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 130 ms: 1.65x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 550 us: 2.11x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 781 us: 2.14x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.46x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.7 ms: 1.40x slower                                                   |
| python_startup         | 11.4 ms                                                               | 17.6 ms: 1.54x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 105 ms: 1.73x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 52.8 ms: 1.92x slower                                                   |
| django_template | 40.7 ms                                                               | 82.3 ms: 2.02x slower                                                   |
| mako            | 12.9 ms                                                               | 29.1 ms: 2.25x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.97x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.45 ms: 1.27x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.60 ms: 1.20x faster                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 6.14 ms: 1.15x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 177 ms: 1.10x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 696 ms: 1.06x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.41 ms: 1.05x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.35 sec: 1.04x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 566 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 871 ms: 1.01x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 767 ms: 1.01x faster                                                    |
| async_tree_none            | 624 ms                                                                | 631 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.44 sec: 1.02x slower                                                  |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 155 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 942 ms: 1.03x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 26.0 ms: 1.06x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.46 sec: 1.13x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 660 ms: 1.17x slower                                                    |
| json                       | 5.54 ms                                                               | 6.96 ms: 1.26x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.33 sec: 1.27x slower                                                  |
| deepcopy                   | 446 us                                                                | 566 us: 1.27x slower                                                    |
| json_loads                 | 30.7 us                                                               | 39.1 us: 1.27x slower                                                   |
| generators                 | 43.5 ms                                                               | 57.0 ms: 1.31x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 39.0 ms: 1.34x slower                                                   |
| docutils                   | 2.98 sec                                                              | 4.15 sec: 1.39x slower                                                  |
| python_startup_no_site     | 8.37 ms                                                               | 11.7 ms: 1.40x slower                                                   |
| async_generators           | 491 ms                                                                | 692 ms: 1.41x slower                                                    |
| scimark_fft                | 418 ms                                                                | 593 ms: 1.42x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.82 ms: 1.42x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.87 ms: 1.43x slower                                                   |
| pylint                     | 355 ms                                                                | 508 ms: 1.43x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 162 ms: 1.45x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 71.9 us: 1.45x slower                                                   |
| telco                      | 8.51 ms                                                               | 12.4 ms: 1.45x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 17.9 ms: 1.46x slower                                                   |
| tornado_http               | 136 ms                                                                | 200 ms: 1.48x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 6.07 us: 1.48x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 152 ms: 1.53x slower                                                    |
| meteor_contest             | 112 ms                                                                | 173 ms: 1.54x slower                                                    |
| python_startup             | 11.4 ms                                                               | 17.6 ms: 1.54x slower                                                   |
| coverage                   | 87.3 ms                                                               | 135 ms: 1.55x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 4.19 sec: 1.62x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 34.9 ms: 1.62x slower                                                   |
| comprehensions             | 25.4 us                                                               | 41.3 us: 1.63x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 141 ms: 1.63x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 2.06 sec: 1.64x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 130 ms: 1.65x slower                                                    |
| 2to3                       | 308 ms                                                                | 516 ms: 1.68x slower                                                    |
| fannkuch                   | 443 ms                                                                | 758 ms: 1.71x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 105 ms: 1.73x slower                                                    |
| spectral_norm              | 131 ms                                                                | 233 ms: 1.78x slower                                                    |
| thrift                     | 937 us                                                                | 1.69 ms: 1.81x slower                                                   |
| pyflate                    | 559 ms                                                                | 1.02 sec: 1.83x slower                                                  |
| sqlglot_normalize          | 126 ms                                                                | 231 ms: 1.84x slower                                                    |
| sympy_str                  | 280 ms                                                                | 514 ms: 1.84x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 334 us: 1.85x slower                                                    |
| regex_compile              | 137 ms                                                                | 256 ms: 1.86x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 114 ms: 1.87x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 121 ms: 1.87x slower                                                    |
| logging_format             | 8.34 us                                                               | 15.8 us: 1.89x slower                                                   |
| logging_simple             | 7.63 us                                                               | 14.7 us: 1.92x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 52.8 ms: 1.92x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 3.64 sec: 1.93x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.77 sec: 1.94x slower                                                  |
| django_template            | 40.7 ms                                                               | 82.3 ms: 2.02x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 313 ms: 2.03x slower                                                    |
| sympy_expand               | 454 ms                                                                | 951 ms: 2.10x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 179 ms: 2.11x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 550 us: 2.11x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 781 us: 2.14x slower                                                    |
| logging_silent             | 127 ns                                                                | 285 ns: 2.25x slower                                                    |
| mako                       | 12.9 ms                                                               | 29.1 ms: 2.25x slower                                                   |
| float                      | 92.1 ms                                                               | 207 ms: 2.25x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 15.8 ms: 2.26x slower                                                   |
| chaos                      | 71.4 ms                                                               | 162 ms: 2.27x slower                                                    |
| scimark_sor                | 150 ms                                                                | 345 ms: 2.30x slower                                                    |
| raytrace                   | 353 ms                                                                | 826 ms: 2.34x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.29 ms: 2.35x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 343 ms: 2.36x slower                                                    |
| richards_super             | 58.5 ms                                                               | 139 ms: 2.38x slower                                                    |
| richards                   | 50.9 ms                                                               | 121 ms: 2.38x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.70 ms: 2.53x slower                                                   |
| nbody                      | 105 ms                                                                | 285 ms: 2.72x slower                                                    |
| go                         | 157 ms                                                                | 448 ms: 2.85x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.8 ms: 3.12x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.55x slower                                                            |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.46x
- 95% likely to have a slowdown of 1.43x
- 99% likely to have a slowdown of 1.39x

# Memory
- memory change: 1.07x