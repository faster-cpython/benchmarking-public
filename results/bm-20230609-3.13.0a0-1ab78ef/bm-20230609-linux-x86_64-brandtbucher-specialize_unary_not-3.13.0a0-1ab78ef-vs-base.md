
# Results vs. base

- fork: brandtbucher
- ref: specialize_unary_not
- machine: linux-x86_64
- commit hash: 1ab78ef
- commit date: 2023-06-09
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.71 sec                                              | 2.74 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 89.0 ms                                               | 89.7 ms: 1.01x slower                                                       |
| pidigits       | 192 ms                                                | 197 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.56 ms                                               | 3.53 ms: 1.01x faster                                                       |
| regex_v8       | 21.9 ms                                               | 21.7 ms: 1.01x faster                                                       |
| regex_compile  | 145 ms                                                | 146 ms: 1.01x slower                                                        |
| regex_dna      | 205 ms                                                | 207 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                 | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_list        | 4.99 us                                               | 4.87 us: 1.02x faster                                                       |
| unpickle             | 15.2 us                                               | 15.0 us: 1.01x faster                                                       |
| xml_etree_process    | 59.0 ms                                               | 58.5 ms: 1.01x faster                                                       |
| json_loads           | 25.2 us                                               | 25.0 us: 1.01x faster                                                       |
| xml_etree_generate   | 84.5 ms                                               | 84.9 ms: 1.00x slower                                                       |
| json_dumps           | 9.78 ms                                               | 9.84 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                | 104 ms: 1.01x slower                                                        |
| pickle_pure_python   | 312 us                                                | 317 us: 1.02x slower                                                        |
| pickle_list          | 4.66 us                                               | 4.75 us: 1.02x slower                                                       |
| pickle_dict          | 31.6 us                                               | 32.1 us: 1.02x slower                                                       |
| tomli_loads          | 2.22 sec                                              | 2.27 sec: 1.02x slower                                                      |
| unpickle_pure_python | 218 us                                                | 226 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|------------------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 9.30 ms                                               | 9.28 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.77 ms                                               | 6.76 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                 | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|-----------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.8 ms                                               | 10.6 ms: 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|-------------------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 4.95 ms                                               | 4.73 ms: 1.05x faster                                                       |
| coroutines              | 23.7 ms                                               | 22.8 ms: 1.04x faster                                                       |
| unpickle_list           | 4.99 us                                               | 4.87 us: 1.02x faster                                                       |
| mako                    | 10.8 ms                                               | 10.6 ms: 1.02x faster                                                       |
| coverage                | 96.3 ms                                               | 95.0 ms: 1.01x faster                                                       |
| unpickle                | 15.2 us                                               | 15.0 us: 1.01x faster                                                       |
| create_gc_cycles        | 1.51 ms                                               | 1.50 ms: 1.01x faster                                                       |
| scimark_fft             | 358 ms                                                | 354 ms: 1.01x faster                                                        |
| regex_effbot            | 3.56 ms                                               | 3.53 ms: 1.01x faster                                                       |
| xml_etree_process       | 59.0 ms                                               | 58.5 ms: 1.01x faster                                                       |
| json_loads              | 25.2 us                                               | 25.0 us: 1.01x faster                                                       |
| regex_v8                | 21.9 ms                                               | 21.7 ms: 1.01x faster                                                       |
| nqueens                 | 81.6 ms                                               | 81.3 ms: 1.00x faster                                                       |
| python_startup          | 9.30 ms                                               | 9.28 ms: 1.00x faster                                                       |
| python_startup_no_site  | 6.77 ms                                               | 6.76 ms: 1.00x faster                                                       |
| xml_etree_generate      | 84.5 ms                                               | 84.9 ms: 1.00x slower                                                       |
| meteor_contest          | 105 ms                                                | 106 ms: 1.00x slower                                                        |
| bench_thread_pool       | 831 us                                                | 836 us: 1.01x slower                                                        |
| fannkuch                | 386 ms                                                | 389 ms: 1.01x slower                                                        |
| json_dumps              | 9.78 ms                                               | 9.84 ms: 1.01x slower                                                       |
| chaos                   | 64.5 ms                                               | 64.9 ms: 1.01x slower                                                       |
| generators              | 30.5 ms                                               | 30.8 ms: 1.01x slower                                                       |
| nbody                   | 89.0 ms                                               | 89.7 ms: 1.01x slower                                                       |
| dask                    | 538 ms                                                | 542 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 103 ms                                                | 104 ms: 1.01x slower                                                        |
| regex_compile           | 145 ms                                                | 146 ms: 1.01x slower                                                        |
| async_tree_memoization  | 595 ms                                                | 600 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl         | 1.79 sec                                              | 1.80 sec: 1.01x slower                                                      |
| dulwich_log             | 67.7 ms                                               | 68.3 ms: 1.01x slower                                                       |
| scimark_lu              | 114 ms                                                | 115 ms: 1.01x slower                                                        |
| telco                   | 6.82 ms                                               | 6.89 ms: 1.01x slower                                                       |
| docutils                | 2.71 sec                                              | 2.74 sec: 1.01x slower                                                      |
| regex_dna               | 205 ms                                                | 207 ms: 1.01x slower                                                        |
| pprint_pformat          | 1.50 sec                                              | 1.51 sec: 1.01x slower                                                      |
| async_tree_io           | 1.21 sec                                              | 1.23 sec: 1.01x slower                                                      |
| raytrace                | 297 ms                                                | 301 ms: 1.01x slower                                                        |
| deepcopy                | 354 us                                                | 359 us: 1.01x slower                                                        |
| crypto_pyaes            | 78.7 ms                                               | 79.7 ms: 1.01x slower                                                       |
| asyncio_tcp             | 511 ms                                                | 518 ms: 1.01x slower                                                        |
| pycparser               | 1.19 sec                                              | 1.20 sec: 1.01x slower                                                      |
| pickle_pure_python      | 312 us                                                | 317 us: 1.02x slower                                                        |
| comprehensions          | 20.5 us                                               | 20.8 us: 1.02x slower                                                       |
| pprint_safe_repr        | 733 ms                                                | 744 ms: 1.02x slower                                                        |
| richards_super          | 50.5 ms                                               | 51.4 ms: 1.02x slower                                                       |
| pickle_list             | 4.66 us                                               | 4.75 us: 1.02x slower                                                       |
| pickle_dict             | 31.6 us                                               | 32.1 us: 1.02x slower                                                       |
| go                      | 136 ms                                                | 138 ms: 1.02x slower                                                        |
| logging_format          | 7.05 us                                               | 7.20 us: 1.02x slower                                                       |
| hexiom                  | 6.21 ms                                               | 6.34 ms: 1.02x slower                                                       |
| tomli_loads             | 2.22 sec                                              | 2.27 sec: 1.02x slower                                                      |
| sqlglot_optimize        | 54.0 ms                                               | 55.3 ms: 1.02x slower                                                       |
| deepcopy_memo           | 38.0 us                                               | 39.0 us: 1.02x slower                                                       |
| pyflate                 | 442 ms                                                | 454 ms: 1.03x slower                                                        |
| sqlglot_parse           | 1.34 ms                                               | 1.38 ms: 1.03x slower                                                       |
| richards                | 44.5 ms                                               | 45.7 ms: 1.03x slower                                                       |
| pidigits                | 192 ms                                                | 197 ms: 1.03x slower                                                        |
| sqlglot_normalize       | 109 ms                                                | 112 ms: 1.03x slower                                                        |
| logging_simple          | 6.37 us                                               | 6.56 us: 1.03x slower                                                       |
| deepcopy_reduce         | 3.12 us                                               | 3.22 us: 1.03x slower                                                       |
| unpickle_pure_python    | 218 us                                                | 226 us: 1.03x slower                                                        |
| sqlglot_transpile       | 1.66 ms                                               | 1.71 ms: 1.03x slower                                                       |
| deltablue               | 3.49 ms                                               | 3.63 ms: 1.04x slower                                                       |
| scimark_monte_carlo     | 71.7 ms                                               | 74.5 ms: 1.04x slower                                                       |
| gc_traversal            | 3.91 ms                                               | 4.07 ms: 1.04x slower                                                       |
| logging_silent          | 103 ns                                                | 108 ns: 1.05x slower                                                        |
| scimark_sor             | 119 ms                                                | 126 ms: 1.05x slower                                                        |
| unpack_sequence         | 44.2 ns                                               | 49.0 ns: 1.11x slower                                                       |
| Geometric mean          | (ref)                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (15): async_generators, sqlite_synth, mdp, bench_mp_pool, async_tree_none, typing_runtime_protocols, async_tree_cpu_io_mixed, json, pathlib, pickle, spectral_norm, float, mypy2, xml_etree_parse, tornado_http
