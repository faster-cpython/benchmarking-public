# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: windows-x86
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 255 ms: 1.04x faster                                                     |
| docutils       | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                   |
| html5lib       | 52.1 ms                                                         | 46.2 ms: 1.13x faster                                                    |
| tornado_http   | 118 ms                                                          | 109 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                           | 1.06x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                     |
| async_tree_none         | 394 ms                                                          | 217 ms: 1.82x faster                                                     |
| async_tree_io           | 940 ms                                                          | 522 ms: 1.80x faster                                                     |
| async_tree_memoization  | 467 ms                                                          | 277 ms: 1.68x faster                                                     |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.47x faster                                                     |
| float          | 69.6 ms                                                         | 45.9 ms: 1.52x faster                                                    |
| nbody          | 79.1 ms                                                         | 57.9 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                           | 1.72x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 97.7 ms: 1.19x faster                                                    |
| regex_dna      | 131 ms                                                          | 113 ms: 1.15x faster                                                     |
| regex_v8       | 15.8 ms                                                         | 15.2 ms: 1.03x faster                                                    |
| regex_effbot   | 1.66 ms                                                         | 1.76 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                           | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                   |
| json_dumps           | 9.82 ms                                                         | 8.03 ms: 1.22x faster                                                    |
| unpickle_pure_python | 189 us                                                          | 156 us: 1.22x faster                                                     |
| pickle_pure_python   | 280 us                                                          | 237 us: 1.18x faster                                                     |
| xml_etree_process    | 48.1 ms                                                         | 40.8 ms: 1.18x faster                                                    |
| xml_etree_generate   | 61.6 ms                                                         | 54.9 ms: 1.12x faster                                                    |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.5 ms: 1.12x faster                                                    |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                     |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                    |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.6 ms: 1.14x slower                                                    |
| python_startup         | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                    |
| Geometric mean         | (ref)                                                           | 1.16x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.68 ms: 1.60x faster                                                    |
| django_template | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                    |
| genshi_xml      | 46.6 ms                                                         | 48.9 ms: 1.05x slower                                                    |
| genshi_text     | 21.0 ms                                                         | 22.5 ms: 1.07x slower                                                    |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.86x faster                                                     |
| pidigits                 | 502 ms                                                          | 203 ms: 2.47x faster                                                     |
| sqlglot_normalize        | 230 ms                                                          | 99.3 ms: 2.32x faster                                                    |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                     |
| deepcopy_memo            | 29.6 us                                                         | 15.8 us: 1.87x faster                                                    |
| async_tree_none          | 394 ms                                                          | 217 ms: 1.82x faster                                                     |
| async_tree_io            | 940 ms                                                          | 522 ms: 1.80x faster                                                     |
| logging_silent           | 97.9 ns                                                         | 55.1 ns: 1.78x faster                                                    |
| scimark_sor              | 115 ms                                                          | 67.0 ms: 1.72x faster                                                    |
| async_tree_memoization   | 467 ms                                                          | 277 ms: 1.68x faster                                                     |
| crypto_pyaes             | 81.3 ms                                                         | 48.9 ms: 1.66x faster                                                    |
| go                       | 146 ms                                                          | 89.2 ms: 1.63x faster                                                    |
| scimark_monte_carlo      | 61.9 ms                                                         | 37.9 ms: 1.63x faster                                                    |
| mako                     | 9.10 ms                                                         | 5.68 ms: 1.60x faster                                                    |
| deltablue                | 4.04 ms                                                         | 2.52 ms: 1.60x faster                                                    |
| scimark_lu               | 89.8 ms                                                         | 57.7 ms: 1.56x faster                                                    |
| float                    | 69.6 ms                                                         | 45.9 ms: 1.52x faster                                                    |
| comprehensions           | 17.7 us                                                         | 12.5 us: 1.42x faster                                                    |
| generators               | 31.6 ms                                                         | 22.4 ms: 1.41x faster                                                    |
| pyflate                  | 422 ms                                                          | 300 ms: 1.41x faster                                                     |
| chaos                    | 74.4 ms                                                         | 53.0 ms: 1.40x faster                                                    |
| pylint                   | 384 ms                                                          | 278 ms: 1.38x faster                                                     |
| fannkuch                 | 317 ms                                                          | 232 ms: 1.37x faster                                                     |
| nbody                    | 79.1 ms                                                         | 57.9 ms: 1.37x faster                                                    |
| spectral_norm            | 80.2 ms                                                         | 58.7 ms: 1.37x faster                                                    |
| pycparser                | 1.04 sec                                                        | 781 ms: 1.33x faster                                                     |
| deepcopy                 | 310 us                                                          | 233 us: 1.33x faster                                                     |
| sqlglot_parse            | 1.33 ms                                                         | 1.01 ms: 1.32x faster                                                    |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.48 ms: 1.31x faster                                                    |
| hexiom                   | 6.13 ms                                                         | 4.70 ms: 1.31x faster                                                    |
| tomli_loads              | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                   |
| scimark_fft              | 216 ms                                                          | 175 ms: 1.23x faster                                                     |
| richards_super           | 49.9 ms                                                         | 40.7 ms: 1.23x faster                                                    |
| json_dumps               | 9.82 ms                                                         | 8.03 ms: 1.22x faster                                                    |
| unpickle_pure_python     | 189 us                                                          | 156 us: 1.22x faster                                                     |
| sqlglot_transpile        | 1.58 ms                                                         | 1.30 ms: 1.22x faster                                                    |
| pprint_pformat           | 1.37 sec                                                        | 1.13 sec: 1.21x faster                                                   |
| dulwich_log              | 58.5 ms                                                         | 48.7 ms: 1.20x faster                                                    |
| regex_compile            | 117 ms                                                          | 97.7 ms: 1.19x faster                                                    |
| nqueens                  | 87.1 ms                                                         | 73.4 ms: 1.19x faster                                                    |
| pprint_safe_repr         | 658 ms                                                          | 556 ms: 1.18x faster                                                     |
| pickle_pure_python       | 280 us                                                          | 237 us: 1.18x faster                                                     |
| xml_etree_process        | 48.1 ms                                                         | 40.8 ms: 1.18x faster                                                    |
| regex_dna                | 131 ms                                                          | 113 ms: 1.15x faster                                                     |
| richards                 | 40.3 ms                                                         | 34.9 ms: 1.15x faster                                                    |
| raytrace                 | 303 ms                                                          | 263 ms: 1.15x faster                                                     |
| thrift                   | 902 us                                                          | 784 us: 1.15x faster                                                     |
| deepcopy_reduce          | 2.68 us                                                         | 2.36 us: 1.14x faster                                                    |
| meteor_contest           | 80.0 ms                                                         | 70.7 ms: 1.13x faster                                                    |
| html5lib                 | 52.1 ms                                                         | 46.2 ms: 1.13x faster                                                    |
| xml_etree_generate       | 61.6 ms                                                         | 54.9 ms: 1.12x faster                                                    |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.5 ms: 1.12x faster                                                    |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.11x faster                                                    |
| django_template          | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                    |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                     |
| mdp                      | 1.83 sec                                                        | 1.67 sec: 1.09x faster                                                   |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.08x faster                                                     |
| tornado_http             | 118 ms                                                          | 109 ms: 1.08x faster                                                     |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                    |
| sympy_str                | 229 ms                                                          | 219 ms: 1.04x faster                                                     |
| 2to3                     | 265 ms                                                          | 255 ms: 1.04x faster                                                     |
| regex_v8                 | 15.8 ms                                                         | 15.2 ms: 1.03x faster                                                    |
| coroutines               | 17.9 ms                                                         | 17.4 ms: 1.03x faster                                                    |
| sympy_expand             | 391 ms                                                          | 382 ms: 1.02x faster                                                     |
| docutils                 | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                   |
| sympy_integrate          | 16.6 ms                                                         | 17.0 ms: 1.02x slower                                                    |
| logging_simple           | 7.29 us                                                         | 7.50 us: 1.03x slower                                                    |
| logging_format           | 7.91 us                                                         | 8.23 us: 1.04x slower                                                    |
| genshi_xml               | 46.6 ms                                                         | 48.9 ms: 1.05x slower                                                    |
| regex_effbot             | 1.66 ms                                                         | 1.76 ms: 1.06x slower                                                    |
| sqlglot_optimize         | 44.7 ms                                                         | 47.8 ms: 1.07x slower                                                    |
| genshi_text              | 21.0 ms                                                         | 22.5 ms: 1.07x slower                                                    |
| json                     | 4.76 ms                                                         | 5.15 ms: 1.08x slower                                                    |
| pathlib                  | 81.2 ms                                                         | 88.4 ms: 1.09x slower                                                    |
| python_startup_no_site   | 18.1 ms                                                         | 20.6 ms: 1.14x slower                                                    |
| coverage                 | 46.6 ms                                                         | 53.3 ms: 1.15x slower                                                    |
| python_startup           | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                    |
| telco                    | 4.83 ms                                                         | 6.16 ms: 1.28x slower                                                    |
| async_generators         | 241 ms                                                          | 319 ms: 1.32x slower                                                     |
| bench_mp_pool            | 66.4 ms                                                         | 93.6 ms: 1.41x slower                                                    |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                    |
| create_gc_cycles         | 694 us                                                          | 1.18 ms: 1.69x slower                                                    |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                             |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown