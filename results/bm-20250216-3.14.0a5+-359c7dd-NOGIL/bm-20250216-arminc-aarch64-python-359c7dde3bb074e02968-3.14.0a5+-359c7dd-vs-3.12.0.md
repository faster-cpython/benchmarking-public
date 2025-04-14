# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.117x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 377 ms: 1.22x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.32 sec: 1.11x slower                                                   |
| html5lib       | 65.1 ms                                                               | 75.3 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 925 ms: 1.52x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 499 ms: 1.48x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 974 ms: 1.45x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 549 ms: 1.42x faster                                                     |
| async_tree_none            | 624 ms                                                                | 452 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 690 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.26x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.39x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 101 ms: 1.10x slower                                                     |
| nbody          | 105 ms                                                                | 185 ms: 1.77x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.00 ms: 1.16x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                                    |
| regex_compile  | 137 ms                                                                | 165 ms: 1.20x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 130 ms: 1.16x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 41.0 us: 1.10x slower                                                    |
| unpickle             | 18.5 us                                                               | 21.0 us: 1.14x slower                                                    |
| pickle_list          | 5.25 us                                                               | 6.13 us: 1.17x slower                                                    |
| pickle               | 13.4 us                                                               | 15.8 us: 1.18x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 7.42 us: 1.20x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 319 us: 1.23x slower                                                     |
| xml_etree_generate   | 112 ms                                                                | 139 ms: 1.24x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.23 sec: 1.25x slower                                                   |
| json_loads           | 30.7 us                                                               | 38.4 us: 1.25x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 460 us: 1.26x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 101 ms: 1.28x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 17.1 ms: 1.40x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.61x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 78.7 ms: 1.30x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 36.8 ms: 1.34x slower                                                    |
| django_template | 40.7 ms                                                               | 54.6 ms: 1.34x slower                                                    |
| mako            | 12.9 ms                                                               | 22.4 ms: 1.73x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.42x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 2.78 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 925 ms: 1.52x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 499 ms: 1.48x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 974 ms: 1.45x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 549 ms: 1.42x faster                                                     |
| async_tree_none            | 624 ms                                                                | 452 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 690 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.26x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.00 ms: 1.16x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 130 ms: 1.16x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| deepcopy                   | 446 us                                                                | 423 us: 1.05x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 51.6 us: 1.04x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 687 ms: 1.04x slower                                                     |
| comprehensions             | 25.4 us                                                               | 27.0 us: 1.06x slower                                                    |
| pylint                     | 355 ms                                                                | 382 ms: 1.08x slower                                                     |
| async_generators           | 491 ms                                                                | 530 ms: 1.08x slower                                                     |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                                     |
| asyncio_tcp                | 566 ms                                                                | 619 ms: 1.09x slower                                                     |
| float                      | 92.1 ms                                                               | 101 ms: 1.10x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 41.0 us: 1.10x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 31.9 ms: 1.10x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.51 us: 1.10x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.32 sec: 1.11x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.86 sec: 1.13x slower                                                   |
| go                         | 157 ms                                                                | 178 ms: 1.13x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 70.4 ms: 1.14x slower                                                    |
| unpickle                   | 18.5 us                                                               | 21.0 us: 1.14x slower                                                    |
| logging_simple             | 7.63 us                                                               | 8.75 us: 1.15x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.44 sec: 1.15x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 75.3 ms: 1.16x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.22 ms: 1.16x slower                                                    |
| scimark_fft                | 418 ms                                                                | 487 ms: 1.16x slower                                                     |
| pickle_list                | 5.25 us                                                               | 6.13 us: 1.17x slower                                                    |
| json                       | 5.54 ms                                                               | 6.50 ms: 1.17x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.57 sec: 1.17x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.8 us: 1.18x slower                                                    |
| scimark_sor                | 150 ms                                                                | 178 ms: 1.19x slower                                                     |
| logging_format             | 8.34 us                                                               | 9.96 us: 1.19x slower                                                    |
| raytrace                   | 353 ms                                                                | 423 ms: 1.20x slower                                                     |
| pyflate                    | 559 ms                                                                | 671 ms: 1.20x slower                                                     |
| regex_compile              | 137 ms                                                                | 165 ms: 1.20x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 7.42 us: 1.20x slower                                                    |
| 2to3                       | 308 ms                                                                | 377 ms: 1.22x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 319 us: 1.23x slower                                                     |
| logging_silent             | 127 ns                                                                | 156 ns: 1.23x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 155 ms: 1.23x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 139 ms: 1.24x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 196 ms: 1.25x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 3.23 sec: 1.25x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 76.5 ms: 1.25x slower                                                    |
| json_loads                 | 30.7 us                                                               | 38.4 us: 1.25x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 194 ms: 1.25x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 460 us: 1.26x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.37 sec: 1.26x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.26x slower                                                   |
| chaos                      | 71.4 ms                                                               | 90.0 ms: 1.26x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 101 ms: 1.28x slower                                                     |
| sympy_str                  | 280 ms                                                                | 359 ms: 1.28x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 5.29 ms: 1.28x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.06 ms: 1.30x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 78.7 ms: 1.30x slower                                                    |
| thrift                     | 937 us                                                                | 1.22 ms: 1.31x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 193 ms: 1.33x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.22 ms: 1.33x slower                                                    |
| sympy_expand               | 454 ms                                                                | 605 ms: 1.33x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 22.2 ms: 1.33x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 133 ms: 1.34x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 29.0 ms: 1.34x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 36.8 ms: 1.34x slower                                                    |
| django_template            | 40.7 ms                                                               | 54.6 ms: 1.34x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.45 ms: 1.34x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.98 ms: 1.35x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 117 ms: 1.35x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 116 ms: 1.36x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 17.1 ms: 1.40x slower                                                    |
| richards                   | 50.9 ms                                                               | 71.5 ms: 1.40x slower                                                    |
| meteor_contest             | 112 ms                                                                | 157 ms: 1.41x slower                                                     |
| telco                      | 8.51 ms                                                               | 12.0 ms: 1.42x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.87 ms: 1.43x slower                                                    |
| coverage                   | 87.3 ms                                                               | 127 ms: 1.45x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                    |
| richards_super             | 58.5 ms                                                               | 87.4 ms: 1.49x slower                                                    |
| fannkuch                   | 443 ms                                                                | 681 ms: 1.54x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 287 us: 1.59x slower                                                     |
| mako                       | 12.9 ms                                                               | 22.4 ms: 1.73x slower                                                    |
| nbody                      | 105 ms                                                                | 185 ms: 1.77x slower                                                     |
| python_startup             | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 58.8 ms: 8.34x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.18x slower                                                             |

Benchmark hidden because not significant (5): pathlib, generators, sqlite_synth, regex_dna, pidigits
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.117x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.26x