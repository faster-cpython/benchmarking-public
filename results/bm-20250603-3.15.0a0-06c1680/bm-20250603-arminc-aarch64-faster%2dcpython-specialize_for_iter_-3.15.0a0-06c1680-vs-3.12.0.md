# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.027x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 2.92 sec: 1.02x faster                                                            |
| html5lib       | 65.1 ms                                                               | 61.2 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 463 ms: 1.68x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 877 ms: 1.61x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 462 ms: 1.60x faster                                                              |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 910 ms: 1.54x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 645 ms: 1.37x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                             |
| nbody          | 105 ms                                                                | 123 ms: 1.18x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                             |
| regex_compile  | 137 ms                                                                | 123 ms: 1.12x faster                                                              |
| regex_dna      | 254 ms                                                                | 229 ms: 1.11x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                              |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.07x faster                                                              |
| tomli_loads         | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                            |
| xml_etree_process   | 79.0 ms                                                               | 80.0 ms: 1.01x slower                                                             |
| json_loads          | 30.7 us                                                               | 32.5 us: 1.06x slower                                                             |
| pickle_pure_python  | 365 us                                                                | 396 us: 1.09x slower                                                              |
| json_dumps          | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                             |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.59 ms: 1.03x slower                                                             |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 61.0 ms: 1.01x slower                                                             |
| mako           | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.65 sec: 2.07x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 463 ms: 1.68x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 877 ms: 1.61x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 462 ms: 1.60x faster                                                              |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 910 ms: 1.54x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 645 ms: 1.37x faster                                                              |
| deepcopy                   | 446 us                                                                | 328 us: 1.36x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                             |
| go                         | 157 ms                                                                | 127 ms: 1.24x faster                                                              |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                             |
| generators                 | 43.5 ms                                                               | 35.8 ms: 1.22x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.52 us: 1.16x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 53.9 ms: 1.15x faster                                                             |
| pylint                     | 355 ms                                                                | 313 ms: 1.14x faster                                                              |
| regex_compile              | 137 ms                                                                | 123 ms: 1.12x faster                                                              |
| regex_dna                  | 254 ms                                                                | 229 ms: 1.11x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 22.3 ms: 1.10x faster                                                             |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                              |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                              |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                              |
| async_generators           | 491 ms                                                                | 455 ms: 1.08x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.0 ms: 1.08x faster                                                             |
| float                      | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                             |
| sympy_integrate            | 21.6 ms                                                               | 20.3 ms: 1.07x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                              |
| html5lib                   | 65.1 ms                                                               | 61.2 ms: 1.06x faster                                                             |
| pyflate                    | 559 ms                                                                | 526 ms: 1.06x faster                                                              |
| tomli_loads                | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                            |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                             |
| crypto_pyaes               | 86.6 ms                                                               | 82.8 ms: 1.05x faster                                                             |
| docutils                   | 2.98 sec                                                              | 2.92 sec: 1.02x faster                                                            |
| nqueens                    | 99.2 ms                                                               | 97.2 ms: 1.02x faster                                                             |
| hexiom                     | 6.98 ms                                                               | 6.84 ms: 1.02x faster                                                             |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.01x faster                                                            |
| logging_format             | 8.34 us                                                               | 8.25 us: 1.01x faster                                                             |
| genshi_xml                 | 60.6 ms                                                               | 61.0 ms: 1.01x slower                                                             |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                              |
| xml_etree_process          | 79.0 ms                                                               | 80.0 ms: 1.01x slower                                                             |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                              |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.02x slower                                                             |
| richards                   | 50.9 ms                                                               | 51.7 ms: 1.02x slower                                                             |
| coroutines                 | 29.0 ms                                                               | 29.7 ms: 1.02x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.59 ms: 1.03x slower                                                             |
| sympy_expand               | 454 ms                                                                | 467 ms: 1.03x slower                                                              |
| scimark_fft                | 418 ms                                                                | 435 ms: 1.04x slower                                                              |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.05x slower                                                             |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                             |
| fannkuch                   | 443 ms                                                                | 472 ms: 1.06x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.01 sec: 1.07x slower                                                            |
| pprint_safe_repr           | 916 ms                                                                | 983 ms: 1.07x slower                                                              |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.09x slower                                                              |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.47 ms: 1.11x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.92 ms: 1.12x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 203 us: 1.12x slower                                                              |
| nbody                      | 105 ms                                                                | 123 ms: 1.18x slower                                                              |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.84 ms: 1.56x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.74 ms: 1.95x slower                                                             |
| logging_silent             | 127 ns                                                                | 634 ns: 5.00x slower                                                              |
| coverage                   | 87.3 ms                                                               | 568 ms: 6.51x slower                                                              |
| thrift                     | 937 us                                                                | 191 ms: 203.64x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                                      |

Benchmark hidden because not significant (14): chaos, scimark_sor, django_template, regex_v8, 2to3, sympy_str, logging_simple, spectral_norm, unpickle_pure_python, genshi_text, richards_super, pidigits, xml_etree_generate, scimark_lu
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250603-3.15.0a0-06c1680/bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.027x slower

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x