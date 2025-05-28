# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.031x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 302 ms: 1.02x faster                                                              |
| docutils       | 2.98 sec                                                              | 2.94 sec: 1.02x faster                                                            |
| html5lib       | 65.1 ms                                                               | 61.1 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 464 ms: 1.67x faster                                                              |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 879 ms: 1.61x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 904 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                             |
| nbody          | 105 ms                                                                | 120 ms: 1.14x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                             |
| regex_compile  | 137 ms                                                                | 121 ms: 1.13x faster                                                              |
| regex_dna      | 254 ms                                                                | 229 ms: 1.11x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                            |
| xml_etree_parse     | 195 ms                                                                | 184 ms: 1.06x faster                                                              |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                              |
| xml_etree_process   | 79.0 ms                                                               | 78.6 ms: 1.00x faster                                                             |
| pickle_pure_python  | 365 us                                                                | 386 us: 1.06x slower                                                              |
| json_dumps          | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                             |
| json_loads          | 30.7 us                                                               | 35.3 us: 1.15x slower                                                             |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                             |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.6 ms: 1.03x faster                                                             |
| genshi_text     | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                                             |
| genshi_xml      | 60.6 ms                                                               | 61.5 ms: 1.02x slower                                                             |
| mako            | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                             |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.71 sec: 1.99x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 464 ms: 1.67x faster                                                              |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 879 ms: 1.61x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 904 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                              |
| deepcopy                   | 446 us                                                                | 328 us: 1.36x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                             |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.22x faster                                                             |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                              |
| regex_effbot               | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                             |
| generators                 | 43.5 ms                                                               | 36.7 ms: 1.18x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 52.6 ms: 1.18x faster                                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.53 us: 1.16x faster                                                             |
| pylint                     | 355 ms                                                                | 310 ms: 1.14x faster                                                              |
| regex_compile              | 137 ms                                                                | 121 ms: 1.13x faster                                                              |
| regex_dna                  | 254 ms                                                                | 229 ms: 1.11x faster                                                              |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.10x faster                                                              |
| async_generators           | 491 ms                                                                | 450 ms: 1.09x faster                                                              |
| raytrace                   | 353 ms                                                                | 328 ms: 1.08x faster                                                              |
| sympy_integrate            | 21.6 ms                                                               | 20.3 ms: 1.07x faster                                                             |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                             |
| html5lib                   | 65.1 ms                                                               | 61.1 ms: 1.06x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                            |
| xml_etree_parse            | 195 ms                                                                | 184 ms: 1.06x faster                                                              |
| crypto_pyaes               | 86.6 ms                                                               | 82.1 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                              |
| float                      | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.1 ms: 1.05x faster                                                             |
| scimark_sor                | 150 ms                                                                | 145 ms: 1.04x faster                                                              |
| pyflate                    | 559 ms                                                                | 541 ms: 1.03x faster                                                              |
| django_template            | 40.7 ms                                                               | 39.6 ms: 1.03x faster                                                             |
| 2to3                       | 308 ms                                                                | 302 ms: 1.02x faster                                                              |
| docutils                   | 2.98 sec                                                              | 2.94 sec: 1.02x faster                                                            |
| genshi_text                | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                                             |
| richards_super             | 58.5 ms                                                               | 57.7 ms: 1.01x faster                                                             |
| xml_etree_process          | 79.0 ms                                                               | 78.6 ms: 1.00x faster                                                             |
| logging_format             | 8.34 us                                                               | 8.41 us: 1.01x slower                                                             |
| logging_simple             | 7.63 us                                                               | 7.70 us: 1.01x slower                                                             |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                              |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.01x slower                                                             |
| genshi_xml                 | 60.6 ms                                                               | 61.5 ms: 1.02x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                             |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                                              |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 386 us: 1.06x slower                                                              |
| fannkuch                   | 443 ms                                                                | 471 ms: 1.06x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.02 sec: 1.07x slower                                                            |
| pprint_safe_repr           | 916 ms                                                                | 985 ms: 1.08x slower                                                              |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                             |
| json                       | 5.54 ms                                                               | 6.07 ms: 1.10x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.83 ms: 1.10x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.38 ms: 1.10x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 202 us: 1.12x slower                                                              |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                             |
| nbody                      | 105 ms                                                                | 120 ms: 1.14x slower                                                              |
| json_loads                 | 30.7 us                                                               | 35.3 us: 1.15x slower                                                             |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.97 ms: 1.58x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.78 ms: 1.97x slower                                                             |
| logging_silent             | 127 ns                                                                | 628 ns: 4.95x slower                                                              |
| coverage                   | 87.3 ms                                                               | 553 ms: 6.33x slower                                                              |
| thrift                     | 937 us                                                                | 193 ms: 205.71x slower                                                            |
| bench_mp_pool              | 7.05 ms                                                               | 2.26 sec: 320.25x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                                      |

Benchmark hidden because not significant (16): regex_v8, sympy_str, chaos, deltablue, spectral_norm, nqueens, pycparser, xml_etree_generate, richards, meteor_contest, hexiom, scimark_lu, sympy_expand, pidigits, unpickle_pure_python, coroutines
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250528-3.15.0a0-a684067/bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.031x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x