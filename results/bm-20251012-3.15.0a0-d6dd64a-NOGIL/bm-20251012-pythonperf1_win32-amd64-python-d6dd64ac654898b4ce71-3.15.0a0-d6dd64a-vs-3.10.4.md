# Results vs. 3.10.4

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.325x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 222 ms: 1.20x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.84 sec: 1.46x slower                                                           |
| html5lib       | 52.1 ms                                                         | 40.3 ms: 1.29x faster                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 325 ms: 2.84x faster                                                             |
| async_tree_io           | 940 ms                                                          | 346 ms: 2.72x faster                                                             |
| async_tree_none         | 394 ms                                                          | 167 ms: 2.35x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.54x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 136 ms: 3.68x faster                                                             |
| float          | 69.6 ms                                                         | 45.9 ms: 1.52x faster                                                            |
| nbody          | 79.1 ms                                                         | 78.1 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.78x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 90.0 ms: 1.30x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.6 ms: 1.16x faster                                                            |
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.05 ms: 1.62x faster                                                            |
| json_loads           | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 92.2 ms: 1.30x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 150 us: 1.27x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 226 us: 1.24x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 59.3 ms: 1.19x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 43.2 ms: 1.11x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.10 us: 1.04x faster                                                            |
| unpickle             | 9.82 us                                                         | 10.0 us: 1.02x slower                                                            |
| pickle               | 7.83 us                                                         | 8.04 us: 1.03x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.5 us: 1.12x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.36 us: 1.13x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.31 sec: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.2 ms: 1.33x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 37.8 ms: 1.23x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 18.5 ms: 1.13x faster                                                            |
| mako            | 9.10 ms                                                         | 9.66 ms: 1.06x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.19 sec: 7.76x faster                                                           |
| pidigits                 | 502 ms                                                          | 136 ms: 3.68x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 130 us: 3.05x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 28.6 ms: 2.84x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 325 ms: 2.84x faster                                                             |
| async_tree_io            | 940 ms                                                          | 346 ms: 2.72x faster                                                             |
| async_tree_none          | 394 ms                                                          | 167 ms: 2.35x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| pylint                   | 384 ms                                                          | 202 ms: 1.90x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.06 sec: 1.71x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.36 us: 1.68x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 445 ms: 1.67x faster                                                             |
| deepcopy                 | 310 us                                                          | 186 us: 1.67x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.44 ms: 1.66x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 59.6 ns: 1.64x faster                                                            |
| chaos                    | 74.4 ms                                                         | 45.4 ms: 1.64x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.05 ms: 1.62x faster                                                            |
| go                       | 146 ms                                                          | 89.9 ms: 1.62x faster                                                            |
| thrift                   | 902 us                                                          | 560 us: 1.61x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 18.7 us: 1.58x faster                                                            |
| json                     | 4.76 ms                                                         | 3.06 ms: 1.55x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.5 us: 1.54x faster                                                            |
| float                    | 69.6 ms                                                         | 45.9 ms: 1.52x faster                                                            |
| pycparser                | 1.04 sec                                                        | 693 ms: 1.50x faster                                                             |
| generators               | 31.6 ms                                                         | 21.3 ms: 1.48x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 55.8 ms: 1.46x faster                                                            |
| raytrace                 | 303 ms                                                          | 210 ms: 1.44x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 41.4 ms: 1.41x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 64.0 ms: 1.40x faster                                                            |
| json_loads               | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| pyflate                  | 422 ms                                                          | 307 ms: 1.38x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.52 ms: 1.36x faster                                                            |
| richards_super           | 49.9 ms                                                         | 37.2 ms: 1.34x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.01 us: 1.34x faster                                                            |
| scimark_sor              | 115 ms                                                          | 86.8 ms: 1.33x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.2 ms: 1.33x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 92.2 ms: 1.30x faster                                                            |
| regex_compile            | 117 ms                                                          | 90.0 ms: 1.30x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 40.3 ms: 1.29x faster                                                            |
| sympy_sum                | 122 ms                                                          | 94.8 ms: 1.29x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 150 us: 1.27x faster                                                             |
| sympy_str                | 229 ms                                                          | 183 ms: 1.25x faster                                                             |
| sympy_expand             | 391 ms                                                          | 313 ms: 1.25x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 226 us: 1.24x faster                                                             |
| richards                 | 40.3 ms                                                         | 32.5 ms: 1.24x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.2 ms: 1.23x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 37.8 ms: 1.23x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.6 ms: 1.23x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 536 ms: 1.23x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 71.3 ms: 1.22x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 13.8 ms: 1.20x faster                                                            |
| 2to3                     | 265 ms                                                          | 222 ms: 1.20x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 59.3 ms: 1.19x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.6 ms: 1.16x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 18.5 ms: 1.13x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.00 us: 1.13x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 71.2 ms: 1.13x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.50 us: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 43.2 ms: 1.11x faster                                                            |
| scimark_fft              | 216 ms                                                          | 194 ms: 1.11x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.01 ms: 1.08x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.6 ns: 1.06x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.23 ms: 1.04x faster                                                            |
| fannkuch                 | 317 ms                                                          | 304 ms: 1.04x faster                                                             |
| pickle_list              | 3.22 us                                                         | 3.10 us: 1.04x faster                                                            |
| nbody                    | 79.1 ms                                                         | 78.1 ms: 1.01x faster                                                            |
| unpickle                 | 9.82 us                                                         | 10.0 us: 1.02x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.04 us: 1.03x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.00 ms: 1.03x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 84.3 ms: 1.05x slower                                                            |
| mako                     | 9.10 ms                                                         | 9.66 ms: 1.06x slower                                                            |
| async_generators         | 241 ms                                                          | 258 ms: 1.07x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 74.4 ms: 1.12x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.5 us: 1.12x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.36 us: 1.13x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.61 sec: 1.18x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.31 sec: 1.21x slower                                                           |
| coverage                 | 46.6 ms                                                         | 66.2 ms: 1.42x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.84 sec: 1.46x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.04 ms: 1.50x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.32x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251012-3.15.0a0-d6dd64a-NOGIL/bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.325x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown