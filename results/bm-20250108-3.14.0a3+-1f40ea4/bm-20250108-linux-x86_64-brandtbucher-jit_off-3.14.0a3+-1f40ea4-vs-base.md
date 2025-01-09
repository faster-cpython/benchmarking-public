# Results vs. base

- fork: brandtbucher
- ref: jit_off
- machine: linux-x86_64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.003x slower
- HPT reliability: 89.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 255 ms: 1.00x faster                                            |
| docutils       | 2.60 sec                                                               | 2.62 sec: 1.00x slower                                          |
| html5lib       | 62.6 ms                                                                | 61.8 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| coroutines                 | 23.7 ms                                                                | 23.1 ms: 1.03x faster                                           |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 461 ms: 1.02x faster                                            |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 483 ms: 1.02x faster                                            |
| asyncio_websockets         | 551 ms                                                                 | 553 ms: 1.00x slower                                            |
| async_generators           | 418 ms                                                                 | 429 ms: 1.03x slower                                            |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 190 ms: 1.00x faster                                            |
| nbody          | 92.9 ms                                                                | 97.8 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.52 ms                                                                | 3.42 ms: 1.03x faster                                           |
| regex_dna      | 221 ms                                                                 | 215 ms: 1.03x faster                                            |
| regex_v8       | 25.6 ms                                                                | 25.8 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 11.5 ms                                                                | 11.3 ms: 1.02x faster                                           |
| xml_etree_process    | 59.9 ms                                                                | 59.1 ms: 1.01x faster                                           |
| xml_etree_generate   | 85.6 ms                                                                | 84.7 ms: 1.01x faster                                           |
| xml_etree_parse      | 139 ms                                                                 | 138 ms: 1.01x faster                                            |
| unpickle_pure_python | 218 us                                                                 | 217 us: 1.00x faster                                            |
| pickle_pure_python   | 320 us                                                                 | 323 us: 1.01x slower                                            |
| tomli_loads          | 1.97 sec                                                               | 1.99 sec: 1.01x slower                                          |
| xml_etree_iterparse  | 96.4 ms                                                                | 98.3 ms: 1.02x slower                                           |
| json_loads           | 26.4 us                                                                | 27.1 us: 1.03x slower                                           |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                           |
| python_startup_no_site | 7.06 ms                                                                | 7.06 ms: 1.00x slower                                           |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 11.7 ms                                                                | 11.4 ms: 1.02x faster                                           |
| django_template | 31.5 ms                                                                | 32.0 ms: 1.01x slower                                           |
| genshi_text     | 22.1 ms                                                                | 22.7 ms: 1.03x slower                                           |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot               | 3.52 ms                                                                | 3.42 ms: 1.03x faster                                           |
| regex_dna                  | 221 ms                                                                 | 215 ms: 1.03x faster                                            |
| pprint_safe_repr           | 732 ms                                                                 | 713 ms: 1.03x faster                                            |
| coroutines                 | 23.7 ms                                                                | 23.1 ms: 1.03x faster                                           |
| mako                       | 11.7 ms                                                                | 11.4 ms: 1.02x faster                                           |
| json_dumps                 | 11.5 ms                                                                | 11.3 ms: 1.02x faster                                           |
| pprint_pformat             | 1.49 sec                                                               | 1.46 sec: 1.02x faster                                          |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 461 ms: 1.02x faster                                            |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 483 ms: 1.02x faster                                            |
| scimark_fft                | 353 ms                                                                 | 347 ms: 1.02x faster                                            |
| logging_simple             | 5.65 us                                                                | 5.57 us: 1.02x faster                                           |
| xml_etree_process          | 59.9 ms                                                                | 59.1 ms: 1.01x faster                                           |
| html5lib                   | 62.6 ms                                                                | 61.8 ms: 1.01x faster                                           |
| xml_etree_generate         | 85.6 ms                                                                | 84.7 ms: 1.01x faster                                           |
| hexiom                     | 6.29 ms                                                                | 6.24 ms: 1.01x faster                                           |
| coverage                   | 84.3 ms                                                                | 83.6 ms: 1.01x faster                                           |
| nqueens                    | 80.5 ms                                                                | 79.9 ms: 1.01x faster                                           |
| deltablue                  | 3.32 ms                                                                | 3.29 ms: 1.01x faster                                           |
| xml_etree_parse            | 139 ms                                                                 | 138 ms: 1.01x faster                                            |
| logging_format             | 6.17 us                                                                | 6.12 us: 1.01x faster                                           |
| comprehensions             | 16.8 us                                                                | 16.7 us: 1.01x faster                                           |
| scimark_sparse_mat_mult    | 4.82 ms                                                                | 4.79 ms: 1.01x faster                                           |
| sympy_expand               | 459 ms                                                                 | 456 ms: 1.01x faster                                            |
| sympy_integrate            | 19.9 ms                                                                | 19.8 ms: 1.01x faster                                           |
| sqlglot_transpile          | 1.59 ms                                                                | 1.58 ms: 1.00x faster                                           |
| scimark_sor                | 124 ms                                                                 | 124 ms: 1.00x faster                                            |
| sqlglot_parse              | 1.28 ms                                                                | 1.27 ms: 1.00x faster                                           |
| unpickle_pure_python       | 218 us                                                                 | 217 us: 1.00x faster                                            |
| bench_thread_pool          | 867 us                                                                 | 864 us: 1.00x faster                                            |
| 2to3                       | 255 ms                                                                 | 255 ms: 1.00x faster                                            |
| sqlalchemy_declarative     | 130 ms                                                                 | 129 ms: 1.00x faster                                            |
| pidigits                   | 190 ms                                                                 | 190 ms: 1.00x faster                                            |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                           |
| python_startup_no_site     | 7.06 ms                                                                | 7.06 ms: 1.00x slower                                           |
| many_optionals             | 947 us                                                                 | 950 us: 1.00x slower                                            |
| asyncio_websockets         | 551 ms                                                                 | 553 ms: 1.00x slower                                            |
| go                         | 118 ms                                                                 | 119 ms: 1.00x slower                                            |
| sqlglot_optimize           | 52.4 ms                                                                | 52.7 ms: 1.00x slower                                           |
| docutils                   | 2.60 sec                                                               | 2.62 sec: 1.00x slower                                          |
| regex_v8                   | 25.6 ms                                                                | 25.8 ms: 1.01x slower                                           |
| dulwich_log                | 63.8 ms                                                                | 64.2 ms: 1.01x slower                                           |
| subparsers                 | 20.7 ms                                                                | 20.8 ms: 1.01x slower                                           |
| create_gc_cycles           | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                           |
| raytrace                   | 272 ms                                                                 | 275 ms: 1.01x slower                                            |
| crypto_pyaes               | 71.7 ms                                                                | 72.4 ms: 1.01x slower                                           |
| deepcopy                   | 261 us                                                                 | 263 us: 1.01x slower                                            |
| bpe_tokeniser              | 4.52 sec                                                               | 4.57 sec: 1.01x slower                                          |
| richards_super             | 51.2 ms                                                                | 51.8 ms: 1.01x slower                                           |
| sqlglot_normalize          | 103 ms                                                                 | 104 ms: 1.01x slower                                            |
| pickle_pure_python         | 320 us                                                                 | 323 us: 1.01x slower                                            |
| thrift                     | 761 us                                                                 | 771 us: 1.01x slower                                            |
| django_template            | 31.5 ms                                                                | 32.0 ms: 1.01x slower                                           |
| tomli_loads                | 1.97 sec                                                               | 1.99 sec: 1.01x slower                                          |
| typing_runtime_protocols   | 164 us                                                                 | 166 us: 1.01x slower                                            |
| telco                      | 7.71 ms                                                                | 7.83 ms: 1.02x slower                                           |
| pyflate                    | 467 ms                                                                 | 476 ms: 1.02x slower                                            |
| meteor_contest             | 105 ms                                                                 | 107 ms: 1.02x slower                                            |
| shortest_path              | 475 ms                                                                 | 484 ms: 1.02x slower                                            |
| xml_etree_iterparse        | 96.4 ms                                                                | 98.3 ms: 1.02x slower                                           |
| generators                 | 27.1 ms                                                                | 27.8 ms: 1.02x slower                                           |
| json_loads                 | 26.4 us                                                                | 27.1 us: 1.03x slower                                           |
| fannkuch                   | 401 ms                                                                 | 412 ms: 1.03x slower                                            |
| async_generators           | 418 ms                                                                 | 429 ms: 1.03x slower                                            |
| genshi_text                | 22.1 ms                                                                | 22.7 ms: 1.03x slower                                           |
| json                       | 4.90 ms                                                                | 5.04 ms: 1.03x slower                                           |
| spectral_norm              | 104 ms                                                                 | 107 ms: 1.03x slower                                            |
| mdp                        | 2.53 sec                                                               | 2.63 sec: 1.04x slower                                          |
| pycparser                  | 1.12 sec                                                               | 1.17 sec: 1.05x slower                                          |
| nbody                      | 92.9 ms                                                                | 97.8 ms: 1.05x slower                                           |
| gc_traversal               | 4.71 ms                                                                | 5.03 ms: 1.07x slower                                           |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (26): async_tree_memoization, async_tree_none, sympy_str, async_tree_io, pylint, sqlite_synth, genshi_xml, sqlalchemy_imperative, sympy_sum, regex_compile, richards, chaos, bench_mp_pool, async_tree_memoization_tg, pathlib, scimark_monte_carlo, async_tree_none_tg, deepcopy_memo, async_tree_io_tg, sphinx, deepcopy_reduce, scimark_lu, k_core, connected_components, logging_silent, float
Ignored benchmarks (1) of results/bm-20250106-3.14.0a3+-7363476/bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476.json: mypy2

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 89.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x