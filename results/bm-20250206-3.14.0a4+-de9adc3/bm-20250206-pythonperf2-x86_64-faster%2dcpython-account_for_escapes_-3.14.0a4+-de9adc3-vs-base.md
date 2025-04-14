# Results vs. base

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: de9adc3
- commit date: 2025-02-06
- overall geometric mean: 1.008x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 286 ms: 1.02x slower                                                                   |
| docutils       | 2.85 sec                                                                     | 2.87 sec: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| asyncio_websockets     | 389 ms                                                                       | 385 ms: 1.01x faster                                                                   |
| async_generators       | 403 ms                                                                       | 405 ms: 1.00x slower                                                                   |
| async_tree_memoization | 351 ms                                                                       | 353 ms: 1.01x slower                                                                   |
| async_tree_none        | 287 ms                                                                       | 290 ms: 1.01x slower                                                                   |
| async_tree_io          | 652 ms                                                                       | 658 ms: 1.01x slower                                                                   |
| coroutines             | 20.8 ms                                                                      | 21.1 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 95.8 ms                                                                      | 90.8 ms: 1.06x faster                                                                  |
| float          | 68.8 ms                                                                      | 70.3 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 251 ms                                                                       | 231 ms: 1.09x faster                                                                   |
| regex_v8       | 26.1 ms                                                                      | 25.2 ms: 1.03x faster                                                                  |
| regex_effbot   | 3.19 ms                                                                      | 3.11 ms: 1.02x faster                                                                  |
| regex_compile  | 134 ms                                                                       | 135 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.04x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                       | 211 us: 1.01x faster                                                                   |
| pickle_pure_python   | 328 us                                                                       | 329 us: 1.00x slower                                                                   |
| json_dumps           | 11.6 ms                                                                      | 11.8 ms: 1.02x slower                                                                  |
| xml_etree_parse      | 136 ms                                                                       | 139 ms: 1.02x slower                                                                   |
| tomli_loads          | 2.04 sec                                                                     | 2.09 sec: 1.02x slower                                                                 |
| xml_etree_iterparse  | 96.2 ms                                                                      | 98.7 ms: 1.03x slower                                                                  |
| Geometric mean       | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 9.01 ms: 1.00x faster                                                                  |
| python_startup         | 16.0 ms                                                                      | 16.2 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 34.5 ms                                                                      | 35.9 ms: 1.04x slower                                                                  |
| genshi_text     | 23.1 ms                                                                      | 24.7 ms: 1.07x slower                                                                  |
| genshi_xml      | 53.6 ms                                                                      | 57.9 ms: 1.08x slower                                                                  |
| Geometric mean  | (ref)                                                                        | 1.05x slower                                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|-------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna               | 251 ms                                                                       | 231 ms: 1.09x faster                                                                   |
| nbody                   | 95.8 ms                                                                      | 90.8 ms: 1.06x faster                                                                  |
| regex_v8                | 26.1 ms                                                                      | 25.2 ms: 1.03x faster                                                                  |
| coverage                | 79.7 ms                                                                      | 77.5 ms: 1.03x faster                                                                  |
| regex_effbot            | 3.19 ms                                                                      | 3.11 ms: 1.02x faster                                                                  |
| gc_traversal            | 6.53 ms                                                                      | 6.38 ms: 1.02x faster                                                                  |
| chaos                   | 61.2 ms                                                                      | 60.0 ms: 1.02x faster                                                                  |
| logging_format          | 6.97 us                                                                      | 6.87 us: 1.01x faster                                                                  |
| logging_simple          | 6.29 us                                                                      | 6.20 us: 1.01x faster                                                                  |
| spectral_norm           | 84.2 ms                                                                      | 83.1 ms: 1.01x faster                                                                  |
| raytrace                | 280 ms                                                                       | 277 ms: 1.01x faster                                                                   |
| asyncio_websockets      | 389 ms                                                                       | 385 ms: 1.01x faster                                                                   |
| unpickle_pure_python    | 213 us                                                                       | 211 us: 1.01x faster                                                                   |
| meteor_contest          | 125 ms                                                                       | 124 ms: 1.01x faster                                                                   |
| logging_silent          | 97.8 ns                                                                      | 96.9 ns: 1.01x faster                                                                  |
| richards_super          | 53.2 ms                                                                      | 52.9 ms: 1.01x faster                                                                  |
| pyflate                 | 441 ms                                                                       | 439 ms: 1.01x faster                                                                   |
| connected_components    | 417 ms                                                                       | 415 ms: 1.00x faster                                                                   |
| shortest_path           | 446 ms                                                                       | 445 ms: 1.00x faster                                                                   |
| python_startup_no_site  | 9.02 ms                                                                      | 9.01 ms: 1.00x faster                                                                  |
| pickle_pure_python      | 328 us                                                                       | 329 us: 1.00x slower                                                                   |
| async_generators        | 403 ms                                                                       | 405 ms: 1.00x slower                                                                   |
| generators              | 29.0 ms                                                                      | 29.2 ms: 1.01x slower                                                                  |
| docutils                | 2.85 sec                                                                     | 2.87 sec: 1.01x slower                                                                 |
| async_tree_memoization  | 351 ms                                                                       | 353 ms: 1.01x slower                                                                   |
| many_optionals          | 995 us                                                                       | 1.00 ms: 1.01x slower                                                                  |
| regex_compile           | 134 ms                                                                       | 135 ms: 1.01x slower                                                                   |
| comprehensions          | 17.1 us                                                                      | 17.2 us: 1.01x slower                                                                  |
| richards                | 46.6 ms                                                                      | 47.0 ms: 1.01x slower                                                                  |
| subparsers              | 22.8 ms                                                                      | 22.9 ms: 1.01x slower                                                                  |
| python_startup          | 16.0 ms                                                                      | 16.2 ms: 1.01x slower                                                                  |
| async_tree_none         | 287 ms                                                                       | 290 ms: 1.01x slower                                                                   |
| deepcopy_reduce         | 2.92 us                                                                      | 2.95 us: 1.01x slower                                                                  |
| async_tree_io           | 652 ms                                                                       | 658 ms: 1.01x slower                                                                   |
| sqlalchemy_imperative   | 17.5 ms                                                                      | 17.8 ms: 1.01x slower                                                                  |
| sympy_sum               | 150 ms                                                                       | 152 ms: 1.01x slower                                                                   |
| bpe_tokeniser           | 4.53 sec                                                                     | 4.59 sec: 1.01x slower                                                                 |
| crypto_pyaes            | 74.3 ms                                                                      | 75.4 ms: 1.01x slower                                                                  |
| coroutines              | 20.8 ms                                                                      | 21.1 ms: 1.01x slower                                                                  |
| sympy_str               | 287 ms                                                                       | 291 ms: 1.01x slower                                                                   |
| sqlalchemy_declarative  | 141 ms                                                                       | 143 ms: 1.01x slower                                                                   |
| mdp                     | 2.42 sec                                                                     | 2.46 sec: 1.01x slower                                                                 |
| pathlib                 | 15.5 ms                                                                      | 15.8 ms: 1.02x slower                                                                  |
| hexiom                  | 6.06 ms                                                                      | 6.16 ms: 1.02x slower                                                                  |
| json_dumps              | 11.6 ms                                                                      | 11.8 ms: 1.02x slower                                                                  |
| 2to3                    | 281 ms                                                                       | 286 ms: 1.02x slower                                                                   |
| pycparser               | 1.24 sec                                                                     | 1.26 sec: 1.02x slower                                                                 |
| sympy_expand            | 488 ms                                                                       | 497 ms: 1.02x slower                                                                   |
| dulwich_log             | 65.7 ms                                                                      | 67.0 ms: 1.02x slower                                                                  |
| sqlglot_normalize       | 114 ms                                                                       | 116 ms: 1.02x slower                                                                   |
| sqlglot_parse           | 1.32 ms                                                                      | 1.35 ms: 1.02x slower                                                                  |
| nqueens                 | 87.0 ms                                                                      | 88.9 ms: 1.02x slower                                                                  |
| thrift                  | 851 us                                                                       | 870 us: 1.02x slower                                                                   |
| float                   | 68.8 ms                                                                      | 70.3 ms: 1.02x slower                                                                  |
| sqlglot_optimize        | 56.2 ms                                                                      | 57.5 ms: 1.02x slower                                                                  |
| fannkuch                | 358 ms                                                                       | 366 ms: 1.02x slower                                                                   |
| xml_etree_parse         | 136 ms                                                                       | 139 ms: 1.02x slower                                                                   |
| pprint_safe_repr        | 774 ms                                                                       | 792 ms: 1.02x slower                                                                   |
| sqlglot_transpile       | 1.70 ms                                                                      | 1.74 ms: 1.02x slower                                                                  |
| tomli_loads             | 2.04 sec                                                                     | 2.09 sec: 1.02x slower                                                                 |
| xml_etree_iterparse     | 96.2 ms                                                                      | 98.7 ms: 1.03x slower                                                                  |
| pprint_pformat          | 1.59 sec                                                                     | 1.64 sec: 1.03x slower                                                                 |
| deepcopy                | 278 us                                                                       | 288 us: 1.04x slower                                                                   |
| django_template         | 34.5 ms                                                                      | 35.9 ms: 1.04x slower                                                                  |
| bench_thread_pool       | 919 us                                                                       | 957 us: 1.04x slower                                                                   |
| scimark_sor             | 106 ms                                                                       | 111 ms: 1.04x slower                                                                   |
| scimark_monte_carlo     | 62.4 ms                                                                      | 65.4 ms: 1.05x slower                                                                  |
| deepcopy_memo           | 29.1 us                                                                      | 30.5 us: 1.05x slower                                                                  |
| scimark_fft             | 295 ms                                                                       | 313 ms: 1.06x slower                                                                   |
| genshi_text             | 23.1 ms                                                                      | 24.7 ms: 1.07x slower                                                                  |
| genshi_xml              | 53.6 ms                                                                      | 57.9 ms: 1.08x slower                                                                  |
| scimark_sparse_mat_mult | 4.35 ms                                                                      | 4.76 ms: 1.09x slower                                                                  |
| Geometric mean          | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (24): html5lib, scimark_lu, deltablue, json, xml_etree_process, xml_etree_generate, json_loads, sqlite_synth, async_tree_cpu_io_mixed_tg, sympy_integrate, async_tree_none_tg, k_core, mako, create_gc_cycles, pidigits, go, sphinx, typing_runtime_protocols, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, telco, pylint, bench_mp_pool

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x