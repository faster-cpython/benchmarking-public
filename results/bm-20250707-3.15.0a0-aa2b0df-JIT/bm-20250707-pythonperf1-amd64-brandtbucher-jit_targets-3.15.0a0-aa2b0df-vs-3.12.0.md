# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                    |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                    |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                    |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                    |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                                    |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.9 ms: 1.27x faster                                                   |
| nbody          | 71.9 ms                                                     | 59.8 ms: 1.20x faster                                                   |
| pidigits       | 152 ms                                                      | 146 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                       | 1.17x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                   |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                       | 1.04x faster                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                    |
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                     | 49.2 ms: 1.14x faster                                                   |
| xml_etree_process    | 37.7 ms                                                     | 34.8 ms: 1.08x faster                                                   |
| xml_etree_parse      | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.03x faster                                                   |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                   |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                    |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                   |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.38 ms: 1.32x faster                                                   |
| django_template | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.6 ms: 2.55x faster                                                   |
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                    |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                    |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                    |
| mdp                        | 1.37 sec                                                    | 797 ms: 1.72x faster                                                    |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                    |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                                    |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                    |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.37x faster                                                   |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                   |
| mako                       | 7.09 ms                                                     | 5.38 ms: 1.32x faster                                                   |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                    |
| float                      | 56.8 ms                                                     | 44.9 ms: 1.27x faster                                                   |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                  |
| scimark_fft                | 184 ms                                                      | 152 ms: 1.22x faster                                                    |
| nbody                      | 71.9 ms                                                     | 59.8 ms: 1.20x faster                                                   |
| pprint_pformat             | 1.05 sec                                                    | 881 ms: 1.19x faster                                                    |
| go                         | 91.6 ms                                                     | 77.4 ms: 1.18x faster                                                   |
| pprint_safe_repr           | 513 ms                                                      | 434 ms: 1.18x faster                                                    |
| pyflate                    | 295 ms                                                      | 253 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                   |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.15x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                     | 49.2 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.25 ms: 1.14x faster                                                   |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                   |
| logging_silent             | 60.5 ns                                                     | 54.2 ns: 1.12x faster                                                   |
| regex_compile              | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                   |
| xml_etree_process          | 37.7 ms                                                     | 34.8 ms: 1.08x faster                                                   |
| dulwich_log                | 44.3 ms                                                     | 41.1 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.9 ms: 1.07x faster                                                   |
| chaos                      | 43.3 ms                                                     | 40.6 ms: 1.07x faster                                                   |
| nqueens                    | 62.8 ms                                                     | 59.0 ms: 1.06x faster                                                   |
| fannkuch                   | 247 ms                                                      | 232 ms: 1.06x faster                                                    |
| crypto_pyaes               | 48.5 ms                                                     | 45.9 ms: 1.06x faster                                                   |
| meteor_contest             | 74.6 ms                                                     | 70.8 ms: 1.05x faster                                                   |
| richards                   | 28.4 ms                                                     | 26.9 ms: 1.05x faster                                                   |
| sympy_sum                  | 91.5 ms                                                     | 86.9 ms: 1.05x faster                                                   |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                   |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                                   |
| raytrace                   | 192 ms                                                      | 183 ms: 1.05x faster                                                    |
| pidigits                   | 152 ms                                                      | 146 ms: 1.05x faster                                                    |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                    |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                   |
| spectral_norm              | 66.9 ms                                                     | 64.5 ms: 1.04x faster                                                   |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                    |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.03x faster                                                   |
| logging_format             | 6.72 us                                                     | 6.58 us: 1.02x faster                                                   |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                   |
| logging_simple             | 6.28 us                                                     | 6.16 us: 1.02x faster                                                   |
| scimark_sor                | 78.8 ms                                                     | 77.9 ms: 1.01x faster                                                   |
| hexiom                     | 4.10 ms                                                     | 4.12 ms: 1.01x slower                                                   |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                   |
| deltablue                  | 2.16 ms                                                     | 2.21 ms: 1.02x slower                                                   |
| sympy_expand               | 284 ms                                                      | 291 ms: 1.03x slower                                                    |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                    |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                   |
| telco                      | 4.13 ms                                                     | 4.37 ms: 1.06x slower                                                   |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                    |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.09x slower                                                    |
| django_template            | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                                   |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                   |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                   |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                   |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                   |
| gc_traversal               | 1.52 ms                                                     | 2.13 ms: 1.40x slower                                                   |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.75x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                            |

Benchmark hidden because not significant (6): pycparser, docutils, regex_v8, scimark_lu, 2to3, regex_effbot
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250707-3.15.0a0-aa2b0df-JIT/bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown