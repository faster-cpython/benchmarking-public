# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-aarch64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.030x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 293 ms: 1.03x faster                                                              |
| docutils       | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                                            |
| html5lib       | 66.4 ms                                                  | 63.2 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 651 ms                                                   | 551 ms: 1.18x faster                                                              |
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                              |
| async_tree_none            | 497 ms                                                   | 422 ms: 1.18x faster                                                              |
| async_tree_none_tg         | 470 ms                                                   | 419 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 710 ms: 1.08x faster                                                              |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 709 ms: 1.08x faster                                                              |
| async_generators           | 489 ms                                                   | 475 ms: 1.03x faster                                                              |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                            |
| Geometric mean             | (ref)                                                    | 1.07x faster                                                                      |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 93.9 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                             |
| regex_compile  | 127 ms                                                   | 125 ms: 1.02x faster                                                              |
| regex_effbot   | 4.89 ms                                                  | 4.97 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 187 ms: 1.05x faster                                                              |
| xml_etree_iterparse  | 149 ms                                                   | 146 ms: 1.02x faster                                                              |
| json_loads           | 31.7 us                                                  | 31.2 us: 1.01x faster                                                             |
| pickle_pure_python   | 357 us                                                   | 358 us: 1.00x slower                                                              |
| unpickle_pure_python | 251 us                                                   | 254 us: 1.01x slower                                                              |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                            |
| json_dumps           | 13.6 ms                                                  | 14.7 ms: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                             |
| python_startup_no_site | 8.73 ms                                                  | 8.61 ms: 1.01x faster                                                             |
| Geometric mean         | (ref)                                                    | 1.10x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                                             |
| mako            | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                                             |
| django_template | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                                             |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.39 ms: 1.40x faster                                                             |
| deepcopy                   | 447 us                                                   | 330 us: 1.35x faster                                                              |
| deepcopy_memo              | 50.4 us                                                  | 38.0 us: 1.32x faster                                                             |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                             |
| async_tree_memoization     | 651 ms                                                   | 551 ms: 1.18x faster                                                              |
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                              |
| deepcopy_reduce            | 4.07 us                                                  | 3.46 us: 1.18x faster                                                             |
| async_tree_none            | 497 ms                                                   | 422 ms: 1.18x faster                                                              |
| go                         | 160 ms                                                   | 138 ms: 1.16x faster                                                              |
| async_tree_none_tg         | 470 ms                                                   | 419 ms: 1.12x faster                                                              |
| gc_traversal               | 5.77 ms                                                  | 5.22 ms: 1.11x faster                                                             |
| generators                 | 37.6 ms                                                  | 34.6 ms: 1.09x faster                                                             |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 710 ms: 1.08x faster                                                              |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 709 ms: 1.08x faster                                                              |
| pathlib                    | 22.7 ms                                                  | 21.4 ms: 1.06x faster                                                             |
| html5lib                   | 66.4 ms                                                  | 63.2 ms: 1.05x faster                                                             |
| xml_etree_parse            | 197 ms                                                   | 187 ms: 1.05x faster                                                              |
| thrift                     | 968 us                                                   | 926 us: 1.05x faster                                                              |
| telco                      | 9.74 ms                                                  | 9.35 ms: 1.04x faster                                                             |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                              |
| 2to3                       | 304 ms                                                   | 293 ms: 1.03x faster                                                              |
| scimark_fft                | 447 ms                                                   | 432 ms: 1.03x faster                                                              |
| bpe_tokeniser              | 5.87 sec                                                 | 5.70 sec: 1.03x faster                                                            |
| meteor_contest             | 114 ms                                                   | 110 ms: 1.03x faster                                                              |
| async_generators           | 489 ms                                                   | 475 ms: 1.03x faster                                                              |
| crypto_pyaes               | 83.7 ms                                                  | 81.4 ms: 1.03x faster                                                             |
| regex_v8                   | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                             |
| pycparser                  | 1.27 sec                                                 | 1.24 sec: 1.03x faster                                                            |
| spectral_norm              | 143 ms                                                   | 139 ms: 1.02x faster                                                              |
| xml_etree_iterparse        | 149 ms                                                   | 146 ms: 1.02x faster                                                              |
| pprint_safe_repr           | 926 ms                                                   | 908 ms: 1.02x faster                                                              |
| regex_compile              | 127 ms                                                   | 125 ms: 1.02x faster                                                              |
| richards                   | 53.6 ms                                                  | 52.6 ms: 1.02x faster                                                             |
| genshi_text                | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                                             |
| sympy_sum                  | 144 ms                                                   | 141 ms: 1.02x faster                                                              |
| logging_silent             | 133 ns                                                   | 131 ns: 1.02x faster                                                              |
| scimark_monte_carlo        | 83.6 ms                                                  | 82.3 ms: 1.02x faster                                                             |
| json_loads                 | 31.7 us                                                  | 31.2 us: 1.01x faster                                                             |
| python_startup_no_site     | 8.73 ms                                                  | 8.61 ms: 1.01x faster                                                             |
| richards_super             | 60.1 ms                                                  | 59.4 ms: 1.01x faster                                                             |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                            |
| pickle_pure_python         | 357 us                                                   | 358 us: 1.00x slower                                                              |
| float                      | 93.3 ms                                                  | 93.9 ms: 1.01x slower                                                             |
| unpickle_pure_python       | 251 us                                                   | 254 us: 1.01x slower                                                              |
| regex_effbot               | 4.89 ms                                                  | 4.97 ms: 1.02x slower                                                             |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.02x slower                                                             |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                             |
| mako                       | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                                             |
| django_template            | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                                             |
| chaos                      | 68.0 ms                                                  | 69.6 ms: 1.02x slower                                                             |
| deltablue                  | 3.82 ms                                                  | 3.93 ms: 1.03x slower                                                             |
| raytrace                   | 300 ms                                                   | 312 ms: 1.04x slower                                                              |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                            |
| pyflate                    | 556 ms                                                   | 580 ms: 1.04x slower                                                              |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                            |
| docutils                   | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                                            |
| json_dumps                 | 13.6 ms                                                  | 14.7 ms: 1.08x slower                                                             |
| bench_mp_pool              | 7.68 ms                                                  | 5.94 sec: 772.72x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                                      |

Benchmark hidden because not significant (29): xml_etree_process, tornado_http, logging_format, scimark_sparse_mat_mult, xml_etree_generate, coverage, hexiom, scimark_sor, json, nqueens, nbody, sympy_str, mdp, sqlglot_transpile, asyncio_websockets, sympy_expand, async_tree_io_tg, genshi_xml, sqlglot_optimize, coroutines, sqlglot_normalize, pidigits, bench_thread_pool, regex_dna, typing_runtime_protocols, fannkuch, sympy_integrate, logging_simple, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x