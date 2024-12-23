# Results vs. 3.13.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.031x faster
- HPT reliability: 99.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 484 ms: 1.37x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 520 ms: 1.28x faster                                                     |
| async_tree_none            | 504 ms                                                   | 403 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 928 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 680 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 686 ms: 1.15x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.18x faster                                                             |

Benchmark hidden because not significant (3): coroutines, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                    |
| regex_compile  | 134 ms                                                   | 127 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.62 sec: 1.02x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (6): json_loads, unpickle_pure_python, xml_etree_process, json_dumps, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 41.5 ms: 1.05x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 66.6 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 346 us: 1.39x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 484 ms: 1.37x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 41.3 us: 1.28x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 520 ms: 1.28x faster                                                     |
| async_tree_none            | 504 ms                                                   | 403 ms: 1.25x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 928 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 680 ms: 1.18x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.61 us: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 686 ms: 1.15x faster                                                     |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.7 ms: 1.12x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.52 ms: 1.10x faster                                                    |
| scimark_fft                | 463 ms                                                   | 423 ms: 1.09x faster                                                     |
| generators                 | 40.3 ms                                                  | 37.1 ms: 1.09x faster                                                    |
| spectral_norm              | 143 ms                                                   | 132 ms: 1.08x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.20 ms: 1.07x faster                                                    |
| regex_compile              | 134 ms                                                   | 127 ms: 1.06x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                   |
| scimark_sor                | 164 ms                                                   | 157 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.74 sec: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.62 sec: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.56 ms: 1.05x slower                                                    |
| django_template            | 39.4 ms                                                  | 41.5 ms: 1.05x slower                                                    |
| raytrace                   | 310 ms                                                   | 327 ms: 1.05x slower                                                     |
| logging_silent             | 135 ns                                                   | 142 ns: 1.06x slower                                                     |
| comprehensions             | 20.8 us                                                  | 22.4 us: 1.08x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 66.6 ms: 1.08x slower                                                    |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| many_optionals             | 626 us                                                   | 707 us: 1.13x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.92 ms: 1.17x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.5 ms: 1.31x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 5.45 sec: 676.04x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (57): pylint, thrift, coverage, sympy_sum, sqlalchemy_declarative, scimark_monte_carlo, scimark_lu, json, coroutines, 2to3, logging_format, crypto_pyaes, html5lib, sqlglot_normalize, logging_simple, sqlalchemy_imperative, sphinx, richards_super, async_generators, meteor_contest, mdp, connected_components, djangocms, json_loads, sqlite_synth, genshi_text, regex_v8, asyncio_websockets, nqueens, unpickle_pure_python, pidigits, float, regex_dna, python_startup, bench_thread_pool, pprint_safe_repr, xml_etree_process, deltablue, shortest_path, sqlglot_transpile, pprint_pformat, sqlglot_optimize, sympy_expand, python_startup_no_site, mako, hexiom, json_dumps, pyflate, sqlglot_parse, chaos, fannkuch, pickle_pure_python, sympy_str, richards, sympy_integrate, typing_runtime_protocols, xml_etree_generate
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 99.30% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x