
# Results vs. base

- fork: brandtbucher
- ref: not_none
- machine: linux-x86_64
- commit hash: 806df38
- commit date: 2023-07-10
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.67 sec: 1.01x slower                                          |
| tornado_http   | 96.1 ms                                                               | 97.4 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 79.9 ms                                                               | 78.7 ms: 1.01x faster                                           |
| nbody          | 88.2 ms                                                               | 89.4 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                | 210 ms: 1.01x slower                                            |
| regex_compile  | 136 ms                                                                | 138 ms: 1.01x slower                                            |
| regex_effbot   | 3.49 ms                                                               | 3.57 ms: 1.03x slower                                           |
| regex_v8       | 21.8 ms                                                               | 23.0 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_process    | 57.7 ms                                                               | 57.4 ms: 1.01x faster                                           |
| unpickle_pure_python | 212 us                                                                | 211 us: 1.00x faster                                            |
| json_loads           | 25.8 us                                                               | 25.7 us: 1.00x faster                                           |
| pickle_pure_python   | 294 us                                                                | 296 us: 1.01x slower                                            |
| xml_etree_generate   | 83.9 ms                                                               | 84.6 ms: 1.01x slower                                           |
| xml_etree_parse      | 151 ms                                                                | 153 ms: 1.01x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (8): pickle, unpickle, unpickle_list, pickle_dict, tomli_loads, pickle_list, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.72 ms                                                               | 6.67 ms: 1.01x faster                                           |
| python_startup         | 9.23 ms                                                               | 9.17 ms: 1.01x faster                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                     | 2.71 sec                                                              | 2.58 sec: 1.05x faster                                          |
| spectral_norm           | 108 ms                                                                | 104 ms: 1.04x faster                                            |
| gc_traversal            | 4.21 ms                                                               | 4.07 ms: 1.03x faster                                           |
| pycparser               | 1.19 sec                                                              | 1.16 sec: 1.03x faster                                          |
| deepcopy_memo           | 38.0 us                                                               | 37.4 us: 1.02x faster                                           |
| create_gc_cycles        | 1.51 ms                                                               | 1.48 ms: 1.02x faster                                           |
| scimark_lu              | 112 ms                                                                | 110 ms: 1.02x faster                                            |
| async_generators        | 450 ms                                                                | 443 ms: 1.02x faster                                            |
| float                   | 79.9 ms                                                               | 78.7 ms: 1.01x faster                                           |
| sqlite_synth            | 2.77 us                                                               | 2.73 us: 1.01x faster                                           |
| pathlib                 | 18.8 ms                                                               | 18.5 ms: 1.01x faster                                           |
| async_tree_cpu_io_mixed | 726 ms                                                                | 717 ms: 1.01x faster                                            |
| pprint_safe_repr        | 734 ms                                                                | 725 ms: 1.01x faster                                            |
| crypto_pyaes            | 70.3 ms                                                               | 69.6 ms: 1.01x faster                                           |
| raytrace                | 273 ms                                                                | 271 ms: 1.01x faster                                            |
| logging_format          | 6.60 us                                                               | 6.54 us: 1.01x faster                                           |
| async_tree_io           | 1.19 sec                                                              | 1.18 sec: 1.01x faster                                          |
| async_tree_memoization  | 589 ms                                                                | 584 ms: 1.01x faster                                            |
| scimark_monte_carlo     | 68.0 ms                                                               | 67.4 ms: 1.01x faster                                           |
| mako                    | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                           |
| pyflate                 | 450 ms                                                                | 446 ms: 1.01x faster                                            |
| async_tree_none         | 483 ms                                                                | 479 ms: 1.01x faster                                            |
| python_startup_no_site  | 6.72 ms                                                               | 6.67 ms: 1.01x faster                                           |
| asyncio_tcp             | 510 ms                                                                | 507 ms: 1.01x faster                                            |
| python_startup          | 9.23 ms                                                               | 9.17 ms: 1.01x faster                                           |
| pprint_pformat          | 1.50 sec                                                              | 1.49 sec: 1.01x faster                                          |
| xml_etree_process       | 57.7 ms                                                               | 57.4 ms: 1.01x faster                                           |
| unpickle_pure_python    | 212 us                                                                | 211 us: 1.00x faster                                            |
| bench_thread_pool       | 820 us                                                                | 816 us: 1.00x faster                                            |
| json_loads              | 25.8 us                                                               | 25.7 us: 1.00x faster                                           |
| sqlglot_parse           | 1.29 ms                                                               | 1.30 ms: 1.00x slower                                           |
| mypy2                   | 336 ms                                                                | 338 ms: 1.00x slower                                            |
| fannkuch                | 387 ms                                                                | 389 ms: 1.01x slower                                            |
| docutils                | 2.65 sec                                                              | 2.67 sec: 1.01x slower                                          |
| sqlglot_optimize        | 52.6 ms                                                               | 53.0 ms: 1.01x slower                                           |
| logging_simple          | 5.93 us                                                               | 5.96 us: 1.01x slower                                           |
| pickle_pure_python      | 294 us                                                                | 296 us: 1.01x slower                                            |
| generators              | 28.8 ms                                                               | 29.0 ms: 1.01x slower                                           |
| xml_etree_generate      | 83.9 ms                                                               | 84.6 ms: 1.01x slower                                           |
| regex_dna               | 208 ms                                                                | 210 ms: 1.01x slower                                            |
| meteor_contest          | 105 ms                                                                | 106 ms: 1.01x slower                                            |
| deepcopy_reduce         | 3.17 us                                                               | 3.21 us: 1.01x slower                                           |
| chaos                   | 58.9 ms                                                               | 59.7 ms: 1.01x slower                                           |
| sqlglot_normalize       | 105 ms                                                                | 106 ms: 1.01x slower                                            |
| xml_etree_parse         | 151 ms                                                                | 153 ms: 1.01x slower                                            |
| nbody                   | 88.2 ms                                                               | 89.4 ms: 1.01x slower                                           |
| tornado_http            | 96.1 ms                                                               | 97.4 ms: 1.01x slower                                           |
| regex_compile           | 136 ms                                                                | 138 ms: 1.01x slower                                            |
| dulwich_log             | 65.4 ms                                                               | 66.4 ms: 1.01x slower                                           |
| scimark_sparse_mat_mult | 4.70 ms                                                               | 4.79 ms: 1.02x slower                                           |
| coroutines              | 22.1 ms                                                               | 22.6 ms: 1.02x slower                                           |
| regex_effbot            | 3.49 ms                                                               | 3.57 ms: 1.03x slower                                           |
| telco                   | 7.12 ms                                                               | 7.30 ms: 1.03x slower                                           |
| richards                | 46.3 ms                                                               | 47.8 ms: 1.03x slower                                           |
| richards_super          | 52.4 ms                                                               | 54.3 ms: 1.04x slower                                           |
| regex_v8                | 21.8 ms                                                               | 23.0 ms: 1.05x slower                                           |
| unpack_sequence         | 43.8 ns                                                               | 47.0 ns: 1.07x slower                                           |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (25): logging_silent, typing_runtime_protocols, pickle, unpickle, nqueens, unpickle_list, comprehensions, scimark_sor, pickle_dict, tomli_loads, pidigits, deltablue, asyncio_tcp_ssl, bench_mp_pool, hexiom, pickle_list, go, scimark_fft, sqlglot_transpile, deepcopy, json_dumps, xml_etree_iterparse, coverage, json, dask
