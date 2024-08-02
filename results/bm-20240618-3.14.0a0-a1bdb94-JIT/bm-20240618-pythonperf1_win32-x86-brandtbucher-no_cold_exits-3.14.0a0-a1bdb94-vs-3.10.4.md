# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-x86
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.07x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.92 sec: 1.02x faster                                                        |
| html5lib       | 52.1 ms                                                         | 48.9 ms: 1.06x faster                                                         |
| tornado_http   | 118 ms                                                          | 97.8 ms: 1.20x faster                                                         |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 488 ms: 1.89x faster                                                          |
| async_tree_io           | 940 ms                                                          | 555 ms: 1.69x faster                                                          |
| async_tree_none         | 394 ms                                                          | 238 ms: 1.65x faster                                                          |
| async_tree_memoization  | 467 ms                                                          | 289 ms: 1.62x faster                                                          |
| Geometric mean          | (ref)                                                           | 1.71x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.56x faster                                                          |
| float          | 69.6 ms                                                         | 43.0 ms: 1.62x faster                                                         |
| nbody          | 79.1 ms                                                         | 52.5 ms: 1.51x faster                                                         |
| Geometric mean | (ref)                                                           | 1.84x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.7 ms: 1.23x faster                                                         |
| regex_dna      | 131 ms                                                          | 132 ms: 1.01x slower                                                          |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                         |
| regex_effbot   | 1.66 ms                                                         | 2.07 ms: 1.25x slower                                                         |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.01 ms: 1.40x faster                                                         |
| pickle_pure_python   | 280 us                                                          | 210 us: 1.34x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 143 us: 1.33x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                        |
| xml_etree_parse      | 120 ms                                                          | 102 ms: 1.17x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.3 ms: 1.15x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 43.2 ms: 1.11x faster                                                         |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 58.3 ms: 1.06x faster                                                         |
| unpickle_list        | 2.98 us                                                         | 2.89 us: 1.03x faster                                                         |
| unpickle             | 9.82 us                                                         | 10.1 us: 1.03x slower                                                         |
| pickle               | 7.83 us                                                         | 8.35 us: 1.07x slower                                                         |
| pickle_list          | 3.22 us                                                         | 3.60 us: 1.12x slower                                                         |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.8 ms: 1.01x faster                                                         |
| python_startup_no_site | 18.1 ms                                                         | 18.6 ms: 1.03x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.50 ms: 1.66x faster                                                         |
| django_template | 36.0 ms                                                         | 32.9 ms: 1.10x faster                                                         |
| genshi_text     | 21.0 ms                                                         | 21.1 ms: 1.01x slower                                                         |
| genshi_xml      | 46.6 ms                                                         | 51.7 ms: 1.11x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 142 us: 2.78x faster                                                          |
| pidigits                 | 502 ms                                                          | 197 ms: 2.56x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 15.4 us: 1.91x faster                                                         |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 488 ms: 1.89x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 57.4 ns: 1.71x faster                                                         |
| async_tree_io            | 940 ms                                                          | 555 ms: 1.69x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.1 ms: 1.69x faster                                                         |
| mako                     | 9.10 ms                                                         | 5.50 ms: 1.66x faster                                                         |
| async_tree_none          | 394 ms                                                          | 238 ms: 1.65x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 49.3 ms: 1.63x faster                                                         |
| float                    | 69.6 ms                                                         | 43.0 ms: 1.62x faster                                                         |
| async_tree_memoization   | 467 ms                                                          | 289 ms: 1.62x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.59x faster                                                         |
| pylint                   | 384 ms                                                          | 243 ms: 1.58x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.7 ms: 1.56x faster                                                         |
| nbody                    | 79.1 ms                                                         | 52.5 ms: 1.51x faster                                                         |
| pyflate                  | 422 ms                                                          | 283 ms: 1.49x faster                                                          |
| fannkuch                 | 317 ms                                                          | 215 ms: 1.47x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.74 ms: 1.47x faster                                                         |
| sqlglot_parse            | 1.33 ms                                                         | 939 us: 1.42x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.01 ms: 1.40x faster                                                         |
| chaos                    | 74.4 ms                                                         | 53.1 ms: 1.40x faster                                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.40 ms: 1.35x faster                                                         |
| hexiom                   | 6.13 ms                                                         | 4.55 ms: 1.35x faster                                                         |
| pickle_pure_python       | 280 us                                                          | 210 us: 1.34x faster                                                          |
| raytrace                 | 303 ms                                                          | 227 ms: 1.34x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 143 us: 1.33x faster                                                          |
| deepcopy                 | 310 us                                                          | 234 us: 1.32x faster                                                          |
| richards_super           | 49.9 ms                                                         | 37.8 ms: 1.32x faster                                                         |
| sqlglot_transpile        | 1.58 ms                                                         | 1.20 ms: 1.32x faster                                                         |
| go                       | 146 ms                                                          | 111 ms: 1.32x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                        |
| scimark_fft              | 216 ms                                                          | 169 ms: 1.28x faster                                                          |
| pycparser                | 1.04 sec                                                        | 827 ms: 1.26x faster                                                          |
| richards                 | 40.3 ms                                                         | 32.6 ms: 1.23x faster                                                         |
| regex_compile            | 117 ms                                                          | 94.7 ms: 1.23x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 71.9 ms: 1.21x faster                                                         |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.21x faster                                                         |
| asyncio_tcp              | 744 ms                                                          | 617 ms: 1.21x faster                                                          |
| tornado_http             | 118 ms                                                          | 97.8 ms: 1.20x faster                                                         |
| scimark_lu               | 89.8 ms                                                         | 74.8 ms: 1.20x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.14 sec: 1.20x faster                                                        |
| scimark_sor              | 115 ms                                                          | 96.2 ms: 1.20x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 553 ms: 1.19x faster                                                          |
| thrift                   | 902 us                                                          | 764 us: 1.18x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 102 ms: 1.17x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.3 ms: 1.15x faster                                                         |
| json                     | 4.76 ms                                                         | 4.14 ms: 1.15x faster                                                         |
| bench_thread_pool        | 1.12 ms                                                         | 976 us: 1.15x faster                                                          |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                          |
| generators               | 31.6 ms                                                         | 27.9 ms: 1.13x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.39 us: 1.12x faster                                                         |
| xml_etree_process        | 48.1 ms                                                         | 43.2 ms: 1.11x faster                                                         |
| meteor_contest           | 80.0 ms                                                         | 72.6 ms: 1.10x faster                                                         |
| django_template          | 36.0 ms                                                         | 32.9 ms: 1.10x faster                                                         |
| mdp                      | 1.83 sec                                                        | 1.67 sec: 1.09x faster                                                        |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                         |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                                          |
| 2to3                     | 265 ms                                                          | 249 ms: 1.07x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.9 ms: 1.06x faster                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 58.3 ms: 1.06x faster                                                         |
| sympy_integrate          | 16.6 ms                                                         | 15.8 ms: 1.05x faster                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 43.2 ms: 1.03x faster                                                         |
| unpickle_list            | 2.98 us                                                         | 2.89 us: 1.03x faster                                                         |
| sympy_expand             | 391 ms                                                          | 381 ms: 1.03x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.92 sec: 1.02x faster                                                        |
| coroutines               | 17.9 ms                                                         | 17.7 ms: 1.01x faster                                                         |
| python_startup           | 22.9 ms                                                         | 22.8 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                        |
| genshi_text              | 21.0 ms                                                         | 21.1 ms: 1.01x slower                                                         |
| regex_dna                | 131 ms                                                          | 132 ms: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                         |
| pathlib                  | 81.2 ms                                                         | 82.8 ms: 1.02x slower                                                         |
| sqlglot_normalize        | 230 ms                                                          | 236 ms: 1.02x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 18.6 ms: 1.03x slower                                                         |
| unpickle                 | 9.82 us                                                         | 10.1 us: 1.03x slower                                                         |
| logging_simple           | 7.29 us                                                         | 7.56 us: 1.04x slower                                                         |
| logging_format           | 7.91 us                                                         | 8.21 us: 1.04x slower                                                         |
| pickle                   | 7.83 us                                                         | 8.35 us: 1.07x slower                                                         |
| coverage                 | 46.6 ms                                                         | 50.9 ms: 1.09x slower                                                         |
| create_gc_cycles         | 694 us                                                          | 759 us: 1.09x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.5 ms: 1.11x slower                                                         |
| genshi_xml               | 46.6 ms                                                         | 51.7 ms: 1.11x slower                                                         |
| pickle_list              | 3.22 us                                                         | 3.60 us: 1.12x slower                                                         |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                         |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                         |
| telco                    | 4.83 ms                                                         | 5.64 ms: 1.17x slower                                                         |
| regex_effbot             | 1.66 ms                                                         | 2.07 ms: 1.25x slower                                                         |
| async_generators         | 241 ms                                                          | 302 ms: 1.25x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                                  |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown