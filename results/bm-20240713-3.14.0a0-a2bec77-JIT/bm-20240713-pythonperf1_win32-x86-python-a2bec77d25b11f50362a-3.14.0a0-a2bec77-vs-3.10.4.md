# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-x86
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 253 ms: 1.05x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.0 ms: 1.11x faster                                                          |
| tornado_http   | 118 ms                                                          | 97.5 ms: 1.21x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 468 ms: 1.97x faster                                                           |
| async_tree_none         | 394 ms                                                          | 220 ms: 1.79x faster                                                           |
| async_tree_io           | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 272 ms: 1.72x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| float          | 69.6 ms                                                         | 43.9 ms: 1.59x faster                                                          |
| nbody          | 79.1 ms                                                         | 54.7 ms: 1.45x faster                                                          |
| Geometric mean | (ref)                                                           | 1.81x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 95.3 ms: 1.22x faster                                                          |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.15 ms: 1.37x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 209 us: 1.34x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 147 us: 1.29x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.9 ms: 1.14x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 46.5 ms: 1.03x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.1 ms: 1.01x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.44 ms: 1.67x faster                                                          |
| django_template | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 23.5 ms: 1.12x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 53.6 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 153 us: 2.58x faster                                                           |
| pidigits                 | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 468 ms: 1.97x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.3 us: 1.93x faster                                                          |
| async_tree_none          | 394 ms                                                          | 220 ms: 1.79x faster                                                           |
| async_tree_io            | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 272 ms: 1.72x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 47.2 ms: 1.70x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.0 ms: 1.69x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 58.4 ns: 1.68x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.44 ms: 1.67x faster                                                          |
| pylint                   | 384 ms                                                          | 241 ms: 1.59x faster                                                           |
| float                    | 69.6 ms                                                         | 43.9 ms: 1.59x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.5 us: 1.54x faster                                                          |
| pyflate                  | 422 ms                                                          | 277 ms: 1.53x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.69 ms: 1.50x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.3 ms: 1.46x faster                                                          |
| nbody                    | 79.1 ms                                                         | 54.7 ms: 1.45x faster                                                          |
| chaos                    | 74.4 ms                                                         | 52.3 ms: 1.42x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 956 us: 1.39x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.15 ms: 1.37x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.38 ms: 1.36x faster                                                          |
| fannkuch                 | 317 ms                                                          | 236 ms: 1.34x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 209 us: 1.34x faster                                                           |
| raytrace                 | 303 ms                                                          | 229 ms: 1.32x faster                                                           |
| deepcopy                 | 310 us                                                          | 237 us: 1.31x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.70 ms: 1.30x faster                                                          |
| scimark_fft              | 216 ms                                                          | 166 ms: 1.30x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.22 ms: 1.30x faster                                                          |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 147 us: 1.29x faster                                                           |
| richards_super           | 49.9 ms                                                         | 39.1 ms: 1.28x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                         |
| pycparser                | 1.04 sec                                                        | 845 ms: 1.23x faster                                                           |
| regex_compile            | 117 ms                                                          | 95.3 ms: 1.22x faster                                                          |
| tornado_http             | 118 ms                                                          | 97.5 ms: 1.21x faster                                                          |
| richards                 | 40.3 ms                                                         | 33.7 ms: 1.19x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 73.3 ms: 1.19x faster                                                          |
| thrift                   | 902 us                                                          | 760 us: 1.19x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.16 sec: 1.18x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 565 ms: 1.16x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.16x faster                                                           |
| generators               | 31.6 ms                                                         | 27.6 ms: 1.14x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.9 ms: 1.14x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 983 us: 1.14x faster                                                           |
| json                     | 4.76 ms                                                         | 4.20 ms: 1.13x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.41 us: 1.11x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 47.0 ms: 1.11x faster                                                          |
| scimark_sor              | 115 ms                                                          | 104 ms: 1.11x faster                                                           |
| sympy_sum                | 122 ms                                                          | 111 ms: 1.10x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 82.6 ms: 1.09x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.08x faster                                                         |
| django_template          | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 75.1 ms: 1.07x faster                                                          |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                           |
| 2to3                     | 265 ms                                                          | 253 ms: 1.05x faster                                                           |
| sympy_str                | 229 ms                                                          | 220 ms: 1.04x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 46.5 ms: 1.03x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 44.4 ms: 1.01x faster                                                          |
| sympy_expand             | 391 ms                                                          | 393 ms: 1.01x slower                                                           |
| python_startup           | 22.9 ms                                                         | 23.1 ms: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.0 ms: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.56 us: 1.04x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.21 us: 1.04x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 241 ms: 1.05x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 757 us: 1.09x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.31 ms: 1.10x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.7 ms: 1.11x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.0 ms: 1.12x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 23.5 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 53.6 ms: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| async_generators         | 241 ms                                                          | 307 ms: 1.27x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                                   |

Benchmark hidden because not significant (4): asyncio_tcp, asyncio_tcp_ssl, xml_etree_generate, coroutines
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown