# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-aarch64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.252x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 463 ms: 1.50x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                 |
| html5lib       | 65.1 ms                                                               | 108 ms: 1.66x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.46x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.23x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 616 ms: 1.20x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.20x faster                                                 |
| async_tree_memoization     | 777 ms                                                                | 655 ms: 1.19x faster                                                   |
| async_tree_none            | 624 ms                                                                | 540 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 505 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 802 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 833 ms: 1.09x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.16x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 154 ms: 1.67x slower                                                   |
| nbody          | 105 ms                                                                | 182 ms: 1.74x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.45x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.15 ms: 1.12x faster                                                  |
| regex_dna      | 254 ms                                                                | 274 ms: 1.08x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 33.3 ms: 1.17x slower                                                  |
| regex_compile  | 137 ms                                                                | 191 ms: 1.39x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 135 ms: 1.11x faster                                                   |
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                   |
| json_loads           | 30.7 us                                                               | 36.0 us: 1.17x slower                                                  |
| xml_etree_generate   | 112 ms                                                                | 143 ms: 1.28x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 3.56 sec: 1.37x slower                                                 |
| xml_etree_process    | 79.0 ms                                                               | 111 ms: 1.40x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 18.1 ms: 1.48x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 455 us: 1.75x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 702 us: 1.92x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.32x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.5 ms: 1.49x slower                                                  |
| python_startup         | 11.4 ms                                                               | 20.4 ms: 1.80x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.64x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 81.2 ms: 1.34x slower                                                  |
| genshi_text     | 27.4 ms                                                               | 40.5 ms: 1.48x slower                                                  |
| django_template | 40.7 ms                                                               | 66.8 ms: 1.64x slower                                                  |
| mako            | 12.9 ms                                                               | 25.2 ms: 1.96x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.59x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.23x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 616 ms: 1.20x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.20x faster                                                 |
| async_tree_memoization     | 777 ms                                                                | 655 ms: 1.19x faster                                                   |
| async_tree_none            | 624 ms                                                                | 540 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 505 ms: 1.14x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.15 ms: 1.12x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 135 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 802 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 833 ms: 1.09x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 688 ms: 1.05x slower                                                   |
| regex_dna                  | 254 ms                                                                | 274 ms: 1.08x slower                                                   |
| json                       | 5.54 ms                                                               | 6.23 ms: 1.13x slower                                                  |
| deepcopy_memo              | 49.6 us                                                               | 56.9 us: 1.15x slower                                                  |
| coroutines                 | 29.0 ms                                                               | 33.5 ms: 1.15x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 5.09 ms: 1.16x slower                                                  |
| json_loads                 | 30.7 us                                                               | 36.0 us: 1.17x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 33.3 ms: 1.17x slower                                                  |
| mdp                        | 3.41 sec                                                              | 4.03 sec: 1.18x slower                                                 |
| spectral_norm              | 131 ms                                                                | 156 ms: 1.19x slower                                                   |
| scimark_fft                | 418 ms                                                                | 500 ms: 1.20x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.90 us: 1.20x slower                                                  |
| pylint                     | 355 ms                                                                | 442 ms: 1.25x slower                                                   |
| async_generators           | 491 ms                                                                | 614 ms: 1.25x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                 |
| xml_etree_generate         | 112 ms                                                                | 143 ms: 1.28x slower                                                   |
| generators                 | 43.5 ms                                                               | 55.9 ms: 1.28x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.15 ms: 1.32x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 81.2 ms: 1.34x slower                                                  |
| sympy_sum                  | 154 ms                                                                | 210 ms: 1.36x slower                                                   |
| sympy_str                  | 280 ms                                                                | 381 ms: 1.36x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.71 sec: 1.37x slower                                                 |
| tomli_loads                | 2.59 sec                                                              | 3.56 sec: 1.37x slower                                                 |
| nqueens                    | 99.2 ms                                                               | 136 ms: 1.37x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 29.8 ms: 1.38x slower                                                  |
| regex_compile              | 137 ms                                                                | 191 ms: 1.39x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 121 ms: 1.39x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 111 ms: 1.40x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 176 ms: 1.40x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 87.1 ms: 1.40x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 86.6 ms: 1.41x slower                                                  |
| meteor_contest             | 112 ms                                                                | 160 ms: 1.43x slower                                                   |
| telco                      | 8.51 ms                                                               | 12.3 ms: 1.45x slower                                                  |
| logging_simple             | 7.63 us                                                               | 11.1 us: 1.46x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.34 sec: 1.47x slower                                                 |
| pprint_pformat             | 1.88 sec                                                              | 2.76 sec: 1.47x slower                                                 |
| genshi_text                | 27.4 ms                                                               | 40.5 ms: 1.48x slower                                                  |
| logging_format             | 8.34 us                                                               | 12.3 us: 1.48x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 18.1 ms: 1.48x slower                                                  |
| thrift                     | 937 us                                                                | 1.39 ms: 1.48x slower                                                  |
| sympy_expand               | 454 ms                                                                | 674 ms: 1.49x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 12.5 ms: 1.49x slower                                                  |
| comprehensions             | 25.4 us                                                               | 38.1 us: 1.50x slower                                                  |
| 2to3                       | 308 ms                                                                | 463 ms: 1.50x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 221 ms: 1.52x slower                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 241 ms: 1.53x slower                                                   |
| sqlalchemy_imperative      | 16.7 ms                                                               | 26.1 ms: 1.56x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 3.01 ms: 1.57x slower                                                  |
| fannkuch                   | 443 ms                                                                | 695 ms: 1.57x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 2.07 ms: 1.58x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 288 us: 1.59x slower                                                   |
| pyflate                    | 559 ms                                                                | 901 ms: 1.61x slower                                                   |
| django_template            | 40.7 ms                                                               | 66.8 ms: 1.64x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 108 ms: 1.66x slower                                                   |
| coverage                   | 87.3 ms                                                               | 145 ms: 1.66x slower                                                   |
| float                      | 92.1 ms                                                               | 154 ms: 1.67x slower                                                   |
| mypy2                      | 873 ms                                                                | 1.48 sec: 1.70x slower                                                 |
| nbody                      | 105 ms                                                                | 182 ms: 1.74x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 455 us: 1.75x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 151 ms: 1.77x slower                                                   |
| chaos                      | 71.4 ms                                                               | 127 ms: 1.78x slower                                                   |
| python_startup             | 11.4 ms                                                               | 20.4 ms: 1.80x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 12.8 ms: 1.84x slower                                                  |
| richards_super             | 58.5 ms                                                               | 109 ms: 1.86x slower                                                   |
| raytrace                   | 353 ms                                                                | 658 ms: 1.86x slower                                                   |
| richards                   | 50.9 ms                                                               | 97.7 ms: 1.92x slower                                                  |
| pickle_pure_python         | 365 us                                                                | 702 us: 1.92x slower                                                   |
| scimark_sor                | 150 ms                                                                | 289 ms: 1.93x slower                                                   |
| mako                       | 12.9 ms                                                               | 25.2 ms: 1.96x slower                                                  |
| sqlglot_transpile          | 1.83 ms                                                               | 3.64 ms: 1.99x slower                                                  |
| logging_silent             | 127 ns                                                                | 255 ns: 2.01x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 3.10 ms: 2.12x slower                                                  |
| go                         | 157 ms                                                                | 341 ms: 2.17x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 11.0 ms: 2.67x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 61.1 ms: 8.66x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.40x slower                                                           |

Benchmark hidden because not significant (4): pathlib, deepcopy, sqlite_synth, pidigits
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.252x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.28x
- 95% likely to have a slowdown of 1.26x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 1.24x