# Results vs. base

- fork: diegorusso
- ref: remove_jumps_aarch64
- machine: linux-aarch64
- commit hash: 460d0d3
- commit date: 2025-03-10
- overall geometric mean: 1.014x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                   | 300 ms: 1.01x faster                                                         |
| docutils       | 3.09 sec                                                                 | 3.07 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 886 ms                                                                   | 870 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 660 ms                                                                   | 652 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 652 ms                                                                   | 644 ms: 1.01x faster                                                         |
| async_tree_none_tg         | 373 ms                                                                   | 369 ms: 1.01x faster                                                         |
| async_tree_memoization     | 468 ms                                                                   | 465 ms: 1.01x faster                                                         |
| coroutines                 | 27.7 ms                                                                  | 27.8 ms: 1.00x slower                                                        |
| Geometric mean             | (ref)                                                                    | 1.01x faster                                                                 |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_none, asyncio_websockets, async_tree_memoization_tg, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 124 ms                                                                   | 122 ms: 1.02x faster                                                         |
| regex_v8       | 27.8 ms                                                                  | 28.0 ms: 1.01x slower                                                        |
| regex_effbot   | 3.79 ms                                                                  | 3.92 ms: 1.03x slower                                                        |
| regex_dna      | 237 ms                                                                   | 249 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                                    | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 269 us                                                                   | 251 us: 1.07x faster                                                         |
| tomli_loads          | 2.39 sec                                                                 | 2.31 sec: 1.04x faster                                                       |
| xml_etree_parse      | 178 ms                                                                   | 175 ms: 1.01x faster                                                         |
| xml_etree_generate   | 107 ms                                                                   | 108 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                    | 1.01x faster                                                                 |

Benchmark hidden because not significant (5): json_loads, pickle_pure_python, xml_etree_iterparse, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 15.8 ms                                                                  | 16.1 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 13.4 ms                                                                  | 12.5 ms: 1.07x faster                                                        |
| genshi_xml     | 61.2 ms                                                                  | 60.0 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                    | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| fannkuch                   | 515 ms                                                                   | 457 ms: 1.13x faster                                                         |
| pprint_safe_repr           | 1.24 sec                                                                 | 1.11 sec: 1.12x faster                                                       |
| spectral_norm              | 130 ms                                                                   | 117 ms: 1.11x faster                                                         |
| pprint_pformat             | 2.52 sec                                                                 | 2.31 sec: 1.09x faster                                                       |
| scimark_fft                | 417 ms                                                                   | 385 ms: 1.09x faster                                                         |
| pyflate                    | 581 ms                                                                   | 540 ms: 1.08x faster                                                         |
| hexiom                     | 8.12 ms                                                                  | 7.57 ms: 1.07x faster                                                        |
| mako                       | 13.4 ms                                                                  | 12.5 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 269 us                                                                   | 251 us: 1.07x faster                                                         |
| go                         | 172 ms                                                                   | 161 ms: 1.07x faster                                                         |
| richards                   | 48.1 ms                                                                  | 45.7 ms: 1.05x faster                                                        |
| crypto_pyaes               | 98.3 ms                                                                  | 93.5 ms: 1.05x faster                                                        |
| richards_super             | 53.9 ms                                                                  | 51.7 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 6.67 ms                                                                  | 6.41 ms: 1.04x faster                                                        |
| dulwich_log                | 55.8 ms                                                                  | 53.8 ms: 1.04x faster                                                        |
| tomli_loads                | 2.39 sec                                                                 | 2.31 sec: 1.04x faster                                                       |
| pycparser                  | 1.37 sec                                                                 | 1.33 sec: 1.03x faster                                                       |
| bpe_tokeniser              | 5.62 sec                                                                 | 5.45 sec: 1.03x faster                                                       |
| sqlite_synth               | 3.73 us                                                                  | 3.63 us: 1.03x faster                                                        |
| k_core                     | 2.92 sec                                                                 | 2.85 sec: 1.02x faster                                                       |
| deltablue                  | 3.89 ms                                                                  | 3.81 ms: 1.02x faster                                                        |
| genshi_xml                 | 61.2 ms                                                                  | 60.0 ms: 1.02x faster                                                        |
| async_tree_io              | 886 ms                                                                   | 870 ms: 1.02x faster                                                         |
| sympy_expand               | 475 ms                                                                   | 466 ms: 1.02x faster                                                         |
| regex_compile              | 124 ms                                                                   | 122 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 15.8 ms                                                                  | 15.5 ms: 1.02x faster                                                        |
| xml_etree_parse            | 178 ms                                                                   | 175 ms: 1.01x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                                   | 145 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 660 ms                                                                   | 652 ms: 1.01x faster                                                         |
| sympy_str                  | 271 ms                                                                   | 268 ms: 1.01x faster                                                         |
| 2to3                       | 303 ms                                                                   | 300 ms: 1.01x faster                                                         |
| raytrace                   | 317 ms                                                                   | 314 ms: 1.01x faster                                                         |
| many_optionals             | 846 us                                                                   | 837 us: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 652 ms                                                                   | 644 ms: 1.01x faster                                                         |
| async_tree_none_tg         | 373 ms                                                                   | 369 ms: 1.01x faster                                                         |
| deepcopy_memo              | 37.9 us                                                                  | 37.6 us: 1.01x faster                                                        |
| sqlglot_v2_parse           | 1.50 ms                                                                  | 1.49 ms: 1.01x faster                                                        |
| sqlglot_v2_optimize        | 62.8 ms                                                                  | 62.3 ms: 1.01x faster                                                        |
| async_tree_memoization     | 468 ms                                                                   | 465 ms: 1.01x faster                                                         |
| docutils                   | 3.09 sec                                                                 | 3.07 sec: 1.01x faster                                                       |
| generators                 | 36.0 ms                                                                  | 35.7 ms: 1.01x faster                                                        |
| coroutines                 | 27.7 ms                                                                  | 27.8 ms: 1.00x slower                                                        |
| regex_v8                   | 27.8 ms                                                                  | 28.0 ms: 1.01x slower                                                        |
| xml_etree_generate         | 107 ms                                                                   | 108 ms: 1.01x slower                                                         |
| subparsers                 | 25.1 ms                                                                  | 25.4 ms: 1.01x slower                                                        |
| python_startup             | 15.8 ms                                                                  | 16.1 ms: 1.02x slower                                                        |
| json                       | 5.69 ms                                                                  | 5.80 ms: 1.02x slower                                                        |
| shortest_path              | 571 ms                                                                   | 583 ms: 1.02x slower                                                         |
| connected_components       | 547 ms                                                                   | 559 ms: 1.02x slower                                                         |
| regex_effbot               | 3.79 ms                                                                  | 3.92 ms: 1.03x slower                                                        |
| create_gc_cycles           | 3.60 ms                                                                  | 3.73 ms: 1.04x slower                                                        |
| regex_dna                  | 237 ms                                                                   | 249 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                                    | 1.01x faster                                                                 |

Benchmark hidden because not significant (44): genshi_text, nbody, comprehensions, telco, scimark_lu, django_template, thrift, json_loads, scimark_monte_carlo, async_tree_io_tg, meteor_contest, async_tree_none, coverage, pickle_pure_python, sqlglot_v2_normalize, html5lib, sphinx, pylint, gc_traversal, typing_runtime_protocols, xml_etree_iterparse, pidigits, asyncio_websockets, async_tree_memoization_tg, xml_etree_process, sqlglot_v2_transpile, logging_format, float, sympy_integrate, nqueens, python_startup_no_site, logging_simple, logging_silent, scimark_sor, deepcopy_reduce, mdp, async_generators, sympy_sum, chaos, bench_thread_pool, deepcopy, json_dumps, pathlib, bench_mp_pool

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x