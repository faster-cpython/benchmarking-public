# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-x86
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.148x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 241 ms: 1.10x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.07x faster                                                          |
| html5lib       | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 479 ms: 1.93x faster                                                            |
| async_tree_none         | 394 ms                                                          | 215 ms: 1.83x faster                                                            |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 204 ms: 2.46x faster                                                            |
| float          | 69.6 ms                                                         | 60.2 ms: 1.16x faster                                                           |
| nbody          | 79.1 ms                                                         | 83.6 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                            |
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.64 ms: 1.14x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 173 us: 1.09x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 257 us: 1.09x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.6 ms: 1.05x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 47.9 ms: 1.00x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 66.3 ms: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.49 ms: 1.22x faster                                                           |
| django_template | 36.0 ms                                                         | 32.6 ms: 1.11x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 46.2 ms: 1.01x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 21.6 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.77x faster                                                            |
| pidigits                 | 502 ms                                                          | 204 ms: 2.46x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 479 ms: 1.93x faster                                                            |
| async_tree_none          | 394 ms                                                          | 215 ms: 1.83x faster                                                            |
| pylint                   | 384 ms                                                          | 210 ms: 1.83x faster                                                            |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.59 ms: 1.56x faster                                                           |
| go                       | 146 ms                                                          | 102 ms: 1.42x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 21.2 us: 1.39x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.4 ms: 1.39x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 71.0 ns: 1.38x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.1 ms: 1.38x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 66.0 ms: 1.36x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.4 us: 1.33x faster                                                           |
| generators               | 31.6 ms                                                         | 24.0 ms: 1.32x faster                                                           |
| pycparser                | 1.04 sec                                                        | 812 ms: 1.28x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.27x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.81 ms: 1.27x faster                                                           |
| deepcopy                 | 310 us                                                          | 245 us: 1.27x faster                                                            |
| raytrace                 | 303 ms                                                          | 244 ms: 1.24x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.29 ms: 1.23x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.49 ms: 1.22x faster                                                           |
| thrift                   | 902 us                                                          | 744 us: 1.21x faster                                                            |
| pyflate                  | 422 ms                                                          | 353 ms: 1.19x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 74.0 ms: 1.18x faster                                                           |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.17x faster                                                            |
| richards_super           | 49.9 ms                                                         | 42.9 ms: 1.16x faster                                                           |
| scimark_sor              | 115 ms                                                          | 99.1 ms: 1.16x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                           |
| float                    | 69.6 ms                                                         | 60.2 ms: 1.16x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 53.7 ms: 1.15x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 2.00 us: 1.15x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.64 ms: 1.14x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 71.4 ms: 1.12x faster                                                           |
| json                     | 4.76 ms                                                         | 4.25 ms: 1.12x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.6 ms: 1.11x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.1 ms: 1.10x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.3 ms: 1.10x faster                                                           |
| 2to3                     | 265 ms                                                          | 241 ms: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                            |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 173 us: 1.09x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 257 us: 1.09x faster                                                            |
| sympy_str                | 229 ms                                                          | 210 ms: 1.09x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.07x faster                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.53 us: 1.06x faster                                                           |
| sympy_expand             | 391 ms                                                          | 369 ms: 1.06x faster                                                            |
| richards                 | 40.3 ms                                                         | 38.2 ms: 1.05x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 220 ms: 1.05x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.6 ms: 1.05x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 42.8 ms: 1.04x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.75 sec: 1.04x faster                                                          |
| fannkuch                 | 317 ms                                                          | 305 ms: 1.04x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 639 ms: 1.03x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.34 sec: 1.02x faster                                                          |
| regex_v8                 | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.20 ms: 1.01x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 46.2 ms: 1.01x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 79.5 ms: 1.01x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 47.9 ms: 1.00x faster                                                           |
| pathlib                  | 81.2 ms                                                         | 81.7 ms: 1.01x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 21.6 ms: 1.03x slower                                                           |
| nbody                    | 79.1 ms                                                         | 83.6 ms: 1.06x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.75 us: 1.06x slower                                                           |
| scimark_fft              | 216 ms                                                          | 230 ms: 1.06x slower                                                            |
| logging_format           | 7.91 us                                                         | 8.46 us: 1.07x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 66.3 ms: 1.07x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                           |
| coverage                 | 46.6 ms                                                         | 54.1 ms: 1.16x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| async_generators         | 241 ms                                                          | 298 ms: 1.23x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.72 ms: 1.34x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 92.1 ms: 1.39x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.87 ms: 1.42x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.12 ms: 1.61x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.14x faster                                                                    |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.148x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown