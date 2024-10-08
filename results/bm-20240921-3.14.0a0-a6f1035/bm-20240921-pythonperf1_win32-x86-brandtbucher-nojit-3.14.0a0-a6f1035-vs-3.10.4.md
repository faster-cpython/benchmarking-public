# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.11x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 253 ms: 1.05x faster                                                  |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                |
| html5lib       | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                 |
| tornado_http   | 118 ms                                                          | 95.1 ms: 1.24x faster                                                 |
| Geometric mean | (ref)                                                           | 1.11x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                  |
| async_tree_none         | 394 ms                                                          | 217 ms: 1.81x faster                                                  |
| async_tree_io           | 940 ms                                                          | 540 ms: 1.74x faster                                                  |
| async_tree_memoization  | 467 ms                                                          | 270 ms: 1.73x faster                                                  |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                  |
| float          | 69.6 ms                                                         | 63.2 ms: 1.10x faster                                                 |
| nbody          | 79.1 ms                                                         | 90.2 ms: 1.14x slower                                                 |
| Geometric mean | (ref)                                                           | 1.35x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                  |
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                  |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                 |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                           | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.57 ms: 1.30x faster                                                 |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                  |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.08x faster                                                 |
| pickle_pure_python   | 280 us                                                          | 260 us: 1.08x faster                                                  |
| unpickle_list        | 2.98 us                                                         | 2.85 us: 1.05x faster                                                 |
| unpickle_pure_python | 189 us                                                          | 182 us: 1.04x faster                                                  |
| tomli_loads          | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.9 ms: 1.03x faster                                                 |
| xml_etree_process    | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                 |
| pickle               | 7.83 us                                                         | 8.03 us: 1.03x slower                                                 |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                 |
| pickle_list          | 3.22 us                                                         | 3.42 us: 1.06x slower                                                 |
| xml_etree_generate   | 61.6 ms                                                         | 67.0 ms: 1.09x slower                                                 |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                 |
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 32.1 ms: 1.12x faster                                                 |
| mako            | 9.10 ms                                                         | 8.30 ms: 1.10x faster                                                 |
| genshi_xml      | 46.6 ms                                                         | 47.6 ms: 1.02x slower                                                 |
| genshi_text     | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 142 us: 2.79x faster                                                  |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                  |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                  |
| async_tree_none          | 394 ms                                                          | 217 ms: 1.81x faster                                                  |
| async_tree_io            | 940 ms                                                          | 540 ms: 1.74x faster                                                  |
| async_tree_memoization   | 467 ms                                                          | 270 ms: 1.73x faster                                                  |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                  |
| deltablue                | 4.04 ms                                                         | 2.82 ms: 1.43x faster                                                 |
| crypto_pyaes             | 81.3 ms                                                         | 57.9 ms: 1.40x faster                                                 |
| chaos                    | 74.4 ms                                                         | 54.6 ms: 1.36x faster                                                 |
| go                       | 146 ms                                                          | 109 ms: 1.34x faster                                                  |
| logging_silent           | 97.9 ns                                                         | 75.2 ns: 1.30x faster                                                 |
| json_dumps               | 9.82 ms                                                         | 7.57 ms: 1.30x faster                                                 |
| deepcopy_memo            | 29.6 us                                                         | 23.1 us: 1.28x faster                                                 |
| raytrace                 | 303 ms                                                          | 237 ms: 1.28x faster                                                  |
| scimark_lu               | 89.8 ms                                                         | 71.7 ms: 1.25x faster                                                 |
| deepcopy                 | 310 us                                                          | 249 us: 1.25x faster                                                  |
| tornado_http             | 118 ms                                                          | 95.1 ms: 1.24x faster                                                 |
| pycparser                | 1.04 sec                                                        | 854 ms: 1.22x faster                                                  |
| comprehensions           | 17.7 us                                                         | 14.6 us: 1.22x faster                                                 |
| sqlglot_parse            | 1.33 ms                                                         | 1.10 ms: 1.21x faster                                                 |
| thrift                   | 902 us                                                          | 766 us: 1.18x faster                                                  |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.17x faster                                                 |
| sqlglot_transpile        | 1.58 ms                                                         | 1.36 ms: 1.17x faster                                                 |
| generators               | 31.6 ms                                                         | 27.2 ms: 1.16x faster                                                 |
| pyflate                  | 422 ms                                                          | 364 ms: 1.16x faster                                                  |
| hexiom                   | 6.13 ms                                                         | 5.33 ms: 1.15x faster                                                 |
| dulwich_log              | 58.5 ms                                                         | 50.8 ms: 1.15x faster                                                 |
| json                     | 4.76 ms                                                         | 4.16 ms: 1.14x faster                                                 |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                  |
| django_template          | 36.0 ms                                                         | 32.1 ms: 1.12x faster                                                 |
| nqueens                  | 87.1 ms                                                         | 78.2 ms: 1.11x faster                                                 |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                  |
| deepcopy_reduce          | 2.68 us                                                         | 2.42 us: 1.11x faster                                                 |
| html5lib                 | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                 |
| float                    | 69.6 ms                                                         | 63.2 ms: 1.10x faster                                                 |
| scimark_sor              | 115 ms                                                          | 105 ms: 1.10x faster                                                  |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                 |
| mako                     | 9.10 ms                                                         | 8.30 ms: 1.10x faster                                                 |
| richards_super           | 49.9 ms                                                         | 45.6 ms: 1.09x faster                                                 |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                  |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.08x faster                                                 |
| pickle_pure_python       | 280 us                                                          | 260 us: 1.08x faster                                                  |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                  |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.08x faster                                                 |
| scimark_monte_carlo      | 61.9 ms                                                         | 58.6 ms: 1.06x faster                                                 |
| sympy_str                | 229 ms                                                          | 217 ms: 1.06x faster                                                  |
| 2to3                     | 265 ms                                                          | 253 ms: 1.05x faster                                                  |
| unpickle_list            | 2.98 us                                                         | 2.85 us: 1.05x faster                                                 |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                |
| unpickle_pure_python     | 189 us                                                          | 182 us: 1.04x faster                                                  |
| pprint_pformat           | 1.37 sec                                                        | 1.32 sec: 1.04x faster                                                |
| tomli_loads              | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                |
| pprint_safe_repr         | 658 ms                                                          | 636 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.13 ms: 1.04x faster                                                 |
| sqlglot_optimize         | 44.7 ms                                                         | 43.4 ms: 1.03x faster                                                 |
| mdp                      | 1.83 sec                                                        | 1.77 sec: 1.03x faster                                                |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.9 ms: 1.03x faster                                                 |
| sympy_expand             | 391 ms                                                          | 380 ms: 1.03x faster                                                  |
| sqlglot_normalize        | 230 ms                                                          | 230 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                |
| richards                 | 40.3 ms                                                         | 40.5 ms: 1.01x slower                                                 |
| xml_etree_process        | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                 |
| genshi_xml               | 46.6 ms                                                         | 47.6 ms: 1.02x slower                                                 |
| meteor_contest           | 80.0 ms                                                         | 81.8 ms: 1.02x slower                                                 |
| spectral_norm            | 80.2 ms                                                         | 82.1 ms: 1.02x slower                                                 |
| pickle                   | 7.83 us                                                         | 8.03 us: 1.03x slower                                                 |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                 |
| pathlib                  | 81.2 ms                                                         | 83.8 ms: 1.03x slower                                                 |
| python_startup           | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                 |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                 |
| coroutines               | 17.9 ms                                                         | 18.7 ms: 1.04x slower                                                 |
| create_gc_cycles         | 694 us                                                          | 735 us: 1.06x slower                                                  |
| genshi_text              | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                 |
| pickle_list              | 3.22 us                                                         | 3.42 us: 1.06x slower                                                 |
| fannkuch                 | 317 ms                                                          | 341 ms: 1.08x slower                                                  |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                 |
| xml_etree_generate       | 61.6 ms                                                         | 67.0 ms: 1.09x slower                                                 |
| bench_mp_pool            | 66.4 ms                                                         | 72.2 ms: 1.09x slower                                                 |
| scimark_fft              | 216 ms                                                          | 236 ms: 1.09x slower                                                  |
| gc_traversal             | 1.28 ms                                                         | 1.41 ms: 1.10x slower                                                 |
| logging_format           | 7.91 us                                                         | 8.76 us: 1.11x slower                                                 |
| logging_simple           | 7.29 us                                                         | 8.09 us: 1.11x slower                                                 |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                 |
| nbody                    | 79.1 ms                                                         | 90.2 ms: 1.14x slower                                                 |
| coverage                 | 46.6 ms                                                         | 53.2 ms: 1.14x slower                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                 |
| unpack_sequence          | 40.0 ns                                                         | 46.1 ns: 1.15x slower                                                 |
| async_generators         | 241 ms                                                          | 307 ms: 1.28x slower                                                  |
| telco                    | 4.83 ms                                                         | 6.54 ms: 1.35x slower                                                 |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                          |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown