# Results vs. 3.12.0

- fork: JelleZijlstra
- ref: sunder_io
- machine: linux-aarch64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 295 ms: 1.04x faster                                                 |
| docutils       | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                               |
| html5lib       | 65.1 ms                                                               | 61.7 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 461 ms: 1.69x faster                                                 |
| async_tree_none            | 624 ms                                                                | 385 ms: 1.62x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 887 ms: 1.58x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 894 ms: 1.58x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 644 ms: 1.37x faster                                                 |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.8 ms: 1.09x faster                                                |
| nbody          | 105 ms                                                                | 120 ms: 1.14x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.82 ms: 1.21x faster                                                |
| regex_compile  | 137 ms                                                                | 120 ms: 1.14x faster                                                 |
| regex_dna      | 254 ms                                                                | 236 ms: 1.08x faster                                                 |
| regex_v8       | 28.3 ms                                                               | 27.4 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                 |
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                               |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.05x faster                                                 |
| xml_etree_process   | 79.0 ms                                                               | 79.5 ms: 1.01x slower                                                |
| pickle_pure_python  | 365 us                                                                | 380 us: 1.04x slower                                                 |
| json_loads          | 30.7 us                                                               | 35.1 us: 1.14x slower                                                |
| json_dumps          | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                                |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                         |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.59 ms: 1.03x slower                                                |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.4 ms: 1.04x faster                                                |
| genshi_xml     | 60.6 ms                                                               | 60.1 ms: 1.01x faster                                                |
| mako           | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.64 sec: 2.08x faster                                               |
| async_tree_memoization     | 777 ms                                                                | 461 ms: 1.69x faster                                                 |
| async_tree_none            | 624 ms                                                                | 385 ms: 1.62x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 887 ms: 1.58x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 894 ms: 1.58x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 644 ms: 1.37x faster                                                 |
| deepcopy                   | 446 us                                                                | 334 us: 1.34x faster                                                 |
| deepcopy_memo              | 49.6 us                                                               | 38.6 us: 1.29x faster                                                |
| comprehensions             | 25.4 us                                                               | 20.8 us: 1.22x faster                                                |
| regex_effbot               | 4.64 ms                                                               | 3.82 ms: 1.21x faster                                                |
| dulwich_log                | 62.0 ms                                                               | 52.0 ms: 1.19x faster                                                |
| generators                 | 43.5 ms                                                               | 36.5 ms: 1.19x faster                                                |
| go                         | 157 ms                                                                | 134 ms: 1.18x faster                                                 |
| deepcopy_reduce            | 4.10 us                                                               | 3.55 us: 1.16x faster                                                |
| regex_compile              | 137 ms                                                                | 120 ms: 1.14x faster                                                 |
| pylint                     | 355 ms                                                                | 314 ms: 1.13x faster                                                 |
| async_generators           | 491 ms                                                                | 446 ms: 1.10x faster                                                 |
| pathlib                    | 24.5 ms                                                               | 22.4 ms: 1.09x faster                                                |
| logging_format             | 8.34 us                                                               | 7.65 us: 1.09x faster                                                |
| logging_simple             | 7.63 us                                                               | 7.00 us: 1.09x faster                                                |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                 |
| float                      | 92.1 ms                                                               | 84.8 ms: 1.09x faster                                                |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                 |
| sympy_str                  | 280 ms                                                                | 259 ms: 1.08x faster                                                 |
| scimark_monte_carlo        | 85.1 ms                                                               | 78.9 ms: 1.08x faster                                                |
| regex_dna                  | 254 ms                                                                | 236 ms: 1.08x faster                                                 |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.08x faster                                                |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                                 |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.07x faster                                                 |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                               |
| sympy_integrate            | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                                |
| html5lib                   | 65.1 ms                                                               | 61.7 ms: 1.05x faster                                                |
| chaos                      | 71.4 ms                                                               | 67.8 ms: 1.05x faster                                                |
| spectral_norm              | 131 ms                                                                | 125 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                 |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                |
| crypto_pyaes               | 86.6 ms                                                               | 82.8 ms: 1.05x faster                                                |
| 2to3                       | 308 ms                                                                | 295 ms: 1.04x faster                                                 |
| genshi_text                | 27.4 ms                                                               | 26.4 ms: 1.04x faster                                                |
| regex_v8                   | 28.3 ms                                                               | 27.4 ms: 1.04x faster                                                |
| pprint_pformat             | 1.88 sec                                                              | 1.84 sec: 1.02x faster                                               |
| pyflate                    | 559 ms                                                                | 548 ms: 1.02x faster                                                 |
| docutils                   | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                               |
| genshi_xml                 | 60.6 ms                                                               | 60.1 ms: 1.01x faster                                                |
| sqlite_synth               | 3.77 us                                                               | 3.75 us: 1.01x faster                                                |
| xml_etree_process          | 79.0 ms                                                               | 79.5 ms: 1.01x slower                                                |
| richards                   | 50.9 ms                                                               | 51.6 ms: 1.01x slower                                                |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                 |
| coroutines                 | 29.0 ms                                                               | 29.8 ms: 1.03x slower                                                |
| python_startup_no_site     | 8.37 ms                                                               | 8.59 ms: 1.03x slower                                                |
| pickle_pure_python         | 365 us                                                                | 380 us: 1.04x slower                                                 |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                                |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                 |
| telco                      | 8.51 ms                                                               | 9.00 ms: 1.06x slower                                                |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.56 ms: 1.06x slower                                                |
| fannkuch                   | 443 ms                                                                | 478 ms: 1.08x slower                                                 |
| json                       | 5.54 ms                                                               | 5.98 ms: 1.08x slower                                                |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                |
| json_loads                 | 30.7 us                                                               | 35.1 us: 1.14x slower                                                |
| nbody                      | 105 ms                                                                | 120 ms: 1.14x slower                                                 |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                                 |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                 |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                                |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                |
| gc_traversal               | 4.40 ms                                                               | 6.56 ms: 1.49x slower                                                |
| create_gc_cycles           | 1.92 ms                                                               | 3.55 ms: 1.85x slower                                                |
| bench_mp_pool              | 7.05 ms                                                               | 2.22 sec: 314.75x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (14): django_template, nqueens, scimark_sor, pprint_safe_repr, pycparser, meteor_contest, scimark_fft, xml_etree_generate, richards_super, sympy_expand, pidigits, unpickle_pure_python, scimark_lu, hexiom
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x