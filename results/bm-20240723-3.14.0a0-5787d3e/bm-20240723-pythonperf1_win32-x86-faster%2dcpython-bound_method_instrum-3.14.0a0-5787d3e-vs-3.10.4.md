# Results vs. 3.10.4

- fork: faster-cpython
- ref: bound_method_instrum
- machine: windows-x86
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 254 ms: 1.05x faster                                                                     |
| docutils       | 1.95 sec                                                        | 1.90 sec: 1.02x faster                                                                   |
| html5lib       | 52.1 ms                                                         | 48.2 ms: 1.08x faster                                                                    |
| tornado_http   | 118 ms                                                          | 105 ms: 1.12x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 472 ms: 1.96x faster                                                                     |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.76x faster                                                                     |
| async_tree_io           | 940 ms                                                          | 547 ms: 1.72x faster                                                                     |
| async_tree_memoization  | 467 ms                                                          | 274 ms: 1.70x faster                                                                     |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                                     |
| float          | 69.6 ms                                                         | 58.9 ms: 1.18x faster                                                                    |
| nbody          | 79.1 ms                                                         | 90.3 ms: 1.14x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 105 ms: 1.11x faster                                                                     |
| regex_dna      | 131 ms                                                          | 128 ms: 1.02x faster                                                                     |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                                    |
| regex_effbot   | 1.66 ms                                                         | 1.98 ms: 1.19x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.12 ms: 1.38x faster                                                                    |
| pickle_pure_python   | 280 us                                                          | 242 us: 1.16x faster                                                                     |
| unpickle_pure_python | 189 us                                                          | 166 us: 1.14x faster                                                                     |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                                                     |
| json_loads           | 22.4 us                                                         | 20.3 us: 1.10x faster                                                                    |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.6 ms: 1.05x faster                                                                    |
| tomli_loads          | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                                   |
| xml_etree_process    | 48.1 ms                                                         | 47.2 ms: 1.02x faster                                                                    |
| xml_etree_generate   | 61.6 ms                                                         | 64.4 ms: 1.05x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.6 ms: 1.03x slower                                                                    |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.96 ms: 1.14x faster                                                                    |
| django_template | 36.0 ms                                                         | 35.0 ms: 1.03x faster                                                                    |
| genshi_xml      | 46.6 ms                                                         | 48.2 ms: 1.04x slower                                                                    |
| genshi_text     | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 149 us: 2.66x faster                                                                     |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                                     |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 472 ms: 1.96x faster                                                                     |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.76x faster                                                                     |
| async_tree_io            | 940 ms                                                          | 547 ms: 1.72x faster                                                                     |
| async_tree_memoization   | 467 ms                                                          | 274 ms: 1.70x faster                                                                     |
| pylint                   | 384 ms                                                          | 235 ms: 1.63x faster                                                                     |
| deltablue                | 4.04 ms                                                         | 2.58 ms: 1.57x faster                                                                    |
| deepcopy_memo            | 29.6 us                                                         | 21.3 us: 1.39x faster                                                                    |
| chaos                    | 74.4 ms                                                         | 53.7 ms: 1.38x faster                                                                    |
| json_dumps               | 9.82 ms                                                         | 7.12 ms: 1.38x faster                                                                    |
| crypto_pyaes             | 81.3 ms                                                         | 58.9 ms: 1.38x faster                                                                    |
| raytrace                 | 303 ms                                                          | 221 ms: 1.37x faster                                                                     |
| logging_silent           | 97.9 ns                                                         | 72.7 ns: 1.35x faster                                                                    |
| comprehensions           | 17.7 us                                                         | 13.7 us: 1.30x faster                                                                    |
| scimark_lu               | 89.8 ms                                                         | 69.4 ms: 1.29x faster                                                                    |
| go                       | 146 ms                                                          | 114 ms: 1.27x faster                                                                     |
| pyflate                  | 422 ms                                                          | 337 ms: 1.25x faster                                                                     |
| deepcopy                 | 310 us                                                          | 249 us: 1.25x faster                                                                     |
| sqlglot_parse            | 1.33 ms                                                         | 1.08 ms: 1.23x faster                                                                    |
| scimark_sor              | 115 ms                                                          | 93.9 ms: 1.23x faster                                                                    |
| hexiom                   | 6.13 ms                                                         | 5.06 ms: 1.21x faster                                                                    |
| pycparser                | 1.04 sec                                                        | 863 ms: 1.21x faster                                                                     |
| generators               | 31.6 ms                                                         | 26.3 ms: 1.20x faster                                                                    |
| richards_super           | 49.9 ms                                                         | 41.8 ms: 1.19x faster                                                                    |
| thrift                   | 902 us                                                          | 758 us: 1.19x faster                                                                     |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                                    |
| float                    | 69.6 ms                                                         | 58.9 ms: 1.18x faster                                                                    |
| scimark_monte_carlo      | 61.9 ms                                                         | 52.7 ms: 1.17x faster                                                                    |
| pickle_pure_python       | 280 us                                                          | 242 us: 1.16x faster                                                                     |
| mako                     | 9.10 ms                                                         | 7.96 ms: 1.14x faster                                                                    |
| unpickle_pure_python     | 189 us                                                          | 166 us: 1.14x faster                                                                     |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                                                     |
| bench_thread_pool        | 1.12 ms                                                         | 994 us: 1.13x faster                                                                     |
| tornado_http             | 118 ms                                                          | 105 ms: 1.12x faster                                                                     |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.12x faster                                                                     |
| json                     | 4.76 ms                                                         | 4.28 ms: 1.11x faster                                                                    |
| regex_compile            | 117 ms                                                          | 105 ms: 1.11x faster                                                                     |
| json_loads               | 22.4 us                                                         | 20.3 us: 1.10x faster                                                                    |
| mdp                      | 1.83 sec                                                        | 1.69 sec: 1.08x faster                                                                   |
| html5lib                 | 52.1 ms                                                         | 48.2 ms: 1.08x faster                                                                    |
| richards                 | 40.3 ms                                                         | 37.3 ms: 1.08x faster                                                                    |
| nqueens                  | 87.1 ms                                                         | 80.9 ms: 1.08x faster                                                                    |
| sympy_integrate          | 16.6 ms                                                         | 15.6 ms: 1.07x faster                                                                    |
| spectral_norm            | 80.2 ms                                                         | 75.4 ms: 1.06x faster                                                                    |
| deepcopy_reduce          | 2.68 us                                                         | 2.53 us: 1.06x faster                                                                    |
| coroutines               | 17.9 ms                                                         | 17.1 ms: 1.05x faster                                                                    |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.6 ms: 1.05x faster                                                                    |
| fannkuch                 | 317 ms                                                          | 303 ms: 1.05x faster                                                                     |
| 2to3                     | 265 ms                                                          | 254 ms: 1.05x faster                                                                     |
| tomli_loads              | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                                   |
| sympy_str                | 229 ms                                                          | 221 ms: 1.04x faster                                                                     |
| asyncio_tcp              | 744 ms                                                          | 719 ms: 1.04x faster                                                                     |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                                   |
| meteor_contest           | 80.0 ms                                                         | 77.5 ms: 1.03x faster                                                                    |
| django_template          | 36.0 ms                                                         | 35.0 ms: 1.03x faster                                                                    |
| docutils                 | 1.95 sec                                                        | 1.90 sec: 1.02x faster                                                                   |
| regex_dna                | 131 ms                                                          | 128 ms: 1.02x faster                                                                     |
| xml_etree_process        | 48.1 ms                                                         | 47.2 ms: 1.02x faster                                                                    |
| pprint_safe_repr         | 658 ms                                                          | 648 ms: 1.02x faster                                                                     |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.29 ms: 1.01x slower                                                                    |
| sqlglot_normalize        | 230 ms                                                          | 235 ms: 1.02x slower                                                                     |
| sqlglot_optimize         | 44.7 ms                                                         | 45.7 ms: 1.02x slower                                                                    |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                                    |
| scimark_fft              | 216 ms                                                          | 223 ms: 1.03x slower                                                                     |
| python_startup           | 22.9 ms                                                         | 23.6 ms: 1.03x slower                                                                    |
| genshi_xml               | 46.6 ms                                                         | 48.2 ms: 1.04x slower                                                                    |
| xml_etree_generate       | 61.6 ms                                                         | 64.4 ms: 1.05x slower                                                                    |
| genshi_text              | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                                    |
| create_gc_cycles         | 694 us                                                          | 741 us: 1.07x slower                                                                     |
| bench_mp_pool            | 66.4 ms                                                         | 72.0 ms: 1.08x slower                                                                    |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                                    |
| pathlib                  | 81.2 ms                                                         | 88.6 ms: 1.09x slower                                                                    |
| logging_simple           | 7.29 us                                                         | 7.99 us: 1.10x slower                                                                    |
| logging_format           | 7.91 us                                                         | 8.72 us: 1.10x slower                                                                    |
| coverage                 | 46.6 ms                                                         | 51.5 ms: 1.11x slower                                                                    |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                                    |
| nbody                    | 79.1 ms                                                         | 90.3 ms: 1.14x slower                                                                    |
| async_generators         | 241 ms                                                          | 284 ms: 1.18x slower                                                                     |
| regex_effbot             | 1.66 ms                                                         | 1.98 ms: 1.19x slower                                                                    |
| telco                    | 4.83 ms                                                         | 6.37 ms: 1.32x slower                                                                    |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                             |

Benchmark hidden because not significant (2): sympy_expand, asyncio_tcp_ssl
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown