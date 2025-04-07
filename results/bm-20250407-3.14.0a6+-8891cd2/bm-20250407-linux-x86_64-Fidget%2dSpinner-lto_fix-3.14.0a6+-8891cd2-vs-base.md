# Results vs. base

- fork: Fidget-Spinner
- ref: lto_fix
- machine: linux-x86_64
- commit hash: 8891cd2
- commit date: 2025-04-07
- overall geometric mean: 1.004x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 250 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 23.7 ms                                                                | 23.6 ms: 1.01x faster                                               |
| async_tree_memoization     | 307 ms                                                                 | 311 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed    | 478 ms                                                                 | 484 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 481 ms: 1.02x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (7): async_tree_io_tg, async_generators, async_tree_io, asyncio_websockets, async_tree_none, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 87.2 ms                                                                | 91.0 ms: 1.04x slower                                               |
| pidigits       | 186 ms                                                                 | 194 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                                | 22.7 ms: 1.05x faster                                               |
| regex_dna      | 210 ms                                                                 | 205 ms: 1.03x faster                                                |
| regex_effbot   | 3.12 ms                                                                | 3.04 ms: 1.03x faster                                               |
| regex_compile  | 123 ms                                                                 | 124 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 29.8 us                                                                | 29.0 us: 1.03x faster                                               |
| json_dumps           | 11.6 ms                                                                | 11.3 ms: 1.02x faster                                               |
| unpickle_pure_python | 214 us                                                                 | 211 us: 1.01x faster                                                |
| pickle_pure_python   | 312 us                                                                 | 314 us: 1.00x slower                                                |
| xml_etree_process    | 58.1 ms                                                                | 58.5 ms: 1.01x slower                                               |
| xml_etree_generate   | 83.0 ms                                                                | 84.2 ms: 1.01x slower                                               |
| tomli_loads          | 1.93 sec                                                               | 1.97 sec: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                               |
| python_startup_no_site | 8.17 ms                                                                | 8.20 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 20.6 ms                                                                | 21.1 ms: 1.02x slower                                               |
| mako           | 11.0 ms                                                                | 11.3 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8                   | 23.8 ms                                                                | 22.7 ms: 1.05x faster                                               |
| gc_traversal               | 5.01 ms                                                                | 4.79 ms: 1.05x faster                                               |
| json_loads                 | 29.8 us                                                                | 29.0 us: 1.03x faster                                               |
| json                       | 5.36 ms                                                                | 5.21 ms: 1.03x faster                                               |
| regex_dna                  | 210 ms                                                                 | 205 ms: 1.03x faster                                                |
| regex_effbot               | 3.12 ms                                                                | 3.04 ms: 1.03x faster                                               |
| pprint_safe_repr           | 722 ms                                                                 | 704 ms: 1.03x faster                                                |
| json_dumps                 | 11.6 ms                                                                | 11.3 ms: 1.02x faster                                               |
| generators                 | 29.6 ms                                                                | 29.2 ms: 1.02x faster                                               |
| pprint_pformat             | 1.47 sec                                                               | 1.45 sec: 1.02x faster                                              |
| deepcopy_memo              | 28.6 us                                                                | 28.2 us: 1.01x faster                                               |
| unpickle_pure_python       | 214 us                                                                 | 211 us: 1.01x faster                                                |
| logging_silent             | 96.6 ns                                                                | 95.5 ns: 1.01x faster                                               |
| mdp                        | 1.23 sec                                                               | 1.22 sec: 1.01x faster                                              |
| telco                      | 7.72 ms                                                                | 7.68 ms: 1.01x faster                                               |
| coroutines                 | 23.7 ms                                                                | 23.6 ms: 1.01x faster                                               |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.7 ms: 1.00x faster                                               |
| sqlglot_v2_transpile       | 1.52 ms                                                                | 1.52 ms: 1.00x faster                                               |
| create_gc_cycles           | 2.46 ms                                                                | 2.47 ms: 1.00x slower                                               |
| python_startup             | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                               |
| many_optionals             | 925 us                                                                 | 929 us: 1.00x slower                                                |
| python_startup_no_site     | 8.17 ms                                                                | 8.20 ms: 1.00x slower                                               |
| pickle_pure_python         | 312 us                                                                 | 314 us: 1.00x slower                                                |
| 2to3                       | 249 ms                                                                 | 250 ms: 1.01x slower                                                |
| crypto_pyaes               | 72.4 ms                                                                | 72.7 ms: 1.01x slower                                               |
| richards_super             | 49.2 ms                                                                | 49.5 ms: 1.01x slower                                               |
| subparsers                 | 20.8 ms                                                                | 20.9 ms: 1.01x slower                                               |
| go                         | 109 ms                                                                 | 109 ms: 1.01x slower                                                |
| xml_etree_process          | 58.1 ms                                                                | 58.5 ms: 1.01x slower                                               |
| bpe_tokeniser              | 4.52 sec                                                               | 4.55 sec: 1.01x slower                                              |
| typing_runtime_protocols   | 163 us                                                                 | 164 us: 1.01x slower                                                |
| sympy_str                  | 265 ms                                                                 | 267 ms: 1.01x slower                                                |
| regex_compile              | 123 ms                                                                 | 124 ms: 1.01x slower                                                |
| sympy_expand               | 451 ms                                                                 | 454 ms: 1.01x slower                                                |
| sympy_integrate            | 19.0 ms                                                                | 19.2 ms: 1.01x slower                                               |
| deltablue                  | 3.30 ms                                                                | 3.33 ms: 1.01x slower                                               |
| sqlite_synth               | 2.76 us                                                                | 2.79 us: 1.01x slower                                               |
| sqlglot_v2_optimize        | 51.5 ms                                                                | 52.0 ms: 1.01x slower                                               |
| scimark_sor                | 114 ms                                                                 | 115 ms: 1.01x slower                                                |
| scimark_lu                 | 115 ms                                                                 | 116 ms: 1.01x slower                                                |
| async_tree_memoization     | 307 ms                                                                 | 311 ms: 1.01x slower                                                |
| fannkuch                   | 401 ms                                                                 | 406 ms: 1.01x slower                                                |
| sympy_sum                  | 147 ms                                                                 | 149 ms: 1.01x slower                                                |
| hexiom                     | 6.16 ms                                                                | 6.24 ms: 1.01x slower                                               |
| nqueens                    | 80.3 ms                                                                | 81.3 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 478 ms                                                                 | 484 ms: 1.01x slower                                                |
| sqlalchemy_declarative     | 130 ms                                                                 | 132 ms: 1.01x slower                                                |
| xml_etree_generate         | 83.0 ms                                                                | 84.2 ms: 1.01x slower                                               |
| coverage                   | 84.6 ms                                                                | 85.8 ms: 1.01x slower                                               |
| shortest_path              | 492 ms                                                                 | 499 ms: 1.01x slower                                                |
| scimark_monte_carlo        | 64.1 ms                                                                | 65.1 ms: 1.02x slower                                               |
| chaos                      | 55.3 ms                                                                | 56.2 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 481 ms: 1.02x slower                                                |
| tomli_loads                | 1.93 sec                                                               | 1.97 sec: 1.02x slower                                              |
| spectral_norm              | 100 ms                                                                 | 102 ms: 1.02x slower                                                |
| genshi_text                | 20.6 ms                                                                | 21.1 ms: 1.02x slower                                               |
| raytrace                   | 253 ms                                                                 | 259 ms: 1.02x slower                                                |
| mako                       | 11.0 ms                                                                | 11.3 ms: 1.03x slower                                               |
| scimark_fft                | 333 ms                                                                 | 346 ms: 1.04x slower                                                |
| nbody                      | 87.2 ms                                                                | 91.0 ms: 1.04x slower                                               |
| pidigits                   | 186 ms                                                                 | 194 ms: 1.04x slower                                                |
| pyflate                    | 419 ms                                                                 | 439 ms: 1.05x slower                                                |
| scimark_sparse_mat_mult    | 4.62 ms                                                                | 4.86 ms: 1.05x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (32): async_tree_io_tg, k_core, logging_simple, logging_format, sphinx, genshi_xml, deepcopy, docutils, async_generators, xml_etree_iterparse, bench_thread_pool, connected_components, richards, sqlglot_v2_parse, sqlglot_v2_normalize, comprehensions, django_template, async_tree_io, pathlib, asyncio_websockets, dulwich_log, async_tree_none, pylint, meteor_contest, bench_mp_pool, float, xml_etree_parse, deepcopy_reduce, async_tree_none_tg, html5lib, pycparser, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x