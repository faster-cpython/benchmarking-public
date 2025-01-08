# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.010x faster
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 226 ms                                                                      | 222 ms: 1.02x faster                                               |
| docutils       | 1.68 sec                                                                    | 1.66 sec: 1.01x faster                                             |
| html5lib       | 39.7 ms                                                                     | 37.1 ms: 1.07x faster                                              |
| sphinx         | 653 ms                                                                      | 641 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_websockets         | 313 ms                                                                      | 303 ms: 1.03x faster                                               |
| coroutines                 | 13.4 ms                                                                     | 13.3 ms: 1.01x faster                                              |
| async_tree_io_tg           | 396 ms                                                                      | 402 ms: 1.01x slower                                               |
| async_tree_memoization_tg  | 207 ms                                                                      | 210 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed    | 343 ms                                                                      | 349 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 337 ms                                                                      | 347 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                       |

Benchmark hidden because not significant (5): async_generators, async_tree_io, async_tree_memoization, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 77.7 ms                                                                     | 73.5 ms: 1.06x faster                                              |
| float          | 53.0 ms                                                                     | 51.2 ms: 1.04x faster                                              |
| pidigits       | 146 ms                                                                      | 148 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 88.9 ms                                                                     | 82.9 ms: 1.07x faster                                              |
| regex_effbot   | 1.49 ms                                                                     | 1.45 ms: 1.03x faster                                              |
| regex_dna      | 125 ms                                                                      | 124 ms: 1.01x faster                                               |
| regex_v8       | 15.5 ms                                                                     | 15.6 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 152 us                                                                      | 144 us: 1.06x faster                                               |
| pickle_pure_python   | 227 us                                                                      | 220 us: 1.03x faster                                               |
| xml_etree_generate   | 57.6 ms                                                                     | 57.0 ms: 1.01x faster                                              |
| xml_etree_parse      | 89.3 ms                                                                     | 88.6 ms: 1.01x faster                                              |
| xml_etree_process    | 40.8 ms                                                                     | 40.6 ms: 1.01x faster                                              |
| tomli_loads          | 1.42 sec                                                                    | 1.41 sec: 1.00x faster                                             |
| xml_etree_iterparse  | 62.3 ms                                                                     | 63.8 ms: 1.02x slower                                              |
| json_dumps           | 6.61 ms                                                                     | 6.80 ms: 1.03x slower                                              |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup | 23.2 ms                                                                     | 23.4 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 35.5 ms                                                                     | 34.9 ms: 1.02x faster                                              |
| mako           | 6.78 ms                                                                     | 6.71 ms: 1.01x faster                                              |
| genshi_text    | 16.3 ms                                                                     | 16.9 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| scimark_lu                 | 62.7 ms                                                                     | 57.0 ms: 1.10x faster                                              |
| dulwich_log                | 42.1 ms                                                                     | 39.0 ms: 1.08x faster                                              |
| logging_silent             | 66.2 ns                                                                     | 61.7 ns: 1.07x faster                                              |
| regex_compile              | 88.9 ms                                                                     | 82.9 ms: 1.07x faster                                              |
| html5lib                   | 39.7 ms                                                                     | 37.1 ms: 1.07x faster                                              |
| unpickle_pure_python       | 152 us                                                                      | 144 us: 1.06x faster                                               |
| nbody                      | 77.7 ms                                                                     | 73.5 ms: 1.06x faster                                              |
| sympy_expand               | 304 ms                                                                      | 288 ms: 1.06x faster                                               |
| scimark_monte_carlo        | 47.1 ms                                                                     | 44.5 ms: 1.06x faster                                              |
| spectral_norm              | 61.7 ms                                                                     | 59.1 ms: 1.05x faster                                              |
| go                         | 89.0 ms                                                                     | 85.3 ms: 1.04x faster                                              |
| deepcopy_memo              | 21.3 us                                                                     | 20.4 us: 1.04x faster                                              |
| sqlglot_parse              | 912 us                                                                      | 877 us: 1.04x faster                                               |
| float                      | 53.0 ms                                                                     | 51.2 ms: 1.04x faster                                              |
| sympy_str                  | 177 ms                                                                      | 171 ms: 1.04x faster                                               |
| asyncio_websockets         | 313 ms                                                                      | 303 ms: 1.03x faster                                               |
| pickle_pure_python         | 227 us                                                                      | 220 us: 1.03x faster                                               |
| scimark_fft                | 191 ms                                                                      | 185 ms: 1.03x faster                                               |
| regex_effbot               | 1.49 ms                                                                     | 1.45 ms: 1.03x faster                                              |
| pprint_pformat             | 1.11 sec                                                                    | 1.09 sec: 1.02x faster                                             |
| hexiom                     | 4.43 ms                                                                     | 4.33 ms: 1.02x faster                                              |
| sympy_sum                  | 90.3 ms                                                                     | 88.4 ms: 1.02x faster                                              |
| deltablue                  | 2.28 ms                                                                     | 2.23 ms: 1.02x faster                                              |
| json                       | 3.03 ms                                                                     | 2.97 ms: 1.02x faster                                              |
| scimark_sparse_mat_mult    | 2.59 ms                                                                     | 2.54 ms: 1.02x faster                                              |
| sqlglot_transpile          | 1.13 ms                                                                     | 1.10 ms: 1.02x faster                                              |
| sphinx                     | 653 ms                                                                      | 641 ms: 1.02x faster                                               |
| many_optionals             | 441 us                                                                      | 433 us: 1.02x faster                                               |
| richards                   | 31.6 ms                                                                     | 31.1 ms: 1.02x faster                                              |
| 2to3                       | 226 ms                                                                      | 222 ms: 1.02x faster                                               |
| genshi_xml                 | 35.5 ms                                                                     | 34.9 ms: 1.02x faster                                              |
| logging_simple             | 6.45 us                                                                     | 6.37 us: 1.01x faster                                              |
| xml_etree_generate         | 57.6 ms                                                                     | 57.0 ms: 1.01x faster                                              |
| regex_dna                  | 125 ms                                                                      | 124 ms: 1.01x faster                                               |
| docutils                   | 1.68 sec                                                                    | 1.66 sec: 1.01x faster                                             |
| mako                       | 6.78 ms                                                                     | 6.71 ms: 1.01x faster                                              |
| richards_super             | 35.6 ms                                                                     | 35.3 ms: 1.01x faster                                              |
| thrift                     | 520 us                                                                      | 514 us: 1.01x faster                                               |
| logging_format             | 6.90 us                                                                     | 6.83 us: 1.01x faster                                              |
| gc_traversal               | 1.98 ms                                                                     | 1.96 ms: 1.01x faster                                              |
| mypy2                      | 645 ms                                                                      | 639 ms: 1.01x faster                                               |
| scimark_sor                | 89.7 ms                                                                     | 88.9 ms: 1.01x faster                                              |
| coroutines                 | 13.4 ms                                                                     | 13.3 ms: 1.01x faster                                              |
| xml_etree_parse            | 89.3 ms                                                                     | 88.6 ms: 1.01x faster                                              |
| crypto_pyaes               | 48.6 ms                                                                     | 48.2 ms: 1.01x faster                                              |
| sqlglot_optimize           | 35.8 ms                                                                     | 35.6 ms: 1.01x faster                                              |
| telco                      | 4.82 ms                                                                     | 4.78 ms: 1.01x faster                                              |
| xml_etree_process          | 40.8 ms                                                                     | 40.6 ms: 1.01x faster                                              |
| pprint_safe_repr           | 545 ms                                                                      | 542 ms: 1.01x faster                                               |
| deepcopy_reduce            | 1.90 us                                                                     | 1.89 us: 1.01x faster                                              |
| tomli_loads                | 1.42 sec                                                                    | 1.41 sec: 1.00x faster                                             |
| regex_v8                   | 15.5 ms                                                                     | 15.6 ms: 1.00x slower                                              |
| sqlglot_normalize          | 195 ms                                                                      | 196 ms: 1.00x slower                                               |
| bpe_tokeniser              | 2.98 sec                                                                    | 3.00 sec: 1.01x slower                                             |
| deepcopy                   | 185 us                                                                      | 187 us: 1.01x slower                                               |
| mdp                        | 1.49 sec                                                                    | 1.50 sec: 1.01x slower                                             |
| create_gc_cycles           | 1.19 ms                                                                     | 1.20 ms: 1.01x slower                                              |
| generators                 | 21.7 ms                                                                     | 21.9 ms: 1.01x slower                                              |
| pidigits                   | 146 ms                                                                      | 148 ms: 1.01x slower                                               |
| python_startup             | 23.2 ms                                                                     | 23.4 ms: 1.01x slower                                              |
| nqueens                    | 63.0 ms                                                                     | 63.8 ms: 1.01x slower                                              |
| async_tree_io_tg           | 396 ms                                                                      | 402 ms: 1.01x slower                                               |
| shortest_path              | 349 ms                                                                      | 354 ms: 1.01x slower                                               |
| raytrace                   | 186 ms                                                                      | 188 ms: 1.01x slower                                               |
| fannkuch                   | 267 ms                                                                      | 271 ms: 1.02x slower                                               |
| connected_components       | 317 ms                                                                      | 322 ms: 1.02x slower                                               |
| async_tree_memoization_tg  | 207 ms                                                                      | 210 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed    | 343 ms                                                                      | 349 ms: 1.02x slower                                               |
| coverage                   | 46.0 ms                                                                     | 46.8 ms: 1.02x slower                                              |
| subparsers                 | 16.1 ms                                                                     | 16.5 ms: 1.02x slower                                              |
| xml_etree_iterparse        | 62.3 ms                                                                     | 63.8 ms: 1.02x slower                                              |
| comprehensions             | 12.0 us                                                                     | 12.3 us: 1.03x slower                                              |
| async_tree_cpu_io_mixed_tg | 337 ms                                                                      | 347 ms: 1.03x slower                                               |
| json_dumps                 | 6.61 ms                                                                     | 6.80 ms: 1.03x slower                                              |
| sqlite_synth               | 1.61 us                                                                     | 1.66 us: 1.03x slower                                              |
| genshi_text                | 16.3 ms                                                                     | 16.9 ms: 1.04x slower                                              |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                       |

Benchmark hidden because not significant (19): pyflate, k_core, pycparser, pathlib, json_loads, typing_runtime_protocols, async_generators, meteor_contest, async_tree_io, async_tree_memoization, django_template, bench_mp_pool, python_startup_no_site, async_tree_none, chaos, sympy_integrate, pylint, async_tree_none_tg, bench_thread_pool

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 99.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown