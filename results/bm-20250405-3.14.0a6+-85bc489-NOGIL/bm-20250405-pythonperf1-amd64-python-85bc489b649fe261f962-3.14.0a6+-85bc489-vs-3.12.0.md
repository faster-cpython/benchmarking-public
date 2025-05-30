# Results vs. 3.12.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.000x slower
- HPT reliability: 96.70%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.06x slower                                                        |
| docutils       | 1.66 sec                                                    | 2.94 sec: 1.77x slower                                                      |
| Geometric mean | (ref)                                                       | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 332 ms: 2.32x faster                                                        |
| async_tree_io              | 731 ms                                                      | 358 ms: 2.04x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 191 ms: 1.92x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 150 ms: 1.91x faster                                                        |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 307 ms: 1.64x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 212 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.81x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.7 ms: 1.24x faster                                                       |
| pidigits       | 152 ms                                                      | 138 ms: 1.10x faster                                                        |
| nbody          | 71.9 ms                                                     | 80.9 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 93.4 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 58.0 ms: 1.12x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 89.0 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 61.8 ms: 1.11x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 20.9 us: 1.13x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                                        |
| pickle               | 7.43 us                                                     | 8.65 us: 1.16x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.21 us: 1.17x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 44.1 ms: 1.17x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 231 us: 1.18x slower                                                        |
| pickle_list          | 2.83 us                                                     | 3.43 us: 1.21x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.0 us: 1.23x slower                                                       |
| json_loads           | 13.9 us                                                     | 17.3 us: 1.25x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.46 ms: 1.31x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.62 sec: 1.92x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                                       |
| mako            | 7.09 ms                                                     | 9.86 ms: 1.39x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.27x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.52x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 332 ms: 2.32x faster                                                        |
| async_tree_io              | 731 ms                                                      | 358 ms: 2.04x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 191 ms: 1.92x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 150 ms: 1.91x faster                                                        |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 307 ms: 1.64x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 212 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.30 us: 1.35x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.16 ms: 1.31x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                      |
| float                      | 56.8 ms                                                     | 45.7 ms: 1.24x faster                                                       |
| deepcopy                   | 238 us                                                      | 203 us: 1.17x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.0 ms: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                       |
| pidigits                   | 152 ms                                                      | 138 ms: 1.10x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| comprehensions             | 14.1 us                                                     | 13.1 us: 1.08x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 22.0 us: 1.08x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.0 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.7 ms: 1.04x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 65.9 ms: 1.02x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.12 us: 1.01x slower                                                       |
| pycparser                  | 699 ms                                                      | 710 ms: 1.02x slower                                                        |
| go                         | 91.6 ms                                                     | 94.3 ms: 1.03x slower                                                       |
| chaos                      | 43.3 ms                                                     | 44.8 ms: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 62.9 ns: 1.04x slower                                                       |
| scimark_fft                | 184 ms                                                      | 194 ms: 1.05x slower                                                        |
| pyflate                    | 295 ms                                                      | 310 ms: 1.05x slower                                                        |
| 2to3                       | 218 ms                                                      | 230 ms: 1.06x slower                                                        |
| json                       | 3.05 ms                                                     | 3.22 ms: 1.06x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 62.7 ms: 1.06x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.69 us: 1.07x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 93.4 ms: 1.07x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 97.7 ms: 1.07x slower                                                       |
| raytrace                   | 192 ms                                                      | 205 ms: 1.07x slower                                                        |
| logging_format             | 6.72 us                                                     | 7.17 us: 1.07x slower                                                       |
| generators                 | 22.5 ms                                                     | 24.3 ms: 1.08x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 85.3 ms: 1.08x slower                                                       |
| sympy_str                  | 175 ms                                                      | 190 ms: 1.09x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 40.9 ns: 1.09x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.38 ms: 1.10x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 76.4 ms: 1.10x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 61.8 ms: 1.11x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 570 ms: 1.11x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.85 ms: 1.12x slower                                                       |
| nbody                      | 71.9 ms                                                     | 80.9 ms: 1.13x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 70.7 ms: 1.13x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 553 ms: 1.13x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.6 ms: 1.13x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.9 us: 1.13x slower                                                       |
| sympy_expand               | 284 ms                                                      | 324 ms: 1.14x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.69 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                                        |
| pickle                     | 7.43 us                                                     | 8.65 us: 1.16x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 86.9 ms: 1.16x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.21 us: 1.17x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 44.1 ms: 1.17x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 56.8 ms: 1.17x slower                                                       |
| richards                   | 28.4 ms                                                     | 33.4 ms: 1.18x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 231 us: 1.18x slower                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.52 sec: 1.20x slower                                                      |
| richards_super             | 32.1 ms                                                     | 38.9 ms: 1.21x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.43 us: 1.21x slower                                                       |
| unpickle                   | 8.18 us                                                     | 10.0 us: 1.23x slower                                                       |
| fannkuch                   | 247 ms                                                      | 307 ms: 1.24x slower                                                        |
| json_loads                 | 13.9 us                                                     | 17.3 us: 1.25x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 1.08 ms: 1.26x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.30 ms: 1.28x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.46 ms: 1.31x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.00 ms: 1.33x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| mako                       | 7.09 ms                                                     | 9.86 ms: 1.39x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 133 us: 1.40x slower                                                        |
| coverage                   | 40.8 ms                                                     | 67.3 ms: 1.65x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.73 sec: 1.65x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.94 sec: 1.77x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.62 sec: 1.92x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250405-3.14.0a6+-85bc489-NOGIL/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 96.70% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown