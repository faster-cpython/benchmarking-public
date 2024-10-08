# Results vs. 3.10.4

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-x86
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.11x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 250 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 479 ms: 1.92x faster                                                           |
| async_tree_none         | 394 ms                                                          | 226 ms: 1.74x faster                                                           |
| async_tree_io           | 940 ms                                                          | 556 ms: 1.69x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 284 ms: 1.65x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.75x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| float          | 69.6 ms                                                         | 62.1 ms: 1.12x faster                                                          |
| nbody          | 79.1 ms                                                         | 97.8 ms: 1.24x slower                                                          |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.94 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.52 ms: 1.31x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 258 us: 1.09x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 180 us: 1.05x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 51.2 ms: 1.06x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 67.8 ms: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 33.2 ms: 1.09x faster                                                          |
| mako            | 9.10 ms                                                         | 8.45 ms: 1.08x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 45.9 ms: 1.02x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 158 us: 2.50x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 479 ms: 1.92x faster                                                           |
| async_tree_none          | 394 ms                                                          | 226 ms: 1.74x faster                                                           |
| async_tree_io            | 940 ms                                                          | 556 ms: 1.69x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 284 ms: 1.65x faster                                                           |
| pylint                   | 384 ms                                                          | 239 ms: 1.61x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.74 ms: 1.47x faster                                                          |
| go                       | 146 ms                                                          | 105 ms: 1.39x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.9 ms: 1.38x faster                                                          |
| chaos                    | 74.4 ms                                                         | 55.5 ms: 1.34x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.2 us: 1.33x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 74.6 ns: 1.31x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.52 ms: 1.31x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 69.6 ms: 1.29x faster                                                          |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.27x faster                                                          |
| deepcopy                 | 310 us                                                          | 249 us: 1.24x faster                                                           |
| raytrace                 | 303 ms                                                          | 245 ms: 1.24x faster                                                           |
| thrift                   | 902 us                                                          | 752 us: 1.20x faster                                                           |
| pycparser                | 1.04 sec                                                        | 873 ms: 1.19x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.12 ms: 1.19x faster                                                          |
| pyflate                  | 422 ms                                                          | 360 ms: 1.17x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.27 ms: 1.16x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.38 ms: 1.15x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.9 ms: 1.15x faster                                                          |
| generators               | 31.6 ms                                                         | 27.5 ms: 1.15x faster                                                          |
| float                    | 69.6 ms                                                         | 62.1 ms: 1.12x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.12x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 78.0 ms: 1.12x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| scimark_sor              | 115 ms                                                          | 104 ms: 1.11x faster                                                           |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.0 ms: 1.11x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                          |
| richards_super           | 49.9 ms                                                         | 45.7 ms: 1.09x faster                                                          |
| json                     | 4.76 ms                                                         | 4.36 ms: 1.09x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 258 us: 1.09x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.2 ms: 1.09x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.48 us: 1.08x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.45 ms: 1.08x faster                                                          |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                           |
| 2to3                     | 265 ms                                                          | 250 ms: 1.06x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.7 ms: 1.06x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.06x faster                                                         |
| unpickle_pure_python     | 189 us                                                          | 180 us: 1.05x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 76.2 ms: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 219 ms: 1.04x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                         |
| genshi_xml               | 46.6 ms                                                         | 45.9 ms: 1.02x faster                                                          |
| sympy_expand             | 391 ms                                                          | 386 ms: 1.01x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 44.2 ms: 1.01x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.35 sec: 1.01x faster                                                         |
| coroutines               | 17.9 ms                                                         | 17.7 ms: 1.01x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 230 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| richards                 | 40.3 ms                                                         | 40.8 ms: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 82.7 ms: 1.03x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                          |
| fannkuch                 | 317 ms                                                          | 334 ms: 1.05x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 51.2 ms: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.4 ms: 1.08x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 747 us: 1.08x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.8 ms: 1.10x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.1 ms: 1.10x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| scimark_fft              | 216 ms                                                          | 239 ms: 1.11x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.15 us: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.94 us: 1.13x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.8 ms: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.94 ms: 1.16x slower                                                          |
| async_generators         | 241 ms                                                          | 294 ms: 1.22x slower                                                           |
| nbody                    | 79.1 ms                                                         | 97.8 ms: 1.24x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.99 ms: 1.45x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (4): asyncio_tcp, scimark_sparse_mat_mult, pprint_safe_repr, tomli_loads
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown