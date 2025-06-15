# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.027x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 298 ms: 1.03x faster                                                              |
| docutils       | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                            |
| html5lib       | 65.1 ms                                                               | 61.2 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 461 ms: 1.60x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 888 ms: 1.59x faster                                                              |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 905 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 656 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.5 ms: 1.08x faster                                                             |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                              |
| nbody          | 105 ms                                                                | 122 ms: 1.17x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.93 ms: 1.18x faster                                                             |
| regex_dna      | 254 ms                                                                | 221 ms: 1.15x faster                                                              |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                              |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                              |
| tomli_loads         | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                            |
| xml_etree_process   | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                                             |
| json_loads          | 30.7 us                                                               | 32.2 us: 1.05x slower                                                             |
| pickle_pure_python  | 365 us                                                                | 395 us: 1.08x slower                                                              |
| json_dumps          | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                             |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.65 ms: 1.03x slower                                                             |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                             |
| mako           | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 461 ms: 1.60x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 888 ms: 1.59x faster                                                              |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 905 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 656 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                              |
| deepcopy                   | 446 us                                                                | 334 us: 1.34x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 38.6 us: 1.28x faster                                                             |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                             |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                              |
| generators                 | 43.5 ms                                                               | 36.0 ms: 1.21x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 52.3 ms: 1.19x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 3.93 ms: 1.18x faster                                                             |
| regex_dna                  | 254 ms                                                                | 221 ms: 1.15x faster                                                              |
| pylint                     | 355 ms                                                                | 312 ms: 1.14x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.65 us: 1.12x faster                                                             |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                              |
| sympy_integrate            | 21.6 ms                                                               | 19.8 ms: 1.09x faster                                                             |
| chaos                      | 71.4 ms                                                               | 65.8 ms: 1.09x faster                                                             |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                             |
| pyflate                    | 559 ms                                                                | 516 ms: 1.08x faster                                                              |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                              |
| async_generators           | 491 ms                                                                | 455 ms: 1.08x faster                                                              |
| float                      | 92.1 ms                                                               | 85.5 ms: 1.08x faster                                                             |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                              |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                              |
| html5lib                   | 65.1 ms                                                               | 61.2 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.7 ms: 1.05x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                            |
| hexiom                     | 6.98 ms                                                               | 6.76 ms: 1.03x faster                                                             |
| 2to3                       | 308 ms                                                                | 298 ms: 1.03x faster                                                              |
| genshi_text                | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                             |
| logging_format             | 8.34 us                                                               | 8.10 us: 1.03x faster                                                             |
| docutils                   | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                            |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                              |
| richards                   | 50.9 ms                                                               | 51.4 ms: 1.01x slower                                                             |
| xml_etree_process          | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                                             |
| sqlite_synth               | 3.77 us                                                               | 3.82 us: 1.01x slower                                                             |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.65 ms: 1.03x slower                                                             |
| coroutines                 | 29.0 ms                                                               | 30.0 ms: 1.03x slower                                                             |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                                              |
| json_loads                 | 30.7 us                                                               | 32.2 us: 1.05x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 190 us: 1.05x slower                                                              |
| scimark_lu                 | 146 ms                                                                | 154 ms: 1.06x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.03 sec: 1.08x slower                                                            |
| pickle_pure_python         | 365 us                                                                | 395 us: 1.08x slower                                                              |
| telco                      | 8.51 ms                                                               | 9.20 ms: 1.08x slower                                                             |
| fannkuch                   | 443 ms                                                                | 481 ms: 1.09x slower                                                              |
| pprint_safe_repr           | 916 ms                                                                | 994 ms: 1.09x slower                                                              |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.92 ms: 1.12x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                             |
| nbody                      | 105 ms                                                                | 122 ms: 1.17x slower                                                              |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.73 ms: 1.53x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.78 ms: 1.97x slower                                                             |
| logging_silent             | 127 ns                                                                | 620 ns: 4.89x slower                                                              |
| coverage                   | 87.3 ms                                                               | 556 ms: 6.36x slower                                                              |
| thrift                     | 937 us                                                                | 197 ms: 210.30x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                                      |

Benchmark hidden because not significant (17): crypto_pyaes, sympy_str, regex_v8, django_template, deltablue, scimark_sor, nqueens, meteor_contest, unpickle_pure_python, spectral_norm, pycparser, genshi_xml, logging_simple, richards_super, asyncio_websockets, xml_etree_generate, sympy_expand
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250613-3.15.0a0-9b65402/bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.027x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.10x