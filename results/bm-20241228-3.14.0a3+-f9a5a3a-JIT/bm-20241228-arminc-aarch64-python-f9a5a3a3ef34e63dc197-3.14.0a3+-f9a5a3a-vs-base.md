# Results vs. base

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.057x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                                                              | 324 ms: 1.05x slower                                                                                                    |
| docutils       | 3.04 sec                                                                                                            | 3.23 sec: 1.06x slower                                                                                                  |
| html5lib       | 65.4 ms                                                                                                             | 70.2 ms: 1.07x slower                                                                                                   |
| sphinx         | 1.18 sec                                                                                                            | 1.26 sec: 1.07x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 694 ms                                                                                                              | 714 ms: 1.03x slower                                                                                                    |
| async_tree_io           | 929 ms                                                                                                              | 956 ms: 1.03x slower                                                                                                    |
| async_tree_io_tg        | 910 ms                                                                                                              | 951 ms: 1.05x slower                                                                                                    |
| async_generators        | 488 ms                                                                                                              | 542 ms: 1.11x slower                                                                                                    |
| Geometric mean          | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (7): asyncio_websockets, async_tree_memoization_tg, coroutines, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                                                                              | 252 ms: 1.02x slower                                                                                                    |
| regex_compile  | 131 ms                                                                                                              | 145 ms: 1.11x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark      | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| tomli_loads    | 2.61 sec                                                                                                            | 2.54 sec: 1.03x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                            |

Benchmark hidden because not significant (8): xml_etree_parse, unpickle_pure_python, xml_etree_generate, json_dumps, json_loads, pickle_pure_python, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako            | 14.4 ms                                                                                                             | 13.4 ms: 1.07x faster                                                                                                   |
| django_template | 40.5 ms                                                                                                             | 48.3 ms: 1.19x slower                                                                                                   |
| genshi_text     | 27.7 ms                                                                                                             | 35.8 ms: 1.29x slower                                                                                                   |
| genshi_xml      | 64.5 ms                                                                                                             | 87.0 ms: 1.35x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.18x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 6.30 sec                                                                                                            | 1.56 sec: 4.04x faster                                                                                                  |
| mako                     | 14.4 ms                                                                                                             | 13.4 ms: 1.07x faster                                                                                                   |
| tomli_loads              | 2.61 sec                                                                                                            | 2.54 sec: 1.03x faster                                                                                                  |
| bpe_tokeniser            | 5.79 sec                                                                                                            | 5.84 sec: 1.01x slower                                                                                                  |
| regex_dna                | 247 ms                                                                                                              | 252 ms: 1.02x slower                                                                                                    |
| async_tree_cpu_io_mixed  | 694 ms                                                                                                              | 714 ms: 1.03x slower                                                                                                    |
| async_tree_io            | 929 ms                                                                                                              | 956 ms: 1.03x slower                                                                                                    |
| k_core                   | 2.86 sec                                                                                                            | 2.96 sec: 1.04x slower                                                                                                  |
| pyflate                  | 592 ms                                                                                                              | 616 ms: 1.04x slower                                                                                                    |
| mypy2                    | 1.06 sec                                                                                                            | 1.10 sec: 1.04x slower                                                                                                  |
| async_tree_io_tg         | 910 ms                                                                                                              | 951 ms: 1.05x slower                                                                                                    |
| 2to3                     | 308 ms                                                                                                              | 324 ms: 1.05x slower                                                                                                    |
| fannkuch                 | 480 ms                                                                                                              | 506 ms: 1.05x slower                                                                                                    |
| mdp                      | 3.41 sec                                                                                                            | 3.59 sec: 1.05x slower                                                                                                  |
| docutils                 | 3.04 sec                                                                                                            | 3.23 sec: 1.06x slower                                                                                                  |
| sqlglot_parse            | 1.48 ms                                                                                                             | 1.57 ms: 1.06x slower                                                                                                   |
| richards                 | 52.6 ms                                                                                                             | 56.0 ms: 1.06x slower                                                                                                   |
| sympy_integrate          | 22.2 ms                                                                                                             | 23.6 ms: 1.07x slower                                                                                                   |
| sphinx                   | 1.18 sec                                                                                                            | 1.26 sec: 1.07x slower                                                                                                  |
| html5lib                 | 65.4 ms                                                                                                             | 70.2 ms: 1.07x slower                                                                                                   |
| deltablue                | 3.98 ms                                                                                                             | 4.33 ms: 1.09x slower                                                                                                   |
| sympy_expand             | 482 ms                                                                                                              | 525 ms: 1.09x slower                                                                                                    |
| sqlglot_normalize        | 131 ms                                                                                                              | 144 ms: 1.09x slower                                                                                                    |
| deepcopy_reduce          | 3.67 us                                                                                                             | 4.02 us: 1.10x slower                                                                                                   |
| meteor_contest           | 117 ms                                                                                                              | 128 ms: 1.10x slower                                                                                                    |
| crypto_pyaes             | 85.2 ms                                                                                                             | 94.0 ms: 1.10x slower                                                                                                   |
| sqlglot_optimize         | 64.4 ms                                                                                                             | 71.1 ms: 1.10x slower                                                                                                   |
| spectral_norm            | 133 ms                                                                                                              | 147 ms: 1.11x slower                                                                                                    |
| scimark_sparse_mat_mult  | 6.16 ms                                                                                                             | 6.83 ms: 1.11x slower                                                                                                   |
| sqlalchemy_imperative    | 15.9 ms                                                                                                             | 17.6 ms: 1.11x slower                                                                                                   |
| logging_format           | 7.89 us                                                                                                             | 8.75 us: 1.11x slower                                                                                                   |
| regex_compile            | 131 ms                                                                                                              | 145 ms: 1.11x slower                                                                                                    |
| async_generators         | 488 ms                                                                                                              | 542 ms: 1.11x slower                                                                                                    |
| scimark_lu               | 139 ms                                                                                                              | 154 ms: 1.11x slower                                                                                                    |
| comprehensions           | 22.4 us                                                                                                             | 25.0 us: 1.11x slower                                                                                                   |
| sympy_str                | 277 ms                                                                                                              | 310 ms: 1.12x slower                                                                                                    |
| logging_simple           | 7.22 us                                                                                                             | 8.13 us: 1.13x slower                                                                                                   |
| dulwich_log              | 63.9 ms                                                                                                             | 72.5 ms: 1.14x slower                                                                                                   |
| typing_runtime_protocols | 202 us                                                                                                              | 230 us: 1.14x slower                                                                                                    |
| raytrace                 | 321 ms                                                                                                              | 367 ms: 1.14x slower                                                                                                    |
| pycparser                | 1.29 sec                                                                                                            | 1.48 sec: 1.15x slower                                                                                                  |
| deepcopy                 | 344 us                                                                                                              | 397 us: 1.15x slower                                                                                                    |
| go                       | 145 ms                                                                                                              | 168 ms: 1.16x slower                                                                                                    |
| sympy_sum                | 146 ms                                                                                                              | 171 ms: 1.17x slower                                                                                                    |
| chaos                    | 72.8 ms                                                                                                             | 86.2 ms: 1.18x slower                                                                                                   |
| many_optionals           | 724 us                                                                                                              | 860 us: 1.19x slower                                                                                                    |
| django_template          | 40.5 ms                                                                                                             | 48.3 ms: 1.19x slower                                                                                                   |
| nqueens                  | 105 ms                                                                                                              | 131 ms: 1.25x slower                                                                                                    |
| hexiom                   | 7.57 ms                                                                                                             | 9.50 ms: 1.25x slower                                                                                                   |
| genshi_text              | 27.7 ms                                                                                                             | 35.8 ms: 1.29x slower                                                                                                   |
| pprint_pformat           | 2.03 sec                                                                                                            | 2.67 sec: 1.32x slower                                                                                                  |
| pprint_safe_repr         | 996 ms                                                                                                              | 1.32 sec: 1.32x slower                                                                                                  |
| genshi_xml               | 64.5 ms                                                                                                             | 87.0 ms: 1.35x slower                                                                                                   |
| generators               | 36.6 ms                                                                                                             | 52.2 ms: 1.43x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (44): xml_etree_parse, nbody, unpickle_pure_python, regex_v8, xml_etree_generate, json_dumps, scimark_fft, pathlib, python_startup, float, gc_traversal, asyncio_websockets, regex_effbot, scimark_sor, pidigits, json_loads, pickle_pure_python, python_startup_no_site, connected_components, xml_etree_iterparse, async_tree_memoization_tg, deepcopy_memo, xml_etree_process, djangocms, coroutines, create_gc_cycles, shortest_path, scimark_monte_carlo, json, subparsers, sqlalchemy_declarative, async_tree_cpu_io_mixed_tg, async_tree_none_tg, telco, async_tree_memoization, coverage, async_tree_none, sqlite_synth, bench_thread_pool, thrift, pylint, logging_silent, sqlglot_transpile, richards_super

- Geometric mean (including insignificant results): 1.057x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.02x