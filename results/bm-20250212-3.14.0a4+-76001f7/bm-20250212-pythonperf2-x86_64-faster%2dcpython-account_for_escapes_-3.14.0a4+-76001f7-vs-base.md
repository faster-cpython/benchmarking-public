# Results vs. base

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 76001f7
- commit date: 2025-02-12
- overall geometric mean: 1.007x slower
- HPT reliability: 87.71%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 283 ms: 1.01x slower                                                                   |
| docutils       | 2.87 sec                                                                     | 2.87 sec: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                                       | 282 ms: 1.01x faster                                                                   |
| async_tree_none            | 295 ms                                                                       | 292 ms: 1.01x faster                                                                   |
| asyncio_websockets         | 385 ms                                                                       | 383 ms: 1.01x faster                                                                   |
| async_generators           | 411 ms                                                                       | 408 ms: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                                       | 522 ms: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 515 ms                                                                       | 511 ms: 1.01x faster                                                                   |
| async_tree_memoization     | 357 ms                                                                       | 355 ms: 1.01x faster                                                                   |
| coroutines                 | 21.1 ms                                                                      | 21.4 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 101 ms                                                                       | 91.7 ms: 1.10x faster                                                                  |
| pidigits       | 254 ms                                                                       | 255 ms: 1.00x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.12 ms                                                                      | 3.08 ms: 1.01x faster                                                                  |
| regex_v8       | 25.6 ms                                                                      | 25.5 ms: 1.00x faster                                                                  |
| regex_dna      | 237 ms                                                                       | 238 ms: 1.01x slower                                                                   |
| regex_compile  | 134 ms                                                                       | 135 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_loads           | 26.7 us                                                                      | 26.4 us: 1.01x faster                                                                  |
| tomli_loads          | 2.06 sec                                                                     | 2.04 sec: 1.01x faster                                                                 |
| xml_etree_process    | 59.6 ms                                                                      | 59.9 ms: 1.01x slower                                                                  |
| pickle_pure_python   | 327 us                                                                       | 332 us: 1.02x slower                                                                   |
| json_dumps           | 11.5 ms                                                                      | 11.7 ms: 1.02x slower                                                                  |
| xml_etree_iterparse  | 95.4 ms                                                                      | 97.7 ms: 1.02x slower                                                                  |
| unpickle_pure_python | 207 us                                                                       | 213 us: 1.03x slower                                                                   |
| xml_etree_parse      | 134 ms                                                                       | 140 ms: 1.04x slower                                                                   |
| Geometric mean       | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                                      | 16.0 ms: 1.00x slower                                                                  |
| python_startup_no_site | 9.00 ms                                                                      | 9.03 ms: 1.00x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                                      | 35.7 ms: 1.01x slower                                                                  |
| mako            | 10.6 ms                                                                      | 10.8 ms: 1.02x slower                                                                  |
| genshi_text     | 23.4 ms                                                                      | 24.1 ms: 1.03x slower                                                                  |
| genshi_xml      | 52.2 ms                                                                      | 54.6 ms: 1.05x slower                                                                  |
| Geometric mean  | (ref)                                                                        | 1.03x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody                      | 101 ms                                                                       | 91.7 ms: 1.10x faster                                                                  |
| scimark_sparse_mat_mult    | 4.86 ms                                                                      | 4.56 ms: 1.07x faster                                                                  |
| scimark_lu                 | 95.7 ms                                                                      | 93.5 ms: 1.02x faster                                                                  |
| logging_silent             | 97.7 ns                                                                      | 96.3 ns: 1.02x faster                                                                  |
| async_tree_none_tg         | 285 ms                                                                       | 282 ms: 1.01x faster                                                                   |
| pyflate                    | 445 ms                                                                       | 439 ms: 1.01x faster                                                                   |
| chaos                      | 60.2 ms                                                                      | 59.4 ms: 1.01x faster                                                                  |
| regex_effbot               | 3.12 ms                                                                      | 3.08 ms: 1.01x faster                                                                  |
| async_tree_none            | 295 ms                                                                       | 292 ms: 1.01x faster                                                                   |
| spectral_norm              | 85.1 ms                                                                      | 84.1 ms: 1.01x faster                                                                  |
| json_loads                 | 26.7 us                                                                      | 26.4 us: 1.01x faster                                                                  |
| scimark_fft                | 313 ms                                                                       | 310 ms: 1.01x faster                                                                   |
| telco                      | 7.95 ms                                                                      | 7.88 ms: 1.01x faster                                                                  |
| connected_components       | 414 ms                                                                       | 411 ms: 1.01x faster                                                                   |
| asyncio_websockets         | 385 ms                                                                       | 383 ms: 1.01x faster                                                                   |
| async_generators           | 411 ms                                                                       | 408 ms: 1.01x faster                                                                   |
| go                         | 127 ms                                                                       | 126 ms: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                                       | 522 ms: 1.01x faster                                                                   |
| sympy_sum                  | 152 ms                                                                       | 151 ms: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 515 ms                                                                       | 511 ms: 1.01x faster                                                                   |
| tomli_loads                | 2.06 sec                                                                     | 2.04 sec: 1.01x faster                                                                 |
| async_tree_memoization     | 357 ms                                                                       | 355 ms: 1.01x faster                                                                   |
| scimark_monte_carlo        | 60.8 ms                                                                      | 60.5 ms: 1.00x faster                                                                  |
| regex_v8                   | 25.6 ms                                                                      | 25.5 ms: 1.00x faster                                                                  |
| mdp                        | 2.50 sec                                                                     | 2.49 sec: 1.00x faster                                                                 |
| docutils                   | 2.87 sec                                                                     | 2.87 sec: 1.00x faster                                                                 |
| sympy_integrate            | 23.1 ms                                                                      | 23.1 ms: 1.00x faster                                                                  |
| python_startup             | 16.0 ms                                                                      | 16.0 ms: 1.00x slower                                                                  |
| python_startup_no_site     | 9.00 ms                                                                      | 9.03 ms: 1.00x slower                                                                  |
| shortest_path              | 443 ms                                                                       | 445 ms: 1.00x slower                                                                   |
| pidigits                   | 254 ms                                                                       | 255 ms: 1.00x slower                                                                   |
| sympy_str                  | 287 ms                                                                       | 289 ms: 1.01x slower                                                                   |
| sqlalchemy_imperative      | 17.8 ms                                                                      | 17.9 ms: 1.01x slower                                                                  |
| xml_etree_process          | 59.6 ms                                                                      | 59.9 ms: 1.01x slower                                                                  |
| regex_dna                  | 237 ms                                                                       | 238 ms: 1.01x slower                                                                   |
| sympy_expand               | 488 ms                                                                       | 491 ms: 1.01x slower                                                                   |
| regex_compile              | 134 ms                                                                       | 135 ms: 1.01x slower                                                                   |
| 2to3                       | 281 ms                                                                       | 283 ms: 1.01x slower                                                                   |
| many_optionals             | 995 us                                                                       | 1.01 ms: 1.01x slower                                                                  |
| bpe_tokeniser              | 4.56 sec                                                                     | 4.61 sec: 1.01x slower                                                                 |
| coverage                   | 78.0 ms                                                                      | 78.9 ms: 1.01x slower                                                                  |
| subparsers                 | 22.6 ms                                                                      | 22.9 ms: 1.01x slower                                                                  |
| typing_runtime_protocols   | 167 us                                                                       | 169 us: 1.01x slower                                                                   |
| richards_super             | 52.1 ms                                                                      | 52.8 ms: 1.01x slower                                                                  |
| meteor_contest             | 125 ms                                                                       | 126 ms: 1.01x slower                                                                   |
| pprint_pformat             | 1.61 sec                                                                     | 1.63 sec: 1.01x slower                                                                 |
| django_template            | 35.2 ms                                                                      | 35.7 ms: 1.01x slower                                                                  |
| hexiom                     | 6.07 ms                                                                      | 6.16 ms: 1.01x slower                                                                  |
| comprehensions             | 17.0 us                                                                      | 17.3 us: 1.01x slower                                                                  |
| raytrace                   | 276 ms                                                                       | 280 ms: 1.02x slower                                                                   |
| sqlglot_optimize           | 56.8 ms                                                                      | 57.7 ms: 1.02x slower                                                                  |
| pickle_pure_python         | 327 us                                                                       | 332 us: 1.02x slower                                                                   |
| coroutines                 | 21.1 ms                                                                      | 21.4 ms: 1.02x slower                                                                  |
| pprint_safe_repr           | 783 ms                                                                       | 795 ms: 1.02x slower                                                                   |
| fannkuch                   | 362 ms                                                                       | 368 ms: 1.02x slower                                                                   |
| json_dumps                 | 11.5 ms                                                                      | 11.7 ms: 1.02x slower                                                                  |
| crypto_pyaes               | 71.7 ms                                                                      | 73.1 ms: 1.02x slower                                                                  |
| mako                       | 10.6 ms                                                                      | 10.8 ms: 1.02x slower                                                                  |
| xml_etree_iterparse        | 95.4 ms                                                                      | 97.7 ms: 1.02x slower                                                                  |
| pycparser                  | 1.24 sec                                                                     | 1.27 sec: 1.02x slower                                                                 |
| gc_traversal               | 6.37 ms                                                                      | 6.52 ms: 1.02x slower                                                                  |
| sqlglot_normalize          | 115 ms                                                                       | 118 ms: 1.03x slower                                                                   |
| richards                   | 45.8 ms                                                                      | 47.0 ms: 1.03x slower                                                                  |
| deepcopy_memo              | 29.5 us                                                                      | 30.4 us: 1.03x slower                                                                  |
| unpickle_pure_python       | 207 us                                                                       | 213 us: 1.03x slower                                                                   |
| sqlglot_transpile          | 1.72 ms                                                                      | 1.77 ms: 1.03x slower                                                                  |
| genshi_text                | 23.4 ms                                                                      | 24.1 ms: 1.03x slower                                                                  |
| create_gc_cycles           | 2.73 ms                                                                      | 2.81 ms: 1.03x slower                                                                  |
| deepcopy_reduce            | 2.89 us                                                                      | 2.98 us: 1.03x slower                                                                  |
| sqlglot_parse              | 1.33 ms                                                                      | 1.38 ms: 1.04x slower                                                                  |
| nqueens                    | 87.1 ms                                                                      | 90.6 ms: 1.04x slower                                                                  |
| xml_etree_parse            | 134 ms                                                                       | 140 ms: 1.04x slower                                                                   |
| deepcopy                   | 281 us                                                                       | 293 us: 1.04x slower                                                                   |
| genshi_xml                 | 52.2 ms                                                                      | 54.6 ms: 1.05x slower                                                                  |
| logging_format             | 6.78 us                                                                      | 7.15 us: 1.05x slower                                                                  |
| logging_simple             | 6.19 us                                                                      | 6.54 us: 1.06x slower                                                                  |
| generators                 | 28.0 ms                                                                      | 29.8 ms: 1.06x slower                                                                  |
| Geometric mean             | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (19): bench_mp_pool, scimark_sor, bench_thread_pool, deltablue, async_tree_memoization_tg, thrift, sqlalchemy_declarative, pylint, pathlib, xml_etree_generate, async_tree_io, html5lib, json, k_core, sphinx, dulwich_log, float, sqlite_synth, async_tree_io_tg

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 87.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x