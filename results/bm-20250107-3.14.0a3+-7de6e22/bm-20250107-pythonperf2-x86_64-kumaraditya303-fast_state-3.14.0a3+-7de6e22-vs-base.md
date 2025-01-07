# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.008x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 279 ms: 1.01x faster                                                       |
| docutils       | 2.90 sec                                                                     | 2.87 sec: 1.01x faster                                                     |
| sphinx         | 1.11 sec                                                                     | 1.10 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 629 ms                                                                       | 606 ms: 1.04x faster                                                       |
| async_tree_memoization_tg  | 328 ms                                                                       | 318 ms: 1.03x faster                                                       |
| async_tree_none_tg         | 270 ms                                                                       | 262 ms: 1.03x faster                                                       |
| async_tree_io              | 638 ms                                                                       | 618 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 499 ms                                                                       | 487 ms: 1.03x faster                                                       |
| async_tree_none            | 288 ms                                                                       | 282 ms: 1.02x faster                                                       |
| async_tree_memoization     | 352 ms                                                                       | 345 ms: 1.02x faster                                                       |
| coroutines                 | 21.3 ms                                                                      | 20.9 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 515 ms                                                                       | 511 ms: 1.01x faster                                                       |
| async_generators           | 433 ms                                                                       | 430 ms: 1.01x faster                                                       |
| Geometric mean             | (ref)                                                                        | 1.02x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 252 ms                                                                       | 231 ms: 1.09x faster                                                       |
| regex_effbot   | 3.34 ms                                                                      | 3.19 ms: 1.05x faster                                                      |
| regex_v8       | 26.8 ms                                                                      | 26.5 ms: 1.01x faster                                                      |
| regex_compile  | 135 ms                                                                       | 134 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                        | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 83.5 ms                                                                      | 82.2 ms: 1.02x faster                                                      |
| tomli_loads          | 2.05 sec                                                                     | 2.03 sec: 1.01x faster                                                     |
| xml_etree_process    | 59.2 ms                                                                      | 58.6 ms: 1.01x faster                                                      |
| pickle_pure_python   | 329 us                                                                       | 326 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 95.7 ms                                                                      | 95.1 ms: 1.01x faster                                                      |
| unpickle_pure_python | 207 us                                                                       | 206 us: 1.01x faster                                                       |
| json_dumps           | 11.6 ms                                                                      | 11.5 ms: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 9.04 ms                                                                      | 8.98 ms: 1.01x faster                                                      |
| python_startup         | 16.1 ms                                                                      | 16.0 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                        | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 11.2 ms                                                                      | 11.0 ms: 1.01x faster                                                      |
| genshi_xml     | 53.9 ms                                                                      | 54.4 ms: 1.01x slower                                                      |
| genshi_text    | 23.6 ms                                                                      | 24.0 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna                  | 252 ms                                                                       | 231 ms: 1.09x faster                                                       |
| gc_traversal               | 6.53 ms                                                                      | 6.15 ms: 1.06x faster                                                      |
| regex_effbot               | 3.34 ms                                                                      | 3.19 ms: 1.05x faster                                                      |
| async_tree_io_tg           | 629 ms                                                                       | 606 ms: 1.04x faster                                                       |
| coverage                   | 79.6 ms                                                                      | 76.7 ms: 1.04x faster                                                      |
| async_tree_memoization_tg  | 328 ms                                                                       | 318 ms: 1.03x faster                                                       |
| async_tree_none_tg         | 270 ms                                                                       | 262 ms: 1.03x faster                                                       |
| async_tree_io              | 638 ms                                                                       | 618 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 3.00 us                                                                      | 2.91 us: 1.03x faster                                                      |
| typing_runtime_protocols   | 178 us                                                                       | 173 us: 1.03x faster                                                       |
| deepcopy                   | 287 us                                                                       | 280 us: 1.03x faster                                                       |
| raytrace                   | 273 ms                                                                       | 266 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 499 ms                                                                       | 487 ms: 1.03x faster                                                       |
| deepcopy_memo              | 30.4 us                                                                      | 29.6 us: 1.02x faster                                                      |
| generators                 | 28.8 ms                                                                      | 28.1 ms: 1.02x faster                                                      |
| async_tree_none            | 288 ms                                                                       | 282 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 783 ms                                                                       | 768 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.59 sec                                                                     | 1.56 sec: 1.02x faster                                                     |
| go                         | 131 ms                                                                       | 129 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 115 ms                                                                       | 113 ms: 1.02x faster                                                       |
| async_tree_memoization     | 352 ms                                                                       | 345 ms: 1.02x faster                                                       |
| sqlglot_transpile          | 1.74 ms                                                                      | 1.71 ms: 1.02x faster                                                      |
| create_gc_cycles           | 2.80 ms                                                                      | 2.75 ms: 1.02x faster                                                      |
| coroutines                 | 21.3 ms                                                                      | 20.9 ms: 1.02x faster                                                      |
| sqlglot_parse              | 1.34 ms                                                                      | 1.32 ms: 1.02x faster                                                      |
| xml_etree_generate         | 83.5 ms                                                                      | 82.2 ms: 1.02x faster                                                      |
| sqlglot_optimize           | 58.1 ms                                                                      | 57.3 ms: 1.01x faster                                                      |
| comprehensions             | 17.9 us                                                                      | 17.7 us: 1.01x faster                                                      |
| mako                       | 11.2 ms                                                                      | 11.0 ms: 1.01x faster                                                      |
| sphinx                     | 1.11 sec                                                                     | 1.10 sec: 1.01x faster                                                     |
| sympy_integrate            | 23.2 ms                                                                      | 23.0 ms: 1.01x faster                                                      |
| regex_v8                   | 26.8 ms                                                                      | 26.5 ms: 1.01x faster                                                      |
| docutils                   | 2.90 sec                                                                     | 2.87 sec: 1.01x faster                                                     |
| regex_compile              | 135 ms                                                                       | 134 ms: 1.01x faster                                                       |
| tomli_loads                | 2.05 sec                                                                     | 2.03 sec: 1.01x faster                                                     |
| sympy_sum                  | 152 ms                                                                       | 151 ms: 1.01x faster                                                       |
| meteor_contest             | 127 ms                                                                       | 126 ms: 1.01x faster                                                       |
| xml_etree_process          | 59.2 ms                                                                      | 58.6 ms: 1.01x faster                                                      |
| json                       | 5.14 ms                                                                      | 5.10 ms: 1.01x faster                                                      |
| pickle_pure_python         | 329 us                                                                       | 326 us: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 515 ms                                                                       | 511 ms: 1.01x faster                                                       |
| 2to3                       | 281 ms                                                                       | 279 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 95.7 ms                                                                      | 95.1 ms: 1.01x faster                                                      |
| python_startup_no_site     | 9.04 ms                                                                      | 8.98 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 207 us                                                                       | 206 us: 1.01x faster                                                       |
| pathlib                    | 16.0 ms                                                                      | 15.9 ms: 1.01x faster                                                      |
| async_generators           | 433 ms                                                                       | 430 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.85 us                                                                      | 2.83 us: 1.01x faster                                                      |
| hexiom                     | 6.07 ms                                                                      | 6.04 ms: 1.01x faster                                                      |
| sqlalchemy_imperative      | 17.9 ms                                                                      | 17.8 ms: 1.01x faster                                                      |
| json_dumps                 | 11.6 ms                                                                      | 11.5 ms: 1.01x faster                                                      |
| python_startup             | 16.1 ms                                                                      | 16.0 ms: 1.00x faster                                                      |
| connected_components       | 418 ms                                                                       | 417 ms: 1.00x faster                                                       |
| mdp                        | 2.47 sec                                                                     | 2.46 sec: 1.00x faster                                                     |
| nqueens                    | 89.9 ms                                                                      | 89.5 ms: 1.00x faster                                                      |
| sympy_expand               | 500 ms                                                                       | 499 ms: 1.00x faster                                                       |
| sympy_str                  | 291 ms                                                                       | 290 ms: 1.00x faster                                                       |
| deltablue                  | 3.40 ms                                                                      | 3.41 ms: 1.00x slower                                                      |
| shortest_path              | 444 ms                                                                       | 445 ms: 1.00x slower                                                       |
| bpe_tokeniser              | 4.69 sec                                                                     | 4.71 sec: 1.00x slower                                                     |
| chaos                      | 61.8 ms                                                                      | 62.3 ms: 1.01x slower                                                      |
| genshi_xml                 | 53.9 ms                                                                      | 54.4 ms: 1.01x slower                                                      |
| sqlalchemy_declarative     | 143 ms                                                                       | 144 ms: 1.01x slower                                                       |
| crypto_pyaes               | 72.0 ms                                                                      | 73.0 ms: 1.01x slower                                                      |
| spectral_norm              | 86.1 ms                                                                      | 87.4 ms: 1.01x slower                                                      |
| genshi_text                | 23.6 ms                                                                      | 24.0 ms: 1.02x slower                                                      |
| pyflate                    | 433 ms                                                                       | 440 ms: 1.02x slower                                                       |
| fannkuch                   | 348 ms                                                                       | 355 ms: 1.02x slower                                                       |
| scimark_sor                | 110 ms                                                                       | 112 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 62.1 ms                                                                      | 63.5 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 4.36 ms                                                                      | 4.52 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (26): bench_mp_pool, mypy2, html5lib, pycparser, subparsers, bench_thread_pool, scimark_lu, logging_simple, many_optionals, telco, json_loads, pidigits, scimark_fft, asyncio_websockets, dulwich_log, thrift, richards, xml_etree_parse, nbody, pylint, logging_format, richards_super, django_template, float, logging_silent, k_core

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x