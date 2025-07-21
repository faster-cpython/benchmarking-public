# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.294x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 227 ms: 1.17x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.87 sec: 1.47x slower                                                           |
| html5lib       | 52.1 ms                                                         | 40.2 ms: 1.30x faster                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 332 ms: 2.78x faster                                                             |
| async_tree_io           | 940 ms                                                          | 353 ms: 2.67x faster                                                             |
| async_tree_none         | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 214 ms: 2.18x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 135 ms: 3.71x faster                                                             |
| float          | 69.6 ms                                                         | 46.0 ms: 1.51x faster                                                            |
| nbody          | 79.1 ms                                                         | 80.4 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.77x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                            |
| regex_compile  | 117 ms                                                          | 95.4 ms: 1.22x faster                                                            |
| regex_dna      | 131 ms                                                          | 112 ms: 1.16x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.49 ms: 1.11x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.58 ms: 1.49x faster                                                            |
| json_loads           | 22.4 us                                                         | 15.8 us: 1.42x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 89.9 ms: 1.33x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 155 us: 1.22x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.0 ms: 1.22x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 233 us: 1.20x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 45.1 ms: 1.07x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.15 us: 1.02x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 63.7 ms: 1.03x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.09 us: 1.04x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                            |
| pickle               | 7.83 us                                                         | 8.18 us: 1.04x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.5 us: 1.13x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.73 sec: 1.43x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.1 ms: 1.33x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 39.9 ms: 1.17x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 20.0 ms: 1.05x faster                                                            |
| mako            | 9.10 ms                                                         | 9.68 ms: 1.06x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.14 sec: 7.92x faster                                                           |
| pidigits                 | 502 ms                                                          | 135 ms: 3.71x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 128 us: 3.08x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 332 ms: 2.78x faster                                                             |
| async_tree_io            | 940 ms                                                          | 353 ms: 2.67x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 30.5 ms: 2.67x faster                                                            |
| async_tree_none          | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 214 ms: 2.18x faster                                                             |
| pylint                   | 384 ms                                                          | 205 ms: 1.87x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.33 us: 1.72x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 436 ms: 1.70x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.41 ms: 1.67x faster                                                            |
| chaos                    | 74.4 ms                                                         | 46.2 ms: 1.61x faster                                                            |
| go                       | 146 ms                                                          | 91.4 ms: 1.59x faster                                                            |
| thrift                   | 902 us                                                          | 570 us: 1.58x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 62.0 ns: 1.58x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.16 sec: 1.58x faster                                                           |
| json                     | 4.76 ms                                                         | 3.06 ms: 1.56x faster                                                            |
| deepcopy                 | 310 us                                                          | 200 us: 1.55x faster                                                             |
| float                    | 69.6 ms                                                         | 46.0 ms: 1.51x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.8 us: 1.50x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.58 ms: 1.49x faster                                                            |
| pycparser                | 1.04 sec                                                        | 715 ms: 1.46x faster                                                             |
| json_loads               | 22.4 us                                                         | 15.8 us: 1.42x faster                                                            |
| raytrace                 | 303 ms                                                          | 214 ms: 1.41x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 21.0 us: 1.41x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 58.3 ms: 1.39x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 42.1 ms: 1.39x faster                                                            |
| generators               | 31.6 ms                                                         | 22.9 ms: 1.38x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 65.3 ms: 1.38x faster                                                            |
| pyflate                  | 422 ms                                                          | 308 ms: 1.37x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 89.9 ms: 1.33x faster                                                            |
| scimark_sor              | 115 ms                                                          | 86.6 ms: 1.33x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.1 ms: 1.33x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.64 ms: 1.32x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 40.2 ms: 1.30x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.10 us: 1.28x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.1 ms: 1.27x faster                                                            |
| sympy_sum                | 122 ms                                                          | 97.0 ms: 1.26x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.3 ms: 1.26x faster                                                            |
| richards_super           | 49.9 ms                                                         | 40.2 ms: 1.24x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                            |
| regex_compile            | 117 ms                                                          | 95.4 ms: 1.22x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 155 us: 1.22x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.0 ms: 1.22x faster                                                            |
| sympy_expand             | 391 ms                                                          | 321 ms: 1.22x faster                                                             |
| sympy_str                | 229 ms                                                          | 189 ms: 1.21x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 233 us: 1.20x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 72.6 ms: 1.20x faster                                                            |
| richards                 | 40.3 ms                                                         | 34.0 ms: 1.18x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 14.1 ms: 1.18x faster                                                            |
| 2to3                     | 265 ms                                                          | 227 ms: 1.17x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 39.9 ms: 1.17x faster                                                            |
| regex_dna                | 131 ms                                                          | 112 ms: 1.16x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 567 ms: 1.16x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.49 ms: 1.11x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.15 ms: 1.11x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.32 us: 1.08x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 74.6 ms: 1.08x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 45.1 ms: 1.07x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.86 us: 1.06x faster                                                            |
| fannkuch                 | 317 ms                                                          | 300 ms: 1.06x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 20.0 ms: 1.05x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 38.6 ns: 1.04x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.15 us: 1.02x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.18 ms: 1.02x faster                                                            |
| scimark_fft              | 216 ms                                                          | 213 ms: 1.02x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 1.10 ms: 1.01x faster                                                            |
| nbody                    | 79.1 ms                                                         | 80.4 ms: 1.02x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 63.7 ms: 1.03x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.09 us: 1.04x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.18 us: 1.04x slower                                                            |
| async_generators         | 241 ms                                                          | 255 ms: 1.06x slower                                                             |
| mako                     | 9.10 ms                                                         | 9.68 ms: 1.06x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 85.4 ms: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.25 ms: 1.09x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.5 us: 1.13x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 78.5 ms: 1.18x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.69 sec: 1.24x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.73 sec: 1.43x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 996 us: 1.44x slower                                                             |
| coverage                 | 46.6 ms                                                         | 68.3 ms: 1.47x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.87 sec: 1.47x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.29x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.294x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown