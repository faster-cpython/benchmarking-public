# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 261 ms: 1.02x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.98 sec: 1.02x slower                                                         |
| html5lib       | 52.1 ms                                                         | 47.7 ms: 1.09x faster                                                          |
| tornado_http   | 118 ms                                                          | 107 ms: 1.10x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 479 ms: 1.92x faster                                                           |
| async_tree_io           | 940 ms                                                          | 546 ms: 1.72x faster                                                           |
| async_tree_none         | 394 ms                                                          | 229 ms: 1.72x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 288 ms: 1.62x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.74x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.57x faster                                                           |
| float          | 69.6 ms                                                         | 42.5 ms: 1.64x faster                                                          |
| nbody          | 79.1 ms                                                         | 52.6 ms: 1.50x faster                                                          |
| Geometric mean | (ref)                                                           | 1.85x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 96.1 ms: 1.21x faster                                                          |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 2.00 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.05 ms: 1.39x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 213 us: 1.32x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 147 us: 1.29x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.54 sec: 1.24x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.9 ms: 1.11x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 44.9 ms: 1.07x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 59.6 ms: 1.03x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.8 ms: 1.15x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                          |
| django_template | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 53.5 ms: 1.15x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 24.5 ms: 1.17x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 153 us: 2.58x faster                                                           |
| pidigits                 | 502 ms                                                          | 196 ms: 2.57x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 479 ms: 1.92x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 16.4 us: 1.80x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 46.9 ms: 1.73x faster                                                          |
| async_tree_io            | 940 ms                                                          | 546 ms: 1.72x faster                                                           |
| async_tree_none          | 394 ms                                                          | 229 ms: 1.72x faster                                                           |
| scimark_sor              | 115 ms                                                          | 67.0 ms: 1.72x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 58.2 ns: 1.68x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 47.9 ms: 1.68x faster                                                          |
| float                    | 69.6 ms                                                         | 42.5 ms: 1.64x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 288 ms: 1.62x faster                                                           |
| pyflate                  | 422 ms                                                          | 269 ms: 1.57x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.5 us: 1.54x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 59.7 ms: 1.50x faster                                                          |
| nbody                    | 79.1 ms                                                         | 52.6 ms: 1.50x faster                                                          |
| pylint                   | 384 ms                                                          | 257 ms: 1.49x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.8 ms: 1.48x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.75 ms: 1.47x faster                                                          |
| chaos                    | 74.4 ms                                                         | 51.6 ms: 1.44x faster                                                          |
| fannkuch                 | 317 ms                                                          | 227 ms: 1.40x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.32 ms: 1.40x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.05 ms: 1.39x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 973 us: 1.37x faster                                                           |
| raytrace                 | 303 ms                                                          | 227 ms: 1.33x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 213 us: 1.32x faster                                                           |
| pycparser                | 1.04 sec                                                        | 793 ms: 1.31x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 147 us: 1.29x faster                                                           |
| scimark_fft              | 216 ms                                                          | 168 ms: 1.29x faster                                                           |
| generators               | 31.6 ms                                                         | 24.7 ms: 1.28x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.84 ms: 1.27x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.25 ms: 1.27x faster                                                          |
| go                       | 146 ms                                                          | 115 ms: 1.26x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.54 sec: 1.24x faster                                                         |
| deepcopy                 | 310 us                                                          | 254 us: 1.22x faster                                                           |
| regex_compile            | 117 ms                                                          | 96.1 ms: 1.21x faster                                                          |
| richards_super           | 49.9 ms                                                         | 41.7 ms: 1.19x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.2 ms: 1.17x faster                                                          |
| thrift                   | 902 us                                                          | 774 us: 1.17x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 69.0 ms: 1.16x faster                                                          |
| richards                 | 40.3 ms                                                         | 35.1 ms: 1.15x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.20 sec: 1.14x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 77.2 ms: 1.13x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 586 ms: 1.12x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.9 ms: 1.11x faster                                                          |
| tornado_http             | 118 ms                                                          | 107 ms: 1.10x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                          |
| django_template          | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 47.7 ms: 1.09x faster                                                          |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.09x faster                                                           |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.69 sec: 1.08x faster                                                         |
| json                     | 4.76 ms                                                         | 4.43 ms: 1.08x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 44.9 ms: 1.07x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.54 us: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 222 ms: 1.03x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 59.6 ms: 1.03x faster                                                          |
| 2to3                     | 265 ms                                                          | 261 ms: 1.02x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.8 ms: 1.01x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 16.6 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| sqlglot_normalize        | 230 ms                                                          | 232 ms: 1.01x slower                                                           |
| sympy_expand             | 391 ms                                                          | 394 ms: 1.01x slower                                                           |
| docutils                 | 1.95 sec                                                        | 1.98 sec: 1.02x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.62 us: 1.04x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.36 us: 1.06x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 88.7 ms: 1.09x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 771 us: 1.11x slower                                                           |
| coverage                 | 46.6 ms                                                         | 51.8 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 53.5 ms: 1.15x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.8 ms: 1.15x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 77.3 ms: 1.16x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 24.5 ms: 1.17x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 2.00 ms: 1.21x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.01 ms: 1.24x slower                                                          |
| async_generators         | 241 ms                                                          | 320 ms: 1.33x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (2): sqlglot_optimize, asyncio_tcp
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown