# Results vs. 3.10.4

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-x86
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| chameleon      | 6.42 ms                                                         | 6.16 ms: 1.04x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 45.5 ms: 1.14x faster                                                          |
| tornado_http   | 118 ms                                                          | 97.0 ms: 1.21x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 479 ms: 1.93x faster                                                           |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                           |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.73x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.56x faster                                                           |
| float          | 69.6 ms                                                         | 41.1 ms: 1.69x faster                                                          |
| nbody          | 79.1 ms                                                         | 55.2 ms: 1.43x faster                                                          |
| Geometric mean | (ref)                                                           | 1.84x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 92.2 ms: 1.26x faster                                                          |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.53 ms: 1.50x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 202 us: 1.39x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 137 us: 1.38x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 40.2 ms: 1.20x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.8 ms: 1.15x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 55.3 ms: 1.11x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.73 us: 1.09x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.06x faster                                                          |
| pickle               | 7.83 us                                                         | 8.19 us: 1.05x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.54 us: 1.10x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.4 ms: 1.06x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.31 ms: 1.72x faster                                                          |
| django_template | 36.0 ms                                                         | 32.0 ms: 1.13x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 52.3 ms: 1.12x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 140 us: 2.82x faster                                                           |
| pidigits                 | 502 ms                                                          | 197 ms: 2.56x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 479 ms: 1.93x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 54.7 ns: 1.79x faster                                                          |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                           |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.73x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.31 ms: 1.72x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 47.2 ms: 1.70x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 47.9 ms: 1.70x faster                                                          |
| float                    | 69.6 ms                                                         | 41.1 ms: 1.69x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                           |
| comprehensions           | 17.7 us                                                         | 10.8 us: 1.65x faster                                                          |
| pylint                   | 384 ms                                                          | 240 ms: 1.60x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.53 ms: 1.60x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.53 ms: 1.50x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.2 ms: 1.50x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 903 us: 1.47x faster                                                           |
| raytrace                 | 303 ms                                                          | 208 ms: 1.45x faster                                                           |
| chaos                    | 74.4 ms                                                         | 51.5 ms: 1.44x faster                                                          |
| fannkuch                 | 317 ms                                                          | 220 ms: 1.44x faster                                                           |
| nbody                    | 79.1 ms                                                         | 55.2 ms: 1.43x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 20.8 us: 1.42x faster                                                          |
| richards_super           | 49.9 ms                                                         | 35.7 ms: 1.40x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 202 us: 1.39x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.34 ms: 1.38x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 137 us: 1.38x faster                                                           |
| pyflate                  | 422 ms                                                          | 306 ms: 1.38x faster                                                           |
| go                       | 146 ms                                                          | 106 ms: 1.37x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                         |
| generators               | 31.6 ms                                                         | 23.2 ms: 1.36x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.16 ms: 1.36x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.53 ms: 1.35x faster                                                          |
| pycparser                | 1.04 sec                                                        | 781 ms: 1.33x faster                                                           |
| richards                 | 40.3 ms                                                         | 31.3 ms: 1.29x faster                                                          |
| scimark_sor              | 115 ms                                                          | 89.6 ms: 1.29x faster                                                          |
| scimark_fft              | 216 ms                                                          | 168 ms: 1.28x faster                                                           |
| regex_compile            | 117 ms                                                          | 92.2 ms: 1.26x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 69.2 ms: 1.26x faster                                                          |
| thrift                   | 902 us                                                          | 734 us: 1.23x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.88 us: 1.22x faster                                                          |
| tornado_http             | 118 ms                                                          | 97.0 ms: 1.21x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 40.2 ms: 1.20x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 76.0 ms: 1.18x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.16 sec: 1.18x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 560 ms: 1.18x faster                                                           |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.15x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.15x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.8 ms: 1.15x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 45.5 ms: 1.14x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 991 us: 1.13x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.0 ms: 1.13x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.63 sec: 1.12x faster                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 55.3 ms: 1.11x faster                                                          |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| sympy_str                | 229 ms                                                          | 208 ms: 1.10x faster                                                           |
| json                     | 4.76 ms                                                         | 4.34 ms: 1.10x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 73.3 ms: 1.09x faster                                                          |
| unpickle_list            | 2.98 us                                                         | 2.73 us: 1.09x faster                                                          |
| coroutines               | 17.9 ms                                                         | 16.5 ms: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.07x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 41.7 ms: 1.07x faster                                                          |
| 2to3                     | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.06x faster                                                          |
| sympy_expand             | 391 ms                                                          | 369 ms: 1.06x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 711 ms: 1.05x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 220 ms: 1.05x faster                                                           |
| chameleon                | 6.42 ms                                                         | 6.16 ms: 1.04x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                         |
| deepcopy                 | 310 us                                                          | 302 us: 1.03x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.67 us: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                         |
| logging_simple           | 7.29 us                                                         | 7.37 us: 1.01x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.03 us: 1.02x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.19 us: 1.05x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.4 ms: 1.06x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 751 us: 1.08x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 87.9 ms: 1.08x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.2 ms: 1.10x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.54 us: 1.10x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 52.3 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 75.1 ms: 1.13x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.13x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                          |
| async_generators         | 241 ms                                                          | 285 ms: 1.18x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.72 ms: 1.19x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown