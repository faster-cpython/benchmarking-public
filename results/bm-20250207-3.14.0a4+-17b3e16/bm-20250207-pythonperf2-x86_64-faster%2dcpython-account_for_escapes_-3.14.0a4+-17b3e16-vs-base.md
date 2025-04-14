# Results vs. base

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 17b3e16
- commit date: 2025-02-07
- overall geometric mean: 1.005x slower
- HPT reliability: 93.41%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 285 ms: 1.01x slower                                                                   |
| docutils       | 2.85 sec                                                                     | 2.86 sec: 1.00x slower                                                                 |
| html5lib       | 67.9 ms                                                                      | 66.7 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| asyncio_websockets     | 389 ms                                                                       | 384 ms: 1.01x faster                                                                   |
| async_tree_io_tg       | 652 ms                                                                       | 645 ms: 1.01x faster                                                                   |
| async_generators       | 403 ms                                                                       | 402 ms: 1.00x faster                                                                   |
| async_tree_memoization | 351 ms                                                                       | 353 ms: 1.01x slower                                                                   |
| coroutines             | 20.8 ms                                                                      | 21.1 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 95.8 ms                                                                      | 91.6 ms: 1.05x faster                                                                  |
| float          | 68.8 ms                                                                      | 70.2 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 251 ms                                                                       | 250 ms: 1.01x faster                                                                   |
| regex_v8       | 26.1 ms                                                                      | 26.1 ms: 1.00x slower                                                                  |
| regex_compile  | 134 ms                                                                       | 136 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                       | 206 us: 1.04x faster                                                                   |
| xml_etree_process    | 60.3 ms                                                                      | 58.8 ms: 1.03x faster                                                                  |
| xml_etree_generate   | 84.0 ms                                                                      | 82.3 ms: 1.02x faster                                                                  |
| xml_etree_iterparse  | 96.2 ms                                                                      | 95.1 ms: 1.01x faster                                                                  |
| xml_etree_parse      | 136 ms                                                                       | 135 ms: 1.01x faster                                                                   |
| json_dumps           | 11.6 ms                                                                      | 11.6 ms: 1.00x slower                                                                  |
| pickle_pure_python   | 328 us                                                                       | 332 us: 1.01x slower                                                                   |
| tomli_loads          | 2.04 sec                                                                     | 2.08 sec: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 8.99 ms: 1.00x faster                                                                  |
| python_startup         | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                                      | 11.0 ms: 1.03x slower                                                                  |
| genshi_xml      | 53.6 ms                                                                      | 55.7 ms: 1.04x slower                                                                  |
| django_template | 34.5 ms                                                                      | 35.9 ms: 1.04x slower                                                                  |
| genshi_text     | 23.1 ms                                                                      | 24.4 ms: 1.06x slower                                                                  |
| Geometric mean  | (ref)                                                                        | 1.04x slower                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|-------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| gc_traversal            | 6.53 ms                                                                      | 6.12 ms: 1.07x faster                                                                  |
| nbody                   | 95.8 ms                                                                      | 91.6 ms: 1.05x faster                                                                  |
| unpickle_pure_python    | 213 us                                                                       | 206 us: 1.04x faster                                                                   |
| xml_etree_process       | 60.3 ms                                                                      | 58.8 ms: 1.03x faster                                                                  |
| xml_etree_generate      | 84.0 ms                                                                      | 82.3 ms: 1.02x faster                                                                  |
| spectral_norm           | 84.2 ms                                                                      | 82.5 ms: 1.02x faster                                                                  |
| html5lib                | 67.9 ms                                                                      | 66.7 ms: 1.02x faster                                                                  |
| coverage                | 79.7 ms                                                                      | 78.3 ms: 1.02x faster                                                                  |
| chaos                   | 61.2 ms                                                                      | 60.2 ms: 1.02x faster                                                                  |
| scimark_monte_carlo     | 62.4 ms                                                                      | 61.5 ms: 1.01x faster                                                                  |
| asyncio_websockets      | 389 ms                                                                       | 384 ms: 1.01x faster                                                                   |
| connected_components    | 417 ms                                                                       | 411 ms: 1.01x faster                                                                   |
| xml_etree_iterparse     | 96.2 ms                                                                      | 95.1 ms: 1.01x faster                                                                  |
| async_tree_io_tg        | 652 ms                                                                       | 645 ms: 1.01x faster                                                                   |
| meteor_contest          | 125 ms                                                                       | 124 ms: 1.01x faster                                                                   |
| raytrace                | 280 ms                                                                       | 277 ms: 1.01x faster                                                                   |
| logging_silent          | 97.8 ns                                                                      | 96.9 ns: 1.01x faster                                                                  |
| shortest_path           | 446 ms                                                                       | 442 ms: 1.01x faster                                                                   |
| regex_dna               | 251 ms                                                                       | 250 ms: 1.01x faster                                                                   |
| json                    | 5.50 ms                                                                      | 5.46 ms: 1.01x faster                                                                  |
| comprehensions          | 17.1 us                                                                      | 17.0 us: 1.01x faster                                                                  |
| pyflate                 | 441 ms                                                                       | 439 ms: 1.01x faster                                                                   |
| xml_etree_parse         | 136 ms                                                                       | 135 ms: 1.01x faster                                                                   |
| telco                   | 8.07 ms                                                                      | 8.04 ms: 1.00x faster                                                                  |
| python_startup_no_site  | 9.02 ms                                                                      | 8.99 ms: 1.00x faster                                                                  |
| async_generators        | 403 ms                                                                       | 402 ms: 1.00x faster                                                                   |
| python_startup          | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                                  |
| regex_v8                | 26.1 ms                                                                      | 26.1 ms: 1.00x slower                                                                  |
| docutils                | 2.85 sec                                                                     | 2.86 sec: 1.00x slower                                                                 |
| json_dumps              | 11.6 ms                                                                      | 11.6 ms: 1.00x slower                                                                  |
| many_optionals          | 995 us                                                                       | 1.00 ms: 1.01x slower                                                                  |
| async_tree_memoization  | 351 ms                                                                       | 353 ms: 1.01x slower                                                                   |
| pathlib                 | 15.5 ms                                                                      | 15.6 ms: 1.01x slower                                                                  |
| dulwich_log             | 65.7 ms                                                                      | 66.3 ms: 1.01x slower                                                                  |
| deltablue               | 3.34 ms                                                                      | 3.37 ms: 1.01x slower                                                                  |
| crypto_pyaes            | 74.3 ms                                                                      | 75.0 ms: 1.01x slower                                                                  |
| sympy_str               | 287 ms                                                                       | 290 ms: 1.01x slower                                                                   |
| go                      | 127 ms                                                                       | 129 ms: 1.01x slower                                                                   |
| deepcopy                | 278 us                                                                       | 282 us: 1.01x slower                                                                   |
| deepcopy_reduce         | 2.92 us                                                                      | 2.96 us: 1.01x slower                                                                  |
| 2to3                    | 281 ms                                                                       | 285 ms: 1.01x slower                                                                   |
| regex_compile           | 134 ms                                                                       | 136 ms: 1.01x slower                                                                   |
| sympy_sum               | 150 ms                                                                       | 152 ms: 1.01x slower                                                                   |
| sqlalchemy_imperative   | 17.5 ms                                                                      | 17.8 ms: 1.01x slower                                                                  |
| coroutines              | 20.8 ms                                                                      | 21.1 ms: 1.01x slower                                                                  |
| sympy_expand            | 488 ms                                                                       | 495 ms: 1.01x slower                                                                   |
| pickle_pure_python      | 328 us                                                                       | 332 us: 1.01x slower                                                                   |
| thrift                  | 851 us                                                                       | 863 us: 1.01x slower                                                                   |
| pycparser               | 1.24 sec                                                                     | 1.26 sec: 1.02x slower                                                                 |
| fannkuch                | 358 ms                                                                       | 364 ms: 1.02x slower                                                                   |
| tomli_loads             | 2.04 sec                                                                     | 2.08 sec: 1.02x slower                                                                 |
| hexiom                  | 6.06 ms                                                                      | 6.16 ms: 1.02x slower                                                                  |
| sqlalchemy_declarative  | 141 ms                                                                       | 144 ms: 1.02x slower                                                                   |
| sqlglot_normalize       | 114 ms                                                                       | 116 ms: 1.02x slower                                                                   |
| sqlglot_optimize        | 56.2 ms                                                                      | 57.4 ms: 1.02x slower                                                                  |
| scimark_sor             | 106 ms                                                                       | 109 ms: 1.02x slower                                                                   |
| float                   | 68.8 ms                                                                      | 70.2 ms: 1.02x slower                                                                  |
| deepcopy_memo           | 29.1 us                                                                      | 29.7 us: 1.02x slower                                                                  |
| mdp                     | 2.42 sec                                                                     | 2.48 sec: 1.02x slower                                                                 |
| sqlglot_parse           | 1.32 ms                                                                      | 1.36 ms: 1.02x slower                                                                  |
| logging_format          | 6.97 us                                                                      | 7.14 us: 1.02x slower                                                                  |
| sqlglot_transpile       | 1.70 ms                                                                      | 1.74 ms: 1.03x slower                                                                  |
| mako                    | 10.7 ms                                                                      | 11.0 ms: 1.03x slower                                                                  |
| scimark_fft             | 295 ms                                                                       | 303 ms: 1.03x slower                                                                   |
| nqueens                 | 87.0 ms                                                                      | 89.9 ms: 1.03x slower                                                                  |
| logging_simple          | 6.29 us                                                                      | 6.50 us: 1.03x slower                                                                  |
| genshi_xml              | 53.6 ms                                                                      | 55.7 ms: 1.04x slower                                                                  |
| django_template         | 34.5 ms                                                                      | 35.9 ms: 1.04x slower                                                                  |
| generators              | 29.0 ms                                                                      | 30.2 ms: 1.04x slower                                                                  |
| genshi_text             | 23.1 ms                                                                      | 24.4 ms: 1.06x slower                                                                  |
| scimark_sparse_mat_mult | 4.35 ms                                                                      | 4.73 ms: 1.09x slower                                                                  |
| Geometric mean          | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (25): bench_mp_pool, async_tree_none_tg, pprint_pformat, async_tree_cpu_io_mixed_tg, subparsers, typing_runtime_protocols, sympy_integrate, async_tree_memoization_tg, json_loads, bpe_tokeniser, richards, regex_effbot, k_core, scimark_lu, pidigits, create_gc_cycles, async_tree_cpu_io_mixed, pprint_safe_repr, async_tree_none, async_tree_io, richards_super, sphinx, sqlite_synth, pylint, bench_thread_pool

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 93.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x