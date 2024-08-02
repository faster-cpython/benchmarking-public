# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-aarch64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.04x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 363 ms: 1.18x slower                                                       |
| docutils       | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                                     |
| html5lib       | 65.1 ms                                                               | 69.4 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 411 ms: 1.40x faster                                                       |
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 537 ms: 1.38x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.33x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.26x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 740 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 724 ms: 1.22x faster                                                       |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.1 ms: 1.02x faster                                                      |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                       |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 257 ms: 1.01x slower                                                       |
| regex_effbot   | 4.64 ms                                                               | 4.99 ms: 1.08x slower                                                      |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                      |
| regex_compile  | 137 ms                                                                | 173 ms: 1.26x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                     |
| json_loads         | 30.7 us                                                               | 32.9 us: 1.07x slower                                                      |
| pickle_pure_python | 365 us                                                                | 393 us: 1.08x slower                                                       |
| json_dumps         | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                      |
| Geometric mean     | (ref)                                                                 | 1.03x slower                                                               |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_iterparse, unpickle_pure_python, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                                      |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                      |
| genshi_text     | 27.4 ms                                                               | 32.6 ms: 1.19x slower                                                      |
| django_template | 40.7 ms                                                               | 50.0 ms: 1.23x slower                                                      |
| genshi_xml      | 60.6 ms                                                               | 75.7 ms: 1.25x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 411 ms: 1.40x faster                                                       |
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 537 ms: 1.38x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.33x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 38.4 us: 1.29x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.26x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 740 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 724 ms: 1.22x faster                                                       |
| deepcopy                   | 446 us                                                                | 377 us: 1.18x faster                                                       |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                      |
| generators                 | 43.5 ms                                                               | 39.2 ms: 1.11x faster                                                      |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                       |
| comprehensions             | 25.4 us                                                               | 23.4 us: 1.09x faster                                                      |
| logging_simple             | 7.63 us                                                               | 7.24 us: 1.05x faster                                                      |
| logging_format             | 8.34 us                                                               | 7.94 us: 1.05x faster                                                      |
| float                      | 92.1 ms                                                               | 90.1 ms: 1.02x faster                                                      |
| tomli_loads                | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                     |
| richards_super             | 58.5 ms                                                               | 58.7 ms: 1.00x slower                                                      |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                       |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                       |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                      |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 85.1 ms                                                               | 85.8 ms: 1.01x slower                                                      |
| richards                   | 50.9 ms                                                               | 51.4 ms: 1.01x slower                                                      |
| regex_dna                  | 254 ms                                                                | 257 ms: 1.01x slower                                                       |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.02x slower                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 4.19 us: 1.02x slower                                                      |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.02x slower                                                       |
| coroutines                 | 29.0 ms                                                               | 29.9 ms: 1.03x slower                                                      |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                     |
| thrift                     | 937 us                                                                | 966 us: 1.03x slower                                                       |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                      |
| dask                       | 376 ms                                                                | 392 ms: 1.04x slower                                                       |
| async_generators           | 491 ms                                                                | 515 ms: 1.05x slower                                                       |
| fannkuch                   | 443 ms                                                                | 468 ms: 1.06x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                                      |
| html5lib                   | 65.1 ms                                                               | 69.4 ms: 1.07x slower                                                      |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                      |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                       |
| regex_effbot               | 4.64 ms                                                               | 4.99 ms: 1.08x slower                                                      |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                                       |
| asyncio_tcp                | 566 ms                                                                | 610 ms: 1.08x slower                                                       |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.09x slower                                                      |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                      |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                      |
| sqlglot_transpile          | 1.83 ms                                                               | 2.00 ms: 1.09x slower                                                      |
| pyflate                    | 559 ms                                                                | 612 ms: 1.10x slower                                                       |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                       |
| scimark_fft                | 418 ms                                                                | 462 ms: 1.10x slower                                                       |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.91 ms: 1.12x slower                                                      |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 61.3 ms                                                               | 69.2 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                       |
| go                         | 157 ms                                                                | 178 ms: 1.13x slower                                                       |
| dulwich_log                | 62.0 ms                                                               | 70.6 ms: 1.14x slower                                                      |
| deltablue                  | 4.12 ms                                                               | 4.70 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 181 us                                                                | 208 us: 1.15x slower                                                       |
| gc_traversal               | 4.40 ms                                                               | 5.06 ms: 1.15x slower                                                      |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                      |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                       |
| sympy_str                  | 280 ms                                                                | 324 ms: 1.16x slower                                                       |
| scimark_sor                | 150 ms                                                                | 175 ms: 1.17x slower                                                       |
| 2to3                       | 308 ms                                                                | 363 ms: 1.18x slower                                                       |
| pylint                     | 355 ms                                                                | 418 ms: 1.18x slower                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 8.33 ms: 1.18x slower                                                      |
| genshi_text                | 27.4 ms                                                               | 32.6 ms: 1.19x slower                                                      |
| docutils                   | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 118 ms: 1.19x slower                                                       |
| sympy_sum                  | 154 ms                                                                | 184 ms: 1.19x slower                                                       |
| sympy_expand               | 454 ms                                                                | 547 ms: 1.21x slower                                                       |
| sympy_integrate            | 21.6 ms                                                               | 26.2 ms: 1.21x slower                                                      |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                                     |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.22x slower                                                      |
| chaos                      | 71.4 ms                                                               | 87.0 ms: 1.22x slower                                                      |
| create_gc_cycles           | 1.92 ms                                                               | 2.34 ms: 1.22x slower                                                      |
| django_template            | 40.7 ms                                                               | 50.0 ms: 1.23x slower                                                      |
| pprint_pformat             | 1.88 sec                                                              | 2.32 sec: 1.23x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 75.7 ms: 1.25x slower                                                      |
| regex_compile              | 137 ms                                                                | 173 ms: 1.26x slower                                                       |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.26x slower                                                       |
| hexiom                     | 6.98 ms                                                               | 9.17 ms: 1.31x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                               |

Benchmark hidden because not significant (7): xml_etree_parse, xml_etree_iterparse, tornado_http, crypto_pyaes, unpickle_pure_python, xml_etree_process, xml_etree_generate
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: bpe_tokeniser

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.03x