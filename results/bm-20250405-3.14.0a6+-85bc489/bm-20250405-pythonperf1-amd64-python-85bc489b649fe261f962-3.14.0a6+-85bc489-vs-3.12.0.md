# Results vs. 3.12.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.104x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                        |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                        |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.2 ms: 1.35x faster                                                       |
| nbody          | 71.9 ms                                                     | 62.6 ms: 1.15x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 79.4 ms: 1.10x faster                                                       |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 55.3 ms: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.77 us: 1.01x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                        |
| xml_etree_process    | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.53 us: 1.04x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.49 ms: 1.14x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 21.0 us: 1.14x slower                                                       |
| pickle               | 7.43 us                                                     | 8.57 us: 1.15x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.59 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.6 ms: 1.27x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.47 ms: 1.10x faster                                                       |
| django_template | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.52x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                        |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                        |
| mdp                        | 1.37 sec                                                    | 793 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                        |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.45x faster                                                      |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                        |
| float                      | 56.8 ms                                                     | 42.2 ms: 1.35x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.1 us: 1.31x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.3 us: 1.25x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 55.5 ms: 1.21x faster                                                       |
| go                         | 91.6 ms                                                     | 76.3 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.79 us: 1.17x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                       |
| nbody                      | 71.9 ms                                                     | 62.6 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.2 ms: 1.15x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.7 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                       |
| raytrace                   | 192 ms                                                      | 173 ms: 1.11x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 79.4 ms: 1.10x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.0 ns: 1.10x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.47 ms: 1.10x faster                                                       |
| scimark_fft                | 184 ms                                                      | 171 ms: 1.08x faster                                                        |
| async_generators           | 239 ms                                                      | 224 ms: 1.07x faster                                                        |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 73.8 ms: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.9 ms: 1.06x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 46.0 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 487 ms: 1.05x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.44 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 282 ms: 1.05x faster                                                        |
| richards                   | 28.4 ms                                                     | 27.2 ms: 1.04x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.5 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.04x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.96 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 88.8 ms: 1.03x faster                                                       |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.5 ms: 1.02x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 36.7 ns: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.7 ms: 1.01x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.13 ms: 1.01x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 55.3 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.23 us: 1.01x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                        |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| fannkuch                   | 247 ms                                                      | 250 ms: 1.01x slower                                                        |
| pycparser                  | 699 ms                                                      | 709 ms: 1.01x slower                                                        |
| sympy_expand               | 284 ms                                                      | 291 ms: 1.03x slower                                                        |
| json                       | 3.05 ms                                                     | 3.15 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.53 us: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 515 ms: 1.06x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.62 ms: 1.12x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.49 ms: 1.14x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 21.0 us: 1.14x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.57 us: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.6 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.6 ms: 1.27x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.59 us: 1.27x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.3 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.04 ms: 1.34x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.65x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (3): bench_thread_pool, regex_v8, logging_format
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown