# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: windows-x86
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 232 ms: 1.14x faster                                                |
| chameleon      | 6.42 ms                                                         | 5.40 ms: 1.19x faster                                               |
| docutils       | 1.95 sec                                                        | 1.72 sec: 1.14x faster                                              |
| html5lib       | 52.1 ms                                                         | 44.0 ms: 1.18x faster                                               |
| tornado_http   | 118 ms                                                          | 96.3 ms: 1.22x faster                                               |
| Geometric mean | (ref)                                                           | 1.17x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 499 ms: 1.85x faster                                                |
| async_tree_none         | 394 ms                                                          | 241 ms: 1.63x faster                                                |
| async_tree_io           | 940 ms                                                          | 588 ms: 1.60x faster                                                |
| async_tree_memoization  | 467 ms                                                          | 303 ms: 1.54x faster                                                |
| Geometric mean          | (ref)                                                           | 1.65x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                |
| float          | 69.6 ms                                                         | 51.1 ms: 1.36x faster                                               |
| nbody          | 79.1 ms                                                         | 74.0 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                           | 1.54x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 92.5 ms: 1.26x faster                                               |
| regex_dna      | 131 ms                                                          | 125 ms: 1.05x faster                                                |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                               |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                               |
| Geometric mean | (ref)                                                           | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.75 ms: 1.46x faster                                               |
| pickle_pure_python   | 280 us                                                          | 204 us: 1.38x faster                                                |
| unpickle_pure_python | 189 us                                                          | 140 us: 1.35x faster                                                |
| tomli_loads          | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                              |
| xml_etree_process    | 48.1 ms                                                         | 41.1 ms: 1.17x faster                                               |
| json_loads           | 22.4 us                                                         | 19.8 us: 1.13x faster                                               |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.4 ms: 1.07x faster                                               |
| xml_etree_generate   | 61.6 ms                                                         | 58.8 ms: 1.05x faster                                               |
| pickle               | 7.83 us                                                         | 7.71 us: 1.02x faster                                               |
| unpickle             | 9.82 us                                                         | 9.71 us: 1.01x faster                                               |
| unpickle_list        | 2.98 us                                                         | 3.08 us: 1.03x slower                                               |
| pickle_list          | 3.22 us                                                         | 3.33 us: 1.04x slower                                               |
| pickle_dict          | 18.2 us                                                         | 20.0 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.7 ms: 1.01x faster                                               |
| python_startup_no_site | 18.1 ms                                                         | 20.5 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.84 ms: 1.33x faster                                               |
| django_template | 36.0 ms                                                         | 29.0 ms: 1.24x faster                                               |
| genshi_text     | 21.0 ms                                                         | 18.1 ms: 1.16x faster                                               |
| genshi_xml      | 46.6 ms                                                         | 41.6 ms: 1.12x faster                                               |
| Geometric mean  | (ref)                                                           | 1.21x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 87.7 us: 4.51x faster                                               |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                |
| deltablue                | 4.04 ms                                                         | 2.18 ms: 1.85x faster                                               |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 499 ms: 1.85x faster                                                |
| pylint                   | 384 ms                                                          | 217 ms: 1.77x faster                                                |
| logging_silent           | 97.9 ns                                                         | 57.1 ns: 1.71x faster                                               |
| chaos                    | 74.4 ms                                                         | 45.5 ms: 1.63x faster                                               |
| async_tree_none          | 394 ms                                                          | 241 ms: 1.63x faster                                                |
| async_tree_io            | 940 ms                                                          | 588 ms: 1.60x faster                                                |
| crypto_pyaes             | 81.3 ms                                                         | 51.0 ms: 1.59x faster                                               |
| richards_super           | 49.9 ms                                                         | 31.4 ms: 1.59x faster                                               |
| raytrace                 | 303 ms                                                          | 191 ms: 1.59x faster                                                |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.59x faster                                               |
| sqlglot_parse            | 1.33 ms                                                         | 848 us: 1.57x faster                                                |
| async_tree_memoization   | 467 ms                                                          | 303 ms: 1.54x faster                                                |
| go                       | 146 ms                                                          | 95.1 ms: 1.53x faster                                               |
| scimark_lu               | 89.8 ms                                                         | 60.2 ms: 1.49x faster                                               |
| hexiom                   | 6.13 ms                                                         | 4.14 ms: 1.48x faster                                               |
| sqlglot_transpile        | 1.58 ms                                                         | 1.08 ms: 1.47x faster                                               |
| json_dumps               | 9.82 ms                                                         | 6.75 ms: 1.46x faster                                               |
| scimark_sor              | 115 ms                                                          | 79.6 ms: 1.45x faster                                               |
| richards                 | 40.3 ms                                                         | 27.8 ms: 1.45x faster                                               |
| scimark_monte_carlo      | 61.9 ms                                                         | 44.3 ms: 1.40x faster                                               |
| pyflate                  | 422 ms                                                          | 306 ms: 1.38x faster                                                |
| generators               | 31.6 ms                                                         | 22.9 ms: 1.38x faster                                               |
| pickle_pure_python       | 280 us                                                          | 204 us: 1.38x faster                                                |
| deepcopy_memo            | 29.6 us                                                         | 21.6 us: 1.37x faster                                               |
| float                    | 69.6 ms                                                         | 51.1 ms: 1.36x faster                                               |
| unpickle_pure_python     | 189 us                                                          | 140 us: 1.35x faster                                                |
| mako                     | 9.10 ms                                                         | 6.84 ms: 1.33x faster                                               |
| pycparser                | 1.04 sec                                                        | 793 ms: 1.31x faster                                                |
| spectral_norm            | 80.2 ms                                                         | 63.0 ms: 1.27x faster                                               |
| sqlite_synth             | 2.29 us                                                         | 1.81 us: 1.27x faster                                               |
| coroutines               | 17.9 ms                                                         | 14.2 ms: 1.26x faster                                               |
| regex_compile            | 117 ms                                                          | 92.5 ms: 1.26x faster                                               |
| sympy_sum                | 122 ms                                                          | 98.5 ms: 1.24x faster                                               |
| django_template          | 36.0 ms                                                         | 29.0 ms: 1.24x faster                                               |
| pprint_pformat           | 1.37 sec                                                        | 1.12 sec: 1.23x faster                                              |
| tornado_http             | 118 ms                                                          | 96.3 ms: 1.22x faster                                               |
| deepcopy                 | 310 us                                                          | 255 us: 1.21x faster                                                |
| pprint_safe_repr         | 658 ms                                                          | 543 ms: 1.21x faster                                                |
| deepcopy_reduce          | 2.68 us                                                         | 2.22 us: 1.21x faster                                               |
| nqueens                  | 87.1 ms                                                         | 72.6 ms: 1.20x faster                                               |
| mdp                      | 1.83 sec                                                        | 1.53 sec: 1.19x faster                                              |
| sympy_integrate          | 16.6 ms                                                         | 14.0 ms: 1.19x faster                                               |
| chameleon                | 6.42 ms                                                         | 5.40 ms: 1.19x faster                                               |
| fannkuch                 | 317 ms                                                          | 267 ms: 1.19x faster                                                |
| html5lib                 | 52.1 ms                                                         | 44.0 ms: 1.18x faster                                               |
| tomli_loads              | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                              |
| sympy_str                | 229 ms                                                          | 194 ms: 1.18x faster                                                |
| xml_etree_process        | 48.1 ms                                                         | 41.1 ms: 1.17x faster                                               |
| sqlglot_optimize         | 44.7 ms                                                         | 38.2 ms: 1.17x faster                                               |
| sqlglot_normalize        | 230 ms                                                          | 197 ms: 1.17x faster                                                |
| asyncio_tcp              | 744 ms                                                          | 638 ms: 1.17x faster                                                |
| genshi_text              | 21.0 ms                                                         | 18.1 ms: 1.16x faster                                               |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.79 ms: 1.16x faster                                               |
| json                     | 4.76 ms                                                         | 4.12 ms: 1.16x faster                                               |
| 2to3                     | 265 ms                                                          | 232 ms: 1.14x faster                                                |
| sympy_expand             | 391 ms                                                          | 343 ms: 1.14x faster                                                |
| docutils                 | 1.95 sec                                                        | 1.72 sec: 1.14x faster                                              |
| json_loads               | 22.4 us                                                         | 19.8 us: 1.13x faster                                               |
| genshi_xml               | 46.6 ms                                                         | 41.6 ms: 1.12x faster                                               |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.10x faster                                               |
| scimark_fft              | 216 ms                                                          | 198 ms: 1.09x faster                                                |
| meteor_contest           | 80.0 ms                                                         | 73.7 ms: 1.09x faster                                               |
| nbody                    | 79.1 ms                                                         | 74.0 ms: 1.07x faster                                               |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.4 ms: 1.07x faster                                               |
| create_gc_cycles         | 694 us                                                          | 651 us: 1.07x faster                                                |
| xml_etree_generate       | 61.6 ms                                                         | 58.8 ms: 1.05x faster                                               |
| regex_dna                | 131 ms                                                          | 125 ms: 1.05x faster                                                |
| pickle                   | 7.83 us                                                         | 7.71 us: 1.02x faster                                               |
| python_startup           | 22.9 ms                                                         | 22.7 ms: 1.01x faster                                               |
| unpickle                 | 9.82 us                                                         | 9.71 us: 1.01x faster                                               |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                               |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.4 sec: 1.02x slower                                              |
| unpickle_list            | 2.98 us                                                         | 3.08 us: 1.03x slower                                               |
| pickle_list              | 3.22 us                                                         | 3.33 us: 1.04x slower                                               |
| logging_format           | 7.91 us                                                         | 8.33 us: 1.05x slower                                               |
| logging_simple           | 7.29 us                                                         | 7.69 us: 1.06x slower                                               |
| pathlib                  | 81.2 ms                                                         | 88.6 ms: 1.09x slower                                               |
| gc_traversal             | 1.28 ms                                                         | 1.40 ms: 1.09x slower                                               |
| pickle_dict              | 18.2 us                                                         | 20.0 us: 1.09x slower                                               |
| async_generators         | 241 ms                                                          | 271 ms: 1.12x slower                                                |
| bench_mp_pool            | 66.4 ms                                                         | 74.9 ms: 1.13x slower                                               |
| python_startup_no_site   | 18.1 ms                                                         | 20.5 ms: 1.13x slower                                               |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                               |
| telco                    | 4.83 ms                                                         | 5.62 ms: 1.16x slower                                               |
| coverage                 | 46.6 ms                                                         | 479 ms: 10.28x slower                                               |
| thrift                   | 902 us                                                          | 10.3 ms: 11.37x slower                                              |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                        |

Benchmark hidden because not significant (1): flaskblogging
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown