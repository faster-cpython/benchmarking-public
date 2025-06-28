# Results vs. 3.12.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: linux-aarch64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.053x faster
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 310 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                  |
| html5lib       | 65.1 ms                                                               | 62.5 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 475 ms: 1.56x faster                                                    |
| async_tree_none            | 624 ms                                                                | 404 ms: 1.54x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 918 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.51x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 936 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 666 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 665 ms: 1.33x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.1 ms: 1.11x faster                                                   |
| pidigits       | 233 ms                                                                | 236 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 129 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| regex_dna      | 254 ms                                                                | 217 ms: 1.17x faster                                                    |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.5 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| json_loads          | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 396 us: 1.09x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.67 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                   |
| mako            | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 62.5 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.66 sec: 2.06x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 475 ms: 1.56x faster                                                    |
| async_tree_none            | 624 ms                                                                | 404 ms: 1.54x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 918 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.51x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 936 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 666 ms: 1.37x faster                                                    |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 665 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.8 us: 1.31x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.2 ms: 1.24x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| regex_dna                  | 254 ms                                                                | 217 ms: 1.17x faster                                                    |
| richards                   | 50.9 ms                                                               | 44.3 ms: 1.15x faster                                                   |
| richards_super             | 58.5 ms                                                               | 51.3 ms: 1.14x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.4 us: 1.13x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.62 us: 1.13x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                  |
| dulwich_log                | 62.0 ms                                                               | 55.4 ms: 1.12x faster                                                   |
| pylint                     | 355 ms                                                                | 320 ms: 1.11x faster                                                    |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| float                      | 92.1 ms                                                               | 83.1 ms: 1.11x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| spectral_norm              | 131 ms                                                                | 119 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.02 us: 1.09x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.76 us: 1.08x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 26.5 ms: 1.07x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                   |
| scimark_sor                | 150 ms                                                                | 141 ms: 1.06x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                   |
| raytrace                   | 353 ms                                                                | 333 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.3 ms: 1.06x faster                                                   |
| pyflate                    | 559 ms                                                                | 531 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.5 ms: 1.04x faster                                                   |
| async_generators           | 491 ms                                                                | 473 ms: 1.04x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.66 us: 1.03x faster                                                   |
| go                         | 157 ms                                                                | 156 ms: 1.01x faster                                                    |
| 2to3                       | 308 ms                                                                | 310 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.02x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 62.5 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.67 ms: 1.04x slower                                                   |
| json                       | 5.54 ms                                                               | 5.77 ms: 1.04x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                  |
| sympy_expand               | 454 ms                                                                | 478 ms: 1.05x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.43 ms: 1.07x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.08x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.09x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                  |
| crypto_pyaes               | 86.6 ms                                                               | 95.3 ms: 1.10x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.38 ms: 1.10x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 203 us: 1.13x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.08 ms: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                    |
| nbody                      | 105 ms                                                                | 129 ms: 1.24x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.14 sec: 1.24x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.34 sec: 1.25x slower                                                  |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.93 ms: 1.58x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.75 ms: 1.95x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x faster                                                            |

Benchmark hidden because not significant (14): chaos, sympy_integrate, unpickle_pure_python, scimark_fft, sympy_sum, xml_etree_process, sympy_str, asyncio_websockets, logging_silent, scimark_lu, coroutines, genshi_text, thrift, nqueens
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 99.60% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x