
# Results vs. base

- fork: brandtbucher
- ref: binary_subscr_str_in
- machine: linux-x86_64
- commit hash: ccddc2b
- commit date: 2023-08-03
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.66 sec: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 201 ms: 1.00x faster                                                        |
| nbody          | 92.4 ms                                                               | 94.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 138 ms: 1.01x slower                                                        |
| regex_effbot   | 3.51 ms                                                               | 3.55 ms: 1.01x slower                                                       |
| regex_dna      | 211 ms                                                                | 216 ms: 1.02x slower                                                        |
| regex_v8       | 22.4 ms                                                               | 23.0 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                                              | 2.13 sec: 1.09x faster                                                      |
| pickle_list          | 4.57 us                                                               | 4.51 us: 1.01x faster                                                       |
| json_dumps           | 9.87 ms                                                               | 9.79 ms: 1.01x faster                                                       |
| pickle_dict          | 31.6 us                                                               | 31.5 us: 1.00x faster                                                       |
| pickle_pure_python   | 294 us                                                                | 295 us: 1.00x slower                                                        |
| xml_etree_process    | 57.7 ms                                                               | 58.3 ms: 1.01x slower                                                       |
| pickle               | 10.4 us                                                               | 10.5 us: 1.01x slower                                                       |
| json_loads           | 26.1 us                                                               | 26.4 us: 1.01x slower                                                       |
| unpickle_pure_python | 212 us                                                                | 215 us: 1.01x slower                                                        |
| xml_etree_generate   | 83.3 ms                                                               | 84.6 ms: 1.02x slower                                                       |
| unpickle_list        | 4.99 us                                                               | 5.11 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.87 ms: 1.01x slower                                                       |
| python_startup         | 9.33 ms                                                               | 9.40 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads             | 2.33 sec                                                              | 2.13 sec: 1.09x faster                                                      |
| mdp                     | 2.66 sec                                                              | 2.55 sec: 1.04x faster                                                      |
| scimark_sparse_mat_mult | 4.85 ms                                                               | 4.66 ms: 1.04x faster                                                       |
| scimark_fft             | 366 ms                                                                | 354 ms: 1.03x faster                                                        |
| deltablue               | 3.28 ms                                                               | 3.21 ms: 1.02x faster                                                       |
| unpack_sequence         | 48.0 ns                                                               | 46.9 ns: 1.02x faster                                                       |
| pickle_list             | 4.57 us                                                               | 4.51 us: 1.01x faster                                                       |
| scimark_lu              | 111 ms                                                                | 109 ms: 1.01x faster                                                        |
| mako                    | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                                       |
| telco                   | 7.84 ms                                                               | 7.77 ms: 1.01x faster                                                       |
| sqlglot_parse           | 1.29 ms                                                               | 1.28 ms: 1.01x faster                                                       |
| json_dumps              | 9.87 ms                                                               | 9.79 ms: 1.01x faster                                                       |
| pprint_pformat          | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                                      |
| pprint_safe_repr        | 724 ms                                                                | 719 ms: 1.01x faster                                                        |
| deepcopy_memo           | 38.5 us                                                               | 38.2 us: 1.01x faster                                                       |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                      |
| pickle_dict             | 31.6 us                                                               | 31.5 us: 1.00x faster                                                       |
| pidigits                | 201 ms                                                                | 201 ms: 1.00x faster                                                        |
| docutils                | 2.65 sec                                                              | 2.66 sec: 1.00x slower                                                      |
| pyflate                 | 450 ms                                                                | 452 ms: 1.00x slower                                                        |
| pickle_pure_python      | 294 us                                                                | 295 us: 1.00x slower                                                        |
| sqlglot_optimize        | 52.6 ms                                                               | 52.8 ms: 1.00x slower                                                       |
| regex_compile           | 137 ms                                                                | 138 ms: 1.01x slower                                                        |
| scimark_sor             | 121 ms                                                                | 122 ms: 1.01x slower                                                        |
| async_tree_io           | 1.19 sec                                                              | 1.19 sec: 1.01x slower                                                      |
| python_startup_no_site  | 6.83 ms                                                               | 6.87 ms: 1.01x slower                                                       |
| sqlglot_normalize       | 104 ms                                                                | 105 ms: 1.01x slower                                                        |
| python_startup          | 9.33 ms                                                               | 9.40 ms: 1.01x slower                                                       |
| richards_super          | 54.1 ms                                                               | 54.5 ms: 1.01x slower                                                       |
| comprehensions          | 20.3 us                                                               | 20.4 us: 1.01x slower                                                       |
| deepcopy_reduce         | 3.19 us                                                               | 3.22 us: 1.01x slower                                                       |
| async_tree_none         | 480 ms                                                                | 484 ms: 1.01x slower                                                        |
| sqlite_synth            | 2.74 us                                                               | 2.76 us: 1.01x slower                                                       |
| dulwich_log             | 65.9 ms                                                               | 66.4 ms: 1.01x slower                                                       |
| xml_etree_process       | 57.7 ms                                                               | 58.3 ms: 1.01x slower                                                       |
| coverage                | 92.9 ms                                                               | 93.9 ms: 1.01x slower                                                       |
| pickle                  | 10.4 us                                                               | 10.5 us: 1.01x slower                                                       |
| json_loads              | 26.1 us                                                               | 26.4 us: 1.01x slower                                                       |
| meteor_contest          | 105 ms                                                                | 106 ms: 1.01x slower                                                        |
| logging_format          | 6.48 us                                                               | 6.56 us: 1.01x slower                                                       |
| regex_effbot            | 3.51 ms                                                               | 3.55 ms: 1.01x slower                                                       |
| unpickle_pure_python    | 212 us                                                                | 215 us: 1.01x slower                                                        |
| xml_etree_generate      | 83.3 ms                                                               | 84.6 ms: 1.02x slower                                                       |
| nqueens                 | 79.5 ms                                                               | 80.7 ms: 1.02x slower                                                       |
| pycparser               | 1.15 sec                                                              | 1.17 sec: 1.02x slower                                                      |
| scimark_monte_carlo     | 68.1 ms                                                               | 69.3 ms: 1.02x slower                                                       |
| richards                | 47.5 ms                                                               | 48.3 ms: 1.02x slower                                                       |
| go                      | 137 ms                                                                | 139 ms: 1.02x slower                                                        |
| chaos                   | 59.2 ms                                                               | 60.3 ms: 1.02x slower                                                       |
| fannkuch                | 394 ms                                                                | 402 ms: 1.02x slower                                                        |
| nbody                   | 92.4 ms                                                               | 94.3 ms: 1.02x slower                                                       |
| create_gc_cycles        | 1.48 ms                                                               | 1.51 ms: 1.02x slower                                                       |
| regex_dna               | 211 ms                                                                | 216 ms: 1.02x slower                                                        |
| logging_silent          | 106 ns                                                                | 108 ns: 1.02x slower                                                        |
| unpickle_list           | 4.99 us                                                               | 5.11 us: 1.02x slower                                                       |
| crypto_pyaes            | 68.7 ms                                                               | 70.5 ms: 1.03x slower                                                       |
| regex_v8                | 22.4 ms                                                               | 23.0 ms: 1.03x slower                                                       |
| coroutines              | 21.7 ms                                                               | 22.4 ms: 1.03x slower                                                       |
| spectral_norm           | 106 ms                                                                | 110 ms: 1.04x slower                                                        |
| hexiom                  | 6.01 ms                                                               | 6.23 ms: 1.04x slower                                                       |
| generators              | 28.2 ms                                                               | 29.6 ms: 1.05x slower                                                       |
| gc_traversal            | 3.66 ms                                                               | 3.99 ms: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (20): sqlglot_transpile, float, typing_runtime_protocols, raytrace, deepcopy, unpickle, pathlib, bench_mp_pool, mypy2, bench_thread_pool, asyncio_tcp, xml_etree_iterparse, async_tree_cpu_io_mixed, tornado_http, async_generators, logging_simple, async_tree_memoization, xml_etree_parse, dask, json
