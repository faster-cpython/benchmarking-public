# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.025x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                            |
| html5lib       | 65.1 ms                                                               | 61.2 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 460 ms: 1.69x faster                                                              |
| async_tree_none            | 624 ms                                                                | 385 ms: 1.62x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 457 ms: 1.62x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 892 ms: 1.58x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 365 ms: 1.58x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 649 ms: 1.41x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.4 ms: 1.08x faster                                                             |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                              |
| nbody          | 105 ms                                                                | 125 ms: 1.19x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.01 ms: 1.16x faster                                                             |
| regex_dna      | 254 ms                                                                | 223 ms: 1.14x faster                                                              |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 183 ms: 1.07x faster                                                              |
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                            |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                              |
| xml_etree_process   | 79.0 ms                                                               | 79.5 ms: 1.01x slower                                                             |
| pickle_pure_python  | 365 us                                                                | 387 us: 1.06x slower                                                              |
| json_loads          | 30.7 us                                                               | 32.7 us: 1.07x slower                                                             |
| json_dumps          | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                             |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                             |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.64 sec: 2.08x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 460 ms: 1.69x faster                                                              |
| async_tree_none            | 624 ms                                                                | 385 ms: 1.62x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 457 ms: 1.62x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 892 ms: 1.58x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 365 ms: 1.58x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 649 ms: 1.41x faster                                                              |
| deepcopy                   | 446 us                                                                | 324 us: 1.37x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 36.2 us: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                              |
| go                         | 157 ms                                                                | 128 ms: 1.22x faster                                                              |
| comprehensions             | 25.4 us                                                               | 20.8 us: 1.22x faster                                                             |
| generators                 | 43.5 ms                                                               | 36.1 ms: 1.21x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 4.01 ms: 1.16x faster                                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.54 us: 1.16x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 54.0 ms: 1.15x faster                                                             |
| regex_dna                  | 254 ms                                                                | 223 ms: 1.14x faster                                                              |
| pylint                     | 355 ms                                                                | 317 ms: 1.12x faster                                                              |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| async_generators           | 491 ms                                                                | 447 ms: 1.10x faster                                                              |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.10x faster                                                              |
| float                      | 92.1 ms                                                               | 85.4 ms: 1.08x faster                                                             |
| sympy_integrate            | 21.6 ms                                                               | 20.2 ms: 1.07x faster                                                             |
| raytrace                   | 353 ms                                                                | 330 ms: 1.07x faster                                                              |
| pyflate                    | 559 ms                                                                | 523 ms: 1.07x faster                                                              |
| crypto_pyaes               | 86.6 ms                                                               | 81.2 ms: 1.07x faster                                                             |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                            |
| html5lib                   | 65.1 ms                                                               | 61.2 ms: 1.06x faster                                                             |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                              |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                              |
| deltablue                  | 4.12 ms                                                               | 3.94 ms: 1.04x faster                                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.8 ms: 1.04x faster                                                             |
| hexiom                     | 6.98 ms                                                               | 6.72 ms: 1.04x faster                                                             |
| meteor_contest             | 112 ms                                                                | 108 ms: 1.04x faster                                                              |
| docutils                   | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                            |
| xml_etree_process          | 79.0 ms                                                               | 79.5 ms: 1.01x slower                                                             |
| coroutines                 | 29.0 ms                                                               | 29.2 ms: 1.01x slower                                                             |
| sqlite_synth               | 3.77 us                                                               | 3.80 us: 1.01x slower                                                             |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                              |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                              |
| json                       | 5.54 ms                                                               | 5.63 ms: 1.02x slower                                                             |
| scimark_lu                 | 146 ms                                                                | 148 ms: 1.02x slower                                                              |
| sympy_expand               | 454 ms                                                                | 466 ms: 1.03x slower                                                              |
| python_startup_no_site     | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                             |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                                              |
| pickle_pure_python         | 365 us                                                                | 387 us: 1.06x slower                                                              |
| typing_runtime_protocols   | 181 us                                                                | 191 us: 1.06x slower                                                              |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.07x slower                                                             |
| pprint_pformat             | 1.88 sec                                                              | 2.01 sec: 1.07x slower                                                            |
| pprint_safe_repr           | 916 ms                                                                | 988 ms: 1.08x slower                                                              |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.69 ms: 1.08x slower                                                             |
| fannkuch                   | 443 ms                                                                | 480 ms: 1.08x slower                                                              |
| telco                      | 8.51 ms                                                               | 9.20 ms: 1.08x slower                                                             |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                             |
| nbody                      | 105 ms                                                                | 125 ms: 1.19x slower                                                              |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.96 ms: 1.58x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.83 ms: 2.00x slower                                                             |
| logging_silent             | 127 ns                                                                | 609 ns: 4.80x slower                                                              |
| coverage                   | 87.3 ms                                                               | 545 ms: 6.24x slower                                                              |
| thrift                     | 937 us                                                                | 194 ms: 206.94x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                                      |

Benchmark hidden because not significant (16): chaos, regex_v8, spectral_norm, django_template, 2to3, scimark_sor, nqueens, genshi_xml, logging_format, logging_simple, pycparser, xml_etree_generate, richards_super, unpickle_pure_python, genshi_text, richards
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x