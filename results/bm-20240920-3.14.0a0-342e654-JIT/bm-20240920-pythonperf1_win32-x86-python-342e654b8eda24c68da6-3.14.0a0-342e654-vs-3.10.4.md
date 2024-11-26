# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.222x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                         |
| html5lib       | 52.1 ms                                                         | 46.8 ms: 1.11x faster                                                          |
| tornado_http   | 118 ms                                                          | 100 ms: 1.17x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 472 ms: 1.95x faster                                                           |
| async_tree_none         | 394 ms                                                          | 221 ms: 1.78x faster                                                           |
| async_tree_io           | 940 ms                                                          | 541 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 275 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                           |
| float          | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                          |
| nbody          | 79.1 ms                                                         | 50.5 ms: 1.57x faster                                                          |
| Geometric mean | (ref)                                                           | 1.85x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 102 ms: 1.15x faster                                                           |
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.97 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.03 ms: 1.40x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 39.7 ms: 1.21x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.17x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 60.9 ms: 1.16x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 163 us: 1.16x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 242 us: 1.16x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 53.5 ms: 1.15x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.78 us: 1.08x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.4 us: 1.04x faster                                                          |
| pickle               | 7.83 us                                                         | 7.93 us: 1.01x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.31 us: 1.03x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.47 ms: 1.66x faster                                                          |
| django_template | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 24.1 ms: 1.15x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 53.8 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 146 us: 2.70x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.02 ms: 2.00x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 472 ms: 1.95x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.2 us: 1.95x faster                                                          |
| async_tree_none          | 394 ms                                                          | 221 ms: 1.78x faster                                                           |
| async_tree_io            | 940 ms                                                          | 541 ms: 1.74x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 46.6 ms: 1.72x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 275 ms: 1.69x faster                                                           |
| scimark_sor              | 115 ms                                                          | 68.0 ms: 1.69x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.4 ms: 1.68x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.47 ms: 1.66x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 59.7 ns: 1.64x faster                                                          |
| float                    | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                          |
| nbody                    | 79.1 ms                                                         | 50.5 ms: 1.57x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.6 us: 1.53x faster                                                          |
| pyflate                  | 422 ms                                                          | 282 ms: 1.50x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 60.0 ms: 1.50x faster                                                          |
| pylint                   | 384 ms                                                          | 268 ms: 1.43x faster                                                           |
| go                       | 146 ms                                                          | 102 ms: 1.43x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.03 ms: 1.40x faster                                                          |
| chaos                    | 74.4 ms                                                         | 53.3 ms: 1.40x faster                                                          |
| richards_super           | 49.9 ms                                                         | 35.9 ms: 1.39x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.36 ms: 1.37x faster                                                          |
| fannkuch                 | 317 ms                                                          | 237 ms: 1.34x faster                                                           |
| deepcopy                 | 310 us                                                          | 233 us: 1.33x faster                                                           |
| generators               | 31.6 ms                                                         | 23.8 ms: 1.33x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.86 ms: 1.26x faster                                                          |
| pycparser                | 1.04 sec                                                        | 825 ms: 1.26x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                         |
| raytrace                 | 303 ms                                                          | 244 ms: 1.24x faster                                                           |
| scimark_fft              | 216 ms                                                          | 175 ms: 1.23x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.4 ms: 1.23x faster                                                          |
| richards                 | 40.3 ms                                                         | 32.8 ms: 1.23x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 607 ms: 1.23x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 39.7 ms: 1.21x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.21x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 48.8 ms: 1.20x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.33 ms: 1.19x faster                                                          |
| tornado_http             | 118 ms                                                          | 100 ms: 1.17x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.17x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 60.9 ms: 1.16x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 163 us: 1.16x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 242 us: 1.16x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 53.5 ms: 1.15x faster                                                          |
| regex_compile            | 117 ms                                                          | 102 ms: 1.15x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 76.2 ms: 1.14x faster                                                          |
| thrift                   | 902 us                                                          | 790 us: 1.14x faster                                                           |
| json                     | 4.76 ms                                                         | 4.22 ms: 1.13x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.12x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 71.8 ms: 1.11x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.8 ms: 1.11x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 598 ms: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.25 sec: 1.09x faster                                                         |
| mdp                      | 1.83 sec                                                        | 1.69 sec: 1.08x faster                                                         |
| sympy_sum                | 122 ms                                                          | 113 ms: 1.08x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.78 us: 1.08x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.53 us: 1.06x faster                                                          |
| django_template          | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.4 us: 1.04x faster                                                          |
| sympy_str                | 229 ms                                                          | 220 ms: 1.04x faster                                                           |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                          |
| sympy_expand             | 391 ms                                                          | 394 ms: 1.01x slower                                                           |
| docutils                 | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                         |
| pickle                   | 7.83 us                                                         | 7.93 us: 1.01x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.1 ms: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 83.1 ms: 1.02x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 46.0 ms: 1.03x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.31 us: 1.03x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 41.4 ns: 1.03x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.34 us: 1.05x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.72 us: 1.06x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 745 us: 1.07x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 74.2 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 24.1 ms: 1.15x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 53.8 ms: 1.16x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.8 ms: 1.16x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.97 ms: 1.19x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.00 ms: 1.24x slower                                                          |
| async_generators         | 241 ms                                                          | 335 ms: 1.39x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (3): sqlglot_normalize, asyncio_tcp_ssl, sympy_integrate
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.222x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown