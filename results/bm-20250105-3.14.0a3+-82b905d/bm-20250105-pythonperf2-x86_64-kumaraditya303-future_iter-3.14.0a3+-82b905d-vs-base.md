# Results vs. base

- fork: kumaraditya303
- ref: future_iter
- machine: linux-x86_64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.005x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 280 ms: 1.00x faster                                                        |
| docutils       | 2.90 sec                                                                     | 2.87 sec: 1.01x faster                                                      |
| html5lib       | 67.7 ms                                                                      | 66.8 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 629 ms                                                                       | 604 ms: 1.04x faster                                                        |
| async_tree_io              | 638 ms                                                                       | 618 ms: 1.03x faster                                                        |
| coroutines                 | 21.3 ms                                                                      | 20.6 ms: 1.03x faster                                                       |
| async_tree_none_tg         | 270 ms                                                                       | 262 ms: 1.03x faster                                                        |
| async_tree_memoization_tg  | 328 ms                                                                       | 320 ms: 1.03x faster                                                        |
| async_tree_none            | 288 ms                                                                       | 282 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 499 ms                                                                       | 489 ms: 1.02x faster                                                        |
| async_tree_memoization     | 352 ms                                                                       | 346 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 515 ms                                                                       | 512 ms: 1.01x faster                                                        |
| async_generators           | 433 ms                                                                       | 437 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 252 ms                                                                       | 245 ms: 1.03x faster                                                        |
| regex_effbot   | 3.34 ms                                                                      | 3.25 ms: 1.03x faster                                                       |
| regex_compile  | 135 ms                                                                       | 134 ms: 1.01x faster                                                        |
| regex_v8       | 26.8 ms                                                                      | 26.8 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 207 us                                                                       | 201 us: 1.03x faster                                                        |
| xml_etree_parse      | 137 ms                                                                       | 134 ms: 1.02x faster                                                        |
| json_dumps           | 11.6 ms                                                                      | 11.4 ms: 1.02x faster                                                       |
| pickle_pure_python   | 329 us                                                                       | 326 us: 1.01x faster                                                        |
| xml_etree_process    | 59.2 ms                                                                      | 58.7 ms: 1.01x faster                                                       |
| json_loads           | 24.3 us                                                                      | 24.6 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 16.1 ms                                                                      | 16.0 ms: 1.00x faster                                                       |
| python_startup_no_site | 9.04 ms                                                                      | 9.02 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                                      | 10.9 ms: 1.03x faster                                                       |
| genshi_xml      | 53.9 ms                                                                      | 52.5 ms: 1.03x faster                                                       |
| django_template | 35.9 ms                                                                      | 35.1 ms: 1.02x faster                                                       |
| genshi_text     | 23.6 ms                                                                      | 23.9 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| bench_mp_pool              | 1.64 sec                                                                     | 891 ms: 1.84x faster                                                        |
| typing_runtime_protocols   | 178 us                                                                       | 171 us: 1.04x faster                                                        |
| async_tree_io_tg           | 629 ms                                                                       | 604 ms: 1.04x faster                                                        |
| go                         | 131 ms                                                                       | 126 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 207 us                                                                       | 201 us: 1.03x faster                                                        |
| async_tree_io              | 638 ms                                                                       | 618 ms: 1.03x faster                                                        |
| deepcopy_reduce            | 3.00 us                                                                      | 2.91 us: 1.03x faster                                                       |
| coroutines                 | 21.3 ms                                                                      | 20.6 ms: 1.03x faster                                                       |
| async_tree_none_tg         | 270 ms                                                                       | 262 ms: 1.03x faster                                                        |
| regex_dna                  | 252 ms                                                                       | 245 ms: 1.03x faster                                                        |
| coverage                   | 79.6 ms                                                                      | 77.3 ms: 1.03x faster                                                       |
| regex_effbot               | 3.34 ms                                                                      | 3.25 ms: 1.03x faster                                                       |
| mako                       | 11.2 ms                                                                      | 10.9 ms: 1.03x faster                                                       |
| genshi_xml                 | 53.9 ms                                                                      | 52.5 ms: 1.03x faster                                                       |
| async_tree_memoization_tg  | 328 ms                                                                       | 320 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.59 sec                                                                     | 1.55 sec: 1.02x faster                                                      |
| async_tree_none            | 288 ms                                                                       | 282 ms: 1.02x faster                                                        |
| django_template            | 35.9 ms                                                                      | 35.1 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 783 ms                                                                       | 767 ms: 1.02x faster                                                        |
| raytrace                   | 273 ms                                                                       | 268 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 499 ms                                                                       | 489 ms: 1.02x faster                                                        |
| deepcopy                   | 287 us                                                                       | 282 us: 1.02x faster                                                        |
| xml_etree_parse            | 137 ms                                                                       | 134 ms: 1.02x faster                                                        |
| json_dumps                 | 11.6 ms                                                                      | 11.4 ms: 1.02x faster                                                       |
| sqlglot_parse              | 1.34 ms                                                                      | 1.32 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.2 ms                                                                      | 22.8 ms: 1.02x faster                                                       |
| sqlglot_transpile          | 1.74 ms                                                                      | 1.72 ms: 1.02x faster                                                       |
| async_tree_memoization     | 352 ms                                                                       | 346 ms: 1.02x faster                                                        |
| chaos                      | 61.8 ms                                                                      | 60.9 ms: 1.01x faster                                                       |
| mypy2                      | 1.03 sec                                                                     | 1.02 sec: 1.01x faster                                                      |
| json                       | 5.14 ms                                                                      | 5.07 ms: 1.01x faster                                                       |
| sympy_sum                  | 152 ms                                                                       | 150 ms: 1.01x faster                                                        |
| html5lib                   | 67.7 ms                                                                      | 66.8 ms: 1.01x faster                                                       |
| scimark_lu                 | 96.1 ms                                                                      | 94.8 ms: 1.01x faster                                                       |
| thrift                     | 865 us                                                                       | 854 us: 1.01x faster                                                        |
| sqlglot_normalize          | 115 ms                                                                       | 114 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 58.1 ms                                                                      | 57.5 ms: 1.01x faster                                                       |
| comprehensions             | 17.9 us                                                                      | 17.7 us: 1.01x faster                                                       |
| many_optionals             | 1.02 ms                                                                      | 1.01 ms: 1.01x faster                                                       |
| docutils                   | 2.90 sec                                                                     | 2.87 sec: 1.01x faster                                                      |
| pickle_pure_python         | 329 us                                                                       | 326 us: 1.01x faster                                                        |
| subparsers                 | 22.9 ms                                                                      | 22.7 ms: 1.01x faster                                                       |
| xml_etree_process          | 59.2 ms                                                                      | 58.7 ms: 1.01x faster                                                       |
| pathlib                    | 16.0 ms                                                                      | 15.9 ms: 1.01x faster                                                       |
| regex_compile              | 135 ms                                                                       | 134 ms: 1.01x faster                                                        |
| generators                 | 28.8 ms                                                                      | 28.6 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 515 ms                                                                       | 512 ms: 1.01x faster                                                        |
| logging_silent             | 98.7 ns                                                                      | 98.2 ns: 1.00x faster                                                       |
| sympy_str                  | 291 ms                                                                       | 290 ms: 1.00x faster                                                        |
| shortest_path              | 444 ms                                                                       | 442 ms: 1.00x faster                                                        |
| deltablue                  | 3.40 ms                                                                      | 3.39 ms: 1.00x faster                                                       |
| 2to3                       | 281 ms                                                                       | 280 ms: 1.00x faster                                                        |
| python_startup             | 16.1 ms                                                                      | 16.0 ms: 1.00x faster                                                       |
| sympy_expand               | 500 ms                                                                       | 499 ms: 1.00x faster                                                        |
| regex_v8                   | 26.8 ms                                                                      | 26.8 ms: 1.00x faster                                                       |
| python_startup_no_site     | 9.04 ms                                                                      | 9.02 ms: 1.00x faster                                                       |
| sqlalchemy_declarative     | 143 ms                                                                       | 143 ms: 1.00x slower                                                        |
| mdp                        | 2.47 sec                                                                     | 2.48 sec: 1.00x slower                                                      |
| meteor_contest             | 127 ms                                                                       | 127 ms: 1.00x slower                                                        |
| nqueens                    | 89.9 ms                                                                      | 90.5 ms: 1.01x slower                                                       |
| richards                   | 46.3 ms                                                                      | 46.6 ms: 1.01x slower                                                       |
| scimark_sor                | 110 ms                                                                       | 110 ms: 1.01x slower                                                        |
| logging_format             | 6.86 us                                                                      | 6.92 us: 1.01x slower                                                       |
| async_generators           | 433 ms                                                                       | 437 ms: 1.01x slower                                                        |
| genshi_text                | 23.6 ms                                                                      | 23.9 ms: 1.01x slower                                                       |
| telco                      | 7.76 ms                                                                      | 7.84 ms: 1.01x slower                                                       |
| deepcopy_memo              | 30.4 us                                                                      | 30.7 us: 1.01x slower                                                       |
| scimark_fft                | 298 ms                                                                       | 302 ms: 1.01x slower                                                        |
| json_loads                 | 24.3 us                                                                      | 24.6 us: 1.01x slower                                                       |
| bpe_tokeniser              | 4.69 sec                                                                     | 4.76 sec: 1.01x slower                                                      |
| gc_traversal               | 6.53 ms                                                                      | 6.63 ms: 1.02x slower                                                       |
| spectral_norm              | 86.1 ms                                                                      | 87.7 ms: 1.02x slower                                                       |
| logging_simple             | 6.21 us                                                                      | 6.36 us: 1.02x slower                                                       |
| crypto_pyaes               | 72.0 ms                                                                      | 73.9 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 62.1 ms                                                                      | 63.8 ms: 1.03x slower                                                       |
| pyflate                    | 433 ms                                                                       | 451 ms: 1.04x slower                                                        |
| scimark_sparse_mat_mult    | 4.36 ms                                                                      | 4.64 ms: 1.06x slower                                                       |
| fannkuch                   | 348 ms                                                                       | 373 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (19): sphinx, pylint, create_gc_cycles, bench_thread_pool, xml_etree_generate, xml_etree_iterparse, sqlite_synth, sqlalchemy_imperative, nbody, float, k_core, tomli_loads, pidigits, hexiom, connected_components, pycparser, dulwich_log, asyncio_websockets, richards_super

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x