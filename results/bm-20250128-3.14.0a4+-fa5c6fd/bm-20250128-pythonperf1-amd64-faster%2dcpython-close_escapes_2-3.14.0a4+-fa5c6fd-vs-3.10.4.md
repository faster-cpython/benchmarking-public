# Results vs. 3.10.4

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-amd64
- commit hash: fa5c6fd
- commit date: 2025-01-28
- overall geometric mean: 1.179x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.07x faster                                                             |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                           |
| html5lib       | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                            |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 432 ms: 2.57x faster                                                             |
| async_tree_memoization  | 526 ms                                                      | 228 ms: 2.31x faster                                                             |
| async_tree_none         | 435 ms                                                      | 195 ms: 2.23x faster                                                             |
| async_tree_cpu_io_mixed | 638 ms                                                      | 347 ms: 1.84x faster                                                             |
| Geometric mean          | (ref)                                                       | 2.22x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.9 ms: 1.19x faster                                                            |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                             |
| nbody          | 71.3 ms                                                     | 78.2 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.3 ms: 1.19x faster                                                            |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                             |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                            |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.77 ms: 1.35x faster                                                            |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                             |
| tomli_loads          | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                           |
| pickle_pure_python   | 270 us                                                      | 236 us: 1.14x faster                                                             |
| xml_etree_parse      | 96.8 ms                                                     | 88.0 ms: 1.10x faster                                                            |
| xml_etree_process    | 44.5 ms                                                     | 41.4 ms: 1.07x faster                                                            |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                            |
| xml_etree_generate   | 55.5 ms                                                     | 58.5 ms: 1.05x slower                                                            |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                            |
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.77 ms: 1.33x faster                                                            |
| genshi_text     | 19.8 ms                                                     | 16.3 ms: 1.22x faster                                                            |
| genshi_xml      | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                            |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                            |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.01x faster                                                             |
| async_tree_io            | 1.11 sec                                                    | 432 ms: 2.57x faster                                                             |
| async_tree_memoization   | 526 ms                                                      | 228 ms: 2.31x faster                                                             |
| async_tree_none          | 435 ms                                                      | 195 ms: 2.23x faster                                                             |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 347 ms: 1.84x faster                                                             |
| pylint                   | 350 ms                                                      | 202 ms: 1.74x faster                                                             |
| deltablue                | 4.19 ms                                                     | 2.48 ms: 1.69x faster                                                            |
| generators               | 32.4 ms                                                     | 21.0 ms: 1.55x faster                                                            |
| go                       | 139 ms                                                      | 93.6 ms: 1.48x faster                                                            |
| chaos                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                            |
| richards_super           | 52.2 ms                                                     | 37.4 ms: 1.40x faster                                                            |
| deepcopy_memo            | 28.8 us                                                     | 20.8 us: 1.38x faster                                                            |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                             |
| sqlglot_parse            | 1.22 ms                                                     | 882 us: 1.38x faster                                                             |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.36x faster                                                            |
| logging_silent           | 94.6 ns                                                     | 69.9 ns: 1.35x faster                                                            |
| json_dumps               | 9.16 ms                                                     | 6.77 ms: 1.35x faster                                                            |
| mako                     | 9.03 ms                                                     | 6.77 ms: 1.33x faster                                                            |
| raytrace                 | 273 ms                                                      | 206 ms: 1.33x faster                                                             |
| pyflate                  | 409 ms                                                      | 316 ms: 1.30x faster                                                             |
| html5lib                 | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                            |
| crypto_pyaes             | 62.5 ms                                                     | 48.6 ms: 1.29x faster                                                            |
| richards                 | 42.4 ms                                                     | 33.1 ms: 1.28x faster                                                            |
| comprehensions           | 16.5 us                                                     | 13.0 us: 1.27x faster                                                            |
| pycparser                | 930 ms                                                      | 737 ms: 1.26x faster                                                             |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                            |
| sympy_sum                | 107 ms                                                      | 88.0 ms: 1.22x faster                                                            |
| genshi_text              | 19.8 ms                                                     | 16.3 ms: 1.22x faster                                                            |
| hexiom                   | 5.74 ms                                                     | 4.79 ms: 1.20x faster                                                            |
| scimark_lu               | 85.8 ms                                                     | 71.5 ms: 1.20x faster                                                            |
| float                    | 61.7 ms                                                     | 51.9 ms: 1.19x faster                                                            |
| regex_compile            | 106 ms                                                      | 89.3 ms: 1.19x faster                                                            |
| thrift                   | 617 us                                                      | 520 us: 1.19x faster                                                             |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                             |
| dulwich_log              | 50.5 ms                                                     | 42.7 ms: 1.18x faster                                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.18x faster                                                            |
| genshi_xml               | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                            |
| mdp                      | 1.78 sec                                                    | 1.51 sec: 1.18x faster                                                           |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                             |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.8 ms: 1.17x faster                                                            |
| spectral_norm            | 77.3 ms                                                     | 66.2 ms: 1.17x faster                                                            |
| tomli_loads              | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                           |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                            |
| bench_thread_pool        | 958 us                                                      | 836 us: 1.15x faster                                                             |
| pickle_pure_python       | 270 us                                                      | 236 us: 1.14x faster                                                             |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                           |
| scimark_sor              | 106 ms                                                      | 94.7 ms: 1.12x faster                                                            |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                            |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.11x faster                                                           |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                            |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                             |
| xml_etree_parse          | 96.8 ms                                                     | 88.0 ms: 1.10x faster                                                            |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.09x faster                                                            |
| sqlglot_optimize         | 39.8 ms                                                     | 36.6 ms: 1.09x faster                                                            |
| xml_etree_process        | 44.5 ms                                                     | 41.4 ms: 1.07x faster                                                            |
| pprint_safe_repr         | 592 ms                                                      | 551 ms: 1.07x faster                                                             |
| 2to3                     | 246 ms                                                      | 231 ms: 1.07x faster                                                             |
| sympy_expand             | 314 ms                                                      | 299 ms: 1.05x faster                                                             |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                            |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.03x faster                                                             |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                            |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                             |
| nqueens                  | 66.6 ms                                                     | 66.1 ms: 1.01x faster                                                            |
| meteor_contest           | 75.9 ms                                                     | 75.4 ms: 1.01x faster                                                            |
| logging_format           | 6.76 us                                                     | 6.82 us: 1.01x slower                                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.76 ms: 1.01x slower                                                            |
| scimark_fft              | 187 ms                                                      | 191 ms: 1.02x slower                                                             |
| async_generators         | 222 ms                                                      | 226 ms: 1.02x slower                                                             |
| logging_simple           | 6.22 us                                                     | 6.41 us: 1.03x slower                                                            |
| pathlib                  | 75.7 ms                                                     | 78.0 ms: 1.03x slower                                                            |
| xml_etree_generate       | 55.5 ms                                                     | 58.5 ms: 1.05x slower                                                            |
| nbody                    | 71.3 ms                                                     | 78.2 ms: 1.10x slower                                                            |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                                            |
| fannkuch                 | 256 ms                                                      | 289 ms: 1.13x slower                                                             |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                            |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                            |
| telco                    | 3.94 ms                                                     | 4.79 ms: 1.22x slower                                                            |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                            |
| gc_traversal             | 1.41 ms                                                     | 1.99 ms: 1.41x slower                                                            |
| bench_mp_pool            | 62.0 ms                                                     | 88.5 ms: 1.43x slower                                                            |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.52x slower                                                            |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250128-3.14.0a4+-fa5c6fd/bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.179x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown