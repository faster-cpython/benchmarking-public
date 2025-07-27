# Results vs. 3.12.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.018x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 310 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 466 ms: 1.67x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 460 ms: 1.61x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 883 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 912 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 652 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.5 ms: 1.12x faster                                                   |
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 129 ms: 1.23x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.77 ms: 1.23x faster                                                   |
| regex_dna      | 254 ms                                                                | 216 ms: 1.18x faster                                                    |
| regex_compile  | 137 ms                                                                | 121 ms: 1.13x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.4 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                                  |
| xml_etree_parse      | 195 ms                                                                | 177 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 251 us: 1.04x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 38.4 us: 1.03x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.53 us: 1.06x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 392 us: 1.07x slower                                                    |
| json_loads           | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| pickle_list          | 5.25 us                                                               | 5.71 us: 1.09x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                   |
| pickle               | 13.4 us                                                               | 15.6 us: 1.16x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.2 ms: 1.04x faster                                                   |
| genshi_xml      | 60.6 ms                                                               | 64.1 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.62 sec: 2.10x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 466 ms: 1.67x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 460 ms: 1.61x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 883 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 912 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 652 ms: 1.40x faster                                                    |
| deepcopy                   | 446 us                                                                | 321 us: 1.39x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.0 us: 1.34x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.77 ms: 1.23x faster                                                   |
| comprehensions             | 25.4 us                                                               | 21.5 us: 1.18x faster                                                   |
| regex_dna                  | 254 ms                                                                | 216 ms: 1.18x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.52 us: 1.17x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 53.7 ms: 1.15x faster                                                   |
| richards_super             | 58.5 ms                                                               | 50.8 ms: 1.15x faster                                                   |
| richards                   | 50.9 ms                                                               | 44.3 ms: 1.15x faster                                                   |
| regex_compile              | 137 ms                                                                | 121 ms: 1.13x faster                                                    |
| spectral_norm              | 131 ms                                                                | 116 ms: 1.13x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                                  |
| float                      | 92.1 ms                                                               | 82.5 ms: 1.12x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.58 us: 1.10x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 177 ms: 1.10x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.95 us: 1.10x faster                                                   |
| pylint                     | 355 ms                                                                | 328 ms: 1.08x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.83 ms: 1.08x faster                                                   |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 26.4 ms: 1.07x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 546 ms: 1.04x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.2 ms: 1.04x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.04x faster                                                    |
| async_generators           | 491 ms                                                                | 478 ms: 1.03x faster                                                    |
| scimark_fft                | 418 ms                                                                | 408 ms: 1.02x faster                                                    |
| pyflate                    | 559 ms                                                                | 553 ms: 1.01x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 84.3 ms: 1.01x faster                                                   |
| 2to3                       | 308 ms                                                                | 310 ms: 1.01x slower                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                    |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 38.4 us: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 461 ms: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.77 ms: 1.04x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 91.5 ms: 1.06x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.53 us: 1.06x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 64.1 ms: 1.06x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.33 sec: 1.06x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.44 ms: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.71 us: 1.09x slower                                                   |
| sympy_expand               | 454 ms                                                                | 494 ms: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 205 us: 1.14x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.16 ms: 1.16x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.6 us: 1.16x slower                                                   |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.29 sec: 1.22x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.13 sec: 1.23x slower                                                  |
| nbody                      | 105 ms                                                                | 129 ms: 1.23x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.80 ms: 1.55x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.96 ms: 2.06x slower                                                   |
| telco                      | 8.51 ms                                                               | 164 ms: 19.33x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 1.27 sec: 179.77x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (18): scimark_sor, sympy_sum, chaos, go, html5lib, sympy_str, xml_etree_process, xml_etree_generate, mako, sqlite_synth, genshi_text, asyncio_tcp_ssl, unpickle, logging_silent, scimark_lu, nqueens, thrift, coroutines
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x