# Results vs. 3.12.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.286x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 202 ms: 1.08x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 347 ms: 2.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 339 ms: 2.15x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.94x faster                                                        |
| async_tree_none            | 291 ms                                                      | 153 ms: 1.90x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 194 ms: 1.89x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 183 ms: 1.86x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 315 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 308 ms: 1.59x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.88x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 35.8 ms: 1.59x faster                                                       |
| nbody          | 71.9 ms                                                     | 51.9 ms: 1.39x faster                                                       |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 67.6 ms: 1.29x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 11.7 us: 1.57x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.01 sec: 1.36x faster                                                      |
| pickle_list          | 2.83 us                                                     | 2.12 us: 1.33x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.09 us: 1.31x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 105 us: 1.26x faster                                                        |
| pickle               | 7.43 us                                                     | 6.15 us: 1.21x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 164 us: 1.19x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 46.9 ms: 1.19x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 32.4 ms: 1.16x faster                                                       |
| unpickle             | 8.18 us                                                     | 7.38 us: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.6 us: 1.02x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.9 ms: 1.29x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.6 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.72 ms: 1.24x faster                                                       |
| django_template | 22.9 ms                                                     | 19.4 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.7 ms: 2.62x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 347 ms: 2.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 339 ms: 2.15x faster                                                        |
| mdp                        | 1.37 sec                                                    | 661 ms: 2.08x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.94x faster                                                        |
| async_tree_none            | 291 ms                                                      | 153 ms: 1.90x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 194 ms: 1.89x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 183 ms: 1.86x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 13.0 us: 1.82x faster                                                       |
| deepcopy                   | 238 us                                                      | 133 us: 1.78x faster                                                        |
| comprehensions             | 14.1 us                                                     | 8.35 us: 1.69x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 47.1 ms: 1.67x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 26.9 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 315 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 308 ms: 1.59x faster                                                        |
| float                      | 56.8 ms                                                     | 35.8 ms: 1.59x faster                                                       |
| go                         | 91.6 ms                                                     | 57.9 ms: 1.58x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 11.7 us: 1.57x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.41 us: 1.49x faster                                                       |
| generators                 | 22.5 ms                                                     | 15.2 ms: 1.48x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.45x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 41.9 ns: 1.44x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 46.5 ms: 1.44x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.51 ms: 1.43x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 2.88 ms: 1.42x faster                                                       |
| chaos                      | 43.3 ms                                                     | 31.2 ms: 1.39x faster                                                       |
| nbody                      | 71.9 ms                                                     | 51.9 ms: 1.39x faster                                                       |
| richards                   | 28.4 ms                                                     | 20.7 ms: 1.37x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.01 sec: 1.36x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 379 ms: 1.35x faster                                                        |
| raytrace                   | 192 ms                                                      | 143 ms: 1.35x faster                                                        |
| richards_super             | 32.1 ms                                                     | 23.9 ms: 1.34x faster                                                       |
| scimark_fft                | 184 ms                                                      | 138 ms: 1.34x faster                                                        |
| pickle_list                | 2.83 us                                                     | 2.12 us: 1.33x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 785 ms: 1.33x faster                                                        |
| unpack_sequence            | 37.5 ns                                                     | 28.3 ns: 1.33x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 10.8 ms: 1.32x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.09 us: 1.31x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 47.8 ms: 1.31x faster                                                       |
| async_generators           | 239 ms                                                      | 183 ms: 1.31x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 45.2 ms: 1.30x faster                                                       |
| fannkuch                   | 247 ms                                                      | 190 ms: 1.30x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 67.6 ms: 1.29x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.26x faster                                                        |
| pyflate                    | 295 ms                                                      | 233 ms: 1.26x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.72 ms: 1.24x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 39.2 ms: 1.24x faster                                                       |
| pickle                     | 7.43 us                                                     | 6.15 us: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.19x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 164 us: 1.19x faster                                                        |
| sympy_str                  | 175 ms                                                      | 147 ms: 1.19x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 46.9 ms: 1.19x faster                                                       |
| django_template            | 22.9 ms                                                     | 19.4 ms: 1.18x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 37.6 ms: 1.18x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 77.9 ms: 1.17x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.50 us: 1.17x faster                                                       |
| logging_format             | 6.72 us                                                     | 5.73 us: 1.17x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 11.1 ms: 1.17x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.38 us: 1.17x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 32.4 ms: 1.16x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 84.1 us: 1.13x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 66.2 ms: 1.13x faster                                                       |
| sympy_expand               | 284 ms                                                      | 252 ms: 1.12x faster                                                        |
| unpickle                   | 8.18 us                                                     | 7.38 us: 1.11x faster                                                       |
| pycparser                  | 699 ms                                                      | 641 ms: 1.09x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| 2to3                       | 218 ms                                                      | 202 ms: 1.08x faster                                                        |
| regex_v8                   | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 813 us: 1.05x faster                                                        |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                       |
| telco                      | 4.13 ms                                                     | 4.00 ms: 1.03x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.6 us: 1.02x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| coverage                   | 40.8 ms                                                     | 40.5 ms: 1.01x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 504 ms: 1.03x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 87.9 ms: 1.27x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.9 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.6 ms: 1.36x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.38 ms: 1.84x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.81 ms: 1.85x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                                |

Benchmark hidden because not significant (1): json
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.286x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown