# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-x86
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 254 ms: 1.04x faster                                                            |
| chameleon      | 6.42 ms                                                         | 6.31 ms: 1.02x faster                                                           |
| docutils       | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                          |
| html5lib       | 52.1 ms                                                         | 50.9 ms: 1.02x faster                                                           |
| tornado_http   | 118 ms                                                          | 100 ms: 1.17x faster                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 487 ms: 1.89x faster                                                            |
| async_tree_io           | 940 ms                                                          | 567 ms: 1.66x faster                                                            |
| async_tree_none         | 394 ms                                                          | 244 ms: 1.62x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 304 ms: 1.54x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.67x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| float          | 69.6 ms                                                         | 53.1 ms: 1.31x faster                                                           |
| nbody          | 79.1 ms                                                         | 74.7 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.51x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                           |
| regex_compile  | 117 ms                                                          | 125 ms: 1.07x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.13 ms: 1.38x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 102 ms: 1.17x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 241 us: 1.16x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 171 us: 1.11x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.6 ms: 1.10x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 44.3 ms: 1.09x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.1 us: 1.06x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.90 us: 1.03x faster                                                           |
| pickle               | 7.83 us                                                         | 7.94 us: 1.01x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.05x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.65 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.6 ms: 1.01x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 18.5 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.12 ms: 1.28x faster                                                           |
| django_template | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 48.8 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 149 us: 2.66x faster                                                            |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 487 ms: 1.89x faster                                                            |
| async_tree_io            | 940 ms                                                          | 567 ms: 1.66x faster                                                            |
| async_tree_none          | 394 ms                                                          | 244 ms: 1.62x faster                                                            |
| pylint                   | 384 ms                                                          | 242 ms: 1.59x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 304 ms: 1.54x faster                                                            |
| chaos                    | 74.4 ms                                                         | 51.5 ms: 1.44x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 56.4 ms: 1.44x faster                                                           |
| raytrace                 | 303 ms                                                          | 211 ms: 1.43x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.84 ms: 1.42x faster                                                           |
| richards_super           | 49.9 ms                                                         | 35.4 ms: 1.41x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.13 ms: 1.38x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 73.8 ns: 1.33x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.00 ms: 1.33x faster                                                           |
| generators               | 31.6 ms                                                         | 23.8 ms: 1.32x faster                                                           |
| float                    | 69.6 ms                                                         | 53.1 ms: 1.31x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.6 us: 1.30x faster                                                           |
| richards                 | 40.3 ms                                                         | 31.3 ms: 1.29x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.12 ms: 1.28x faster                                                           |
| go                       | 146 ms                                                          | 115 ms: 1.27x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.26 ms: 1.25x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.8 ms: 1.24x faster                                                           |
| pycparser                | 1.04 sec                                                        | 866 ms: 1.20x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 619 ms: 1.20x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 73.1 ms: 1.19x faster                                                           |
| scimark_sor              | 115 ms                                                          | 97.1 ms: 1.18x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.18x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 102 ms: 1.17x faster                                                            |
| tornado_http             | 118 ms                                                          | 100 ms: 1.17x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 241 us: 1.16x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.6 ms: 1.15x faster                                                           |
| fannkuch                 | 317 ms                                                          | 275 ms: 1.15x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 79.0 ms: 1.14x faster                                                           |
| pyflate                  | 422 ms                                                          | 375 ms: 1.12x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 71.7 ms: 1.12x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                           |
| json                     | 4.76 ms                                                         | 4.30 ms: 1.11x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 171 us: 1.11x faster                                                            |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.95 ms: 1.10x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.6 ms: 1.10x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.65 ms: 1.09x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 44.3 ms: 1.09x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.27 sec: 1.08x faster                                                          |
| scimark_fft              | 216 ms                                                          | 201 ms: 1.08x faster                                                            |
| django_template          | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 27.8 us: 1.06x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 620 ms: 1.06x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.1 us: 1.06x faster                                                           |
| nbody                    | 79.1 ms                                                         | 74.7 ms: 1.06x faster                                                           |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.05x faster                                                            |
| 2to3                     | 265 ms                                                          | 254 ms: 1.04x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.90 us: 1.03x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 50.9 ms: 1.02x faster                                                           |
| chameleon                | 6.42 ms                                                         | 6.31 ms: 1.02x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 78.7 ms: 1.02x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.6 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 44.1 ms: 1.01x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.4 ms: 1.01x faster                                                           |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 232 ms: 1.01x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                           |
| pickle                   | 7.83 us                                                         | 7.94 us: 1.01x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 18.5 ms: 1.02x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                          |
| sympy_str                | 229 ms                                                          | 237 ms: 1.03x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 84.3 ms: 1.04x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.80 us: 1.04x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 48.8 ms: 1.05x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.05x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.72 us: 1.06x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.38 us: 1.06x slower                                                           |
| regex_compile            | 117 ms                                                          | 125 ms: 1.07x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 71.5 ms: 1.08x slower                                                           |
| sympy_expand             | 391 ms                                                          | 422 ms: 1.08x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 760 us: 1.09x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.65 us: 1.14x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.47 ms: 1.15x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.62 ms: 1.16x slower                                                           |
| async_generators         | 241 ms                                                          | 294 ms: 1.22x slower                                                            |
| coverage                 | 46.6 ms                                                         | 333 ms: 7.15x slower                                                            |
| thrift                   | 902 us                                                          | 11.5 ms: 12.72x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (2): deepcopy, xml_etree_generate
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown