# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc1
- machine: windows-x86
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.139x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 244 ms: 1.09x faster                                                  |
| chameleon      | 6.42 ms                                                         | 5.80 ms: 1.11x faster                                                 |
| docutils       | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                |
| html5lib       | 52.1 ms                                                         | 47.2 ms: 1.10x faster                                                 |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                           | 1.09x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 485 ms: 1.90x faster                                                  |
| async_tree_io           | 940 ms                                                          | 550 ms: 1.71x faster                                                  |
| async_tree_none         | 394 ms                                                          | 237 ms: 1.66x faster                                                  |
| async_tree_memoization  | 467 ms                                                          | 290 ms: 1.61x faster                                                  |
| Geometric mean          | (ref)                                                           | 1.72x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                  |
| float          | 69.6 ms                                                         | 54.2 ms: 1.28x faster                                                 |
| nbody          | 79.1 ms                                                         | 77.1 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                           | 1.50x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 99.2 ms: 1.18x faster                                                 |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                  |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                 |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                 |
| Geometric mean | (ref)                                                           | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.61 ms: 1.29x faster                                                 |
| unpickle_pure_python | 189 us                                                          | 148 us: 1.28x faster                                                  |
| pickle_pure_python   | 280 us                                                          | 226 us: 1.24x faster                                                  |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                  |
| tomli_loads          | 1.91 sec                                                        | 1.68 sec: 1.13x faster                                                |
| xml_etree_process    | 48.1 ms                                                         | 42.8 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.7 ms: 1.08x faster                                                 |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.07x faster                                                 |
| xml_etree_generate   | 61.6 ms                                                         | 60.5 ms: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                 |
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.96 ms: 1.31x faster                                                 |
| django_template | 36.0 ms                                                         | 31.3 ms: 1.15x faster                                                 |
| genshi_xml      | 46.6 ms                                                         | 45.2 ms: 1.03x faster                                                 |
| genshi_text     | 21.0 ms                                                         | 20.4 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.76x faster                                                  |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                  |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 485 ms: 1.90x faster                                                  |
| deltablue                | 4.04 ms                                                         | 2.27 ms: 1.77x faster                                                 |
| async_tree_io            | 940 ms                                                          | 550 ms: 1.71x faster                                                  |
| logging_silent           | 97.9 ns                                                         | 57.9 ns: 1.69x faster                                                 |
| async_tree_none          | 394 ms                                                          | 237 ms: 1.66x faster                                                  |
| pylint                   | 384 ms                                                          | 231 ms: 1.66x faster                                                  |
| async_tree_memoization   | 467 ms                                                          | 290 ms: 1.61x faster                                                  |
| raytrace                 | 303 ms                                                          | 193 ms: 1.57x faster                                                  |
| chaos                    | 74.4 ms                                                         | 48.3 ms: 1.54x faster                                                 |
| comprehensions           | 17.7 us                                                         | 12.0 us: 1.48x faster                                                 |
| scimark_lu               | 89.8 ms                                                         | 60.8 ms: 1.48x faster                                                 |
| crypto_pyaes             | 81.3 ms                                                         | 55.7 ms: 1.46x faster                                                 |
| generators               | 31.6 ms                                                         | 21.8 ms: 1.44x faster                                                 |
| go                       | 146 ms                                                          | 101 ms: 1.44x faster                                                  |
| hexiom                   | 6.13 ms                                                         | 4.28 ms: 1.43x faster                                                 |
| richards_super           | 49.9 ms                                                         | 36.1 ms: 1.38x faster                                                 |
| scimark_sor              | 115 ms                                                          | 83.5 ms: 1.38x faster                                                 |
| pyflate                  | 422 ms                                                          | 310 ms: 1.36x faster                                                  |
| sqlglot_parse            | 1.33 ms                                                         | 985 us: 1.35x faster                                                  |
| mako                     | 9.10 ms                                                         | 6.96 ms: 1.31x faster                                                 |
| sqlglot_transpile        | 1.58 ms                                                         | 1.22 ms: 1.30x faster                                                 |
| scimark_monte_carlo      | 61.9 ms                                                         | 47.6 ms: 1.30x faster                                                 |
| nqueens                  | 87.1 ms                                                         | 67.1 ms: 1.30x faster                                                 |
| json_dumps               | 9.82 ms                                                         | 7.61 ms: 1.29x faster                                                 |
| float                    | 69.6 ms                                                         | 54.2 ms: 1.28x faster                                                 |
| unpickle_pure_python     | 189 us                                                          | 148 us: 1.28x faster                                                  |
| pycparser                | 1.04 sec                                                        | 815 ms: 1.28x faster                                                  |
| richards                 | 40.3 ms                                                         | 32.2 ms: 1.25x faster                                                 |
| pickle_pure_python       | 280 us                                                          | 226 us: 1.24x faster                                                  |
| deepcopy_memo            | 29.6 us                                                         | 24.0 us: 1.23x faster                                                 |
| dulwich_log              | 58.5 ms                                                         | 49.3 ms: 1.19x faster                                                 |
| regex_compile            | 117 ms                                                          | 99.2 ms: 1.18x faster                                                 |
| django_template          | 36.0 ms                                                         | 31.3 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.82 ms: 1.15x faster                                                 |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                  |
| coroutines               | 17.9 ms                                                         | 15.7 ms: 1.15x faster                                                 |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                  |
| bench_thread_pool        | 1.12 ms                                                         | 981 us: 1.14x faster                                                  |
| json                     | 4.76 ms                                                         | 4.19 ms: 1.14x faster                                                 |
| tomli_loads              | 1.91 sec                                                        | 1.68 sec: 1.13x faster                                                |
| fannkuch                 | 317 ms                                                          | 280 ms: 1.13x faster                                                  |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                  |
| spectral_norm            | 80.2 ms                                                         | 71.1 ms: 1.13x faster                                                 |
| xml_etree_process        | 48.1 ms                                                         | 42.8 ms: 1.13x faster                                                 |
| sympy_integrate          | 16.6 ms                                                         | 14.9 ms: 1.12x faster                                                 |
| pprint_pformat           | 1.37 sec                                                        | 1.23 sec: 1.11x faster                                                |
| chameleon                | 6.42 ms                                                         | 5.80 ms: 1.11x faster                                                 |
| mdp                      | 1.83 sec                                                        | 1.65 sec: 1.11x faster                                                |
| html5lib                 | 52.1 ms                                                         | 47.2 ms: 1.10x faster                                                 |
| sqlglot_normalize        | 230 ms                                                          | 211 ms: 1.09x faster                                                  |
| pprint_safe_repr         | 658 ms                                                          | 602 ms: 1.09x faster                                                  |
| sqlglot_optimize         | 44.7 ms                                                         | 41.0 ms: 1.09x faster                                                 |
| 2to3                     | 265 ms                                                          | 244 ms: 1.09x faster                                                  |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                                  |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.7 ms: 1.08x faster                                                 |
| meteor_contest           | 80.0 ms                                                         | 74.2 ms: 1.08x faster                                                 |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.07x faster                                                 |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                  |
| deepcopy                 | 310 us                                                          | 292 us: 1.06x faster                                                  |
| scimark_fft              | 216 ms                                                          | 205 ms: 1.06x faster                                                  |
| sympy_expand             | 391 ms                                                          | 371 ms: 1.05x faster                                                  |
| docutils                 | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                |
| genshi_xml               | 46.6 ms                                                         | 45.2 ms: 1.03x faster                                                 |
| genshi_text              | 21.0 ms                                                         | 20.4 ms: 1.03x faster                                                 |
| nbody                    | 79.1 ms                                                         | 77.1 ms: 1.03x faster                                                 |
| xml_etree_generate       | 61.6 ms                                                         | 60.5 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                |
| deepcopy_reduce          | 2.68 us                                                         | 2.72 us: 1.02x slower                                                 |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                 |
| logging_simple           | 7.29 us                                                         | 7.53 us: 1.03x slower                                                 |
| python_startup           | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                 |
| logging_format           | 7.91 us                                                         | 8.25 us: 1.04x slower                                                 |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                 |
| create_gc_cycles         | 694 us                                                          | 744 us: 1.07x slower                                                  |
| asyncio_tcp              | 744 ms                                                          | 816 ms: 1.10x slower                                                  |
| bench_mp_pool            | 66.4 ms                                                         | 72.8 ms: 1.10x slower                                                 |
| pathlib                  | 81.2 ms                                                         | 89.8 ms: 1.11x slower                                                 |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                 |
| async_generators         | 241 ms                                                          | 280 ms: 1.16x slower                                                  |
| telco                    | 4.83 ms                                                         | 6.04 ms: 1.25x slower                                                 |
| coverage                 | 46.6 ms                                                         | 315 ms: 6.77x slower                                                  |
| thrift                   | 902 us                                                          | 10.1 ms: 11.24x slower                                                |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                          |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.139x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown