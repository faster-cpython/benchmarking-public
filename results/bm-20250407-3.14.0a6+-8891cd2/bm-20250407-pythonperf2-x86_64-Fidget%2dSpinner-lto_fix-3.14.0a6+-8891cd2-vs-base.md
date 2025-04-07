# Results vs. base

- fork: Fidget-Spinner
- ref: lto_fix
- machine: linux-x86_64
- commit hash: 8891cd2
- commit date: 2025-04-07
- overall geometric mean: 1.000x faster
- HPT reliability: 91.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                       | 274 ms: 1.00x faster                                                      |
| docutils       | 2.86 sec                                                                     | 2.85 sec: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                              |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 507 ms                                                                       | 499 ms: 1.01x faster                                                      |
| async_generators           | 411 ms                                                                       | 407 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed    | 509 ms                                                                       | 504 ms: 1.01x faster                                                      |
| async_tree_none_tg         | 275 ms                                                                       | 273 ms: 1.01x faster                                                      |
| async_tree_memoization     | 328 ms                                                                       | 332 ms: 1.01x slower                                                      |
| coroutines                 | 21.2 ms                                                                      | 21.6 ms: 1.02x slower                                                     |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                              |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_memoization_tg, async_tree_io, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 69.1 ms                                                                      | 68.1 ms: 1.02x faster                                                     |
| nbody          | 93.9 ms                                                                      | 93.4 ms: 1.01x faster                                                     |
| pidigits       | 253 ms                                                                       | 254 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                                      | 24.4 ms: 1.00x faster                                                     |
| regex_compile  | 134 ms                                                                       | 133 ms: 1.00x faster                                                      |
| regex_dna      | 232 ms                                                                       | 238 ms: 1.02x slower                                                      |
| regex_effbot   | 3.03 ms                                                                      | 3.12 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                       | 210 us: 1.02x faster                                                      |
| xml_etree_process    | 59.6 ms                                                                      | 58.3 ms: 1.02x faster                                                     |
| pickle_pure_python   | 332 us                                                                       | 328 us: 1.01x faster                                                      |
| json_dumps           | 11.3 ms                                                                      | 11.3 ms: 1.00x faster                                                     |
| xml_etree_parse      | 135 ms                                                                       | 139 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 95.5 ms                                                                      | 98.4 ms: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                              |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 10.5 ms                                                                      | 10.5 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 23.8 ms                                                                      | 22.9 ms: 1.04x faster                                                     |
| genshi_xml     | 52.8 ms                                                                      | 53.1 ms: 1.01x slower                                                     |
| mako           | 10.9 ms                                                                      | 11.1 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text                | 23.8 ms                                                                      | 22.9 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 4.77 ms                                                                      | 4.59 ms: 1.04x faster                                                     |
| scimark_lu                 | 97.8 ms                                                                      | 94.9 ms: 1.03x faster                                                     |
| pathlib                    | 17.3 ms                                                                      | 16.9 ms: 1.03x faster                                                     |
| deepcopy                   | 281 us                                                                       | 274 us: 1.02x faster                                                      |
| unpickle_pure_python       | 215 us                                                                       | 210 us: 1.02x faster                                                      |
| xml_etree_process          | 59.6 ms                                                                      | 58.3 ms: 1.02x faster                                                     |
| subparsers                 | 22.8 ms                                                                      | 22.3 ms: 1.02x faster                                                     |
| fannkuch                   | 371 ms                                                                       | 363 ms: 1.02x faster                                                      |
| sqlalchemy_imperative      | 18.1 ms                                                                      | 17.8 ms: 1.02x faster                                                     |
| scimark_monte_carlo        | 59.4 ms                                                                      | 58.3 ms: 1.02x faster                                                     |
| raytrace                   | 273 ms                                                                       | 268 ms: 1.02x faster                                                      |
| telco                      | 7.85 ms                                                                      | 7.72 ms: 1.02x faster                                                     |
| richards_super             | 52.4 ms                                                                      | 51.5 ms: 1.02x faster                                                     |
| deltablue                  | 3.25 ms                                                                      | 3.19 ms: 1.02x faster                                                     |
| meteor_contest             | 126 ms                                                                       | 124 ms: 1.02x faster                                                      |
| float                      | 69.1 ms                                                                      | 68.1 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                       | 499 ms: 1.01x faster                                                      |
| richards                   | 46.1 ms                                                                      | 45.4 ms: 1.01x faster                                                     |
| sympy_sum                  | 153 ms                                                                       | 151 ms: 1.01x faster                                                      |
| deepcopy_reduce            | 2.90 us                                                                      | 2.86 us: 1.01x faster                                                     |
| typing_runtime_protocols   | 171 us                                                                       | 170 us: 1.01x faster                                                      |
| json                       | 5.50 ms                                                                      | 5.44 ms: 1.01x faster                                                     |
| async_generators           | 411 ms                                                                       | 407 ms: 1.01x faster                                                      |
| pickle_pure_python         | 332 us                                                                       | 328 us: 1.01x faster                                                      |
| logging_silent             | 92.9 ns                                                                      | 92.0 ns: 1.01x faster                                                     |
| async_tree_cpu_io_mixed    | 509 ms                                                                       | 504 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.59 sec                                                                     | 1.58 sec: 1.01x faster                                                    |
| sympy_expand               | 488 ms                                                                       | 484 ms: 1.01x faster                                                      |
| many_optionals             | 1.01 ms                                                                      | 1.00 ms: 1.01x faster                                                     |
| async_tree_none_tg         | 275 ms                                                                       | 273 ms: 1.01x faster                                                      |
| scimark_fft                | 303 ms                                                                       | 300 ms: 1.01x faster                                                      |
| scimark_sor                | 105 ms                                                                       | 104 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 779 ms                                                                       | 773 ms: 1.01x faster                                                      |
| nbody                      | 93.9 ms                                                                      | 93.4 ms: 1.01x faster                                                     |
| dulwich_log                | 62.4 ms                                                                      | 62.0 ms: 1.01x faster                                                     |
| sympy_integrate            | 22.2 ms                                                                      | 22.1 ms: 1.01x faster                                                     |
| pyflate                    | 422 ms                                                                       | 421 ms: 1.00x faster                                                      |
| regex_v8                   | 24.4 ms                                                                      | 24.4 ms: 1.00x faster                                                     |
| deepcopy_memo              | 28.0 us                                                                      | 27.9 us: 1.00x faster                                                     |
| regex_compile              | 134 ms                                                                       | 133 ms: 1.00x faster                                                      |
| json_dumps                 | 11.3 ms                                                                      | 11.3 ms: 1.00x faster                                                     |
| 2to3                       | 275 ms                                                                       | 274 ms: 1.00x faster                                                      |
| docutils                   | 2.86 sec                                                                     | 2.85 sec: 1.00x faster                                                    |
| python_startup_no_site     | 10.5 ms                                                                      | 10.5 ms: 1.00x faster                                                     |
| pidigits                   | 253 ms                                                                       | 254 ms: 1.00x slower                                                      |
| bpe_tokeniser              | 4.67 sec                                                                     | 4.68 sec: 1.00x slower                                                    |
| crypto_pyaes               | 79.1 ms                                                                      | 79.4 ms: 1.00x slower                                                     |
| mdp                        | 1.29 sec                                                                     | 1.30 sec: 1.00x slower                                                    |
| nqueens                    | 93.7 ms                                                                      | 94.1 ms: 1.00x slower                                                     |
| genshi_xml                 | 52.8 ms                                                                      | 53.1 ms: 1.01x slower                                                     |
| sqlite_synth               | 2.82 us                                                                      | 2.83 us: 1.01x slower                                                     |
| sqlalchemy_declarative     | 146 ms                                                                       | 147 ms: 1.01x slower                                                      |
| chaos                      | 58.5 ms                                                                      | 59.0 ms: 1.01x slower                                                     |
| async_tree_memoization     | 328 ms                                                                       | 332 ms: 1.01x slower                                                      |
| connected_components       | 415 ms                                                                       | 420 ms: 1.01x slower                                                      |
| pycparser                  | 1.22 sec                                                                     | 1.24 sec: 1.01x slower                                                    |
| shortest_path              | 444 ms                                                                       | 450 ms: 1.02x slower                                                      |
| sqlglot_v2_transpile       | 1.69 ms                                                                      | 1.72 ms: 1.02x slower                                                     |
| hexiom                     | 6.16 ms                                                                      | 6.27 ms: 1.02x slower                                                     |
| mako                       | 10.9 ms                                                                      | 11.1 ms: 1.02x slower                                                     |
| sqlglot_v2_parse           | 1.30 ms                                                                      | 1.33 ms: 1.02x slower                                                     |
| go                         | 124 ms                                                                       | 126 ms: 1.02x slower                                                      |
| coroutines                 | 21.2 ms                                                                      | 21.6 ms: 1.02x slower                                                     |
| comprehensions             | 17.4 us                                                                      | 17.7 us: 1.02x slower                                                     |
| sqlglot_v2_optimize        | 55.9 ms                                                                      | 57.1 ms: 1.02x slower                                                     |
| regex_dna                  | 232 ms                                                                       | 238 ms: 1.02x slower                                                      |
| logging_simple             | 6.13 us                                                                      | 6.28 us: 1.02x slower                                                     |
| coverage                   | 79.8 ms                                                                      | 81.8 ms: 1.02x slower                                                     |
| xml_etree_parse            | 135 ms                                                                       | 139 ms: 1.02x slower                                                      |
| spectral_norm              | 87.3 ms                                                                      | 89.5 ms: 1.03x slower                                                     |
| generators                 | 28.1 ms                                                                      | 28.9 ms: 1.03x slower                                                     |
| regex_effbot               | 3.03 ms                                                                      | 3.12 ms: 1.03x slower                                                     |
| xml_etree_iterparse        | 95.5 ms                                                                      | 98.4 ms: 1.03x slower                                                     |
| gc_traversal               | 6.39 ms                                                                      | 6.58 ms: 1.03x slower                                                     |
| sqlglot_v2_normalize       | 112 ms                                                                       | 116 ms: 1.03x slower                                                      |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                              |

Benchmark hidden because not significant (19): bench_mp_pool, pylint, async_tree_io_tg, async_tree_memoization_tg, html5lib, sphinx, xml_etree_generate, django_template, json_loads, async_tree_io, python_startup, k_core, logging_format, sympy_str, tomli_loads, async_tree_none, create_gc_cycles, asyncio_websockets, bench_thread_pool

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 91.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x