# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.029x slower
- HPT reliability: 99.36%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 319 ms: 1.03x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.18 sec: 1.07x slower                                                   |
| html5lib       | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 409 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 924 ms: 1.52x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 938 ms: 1.50x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 494 ms: 1.50x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 524 ms: 1.48x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 396 ms: 1.46x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 702 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 687 ms: 1.29x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.44x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 244 ms: 1.05x slower                                                     |
| nbody          | 105 ms                                                                | 118 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.98 ms: 1.16x faster                                                    |
| regex_compile  | 137 ms                                                                | 145 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.52 sec: 1.03x faster                                                   |
| json_loads          | 30.7 us                                                               | 32.7 us: 1.07x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 416 us: 1.14x slower                                                     |
| json_dumps          | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                                    |
| django_template | 40.7 ms                                                               | 49.1 ms: 1.21x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 34.5 ms: 1.26x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 80.3 ms: 1.33x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 409 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 924 ms: 1.52x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 938 ms: 1.50x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 494 ms: 1.50x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 524 ms: 1.48x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 396 ms: 1.46x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 702 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 687 ms: 1.29x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.1 us: 1.24x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.98 ms: 1.16x faster                                                    |
| deepcopy                   | 446 us                                                                | 383 us: 1.16x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.52 sec: 1.03x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.02x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 159 ms: 1.03x slower                                                     |
| 2to3                       | 308 ms                                                                | 319 ms: 1.03x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 681 ms: 1.04x slower                                                     |
| logging_simple             | 7.63 us                                                               | 7.92 us: 1.04x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.30 ms: 1.04x slower                                                    |
| pidigits                   | 233 ms                                                                | 244 ms: 1.05x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.58 sec: 1.05x slower                                                   |
| logging_format             | 8.34 us                                                               | 8.79 us: 1.05x slower                                                    |
| regex_compile              | 137 ms                                                                | 145 ms: 1.05x slower                                                     |
| json                       | 5.54 ms                                                               | 5.86 ms: 1.06x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 23.0 ms: 1.06x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.18 sec: 1.07x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.07x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.40 ms: 1.07x slower                                                    |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                                     |
| sympy_str                  | 280 ms                                                                | 300 ms: 1.07x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 92.9 ms: 1.07x slower                                                    |
| pyflate                    | 559 ms                                                                | 603 ms: 1.08x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.08x slower                                                    |
| thrift                     | 937 us                                                                | 1.02 ms: 1.09x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.10 us: 1.09x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.00 ms: 1.09x slower                                                    |
| go                         | 157 ms                                                                | 172 ms: 1.09x slower                                                     |
| richards                   | 50.9 ms                                                               | 55.8 ms: 1.09x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                    |
| async_generators           | 491 ms                                                                | 540 ms: 1.10x slower                                                     |
| richards_super             | 58.5 ms                                                               | 64.6 ms: 1.11x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 140 ms: 1.11x slower                                                     |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                     |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.12x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.95 ms: 1.12x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 70.0 ms: 1.13x slower                                                    |
| nbody                      | 105 ms                                                                | 118 ms: 1.13x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 69.4 ms: 1.13x slower                                                    |
| sympy_expand               | 454 ms                                                                | 517 ms: 1.14x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 416 us: 1.14x slower                                                     |
| generators                 | 43.5 ms                                                               | 49.7 ms: 1.14x slower                                                    |
| logging_silent             | 127 ns                                                                | 145 ns: 1.15x slower                                                     |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.44 sec: 1.15x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.82 ms: 1.15x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                                    |
| fannkuch                   | 443 ms                                                                | 522 ms: 1.18x slower                                                     |
| chaos                      | 71.4 ms                                                               | 84.6 ms: 1.19x slower                                                    |
| django_template            | 40.7 ms                                                               | 49.1 ms: 1.21x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 222 us: 1.23x slower                                                     |
| mypy2                      | 873 ms                                                                | 1.08 sec: 1.24x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.5 ms: 1.26x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 131 ms: 1.32x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 80.3 ms: 1.33x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.28 ms: 1.33x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.31 sec: 1.43x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.69 sec: 1.43x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.80 ms: 1.55x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.62 ms: 1.89x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.51 sec: 214.48x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                             |

Benchmark hidden because not significant (14): pathlib, deepcopy_reduce, comprehensions, scimark_monte_carlo, xml_etree_generate, coroutines, scimark_fft, raytrace, unpickle_pure_python, xml_etree_process, pylint, float, sqlalchemy_imperative, regex_dna
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.029x slower

# HPT report

- Reliability score: 99.36% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x