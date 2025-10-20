# Results vs. 3.12.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.150x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 377 ms: 2.05x faster                                                        |
| async_tree_io              | 731 ms                                                      | 386 ms: 1.89x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.73x faster                                                        |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.72x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 40.8 ms: 1.39x faster                                                       |
| nbody          | 71.9 ms                                                     | 54.6 ms: 1.32x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.6 ms: 1.13x faster                                                       |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.4 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 104 us: 1.28x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 49.5 ms: 1.13x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 84.9 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.1 ms: 1.09x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                       |
| pickle               | 7.43 us                                                     | 7.34 us: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.79 us: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 198 us: 1.01x slower                                                        |
| pickle_dict          | 18.4 us                                                     | 19.3 us: 1.05x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.60 us: 1.05x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.18 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.32 ms: 1.33x faster                                                       |
| django_template | 22.9 ms                                                     | 23.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.2 ms: 2.76x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 377 ms: 2.05x faster                                                        |
| async_tree_io              | 731 ms                                                      | 386 ms: 1.89x faster                                                        |
| mdp                        | 1.37 sec                                                    | 781 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.73x faster                                                        |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.41 sec: 1.49x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                        |
| deepcopy                   | 238 us                                                      | 163 us: 1.46x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.9 us: 1.41x faster                                                       |
| float                      | 56.8 ms                                                     | 40.8 ms: 1.39x faster                                                       |
| scimark_fft                | 184 ms                                                      | 134 ms: 1.38x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.32 ms: 1.33x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.33x faster                                                       |
| nbody                      | 71.9 ms                                                     | 54.6 ms: 1.32x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 104 us: 1.28x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 850 ms: 1.23x faster                                                        |
| go                         | 91.6 ms                                                     | 76.4 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.16 ms: 1.18x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                       |
| pyflate                    | 295 ms                                                      | 252 ms: 1.17x faster                                                        |
| fannkuch                   | 247 ms                                                      | 211 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 77.6 ms: 1.13x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 49.5 ms: 1.13x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.3 ms: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| unpack_sequence            | 37.5 ns                                                     | 34.2 ns: 1.10x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 84.9 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.1 ms: 1.09x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 44.8 ms: 1.08x faster                                                       |
| raytrace                   | 192 ms                                                      | 179 ms: 1.08x faster                                                        |
| json                       | 3.05 ms                                                     | 2.83 ms: 1.08x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 85.2 ms: 1.07x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.4 ns: 1.07x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.4 ms: 1.07x faster                                                       |
| telco                      | 4.13 ms                                                     | 3.88 ms: 1.06x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 63.0 ms: 1.06x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.3 ms: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.1 ms: 1.05x faster                                                       |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.05x faster                                                        |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.05x faster                                                       |
| pycparser                  | 699 ms                                                      | 670 ms: 1.04x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 71.8 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.4 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 76.7 ms: 1.03x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.13 us: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.58 us: 1.02x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 57.8 ms: 1.02x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.34 us: 1.01x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.07 ms: 1.01x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.79 us: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 198 us: 1.01x slower                                                        |
| sympy_expand               | 284 ms                                                      | 289 ms: 1.02x slower                                                        |
| async_generators           | 239 ms                                                      | 248 ms: 1.03x slower                                                        |
| django_template            | 22.9 ms                                                     | 23.8 ms: 1.04x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.3 us: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.60 us: 1.05x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.18 us: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 51.3 ms: 1.26x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.5 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.09 ms: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (4): bench_thread_pool, 2to3, coroutines, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.150x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown