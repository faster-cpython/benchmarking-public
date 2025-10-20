# Results vs. 3.12.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 216 ms: 1.01x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 378 ms: 2.04x faster                                                        |
| async_tree_io              | 731 ms                                                      | 387 ms: 1.89x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                        |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.71x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                       |
| nbody          | 71.9 ms                                                     | 62.9 ms: 1.14x faster                                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 86.3 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.44 ms: 1.05x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 133 us: 1.00x faster                                                        |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.0 ms: 1.03x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.54 us: 1.04x slower                                                       |
| pickle               | 7.43 us                                                     | 7.76 us: 1.04x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.3 us: 1.05x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 206 us: 1.05x slower                                                        |
| pickle_list          | 2.83 us                                                     | 3.20 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 7.09 ms                                                     | 6.63 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.5 ms: 2.82x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 378 ms: 2.04x faster                                                        |
| async_tree_io              | 731 ms                                                      | 387 ms: 1.89x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                        |
| mdp                        | 1.37 sec                                                    | 813 ms: 1.69x faster                                                        |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.25 sec: 1.67x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                        |
| deepcopy                   | 238 us                                                      | 163 us: 1.46x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.9 us: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                       |
| float                      | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 387 ms: 1.26x faster                                                        |
| go                         | 91.6 ms                                                     | 75.7 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.75 us: 1.19x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                       |
| nbody                      | 71.9 ms                                                     | 62.9 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.0 ms: 1.13x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.9 ms: 1.11x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.7 ms: 1.10x faster                                                       |
| scimark_fft                | 184 ms                                                      | 168 ms: 1.10x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 61.1 ms: 1.10x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.3 ns: 1.09x faster                                                       |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 84.7 ms: 1.08x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 86.3 ms: 1.08x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.6 ms: 1.08x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.1 ms: 1.07x faster                                                       |
| pyflate                    | 295 ms                                                      | 276 ms: 1.07x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.63 ms: 1.07x faster                                                       |
| richards                   | 28.4 ms                                                     | 26.6 ms: 1.07x faster                                                       |
| sympy_str                  | 175 ms                                                      | 165 ms: 1.06x faster                                                        |
| logging_simple             | 6.28 us                                                     | 5.91 us: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 70.7 ms: 1.06x faster                                                       |
| json                       | 3.05 ms                                                     | 2.89 ms: 1.05x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 995 ms: 1.05x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.39 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.44 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 489 ms: 1.05x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.44 ms: 1.05x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 46.4 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 824 us: 1.04x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 75.9 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.5 ms: 1.04x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                        |
| sympy_expand               | 284 ms                                                      | 276 ms: 1.03x faster                                                        |
| hexiom                     | 4.10 ms                                                     | 3.99 ms: 1.03x faster                                                       |
| async_generators           | 239 ms                                                      | 234 ms: 1.02x faster                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                       |
| 2to3                       | 218 ms                                                      | 216 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 133 us: 1.00x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.23 ms: 1.02x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.0 ms: 1.03x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.54 us: 1.04x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.76 us: 1.04x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.3 us: 1.05x slower                                                       |
| fannkuch                   | 247 ms                                                      | 258 ms: 1.05x slower                                                        |
| unpickle_list              | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 206 us: 1.05x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 40.2 ns: 1.07x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.20 us: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.4 ms: 1.18x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.4 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.06 ms: 1.35x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.27 ms: 1.69x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (4): pycparser, xml_etree_generate, deltablue, django_template
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown