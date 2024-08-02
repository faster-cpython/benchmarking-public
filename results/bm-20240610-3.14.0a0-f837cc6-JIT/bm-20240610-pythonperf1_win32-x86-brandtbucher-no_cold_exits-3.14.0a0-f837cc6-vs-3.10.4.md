# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-x86
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 244 ms: 1.09x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                        |
| html5lib       | 52.1 ms                                                         | 45.9 ms: 1.13x faster                                                         |
| tornado_http   | 118 ms                                                          | 97.0 ms: 1.21x faster                                                         |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 479 ms: 1.92x faster                                                          |
| async_tree_io           | 940 ms                                                          | 527 ms: 1.78x faster                                                          |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.73x faster                                                          |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                          |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 195 ms: 2.58x faster                                                          |
| float          | 69.6 ms                                                         | 41.6 ms: 1.67x faster                                                         |
| nbody          | 79.1 ms                                                         | 52.6 ms: 1.51x faster                                                         |
| Geometric mean | (ref)                                                           | 1.87x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 96.3 ms: 1.21x faster                                                         |
| regex_dna      | 131 ms                                                          | 124 ms: 1.05x faster                                                          |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                         |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                         |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.66 ms: 1.48x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.41x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 201 us: 1.39x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                        |
| xml_etree_parse      | 120 ms                                                          | 99.5 ms: 1.21x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 40.2 ms: 1.20x faster                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.1 ms: 1.16x faster                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 54.5 ms: 1.13x faster                                                         |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                         |
| unpickle_list        | 2.98 us                                                         | 2.76 us: 1.08x faster                                                         |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.04x slower                                                         |
| pickle               | 7.83 us                                                         | 8.24 us: 1.05x slower                                                         |
| pickle_list          | 3.22 us                                                         | 3.58 us: 1.11x slower                                                         |
| pickle_dict          | 18.2 us                                                         | 20.9 us: 1.14x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.5 ms: 1.03x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.33 ms: 1.71x faster                                                         |
| django_template | 36.0 ms                                                         | 31.7 ms: 1.13x faster                                                         |
| genshi_xml      | 46.6 ms                                                         | 50.7 ms: 1.09x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 146 us: 2.72x faster                                                          |
| pidigits                 | 502 ms                                                          | 195 ms: 2.58x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 479 ms: 1.92x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 54.8 ns: 1.79x faster                                                         |
| async_tree_io            | 940 ms                                                          | 527 ms: 1.78x faster                                                          |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.73x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.33 ms: 1.71x faster                                                         |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.5 ms: 1.68x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 47.9 ms: 1.68x faster                                                         |
| float                    | 69.6 ms                                                         | 41.6 ms: 1.67x faster                                                         |
| pylint                   | 384 ms                                                          | 236 ms: 1.63x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.51 ms: 1.61x faster                                                         |
| comprehensions           | 17.7 us                                                         | 11.3 us: 1.57x faster                                                         |
| pyflate                  | 422 ms                                                          | 270 ms: 1.56x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.9 ms: 1.55x faster                                                         |
| nbody                    | 79.1 ms                                                         | 52.6 ms: 1.51x faster                                                         |
| fannkuch                 | 317 ms                                                          | 211 ms: 1.50x faster                                                          |
| richards_super           | 49.9 ms                                                         | 33.3 ms: 1.50x faster                                                         |
| sqlglot_parse            | 1.33 ms                                                         | 899 us: 1.48x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 20.0 us: 1.48x faster                                                         |
| json_dumps               | 9.82 ms                                                         | 6.66 ms: 1.48x faster                                                         |
| chaos                    | 74.4 ms                                                         | 51.3 ms: 1.45x faster                                                         |
| raytrace                 | 303 ms                                                          | 213 ms: 1.42x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.41x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 201 us: 1.39x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.34 ms: 1.38x faster                                                         |
| hexiom                   | 6.13 ms                                                         | 4.45 ms: 1.38x faster                                                         |
| richards                 | 40.3 ms                                                         | 29.2 ms: 1.38x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                        |
| sqlglot_transpile        | 1.58 ms                                                         | 1.16 ms: 1.37x faster                                                         |
| generators               | 31.6 ms                                                         | 23.5 ms: 1.34x faster                                                         |
| scimark_fft              | 216 ms                                                          | 163 ms: 1.33x faster                                                          |
| go                       | 146 ms                                                          | 111 ms: 1.32x faster                                                          |
| scimark_sor              | 115 ms                                                          | 87.6 ms: 1.31x faster                                                         |
| pycparser                | 1.04 sec                                                        | 795 ms: 1.31x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 67.4 ms: 1.29x faster                                                         |
| thrift                   | 902 us                                                          | 712 us: 1.27x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 71.1 ms: 1.26x faster                                                         |
| tornado_http             | 118 ms                                                          | 97.0 ms: 1.21x faster                                                         |
| regex_compile            | 117 ms                                                          | 96.3 ms: 1.21x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.13 sec: 1.21x faster                                                        |
| xml_etree_parse          | 120 ms                                                          | 99.5 ms: 1.21x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 550 ms: 1.20x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 40.2 ms: 1.20x faster                                                         |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                         |
| asyncio_tcp              | 744 ms                                                          | 626 ms: 1.19x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.1 ms: 1.16x faster                                                         |
| coroutines               | 17.9 ms                                                         | 15.6 ms: 1.15x faster                                                         |
| mdp                      | 1.83 sec                                                        | 1.59 sec: 1.15x faster                                                        |
| bench_thread_pool        | 1.12 ms                                                         | 976 us: 1.15x faster                                                          |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                          |
| django_template          | 36.0 ms                                                         | 31.7 ms: 1.13x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 45.9 ms: 1.13x faster                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 54.5 ms: 1.13x faster                                                         |
| json                     | 4.76 ms                                                         | 4.30 ms: 1.11x faster                                                         |
| meteor_contest           | 80.0 ms                                                         | 72.3 ms: 1.11x faster                                                         |
| 2to3                     | 265 ms                                                          | 244 ms: 1.09x faster                                                          |
| sympy_str                | 229 ms                                                          | 211 ms: 1.08x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                         |
| unpickle_list            | 2.98 us                                                         | 2.76 us: 1.08x faster                                                         |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.08x faster                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 41.7 ms: 1.07x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 219 ms: 1.05x faster                                                          |
| regex_dna                | 131 ms                                                          | 124 ms: 1.05x faster                                                          |
| sympy_expand             | 391 ms                                                          | 374 ms: 1.04x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                        |
| deepcopy                 | 310 us                                                          | 300 us: 1.03x faster                                                          |
| logging_simple           | 7.29 us                                                         | 7.21 us: 1.01x faster                                                         |
| logging_format           | 7.91 us                                                         | 7.82 us: 1.01x faster                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                        |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                         |
| pathlib                  | 81.2 ms                                                         | 82.7 ms: 1.02x slower                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.74 us: 1.02x slower                                                         |
| python_startup_no_site   | 18.1 ms                                                         | 18.5 ms: 1.03x slower                                                         |
| coverage                 | 46.6 ms                                                         | 48.6 ms: 1.04x slower                                                         |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.04x slower                                                         |
| pickle                   | 7.83 us                                                         | 8.24 us: 1.05x slower                                                         |
| telco                    | 4.83 ms                                                         | 5.23 ms: 1.08x slower                                                         |
| create_gc_cycles         | 694 us                                                          | 755 us: 1.09x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 50.7 ms: 1.09x slower                                                         |
| bench_mp_pool            | 66.4 ms                                                         | 73.0 ms: 1.10x slower                                                         |
| pickle_list              | 3.22 us                                                         | 3.58 us: 1.11x slower                                                         |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                         |
| pickle_dict              | 18.2 us                                                         | 20.9 us: 1.14x slower                                                         |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                         |
| async_generators         | 241 ms                                                          | 301 ms: 1.25x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.24x faster                                                                  |

Benchmark hidden because not significant (2): python_startup, genshi_text
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown