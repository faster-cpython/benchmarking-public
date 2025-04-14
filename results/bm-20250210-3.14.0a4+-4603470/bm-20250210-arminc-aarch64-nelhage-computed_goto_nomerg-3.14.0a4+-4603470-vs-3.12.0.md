# Results vs. 3.12.0

- fork: nelhage
- ref: computed_goto_nomerg
- machine: linux-aarch64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.041x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 396 ms: 1.57x faster                                                      |
| async_tree_memoization     | 777 ms                                                                | 499 ms: 1.56x faster                                                      |
| async_tree_io              | 1.41 sec                                                              | 925 ms: 1.53x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                                      |
| async_tree_memoization_tg  | 740 ms                                                                | 487 ms: 1.52x faster                                                      |
| async_tree_none_tg         | 577 ms                                                                | 391 ms: 1.48x faster                                                      |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 686 ms: 1.33x faster                                                      |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 679 ms: 1.30x faster                                                      |
| Geometric mean             | (ref)                                                                 | 1.47x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.0 ms: 1.06x faster                                                     |
| pidigits       | 233 ms                                                                | 247 ms: 1.06x slower                                                      |
| nbody          | 105 ms                                                                | 124 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.05 ms: 1.15x faster                                                     |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                      |
| regex_v8       | 28.3 ms                                                               | 33.1 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 183 ms: 1.07x faster                                                      |
| tomli_loads         | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 82.9 ms: 1.05x slower                                                     |
| xml_etree_iterparse | 150 ms                                                                | 162 ms: 1.08x slower                                                      |
| pickle_pure_python  | 365 us                                                                | 395 us: 1.08x slower                                                      |
| json_loads          | 30.7 us                                                               | 34.8 us: 1.13x slower                                                     |
| json_dumps          | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.05x slower                                                              |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                     |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                              |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 396 ms: 1.57x faster                                                      |
| async_tree_memoization     | 777 ms                                                                | 499 ms: 1.56x faster                                                      |
| async_tree_io              | 1.41 sec                                                              | 925 ms: 1.53x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                                      |
| async_tree_memoization_tg  | 740 ms                                                                | 487 ms: 1.52x faster                                                      |
| async_tree_none_tg         | 577 ms                                                                | 391 ms: 1.48x faster                                                      |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 686 ms: 1.33x faster                                                      |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 679 ms: 1.30x faster                                                      |
| deepcopy                   | 446 us                                                                | 347 us: 1.28x faster                                                      |
| deepcopy_memo              | 49.6 us                                                               | 41.0 us: 1.21x faster                                                     |
| comprehensions             | 25.4 us                                                               | 21.3 us: 1.19x faster                                                     |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                     |
| pylint                     | 355 ms                                                                | 303 ms: 1.17x faster                                                      |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.05 ms: 1.15x faster                                                     |
| raytrace                   | 353 ms                                                                | 319 ms: 1.11x faster                                                      |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.1 ms: 1.10x faster                                                     |
| spectral_norm              | 131 ms                                                                | 119 ms: 1.09x faster                                                      |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                                      |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                      |
| sympy_str                  | 280 ms                                                                | 261 ms: 1.07x faster                                                      |
| async_generators           | 491 ms                                                                | 458 ms: 1.07x faster                                                      |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                                      |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.07x faster                                                      |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                      |
| float                      | 92.1 ms                                                               | 87.0 ms: 1.06x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.90 us: 1.06x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.90 ms: 1.06x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 59.3 ms: 1.05x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.04x faster                                                      |
| logging_simple             | 7.63 us                                                               | 7.31 us: 1.04x faster                                                     |
| chaos                      | 71.4 ms                                                               | 68.6 ms: 1.04x faster                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                                    |
| thrift                     | 937 us                                                                | 947 us: 1.01x slower                                                      |
| docutils                   | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                    |
| richards_super             | 58.5 ms                                                               | 60.0 ms: 1.03x slower                                                     |
| sympy_expand               | 454 ms                                                                | 470 ms: 1.04x slower                                                      |
| pycparser                  | 1.26 sec                                                              | 1.30 sec: 1.04x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.97 sec: 1.05x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 82.9 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.52 ms: 1.05x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.35 ms: 1.05x slower                                                     |
| pidigits                   | 233 ms                                                                | 247 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 916 ms                                                                | 977 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 150 ms                                                                | 162 ms: 1.08x slower                                                      |
| richards                   | 50.9 ms                                                               | 55.1 ms: 1.08x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 395 us: 1.08x slower                                                      |
| sqlite_synth               | 3.77 us                                                               | 4.10 us: 1.09x slower                                                     |
| json                       | 5.54 ms                                                               | 6.06 ms: 1.09x slower                                                     |
| fannkuch                   | 443 ms                                                                | 486 ms: 1.10x slower                                                      |
| logging_silent             | 127 ns                                                                | 139 ns: 1.10x slower                                                      |
| typing_runtime_protocols   | 181 us                                                                | 201 us: 1.11x slower                                                      |
| json_loads                 | 30.7 us                                                               | 34.8 us: 1.13x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.65 ms: 1.13x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 33.1 ms: 1.17x slower                                                     |
| nbody                      | 105 ms                                                                | 124 ms: 1.18x slower                                                      |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                     |
| coverage                   | 87.3 ms                                                               | 105 ms: 1.21x slower                                                      |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 6.76 ms: 1.54x slower                                                     |
| create_gc_cycles           | 1.92 ms                                                               | 3.59 ms: 1.87x slower                                                     |
| bench_mp_pool              | 7.05 ms                                                               | 3.99 sec: 565.95x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                              |

Benchmark hidden because not significant (23): sqlglot_transpile, crypto_pyaes, scimark_monte_carlo, django_template, 2to3, scimark_fft, mdp, coroutines, genshi_text, sympy_integrate, bench_thread_pool, pyflate, unpickle_pure_python, html5lib, asyncio_websockets, sqlglot_optimize, sqlglot_normalize, meteor_contest, regex_dna, genshi_xml, scimark_sor, xml_etree_generate, nqueens
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250210-3.14.0a4+-4603470/bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x