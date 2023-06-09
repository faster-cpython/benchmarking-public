
# Results vs. base

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: 0463633
- commit date: 2023-06-09
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------|:-----------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.71 sec                                              | 2.76 sec: 1.02x slower                                         |
| tornado_http   | 102 ms                                                | 104 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                 | 1.02x slower                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------|:-----------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 81.4 ms                                               | 82.2 ms: 1.01x slower                                          |
| pidigits       | 192 ms                                                | 197 ms: 1.03x slower                                           |
| nbody          | 89.0 ms                                               | 94.2 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                 | 1.03x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------|:-----------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.56 ms                                               | 3.63 ms: 1.02x slower                                          |
| regex_compile  | 145 ms                                                | 148 ms: 1.03x slower                                           |
| regex_dna      | 205 ms                                                | 212 ms: 1.03x slower                                           |
| regex_v8       | 21.9 ms                                               | 22.7 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                 | 1.03x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------------|:-----------------------------------------------------:|:--------------------------------------------------------------:|
| json_loads           | 25.2 us                                               | 24.9 us: 1.01x faster                                          |
| pickle_list          | 4.66 us                                               | 4.63 us: 1.01x faster                                          |
| pickle               | 10.6 us                                               | 10.5 us: 1.01x faster                                          |
| xml_etree_process    | 59.0 ms                                               | 59.5 ms: 1.01x slower                                          |
| xml_etree_parse      | 153 ms                                                | 154 ms: 1.01x slower                                           |
| json_dumps           | 9.78 ms                                               | 9.86 ms: 1.01x slower                                          |
| xml_etree_generate   | 84.5 ms                                               | 85.5 ms: 1.01x slower                                          |
| xml_etree_iterparse  | 103 ms                                                | 105 ms: 1.01x slower                                           |
| pickle_pure_python   | 312 us                                                | 321 us: 1.03x slower                                           |
| unpickle_pure_python | 218 us                                                | 226 us: 1.04x slower                                           |
| tomli_loads          | 2.22 sec                                              | 2.31 sec: 1.04x slower                                         |
| Geometric mean       | (ref)                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (3): unpickle, pickle_dict, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|------------------------|:-----------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.77 ms                                               | 6.80 ms: 1.01x slower                                          |
| python_startup         | 9.30 ms                                               | 9.35 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                 | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|-----------|:-----------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.8 ms                                               | 10.6 ms: 1.02x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|-------------------------|:-----------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal            | 3.91 ms                                               | 3.82 ms: 1.02x faster                                          |
| asyncio_tcp             | 511 ms                                                | 500 ms: 1.02x faster                                           |
| mako                    | 10.8 ms                                               | 10.6 ms: 1.02x faster                                          |
| json_loads              | 25.2 us                                               | 24.9 us: 1.01x faster                                          |
| pickle_list             | 4.66 us                                               | 4.63 us: 1.01x faster                                          |
| pickle                  | 10.6 us                                               | 10.5 us: 1.01x faster                                          |
| crypto_pyaes            | 78.7 ms                                               | 78.4 ms: 1.00x faster                                          |
| create_gc_cycles        | 1.51 ms                                               | 1.51 ms: 1.00x faster                                          |
| async_tree_io           | 1.21 sec                                              | 1.21 sec: 1.00x slower                                         |
| bench_thread_pool       | 831 us                                                | 834 us: 1.00x slower                                           |
| spectral_norm           | 107 ms                                                | 107 ms: 1.00x slower                                           |
| python_startup_no_site  | 6.77 ms                                               | 6.80 ms: 1.01x slower                                          |
| python_startup          | 9.30 ms                                               | 9.35 ms: 1.01x slower                                          |
| asyncio_tcp_ssl         | 1.79 sec                                              | 1.80 sec: 1.01x slower                                         |
| async_tree_memoization  | 595 ms                                                | 599 ms: 1.01x slower                                           |
| xml_etree_process       | 59.0 ms                                               | 59.5 ms: 1.01x slower                                          |
| xml_etree_parse         | 153 ms                                                | 154 ms: 1.01x slower                                           |
| json_dumps              | 9.78 ms                                               | 9.86 ms: 1.01x slower                                          |
| float                   | 81.4 ms                                               | 82.2 ms: 1.01x slower                                          |
| xml_etree_generate      | 84.5 ms                                               | 85.5 ms: 1.01x slower                                          |
| json                    | 4.77 ms                                               | 4.83 ms: 1.01x slower                                          |
| coverage                | 96.3 ms                                               | 97.5 ms: 1.01x slower                                          |
| async_generators        | 450 ms                                                | 455 ms: 1.01x slower                                           |
| fannkuch                | 386 ms                                                | 392 ms: 1.01x slower                                           |
| deepcopy_memo           | 38.0 us                                               | 38.6 us: 1.01x slower                                          |
| telco                   | 6.82 ms                                               | 6.92 ms: 1.01x slower                                          |
| sqlite_synth            | 2.72 us                                               | 2.76 us: 1.01x slower                                          |
| xml_etree_iterparse     | 103 ms                                                | 105 ms: 1.01x slower                                           |
| scimark_sparse_mat_mult | 4.95 ms                                               | 5.02 ms: 1.02x slower                                          |
| mypy2                   | 345 ms                                                | 350 ms: 1.02x slower                                           |
| tornado_http            | 102 ms                                                | 104 ms: 1.02x slower                                           |
| dask                    | 538 ms                                                | 546 ms: 1.02x slower                                           |
| dulwich_log             | 67.7 ms                                               | 68.9 ms: 1.02x slower                                          |
| meteor_contest          | 105 ms                                                | 107 ms: 1.02x slower                                           |
| comprehensions          | 20.5 us                                               | 20.9 us: 1.02x slower                                          |
| regex_effbot            | 3.56 ms                                               | 3.63 ms: 1.02x slower                                          |
| scimark_fft             | 358 ms                                                | 364 ms: 1.02x slower                                           |
| docutils                | 2.71 sec                                              | 2.76 sec: 1.02x slower                                         |
| chaos                   | 64.5 ms                                               | 65.9 ms: 1.02x slower                                          |
| pprint_safe_repr        | 733 ms                                                | 748 ms: 1.02x slower                                           |
| sqlglot_optimize        | 54.0 ms                                               | 55.2 ms: 1.02x slower                                          |
| hexiom                  | 6.21 ms                                               | 6.35 ms: 1.02x slower                                          |
| deepcopy                | 354 us                                                | 363 us: 1.02x slower                                           |
| pprint_pformat          | 1.50 sec                                              | 1.53 sec: 1.02x slower                                         |
| regex_compile           | 145 ms                                                | 148 ms: 1.03x slower                                           |
| richards                | 44.5 ms                                               | 45.7 ms: 1.03x slower                                          |
| pickle_pure_python      | 312 us                                                | 321 us: 1.03x slower                                           |
| sqlglot_normalize       | 109 ms                                                | 112 ms: 1.03x slower                                           |
| nqueens                 | 81.6 ms                                               | 83.9 ms: 1.03x slower                                          |
| pidigits                | 192 ms                                                | 197 ms: 1.03x slower                                           |
| sqlglot_parse           | 1.34 ms                                               | 1.38 ms: 1.03x slower                                          |
| raytrace                | 297 ms                                                | 307 ms: 1.03x slower                                           |
| logging_format          | 7.05 us                                               | 7.28 us: 1.03x slower                                          |
| sqlglot_transpile       | 1.66 ms                                               | 1.71 ms: 1.03x slower                                          |
| logging_silent          | 103 ns                                                | 107 ns: 1.03x slower                                           |
| regex_dna               | 205 ms                                                | 212 ms: 1.03x slower                                           |
| scimark_lu              | 114 ms                                                | 118 ms: 1.04x slower                                           |
| unpickle_pure_python    | 218 us                                                | 226 us: 1.04x slower                                           |
| deepcopy_reduce         | 3.12 us                                               | 3.23 us: 1.04x slower                                          |
| go                      | 136 ms                                                | 141 ms: 1.04x slower                                           |
| logging_simple          | 6.37 us                                               | 6.61 us: 1.04x slower                                          |
| richards_super          | 50.5 ms                                               | 52.5 ms: 1.04x slower                                          |
| deltablue               | 3.49 ms                                               | 3.63 ms: 1.04x slower                                          |
| regex_v8                | 21.9 ms                                               | 22.7 ms: 1.04x slower                                          |
| tomli_loads             | 2.22 sec                                              | 2.31 sec: 1.04x slower                                         |
| mdp                     | 2.54 sec                                              | 2.67 sec: 1.05x slower                                         |
| pyflate                 | 442 ms                                                | 465 ms: 1.05x slower                                           |
| nbody                   | 89.0 ms                                               | 94.2 ms: 1.06x slower                                          |
| scimark_monte_carlo     | 71.7 ms                                               | 76.2 ms: 1.06x slower                                          |
| generators              | 30.5 ms                                               | 32.6 ms: 1.07x slower                                          |
| scimark_sor             | 119 ms                                                | 141 ms: 1.18x slower                                           |
| unpack_sequence         | 44.2 ns                                               | 53.6 ns: 1.21x slower                                          |
| Geometric mean          | (ref)                                                 | 1.02x slower                                                   |

Benchmark hidden because not significant (10): async_tree_none, coroutines, unpickle, async_tree_cpu_io_mixed, bench_mp_pool, pathlib, pickle_dict, pycparser, unpickle_list, typing_runtime_protocols
