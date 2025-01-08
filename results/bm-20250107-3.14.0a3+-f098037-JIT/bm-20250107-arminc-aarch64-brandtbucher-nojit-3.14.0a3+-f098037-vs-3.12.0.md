# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.032x slower
- HPT reliability: 99.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 324 ms: 1.05x slower                                            |
| docutils       | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                          |
| html5lib       | 65.1 ms                                                               | 72.8 ms: 1.12x slower                                           |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 404 ms: 1.54x faster                                            |
| async_tree_io              | 1.41 sec                                                              | 933 ms: 1.51x faster                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 491 ms: 1.51x faster                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 936 ms: 1.50x faster                                            |
| async_tree_memoization     | 777 ms                                                                | 525 ms: 1.48x faster                                            |
| async_tree_none_tg         | 577 ms                                                                | 400 ms: 1.44x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 698 ms: 1.31x faster                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 686 ms: 1.29x faster                                            |
| Geometric mean             | (ref)                                                                 | 1.44x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                            |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.98 ms: 1.16x faster                                           |
| regex_v8       | 28.3 ms                                                               | 31.9 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 183 ms: 1.07x faster                                            |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                            |
| tomli_loads         | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                          |
| xml_etree_process   | 79.0 ms                                                               | 81.4 ms: 1.03x slower                                           |
| pickle_pure_python  | 365 us                                                                | 412 us: 1.13x slower                                            |
| json_dumps          | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                           |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                    |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.16 ms: 1.09x slower                                           |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.26x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                           |
| django_template | 40.7 ms                                                               | 48.4 ms: 1.19x slower                                           |
| genshi_text     | 27.4 ms                                                               | 34.3 ms: 1.25x slower                                           |
| genshi_xml      | 60.6 ms                                                               | 82.7 ms: 1.37x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 404 ms: 1.54x faster                                            |
| async_tree_io              | 1.41 sec                                                              | 933 ms: 1.51x faster                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 491 ms: 1.51x faster                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 936 ms: 1.50x faster                                            |
| async_tree_memoization     | 777 ms                                                                | 525 ms: 1.48x faster                                            |
| async_tree_none_tg         | 577 ms                                                                | 400 ms: 1.44x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 698 ms: 1.31x faster                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 686 ms: 1.29x faster                                            |
| deepcopy_memo              | 49.6 us                                                               | 40.2 us: 1.23x faster                                           |
| regex_effbot               | 4.64 ms                                                               | 3.98 ms: 1.16x faster                                           |
| deepcopy                   | 446 us                                                                | 392 us: 1.14x faster                                            |
| pathlib                    | 24.5 ms                                                               | 22.3 ms: 1.10x faster                                           |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                            |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                            |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                          |
| asyncio_websockets         | 658 ms                                                                | 675 ms: 1.03x slower                                            |
| xml_etree_process          | 79.0 ms                                                               | 81.4 ms: 1.03x slower                                           |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                            |
| raytrace                   | 353 ms                                                                | 368 ms: 1.04x slower                                            |
| sqlglot_transpile          | 1.83 ms                                                               | 1.91 ms: 1.04x slower                                           |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.05x slower                                           |
| sqlalchemy_imperative      | 16.7 ms                                                               | 17.4 ms: 1.05x slower                                           |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                           |
| 2to3                       | 308 ms                                                                | 324 ms: 1.05x slower                                            |
| mdp                        | 3.41 sec                                                              | 3.60 sec: 1.06x slower                                          |
| logging_simple             | 7.63 us                                                               | 8.08 us: 1.06x slower                                           |
| logging_format             | 8.34 us                                                               | 8.87 us: 1.06x slower                                           |
| thrift                     | 937 us                                                                | 1000 us: 1.07x slower                                           |
| pyflate                    | 559 ms                                                                | 599 ms: 1.07x slower                                            |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                            |
| crypto_pyaes               | 86.6 ms                                                               | 92.9 ms: 1.07x slower                                           |
| docutils                   | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                          |
| scimark_lu                 | 146 ms                                                                | 157 ms: 1.08x slower                                            |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                           |
| scimark_sor                | 150 ms                                                                | 162 ms: 1.08x slower                                            |
| sympy_sum                  | 154 ms                                                                | 167 ms: 1.08x slower                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.72 ms: 1.08x slower                                           |
| sqlite_synth               | 3.77 us                                                               | 4.10 us: 1.09x slower                                           |
| async_generators           | 491 ms                                                                | 534 ms: 1.09x slower                                            |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                            |
| python_startup_no_site     | 8.37 ms                                                               | 9.16 ms: 1.09x slower                                           |
| richards_super             | 58.5 ms                                                               | 64.2 ms: 1.10x slower                                           |
| sqlglot_parse              | 1.46 ms                                                               | 1.61 ms: 1.10x slower                                           |
| sqlglot_normalize          | 126 ms                                                                | 139 ms: 1.10x slower                                            |
| sympy_str                  | 280 ms                                                                | 309 ms: 1.11x slower                                            |
| deltablue                  | 4.12 ms                                                               | 4.56 ms: 1.11x slower                                           |
| richards                   | 50.9 ms                                                               | 56.4 ms: 1.11x slower                                           |
| go                         | 157 ms                                                                | 174 ms: 1.11x slower                                            |
| sympy_integrate            | 21.6 ms                                                               | 24.0 ms: 1.11x slower                                           |
| html5lib                   | 65.1 ms                                                               | 72.8 ms: 1.12x slower                                           |
| telco                      | 8.51 ms                                                               | 9.52 ms: 1.12x slower                                           |
| regex_v8                   | 28.3 ms                                                               | 31.9 ms: 1.13x slower                                           |
| pickle_pure_python         | 365 us                                                                | 412 us: 1.13x slower                                            |
| meteor_contest             | 112 ms                                                                | 126 ms: 1.13x slower                                            |
| sqlglot_optimize           | 61.3 ms                                                               | 69.6 ms: 1.13x slower                                           |
| fannkuch                   | 443 ms                                                                | 507 ms: 1.14x slower                                            |
| dulwich_log                | 62.0 ms                                                               | 71.7 ms: 1.16x slower                                           |
| logging_silent             | 127 ns                                                                | 147 ns: 1.16x slower                                            |
| generators                 | 43.5 ms                                                               | 50.6 ms: 1.16x slower                                           |
| pycparser                  | 1.26 sec                                                              | 1.47 sec: 1.17x slower                                          |
| chaos                      | 71.4 ms                                                               | 83.5 ms: 1.17x slower                                           |
| sympy_expand               | 454 ms                                                                | 531 ms: 1.17x slower                                            |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                           |
| django_template            | 40.7 ms                                                               | 48.4 ms: 1.19x slower                                           |
| typing_runtime_protocols   | 181 us                                                                | 215 us: 1.19x slower                                            |
| genshi_text                | 27.4 ms                                                               | 34.3 ms: 1.25x slower                                           |
| mypy2                      | 873 ms                                                                | 1.10 sec: 1.26x slower                                          |
| coverage                   | 87.3 ms                                                               | 111 ms: 1.27x slower                                            |
| nqueens                    | 99.2 ms                                                               | 127 ms: 1.28x slower                                            |
| pprint_safe_repr           | 916 ms                                                                | 1.24 sec: 1.35x slower                                          |
| genshi_xml                 | 60.6 ms                                                               | 82.7 ms: 1.37x slower                                           |
| pprint_pformat             | 1.88 sec                                                              | 2.58 sec: 1.37x slower                                          |
| hexiom                     | 6.98 ms                                                               | 9.60 ms: 1.38x slower                                           |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                           |
| gc_traversal               | 4.40 ms                                                               | 6.94 ms: 1.58x slower                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.56 ms: 1.85x slower                                           |
| bench_mp_pool              | 7.05 ms                                                               | 1.51 sec: 213.56x slower                                        |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                    |

Benchmark hidden because not significant (13): pylint, comprehensions, deepcopy_reduce, scimark_monte_carlo, float, regex_dna, unpickle_pure_python, scimark_fft, regex_compile, json_loads, coroutines, sqlalchemy_declarative, xml_etree_generate
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 99.50% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x