# Results vs. 3.12.0

- fork: python
- ref: 44e4c479fbf2c28605bd
- machine: windows-amd64
- commit hash: 44e4c47
- commit date: 2025-04-30
- overall geometric mean: 1.096x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 412 ms: 1.78x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                       |
| nbody          | 71.9 ms                                                     | 62.9 ms: 1.14x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 79.8 ms: 1.10x faster                                                       |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 89.6 ms: 1.04x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.83 ms: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.49 ms: 1.09x faster                                                       |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.6 ms: 2.47x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 412 ms: 1.78x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                        |
| mdp                        | 1.37 sec                                                    | 790 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| deepcopy                   | 238 us                                                      | 172 us: 1.38x faster                                                        |
| float                      | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.4 us: 1.29x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                       |
| go                         | 91.6 ms                                                     | 76.3 ms: 1.20x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 57.2 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                       |
| nbody                      | 71.9 ms                                                     | 62.9 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.7 ms: 1.12x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.1 ns: 1.10x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 79.8 ms: 1.10x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.49 ms: 1.09x faster                                                       |
| pyflate                    | 295 ms                                                      | 272 ms: 1.08x faster                                                        |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.7 ms: 1.08x faster                                                       |
| scimark_fft                | 184 ms                                                      | 174 ms: 1.06x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 74.4 ms: 1.06x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 55.7 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.0 ms: 1.05x faster                                                       |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                        |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 491 ms: 1.05x faster                                                        |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 60.2 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.1 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.6 ms: 1.04x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.08 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.2 ms: 1.03x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.97 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.50 ms: 1.02x faster                                                       |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                                        |
| logging_simple             | 6.28 us                                                     | 6.16 us: 1.02x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.65 us: 1.01x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| fannkuch                   | 247 ms                                                      | 250 ms: 1.01x slower                                                        |
| pycparser                  | 699 ms                                                      | 707 ms: 1.01x slower                                                        |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                        |
| json                       | 3.05 ms                                                     | 3.14 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.60 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.15x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.83 ms: 1.20x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 90.0 ms: 1.30x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.08 ms: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.67x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_generate, 2to3, bench_thread_pool
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.096x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown