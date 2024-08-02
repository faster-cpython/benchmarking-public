# Results vs. base

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.01x faster
- HPT reliability: 89.59%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                                                                                   | 248 ms: 1.06x slower                                                                                                         |
| chameleon      | 5.72 ms                                                                                                                  | 6.16 ms: 1.08x slower                                                                                                        |
| docutils       | 1.81 sec                                                                                                                 | 1.88 sec: 1.04x slower                                                                                                       |
| html5lib       | 45.0 ms                                                                                                                  | 45.1 ms: 1.00x slower                                                                                                        |
| tornado_http   | 94.8 ms                                                                                                                  | 96.9 ms: 1.02x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                    | 1.04x slower                                                                                                                 |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 76.4 ms                                                                                                                  | 52.6 ms: 1.45x faster                                                                                                        |
| float          | 52.6 ms                                                                                                                  | 41.8 ms: 1.26x faster                                                                                                        |
| pidigits       | 199 ms                                                                                                                   | 195 ms: 1.02x faster                                                                                                         |
| Geometric mean | (ref)                                                                                                                    | 1.23x faster                                                                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 98.9 ms                                                                                                                  | 98.3 ms: 1.01x faster                                                                                                        |
| regex_dna      | 116 ms                                                                                                                   | 118 ms: 1.01x slower                                                                                                         |
| regex_effbot   | 1.89 ms                                                                                                                  | 1.98 ms: 1.05x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                    | 1.01x slower                                                                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.60 sec                                                                                                                 | 1.41 sec: 1.14x faster                                                                                                       |
| pickle_pure_python   | 221 us                                                                                                                   | 201 us: 1.10x faster                                                                                                         |
| unpickle_pure_python | 148 us                                                                                                                   | 135 us: 1.10x faster                                                                                                         |
| xml_etree_generate   | 60.0 ms                                                                                                                  | 55.7 ms: 1.08x faster                                                                                                        |
| xml_etree_iterparse  | 63.8 ms                                                                                                                  | 61.0 ms: 1.05x faster                                                                                                        |
| xml_etree_process    | 42.9 ms                                                                                                                  | 41.1 ms: 1.04x faster                                                                                                        |
| unpickle_list        | 2.97 us                                                                                                                  | 2.88 us: 1.03x faster                                                                                                        |
| json_dumps           | 6.95 ms                                                                                                                  | 6.76 ms: 1.03x faster                                                                                                        |
| xml_etree_parse      | 105 ms                                                                                                                   | 103 ms: 1.02x faster                                                                                                         |
| pickle_list          | 3.63 us                                                                                                                  | 3.57 us: 1.02x faster                                                                                                        |
| pickle_dict          | 20.9 us                                                                                                                  | 20.5 us: 1.02x faster                                                                                                        |
| unpickle             | 10.4 us                                                                                                                  | 10.3 us: 1.01x faster                                                                                                        |
| json_loads           | 20.9 us                                                                                                                  | 20.8 us: 1.01x faster                                                                                                        |
| Geometric mean       | (ref)                                                                                                                    | 1.05x faster                                                                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|------------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 22.8 ms                                                                                                                  | 24.8 ms: 1.09x slower                                                                                                        |
| python_startup_no_site | 18.6 ms                                                                                                                  | 20.5 ms: 1.10x slower                                                                                                        |
| Geometric mean         | (ref)                                                                                                                    | 1.09x slower                                                                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|-----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                                                                                  | 5.29 ms: 1.31x faster                                                                                                        |
| django_template | 30.4 ms                                                                                                                  | 32.3 ms: 1.06x slower                                                                                                        |
| genshi_text     | 19.1 ms                                                                                                                  | 21.4 ms: 1.12x slower                                                                                                        |
| genshi_xml      | 44.2 ms                                                                                                                  | 51.3 ms: 1.16x slower                                                                                                        |
| Geometric mean  | (ref)                                                                                                                    | 1.01x slower                                                                                                                 |

All benchmarks:
===============

| Benchmark                | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|--------------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 76.4 ms                                                                                                                  | 52.6 ms: 1.45x faster                                                                                                        |
| spectral_norm            | 66.2 ms                                                                                                                  | 47.6 ms: 1.39x faster                                                                                                        |
| mako                     | 6.94 ms                                                                                                                  | 5.29 ms: 1.31x faster                                                                                                        |
| float                    | 52.6 ms                                                                                                                  | 41.8 ms: 1.26x faster                                                                                                        |
| fannkuch                 | 269 ms                                                                                                                   | 225 ms: 1.20x faster                                                                                                         |
| scimark_sparse_mat_mult  | 2.80 ms                                                                                                                  | 2.36 ms: 1.19x faster                                                                                                        |
| deepcopy_memo            | 23.5 us                                                                                                                  | 20.6 us: 1.14x faster                                                                                                        |
| tomli_loads              | 1.60 sec                                                                                                                 | 1.41 sec: 1.14x faster                                                                                                       |
| scimark_monte_carlo      | 46.3 ms                                                                                                                  | 40.9 ms: 1.13x faster                                                                                                        |
| telco                    | 6.20 ms                                                                                                                  | 5.51 ms: 1.13x faster                                                                                                        |
| asyncio_tcp              | 674 ms                                                                                                                   | 608 ms: 1.11x faster                                                                                                         |
| pickle_pure_python       | 221 us                                                                                                                   | 201 us: 1.10x faster                                                                                                         |
| scimark_fft              | 203 ms                                                                                                                   | 185 ms: 1.10x faster                                                                                                         |
| unpickle_pure_python     | 148 us                                                                                                                   | 135 us: 1.10x faster                                                                                                         |
| crypto_pyaes             | 54.4 ms                                                                                                                  | 49.7 ms: 1.10x faster                                                                                                        |
| pprint_pformat           | 1.25 sec                                                                                                                 | 1.15 sec: 1.09x faster                                                                                                       |
| pprint_safe_repr         | 607 ms                                                                                                                   | 562 ms: 1.08x faster                                                                                                         |
| xml_etree_generate       | 60.0 ms                                                                                                                  | 55.7 ms: 1.08x faster                                                                                                        |
| comprehensions           | 11.9 us                                                                                                                  | 11.1 us: 1.08x faster                                                                                                        |
| sqlglot_parse            | 965 us                                                                                                                   | 908 us: 1.06x faster                                                                                                         |
| xml_etree_iterparse      | 63.8 ms                                                                                                                  | 61.0 ms: 1.05x faster                                                                                                        |
| xml_etree_process        | 42.9 ms                                                                                                                  | 41.1 ms: 1.04x faster                                                                                                        |
| sqlite_synth             | 1.94 us                                                                                                                  | 1.87 us: 1.04x faster                                                                                                        |
| logging_format           | 8.19 us                                                                                                                  | 7.93 us: 1.03x faster                                                                                                        |
| unpickle_list            | 2.97 us                                                                                                                  | 2.88 us: 1.03x faster                                                                                                        |
| json_dumps               | 6.95 ms                                                                                                                  | 6.76 ms: 1.03x faster                                                                                                        |
| pidigits                 | 199 ms                                                                                                                   | 195 ms: 1.02x faster                                                                                                         |
| meteor_contest           | 74.4 ms                                                                                                                  | 72.9 ms: 1.02x faster                                                                                                        |
| xml_etree_parse          | 105 ms                                                                                                                   | 103 ms: 1.02x faster                                                                                                         |
| pickle_list              | 3.63 us                                                                                                                  | 3.57 us: 1.02x faster                                                                                                        |
| pickle_dict              | 20.9 us                                                                                                                  | 20.5 us: 1.02x faster                                                                                                        |
| logging_simple           | 7.47 us                                                                                                                  | 7.35 us: 1.02x faster                                                                                                        |
| sqlglot_transpile        | 1.19 ms                                                                                                                  | 1.17 ms: 1.02x faster                                                                                                        |
| pathlib                  | 87.5 ms                                                                                                                  | 86.4 ms: 1.01x faster                                                                                                        |
| unpickle                 | 10.4 us                                                                                                                  | 10.3 us: 1.01x faster                                                                                                        |
| regex_compile            | 98.9 ms                                                                                                                  | 98.3 ms: 1.01x faster                                                                                                        |
| json_loads               | 20.9 us                                                                                                                  | 20.8 us: 1.01x faster                                                                                                        |
| flaskblogging            | 2.03 sec                                                                                                                 | 2.03 sec: 1.00x slower                                                                                                       |
| html5lib                 | 45.0 ms                                                                                                                  | 45.1 ms: 1.00x slower                                                                                                        |
| regex_dna                | 116 ms                                                                                                                   | 118 ms: 1.01x slower                                                                                                         |
| gc_traversal             | 1.44 ms                                                                                                                  | 1.47 ms: 1.02x slower                                                                                                        |
| coroutines               | 15.9 ms                                                                                                                  | 16.2 ms: 1.02x slower                                                                                                        |
| create_gc_cycles         | 750 us                                                                                                                   | 765 us: 1.02x slower                                                                                                         |
| tornado_http             | 94.8 ms                                                                                                                  | 96.9 ms: 1.02x slower                                                                                                        |
| pycparser                | 788 ms                                                                                                                   | 811 ms: 1.03x slower                                                                                                         |
| coverage                 | 48.4 ms                                                                                                                  | 49.9 ms: 1.03x slower                                                                                                        |
| sympy_str                | 206 ms                                                                                                                   | 212 ms: 1.03x slower                                                                                                         |
| typing_runtime_protocols | 133 us                                                                                                                   | 137 us: 1.03x slower                                                                                                         |
| docutils                 | 1.81 sec                                                                                                                 | 1.88 sec: 1.04x slower                                                                                                       |
| thrift                   | 682 us                                                                                                                   | 710 us: 1.04x slower                                                                                                         |
| sympy_sum                | 104 ms                                                                                                                   | 108 ms: 1.04x slower                                                                                                         |
| richards                 | 30.5 ms                                                                                                                  | 31.9 ms: 1.05x slower                                                                                                        |
| nqueens                  | 66.5 ms                                                                                                                  | 69.6 ms: 1.05x slower                                                                                                        |
| sympy_expand             | 361 ms                                                                                                                   | 379 ms: 1.05x slower                                                                                                         |
| richards_super           | 34.2 ms                                                                                                                  | 35.9 ms: 1.05x slower                                                                                                        |
| regex_effbot             | 1.89 ms                                                                                                                  | 1.98 ms: 1.05x slower                                                                                                        |
| bench_mp_pool            | 71.2 ms                                                                                                                  | 75.4 ms: 1.06x slower                                                                                                        |
| hexiom                   | 4.33 ms                                                                                                                  | 4.58 ms: 1.06x slower                                                                                                        |
| django_template          | 30.4 ms                                                                                                                  | 32.3 ms: 1.06x slower                                                                                                        |
| scimark_sor              | 85.0 ms                                                                                                                  | 90.3 ms: 1.06x slower                                                                                                        |
| 2to3                     | 233 ms                                                                                                                   | 248 ms: 1.06x slower                                                                                                         |
| deepcopy_reduce          | 2.66 us                                                                                                                  | 2.84 us: 1.07x slower                                                                                                        |
| sympy_integrate          | 14.6 ms                                                                                                                  | 15.6 ms: 1.07x slower                                                                                                        |
| sqlglot_optimize         | 39.6 ms                                                                                                                  | 42.5 ms: 1.07x slower                                                                                                        |
| chameleon                | 5.72 ms                                                                                                                  | 6.16 ms: 1.08x slower                                                                                                        |
| go                       | 104 ms                                                                                                                   | 113 ms: 1.08x slower                                                                                                         |
| python_startup           | 22.8 ms                                                                                                                  | 24.8 ms: 1.09x slower                                                                                                        |
| generators               | 21.5 ms                                                                                                                  | 23.4 ms: 1.09x slower                                                                                                        |
| async_generators         | 271 ms                                                                                                                   | 296 ms: 1.09x slower                                                                                                         |
| sqlglot_normalize        | 204 ms                                                                                                                   | 222 ms: 1.09x slower                                                                                                         |
| deepcopy                 | 283 us                                                                                                                   | 310 us: 1.10x slower                                                                                                         |
| chaos                    | 46.7 ms                                                                                                                  | 51.4 ms: 1.10x slower                                                                                                        |
| python_startup_no_site   | 18.6 ms                                                                                                                  | 20.5 ms: 1.10x slower                                                                                                        |
| pylint                   | 218 ms                                                                                                                   | 241 ms: 1.11x slower                                                                                                         |
| genshi_text              | 19.1 ms                                                                                                                  | 21.4 ms: 1.12x slower                                                                                                        |
| deltablue                | 2.26 ms                                                                                                                  | 2.57 ms: 1.14x slower                                                                                                        |
| raytrace                 | 185 ms                                                                                                                   | 211 ms: 1.14x slower                                                                                                         |
| genshi_xml               | 44.2 ms                                                                                                                  | 51.3 ms: 1.16x slower                                                                                                        |
| scimark_lu               | 58.3 ms                                                                                                                  | 72.1 ms: 1.24x slower                                                                                                        |
| Geometric mean           | (ref)                                                                                                                    | 1.01x faster                                                                                                                 |

Benchmark hidden because not significant (16): json, logging_silent, async_tree_none_tg, pickle, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, asyncio_tcp_ssl, regex_v8, async_tree_memoization, mdp, pyflate, bench_thread_pool, async_tree_cpu_io_mixed_tg, async_tree_io

# HPT report

- Reliability score: 89.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown