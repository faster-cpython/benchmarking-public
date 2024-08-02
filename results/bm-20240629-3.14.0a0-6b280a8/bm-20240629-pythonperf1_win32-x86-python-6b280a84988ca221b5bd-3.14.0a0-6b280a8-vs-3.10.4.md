# Results vs. 3.10.4

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-x86
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.07x faster
- HPT reliability: 92.68%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 263 ms: 1.01x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                         |
| html5lib       | 52.1 ms                                                         | 51.1 ms: 1.02x faster                                                          |
| tornado_http   | 118 ms                                                          | 98.3 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 494 ms: 1.87x faster                                                           |
| async_tree_none         | 394 ms                                                          | 240 ms: 1.64x faster                                                           |
| async_tree_io           | 940 ms                                                          | 577 ms: 1.63x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 292 ms: 1.60x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.68x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| float          | 69.6 ms                                                         | 67.9 ms: 1.03x faster                                                          |
| nbody          | 79.1 ms                                                         | 102 ms: 1.29x slower                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.91 ms: 1.24x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 106 ms: 1.13x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 70.0 ms: 1.01x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 285 us: 1.02x slower                                                           |
| unpickle_pure_python | 189 us                                                          | 193 us: 1.02x slower                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.97 sec: 1.03x slower                                                         |
| xml_etree_process    | 48.1 ms                                                         | 52.5 ms: 1.09x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 72.5 ms: 1.18x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.86 ms: 1.03x faster                                                          |
| django_template | 36.0 ms                                                         | 35.4 ms: 1.02x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 55.7 ms: 1.20x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 25.2 ms: 1.20x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.08x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 165 us: 2.40x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 494 ms: 1.87x faster                                                           |
| async_tree_none          | 394 ms                                                          | 240 ms: 1.64x faster                                                           |
| async_tree_io            | 940 ms                                                          | 577 ms: 1.63x faster                                                           |
| pylint                   | 384 ms                                                          | 237 ms: 1.62x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 292 ms: 1.60x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.90 ms: 1.39x faster                                                          |
| chaos                    | 74.4 ms                                                         | 58.2 ms: 1.28x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 64.5 ms: 1.26x faster                                                          |
| raytrace                 | 303 ms                                                          | 242 ms: 1.25x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.91 ms: 1.24x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 79.9 ns: 1.22x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 75.0 ms: 1.20x faster                                                          |
| tornado_http             | 118 ms                                                          | 98.3 ms: 1.20x faster                                                          |
| deepcopy                 | 310 us                                                          | 264 us: 1.17x faster                                                           |
| comprehensions           | 17.7 us                                                         | 15.2 us: 1.17x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 25.5 us: 1.16x faster                                                          |
| thrift                   | 902 us                                                          | 787 us: 1.15x faster                                                           |
| go                       | 146 ms                                                          | 128 ms: 1.14x faster                                                           |
| pycparser                | 1.04 sec                                                        | 913 ms: 1.14x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 106 ms: 1.13x faster                                                           |
| pyflate                  | 422 ms                                                          | 374 ms: 1.13x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 78.4 ms: 1.11x faster                                                          |
| richards_super           | 49.9 ms                                                         | 44.9 ms: 1.11x faster                                                          |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.20 ms: 1.10x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 674 ms: 1.10x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.56 ms: 1.10x faster                                                          |
| generators               | 31.6 ms                                                         | 28.6 ms: 1.10x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                          |
| scimark_sor              | 115 ms                                                          | 106 ms: 1.09x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.46 ms: 1.08x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.69 sec: 1.08x faster                                                         |
| json                     | 4.76 ms                                                         | 4.42 ms: 1.08x faster                                                          |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.07x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.86 ms: 1.03x faster                                                          |
| float                    | 69.6 ms                                                         | 67.9 ms: 1.03x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 16.3 ms: 1.02x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 51.1 ms: 1.02x faster                                                          |
| django_template          | 36.0 ms                                                         | 35.4 ms: 1.02x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 70.0 ms: 1.01x faster                                                          |
| 2to3                     | 265 ms                                                          | 263 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 79.8 ms: 1.01x faster                                                          |
| coroutines               | 17.9 ms                                                         | 18.1 ms: 1.01x slower                                                          |
| docutils                 | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                         |
| sympy_str                | 229 ms                                                          | 232 ms: 1.01x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.73 us: 1.02x slower                                                          |
| richards                 | 40.3 ms                                                         | 40.9 ms: 1.02x slower                                                          |
| pickle_pure_python       | 280 us                                                          | 285 us: 1.02x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 193 us: 1.02x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.97 sec: 1.03x slower                                                         |
| meteor_contest           | 80.0 ms                                                         | 82.6 ms: 1.03x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 84.3 ms: 1.04x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 46.9 ms: 1.05x slower                                                          |
| sympy_expand             | 391 ms                                                          | 410 ms: 1.05x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.45 sec: 1.06x slower                                                         |
| sqlglot_normalize        | 230 ms                                                          | 245 ms: 1.06x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 741 us: 1.07x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 71.3 ms: 1.07x slower                                                          |
| pprint_safe_repr         | 658 ms                                                          | 711 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.51 ms: 1.08x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 52.5 ms: 1.09x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                          |
| fannkuch                 | 317 ms                                                          | 349 ms: 1.10x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.56 us: 1.17x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 72.5 ms: 1.18x slower                                                          |
| logging_format           | 7.91 us                                                         | 9.35 us: 1.18x slower                                                          |
| scimark_fft              | 216 ms                                                          | 256 ms: 1.19x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 55.7 ms: 1.20x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 25.2 ms: 1.20x slower                                                          |
| async_generators         | 241 ms                                                          | 310 ms: 1.29x slower                                                           |
| nbody                    | 79.1 ms                                                         | 102 ms: 1.29x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.69 ms: 1.39x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.07x faster                                                                   |

Benchmark hidden because not significant (3): regex_compile, python_startup, scimark_monte_carlo
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 92.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown