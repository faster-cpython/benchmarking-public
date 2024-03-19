# Results vs. 3.10.4

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: windows-x86
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.06x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.67 ms: 1.13x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.83 sec: 1.07x faster                                                          |
| html5lib       | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                           |
| tornado_http   | 118 ms                                                          | 96.2 ms: 1.22x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 507 ms: 1.82x faster                                                            |
| async_tree_none         | 394 ms                                                          | 256 ms: 1.54x faster                                                            |
| async_tree_io           | 940 ms                                                          | 618 ms: 1.52x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 319 ms: 1.46x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.58x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                            |
| float          | 69.6 ms                                                         | 53.9 ms: 1.29x faster                                                           |
| nbody          | 79.1 ms                                                         | 95.1 ms: 1.20x slower                                                           |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 109 ms: 1.07x faster                                                            |
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.91 ms: 1.42x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 210 us: 1.33x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 167 us: 1.14x faster                                                            |
| json_loads           | 22.4 us                                                         | 19.8 us: 1.13x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 42.7 ms: 1.13x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.4 ms: 1.05x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.88 us: 1.04x faster                                                           |
| pickle               | 7.83 us                                                         | 7.89 us: 1.01x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.31 us: 1.03x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.0 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 26.4 ms: 1.15x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 23.9 ms: 1.32x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.23x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.94 ms: 1.31x faster                                                           |
| django_template | 36.0 ms                                                         | 30.0 ms: 1.20x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 49.7 ms: 1.07x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 22.7 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 96.4 us: 4.10x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 507 ms: 1.82x faster                                                            |
| pylint                   | 384 ms                                                          | 228 ms: 1.69x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 61.1 ns: 1.60x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.55 ms: 1.58x faster                                                           |
| async_tree_none          | 394 ms                                                          | 256 ms: 1.54x faster                                                            |
| async_tree_io            | 940 ms                                                          | 618 ms: 1.52x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 319 ms: 1.46x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.91 ms: 1.42x faster                                                           |
| generators               | 31.6 ms                                                         | 22.2 ms: 1.42x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 960 us: 1.39x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 210 us: 1.33x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 61.3 ms: 1.33x faster                                                           |
| mako                     | 9.10 ms                                                         | 6.94 ms: 1.31x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.21 ms: 1.31x faster                                                           |
| float                    | 69.6 ms                                                         | 53.9 ms: 1.29x faster                                                           |
| richards_super           | 49.9 ms                                                         | 39.0 ms: 1.28x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.2 ms: 1.27x faster                                                           |
| chaos                    | 74.4 ms                                                         | 58.8 ms: 1.27x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.2 us: 1.22x faster                                                           |
| tornado_http             | 118 ms                                                          | 96.2 ms: 1.22x faster                                                           |
| scimark_sor              | 115 ms                                                          | 94.8 ms: 1.21x faster                                                           |
| pycparser                | 1.04 sec                                                        | 860 ms: 1.21x faster                                                            |
| comprehensions           | 17.7 us                                                         | 14.7 us: 1.20x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.0 ms: 1.20x faster                                                           |
| go                       | 146 ms                                                          | 123 ms: 1.19x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 628 ms: 1.18x faster                                                            |
| json                     | 4.76 ms                                                         | 4.08 ms: 1.17x faster                                                           |
| richards                 | 40.3 ms                                                         | 34.7 ms: 1.16x faster                                                           |
| raytrace                 | 303 ms                                                          | 266 ms: 1.14x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 167 us: 1.14x faster                                                            |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                            |
| json_loads               | 22.4 us                                                         | 19.8 us: 1.13x faster                                                           |
| chameleon                | 6.42 ms                                                         | 5.67 ms: 1.13x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 42.7 ms: 1.13x faster                                                           |
| pyflate                  | 422 ms                                                          | 374 ms: 1.13x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| deepcopy                 | 310 us                                                          | 279 us: 1.11x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 72.2 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.46 us: 1.09x faster                                                           |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                           |
| regex_compile            | 117 ms                                                          | 109 ms: 1.07x faster                                                            |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.83 sec: 1.07x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 84.3 ms: 1.06x faster                                                           |
| sympy_expand             | 391 ms                                                          | 370 ms: 1.05x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.4 ms: 1.05x faster                                                           |
| create_gc_cycles         | 694 us                                                          | 667 us: 1.04x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.88 us: 1.04x faster                                                           |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 6.04 ms: 1.02x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 227 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.20 ms: 1.01x faster                                                           |
| pickle                   | 7.83 us                                                         | 7.89 us: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 63.0 ms: 1.02x slower                                                           |
| fannkuch                 | 317 ms                                                          | 324 ms: 1.02x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 82.2 ms: 1.03x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.31 us: 1.03x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 90.0 ms: 1.03x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 46.4 ms: 1.04x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 86.0 ms: 1.06x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 49.7 ms: 1.07x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.7 ms: 1.08x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.49 sec: 1.09x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 43.7 ns: 1.09x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.40 ms: 1.09x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.0 us: 1.09x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 722 ms: 1.10x slower                                                            |
| scimark_fft              | 216 ms                                                          | 239 ms: 1.10x slower                                                            |
| logging_format           | 7.91 us                                                         | 8.82 us: 1.11x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 74.6 ms: 1.12x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.21 us: 1.13x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.4 ms: 1.15x slower                                                           |
| nbody                    | 79.1 ms                                                         | 95.1 ms: 1.20x slower                                                           |
| async_generators         | 241 ms                                                          | 297 ms: 1.23x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.33 ms: 1.31x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 23.9 ms: 1.32x slower                                                           |
| coverage                 | 46.6 ms                                                         | 495 ms: 10.63x slower                                                           |
| thrift                   | 902 us                                                          | 10.7 ms: 11.91x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240313-3.13.0a5+-8c094c3-JIT/bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x


# Memory

- memory change: unknown