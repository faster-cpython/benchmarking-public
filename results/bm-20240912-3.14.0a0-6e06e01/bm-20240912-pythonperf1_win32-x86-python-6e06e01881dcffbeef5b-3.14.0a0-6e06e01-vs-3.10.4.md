# Results vs. 3.10.4

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-x86
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 48.1 ms: 1.08x faster                                                          |
| tornado_http   | 118 ms                                                          | 95.1 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 466 ms: 1.98x faster                                                           |
| async_tree_none         | 394 ms                                                          | 217 ms: 1.81x faster                                                           |
| async_tree_io           | 940 ms                                                          | 535 ms: 1.76x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 271 ms: 1.72x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| float          | 69.6 ms                                                         | 62.2 ms: 1.12x faster                                                          |
| nbody          | 79.1 ms                                                         | 91.3 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.69 ms: 1.28x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 257 us: 1.09x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.8 ms: 1.06x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 181 us: 1.05x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.96 us: 1.01x faster                                                          |
| pickle               | 7.83 us                                                         | 7.77 us: 1.01x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.93 sec: 1.01x slower                                                         |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 50.7 ms: 1.05x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.42 us: 1.06x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 68.3 ms: 1.11x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.3 us: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.8 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.99 ms: 1.14x faster                                                          |
| django_template | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 48.7 ms: 1.04x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 137 us: 2.88x faster                                                           |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 466 ms: 1.98x faster                                                           |
| async_tree_none          | 394 ms                                                          | 217 ms: 1.81x faster                                                           |
| async_tree_io            | 940 ms                                                          | 535 ms: 1.76x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 271 ms: 1.72x faster                                                           |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.68 ms: 1.51x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 57.3 ms: 1.42x faster                                                          |
| go                       | 146 ms                                                          | 103 ms: 1.41x faster                                                           |
| chaos                    | 74.4 ms                                                         | 53.4 ms: 1.39x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.9 us: 1.35x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 68.1 ms: 1.32x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 74.5 ns: 1.31x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.8 us: 1.29x faster                                                          |
| raytrace                 | 303 ms                                                          | 236 ms: 1.28x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.69 ms: 1.28x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.05 ms: 1.26x faster                                                          |
| deepcopy                 | 310 us                                                          | 250 us: 1.24x faster                                                           |
| tornado_http             | 118 ms                                                          | 95.1 ms: 1.24x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.30 ms: 1.22x faster                                                          |
| thrift                   | 902 us                                                          | 742 us: 1.22x faster                                                           |
| generators               | 31.6 ms                                                         | 26.2 ms: 1.21x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.10 ms: 1.20x faster                                                          |
| pyflate                  | 422 ms                                                          | 352 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                          |
| pycparser                | 1.04 sec                                                        | 884 ms: 1.18x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.9 ms: 1.17x faster                                                          |
| scimark_sor              | 115 ms                                                          | 98.3 ms: 1.17x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 74.9 ms: 1.16x faster                                                          |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.15x faster                                                           |
| richards_super           | 49.9 ms                                                         | 43.5 ms: 1.15x faster                                                          |
| mako                     | 9.10 ms                                                         | 7.99 ms: 1.14x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| float                    | 69.6 ms                                                         | 62.2 ms: 1.12x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.4 ms: 1.12x faster                                                          |
| json                     | 4.76 ms                                                         | 4.28 ms: 1.11x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 669 ms: 1.11x faster                                                           |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 257 us: 1.09x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 48.1 ms: 1.08x faster                                                          |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.07x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.07x faster                                                         |
| 2to3                     | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 75.2 ms: 1.07x faster                                                          |
| richards                 | 40.3 ms                                                         | 37.9 ms: 1.06x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.8 ms: 1.06x faster                                                          |
| sympy_str                | 229 ms                                                          | 216 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.07 ms: 1.05x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 181 us: 1.05x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 43.0 ms: 1.04x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 223 ms: 1.03x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.60 us: 1.03x faster                                                          |
| sympy_expand             | 391 ms                                                          | 383 ms: 1.02x faster                                                           |
| fannkuch                 | 317 ms                                                          | 314 ms: 1.01x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.96 us: 1.01x faster                                                          |
| pickle                   | 7.83 us                                                         | 7.77 us: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| pprint_safe_repr         | 658 ms                                                          | 665 ms: 1.01x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.93 sec: 1.01x slower                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.39 sec: 1.01x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 83.3 ms: 1.03x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 48.7 ms: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 50.7 ms: 1.05x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 733 us: 1.06x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.42 us: 1.06x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 71.5 ms: 1.08x slower                                                          |
| scimark_fft              | 216 ms                                                          | 233 ms: 1.08x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.8 ms: 1.09x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.00 us: 1.10x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.41 ms: 1.10x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.71 us: 1.10x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 68.3 ms: 1.11x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.3 us: 1.11x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.7 ms: 1.13x slower                                                          |
| nbody                    | 79.1 ms                                                         | 91.3 ms: 1.15x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 47.1 ns: 1.18x slower                                                          |
| async_generators         | 241 ms                                                          | 300 ms: 1.24x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.37 ms: 1.32x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (2): meteor_contest, coroutines
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown