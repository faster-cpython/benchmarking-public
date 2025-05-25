# Results vs. 3.12.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.238x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 204 ms: 1.07x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.53 sec: 1.09x faster                                                     |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 353 ms: 2.19x faster                                                       |
| async_tree_io              | 731 ms                                                      | 358 ms: 2.04x faster                                                       |
| async_tree_none            | 291 ms                                                      | 149 ms: 1.96x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 195 ms: 1.88x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 185 ms: 1.83x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 314 ms: 1.56x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.86x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 37.3 ms: 1.52x faster                                                      |
| nbody          | 71.9 ms                                                     | 50.7 ms: 1.42x faster                                                      |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 67.6 ms: 1.29x faster                                                      |
| regex_dna      | 126 ms                                                      | 112 ms: 1.13x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 12.8 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 11.3 us: 1.62x faster                                                      |
| pickle_list          | 2.83 us                                                     | 2.13 us: 1.33x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.06 sec: 1.29x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 103 us: 1.29x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.17 us: 1.26x faster                                                      |
| pickle               | 7.43 us                                                     | 6.16 us: 1.21x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 47.7 ms: 1.17x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 167 us: 1.17x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 32.7 ms: 1.15x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.20 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.5 ms: 1.08x faster                                                      |
| unpickle             | 8.18 us                                                     | 7.64 us: 1.07x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.90 ms: 1.20x faster                                                      |
| django_template | 22.9 ms                                                     | 20.1 ms: 1.14x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 27.8 ms: 2.90x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 353 ms: 2.19x faster                                                       |
| async_tree_io              | 731 ms                                                      | 358 ms: 2.04x faster                                                       |
| mdp                        | 1.37 sec                                                    | 683 ms: 2.01x faster                                                       |
| async_tree_none            | 291 ms                                                      | 149 ms: 1.96x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 195 ms: 1.88x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 185 ms: 1.83x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 13.8 us: 1.71x faster                                                      |
| deepcopy                   | 238 us                                                      | 139 us: 1.71x faster                                                       |
| comprehensions             | 14.1 us                                                     | 8.61 us: 1.64x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 11.3 us: 1.62x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 48.6 ms: 1.62x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.31 sec: 1.60x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 28.0 ms: 1.56x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 314 ms: 1.56x faster                                                       |
| go                         | 91.6 ms                                                     | 59.9 ms: 1.53x faster                                                      |
| float                      | 56.8 ms                                                     | 37.3 ms: 1.52x faster                                                      |
| generators                 | 22.5 ms                                                     | 15.3 ms: 1.47x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.46 us: 1.44x faster                                                      |
| nbody                      | 71.9 ms                                                     | 50.7 ms: 1.42x faster                                                      |
| chaos                      | 43.3 ms                                                     | 31.0 ms: 1.40x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 2.95 ms: 1.39x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.58 ms: 1.37x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 48.8 ms: 1.37x faster                                                      |
| richards                   | 28.4 ms                                                     | 21.3 ms: 1.33x faster                                                      |
| pickle_list                | 2.83 us                                                     | 2.13 us: 1.33x faster                                                      |
| raytrace                   | 192 ms                                                      | 146 ms: 1.32x faster                                                       |
| richards_super             | 32.1 ms                                                     | 24.6 ms: 1.31x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 67.6 ms: 1.29x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.06 sec: 1.29x faster                                                     |
| scimark_lu                 | 58.9 ms                                                     | 45.7 ms: 1.29x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 103 us: 1.29x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 29.1 ns: 1.29x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 48.8 ms: 1.29x faster                                                      |
| scimark_fft                | 184 ms                                                      | 143 ms: 1.29x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.17 us: 1.26x faster                                                      |
| fannkuch                   | 247 ms                                                      | 196 ms: 1.26x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 11.4 ms: 1.26x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 393 ms: 1.24x faster                                                       |
| pyflate                    | 295 ms                                                      | 238 ms: 1.24x faster                                                       |
| async_generators           | 239 ms                                                      | 195 ms: 1.23x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.1 ms: 1.21x faster                                                      |
| pickle                     | 7.43 us                                                     | 6.16 us: 1.21x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.90 ms: 1.20x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 37.3 ms: 1.19x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.48 us: 1.19x faster                                                      |
| sympy_str                  | 175 ms                                                      | 149 ms: 1.18x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 47.7 ms: 1.17x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 167 us: 1.17x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 78.4 ms: 1.17x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 11.2 ms: 1.16x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 444 ms: 1.16x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 32.7 ms: 1.15x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 908 ms: 1.15x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 65.3 ms: 1.14x faster                                                      |
| django_template            | 22.9 ms                                                     | 20.1 ms: 1.14x faster                                                      |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.13x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.01 us: 1.12x faster                                                      |
| sympy_expand               | 284 ms                                                      | 254 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.29 ms: 1.12x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.64 us: 1.11x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 12.8 ms: 1.11x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.20 ms: 1.09x faster                                                      |
| pycparser                  | 699 ms                                                      | 643 ms: 1.09x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.53 sec: 1.09x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.5 ms: 1.08x faster                                                      |
| unpickle                   | 8.18 us                                                     | 7.64 us: 1.07x faster                                                      |
| 2to3                       | 218 ms                                                      | 204 ms: 1.07x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 90.8 us: 1.05x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 819 us: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                      |
| telco                      | 4.13 ms                                                     | 4.08 ms: 1.01x faster                                                      |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 92.0 ms: 1.33x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.71 ms: 1.78x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.42 ms: 1.88x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 271 ns: 4.48x slower                                                       |
| coverage                   | 40.8 ms                                                     | 221 ms: 5.42x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.238x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown