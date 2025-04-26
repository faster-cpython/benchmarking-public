# Results vs. 3.12.0

- fork: mdboom
- ref: python_startup_time
- machine: windows-amd64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.092x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                       |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.6 ms: 1.33x faster                                                      |
| nbody          | 71.9 ms                                                     | 62.2 ms: 1.16x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 80.6 ms: 1.09x faster                                                      |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.08x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.69 ms: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.9 ms: 1.22x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.65 ms: 1.06x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.52x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                       |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| mdp                        | 1.37 sec                                                    | 781 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                       |
| float                      | 56.8 ms                                                     | 42.6 ms: 1.33x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.5 us: 1.28x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 54.7 ms: 1.22x faster                                                      |
| go                         | 91.6 ms                                                     | 77.3 ms: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.79 us: 1.17x faster                                                      |
| nbody                      | 71.9 ms                                                     | 62.2 ms: 1.16x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.4 ms: 1.13x faster                                                      |
| raytrace                   | 192 ms                                                      | 173 ms: 1.11x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.8 ns: 1.10x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 80.6 ms: 1.09x faster                                                      |
| async_generators           | 239 ms                                                      | 221 ms: 1.08x faster                                                       |
| scimark_fft                | 184 ms                                                      | 171 ms: 1.08x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.65 ms: 1.06x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.3 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.2 ms: 1.06x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.9 ms: 1.06x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                      |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                       |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.5 ms: 1.03x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 76.2 ms: 1.03x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.48 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.02 sec: 1.02x faster                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 47.4 ms: 1.02x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 504 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.22 us: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.07 ms: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| scimark_lu                 | 58.9 ms                                                     | 58.5 ms: 1.01x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| richards_super             | 32.1 ms                                                     | 32.4 ms: 1.01x slower                                                      |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                      |
| pycparser                  | 699 ms                                                      | 707 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| fannkuch                   | 247 ms                                                      | 255 ms: 1.03x slower                                                       |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.08x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.61 ms: 1.12x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.69 ms: 1.18x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.9 ms: 1.22x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.7 ms: 1.27x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 89.0 ms: 1.29x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.08 ms: 1.37x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.67x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (5): richards, logging_format, meteor_contest, bench_thread_pool, deltablue
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.092x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown