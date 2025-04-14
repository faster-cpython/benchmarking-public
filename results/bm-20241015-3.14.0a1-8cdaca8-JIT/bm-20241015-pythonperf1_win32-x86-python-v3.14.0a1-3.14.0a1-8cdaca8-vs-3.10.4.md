# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.169x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 264 ms: 1.01x faster                                                |
| docutils       | 1.95 sec                                                        | 2.07 sec: 1.06x slower                                              |
| html5lib       | 52.1 ms                                                         | 47.2 ms: 1.10x faster                                               |
| tornado_http   | 118 ms                                                          | 109 ms: 1.08x faster                                                |
| Geometric mean | (ref)                                                           | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                |
| async_tree_io           | 940 ms                                                          | 523 ms: 1.80x faster                                                |
| async_tree_none         | 394 ms                                                          | 219 ms: 1.79x faster                                                |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                |
| float          | 69.6 ms                                                         | 47.0 ms: 1.48x faster                                               |
| nbody          | 79.1 ms                                                         | 63.2 ms: 1.25x faster                                               |
| Geometric mean | (ref)                                                           | 1.67x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 104 ms: 1.12x faster                                                |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                |
| regex_v8       | 15.8 ms                                                         | 15.4 ms: 1.02x faster                                               |
| regex_effbot   | 1.66 ms                                                         | 1.82 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                           | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.56 sec: 1.22x faster                                              |
| json_dumps           | 9.82 ms                                                         | 8.11 ms: 1.21x faster                                               |
| unpickle_pure_python | 189 us                                                          | 161 us: 1.17x faster                                                |
| pickle_pure_python   | 280 us                                                          | 246 us: 1.14x faster                                                |
| xml_etree_process    | 48.1 ms                                                         | 42.8 ms: 1.12x faster                                               |
| xml_etree_generate   | 61.6 ms                                                         | 55.7 ms: 1.11x faster                                               |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                |
| unpickle_list        | 2.98 us                                                         | 2.71 us: 1.10x faster                                               |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.3 ms: 1.10x faster                                               |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.07x faster                                               |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                               |
| pickle_list          | 3.22 us                                                         | 3.48 us: 1.08x slower                                               |
| pickle               | 7.83 us                                                         | 8.60 us: 1.10x slower                                               |
| pickle_dict          | 18.2 us                                                         | 21.5 us: 1.18x slower                                               |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                               |
| python_startup         | 22.9 ms                                                         | 27.1 ms: 1.18x slower                                               |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.70 ms: 1.60x faster                                               |
| django_template | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                               |
| genshi_text     | 21.0 ms                                                         | 24.2 ms: 1.15x slower                                               |
| genshi_xml      | 46.6 ms                                                         | 54.0 ms: 1.16x slower                                               |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.67x faster                                                |
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                |
| deepcopy_memo            | 29.6 us                                                         | 16.2 us: 1.83x faster                                               |
| async_tree_io            | 940 ms                                                          | 523 ms: 1.80x faster                                                |
| async_tree_none          | 394 ms                                                          | 219 ms: 1.79x faster                                                |
| logging_silent           | 97.9 ns                                                         | 56.0 ns: 1.75x faster                                               |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                |
| scimark_sor              | 115 ms                                                          | 70.1 ms: 1.64x faster                                               |
| mako                     | 9.10 ms                                                         | 5.70 ms: 1.60x faster                                               |
| crypto_pyaes             | 81.3 ms                                                         | 51.9 ms: 1.57x faster                                               |
| deltablue                | 4.04 ms                                                         | 2.64 ms: 1.53x faster                                               |
| go                       | 146 ms                                                          | 97.2 ms: 1.50x faster                                               |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.6 ms: 1.49x faster                                               |
| scimark_lu               | 89.8 ms                                                         | 60.6 ms: 1.48x faster                                               |
| float                    | 69.6 ms                                                         | 47.0 ms: 1.48x faster                                               |
| spectral_norm            | 80.2 ms                                                         | 57.2 ms: 1.40x faster                                               |
| comprehensions           | 17.7 us                                                         | 13.0 us: 1.36x faster                                               |
| pylint                   | 384 ms                                                          | 283 ms: 1.35x faster                                                |
| pyflate                  | 422 ms                                                          | 312 ms: 1.35x faster                                                |
| chaos                    | 74.4 ms                                                         | 55.8 ms: 1.33x faster                                               |
| deepcopy                 | 310 us                                                          | 238 us: 1.30x faster                                                |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.54 ms: 1.28x faster                                               |
| fannkuch                 | 317 ms                                                          | 249 ms: 1.27x faster                                                |
| sqlglot_parse            | 1.33 ms                                                         | 1.05 ms: 1.27x faster                                               |
| generators               | 31.6 ms                                                         | 25.1 ms: 1.26x faster                                               |
| nbody                    | 79.1 ms                                                         | 63.2 ms: 1.25x faster                                               |
| pycparser                | 1.04 sec                                                        | 834 ms: 1.25x faster                                                |
| pprint_pformat           | 1.37 sec                                                        | 1.12 sec: 1.22x faster                                              |
| tomli_loads              | 1.91 sec                                                        | 1.56 sec: 1.22x faster                                              |
| json_dumps               | 9.82 ms                                                         | 8.11 ms: 1.21x faster                                               |
| pprint_safe_repr         | 658 ms                                                          | 546 ms: 1.21x faster                                                |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                               |
| dulwich_log              | 58.5 ms                                                         | 49.3 ms: 1.19x faster                                               |
| unpickle_pure_python     | 189 us                                                          | 161 us: 1.17x faster                                                |
| thrift                   | 902 us                                                          | 770 us: 1.17x faster                                                |
| scimark_fft              | 216 ms                                                          | 187 ms: 1.16x faster                                                |
| sqlglot_transpile        | 1.58 ms                                                         | 1.37 ms: 1.16x faster                                               |
| nqueens                  | 87.1 ms                                                         | 76.2 ms: 1.14x faster                                               |
| pickle_pure_python       | 280 us                                                          | 246 us: 1.14x faster                                                |
| hexiom                   | 6.13 ms                                                         | 5.38 ms: 1.14x faster                                               |
| raytrace                 | 303 ms                                                          | 269 ms: 1.12x faster                                                |
| xml_etree_process        | 48.1 ms                                                         | 42.8 ms: 1.12x faster                                               |
| regex_compile            | 117 ms                                                          | 104 ms: 1.12x faster                                                |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                               |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                |
| xml_etree_generate       | 61.6 ms                                                         | 55.7 ms: 1.11x faster                                               |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                |
| unpickle_list            | 2.98 us                                                         | 2.71 us: 1.10x faster                                               |
| html5lib                 | 52.1 ms                                                         | 47.2 ms: 1.10x faster                                               |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.3 ms: 1.10x faster                                               |
| deepcopy_reduce          | 2.68 us                                                         | 2.44 us: 1.10x faster                                               |
| richards_super           | 49.9 ms                                                         | 45.6 ms: 1.09x faster                                               |
| meteor_contest           | 80.0 ms                                                         | 73.3 ms: 1.09x faster                                               |
| tornado_http             | 118 ms                                                          | 109 ms: 1.08x faster                                                |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.07x faster                                               |
| django_template          | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                               |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.06x faster                                              |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.05x faster                                                |
| regex_v8                 | 15.8 ms                                                         | 15.4 ms: 1.02x faster                                               |
| coroutines               | 17.9 ms                                                         | 17.8 ms: 1.01x faster                                               |
| sympy_str                | 229 ms                                                          | 227 ms: 1.01x faster                                                |
| 2to3                     | 265 ms                                                          | 264 ms: 1.01x faster                                                |
| sympy_expand             | 391 ms                                                          | 394 ms: 1.01x slower                                                |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.5 sec: 1.03x slower                                              |
| logging_simple           | 7.29 us                                                         | 7.54 us: 1.03x slower                                               |
| unpack_sequence          | 40.0 ns                                                         | 41.7 ns: 1.04x slower                                               |
| logging_format           | 7.91 us                                                         | 8.27 us: 1.05x slower                                               |
| sympy_integrate          | 16.6 ms                                                         | 17.5 ms: 1.05x slower                                               |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                               |
| sqlglot_normalize        | 230 ms                                                          | 244 ms: 1.06x slower                                                |
| asyncio_tcp              | 744 ms                                                          | 789 ms: 1.06x slower                                                |
| docutils                 | 1.95 sec                                                        | 2.07 sec: 1.06x slower                                              |
| pickle_list              | 3.22 us                                                         | 3.48 us: 1.08x slower                                               |
| pathlib                  | 81.2 ms                                                         | 88.4 ms: 1.09x slower                                               |
| regex_effbot             | 1.66 ms                                                         | 1.82 ms: 1.09x slower                                               |
| pickle                   | 7.83 us                                                         | 8.60 us: 1.10x slower                                               |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                               |
| sqlglot_optimize         | 44.7 ms                                                         | 50.3 ms: 1.13x slower                                               |
| genshi_text              | 21.0 ms                                                         | 24.2 ms: 1.15x slower                                               |
| coverage                 | 46.6 ms                                                         | 53.8 ms: 1.16x slower                                               |
| genshi_xml               | 46.6 ms                                                         | 54.0 ms: 1.16x slower                                               |
| pickle_dict              | 18.2 us                                                         | 21.5 us: 1.18x slower                                               |
| python_startup           | 22.9 ms                                                         | 27.1 ms: 1.18x slower                                               |
| telco                    | 4.83 ms                                                         | 6.36 ms: 1.32x slower                                               |
| async_generators         | 241 ms                                                          | 325 ms: 1.35x slower                                                |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.42x slower                                               |
| bench_mp_pool            | 66.4 ms                                                         | 94.5 ms: 1.42x slower                                               |
| create_gc_cycles         | 694 us                                                          | 1.20 ms: 1.72x slower                                               |
| Geometric mean           | (ref)                                                           | 1.14x faster                                                        |

Benchmark hidden because not significant (2): richards, json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.169x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown