# Results vs. 3.10.4

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-x86
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.127x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 250 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.8 ms: 1.11x faster                                                          |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 464 ms: 1.99x faster                                                           |
| async_tree_none         | 394 ms                                                          | 213 ms: 1.85x faster                                                           |
| async_tree_io           | 940 ms                                                          | 531 ms: 1.77x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.83x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| float          | 69.6 ms                                                         | 62.3 ms: 1.12x faster                                                          |
| nbody          | 79.1 ms                                                         | 96.4 ms: 1.22x slower                                                          |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                           |
| regex_dna      | 131 ms                                                          | 124 ms: 1.05x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.60 ms: 1.29x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.12x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 174 us: 1.09x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 262 us: 1.07x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.6 ms: 1.05x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.92 sec: 1.01x slower                                                         |
| xml_etree_process    | 48.1 ms                                                         | 50.6 ms: 1.05x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 68.1 ms: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| mako            | 9.10 ms                                                         | 8.35 ms: 1.09x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 47.2 ms: 1.01x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.67x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 464 ms: 1.99x faster                                                           |
| async_tree_none          | 394 ms                                                          | 213 ms: 1.85x faster                                                           |
| async_tree_io            | 940 ms                                                          | 531 ms: 1.77x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| pylint                   | 384 ms                                                          | 233 ms: 1.65x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.68 ms: 1.50x faster                                                          |
| go                       | 146 ms                                                          | 102 ms: 1.43x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.3 ms: 1.39x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.8 us: 1.36x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.9 ms: 1.36x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.60 ms: 1.29x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 76.0 ns: 1.29x faster                                                          |
| raytrace                 | 303 ms                                                          | 236 ms: 1.28x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.27x faster                                                          |
| deepcopy                 | 310 us                                                          | 247 us: 1.26x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 71.7 ms: 1.25x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.09 ms: 1.22x faster                                                          |
| thrift                   | 902 us                                                          | 742 us: 1.22x faster                                                           |
| pycparser                | 1.04 sec                                                        | 868 ms: 1.20x faster                                                           |
| pyflate                  | 422 ms                                                          | 354 ms: 1.19x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.20 ms: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.9 ms: 1.17x faster                                                          |
| generators               | 31.6 ms                                                         | 27.1 ms: 1.17x faster                                                          |
| scimark_sor              | 115 ms                                                          | 99.5 ms: 1.16x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 77.3 ms: 1.13x faster                                                          |
| richards_super           | 49.9 ms                                                         | 44.4 ms: 1.12x faster                                                          |
| float                    | 69.6 ms                                                         | 62.3 ms: 1.12x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.12x faster                                                           |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 46.8 ms: 1.11x faster                                                          |
| json                     | 4.76 ms                                                         | 4.29 ms: 1.11x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.9 ms: 1.11x faster                                                          |
| django_template          | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.35 ms: 1.09x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 174 us: 1.09x faster                                                           |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 262 us: 1.07x faster                                                           |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.51 us: 1.07x faster                                                          |
| 2to3                     | 265 ms                                                          | 250 ms: 1.06x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                         |
| regex_dna                | 131 ms                                                          | 124 ms: 1.05x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.6 ms: 1.05x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 76.7 ms: 1.05x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 225 ms: 1.02x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.8 ms: 1.02x faster                                                          |
| sympy_expand             | 391 ms                                                          | 383 ms: 1.02x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.34 sec: 1.02x faster                                                         |
| richards                 | 40.3 ms                                                         | 39.6 ms: 1.02x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.7 ms: 1.01x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 650 ms: 1.01x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.92 sec: 1.01x slower                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| genshi_xml               | 46.6 ms                                                         | 47.2 ms: 1.01x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 81.3 ms: 1.02x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| fannkuch                 | 317 ms                                                          | 327 ms: 1.03x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 50.6 ms: 1.05x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.1 ms: 1.07x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 747 us: 1.08x slower                                                           |
| scimark_fft              | 216 ms                                                          | 234 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.54 ms: 1.09x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.97 us: 1.09x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.2 ms: 1.10x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.73 us: 1.10x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 68.1 ms: 1.10x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.4 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                          |
| nbody                    | 79.1 ms                                                         | 96.4 ms: 1.22x slower                                                          |
| async_generators         | 241 ms                                                          | 304 ms: 1.26x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.97 ms: 1.44x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.127x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown