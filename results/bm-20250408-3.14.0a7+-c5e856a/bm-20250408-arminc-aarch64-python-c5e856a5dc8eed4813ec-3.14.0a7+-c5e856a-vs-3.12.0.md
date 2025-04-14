# Results vs. 3.12.0

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: linux-aarch64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 291 ms: 1.06x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                   |
| html5lib       | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                     |
| async_tree_none            | 624 ms                                                                | 385 ms: 1.62x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 875 ms: 1.61x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 874 ms: 1.61x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 365 ms: 1.58x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 642 ms: 1.38x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.56x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.8 ms: 1.10x faster                                                    |
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                                     |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.95 ms: 1.17x faster                                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.13x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 173 ms: 1.12x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 139 ms: 1.08x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                   |
| xml_etree_generate  | 112 ms                                                                | 110 ms: 1.01x faster                                                     |
| pickle_pure_python  | 365 us                                                                | 387 us: 1.06x slower                                                     |
| json_loads          | 30.7 us                                                               | 33.9 us: 1.11x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.2 ms: 1.05x faster                                                    |
| genshi_xml     | 60.6 ms                                                               | 59.6 ms: 1.02x faster                                                    |
| mako           | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.61 sec: 2.12x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                     |
| async_tree_none            | 624 ms                                                                | 385 ms: 1.62x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 875 ms: 1.61x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 874 ms: 1.61x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 365 ms: 1.58x faster                                                     |
| deepcopy                   | 446 us                                                                | 320 us: 1.39x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 642 ms: 1.38x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.5 us: 1.32x faster                                                    |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.38 us: 1.21x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.5 ms: 1.19x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 52.1 ms: 1.19x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.6 us: 1.18x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.95 ms: 1.17x faster                                                    |
| pylint                     | 355 ms                                                                | 307 ms: 1.16x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.14x faster                                                    |
| regex_compile              | 137 ms                                                                | 122 ms: 1.13x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 173 ms: 1.12x faster                                                     |
| raytrace                   | 353 ms                                                                | 315 ms: 1.12x faster                                                     |
| float                      | 92.1 ms                                                               | 83.8 ms: 1.10x faster                                                    |
| async_generators           | 491 ms                                                                | 450 ms: 1.09x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.79 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.07 us: 1.08x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 139 ms: 1.08x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.79 us: 1.07x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                     |
| chaos                      | 71.4 ms                                                               | 66.8 ms: 1.07x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                   |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.6 ms: 1.07x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.8 ms: 1.07x faster                                                    |
| sympy_str                  | 280 ms                                                                | 262 ms: 1.07x faster                                                     |
| 2to3                       | 308 ms                                                                | 291 ms: 1.06x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                                    |
| spectral_norm              | 131 ms                                                                | 124 ms: 1.05x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 26.2 ms: 1.05x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 83.3 ms: 1.04x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                                    |
| pyflate                    | 559 ms                                                                | 547 ms: 1.02x faster                                                     |
| docutils                   | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.85 sec: 1.02x faster                                                   |
| genshi_xml                 | 60.6 ms                                                               | 59.6 ms: 1.02x faster                                                    |
| scimark_fft                | 418 ms                                                                | 412 ms: 1.01x faster                                                     |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.01x faster                                                     |
| hexiom                     | 6.98 ms                                                               | 6.99 ms: 1.00x slower                                                    |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.91 us: 1.04x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 30.3 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.87 ms: 1.06x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 387 us: 1.06x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.08 ms: 1.07x slower                                                    |
| fannkuch                   | 443 ms                                                                | 475 ms: 1.07x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.65 ms: 1.07x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                     |
| json_loads                 | 30.7 us                                                               | 33.9 us: 1.11x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.73 ms: 1.53x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.49 ms: 1.82x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.07 sec: 292.96x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (17): django_template, regex_dna, regex_v8, pprint_safe_repr, pycparser, meteor_contest, nqueens, xml_etree_process, richards_super, scimark_sor, asyncio_websockets, unpickle_pure_python, logging_silent, sympy_expand, richards, bench_thread_pool, scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x