# Results vs. 3.12.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: linux-aarch64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.040x faster
- HPT reliability: 98.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 311 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.12 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                    |
| async_tree_none            | 624 ms                                                                | 396 ms: 1.57x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.3 ms: 1.11x faster                                                   |
| nbody          | 105 ms                                                                | 122 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                   |
| regex_dna      | 254 ms                                                                | 225 ms: 1.13x faster                                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.13x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.42 sec: 1.07x faster                                                  |
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 251 us: 1.04x faster                                                    |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.06x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 408 us: 1.12x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| genshi_xml     | 60.6 ms                                                               | 62.0 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.70 sec: 2.01x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                    |
| async_tree_none            | 624 ms                                                                | 396 ms: 1.57x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 334 us: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.4 ms: 1.19x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 54.1 ms: 1.15x faster                                                   |
| richards_super             | 58.5 ms                                                               | 51.3 ms: 1.14x faster                                                   |
| regex_dna                  | 254 ms                                                                | 225 ms: 1.13x faster                                                    |
| regex_compile              | 137 ms                                                                | 122 ms: 1.13x faster                                                    |
| comprehensions             | 25.4 us                                                               | 22.5 us: 1.13x faster                                                   |
| float                      | 92.1 ms                                                               | 83.3 ms: 1.11x faster                                                   |
| richards                   | 50.9 ms                                                               | 46.1 ms: 1.11x faster                                                   |
| pylint                     | 355 ms                                                                | 322 ms: 1.10x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.42 sec: 1.07x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                   |
| raytrace                   | 353 ms                                                                | 333 ms: 1.06x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 148 ms: 1.04x faster                                                    |
| pyflate                    | 559 ms                                                                | 539 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.04x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.8 ms: 1.03x faster                                                   |
| chaos                      | 71.4 ms                                                               | 69.5 ms: 1.03x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                   |
| 2to3                       | 308 ms                                                                | 311 ms: 1.01x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.81 us: 1.01x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 29.3 ms: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 62.0 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.12 sec: 1.04x slower                                                  |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 90.9 ms: 1.05x slower                                                   |
| json                       | 5.54 ms                                                               | 5.83 ms: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.51 ms: 1.08x slower                                                   |
| fannkuch                   | 443 ms                                                                | 482 ms: 1.09x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                  |
| telco                      | 8.51 ms                                                               | 9.36 ms: 1.10x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 408 us: 1.12x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                   |
| sympy_expand               | 454 ms                                                                | 509 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.15 ms: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| nbody                      | 105 ms                                                                | 122 ms: 1.17x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 219 us: 1.21x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.26 sec: 1.37x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.66 sec: 1.42x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 6.92 ms: 1.57x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.83 ms: 1.99x slower                                                   |
| logging_silent             | 127 ns                                                                | 622 ns: 4.91x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (16): scimark_sor, django_template, async_generators, html5lib, xml_etree_iterparse, sympy_str, genshi_text, xml_etree_process, xml_etree_generate, logging_format, go, spectral_norm, logging_simple, scimark_fft, pidigits, thrift
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 98.59% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x