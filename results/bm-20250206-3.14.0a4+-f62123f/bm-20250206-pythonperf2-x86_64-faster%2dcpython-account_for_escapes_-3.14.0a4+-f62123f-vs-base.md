# Results vs. base

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: f62123f
- commit date: 2025-02-06
- overall geometric mean: 1.004x slower
- HPT reliability: 99.41%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 284 ms: 1.01x slower                                                                   |
| docutils       | 2.85 sec                                                                     | 2.87 sec: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| asyncio_websockets     | 389 ms                                                                       | 385 ms: 1.01x faster                                                                   |
| async_tree_memoization | 351 ms                                                                       | 354 ms: 1.01x slower                                                                   |
| async_generators       | 403 ms                                                                       | 408 ms: 1.01x slower                                                                   |
| async_tree_io          | 652 ms                                                                       | 661 ms: 1.01x slower                                                                   |
| coroutines             | 20.8 ms                                                                      | 21.1 ms: 1.02x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 95.8 ms                                                                      | 91.4 ms: 1.05x faster                                                                  |
| float          | 68.8 ms                                                                      | 71.6 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 251 ms                                                                       | 244 ms: 1.03x faster                                                                   |
| regex_effbot   | 3.19 ms                                                                      | 3.17 ms: 1.00x faster                                                                  |
| regex_compile  | 134 ms                                                                       | 135 ms: 1.01x slower                                                                   |
| regex_v8       | 26.1 ms                                                                      | 26.6 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                       | 209 us: 1.02x faster                                                                   |
| xml_etree_parse      | 136 ms                                                                       | 134 ms: 1.01x faster                                                                   |
| xml_etree_process    | 60.3 ms                                                                      | 59.7 ms: 1.01x faster                                                                  |
| json_loads           | 26.6 us                                                                      | 26.4 us: 1.01x faster                                                                  |
| pickle_pure_python   | 328 us                                                                       | 329 us: 1.00x slower                                                                   |
| json_dumps           | 11.6 ms                                                                      | 11.8 ms: 1.02x slower                                                                  |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (3): xml_etree_generate, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 9.03 ms: 1.00x slower                                                                  |
| python_startup         | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 34.5 ms                                                                      | 34.8 ms: 1.01x slower                                                                  |
| genshi_xml      | 53.6 ms                                                                      | 55.7 ms: 1.04x slower                                                                  |
| genshi_text     | 23.1 ms                                                                      | 24.4 ms: 1.06x slower                                                                  |
| Geometric mean  | (ref)                                                                        | 1.03x slower                                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250205-pythonperf2-x86_64-python-58a4357e29a15135e6fd-3.14.0a4+-58a4357 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|--------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody                    | 95.8 ms                                                                      | 91.4 ms: 1.05x faster                                                                  |
| regex_dna                | 251 ms                                                                       | 244 ms: 1.03x faster                                                                   |
| logging_format           | 6.97 us                                                                      | 6.79 us: 1.03x faster                                                                  |
| scimark_monte_carlo      | 62.4 ms                                                                      | 60.8 ms: 1.03x faster                                                                  |
| coverage                 | 79.7 ms                                                                      | 77.8 ms: 1.02x faster                                                                  |
| logging_simple           | 6.29 us                                                                      | 6.15 us: 1.02x faster                                                                  |
| unpickle_pure_python     | 213 us                                                                       | 209 us: 1.02x faster                                                                   |
| raytrace                 | 280 ms                                                                       | 275 ms: 1.02x faster                                                                   |
| richards_super           | 53.2 ms                                                                      | 52.4 ms: 1.02x faster                                                                  |
| typing_runtime_protocols | 169 us                                                                       | 167 us: 1.01x faster                                                                   |
| generators               | 29.0 ms                                                                      | 28.7 ms: 1.01x faster                                                                  |
| xml_etree_parse          | 136 ms                                                                       | 134 ms: 1.01x faster                                                                   |
| richards                 | 46.6 ms                                                                      | 46.2 ms: 1.01x faster                                                                  |
| xml_etree_process        | 60.3 ms                                                                      | 59.7 ms: 1.01x faster                                                                  |
| meteor_contest           | 125 ms                                                                       | 124 ms: 1.01x faster                                                                   |
| asyncio_websockets       | 389 ms                                                                       | 385 ms: 1.01x faster                                                                   |
| logging_silent           | 97.8 ns                                                                      | 96.9 ns: 1.01x faster                                                                  |
| crypto_pyaes             | 74.3 ms                                                                      | 73.6 ms: 1.01x faster                                                                  |
| spectral_norm            | 84.2 ms                                                                      | 83.5 ms: 1.01x faster                                                                  |
| telco                    | 8.07 ms                                                                      | 8.01 ms: 1.01x faster                                                                  |
| go                       | 127 ms                                                                       | 126 ms: 1.01x faster                                                                   |
| chaos                    | 61.2 ms                                                                      | 60.8 ms: 1.01x faster                                                                  |
| json_loads               | 26.6 us                                                                      | 26.4 us: 1.01x faster                                                                  |
| pyflate                  | 441 ms                                                                       | 439 ms: 1.00x faster                                                                   |
| regex_effbot             | 3.19 ms                                                                      | 3.17 ms: 1.00x faster                                                                  |
| shortest_path            | 446 ms                                                                       | 445 ms: 1.00x faster                                                                   |
| python_startup_no_site   | 9.02 ms                                                                      | 9.03 ms: 1.00x slower                                                                  |
| python_startup           | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                                  |
| sympy_integrate          | 23.1 ms                                                                      | 23.2 ms: 1.00x slower                                                                  |
| pickle_pure_python       | 328 us                                                                       | 329 us: 1.00x slower                                                                   |
| docutils                 | 2.85 sec                                                                     | 2.87 sec: 1.01x slower                                                                 |
| subparsers               | 22.8 ms                                                                      | 22.9 ms: 1.01x slower                                                                  |
| comprehensions           | 17.1 us                                                                      | 17.2 us: 1.01x slower                                                                  |
| sympy_expand             | 488 ms                                                                       | 492 ms: 1.01x slower                                                                   |
| regex_compile            | 134 ms                                                                       | 135 ms: 1.01x slower                                                                   |
| sqlalchemy_imperative    | 17.5 ms                                                                      | 17.7 ms: 1.01x slower                                                                  |
| scimark_lu               | 94.3 ms                                                                      | 95.1 ms: 1.01x slower                                                                  |
| 2to3                     | 281 ms                                                                       | 284 ms: 1.01x slower                                                                   |
| async_tree_memoization   | 351 ms                                                                       | 354 ms: 1.01x slower                                                                   |
| django_template          | 34.5 ms                                                                      | 34.8 ms: 1.01x slower                                                                  |
| many_optionals           | 995 us                                                                       | 1.00 ms: 1.01x slower                                                                  |
| sympy_str                | 287 ms                                                                       | 290 ms: 1.01x slower                                                                   |
| async_generators         | 403 ms                                                                       | 408 ms: 1.01x slower                                                                   |
| dulwich_log              | 65.7 ms                                                                      | 66.5 ms: 1.01x slower                                                                  |
| sqlalchemy_declarative   | 141 ms                                                                       | 143 ms: 1.01x slower                                                                   |
| deepcopy_reduce          | 2.92 us                                                                      | 2.96 us: 1.01x slower                                                                  |
| bench_thread_pool        | 919 us                                                                       | 931 us: 1.01x slower                                                                   |
| async_tree_io            | 652 ms                                                                       | 661 ms: 1.01x slower                                                                   |
| pprint_pformat           | 1.59 sec                                                                     | 1.61 sec: 1.01x slower                                                                 |
| coroutines               | 20.8 ms                                                                      | 21.1 ms: 1.02x slower                                                                  |
| sympy_sum                | 150 ms                                                                       | 152 ms: 1.02x slower                                                                   |
| thrift                   | 851 us                                                                       | 865 us: 1.02x slower                                                                   |
| scimark_sor              | 106 ms                                                                       | 108 ms: 1.02x slower                                                                   |
| pprint_safe_repr         | 774 ms                                                                       | 787 ms: 1.02x slower                                                                   |
| deepcopy                 | 278 us                                                                       | 283 us: 1.02x slower                                                                   |
| regex_v8                 | 26.1 ms                                                                      | 26.6 ms: 1.02x slower                                                                  |
| sqlglot_normalize        | 114 ms                                                                       | 116 ms: 1.02x slower                                                                   |
| bpe_tokeniser            | 4.53 sec                                                                     | 4.64 sec: 1.02x slower                                                                 |
| json_dumps               | 11.6 ms                                                                      | 11.8 ms: 1.02x slower                                                                  |
| sqlglot_parse            | 1.32 ms                                                                      | 1.36 ms: 1.02x slower                                                                  |
| sqlglot_transpile        | 1.70 ms                                                                      | 1.74 ms: 1.03x slower                                                                  |
| sqlglot_optimize         | 56.2 ms                                                                      | 57.7 ms: 1.03x slower                                                                  |
| scimark_fft              | 295 ms                                                                       | 303 ms: 1.03x slower                                                                   |
| nqueens                  | 87.0 ms                                                                      | 89.8 ms: 1.03x slower                                                                  |
| scimark_sparse_mat_mult  | 4.35 ms                                                                      | 4.49 ms: 1.03x slower                                                                  |
| deepcopy_memo            | 29.1 us                                                                      | 30.1 us: 1.04x slower                                                                  |
| genshi_xml               | 53.6 ms                                                                      | 55.7 ms: 1.04x slower                                                                  |
| mdp                      | 2.42 sec                                                                     | 2.52 sec: 1.04x slower                                                                 |
| float                    | 68.8 ms                                                                      | 71.6 ms: 1.04x slower                                                                  |
| genshi_text              | 23.1 ms                                                                      | 24.4 ms: 1.06x slower                                                                  |
| Geometric mean           | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (26): bench_mp_pool, pycparser, async_tree_none_tg, html5lib, pidigits, pathlib, xml_etree_generate, deltablue, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, connected_components, hexiom, k_core, tomli_loads, async_tree_io_tg, xml_etree_iterparse, fannkuch, async_tree_cpu_io_mixed, sqlite_synth, json, async_tree_none, sphinx, gc_traversal, mako, pylint, create_gc_cycles

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x