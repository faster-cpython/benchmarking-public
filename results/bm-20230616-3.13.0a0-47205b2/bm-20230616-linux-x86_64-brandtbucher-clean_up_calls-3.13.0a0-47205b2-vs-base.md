
# Results vs. base

- fork: brandtbucher
- ref: clean_up_calls
- machine: linux-x86_64
- commit hash: 47205b2
- commit date: 2023-06-16
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.66 sec: 1.00x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                               | 91.3 ms: 1.01x slower                                                 |
| float          | 79.9 ms                                                               | 81.2 ms: 1.02x slower                                                 |
| pidigits       | 192 ms                                                                | 197 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 22.3 ms                                                               | 22.1 ms: 1.01x faster                                                 |
| regex_compile  | 136 ms                                                                | 137 ms: 1.01x slower                                                  |
| regex_dna      | 204 ms                                                                | 207 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 32.2 us                                                               | 31.8 us: 1.01x faster                                                 |
| xml_etree_generate   | 83.6 ms                                                               | 84.3 ms: 1.01x slower                                                 |
| xml_etree_process    | 57.3 ms                                                               | 58.1 ms: 1.01x slower                                                 |
| tomli_loads          | 2.18 sec                                                              | 2.21 sec: 1.02x slower                                                |
| json_dumps           | 9.70 ms                                                               | 9.86 ms: 1.02x slower                                                 |
| unpickle_list        | 5.00 us                                                               | 5.09 us: 1.02x slower                                                 |
| pickle_pure_python   | 309 us                                                                | 316 us: 1.02x slower                                                  |
| unpickle_pure_python | 212 us                                                                | 218 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (6): xml_etree_parse, pickle_list, json_loads, xml_etree_iterparse, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 9.14 ms                                                               | 9.16 ms: 1.00x slower                                                 |
| python_startup_no_site | 6.63 ms                                                               | 6.65 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.7 ms                                                               | 10.8 ms: 1.02x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal             | 3.90 ms                                                               | 3.69 ms: 1.06x faster                                                 |
| typing_runtime_protocols | 147 us                                                                | 141 us: 1.05x faster                                                  |
| pickle_dict              | 32.2 us                                                               | 31.8 us: 1.01x faster                                                 |
| create_gc_cycles         | 1.51 ms                                                               | 1.49 ms: 1.01x faster                                                 |
| sqlglot_optimize         | 53.3 ms                                                               | 52.9 ms: 1.01x faster                                                 |
| regex_v8                 | 22.3 ms                                                               | 22.1 ms: 1.01x faster                                                 |
| logging_format           | 6.59 us                                                               | 6.56 us: 1.01x faster                                                 |
| async_tree_io            | 1.20 sec                                                              | 1.19 sec: 1.01x faster                                                |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                |
| python_startup           | 9.14 ms                                                               | 9.16 ms: 1.00x slower                                                 |
| python_startup_no_site   | 6.63 ms                                                               | 6.65 ms: 1.00x slower                                                 |
| docutils                 | 2.64 sec                                                              | 2.66 sec: 1.00x slower                                                |
| sqlglot_normalize        | 107 ms                                                                | 107 ms: 1.01x slower                                                  |
| nbody                    | 90.7 ms                                                               | 91.3 ms: 1.01x slower                                                 |
| async_tree_none          | 479 ms                                                                | 482 ms: 1.01x slower                                                  |
| comprehensions           | 20.2 us                                                               | 20.4 us: 1.01x slower                                                 |
| async_tree_memoization   | 586 ms                                                                | 590 ms: 1.01x slower                                                  |
| scimark_monte_carlo      | 70.8 ms                                                               | 71.4 ms: 1.01x slower                                                 |
| bench_thread_pool        | 816 us                                                                | 822 us: 1.01x slower                                                  |
| regex_compile            | 136 ms                                                                | 137 ms: 1.01x slower                                                  |
| xml_etree_generate       | 83.6 ms                                                               | 84.3 ms: 1.01x slower                                                 |
| mypy2                    | 335 ms                                                                | 339 ms: 1.01x slower                                                  |
| mdp                      | 2.54 sec                                                              | 2.57 sec: 1.01x slower                                                |
| hexiom                   | 5.97 ms                                                               | 6.04 ms: 1.01x slower                                                 |
| sqlglot_parse            | 1.30 ms                                                               | 1.32 ms: 1.01x slower                                                 |
| dulwich_log              | 64.7 ms                                                               | 65.5 ms: 1.01x slower                                                 |
| sqlglot_transpile        | 1.62 ms                                                               | 1.64 ms: 1.01x slower                                                 |
| meteor_contest           | 104 ms                                                                | 106 ms: 1.01x slower                                                  |
| xml_etree_process        | 57.3 ms                                                               | 58.1 ms: 1.01x slower                                                 |
| json                     | 4.73 ms                                                               | 4.79 ms: 1.01x slower                                                 |
| nqueens                  | 78.2 ms                                                               | 79.4 ms: 1.01x slower                                                 |
| deepcopy_memo            | 37.7 us                                                               | 38.3 us: 1.01x slower                                                 |
| tomli_loads              | 2.18 sec                                                              | 2.21 sec: 1.02x slower                                                |
| mako                     | 10.7 ms                                                               | 10.8 ms: 1.02x slower                                                 |
| pyflate                  | 440 ms                                                                | 447 ms: 1.02x slower                                                  |
| regex_dna                | 204 ms                                                                | 207 ms: 1.02x slower                                                  |
| deltablue                | 3.24 ms                                                               | 3.29 ms: 1.02x slower                                                 |
| float                    | 79.9 ms                                                               | 81.2 ms: 1.02x slower                                                 |
| logging_simple           | 5.96 us                                                               | 6.06 us: 1.02x slower                                                 |
| crypto_pyaes             | 76.3 ms                                                               | 77.6 ms: 1.02x slower                                                 |
| json_dumps               | 9.70 ms                                                               | 9.86 ms: 1.02x slower                                                 |
| unpickle_list            | 5.00 us                                                               | 5.09 us: 1.02x slower                                                 |
| pickle_pure_python       | 309 us                                                                | 316 us: 1.02x slower                                                  |
| dask                     | 515 ms                                                                | 526 ms: 1.02x slower                                                  |
| go                       | 134 ms                                                                | 137 ms: 1.02x slower                                                  |
| chaos                    | 60.7 ms                                                               | 62.0 ms: 1.02x slower                                                 |
| logging_silent           | 98.7 ns                                                               | 101 ns: 1.02x slower                                                  |
| telco                    | 6.72 ms                                                               | 6.87 ms: 1.02x slower                                                 |
| coverage                 | 93.3 ms                                                               | 95.5 ms: 1.02x slower                                                 |
| raytrace                 | 290 ms                                                                | 297 ms: 1.02x slower                                                  |
| richards                 | 43.9 ms                                                               | 45.0 ms: 1.03x slower                                                 |
| pprint_safe_repr         | 711 ms                                                                | 730 ms: 1.03x slower                                                  |
| pidigits                 | 192 ms                                                                | 197 ms: 1.03x slower                                                  |
| fannkuch                 | 382 ms                                                                | 393 ms: 1.03x slower                                                  |
| unpickle_pure_python     | 212 us                                                                | 218 us: 1.03x slower                                                  |
| richards_super           | 50.2 ms                                                               | 51.8 ms: 1.03x slower                                                 |
| scimark_fft              | 348 ms                                                                | 360 ms: 1.03x slower                                                  |
| pprint_pformat           | 1.44 sec                                                              | 1.48 sec: 1.03x slower                                                |
| scimark_lu               | 108 ms                                                                | 112 ms: 1.04x slower                                                  |
| scimark_sor              | 117 ms                                                                | 121 ms: 1.04x slower                                                  |
| deepcopy_reduce          | 3.13 us                                                               | 3.25 us: 1.04x slower                                                 |
| deepcopy                 | 348 us                                                                | 363 us: 1.04x slower                                                  |
| unpack_sequence          | 45.7 ns                                                               | 47.7 ns: 1.04x slower                                                 |
| scimark_sparse_mat_mult  | 4.58 ms                                                               | 5.01 ms: 1.09x slower                                                 |
| coroutines               | 21.8 ms                                                               | 24.0 ms: 1.10x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (17): xml_etree_parse, regex_effbot, pycparser, pickle_list, async_tree_cpu_io_mixed, json_loads, asyncio_tcp, spectral_norm, generators, sqlite_synth, xml_etree_iterparse, bench_mp_pool, tornado_http, pickle, pathlib, async_generators, unpickle
