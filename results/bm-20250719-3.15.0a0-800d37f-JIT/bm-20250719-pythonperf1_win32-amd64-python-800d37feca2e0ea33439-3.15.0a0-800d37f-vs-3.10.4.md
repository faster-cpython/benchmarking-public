# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.482x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.65 sec: 1.18x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.8 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 332 ms: 2.78x faster                                                             |
| async_tree_io           | 940 ms                                                          | 393 ms: 2.39x faster                                                             |
| async_tree_none         | 394 ms                                                          | 168 ms: 2.35x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.44x faster                                                             |
| float          | 69.6 ms                                                         | 43.2 ms: 1.61x faster                                                            |
| nbody          | 79.1 ms                                                         | 57.3 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                           | 1.97x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.6 ms: 1.48x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.8 ms: 1.14x faster                                                            |
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 105 us: 1.80x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.11 sec: 1.72x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 6.18 ms: 1.59x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.4 us: 1.55x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 203 us: 1.38x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 87.3 ms: 1.37x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 35.3 ms: 1.36x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 51.0 ms: 1.21x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.68 us: 1.13x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.2 ms: 1.12x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.77 us: 1.08x faster                                                            |
| pickle               | 7.83 us                                                         | 7.59 us: 1.03x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.29 us: 1.02x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.4 us: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.42 ms: 1.68x faster                                                            |
| django_template | 36.0 ms                                                         | 24.6 ms: 1.46x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.5 ms: 1.36x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.8 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.45x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.42 sec: 11.97x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 101 us: 3.93x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.44x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 332 ms: 2.78x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 30.2 ms: 2.69x faster                                                            |
| async_tree_io            | 940 ms                                                          | 393 ms: 2.39x faster                                                             |
| async_tree_none          | 394 ms                                                          | 168 ms: 2.35x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| mdp                      | 1.83 sec                                                        | 796 ms: 2.29x faster                                                             |
| pylint                   | 384 ms                                                          | 197 ms: 1.95x faster                                                             |
| go                       | 146 ms                                                          | 76.7 ms: 1.90x faster                                                            |
| thrift                   | 902 us                                                          | 488 us: 1.85x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.19 ms: 1.84x faster                                                            |
| chaos                    | 74.4 ms                                                         | 40.6 ms: 1.83x faster                                                            |
| deepcopy                 | 310 us                                                          | 170 us: 1.83x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 54.1 ns: 1.81x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 105 us: 1.80x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 45.6 ms: 1.78x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.11 sec: 1.72x faster                                                           |
| raytrace                 | 303 ms                                                          | 178 ms: 1.70x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.5 us: 1.70x faster                                                            |
| pyflate                  | 422 ms                                                          | 251 ms: 1.68x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.42 ms: 1.68x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.0 us: 1.64x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.8 ms: 1.62x faster                                                            |
| float                    | 69.6 ms                                                         | 43.2 ms: 1.61x faster                                                            |
| generators               | 31.6 ms                                                         | 19.6 ms: 1.61x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.18 ms: 1.59x faster                                                            |
| json                     | 4.76 ms                                                         | 3.01 ms: 1.58x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.4 us: 1.55x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 897 ms: 1.53x faster                                                             |
| pycparser                | 1.04 sec                                                        | 689 ms: 1.51x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.08 ms: 1.50x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.8 ms: 1.50x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.5 ms: 1.49x faster                                                            |
| fannkuch                 | 317 ms                                                          | 213 ms: 1.49x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 443 ms: 1.48x faster                                                             |
| regex_compile            | 117 ms                                                          | 78.6 ms: 1.48x faster                                                            |
| scimark_sor              | 115 ms                                                          | 78.0 ms: 1.48x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 506 ms: 1.47x faster                                                             |
| django_template          | 36.0 ms                                                         | 24.6 ms: 1.46x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.84 us: 1.46x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.58 us: 1.45x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.23 ms: 1.45x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.3 ms: 1.45x faster                                                            |
| scimark_fft              | 216 ms                                                          | 149 ms: 1.45x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 61.1 ms: 1.43x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 63.8 ms: 1.41x faster                                                            |
| sympy_sum                | 122 ms                                                          | 87.7 ms: 1.40x faster                                                            |
| nbody                    | 79.1 ms                                                         | 57.3 ms: 1.38x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 203 us: 1.38x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 87.3 ms: 1.37x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 35.3 ms: 1.36x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.5 ms: 1.36x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.8 ms: 1.34x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.8 ms: 1.34x faster                                                            |
| sympy_str                | 229 ms                                                          | 171 ms: 1.34x faster                                                             |
| sympy_expand             | 391 ms                                                          | 293 ms: 1.33x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 847 us: 1.32x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.6 ms: 1.32x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 63.1 ms: 1.27x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.2 ms: 1.26x faster                                                            |
| 2to3                     | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 51.0 ms: 1.21x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.57 us: 1.20x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.14 us: 1.19x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.65 sec: 1.18x faster                                                           |
| unpack_sequence          | 40.0 ns                                                         | 34.5 ns: 1.16x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 69.1 ms: 1.16x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.8 ms: 1.14x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.68 us: 1.13x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.29 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.2 ms: 1.12x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.77 us: 1.08x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.59 us: 1.03x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.29 us: 1.02x slower                                                            |
| async_generators         | 241 ms                                                          | 248 ms: 1.03x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 19.4 us: 1.06x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.7 ms: 1.07x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 94.5 ms: 1.42x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.11 ms: 1.65x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.29 ms: 1.86x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.47x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.482x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.42x
- 95% likely to have a speedup of 1.40x
- 99% likely to have a speedup of 1.38x

# Memory
- memory change: unknown