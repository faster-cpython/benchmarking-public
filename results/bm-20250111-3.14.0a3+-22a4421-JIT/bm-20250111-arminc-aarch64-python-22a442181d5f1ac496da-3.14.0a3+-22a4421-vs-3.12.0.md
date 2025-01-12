# Results vs. 3.12.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.025x slower
- HPT reliability: 98.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 319 ms: 1.03x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.24 sec: 1.09x slower                                                   |
| html5lib       | 65.1 ms                                                               | 68.9 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 406 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.53x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 921 ms: 1.53x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 518 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 675 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 700 ms: 1.30x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.46x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                     |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                                   |
| pickle_dict         | 37.3 us                                                               | 39.0 us: 1.04x slower                                                    |
| unpickle_list       | 6.17 us                                                               | 6.76 us: 1.10x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 403 us: 1.10x slower                                                     |
| pickle_list         | 5.25 us                                                               | 6.02 us: 1.15x slower                                                    |
| pickle              | 13.4 us                                                               | 16.1 us: 1.20x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (5): unpickle, json_loads, unpickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.09 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                    |
| django_template | 40.7 ms                                                               | 47.0 ms: 1.16x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 33.1 ms: 1.21x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 83.7 ms: 1.38x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.19x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 406 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.53x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 921 ms: 1.53x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 518 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 675 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 700 ms: 1.30x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 39.0 us: 1.27x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                    |
| deepcopy                   | 446 us                                                                | 402 us: 1.11x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.9 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                                   |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                     |
| json                       | 5.54 ms                                                               | 5.67 ms: 1.02x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                    |
| logging_format             | 8.34 us                                                               | 8.63 us: 1.03x slower                                                    |
| 2to3                       | 308 ms                                                                | 319 ms: 1.03x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 160 ms: 1.04x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.55 sec: 1.04x slower                                                   |
| sqlalchemy_imperative      | 16.7 ms                                                               | 17.4 ms: 1.04x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 39.0 us: 1.04x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.30 sec: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.52 ms: 1.05x slower                                                    |
| logging_simple             | 7.63 us                                                               | 8.04 us: 1.05x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 154 ms: 1.06x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 68.9 ms: 1.06x slower                                                    |
| async_generators           | 491 ms                                                                | 521 ms: 1.06x slower                                                     |
| asyncio_tcp                | 566 ms                                                                | 603 ms: 1.06x slower                                                     |
| go                         | 157 ms                                                                | 168 ms: 1.07x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.57 ms: 1.07x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.42 ms: 1.07x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.8 ms: 1.07x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 23.4 ms: 1.08x slower                                                    |
| richards                   | 50.9 ms                                                               | 55.3 ms: 1.09x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.09 ms: 1.09x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.24 sec: 1.09x slower                                                   |
| sympy_str                  | 280 ms                                                                | 305 ms: 1.09x slower                                                     |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.00 ms: 1.09x slower                                                    |
| scimark_sor                | 150 ms                                                                | 164 ms: 1.10x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.76 us: 1.10x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 95.1 ms: 1.10x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 403 us: 1.10x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 139 ms: 1.11x slower                                                     |
| pyflate                    | 559 ms                                                                | 619 ms: 1.11x slower                                                     |
| thrift                     | 937 us                                                                | 1.04 ms: 1.11x slower                                                    |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.12x slower                                                     |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.12x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 68.9 ms: 1.12x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.24 us: 1.13x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 70.2 ms: 1.13x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.69 ms: 1.14x slower                                                    |
| sympy_expand               | 454 ms                                                                | 518 ms: 1.14x slower                                                     |
| pickle_list                | 5.25 us                                                               | 6.02 us: 1.15x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                    |
| django_template            | 40.7 ms                                                               | 47.0 ms: 1.16x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.46 sec: 1.17x slower                                                   |
| fannkuch                   | 443 ms                                                                | 517 ms: 1.17x slower                                                     |
| generators                 | 43.5 ms                                                               | 50.8 ms: 1.17x slower                                                    |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                     |
| logging_silent             | 127 ns                                                                | 150 ns: 1.18x slower                                                     |
| pickle                     | 13.4 us                                                               | 16.1 us: 1.20x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 33.1 ms: 1.21x slower                                                    |
| chaos                      | 71.4 ms                                                               | 87.0 ms: 1.22x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 220 us: 1.22x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 129 ms: 1.30x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.23 sec: 1.34x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 9.47 ms: 1.36x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.57 sec: 1.37x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 83.7 ms: 1.38x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.95 ms: 1.58x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.64 ms: 1.90x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.33 sec: 188.43x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.11x slower                                                             |

Benchmark hidden because not significant (17): pylint, deepcopy_reduce, unpickle, comprehensions, float, scimark_monte_carlo, scimark_fft, asyncio_websockets, coroutines, json_loads, unpickle_pure_python, sqlalchemy_declarative, regex_compile, xml_etree_generate, raytrace, xml_etree_process, regex_dna
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 98.58% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x