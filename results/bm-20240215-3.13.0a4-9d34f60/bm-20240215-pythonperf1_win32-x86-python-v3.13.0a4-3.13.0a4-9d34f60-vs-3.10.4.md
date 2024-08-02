# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 230 ms: 1.15x faster                                                |
| chameleon      | 6.42 ms                                                         | 5.61 ms: 1.15x faster                                               |
| docutils       | 1.95 sec                                                        | 1.71 sec: 1.14x faster                                              |
| html5lib       | 52.1 ms                                                         | 43.9 ms: 1.19x faster                                               |
| tornado_http   | 118 ms                                                          | 93.5 ms: 1.26x faster                                               |
| Geometric mean | (ref)                                                           | 1.17x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 496 ms: 1.86x faster                                                |
| async_tree_none         | 394 ms                                                          | 239 ms: 1.65x faster                                                |
| async_tree_io           | 940 ms                                                          | 584 ms: 1.61x faster                                                |
| async_tree_memoization  | 467 ms                                                          | 299 ms: 1.56x faster                                                |
| Geometric mean          | (ref)                                                           | 1.67x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.56x faster                                                |
| float          | 69.6 ms                                                         | 52.8 ms: 1.32x faster                                               |
| nbody          | 79.1 ms                                                         | 76.8 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                           | 1.51x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 93.4 ms: 1.25x faster                                               |
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                               |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                           | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.71 ms: 1.46x faster                                               |
| unpickle_pure_python | 189 us                                                          | 140 us: 1.35x faster                                                |
| pickle_pure_python   | 280 us                                                          | 210 us: 1.34x faster                                                |
| tomli_loads          | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                              |
| xml_etree_process    | 48.1 ms                                                         | 41.2 ms: 1.17x faster                                               |
| json_loads           | 22.4 us                                                         | 20.2 us: 1.11x faster                                               |
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.2 ms: 1.07x faster                                               |
| unpickle_list        | 2.98 us                                                         | 2.88 us: 1.04x faster                                               |
| xml_etree_generate   | 61.6 ms                                                         | 60.0 ms: 1.03x faster                                               |
| pickle               | 7.83 us                                                         | 7.90 us: 1.01x slower                                               |
| pickle_list          | 3.22 us                                                         | 3.25 us: 1.01x slower                                               |
| unpickle             | 9.82 us                                                         | 10.0 us: 1.02x slower                                               |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.0 ms: 1.04x faster                                               |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.76 ms: 1.35x faster                                               |
| django_template | 36.0 ms                                                         | 30.4 ms: 1.19x faster                                               |
| genshi_xml      | 46.6 ms                                                         | 41.8 ms: 1.11x faster                                               |
| genshi_text     | 21.0 ms                                                         | 18.9 ms: 1.11x faster                                               |
| Geometric mean  | (ref)                                                           | 1.19x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 87.8 us: 4.50x faster                                               |
| pidigits                 | 502 ms                                                          | 197 ms: 2.56x faster                                                |
| deltablue                | 4.04 ms                                                         | 2.17 ms: 1.86x faster                                               |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 496 ms: 1.86x faster                                                |
| pylint                   | 384 ms                                                          | 217 ms: 1.77x faster                                                |
| logging_silent           | 97.9 ns                                                         | 56.9 ns: 1.72x faster                                               |
| async_tree_none          | 394 ms                                                          | 239 ms: 1.65x faster                                                |
| async_tree_io            | 940 ms                                                          | 584 ms: 1.61x faster                                                |
| chaos                    | 74.4 ms                                                         | 46.3 ms: 1.61x faster                                               |
| raytrace                 | 303 ms                                                          | 191 ms: 1.59x faster                                                |
| async_tree_memoization   | 467 ms                                                          | 299 ms: 1.56x faster                                                |
| comprehensions           | 17.7 us                                                         | 11.5 us: 1.55x faster                                               |
| crypto_pyaes             | 81.3 ms                                                         | 52.6 ms: 1.55x faster                                               |
| sqlglot_parse            | 1.33 ms                                                         | 868 us: 1.53x faster                                                |
| go                       | 146 ms                                                          | 95.1 ms: 1.53x faster                                               |
| scimark_lu               | 89.8 ms                                                         | 59.0 ms: 1.52x faster                                               |
| richards_super           | 49.9 ms                                                         | 33.7 ms: 1.48x faster                                               |
| json_dumps               | 9.82 ms                                                         | 6.71 ms: 1.46x faster                                               |
| hexiom                   | 6.13 ms                                                         | 4.20 ms: 1.46x faster                                               |
| sqlglot_transpile        | 1.58 ms                                                         | 1.10 ms: 1.43x faster                                               |
| scimark_sor              | 115 ms                                                          | 80.9 ms: 1.42x faster                                               |
| richards                 | 40.3 ms                                                         | 28.4 ms: 1.42x faster                                               |
| generators               | 31.6 ms                                                         | 22.7 ms: 1.39x faster                                               |
| scimark_monte_carlo      | 61.9 ms                                                         | 44.9 ms: 1.38x faster                                               |
| pyflate                  | 422 ms                                                          | 307 ms: 1.37x faster                                                |
| unpickle_pure_python     | 189 us                                                          | 140 us: 1.35x faster                                                |
| mako                     | 9.10 ms                                                         | 6.76 ms: 1.35x faster                                               |
| deepcopy_memo            | 29.6 us                                                         | 22.0 us: 1.35x faster                                               |
| pickle_pure_python       | 280 us                                                          | 210 us: 1.34x faster                                                |
| pycparser                | 1.04 sec                                                        | 784 ms: 1.33x faster                                                |
| float                    | 69.6 ms                                                         | 52.8 ms: 1.32x faster                                               |
| nqueens                  | 87.1 ms                                                         | 66.9 ms: 1.30x faster                                               |
| coroutines               | 17.9 ms                                                         | 14.1 ms: 1.27x faster                                               |
| tornado_http             | 118 ms                                                          | 93.5 ms: 1.26x faster                                               |
| regex_compile            | 117 ms                                                          | 93.4 ms: 1.25x faster                                               |
| sqlite_synth             | 2.29 us                                                         | 1.85 us: 1.24x faster                                               |
| sympy_sum                | 122 ms                                                          | 99.4 ms: 1.23x faster                                               |
| spectral_norm            | 80.2 ms                                                         | 65.4 ms: 1.23x faster                                               |
| asyncio_tcp              | 744 ms                                                          | 618 ms: 1.20x faster                                                |
| deepcopy                 | 310 us                                                          | 261 us: 1.19x faster                                                |
| django_template          | 36.0 ms                                                         | 30.4 ms: 1.19x faster                                               |
| html5lib                 | 52.1 ms                                                         | 43.9 ms: 1.19x faster                                               |
| sympy_integrate          | 16.6 ms                                                         | 14.0 ms: 1.18x faster                                               |
| sympy_str                | 229 ms                                                          | 194 ms: 1.18x faster                                                |
| tomli_loads              | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                              |
| pprint_pformat           | 1.37 sec                                                        | 1.16 sec: 1.17x faster                                              |
| fannkuch                 | 317 ms                                                          | 271 ms: 1.17x faster                                                |
| xml_etree_process        | 48.1 ms                                                         | 41.2 ms: 1.17x faster                                               |
| mdp                      | 1.83 sec                                                        | 1.57 sec: 1.16x faster                                              |
| pprint_safe_repr         | 658 ms                                                          | 568 ms: 1.16x faster                                                |
| sqlglot_optimize         | 44.7 ms                                                         | 38.6 ms: 1.16x faster                                               |
| deepcopy_reduce          | 2.68 us                                                         | 2.32 us: 1.16x faster                                               |
| 2to3                     | 265 ms                                                          | 230 ms: 1.15x faster                                                |
| sympy_expand             | 391 ms                                                          | 341 ms: 1.15x faster                                                |
| sqlglot_normalize        | 230 ms                                                          | 201 ms: 1.15x faster                                                |
| chameleon                | 6.42 ms                                                         | 5.61 ms: 1.15x faster                                               |
| json                     | 4.76 ms                                                         | 4.16 ms: 1.14x faster                                               |
| bench_thread_pool        | 1.12 ms                                                         | 984 us: 1.14x faster                                                |
| docutils                 | 1.95 sec                                                        | 1.71 sec: 1.14x faster                                              |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.88 ms: 1.12x faster                                               |
| genshi_xml               | 46.6 ms                                                         | 41.8 ms: 1.11x faster                                               |
| genshi_text              | 21.0 ms                                                         | 18.9 ms: 1.11x faster                                               |
| json_loads               | 22.4 us                                                         | 20.2 us: 1.11x faster                                               |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                |
| scimark_fft              | 216 ms                                                          | 198 ms: 1.09x faster                                                |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.2 ms: 1.07x faster                                               |
| create_gc_cycles         | 694 us                                                          | 662 us: 1.05x faster                                                |
| python_startup           | 22.9 ms                                                         | 22.0 ms: 1.04x faster                                               |
| unpickle_list            | 2.98 us                                                         | 2.88 us: 1.04x faster                                               |
| meteor_contest           | 80.0 ms                                                         | 77.4 ms: 1.03x faster                                               |
| nbody                    | 79.1 ms                                                         | 76.8 ms: 1.03x faster                                               |
| xml_etree_generate       | 61.6 ms                                                         | 60.0 ms: 1.03x faster                                               |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                              |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                              |
| pickle                   | 7.83 us                                                         | 7.90 us: 1.01x slower                                               |
| pickle_list              | 3.22 us                                                         | 3.25 us: 1.01x slower                                               |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                               |
| unpickle                 | 9.82 us                                                         | 10.0 us: 1.02x slower                                               |
| logging_simple           | 7.29 us                                                         | 7.46 us: 1.02x slower                                               |
| logging_format           | 7.91 us                                                         | 8.10 us: 1.02x slower                                               |
| bench_mp_pool            | 66.4 ms                                                         | 70.4 ms: 1.06x slower                                               |
| gc_traversal             | 1.28 ms                                                         | 1.39 ms: 1.08x slower                                               |
| async_generators         | 241 ms                                                          | 262 ms: 1.09x slower                                                |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.09x slower                                               |
| pathlib                  | 81.2 ms                                                         | 88.6 ms: 1.09x slower                                               |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                               |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.13x slower                                               |
| telco                    | 4.83 ms                                                         | 5.76 ms: 1.19x slower                                               |
| coverage                 | 46.6 ms                                                         | 460 ms: 9.87x slower                                                |
| thrift                   | 902 us                                                          | 9.86 ms: 10.93x slower                                              |
| Geometric mean           | (ref)                                                           | 1.17x faster                                                        |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown