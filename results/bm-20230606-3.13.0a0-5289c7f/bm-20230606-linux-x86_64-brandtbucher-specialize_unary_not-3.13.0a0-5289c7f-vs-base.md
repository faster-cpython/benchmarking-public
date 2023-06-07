
# Results vs. base

- fork: brandtbucher
- ref: specialize_unary_not
- machine: linux-x86_64
- commit hash: 5289c7f
- commit date: 2023-06-06
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.71 sec                                              | 2.75 sec: 1.02x slower                                                      |
| tornado_http   | 102 ms                                                | 103 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                 | 1.02x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 192 ms                                                | 192 ms: 1.00x slower                                                        |
| float          | 81.4 ms                                               | 83.0 ms: 1.02x slower                                                       |
| nbody          | 89.0 ms                                               | 92.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                 | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 145 ms                                                | 146 ms: 1.01x slower                                                        |
| regex_dna      | 205 ms                                                | 208 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_list          | 4.66 us                                               | 4.45 us: 1.05x faster                                                       |
| pickle_dict          | 31.6 us                                               | 30.8 us: 1.02x faster                                                       |
| pickle               | 10.6 us                                               | 10.5 us: 1.01x faster                                                       |
| unpickle_list        | 4.99 us                                               | 4.97 us: 1.00x faster                                                       |
| xml_etree_generate   | 84.5 ms                                               | 85.3 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                | 105 ms: 1.02x slower                                                        |
| json_dumps           | 9.78 ms                                               | 9.96 ms: 1.02x slower                                                       |
| tomli_loads          | 2.22 sec                                              | 2.26 sec: 1.02x slower                                                      |
| pickle_pure_python   | 312 us                                                | 320 us: 1.03x slower                                                        |
| unpickle_pure_python | 218 us                                                | 224 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|------------------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 9.30 ms                                               | 9.36 ms: 1.01x slower                                                       |
| python_startup_no_site | 6.77 ms                                               | 6.81 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|-----------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.8 ms                                               | 10.8 ms: 1.00x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|--------------------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_list              | 4.66 us                                               | 4.45 us: 1.05x faster                                                       |
| pickle_dict              | 31.6 us                                               | 30.8 us: 1.02x faster                                                       |
| coroutines               | 23.7 ms                                               | 23.2 ms: 1.02x faster                                                       |
| pickle                   | 10.6 us                                               | 10.5 us: 1.01x faster                                                       |
| generators               | 30.5 ms                                               | 30.1 ms: 1.01x faster                                                       |
| create_gc_cycles         | 1.51 ms                                               | 1.50 ms: 1.01x faster                                                       |
| unpickle_list            | 4.99 us                                               | 4.97 us: 1.00x faster                                                       |
| spectral_norm            | 107 ms                                                | 106 ms: 1.00x faster                                                        |
| pidigits                 | 192 ms                                                | 192 ms: 1.00x slower                                                        |
| mako                     | 10.8 ms                                               | 10.8 ms: 1.00x slower                                                       |
| regex_compile            | 145 ms                                                | 146 ms: 1.01x slower                                                        |
| python_startup           | 9.30 ms                                               | 9.36 ms: 1.01x slower                                                       |
| python_startup_no_site   | 6.77 ms                                               | 6.81 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl          | 1.79 sec                                              | 1.80 sec: 1.01x slower                                                      |
| logging_silent           | 103 ns                                                | 104 ns: 1.01x slower                                                        |
| asyncio_tcp              | 511 ms                                                | 516 ms: 1.01x slower                                                        |
| xml_etree_generate       | 84.5 ms                                               | 85.3 ms: 1.01x slower                                                       |
| crypto_pyaes             | 78.7 ms                                               | 79.4 ms: 1.01x slower                                                       |
| async_tree_none          | 496 ms                                                | 501 ms: 1.01x slower                                                        |
| deepcopy_memo            | 38.0 us                                               | 38.4 us: 1.01x slower                                                       |
| typing_runtime_protocols | 143 us                                                | 145 us: 1.01x slower                                                        |
| meteor_contest           | 105 ms                                                | 107 ms: 1.01x slower                                                        |
| pathlib                  | 18.5 ms                                               | 18.8 ms: 1.01x slower                                                       |
| sqlite_synth             | 2.72 us                                               | 2.76 us: 1.01x slower                                                       |
| tornado_http             | 102 ms                                                | 103 ms: 1.01x slower                                                        |
| regex_dna                | 205 ms                                                | 208 ms: 1.01x slower                                                        |
| mypy2                    | 345 ms                                                | 349 ms: 1.01x slower                                                        |
| dulwich_log              | 67.7 ms                                               | 68.6 ms: 1.01x slower                                                       |
| scimark_lu               | 114 ms                                                | 115 ms: 1.01x slower                                                        |
| richards_super           | 50.5 ms                                               | 51.2 ms: 1.01x slower                                                       |
| scimark_fft              | 358 ms                                                | 363 ms: 1.01x slower                                                        |
| xml_etree_iterparse      | 103 ms                                                | 105 ms: 1.02x slower                                                        |
| docutils                 | 2.71 sec                                              | 2.75 sec: 1.02x slower                                                      |
| dask                     | 538 ms                                                | 547 ms: 1.02x slower                                                        |
| nqueens                  | 81.6 ms                                               | 83.0 ms: 1.02x slower                                                       |
| fannkuch                 | 386 ms                                                | 394 ms: 1.02x slower                                                        |
| json_dumps               | 9.78 ms                                               | 9.96 ms: 1.02x slower                                                       |
| richards                 | 44.5 ms                                               | 45.3 ms: 1.02x slower                                                       |
| comprehensions           | 20.5 us                                               | 20.9 us: 1.02x slower                                                       |
| float                    | 81.4 ms                                               | 83.0 ms: 1.02x slower                                                       |
| async_generators         | 450 ms                                                | 459 ms: 1.02x slower                                                        |
| tomli_loads              | 2.22 sec                                              | 2.26 sec: 1.02x slower                                                      |
| async_tree_memoization   | 595 ms                                                | 609 ms: 1.02x slower                                                        |
| hexiom                   | 6.21 ms                                               | 6.36 ms: 1.02x slower                                                       |
| chaos                    | 64.5 ms                                               | 66.1 ms: 1.02x slower                                                       |
| async_tree_io            | 1.21 sec                                              | 1.24 sec: 1.02x slower                                                      |
| pickle_pure_python       | 312 us                                                | 320 us: 1.03x slower                                                        |
| pycparser                | 1.19 sec                                              | 1.22 sec: 1.03x slower                                                      |
| unpickle_pure_python     | 218 us                                                | 224 us: 1.03x slower                                                        |
| sqlglot_parse            | 1.34 ms                                               | 1.38 ms: 1.03x slower                                                       |
| raytrace                 | 297 ms                                                | 305 ms: 1.03x slower                                                        |
| sqlglot_optimize         | 54.0 ms                                               | 55.5 ms: 1.03x slower                                                       |
| sqlglot_transpile        | 1.66 ms                                               | 1.71 ms: 1.03x slower                                                       |
| go                       | 136 ms                                                | 140 ms: 1.03x slower                                                        |
| logging_format           | 7.05 us                                               | 7.27 us: 1.03x slower                                                       |
| mdp                      | 2.54 sec                                              | 2.63 sec: 1.03x slower                                                      |
| deepcopy                 | 354 us                                                | 366 us: 1.03x slower                                                        |
| deltablue                | 3.49 ms                                               | 3.61 ms: 1.03x slower                                                       |
| pprint_pformat           | 1.50 sec                                              | 1.55 sec: 1.04x slower                                                      |
| nbody                    | 89.0 ms                                               | 92.2 ms: 1.04x slower                                                       |
| logging_simple           | 6.37 us                                               | 6.60 us: 1.04x slower                                                       |
| pprint_safe_repr         | 733 ms                                                | 762 ms: 1.04x slower                                                        |
| deepcopy_reduce          | 3.12 us                                               | 3.24 us: 1.04x slower                                                       |
| gc_traversal             | 3.91 ms                                               | 4.07 ms: 1.04x slower                                                       |
| sqlglot_normalize        | 109 ms                                                | 114 ms: 1.04x slower                                                        |
| scimark_monte_carlo      | 71.7 ms                                               | 74.9 ms: 1.04x slower                                                       |
| pyflate                  | 442 ms                                                | 463 ms: 1.05x slower                                                        |
| scimark_sor              | 119 ms                                                | 139 ms: 1.16x slower                                                        |
| unpack_sequence          | 44.2 ns                                               | 52.8 ns: 1.19x slower                                                       |
| Geometric mean           | (ref)                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (13): telco, scimark_sparse_mat_mult, regex_effbot, unpickle, bench_mp_pool, xml_etree_parse, bench_thread_pool, regex_v8, json_loads, xml_etree_process, coverage, json, async_tree_cpu_io_mixed
