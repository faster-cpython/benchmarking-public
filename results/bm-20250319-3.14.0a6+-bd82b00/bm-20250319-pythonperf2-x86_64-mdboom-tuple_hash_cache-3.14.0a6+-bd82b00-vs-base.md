# Results vs. base

- fork: mdboom
- ref: tuple_hash_cache
- machine: linux-x86_64
- commit hash: bd82b00
- commit date: 2025-03-19
- overall geometric mean: 1.002x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                                       | 289 ms: 1.01x slower                                                     |
| html5lib       | 72.0 ms                                                                      | 69.9 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 525 ms                                                                       | 529 ms: 1.01x slower                                                     |
| async_tree_memoization     | 354 ms                                                                       | 357 ms: 1.01x slower                                                     |
| coroutines                 | 21.0 ms                                                                      | 21.3 ms: 1.01x slower                                                    |
| async_tree_none            | 293 ms                                                                       | 300 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 510 ms                                                                       | 523 ms: 1.03x slower                                                     |
| async_generators           | 420 ms                                                                       | 432 ms: 1.03x slower                                                     |
| async_tree_none_tg         | 276 ms                                                                       | 286 ms: 1.04x slower                                                     |
| async_tree_memoization_tg  | 342 ms                                                                       | 360 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (3): async_tree_io, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.16 ms                                                                      | 3.23 ms: 1.02x slower                                                    |
| regex_v8       | 23.2 ms                                                                      | 24.0 ms: 1.03x slower                                                    |
| regex_dna      | 230 ms                                                                       | 246 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 142 ms                                                                       | 137 ms: 1.03x faster                                                     |
| tomli_loads          | 2.19 sec                                                                     | 2.17 sec: 1.01x faster                                                   |
| unpickle_pure_python | 225 us                                                                       | 222 us: 1.01x faster                                                     |
| xml_etree_generate   | 84.1 ms                                                                      | 85.1 ms: 1.01x slower                                                    |
| xml_etree_process    | 59.8 ms                                                                      | 60.6 ms: 1.01x slower                                                    |
| xml_etree_iterparse  | 99.2 ms                                                                      | 100 ms: 1.01x slower                                                     |
| json_dumps           | 11.5 ms                                                                      | 11.7 ms: 1.02x slower                                                    |
| json_loads           | 26.1 us                                                                      | 26.6 us: 1.02x slower                                                    |
| pickle_pure_python   | 338 us                                                                       | 346 us: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                      | 16.5 ms: 1.00x slower                                                    |
| python_startup_no_site | 10.5 ms                                                                      | 10.5 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|-----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 37.5 ms                                                                      | 37.9 ms: 1.01x slower                                                    |
| mako            | 11.0 ms                                                                      | 11.2 ms: 1.02x slower                                                    |
| genshi_xml      | 56.1 ms                                                                      | 58.3 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.52 sec                                                                     | 1.36 sec: 1.85x faster                                                   |
| coverage                   | 82.3 ms                                                                      | 79.6 ms: 1.03x faster                                                    |
| xml_etree_parse            | 142 ms                                                                       | 137 ms: 1.03x faster                                                     |
| html5lib                   | 72.0 ms                                                                      | 69.9 ms: 1.03x faster                                                    |
| comprehensions             | 18.2 us                                                                      | 17.8 us: 1.02x faster                                                    |
| raytrace                   | 305 ms                                                                       | 298 ms: 1.02x faster                                                     |
| crypto_pyaes               | 84.2 ms                                                                      | 82.4 ms: 1.02x faster                                                    |
| tomli_loads                | 2.19 sec                                                                     | 2.17 sec: 1.01x faster                                                   |
| unpickle_pure_python       | 225 us                                                                       | 222 us: 1.01x faster                                                     |
| richards                   | 48.1 ms                                                                      | 47.7 ms: 1.01x faster                                                    |
| richards_super             | 54.0 ms                                                                      | 53.6 ms: 1.01x faster                                                    |
| pathlib                    | 17.2 ms                                                                      | 17.1 ms: 1.01x faster                                                    |
| dulwich_log                | 63.4 ms                                                                      | 63.0 ms: 1.01x faster                                                    |
| generators                 | 29.2 ms                                                                      | 29.0 ms: 1.01x faster                                                    |
| deepcopy_memo              | 29.5 us                                                                      | 29.4 us: 1.00x faster                                                    |
| connected_components       | 431 ms                                                                       | 430 ms: 1.00x faster                                                     |
| nqueens                    | 96.3 ms                                                                      | 96.1 ms: 1.00x faster                                                    |
| shortest_path              | 457 ms                                                                       | 459 ms: 1.00x slower                                                     |
| python_startup             | 16.4 ms                                                                      | 16.5 ms: 1.00x slower                                                    |
| python_startup_no_site     | 10.5 ms                                                                      | 10.5 ms: 1.00x slower                                                    |
| sqlglot_v2_parse           | 1.40 ms                                                                      | 1.41 ms: 1.00x slower                                                    |
| many_optionals             | 1.05 ms                                                                      | 1.05 ms: 1.01x slower                                                    |
| sympy_expand               | 509 ms                                                                       | 512 ms: 1.01x slower                                                     |
| meteor_contest             | 128 ms                                                                       | 129 ms: 1.01x slower                                                     |
| logging_format             | 7.30 us                                                                      | 7.34 us: 1.01x slower                                                    |
| logging_silent             | 94.9 ns                                                                      | 95.4 ns: 1.01x slower                                                    |
| 2to3                       | 287 ms                                                                       | 289 ms: 1.01x slower                                                     |
| sympy_sum                  | 156 ms                                                                       | 157 ms: 1.01x slower                                                     |
| hexiom                     | 6.44 ms                                                                      | 6.48 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed    | 525 ms                                                                       | 529 ms: 1.01x slower                                                     |
| async_tree_memoization     | 354 ms                                                                       | 357 ms: 1.01x slower                                                     |
| logging_simple             | 6.71 us                                                                      | 6.76 us: 1.01x slower                                                    |
| sqlalchemy_imperative      | 18.3 ms                                                                      | 18.5 ms: 1.01x slower                                                    |
| sympy_str                  | 298 ms                                                                       | 301 ms: 1.01x slower                                                     |
| django_template            | 37.5 ms                                                                      | 37.9 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 826 ms                                                                       | 836 ms: 1.01x slower                                                     |
| xml_etree_generate         | 84.1 ms                                                                      | 85.1 ms: 1.01x slower                                                    |
| xml_etree_process          | 59.8 ms                                                                      | 60.6 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 99.2 ms                                                                      | 100 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.67 sec                                                                     | 1.69 sec: 1.01x slower                                                   |
| coroutines                 | 21.0 ms                                                                      | 21.3 ms: 1.01x slower                                                    |
| scimark_fft                | 320 ms                                                                       | 325 ms: 1.02x slower                                                     |
| sqlglot_v2_optimize        | 59.3 ms                                                                      | 60.3 ms: 1.02x slower                                                    |
| json_dumps                 | 11.5 ms                                                                      | 11.7 ms: 1.02x slower                                                    |
| sqlglot_v2_normalize       | 120 ms                                                                       | 122 ms: 1.02x slower                                                     |
| sqlalchemy_declarative     | 147 ms                                                                       | 149 ms: 1.02x slower                                                     |
| json_loads                 | 26.1 us                                                                      | 26.6 us: 1.02x slower                                                    |
| scimark_sparse_mat_mult    | 4.74 ms                                                                      | 4.84 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 173 us                                                                       | 177 us: 1.02x slower                                                     |
| async_tree_none            | 293 ms                                                                       | 300 ms: 1.02x slower                                                     |
| pickle_pure_python         | 338 us                                                                       | 346 us: 1.02x slower                                                     |
| subparsers                 | 23.7 ms                                                                      | 24.3 ms: 1.02x slower                                                    |
| regex_effbot               | 3.16 ms                                                                      | 3.23 ms: 1.02x slower                                                    |
| mako                       | 11.0 ms                                                                      | 11.2 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 510 ms                                                                       | 523 ms: 1.03x slower                                                     |
| scimark_sor                | 109 ms                                                                       | 111 ms: 1.03x slower                                                     |
| thrift                     | 872 us                                                                       | 897 us: 1.03x slower                                                     |
| async_generators           | 420 ms                                                                       | 432 ms: 1.03x slower                                                     |
| json                       | 5.43 ms                                                                      | 5.59 ms: 1.03x slower                                                    |
| deepcopy                   | 288 us                                                                       | 297 us: 1.03x slower                                                     |
| scimark_monte_carlo        | 66.7 ms                                                                      | 68.9 ms: 1.03x slower                                                    |
| regex_v8                   | 23.2 ms                                                                      | 24.0 ms: 1.03x slower                                                    |
| async_tree_none_tg         | 276 ms                                                                       | 286 ms: 1.04x slower                                                     |
| genshi_xml                 | 56.1 ms                                                                      | 58.3 ms: 1.04x slower                                                    |
| gc_traversal               | 6.14 ms                                                                      | 6.39 ms: 1.04x slower                                                    |
| chaos                      | 64.3 ms                                                                      | 67.1 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 342 ms                                                                       | 360 ms: 1.05x slower                                                     |
| regex_dna                  | 230 ms                                                                       | 246 ms: 1.07x slower                                                     |
| bpe_tokeniser              | 4.85 sec                                                                     | 5.32 sec: 1.10x slower                                                   |
| bench_mp_pool              | 766 ms                                                                       | 1.58 sec: 2.06x slower                                                   |
| Geometric mean             | (ref)                                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (26): scimark_lu, fannkuch, pyflate, k_core, async_tree_io, docutils, sqlite_synth, deltablue, pidigits, bench_thread_pool, sympy_integrate, spectral_norm, regex_compile, asyncio_websockets, genshi_text, sqlglot_v2_transpile, deepcopy_reduce, float, go, async_tree_io_tg, telco, pycparser, nbody, pylint, sphinx, create_gc_cycles

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x