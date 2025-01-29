# Results vs. 3.10.4

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-x86
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.103x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                                 |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                               |
| html5lib       | 52.1 ms                                                         | 45.3 ms: 1.15x faster                                                                |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 460 ms: 2.00x faster                                                                 |
| async_tree_io           | 940 ms                                                          | 475 ms: 1.98x faster                                                                 |
| async_tree_none         | 394 ms                                                          | 225 ms: 1.75x faster                                                                 |
| async_tree_memoization  | 467 ms                                                          | 269 ms: 1.73x faster                                                                 |
| Geometric mean          | (ref)                                                           | 1.86x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.48x faster                                                                 |
| float          | 69.6 ms                                                         | 56.0 ms: 1.24x faster                                                                |
| nbody          | 79.1 ms                                                         | 87.2 ms: 1.10x slower                                                                |
| Geometric mean | (ref)                                                           | 1.41x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                                 |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                                |
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                                 |
| tomli_loads          | 1.91 sec                                                        | 1.76 sec: 1.08x faster                                                               |
| json_dumps           | 9.82 ms                                                         | 9.24 ms: 1.06x faster                                                                |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.1 ms: 1.05x faster                                                                |
| unpickle_pure_python | 189 us                                                          | 183 us: 1.04x faster                                                                 |
| pickle_pure_python   | 280 us                                                          | 289 us: 1.03x slower                                                                 |
| json_loads           | 22.4 us                                                         | 23.2 us: 1.04x slower                                                                |
| xml_etree_process    | 48.1 ms                                                         | 51.7 ms: 1.07x slower                                                                |
| xml_etree_generate   | 61.6 ms                                                         | 70.5 ms: 1.14x slower                                                                |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                                |
| python_startup         | 22.9 ms                                                         | 26.7 ms: 1.17x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.68 ms: 1.19x faster                                                                |
| django_template | 36.0 ms                                                         | 35.1 ms: 1.03x faster                                                                |
| genshi_xml      | 46.6 ms                                                         | 46.9 ms: 1.01x slower                                                                |
| genshi_text     | 21.0 ms                                                         | 21.3 ms: 1.02x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 202 ms: 2.48x faster                                                                 |
| typing_runtime_protocols | 396 us                                                          | 164 us: 2.41x faster                                                                 |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 460 ms: 2.00x faster                                                                 |
| async_tree_io            | 940 ms                                                          | 475 ms: 1.98x faster                                                                 |
| async_tree_none          | 394 ms                                                          | 225 ms: 1.75x faster                                                                 |
| async_tree_memoization   | 467 ms                                                          | 269 ms: 1.73x faster                                                                 |
| pylint                   | 384 ms                                                          | 225 ms: 1.71x faster                                                                 |
| deltablue                | 4.04 ms                                                         | 2.82 ms: 1.43x faster                                                                |
| deepcopy_memo            | 29.6 us                                                         | 21.7 us: 1.36x faster                                                                |
| go                       | 146 ms                                                          | 107 ms: 1.36x faster                                                                 |
| chaos                    | 74.4 ms                                                         | 58.6 ms: 1.27x faster                                                                |
| logging_silent           | 97.9 ns                                                         | 77.5 ns: 1.26x faster                                                                |
| deepcopy                 | 310 us                                                          | 247 us: 1.26x faster                                                                 |
| crypto_pyaes             | 81.3 ms                                                         | 65.1 ms: 1.25x faster                                                                |
| float                    | 69.6 ms                                                         | 56.0 ms: 1.24x faster                                                                |
| sqlglot_parse            | 1.33 ms                                                         | 1.09 ms: 1.22x faster                                                                |
| comprehensions           | 17.7 us                                                         | 14.6 us: 1.22x faster                                                                |
| pyflate                  | 422 ms                                                          | 354 ms: 1.19x faster                                                                 |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                                |
| mako                     | 9.10 ms                                                         | 7.68 ms: 1.19x faster                                                                |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                                |
| thrift                   | 902 us                                                          | 772 us: 1.17x faster                                                                 |
| generators               | 31.6 ms                                                         | 27.1 ms: 1.17x faster                                                                |
| pycparser                | 1.04 sec                                                        | 900 ms: 1.16x faster                                                                 |
| html5lib                 | 52.1 ms                                                         | 45.3 ms: 1.15x faster                                                                |
| scimark_lu               | 89.8 ms                                                         | 78.3 ms: 1.15x faster                                                                |
| scimark_monte_carlo      | 61.9 ms                                                         | 54.7 ms: 1.13x faster                                                                |
| hexiom                   | 6.13 ms                                                         | 5.43 ms: 1.13x faster                                                                |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                                 |
| dulwich_log              | 58.5 ms                                                         | 52.3 ms: 1.12x faster                                                                |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.11x faster                                                                 |
| spectral_norm            | 80.2 ms                                                         | 72.1 ms: 1.11x faster                                                                |
| nqueens                  | 87.1 ms                                                         | 78.4 ms: 1.11x faster                                                                |
| scimark_sor              | 115 ms                                                          | 104 ms: 1.11x faster                                                                 |
| richards_super           | 49.9 ms                                                         | 45.4 ms: 1.10x faster                                                                |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                                 |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                                |
| tomli_loads              | 1.91 sec                                                        | 1.76 sec: 1.08x faster                                                               |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                                |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                                 |
| json_dumps               | 9.82 ms                                                         | 9.24 ms: 1.06x faster                                                                |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.1 ms: 1.05x faster                                                                |
| raytrace                 | 303 ms                                                          | 287 ms: 1.05x faster                                                                 |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                               |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.05x faster                                                                |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.11 ms: 1.04x faster                                                                |
| unpickle_pure_python     | 189 us                                                          | 183 us: 1.04x faster                                                                 |
| mdp                      | 1.83 sec                                                        | 1.77 sec: 1.03x faster                                                               |
| deepcopy_reduce          | 2.68 us                                                         | 2.60 us: 1.03x faster                                                                |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                                 |
| django_template          | 36.0 ms                                                         | 35.1 ms: 1.03x faster                                                                |
| sympy_str                | 229 ms                                                          | 224 ms: 1.02x faster                                                                 |
| richards                 | 40.3 ms                                                         | 39.8 ms: 1.01x faster                                                                |
| coroutines               | 17.9 ms                                                         | 17.8 ms: 1.01x faster                                                                |
| fannkuch                 | 317 ms                                                          | 316 ms: 1.00x faster                                                                 |
| sqlglot_optimize         | 44.7 ms                                                         | 45.0 ms: 1.01x slower                                                                |
| genshi_xml               | 46.6 ms                                                         | 46.9 ms: 1.01x slower                                                                |
| sqlglot_normalize        | 230 ms                                                          | 232 ms: 1.01x slower                                                                 |
| pprint_pformat           | 1.37 sec                                                        | 1.38 sec: 1.01x slower                                                               |
| meteor_contest           | 80.0 ms                                                         | 81.0 ms: 1.01x slower                                                                |
| genshi_text              | 21.0 ms                                                         | 21.3 ms: 1.02x slower                                                                |
| pprint_safe_repr         | 658 ms                                                          | 670 ms: 1.02x slower                                                                 |
| sympy_expand             | 391 ms                                                          | 398 ms: 1.02x slower                                                                 |
| pickle_pure_python       | 280 us                                                          | 289 us: 1.03x slower                                                                 |
| json_loads               | 22.4 us                                                         | 23.2 us: 1.04x slower                                                                |
| pathlib                  | 81.2 ms                                                         | 85.9 ms: 1.06x slower                                                                |
| xml_etree_process        | 48.1 ms                                                         | 51.7 ms: 1.07x slower                                                                |
| scimark_fft              | 216 ms                                                          | 235 ms: 1.08x slower                                                                 |
| nbody                    | 79.1 ms                                                         | 87.2 ms: 1.10x slower                                                                |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                                |
| coverage                 | 46.6 ms                                                         | 52.8 ms: 1.13x slower                                                                |
| xml_etree_generate       | 61.6 ms                                                         | 70.5 ms: 1.14x slower                                                                |
| logging_simple           | 7.29 us                                                         | 8.43 us: 1.16x slower                                                                |
| logging_format           | 7.91 us                                                         | 9.15 us: 1.16x slower                                                                |
| python_startup           | 22.9 ms                                                         | 26.7 ms: 1.17x slower                                                                |
| async_generators         | 241 ms                                                          | 309 ms: 1.28x slower                                                                 |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                                |
| bench_mp_pool            | 66.4 ms                                                         | 94.2 ms: 1.42x slower                                                                |
| telco                    | 4.83 ms                                                         | 6.91 ms: 1.43x slower                                                                |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                                |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                                         |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-620dde2/bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown