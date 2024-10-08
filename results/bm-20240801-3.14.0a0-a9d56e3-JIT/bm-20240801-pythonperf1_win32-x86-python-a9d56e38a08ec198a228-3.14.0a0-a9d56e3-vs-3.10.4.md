# Results vs. 3.10.4

- fork: python
- ref: a9d56e38a08ec198a228
- machine: windows-x86
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                           |
| html5lib       | 52.1 ms                                                         | 46.8 ms: 1.11x faster                                                          |
| tornado_http   | 118 ms                                                          | 107 ms: 1.10x faster                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 466 ms: 1.98x faster                                                           |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.77x faster                                                           |
| async_tree_io           | 940 ms                                                          | 544 ms: 1.73x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 277 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                           |
| float          | 69.6 ms                                                         | 42.8 ms: 1.63x faster                                                          |
| nbody          | 79.1 ms                                                         | 52.2 ms: 1.52x faster                                                          |
| Geometric mean | (ref)                                                           | 1.84x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.5 ms: 1.23x faster                                                          |
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.06 ms: 1.39x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 209 us: 1.34x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 145 us: 1.31x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.13x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.6 ms: 1.11x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 44.0 ms: 1.09x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 59.1 ms: 1.04x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.19x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.38 ms: 1.69x faster                                                          |
| django_template | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 50.8 ms: 1.09x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.9 ms: 1.09x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 153 us: 2.59x faster                                                           |
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 466 ms: 1.98x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 16.0 us: 1.85x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 45.9 ms: 1.77x faster                                                          |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.77x faster                                                           |
| async_tree_io            | 940 ms                                                          | 544 ms: 1.73x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 56.8 ns: 1.72x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 47.3 ms: 1.70x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.38 ms: 1.69x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 277 ms: 1.69x faster                                                           |
| float                    | 69.6 ms                                                         | 42.8 ms: 1.63x faster                                                          |
| pyflate                  | 422 ms                                                          | 260 ms: 1.62x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.3 us: 1.58x faster                                                          |
| nbody                    | 79.1 ms                                                         | 52.2 ms: 1.52x faster                                                          |
| pylint                   | 384 ms                                                          | 253 ms: 1.52x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.2 ms: 1.50x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.71 ms: 1.49x faster                                                          |
| chaos                    | 74.4 ms                                                         | 52.5 ms: 1.42x faster                                                          |
| fannkuch                 | 317 ms                                                          | 224 ms: 1.42x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.31 ms: 1.40x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.06 ms: 1.39x faster                                                          |
| generators               | 31.6 ms                                                         | 22.9 ms: 1.38x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 988 us: 1.35x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 209 us: 1.34x faster                                                           |
| richards_super           | 49.9 ms                                                         | 37.4 ms: 1.33x faster                                                          |
| raytrace                 | 303 ms                                                          | 229 ms: 1.32x faster                                                           |
| pycparser                | 1.04 sec                                                        | 794 ms: 1.31x faster                                                           |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.69 ms: 1.31x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 145 us: 1.31x faster                                                           |
| scimark_fft              | 216 ms                                                          | 166 ms: 1.31x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                         |
| sqlglot_transpile        | 1.58 ms                                                         | 1.27 ms: 1.25x faster                                                          |
| deepcopy                 | 310 us                                                          | 251 us: 1.24x faster                                                           |
| regex_compile            | 117 ms                                                          | 94.5 ms: 1.23x faster                                                          |
| richards                 | 40.3 ms                                                         | 32.7 ms: 1.23x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 73.9 ms: 1.22x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 73.1 ms: 1.19x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.2 ms: 1.19x faster                                                          |
| thrift                   | 902 us                                                          | 769 us: 1.17x faster                                                           |
| scimark_sor              | 115 ms                                                          | 99.7 ms: 1.15x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 976 us: 1.15x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 70.4 ms: 1.14x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.13x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.22 sec: 1.12x faster                                                         |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 666 ms: 1.12x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.6 ms: 1.11x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.8 ms: 1.11x faster                                                          |
| sympy_sum                | 122 ms                                                          | 111 ms: 1.10x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 597 ms: 1.10x faster                                                           |
| tornado_http             | 118 ms                                                          | 107 ms: 1.10x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 44.0 ms: 1.09x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.49 us: 1.08x faster                                                          |
| json                     | 4.76 ms                                                         | 4.44 ms: 1.07x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.06x faster                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 59.1 ms: 1.04x faster                                                          |
| sympy_str                | 229 ms                                                          | 220 ms: 1.04x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.1 ms: 1.04x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 222 ms: 1.04x faster                                                           |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.4 ms: 1.01x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.8 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.72 us: 1.06x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.44 us: 1.07x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 88.6 ms: 1.09x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 50.8 ms: 1.09x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.9 ms: 1.09x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.0 ms: 1.09x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 764 us: 1.10x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.47 ms: 1.14x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 77.3 ms: 1.16x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.88 ms: 1.22x slower                                                          |
| async_generators         | 241 ms                                                          | 313 ms: 1.30x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (2): docutils, sympy_expand
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240801-3.14.0a0-a9d56e3-JIT/bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown