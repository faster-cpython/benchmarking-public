# Results vs. 3.12.0

- fork: python
- ref: 1e69cd1634e4f0f8c375
- machine: linux-aarch64
- commit hash: 1e69cd1
- commit date: 2025-07-25
- overall geometric mean: 1.016x faster
- HPT reliability: 99.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 311 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 395 ms: 1.58x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 900 ms: 1.57x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 667 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 658 ms: 1.34x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.4 ms: 1.12x faster                                                   |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 129 ms: 1.23x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.79 ms: 1.22x faster                                                   |
| regex_dna      | 254 ms                                                                | 218 ms: 1.17x faster                                                    |
| regex_compile  | 137 ms                                                                | 125 ms: 1.09x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.3 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 178 ms: 1.09x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| json_loads          | 30.7 us                                                               | 33.4 us: 1.09x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 403 us: 1.10x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.56 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.32x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.1 ms: 1.04x faster                                                   |
| genshi_xml      | 60.6 ms                                                               | 64.8 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.67 sec: 2.04x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 395 ms: 1.58x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 900 ms: 1.57x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 667 ms: 1.37x faster                                                    |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 658 ms: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.1 us: 1.34x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.79 ms: 1.22x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.6 ms: 1.22x faster                                                   |
| regex_dna                  | 254 ms                                                                | 218 ms: 1.17x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 53.2 ms: 1.17x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.3 us: 1.14x faster                                                   |
| richards_super             | 58.5 ms                                                               | 51.5 ms: 1.14x faster                                                   |
| richards                   | 50.9 ms                                                               | 45.0 ms: 1.13x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.63 us: 1.13x faster                                                   |
| float                      | 92.1 ms                                                               | 82.4 ms: 1.12x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                   |
| spectral_norm              | 131 ms                                                                | 119 ms: 1.10x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.09x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.09x faster                                                    |
| pylint                     | 355 ms                                                                | 325 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.68 us: 1.09x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.04 us: 1.09x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 26.3 ms: 1.08x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                   |
| raytrace                   | 353 ms                                                                | 333 ms: 1.06x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 148 ms: 1.05x faster                                                    |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.04x faster                                                    |
| pyflate                    | 559 ms                                                                | 536 ms: 1.04x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.1 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.03x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| go                         | 157 ms                                                                | 154 ms: 1.02x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.71 us: 1.02x faster                                                   |
| 2to3                       | 308 ms                                                                | 311 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.56 ms: 1.02x slower                                                   |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                                  |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| fannkuch                   | 443 ms                                                                | 467 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.84 ms: 1.05x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 64.8 ms: 1.07x slower                                                   |
| sympy_expand               | 454 ms                                                                | 488 ms: 1.08x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.52 ms: 1.08x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 93.5 ms: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| json_loads                 | 30.7 us                                                               | 33.4 us: 1.09x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 403 us: 1.10x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 203 us: 1.12x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.23 ms: 1.17x slower                                                   |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.30 sec: 1.22x slower                                                  |
| nbody                      | 105 ms                                                                | 129 ms: 1.23x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.14 sec: 1.24x slower                                                  |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.32x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.82 ms: 1.55x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.76 ms: 1.96x slower                                                   |
| telco                      | 8.51 ms                                                               | 164 ms: 19.24x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (15): scimark_monte_carlo, sympy_str, chaos, unpickle_pure_python, scimark_fft, html5lib, genshi_text, scimark_lu, async_generators, mako, thrift, xml_etree_process, meteor_contest, coroutines, nqueens
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 99.59% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x