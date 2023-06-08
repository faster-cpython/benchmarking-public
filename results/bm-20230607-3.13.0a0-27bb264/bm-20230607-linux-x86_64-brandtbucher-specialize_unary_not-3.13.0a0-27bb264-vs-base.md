
# Results vs. base

- fork: brandtbucher
- ref: specialize_unary_not
- machine: linux-x86_64
- commit hash: 27bb264
- commit date: 2023-06-07
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.71 sec                                              | 2.74 sec: 1.01x slower                                                      |
| tornado_http   | 102 ms                                                | 103 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                 | 1.01x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.4 ms                                               | 80.9 ms: 1.01x faster                                                       |
| nbody          | 89.0 ms                                               | 90.5 ms: 1.02x slower                                                       |
| pidigits       | 192 ms                                                | 196 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                 | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.9 ms                                               | 22.0 ms: 1.00x slower                                                       |
| regex_compile  | 145 ms                                                | 146 ms: 1.01x slower                                                        |
| regex_effbot   | 3.56 ms                                               | 3.61 ms: 1.01x slower                                                       |
| regex_dna      | 205 ms                                                | 208 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                 | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 31.6 us                                               | 30.4 us: 1.04x faster                                                       |
| pickle_list          | 4.66 us                                               | 4.51 us: 1.03x faster                                                       |
| unpickle_list        | 4.99 us                                               | 4.94 us: 1.01x faster                                                       |
| xml_etree_process    | 59.0 ms                                               | 59.3 ms: 1.01x slower                                                       |
| xml_etree_generate   | 84.5 ms                                               | 85.1 ms: 1.01x slower                                                       |
| xml_etree_parse      | 153 ms                                                | 154 ms: 1.01x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                | 104 ms: 1.01x slower                                                        |
| pickle_pure_python   | 312 us                                                | 315 us: 1.01x slower                                                        |
| json_dumps           | 9.78 ms                                               | 9.89 ms: 1.01x slower                                                       |
| pickle               | 10.6 us                                               | 10.8 us: 1.02x slower                                                       |
| tomli_loads          | 2.22 sec                                              | 2.27 sec: 1.02x slower                                                      |
| unpickle_pure_python | 218 us                                                | 224 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|------------------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.77 ms                                               | 6.82 ms: 1.01x slower                                                       |
| python_startup         | 9.30 ms                                               | 9.37 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|--------------------------|:-----------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict              | 31.6 us                                               | 30.4 us: 1.04x faster                                                       |
| scimark_sparse_mat_mult  | 4.95 ms                                               | 4.77 ms: 1.04x faster                                                       |
| pickle_list              | 4.66 us                                               | 4.51 us: 1.03x faster                                                       |
| logging_silent           | 103 ns                                                | 101 ns: 1.02x faster                                                        |
| pathlib                  | 18.5 ms                                               | 18.3 ms: 1.01x faster                                                       |
| unpickle_list            | 4.99 us                                               | 4.94 us: 1.01x faster                                                       |
| deepcopy_memo            | 38.0 us                                               | 37.8 us: 1.01x faster                                                       |
| float                    | 81.4 ms                                               | 80.9 ms: 1.01x faster                                                       |
| bench_thread_pool        | 831 us                                                | 835 us: 1.00x slower                                                        |
| regex_v8                 | 21.9 ms                                               | 22.0 ms: 1.00x slower                                                       |
| create_gc_cycles         | 1.51 ms                                               | 1.52 ms: 1.01x slower                                                       |
| xml_etree_process        | 59.0 ms                                               | 59.3 ms: 1.01x slower                                                       |
| xml_etree_generate       | 84.5 ms                                               | 85.1 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl          | 1.79 sec                                              | 1.80 sec: 1.01x slower                                                      |
| xml_etree_parse          | 153 ms                                                | 154 ms: 1.01x slower                                                        |
| async_tree_none          | 496 ms                                                | 500 ms: 1.01x slower                                                        |
| python_startup_no_site   | 6.77 ms                                               | 6.82 ms: 1.01x slower                                                       |
| python_startup           | 9.30 ms                                               | 9.37 ms: 1.01x slower                                                       |
| regex_compile            | 145 ms                                                | 146 ms: 1.01x slower                                                        |
| xml_etree_iterparse      | 103 ms                                                | 104 ms: 1.01x slower                                                        |
| sqlite_synth             | 2.72 us                                               | 2.74 us: 1.01x slower                                                       |
| mypy2                    | 345 ms                                                | 348 ms: 1.01x slower                                                        |
| richards_super           | 50.5 ms                                               | 51.0 ms: 1.01x slower                                                       |
| asyncio_tcp              | 511 ms                                                | 516 ms: 1.01x slower                                                        |
| pickle_pure_python       | 312 us                                                | 315 us: 1.01x slower                                                        |
| dulwich_log              | 67.7 ms                                               | 68.4 ms: 1.01x slower                                                       |
| richards                 | 44.5 ms                                               | 45.0 ms: 1.01x slower                                                       |
| json_dumps               | 9.78 ms                                               | 9.89 ms: 1.01x slower                                                       |
| deepcopy                 | 354 us                                                | 359 us: 1.01x slower                                                        |
| docutils                 | 2.71 sec                                              | 2.74 sec: 1.01x slower                                                      |
| regex_effbot             | 3.56 ms                                               | 3.61 ms: 1.01x slower                                                       |
| tornado_http             | 102 ms                                                | 103 ms: 1.01x slower                                                        |
| meteor_contest           | 105 ms                                                | 107 ms: 1.01x slower                                                        |
| regex_dna                | 205 ms                                                | 208 ms: 1.01x slower                                                        |
| pickle                   | 10.6 us                                               | 10.8 us: 1.02x slower                                                       |
| chaos                    | 64.5 ms                                               | 65.6 ms: 1.02x slower                                                       |
| crypto_pyaes             | 78.7 ms                                               | 79.9 ms: 1.02x slower                                                       |
| nbody                    | 89.0 ms                                               | 90.5 ms: 1.02x slower                                                       |
| sqlglot_parse            | 1.34 ms                                               | 1.36 ms: 1.02x slower                                                       |
| async_generators         | 450 ms                                                | 457 ms: 1.02x slower                                                        |
| dask                     | 538 ms                                                | 547 ms: 1.02x slower                                                        |
| typing_runtime_protocols | 143 us                                                | 146 us: 1.02x slower                                                        |
| mdp                      | 2.54 sec                                              | 2.59 sec: 1.02x slower                                                      |
| async_tree_memoization   | 595 ms                                                | 607 ms: 1.02x slower                                                        |
| sqlglot_optimize         | 54.0 ms                                               | 55.1 ms: 1.02x slower                                                       |
| pycparser                | 1.19 sec                                              | 1.21 sec: 1.02x slower                                                      |
| gc_traversal             | 3.91 ms                                               | 3.99 ms: 1.02x slower                                                       |
| pprint_pformat           | 1.50 sec                                              | 1.53 sec: 1.02x slower                                                      |
| async_tree_io            | 1.21 sec                                              | 1.24 sec: 1.02x slower                                                      |
| sqlglot_transpile        | 1.66 ms                                               | 1.70 ms: 1.02x slower                                                       |
| deepcopy_reduce          | 3.12 us                                               | 3.19 us: 1.02x slower                                                       |
| tomli_loads              | 2.22 sec                                              | 2.27 sec: 1.02x slower                                                      |
| unpickle_pure_python     | 218 us                                                | 224 us: 1.02x slower                                                        |
| pidigits                 | 192 ms                                                | 196 ms: 1.02x slower                                                        |
| scimark_monte_carlo      | 71.7 ms                                               | 73.5 ms: 1.02x slower                                                       |
| telco                    | 6.82 ms                                               | 7.00 ms: 1.03x slower                                                       |
| pprint_safe_repr         | 733 ms                                                | 752 ms: 1.03x slower                                                        |
| go                       | 136 ms                                                | 140 ms: 1.03x slower                                                        |
| hexiom                   | 6.21 ms                                               | 6.42 ms: 1.03x slower                                                       |
| comprehensions           | 20.5 us                                               | 21.2 us: 1.04x slower                                                       |
| sqlglot_normalize        | 109 ms                                                | 113 ms: 1.04x slower                                                        |
| fannkuch                 | 386 ms                                                | 400 ms: 1.04x slower                                                        |
| logging_simple           | 6.37 us                                               | 6.61 us: 1.04x slower                                                       |
| nqueens                  | 81.6 ms                                               | 84.9 ms: 1.04x slower                                                       |
| logging_format           | 7.05 us                                               | 7.36 us: 1.04x slower                                                       |
| generators               | 30.5 ms                                               | 31.9 ms: 1.04x slower                                                       |
| deltablue                | 3.49 ms                                               | 3.66 ms: 1.05x slower                                                       |
| pyflate                  | 442 ms                                                | 465 ms: 1.05x slower                                                        |
| scimark_sor              | 119 ms                                                | 137 ms: 1.15x slower                                                        |
| unpack_sequence          | 44.2 ns                                               | 54.8 ns: 1.24x slower                                                       |
| Geometric mean           | (ref)                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (12): json_loads, bench_mp_pool, scimark_fft, mako, scimark_lu, unpickle, coverage, coroutines, spectral_norm, json, raytrace, async_tree_cpu_io_mixed
