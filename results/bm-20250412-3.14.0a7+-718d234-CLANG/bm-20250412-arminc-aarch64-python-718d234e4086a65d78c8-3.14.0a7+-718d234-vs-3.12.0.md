# Results vs. 3.12.0

- fork: python
- ref: 718d234e4086a65d78c8
- machine: linux-aarch64
- commit hash: 718d234
- commit date: 2025-04-12
- overall geometric mean: 1.088x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 291 ms: 1.06x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.87 sec: 1.04x faster                                                   |
| html5lib       | 65.1 ms                                                               | 59.6 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                     |
| async_tree_none            | 624 ms                                                                | 366 ms: 1.70x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 449 ms: 1.65x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 854 ms: 1.65x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 859 ms: 1.64x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 355 ms: 1.62x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 709 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 708 ms: 1.25x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.8 ms: 1.09x faster                                                    |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| pidigits       | 233 ms                                                                | 291 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.04 ms: 1.15x faster                                                    |
| regex_compile  | 137 ms                                                                | 121 ms: 1.14x faster                                                     |
| regex_dna      | 254 ms                                                                | 236 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                   |
| unpickle            | 18.5 us                                                               | 16.4 us: 1.12x faster                                                    |
| unpickle_list       | 6.17 us                                                               | 5.56 us: 1.11x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 105 ms: 1.07x faster                                                     |
| xml_etree_process   | 79.0 ms                                                               | 74.5 ms: 1.06x faster                                                    |
| pickle_dict         | 37.3 us                                                               | 36.0 us: 1.04x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 148 ms: 1.01x faster                                                     |
| pickle_pure_python  | 365 us                                                                | 369 us: 1.01x slower                                                     |
| pickle_list         | 5.25 us                                                               | 5.44 us: 1.04x slower                                                    |
| xml_etree_parse     | 195 ms                                                                | 205 ms: 1.05x slower                                                     |
| json_loads          | 30.7 us                                                               | 34.1 us: 1.11x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                    |
| pickle              | 13.4 us                                                               | 15.6 us: 1.16x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 25.7 ms: 1.07x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 57.0 ms: 1.06x faster                                                    |
| django_template | 40.7 ms                                                               | 38.5 ms: 1.06x faster                                                    |
| mako            | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.61 sec: 2.12x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                     |
| async_tree_none            | 624 ms                                                                | 366 ms: 1.70x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 449 ms: 1.65x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 854 ms: 1.65x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 859 ms: 1.64x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 355 ms: 1.62x faster                                                     |
| deepcopy                   | 446 us                                                                | 294 us: 1.51x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 35.0 us: 1.42x faster                                                    |
| comprehensions             | 25.4 us                                                               | 19.7 us: 1.29x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 709 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 708 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.34 us: 1.23x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.5 ms: 1.22x faster                                                    |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                     |
| async_generators           | 491 ms                                                                | 410 ms: 1.20x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 53.5 ms: 1.16x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.04 ms: 1.15x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.4 ms: 1.15x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.70 us: 1.14x faster                                                    |
| regex_compile              | 137 ms                                                                | 121 ms: 1.14x faster                                                     |
| pylint                     | 355 ms                                                                | 313 ms: 1.14x faster                                                     |
| logging_silent             | 127 ns                                                                | 112 ns: 1.13x faster                                                     |
| spectral_norm              | 131 ms                                                                | 116 ms: 1.13x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                   |
| unpickle                   | 18.5 us                                                               | 16.4 us: 1.12x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.47 us: 1.12x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 138 ms: 1.12x faster                                                     |
| raytrace                   | 353 ms                                                                | 317 ms: 1.11x faster                                                     |
| unpickle_list              | 6.17 us                                                               | 5.56 us: 1.11x faster                                                    |
| sympy_str                  | 280 ms                                                                | 253 ms: 1.10x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 77.5 ms: 1.10x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.76 ms: 1.10x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 19.8 ms: 1.09x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 59.6 ms: 1.09x faster                                                    |
| chaos                      | 71.4 ms                                                               | 65.6 ms: 1.09x faster                                                    |
| pyflate                    | 559 ms                                                                | 515 ms: 1.09x faster                                                     |
| float                      | 92.1 ms                                                               | 84.8 ms: 1.09x faster                                                    |
| regex_dna                  | 254 ms                                                                | 236 ms: 1.08x faster                                                     |
| xml_etree_generate         | 112 ms                                                                | 105 ms: 1.07x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 25.7 ms: 1.07x faster                                                    |
| richards_super             | 58.5 ms                                                               | 54.9 ms: 1.07x faster                                                    |
| scimark_fft                | 418 ms                                                                | 393 ms: 1.06x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.7 ms: 1.06x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 57.0 ms: 1.06x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                                     |
| xml_etree_process          | 79.0 ms                                                               | 74.5 ms: 1.06x faster                                                    |
| scimark_sor                | 150 ms                                                                | 141 ms: 1.06x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 149 ms: 1.06x faster                                                     |
| 2to3                       | 308 ms                                                                | 291 ms: 1.06x faster                                                     |
| richards                   | 50.9 ms                                                               | 48.2 ms: 1.06x faster                                                    |
| django_template            | 40.7 ms                                                               | 38.5 ms: 1.06x faster                                                    |
| pickle_dict                | 37.3 us                                                               | 36.0 us: 1.04x faster                                                    |
| docutils                   | 2.98 sec                                                              | 2.87 sec: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 84.3 ms: 1.03x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 552 ms: 1.03x faster                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.84 sec: 1.02x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 900 ms: 1.02x faster                                                     |
| nqueens                    | 99.2 ms                                                               | 97.7 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.01x faster                                                     |
| hexiom                     | 6.98 ms                                                               | 6.90 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.17 sec: 1.01x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 369 us: 1.01x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.84 us: 1.02x slower                                                    |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.03x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.44 us: 1.04x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 187 us: 1.04x slower                                                     |
| telco                      | 8.51 ms                                                               | 8.90 ms: 1.05x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 205 ms: 1.05x slower                                                     |
| json                       | 5.54 ms                                                               | 5.85 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.60 ms: 1.07x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| coverage                   | 87.3 ms                                                               | 96.7 ms: 1.11x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.1 us: 1.11x slower                                                    |
| fannkuch                   | 443 ms                                                                | 493 ms: 1.11x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.6 us: 1.16x slower                                                    |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| pidigits                   | 233 ms                                                                | 291 ms: 1.25x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.56 ms: 1.49x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.62 ms: 1.89x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.97 sec: 421.34x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (5): unpickle_pure_python, coroutines, sympy_expand, bench_thread_pool, regex_v8
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.088x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.09x