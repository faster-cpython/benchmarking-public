
# Results vs. base

- fork: brandtbucher
- ref: binary_subscr_str_in
- machine: linux-x86_64
- commit hash: f077383
- commit date: 2023-08-05
- overall geometric mean: 1.00x faster
- HPT reliability: 97.84%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.7 ms                                                               | 79.2 ms: 1.01x slower                                                       |
| nbody          | 88.9 ms                                                               | 92.3 ms: 1.04x slower                                                       |
| pidigits       | 189 ms                                                                | 201 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                               | 3.44 ms: 1.07x faster                                                       |
| regex_dna      | 215 ms                                                                | 207 ms: 1.03x faster                                                        |
| regex_v8       | 22.6 ms                                                               | 21.9 ms: 1.03x faster                                                       |
| regex_compile  | 137 ms                                                                | 136 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.31 sec                                                              | 2.08 sec: 1.11x faster                                                      |
| unpickle_list        | 5.17 us                                                               | 4.99 us: 1.04x faster                                                       |
| unpickle             | 15.1 us                                                               | 14.8 us: 1.02x faster                                                       |
| json_loads           | 25.6 us                                                               | 25.3 us: 1.01x faster                                                       |
| pickle_pure_python   | 294 us                                                                | 293 us: 1.00x faster                                                        |
| xml_etree_process    | 58.2 ms                                                               | 58.0 ms: 1.00x faster                                                       |
| xml_etree_generate   | 84.3 ms                                                               | 84.1 ms: 1.00x faster                                                       |
| pickle               | 10.4 us                                                               | 10.5 us: 1.01x slower                                                       |
| pickle_dict          | 31.8 us                                                               | 32.1 us: 1.01x slower                                                       |
| unpickle_pure_python | 212 us                                                                | 214 us: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_parse, json_dumps, pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.87 ms                                                               | 6.87 ms: 1.00x faster                                                       |
| python_startup         | 9.38 ms                                                               | 9.40 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads             | 2.31 sec                                                              | 2.08 sec: 1.11x faster                                                      |
| gc_traversal            | 3.98 ms                                                               | 3.67 ms: 1.08x faster                                                       |
| regex_effbot            | 3.67 ms                                                               | 3.44 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult | 4.73 ms                                                               | 4.51 ms: 1.05x faster                                                       |
| unpickle_list           | 5.17 us                                                               | 4.99 us: 1.04x faster                                                       |
| regex_dna               | 215 ms                                                                | 207 ms: 1.03x faster                                                        |
| regex_v8                | 22.6 ms                                                               | 21.9 ms: 1.03x faster                                                       |
| sqlglot_parse           | 1.28 ms                                                               | 1.26 ms: 1.02x faster                                                       |
| async_tree_none         | 488 ms                                                                | 478 ms: 1.02x faster                                                        |
| async_tree_io           | 1.20 sec                                                              | 1.17 sec: 1.02x faster                                                      |
| spectral_norm           | 106 ms                                                                | 104 ms: 1.02x faster                                                        |
| unpickle                | 15.1 us                                                               | 14.8 us: 1.02x faster                                                       |
| unpack_sequence         | 45.4 ns                                                               | 44.7 ns: 1.02x faster                                                       |
| async_tree_cpu_io_mixed | 724 ms                                                                | 715 ms: 1.01x faster                                                        |
| richards_super          | 54.5 ms                                                               | 53.8 ms: 1.01x faster                                                       |
| create_gc_cycles        | 1.51 ms                                                               | 1.49 ms: 1.01x faster                                                       |
| sqlglot_transpile       | 1.60 ms                                                               | 1.58 ms: 1.01x faster                                                       |
| async_tree_memoization  | 589 ms                                                                | 582 ms: 1.01x faster                                                        |
| richards                | 48.1 ms                                                               | 47.6 ms: 1.01x faster                                                       |
| json_loads              | 25.6 us                                                               | 25.3 us: 1.01x faster                                                       |
| scimark_lu              | 111 ms                                                                | 110 ms: 1.01x faster                                                        |
| coroutines              | 21.6 ms                                                               | 21.4 ms: 1.01x faster                                                       |
| raytrace                | 269 ms                                                                | 267 ms: 1.01x faster                                                        |
| pprint_pformat          | 1.46 sec                                                              | 1.45 sec: 1.01x faster                                                      |
| regex_compile           | 137 ms                                                                | 136 ms: 1.01x faster                                                        |
| docutils                | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                                      |
| pickle_pure_python      | 294 us                                                                | 293 us: 1.00x faster                                                        |
| xml_etree_process       | 58.2 ms                                                               | 58.0 ms: 1.00x faster                                                       |
| xml_etree_generate      | 84.3 ms                                                               | 84.1 ms: 1.00x faster                                                       |
| python_startup_no_site  | 6.87 ms                                                               | 6.87 ms: 1.00x faster                                                       |
| python_startup          | 9.38 ms                                                               | 9.40 ms: 1.00x slower                                                       |
| bench_thread_pool       | 822 us                                                                | 824 us: 1.00x slower                                                        |
| comprehensions          | 20.2 us                                                               | 20.3 us: 1.00x slower                                                       |
| sqlglot_optimize        | 52.4 ms                                                               | 52.7 ms: 1.00x slower                                                       |
| dulwich_log             | 65.4 ms                                                               | 65.9 ms: 1.01x slower                                                       |
| float                   | 78.7 ms                                                               | 79.2 ms: 1.01x slower                                                       |
| deepcopy_memo           | 37.5 us                                                               | 37.7 us: 1.01x slower                                                       |
| go                      | 138 ms                                                                | 139 ms: 1.01x slower                                                        |
| pickle                  | 10.4 us                                                               | 10.5 us: 1.01x slower                                                       |
| pickle_dict             | 31.8 us                                                               | 32.1 us: 1.01x slower                                                       |
| unpickle_pure_python    | 212 us                                                                | 214 us: 1.01x slower                                                        |
| pyflate                 | 438 ms                                                                | 443 ms: 1.01x slower                                                        |
| pathlib                 | 18.3 ms                                                               | 18.6 ms: 1.01x slower                                                       |
| coverage                | 92.7 ms                                                               | 94.2 ms: 1.02x slower                                                       |
| nqueens                 | 79.5 ms                                                               | 82.2 ms: 1.03x slower                                                       |
| nbody                   | 88.9 ms                                                               | 92.3 ms: 1.04x slower                                                       |
| mdp                     | 2.53 sec                                                              | 2.64 sec: 1.04x slower                                                      |
| pidigits                | 189 ms                                                                | 201 ms: 1.06x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (34): pycparser, meteor_contest, deepcopy_reduce, xml_etree_parse, fannkuch, json, pprint_safe_repr, scimark_fft, mypy2, tornado_http, json_dumps, sqlglot_normalize, logging_simple, sqlite_synth, mako, chaos, asyncio_tcp_ssl, pickle_list, deepcopy, bench_mp_pool, async_generators, typing_runtime_protocols, hexiom, asyncio_tcp, deltablue, xml_etree_iterparse, scimark_monte_carlo, telco, crypto_pyaes, logging_silent, scimark_sor, dask, generators, logging_format


# HPT report

- Reliability score: 97.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
