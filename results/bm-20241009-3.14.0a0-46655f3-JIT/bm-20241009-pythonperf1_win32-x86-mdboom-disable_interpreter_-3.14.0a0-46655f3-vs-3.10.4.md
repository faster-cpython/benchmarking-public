# Results vs. 3.10.4

- fork: mdboom
- ref: disable_interpreter_
- machine: windows-x86
- commit hash: 46655f3
- commit date: 2024-10-09
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 262 ms: 1.01x faster                                                           |
| docutils       | 1.95 sec                                                        | 2.05 sec: 1.05x slower                                                         |
| html5lib       | 52.1 ms                                                         | 45.3 ms: 1.15x faster                                                          |
| tornado_http   | 118 ms                                                          | 108 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 494 ms: 1.87x faster                                                           |
| async_tree_none         | 394 ms                                                          | 219 ms: 1.80x faster                                                           |
| async_tree_io           | 940 ms                                                          | 539 ms: 1.75x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 274 ms: 1.71x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 205 ms: 2.45x faster                                                           |
| float          | 69.6 ms                                                         | 45.3 ms: 1.54x faster                                                          |
| nbody          | 79.1 ms                                                         | 52.9 ms: 1.50x faster                                                          |
| Geometric mean | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 114 ms: 1.14x faster                                                           |
| regex_compile  | 117 ms                                                          | 106 ms: 1.10x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.84 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.79 ms: 1.45x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 159 us: 1.19x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 40.6 ms: 1.18x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 54.1 ms: 1.14x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 250 us: 1.12x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.2 us: 1.06x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.92 us: 1.02x faster                                                          |
| pickle_list          | 3.22 us                                                         | 3.44 us: 1.07x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.6 us: 1.08x slower                                                          |
| pickle               | 7.83 us                                                         | 8.46 us: 1.08x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 21.6 us: 1.18x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.4 ms: 1.06x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.69 ms: 1.60x faster                                                          |
| django_template | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 23.4 ms: 1.12x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 54.6 ms: 1.17x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 145 us: 2.73x faster                                                           |
| pidigits                 | 502 ms                                                          | 205 ms: 2.45x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 104 ms: 2.22x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.03 ms: 1.98x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 15.2 us: 1.95x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 494 ms: 1.87x faster                                                           |
| async_tree_none          | 394 ms                                                          | 219 ms: 1.80x faster                                                           |
| async_tree_io            | 940 ms                                                          | 539 ms: 1.75x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 56.7 ns: 1.73x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 274 ms: 1.71x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 47.8 ms: 1.70x faster                                                          |
| scimark_sor              | 115 ms                                                          | 69.6 ms: 1.65x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.69 ms: 1.60x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 50.9 ms: 1.58x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 57.9 ms: 1.55x faster                                                          |
| float                    | 69.6 ms                                                         | 45.3 ms: 1.54x faster                                                          |
| nbody                    | 79.1 ms                                                         | 52.9 ms: 1.50x faster                                                          |
| comprehensions           | 17.7 us                                                         | 12.1 us: 1.47x faster                                                          |
| pyflate                  | 422 ms                                                          | 288 ms: 1.46x faster                                                           |
| go                       | 146 ms                                                          | 100 ms: 1.45x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.79 ms: 1.45x faster                                                          |
| chaos                    | 74.4 ms                                                         | 53.9 ms: 1.38x faster                                                          |
| pylint                   | 384 ms                                                          | 281 ms: 1.36x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.41 ms: 1.34x faster                                                          |
| deepcopy                 | 310 us                                                          | 232 us: 1.33x faster                                                           |
| richards_super           | 49.9 ms                                                         | 37.4 ms: 1.33x faster                                                          |
| fannkuch                 | 317 ms                                                          | 239 ms: 1.33x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 46.8 ms: 1.32x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.30x faster                                                          |
| generators               | 31.6 ms                                                         | 24.4 ms: 1.29x faster                                                          |
| scimark_fft              | 216 ms                                                          | 170 ms: 1.27x faster                                                           |
| pycparser                | 1.04 sec                                                        | 824 ms: 1.26x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                         |
| sqlite_synth             | 2.29 us                                                         | 1.89 us: 1.22x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.08 ms: 1.21x faster                                                          |
| raytrace                 | 303 ms                                                          | 253 ms: 1.19x faster                                                           |
| thrift                   | 902 us                                                          | 756 us: 1.19x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 159 us: 1.19x faster                                                           |
| richards                 | 40.3 ms                                                         | 33.8 ms: 1.19x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 40.6 ms: 1.18x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 75.1 ms: 1.16x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 572 ms: 1.15x faster                                                           |
| json                     | 4.76 ms                                                         | 4.14 ms: 1.15x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.19 sec: 1.15x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 45.3 ms: 1.15x faster                                                          |
| regex_dna                | 131 ms                                                          | 114 ms: 1.14x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 54.1 ms: 1.14x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.39 us: 1.12x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 250 us: 1.12x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                          |
| django_template          | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| regex_compile            | 117 ms                                                          | 106 ms: 1.10x faster                                                           |
| tornado_http             | 118 ms                                                          | 108 ms: 1.08x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 74.3 ms: 1.08x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.07x faster                                                         |
| json_loads               | 22.4 us                                                         | 21.2 us: 1.06x faster                                                          |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.04x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.92 us: 1.02x faster                                                          |
| 2to3                     | 265 ms                                                          | 262 ms: 1.01x faster                                                           |
| sympy_str                | 229 ms                                                          | 230 ms: 1.01x slower                                                           |
| coroutines               | 17.9 ms                                                         | 18.1 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.4 sec: 1.03x slower                                                         |
| sympy_expand             | 391 ms                                                          | 403 ms: 1.03x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.05 sec: 1.05x slower                                                         |
| logging_simple           | 7.29 us                                                         | 7.69 us: 1.05x slower                                                          |
| sympy_integrate          | 16.6 ms                                                         | 17.6 ms: 1.06x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.36 us: 1.06x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.4 ms: 1.06x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.44 us: 1.07x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 42.8 ns: 1.07x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.6 us: 1.08x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.46 us: 1.08x slower                                                          |
| asyncio_tcp              | 744 ms                                                          | 809 ms: 1.09x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 88.4 ms: 1.09x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.84 ms: 1.10x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 23.4 ms: 1.12x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 50.1 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 784 us: 1.13x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 54.6 ms: 1.17x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 77.8 ms: 1.17x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 21.6 us: 1.18x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.02 ms: 1.25x slower                                                          |
| async_generators         | 241 ms                                                          | 326 ms: 1.35x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.19x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241009-3.14.0a0-46655f3-JIT/bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown