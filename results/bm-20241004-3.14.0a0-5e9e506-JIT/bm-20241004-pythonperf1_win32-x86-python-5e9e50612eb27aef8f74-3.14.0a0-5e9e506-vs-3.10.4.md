# Results vs. 3.10.4

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-x86
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 261 ms: 1.02x faster                                                           |
| docutils       | 1.95 sec                                                        | 2.04 sec: 1.05x slower                                                         |
| html5lib       | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                          |
| tornado_http   | 118 ms                                                          | 109 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 468 ms: 1.97x faster                                                           |
| async_tree_io           | 940 ms                                                          | 524 ms: 1.79x faster                                                           |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.77x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 279 ms: 1.67x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                           |
| nbody          | 79.1 ms                                                         | 50.4 ms: 1.57x faster                                                          |
| float          | 69.6 ms                                                         | 46.2 ms: 1.51x faster                                                          |
| Geometric mean | (ref)                                                           | 1.82x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                           |
| regex_compile  | 117 ms                                                          | 105 ms: 1.12x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.3 ms: 1.03x faster                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.98 ms: 1.41x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 158 us: 1.20x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 41.5 ms: 1.16x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 242 us: 1.16x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 54.7 ms: 1.13x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.5 ms: 1.10x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.93 us: 1.02x faster                                                          |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.05x slower                                                          |
| pickle               | 7.83 us                                                         | 8.37 us: 1.07x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.47 us: 1.08x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 21.3 us: 1.17x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.5 ms: 1.13x slower                                                          |
| python_startup         | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.57 ms: 1.63x faster                                                          |
| django_template | 36.0 ms                                                         | 32.0 ms: 1.13x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 23.8 ms: 1.14x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 56.2 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.84x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 102 ms: 2.25x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 468 ms: 1.97x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 16.0 us: 1.85x faster                                                          |
| async_tree_io            | 940 ms                                                          | 524 ms: 1.79x faster                                                           |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.77x faster                                                           |
| scimark_sor              | 115 ms                                                          | 68.5 ms: 1.68x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 279 ms: 1.67x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 58.6 ns: 1.67x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.57 ms: 1.63x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.0 ms: 1.59x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 51.2 ms: 1.59x faster                                                          |
| nbody                    | 79.1 ms                                                         | 50.4 ms: 1.57x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.63 ms: 1.54x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 59.1 ms: 1.52x faster                                                          |
| float                    | 69.6 ms                                                         | 46.2 ms: 1.51x faster                                                          |
| go                       | 146 ms                                                          | 97.1 ms: 1.50x faster                                                          |
| comprehensions           | 17.7 us                                                         | 12.3 us: 1.45x faster                                                          |
| chaos                    | 74.4 ms                                                         | 52.4 ms: 1.42x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.98 ms: 1.41x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 58.4 ms: 1.37x faster                                                          |
| pylint                   | 384 ms                                                          | 282 ms: 1.36x faster                                                           |
| deepcopy                 | 310 us                                                          | 234 us: 1.32x faster                                                           |
| pyflate                  | 422 ms                                                          | 325 ms: 1.30x faster                                                           |
| fannkuch                 | 317 ms                                                          | 245 ms: 1.29x faster                                                           |
| pycparser                | 1.04 sec                                                        | 822 ms: 1.27x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                         |
| sqlglot_parse            | 1.33 ms                                                         | 1.07 ms: 1.25x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.60 ms: 1.24x faster                                                          |
| scimark_fft              | 216 ms                                                          | 177 ms: 1.22x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.89 us: 1.21x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 158 us: 1.20x faster                                                           |
| raytrace                 | 303 ms                                                          | 255 ms: 1.19x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 73.9 ms: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                          |
| thrift                   | 902 us                                                          | 774 us: 1.17x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 565 ms: 1.16x faster                                                           |
| generators               | 31.6 ms                                                         | 27.1 ms: 1.16x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.37 ms: 1.16x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 41.5 ms: 1.16x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.18 sec: 1.16x faster                                                         |
| pickle_pure_python       | 280 us                                                          | 242 us: 1.16x faster                                                           |
| json                     | 4.76 ms                                                         | 4.22 ms: 1.13x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 54.7 ms: 1.13x faster                                                          |
| django_template          | 36.0 ms                                                         | 32.0 ms: 1.13x faster                                                          |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.48 ms: 1.12x faster                                                          |
| regex_compile            | 117 ms                                                          | 105 ms: 1.12x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.43 us: 1.11x faster                                                          |
| richards_super           | 49.9 ms                                                         | 45.2 ms: 1.10x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.5 ms: 1.10x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.09x faster                                                          |
| tornado_http             | 118 ms                                                          | 109 ms: 1.08x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.07x faster                                                         |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 75.0 ms: 1.07x faster                                                          |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.04x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.3 ms: 1.03x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.5 ms: 1.02x faster                                                          |
| unpickle_list            | 2.98 us                                                         | 2.93 us: 1.02x faster                                                          |
| 2to3                     | 265 ms                                                          | 261 ms: 1.02x faster                                                           |
| sympy_str                | 229 ms                                                          | 227 ms: 1.01x faster                                                           |
| richards                 | 40.3 ms                                                         | 39.9 ms: 1.01x faster                                                          |
| sympy_expand             | 391 ms                                                          | 394 ms: 1.01x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 40.5 ns: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.3 sec: 1.02x slower                                                         |
| sympy_integrate          | 16.6 ms                                                         | 17.1 ms: 1.03x slower                                                          |
| asyncio_tcp              | 744 ms                                                          | 771 ms: 1.04x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.04 sec: 1.05x slower                                                         |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.05x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.37 us: 1.07x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.52 us: 1.08x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.47 us: 1.08x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.8 ms: 1.08x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.02 us: 1.10x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 49.7 ms: 1.11x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.5 ms: 1.13x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 23.8 ms: 1.14x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.5 ms: 1.15x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 21.3 us: 1.17x slower                                                          |
| python_startup           | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 56.2 ms: 1.21x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.42 ms: 1.33x slower                                                          |
| async_generators         | 241 ms                                                          | 326 ms: 1.35x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 94.3 ms: 1.42x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 1.16 ms: 1.67x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.17x faster                                                                   |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown