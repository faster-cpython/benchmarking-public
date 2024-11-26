# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.001x slower
- HPT reliability: 97.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 317 ms                                                                       | 314 ms: 1.01x faster                                                  |
| docutils       | 3.21 sec                                                                     | 3.18 sec: 1.01x faster                                                |
| html5lib       | 72.2 ms                                                                      | 70.4 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                          |

Benchmark hidden because not significant (2): sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 846 ms                                                                       | 835 ms: 1.01x faster                                                  |
| async_tree_memoization_tg  | 378 ms                                                                       | 374 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg | 568 ms                                                                       | 562 ms: 1.01x faster                                                  |
| async_tree_io_tg           | 874 ms                                                                       | 871 ms: 1.00x faster                                                  |
| async_generators           | 382 ms                                                                       | 387 ms: 1.01x slower                                                  |
| coroutines                 | 21.1 ms                                                                      | 22.3 ms: 1.06x slower                                                 |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                          |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                                      | 79.6 ms: 1.01x slower                                                 |
| nbody          | 85.2 ms                                                                      | 87.0 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 147 ms                                                                       | 147 ms: 1.00x slower                                                  |
| regex_v8       | 25.6 ms                                                                      | 25.9 ms: 1.01x slower                                                 |
| regex_effbot   | 3.56 ms                                                                      | 3.73 ms: 1.05x slower                                                 |
| regex_dna      | 244 ms                                                                       | 257 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 59.0 ms                                                                      | 58.1 ms: 1.02x faster                                                 |
| pickle_pure_python   | 337 us                                                                       | 332 us: 1.02x faster                                                  |
| xml_etree_generate   | 82.3 ms                                                                      | 81.1 ms: 1.02x faster                                                 |
| json_loads           | 24.8 us                                                                      | 25.0 us: 1.01x slower                                                 |
| json_dumps           | 11.0 ms                                                                      | 11.1 ms: 1.01x slower                                                 |
| xml_etree_iterparse  | 99.6 ms                                                                      | 100 ms: 1.01x slower                                                  |
| tomli_loads          | 2.09 sec                                                                     | 2.11 sec: 1.01x slower                                                |
| unpickle_pure_python | 217 us                                                                       | 220 us: 1.01x slower                                                  |
| xml_etree_parse      | 141 ms                                                                       | 146 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.99 ms                                                                      | 9.03 ms: 1.01x slower                                                 |
| python_startup         | 14.8 ms                                                                      | 14.9 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                        | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 44.8 ms                                                                      | 43.1 ms: 1.04x faster                                                 |
| genshi_xml      | 63.2 ms                                                                      | 61.9 ms: 1.02x faster                                                 |
| mako            | 9.48 ms                                                                      | 9.62 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 4.42 ms                                                                      | 4.21 ms: 1.05x faster                                                 |
| coverage                   | 81.3 ms                                                                      | 77.8 ms: 1.05x faster                                                 |
| logging_format             | 7.53 us                                                                      | 7.23 us: 1.04x faster                                                 |
| django_template            | 44.8 ms                                                                      | 43.1 ms: 1.04x faster                                                 |
| richards                   | 46.4 ms                                                                      | 45.1 ms: 1.03x faster                                                 |
| html5lib                   | 72.2 ms                                                                      | 70.4 ms: 1.02x faster                                                 |
| genshi_xml                 | 63.2 ms                                                                      | 61.9 ms: 1.02x faster                                                 |
| sqlglot_optimize           | 70.2 ms                                                                      | 68.8 ms: 1.02x faster                                                 |
| sqlglot_transpile          | 1.99 ms                                                                      | 1.96 ms: 1.02x faster                                                 |
| sqlglot_parse              | 1.52 ms                                                                      | 1.50 ms: 1.02x faster                                                 |
| xml_etree_process          | 59.0 ms                                                                      | 58.1 ms: 1.02x faster                                                 |
| pickle_pure_python         | 337 us                                                                       | 332 us: 1.02x faster                                                  |
| sqlglot_normalize          | 135 ms                                                                       | 133 ms: 1.02x faster                                                  |
| xml_etree_generate         | 82.3 ms                                                                      | 81.1 ms: 1.02x faster                                                 |
| richards_super             | 55.4 ms                                                                      | 54.7 ms: 1.01x faster                                                 |
| logging_simple             | 6.84 us                                                                      | 6.75 us: 1.01x faster                                                 |
| async_tree_io              | 846 ms                                                                       | 835 ms: 1.01x faster                                                  |
| sympy_str                  | 321 ms                                                                       | 317 ms: 1.01x faster                                                  |
| async_tree_memoization_tg  | 378 ms                                                                       | 374 ms: 1.01x faster                                                  |
| sympy_expand               | 533 ms                                                                       | 527 ms: 1.01x faster                                                  |
| scimark_lu                 | 96.5 ms                                                                      | 95.4 ms: 1.01x faster                                                 |
| scimark_fft                | 288 ms                                                                       | 285 ms: 1.01x faster                                                  |
| pathlib                    | 16.0 ms                                                                      | 15.8 ms: 1.01x faster                                                 |
| docutils                   | 3.21 sec                                                                     | 3.18 sec: 1.01x faster                                                |
| pycparser                  | 1.29 sec                                                                     | 1.27 sec: 1.01x faster                                                |
| sympy_sum                  | 175 ms                                                                       | 173 ms: 1.01x faster                                                  |
| 2to3                       | 317 ms                                                                       | 314 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg | 568 ms                                                                       | 562 ms: 1.01x faster                                                  |
| nqueens                    | 102 ms                                                                       | 102 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 69.3 ms                                                                      | 68.8 ms: 1.01x faster                                                 |
| sympy_integrate            | 27.3 ms                                                                      | 27.2 ms: 1.01x faster                                                 |
| async_tree_io_tg           | 874 ms                                                                       | 871 ms: 1.00x faster                                                  |
| scimark_sor                | 105 ms                                                                       | 105 ms: 1.00x faster                                                  |
| mdp                        | 2.58 sec                                                                     | 2.57 sec: 1.00x faster                                                |
| bpe_tokeniser              | 4.77 sec                                                                     | 4.76 sec: 1.00x faster                                                |
| hexiom                     | 7.19 ms                                                                      | 7.21 ms: 1.00x slower                                                 |
| regex_compile              | 147 ms                                                                       | 147 ms: 1.00x slower                                                  |
| python_startup_no_site     | 8.99 ms                                                                      | 9.03 ms: 1.01x slower                                                 |
| float                      | 79.2 ms                                                                      | 79.6 ms: 1.01x slower                                                 |
| json_loads                 | 24.8 us                                                                      | 25.0 us: 1.01x slower                                                 |
| dulwich_log                | 63.1 ms                                                                      | 63.5 ms: 1.01x slower                                                 |
| json_dumps                 | 11.0 ms                                                                      | 11.1 ms: 1.01x slower                                                 |
| python_startup             | 14.8 ms                                                                      | 14.9 ms: 1.01x slower                                                 |
| chaos                      | 68.1 ms                                                                      | 68.7 ms: 1.01x slower                                                 |
| deepcopy_memo              | 30.0 us                                                                      | 30.3 us: 1.01x slower                                                 |
| xml_etree_iterparse        | 99.6 ms                                                                      | 100 ms: 1.01x slower                                                  |
| tomli_loads                | 2.09 sec                                                                     | 2.11 sec: 1.01x slower                                                |
| comprehensions             | 18.7 us                                                                      | 18.8 us: 1.01x slower                                                 |
| unpickle_pure_python       | 217 us                                                                       | 220 us: 1.01x slower                                                  |
| regex_v8                   | 25.6 ms                                                                      | 25.9 ms: 1.01x slower                                                 |
| async_generators           | 382 ms                                                                       | 387 ms: 1.01x slower                                                  |
| json                       | 5.15 ms                                                                      | 5.22 ms: 1.01x slower                                                 |
| pprint_pformat             | 1.62 sec                                                                     | 1.65 sec: 1.01x slower                                                |
| mako                       | 9.48 ms                                                                      | 9.62 ms: 1.02x slower                                                 |
| meteor_contest             | 130 ms                                                                       | 132 ms: 1.02x slower                                                  |
| raytrace                   | 310 ms                                                                       | 316 ms: 1.02x slower                                                  |
| nbody                      | 85.2 ms                                                                      | 87.0 ms: 1.02x slower                                                 |
| deepcopy                   | 307 us                                                                       | 314 us: 1.02x slower                                                  |
| pyflate                    | 456 ms                                                                       | 466 ms: 1.02x slower                                                  |
| spectral_norm              | 92.5 ms                                                                      | 94.8 ms: 1.03x slower                                                 |
| xml_etree_parse            | 141 ms                                                                       | 146 ms: 1.03x slower                                                  |
| regex_effbot               | 3.56 ms                                                                      | 3.73 ms: 1.05x slower                                                 |
| regex_dna                  | 244 ms                                                                       | 257 ms: 1.05x slower                                                  |
| coroutines                 | 21.1 ms                                                                      | 22.3 ms: 1.06x slower                                                 |
| gc_traversal               | 5.21 ms                                                                      | 5.81 ms: 1.11x slower                                                 |
| bench_mp_pool              | 1.74 sec                                                                     | 3.17 sec: 1.82x slower                                                |
| Geometric mean             | (ref)                                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (23): pylint, async_tree_memoization, deepcopy_reduce, async_tree_none, async_tree_none_tg, sphinx, async_tree_cpu_io_mixed, bench_thread_pool, thrift, fannkuch, pidigits, typing_runtime_protocols, generators, tornado_http, pprint_safe_repr, asyncio_websockets, deltablue, go, telco, logging_silent, create_gc_cycles, crypto_pyaes, genshi_text

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 97.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x