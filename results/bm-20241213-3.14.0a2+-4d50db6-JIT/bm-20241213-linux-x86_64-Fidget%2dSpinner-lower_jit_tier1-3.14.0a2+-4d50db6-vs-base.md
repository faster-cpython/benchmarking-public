# Results vs. base

- fork: Fidget-Spinner
- ref: lower_jit_tier1
- machine: linux-x86_64
- commit hash: 4d50db6
- commit date: 2024-12-13
- overall geometric mean: 1.001x slower
- HPT reliability: 97.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2+-487fdbe | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                 | 260 ms: 1.01x slower                                                        |
| docutils       | 2.67 sec                                                               | 2.73 sec: 1.02x slower                                                      |
| html5lib       | 65.1 ms                                                                | 64.2 ms: 1.01x faster                                                       |
| sphinx         | 1.05 sec                                                               | 1.06 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2+-487fdbe | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines       | 24.3 ms                                                                | 23.9 ms: 1.02x faster                                                       |
| async_generators | 451 ms                                                                 | 446 ms: 1.01x faster                                                        |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, asyncio_websockets, async_tree_memoization_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2+-487fdbe | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 86.3 ms                                                                | 83.6 ms: 1.03x faster                                                       |
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2+-487fdbe | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.43 ms                                                                | 3.21 ms: 1.07x faster                                                       |
| regex_dna      | 216 ms                                                                 | 211 ms: 1.02x faster                                                        |
| regex_v8       | 25.4 ms                                                                | 25.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2+-487fdbe | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps          | 11.3 ms                                                                | 11.1 ms: 1.01x faster                                                       |
| json_loads          | 26.4 us                                                                | 26.0 us: 1.01x faster                                                       |
| xml_etree_iterparse | 94.1 ms                                                                | 94.7 ms: 1.01x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (6): unpickle_pure_python, xml_etree_process, tomli_loads, xml_etree_generate, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2+-487fdbe | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                       |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2+-487fdbe | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                                | 56.2 ms: 1.02x faster                                                       |
| genshi_text     | 24.2 ms                                                                | 23.7 ms: 1.02x faster                                                       |
| mako            | 10.1 ms                                                                | 9.95 ms: 1.01x faster                                                       |
| django_template | 33.3 ms                                                                | 34.2 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2+-487fdbe | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot            | 3.43 ms                                                                | 3.21 ms: 1.07x faster                                                       |
| gc_traversal            | 4.94 ms                                                                | 4.77 ms: 1.03x faster                                                       |
| nbody                   | 86.3 ms                                                                | 83.6 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult | 4.89 ms                                                                | 4.76 ms: 1.03x faster                                                       |
| generators              | 34.9 ms                                                                | 34.2 ms: 1.02x faster                                                       |
| genshi_xml              | 57.3 ms                                                                | 56.2 ms: 1.02x faster                                                       |
| genshi_text             | 24.2 ms                                                                | 23.7 ms: 1.02x faster                                                       |
| regex_dna               | 216 ms                                                                 | 211 ms: 1.02x faster                                                        |
| coroutines              | 24.3 ms                                                                | 23.9 ms: 1.02x faster                                                       |
| telco                   | 7.57 ms                                                                | 7.46 ms: 1.02x faster                                                       |
| mako                    | 10.1 ms                                                                | 9.95 ms: 1.01x faster                                                       |
| json_dumps              | 11.3 ms                                                                | 11.1 ms: 1.01x faster                                                       |
| html5lib                | 65.1 ms                                                                | 64.2 ms: 1.01x faster                                                       |
| json_loads              | 26.4 us                                                                | 26.0 us: 1.01x faster                                                       |
| deepcopy_reduce         | 2.70 us                                                                | 2.67 us: 1.01x faster                                                       |
| coverage                | 83.9 ms                                                                | 82.9 ms: 1.01x faster                                                       |
| deepcopy_memo           | 29.8 us                                                                | 29.4 us: 1.01x faster                                                       |
| async_generators        | 451 ms                                                                 | 446 ms: 1.01x faster                                                        |
| scimark_monte_carlo     | 63.4 ms                                                                | 62.8 ms: 1.01x faster                                                       |
| subparsers              | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                       |
| pathlib                 | 16.2 ms                                                                | 16.0 ms: 1.01x faster                                                       |
| json                    | 4.80 ms                                                                | 4.76 ms: 1.01x faster                                                       |
| regex_v8                | 25.4 ms                                                                | 25.2 ms: 1.01x faster                                                       |
| logging_format          | 6.41 us                                                                | 6.35 us: 1.01x faster                                                       |
| pyflate                 | 441 ms                                                                 | 438 ms: 1.01x faster                                                        |
| scimark_sor             | 119 ms                                                                 | 118 ms: 1.01x faster                                                        |
| hexiom                  | 6.97 ms                                                                | 6.93 ms: 1.01x faster                                                       |
| create_gc_cycles        | 2.44 ms                                                                | 2.44 ms: 1.00x faster                                                       |
| pidigits                | 186 ms                                                                 | 187 ms: 1.00x slower                                                        |
| python_startup_no_site  | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                       |
| bench_thread_pool       | 881 us                                                                 | 884 us: 1.00x slower                                                        |
| scimark_fft             | 331 ms                                                                 | 333 ms: 1.00x slower                                                        |
| python_startup          | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                       |
| sqlalchemy_declarative  | 129 ms                                                                 | 129 ms: 1.00x slower                                                        |
| sqlglot_normalize       | 108 ms                                                                 | 109 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 94.1 ms                                                                | 94.7 ms: 1.01x slower                                                       |
| sqlglot_transpile       | 1.61 ms                                                                | 1.62 ms: 1.01x slower                                                       |
| bpe_tokeniser           | 4.36 sec                                                               | 4.39 sec: 1.01x slower                                                      |
| spectral_norm           | 112 ms                                                                 | 113 ms: 1.01x slower                                                        |
| sqlglot_optimize        | 54.5 ms                                                                | 55.0 ms: 1.01x slower                                                       |
| fannkuch                | 378 ms                                                                 | 382 ms: 1.01x slower                                                        |
| sympy_integrate         | 20.6 ms                                                                | 20.8 ms: 1.01x slower                                                       |
| 2to3                    | 257 ms                                                                 | 260 ms: 1.01x slower                                                        |
| many_optionals          | 982 us                                                                 | 992 us: 1.01x slower                                                        |
| shortest_path           | 477 ms                                                                 | 482 ms: 1.01x slower                                                        |
| dulwich_log             | 68.1 ms                                                                | 68.9 ms: 1.01x slower                                                       |
| sympy_sum               | 155 ms                                                                 | 157 ms: 1.01x slower                                                        |
| sphinx                  | 1.05 sec                                                               | 1.06 sec: 1.01x slower                                                      |
| sqlglot_parse           | 1.28 ms                                                                | 1.30 ms: 1.01x slower                                                       |
| connected_components    | 431 ms                                                                 | 437 ms: 1.01x slower                                                        |
| pprint_safe_repr        | 744 ms                                                                 | 755 ms: 1.01x slower                                                        |
| sympy_expand            | 477 ms                                                                 | 484 ms: 1.01x slower                                                        |
| sympy_str               | 282 ms                                                                 | 287 ms: 1.02x slower                                                        |
| pprint_pformat          | 1.51 sec                                                               | 1.54 sec: 1.02x slower                                                      |
| sqlalchemy_imperative   | 16.5 ms                                                                | 16.9 ms: 1.02x slower                                                       |
| docutils                | 2.67 sec                                                               | 2.73 sec: 1.02x slower                                                      |
| django_template         | 33.3 ms                                                                | 34.2 ms: 1.03x slower                                                       |
| richards                | 43.9 ms                                                                | 45.6 ms: 1.04x slower                                                       |
| richards_super          | 50.0 ms                                                                | 52.3 ms: 1.04x slower                                                       |
| pycparser               | 1.13 sec                                                               | 1.20 sec: 1.07x slower                                                      |
| mdp                     | 2.60 sec                                                               | 2.81 sec: 1.08x slower                                                      |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (37): nqueens, chaos, async_tree_memoization, sqlite_synth, unpickle_pure_python, go, float, xml_etree_process, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, deepcopy, async_tree_none_tg, comprehensions, meteor_contest, tomli_loads, async_tree_none, xml_etree_generate, bench_mp_pool, crypto_pyaes, logging_simple, typing_runtime_protocols, xml_etree_parse, asyncio_websockets, thrift, deltablue, regex_compile, raytrace, async_tree_memoization_tg, pickle_pure_python, async_tree_io, scimark_lu, k_core, djangocms, logging_silent, mypy2, async_tree_io_tg, pylint

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 97.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x