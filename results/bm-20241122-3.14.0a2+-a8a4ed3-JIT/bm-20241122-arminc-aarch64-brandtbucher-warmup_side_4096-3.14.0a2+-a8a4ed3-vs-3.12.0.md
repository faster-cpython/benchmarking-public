# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-aarch64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.044x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.24 sec: 1.09x slower                                                     |
| html5lib       | 65.1 ms                                                               | 72.3 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 469 ms: 1.33x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 598 ms: 1.30x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 573 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 481 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 766 ms: 1.19x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 779 ms: 1.13x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.11x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                                       |
| float          | 92.1 ms                                                               | 98.4 ms: 1.07x slower                                                      |
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.22 ms: 1.10x faster                                                      |
| regex_dna      | 254 ms                                                                | 270 ms: 1.06x slower                                                       |
| regex_v8       | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                     |
| json_loads         | 30.7 us                                                               | 32.3 us: 1.05x slower                                                      |
| pickle_pure_python | 365 us                                                                | 392 us: 1.07x slower                                                       |
| json_dumps         | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                      |
| Geometric mean     | (ref)                                                                 | 1.04x slower                                                               |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, xml_etree_iterparse, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.89 ms: 1.06x slower                                                      |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                      |
| genshi_text     | 27.4 ms                                                               | 32.7 ms: 1.19x slower                                                      |
| django_template | 40.7 ms                                                               | 48.7 ms: 1.20x slower                                                      |
| genshi_xml      | 60.6 ms                                                               | 81.0 ms: 1.34x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.19x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 469 ms: 1.33x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 598 ms: 1.30x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 573 ms: 1.29x faster                                                       |
| deepcopy_memo              | 49.6 us                                                               | 41.0 us: 1.21x faster                                                      |
| async_tree_none_tg         | 577 ms                                                                | 481 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 766 ms: 1.19x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 779 ms: 1.13x faster                                                       |
| deepcopy                   | 446 us                                                                | 397 us: 1.12x faster                                                       |
| pylint                     | 355 ms                                                                | 318 ms: 1.11x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.11x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.3 ms: 1.10x faster                                                      |
| regex_effbot               | 4.64 ms                                                               | 4.22 ms: 1.10x faster                                                      |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.06x faster                                                       |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                     |
| logging_format             | 8.34 us                                                               | 8.52 us: 1.02x slower                                                      |
| crypto_pyaes               | 86.6 ms                                                               | 88.7 ms: 1.02x slower                                                      |
| sympy_sum                  | 154 ms                                                                | 159 ms: 1.03x slower                                                       |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                                       |
| mdp                        | 3.41 sec                                                              | 3.56 sec: 1.04x slower                                                     |
| logging_simple             | 7.63 us                                                               | 7.97 us: 1.04x slower                                                      |
| scimark_lu                 | 146 ms                                                                | 153 ms: 1.05x slower                                                       |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                      |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                      |
| json                       | 5.54 ms                                                               | 5.84 ms: 1.05x slower                                                      |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                      |
| thrift                     | 937 us                                                                | 994 us: 1.06x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 8.89 ms: 1.06x slower                                                      |
| regex_dna                  | 254 ms                                                                | 270 ms: 1.06x slower                                                       |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                                       |
| float                      | 92.1 ms                                                               | 98.4 ms: 1.07x slower                                                      |
| sympy_str                  | 280 ms                                                                | 300 ms: 1.07x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                       |
| pyflate                    | 559 ms                                                                | 603 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.83 ms                                                               | 1.98 ms: 1.08x slower                                                      |
| scimark_fft                | 418 ms                                                                | 454 ms: 1.08x slower                                                       |
| docutils                   | 2.98 sec                                                              | 3.24 sec: 1.09x slower                                                     |
| async_generators           | 491 ms                                                                | 539 ms: 1.10x slower                                                       |
| sqlglot_parse              | 1.46 ms                                                               | 1.61 ms: 1.10x slower                                                      |
| sqlite_synth               | 3.77 us                                                               | 4.16 us: 1.10x slower                                                      |
| richards                   | 50.9 ms                                                               | 56.4 ms: 1.11x slower                                                      |
| logging_silent             | 127 ns                                                                | 141 ns: 1.11x slower                                                       |
| sympy_integrate            | 21.6 ms                                                               | 24.0 ms: 1.11x slower                                                      |
| html5lib                   | 65.1 ms                                                               | 72.3 ms: 1.11x slower                                                      |
| fannkuch                   | 443 ms                                                                | 494 ms: 1.11x slower                                                       |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                                       |
| meteor_contest             | 112 ms                                                                | 126 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 126 ms                                                                | 141 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 61.3 ms                                                               | 69.3 ms: 1.13x slower                                                      |
| telco                      | 8.51 ms                                                               | 9.64 ms: 1.13x slower                                                      |
| sympy_expand               | 454 ms                                                                | 516 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.11 ms: 1.15x slower                                                      |
| generators                 | 43.5 ms                                                               | 50.4 ms: 1.16x slower                                                      |
| pycparser                  | 1.26 sec                                                              | 1.46 sec: 1.16x slower                                                     |
| go                         | 157 ms                                                                | 183 ms: 1.16x slower                                                       |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                       |
| regex_v8                   | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                      |
| spectral_norm              | 131 ms                                                                | 154 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 181 us                                                                | 214 us: 1.18x slower                                                       |
| genshi_text                | 27.4 ms                                                               | 32.7 ms: 1.19x slower                                                      |
| chaos                      | 71.4 ms                                                               | 85.2 ms: 1.19x slower                                                      |
| dulwich_log                | 62.0 ms                                                               | 74.1 ms: 1.19x slower                                                      |
| django_template            | 40.7 ms                                                               | 48.7 ms: 1.20x slower                                                      |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                      |
| hexiom                     | 6.98 ms                                                               | 9.22 ms: 1.32x slower                                                      |
| nqueens                    | 99.2 ms                                                               | 132 ms: 1.33x slower                                                       |
| genshi_xml                 | 60.6 ms                                                               | 81.0 ms: 1.34x slower                                                      |
| pprint_safe_repr           | 916 ms                                                                | 1.27 sec: 1.39x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.64 sec: 1.40x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                      |
| gc_traversal               | 4.40 ms                                                               | 6.42 ms: 1.46x slower                                                      |
| create_gc_cycles           | 1.92 ms                                                               | 3.74 ms: 1.95x slower                                                      |
| bench_mp_pool              | 7.05 ms                                                               | 2.26 sec: 320.37x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.14x slower                                                               |

Benchmark hidden because not significant (16): deepcopy_reduce, comprehensions, xml_etree_generate, deltablue, xml_etree_process, xml_etree_iterparse, richards_super, sqlalchemy_imperative, asyncio_websockets, coroutines, raytrace, 2to3, regex_compile, xml_etree_parse, scimark_monte_carlo, unpickle_pure_python
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.044x slower
# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x