# Results vs. base

- fork: nelhage
- ref: computed_goto_nomerg
- machine: linux-x86_64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.000x faster
- HPT reliability: 66.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250208-linux-x86_64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                    |
| html5lib       | 60.3 ms                                                                | 61.2 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250208-linux-x86_64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 479 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 495 ms                                                                 | 488 ms: 1.01x faster                                                    |
| coroutines                 | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                                   |
| async_tree_memoization     | 323 ms                                                                 | 325 ms: 1.01x slower                                                    |
| async_tree_none_tg         | 255 ms                                                                 | 259 ms: 1.02x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_memoization_tg, async_generators, asyncio_websockets, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250208-linux-x86_64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                                | 91.7 ms: 1.01x faster                                                   |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250208-linux-x86_64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                                | 25.2 ms: 1.04x faster                                                   |
| regex_effbot   | 3.30 ms                                                                | 3.21 ms: 1.03x faster                                                   |
| regex_compile  | 124 ms                                                                 | 125 ms: 1.01x slower                                                    |
| regex_dna      | 209 ms                                                                 | 211 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250208-linux-x86_64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 11.7 ms                                                                | 11.6 ms: 1.01x faster                                                   |
| unpickle_pure_python | 218 us                                                                 | 215 us: 1.01x faster                                                    |
| xml_etree_iterparse  | 97.0 ms                                                                | 96.5 ms: 1.00x faster                                                   |
| xml_etree_generate   | 83.0 ms                                                                | 83.4 ms: 1.00x slower                                                   |
| xml_etree_process    | 57.8 ms                                                                | 58.4 ms: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (4): tomli_loads, pickle_pure_python, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250208-linux-x86_64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250208-linux-x86_64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 31.8 ms                                                                | 31.6 ms: 1.01x faster                                                   |
| mako            | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                                   |
| genshi_xml      | 47.8 ms                                                                | 48.1 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250208-linux-x86_64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pyflate                    | 464 ms                                                                 | 435 ms: 1.07x faster                                                    |
| pycparser                  | 1.17 sec                                                               | 1.13 sec: 1.04x faster                                                  |
| regex_v8                   | 26.1 ms                                                                | 25.2 ms: 1.04x faster                                                   |
| regex_effbot               | 3.30 ms                                                                | 3.21 ms: 1.03x faster                                                   |
| logging_simple             | 5.53 us                                                                | 5.39 us: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 479 ms: 1.02x faster                                                    |
| nbody                      | 93.0 ms                                                                | 91.7 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 4.39 sec                                                               | 4.33 sec: 1.01x faster                                                  |
| async_tree_cpu_io_mixed    | 495 ms                                                                 | 488 ms: 1.01x faster                                                    |
| thrift                     | 763 us                                                                 | 753 us: 1.01x faster                                                    |
| json_dumps                 | 11.7 ms                                                                | 11.6 ms: 1.01x faster                                                   |
| spectral_norm              | 95.2 ms                                                                | 94.1 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 218 us                                                                 | 215 us: 1.01x faster                                                    |
| raytrace                   | 270 ms                                                                 | 268 ms: 1.01x faster                                                    |
| coroutines                 | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                                   |
| coverage                   | 90.2 ms                                                                | 89.5 ms: 1.01x faster                                                   |
| django_template            | 31.8 ms                                                                | 31.6 ms: 1.01x faster                                                   |
| scimark_monte_carlo        | 66.7 ms                                                                | 66.2 ms: 1.01x faster                                                   |
| sqlalchemy_declarative     | 128 ms                                                                 | 127 ms: 1.01x faster                                                    |
| fannkuch                   | 405 ms                                                                 | 403 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 97.0 ms                                                                | 96.5 ms: 1.00x faster                                                   |
| richards_super             | 50.5 ms                                                                | 50.2 ms: 1.00x faster                                                   |
| mako                       | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                                   |
| sqlglot_transpile          | 1.54 ms                                                                | 1.54 ms: 1.00x faster                                                   |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| meteor_contest             | 105 ms                                                                 | 105 ms: 1.00x slower                                                    |
| go                         | 115 ms                                                                 | 116 ms: 1.00x slower                                                    |
| sympy_integrate            | 19.6 ms                                                                | 19.6 ms: 1.00x slower                                                   |
| bench_thread_pool          | 858 us                                                                 | 860 us: 1.00x slower                                                    |
| 2to3                       | 251 ms                                                                 | 252 ms: 1.00x slower                                                    |
| scimark_sor                | 118 ms                                                                 | 118 ms: 1.00x slower                                                    |
| xml_etree_generate         | 83.0 ms                                                                | 83.4 ms: 1.00x slower                                                   |
| deepcopy                   | 257 us                                                                 | 258 us: 1.00x slower                                                    |
| genshi_xml                 | 47.8 ms                                                                | 48.1 ms: 1.01x slower                                                   |
| regex_compile              | 124 ms                                                                 | 125 ms: 1.01x slower                                                    |
| pathlib                    | 16.2 ms                                                                | 16.3 ms: 1.01x slower                                                   |
| async_tree_memoization     | 323 ms                                                                 | 325 ms: 1.01x slower                                                    |
| telco                      | 7.74 ms                                                                | 7.80 ms: 1.01x slower                                                   |
| sympy_expand               | 446 ms                                                                 | 450 ms: 1.01x slower                                                    |
| typing_runtime_protocols   | 157 us                                                                 | 158 us: 1.01x slower                                                    |
| deepcopy_memo              | 30.1 us                                                                | 30.4 us: 1.01x slower                                                   |
| json                       | 5.10 ms                                                                | 5.15 ms: 1.01x slower                                                   |
| regex_dna                  | 209 ms                                                                 | 211 ms: 1.01x slower                                                    |
| sympy_str                  | 264 ms                                                                 | 267 ms: 1.01x slower                                                    |
| create_gc_cycles           | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                                   |
| xml_etree_process          | 57.8 ms                                                                | 58.4 ms: 1.01x slower                                                   |
| richards                   | 43.8 ms                                                                | 44.3 ms: 1.01x slower                                                   |
| crypto_pyaes               | 69.7 ms                                                                | 70.4 ms: 1.01x slower                                                   |
| scimark_fft                | 334 ms                                                                 | 339 ms: 1.01x slower                                                    |
| generators                 | 27.4 ms                                                                | 27.8 ms: 1.01x slower                                                   |
| scimark_lu                 | 115 ms                                                                 | 117 ms: 1.02x slower                                                    |
| async_tree_none_tg         | 255 ms                                                                 | 259 ms: 1.02x slower                                                    |
| html5lib                   | 60.3 ms                                                                | 61.2 ms: 1.02x slower                                                   |
| deltablue                  | 3.12 ms                                                                | 3.18 ms: 1.02x slower                                                   |
| gc_traversal               | 4.63 ms                                                                | 4.73 ms: 1.02x slower                                                   |
| logging_silent             | 102 ns                                                                 | 104 ns: 1.02x slower                                                    |
| deepcopy_reduce            | 2.67 us                                                                | 2.74 us: 1.03x slower                                                   |
| nqueens                    | 78.4 ms                                                                | 81.0 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult    | 4.64 ms                                                                | 4.85 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (36): async_tree_io_tg, float, pprint_safe_repr, tomli_loads, subparsers, async_tree_memoization_tg, async_generators, chaos, docutils, bench_mp_pool, sqlglot_parse, sqlalchemy_imperative, sqlglot_normalize, comprehensions, pickle_pure_python, sqlglot_optimize, genshi_text, sphinx, pylint, logging_format, connected_components, many_optionals, python_startup_no_site, asyncio_websockets, sympy_sum, mdp, hexiom, json_loads, dulwich_log, pprint_pformat, k_core, async_tree_io, shortest_path, xml_etree_parse, sqlite_synth, async_tree_none

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 66.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x