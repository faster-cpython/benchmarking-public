# Results vs. 3.12.0

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: windows-amd64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                        |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.4 ms: 1.34x faster                                                       |
| nbody          | 71.9 ms                                                     | 61.9 ms: 1.16x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.43 ms: 1.13x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 79.2 ms: 1.10x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.00x slower                                                        |
| xml_etree_process    | 37.7 ms                                                     | 39.0 ms: 1.03x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.07x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.45 ms: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.31 ms: 1.12x faster                                                       |
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.5 ms: 2.82x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                        |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                        |
| mdp                        | 1.37 sec                                                    | 772 ms: 1.78x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                        |
| deepcopy                   | 238 us                                                      | 167 us: 1.43x faster                                                        |
| float                      | 56.8 ms                                                     | 42.4 ms: 1.34x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                       |
| go                         | 91.6 ms                                                     | 76.4 ms: 1.20x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 56.2 ms: 1.19x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.0 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.78 us: 1.18x faster                                                       |
| nbody                      | 71.9 ms                                                     | 61.9 ms: 1.16x faster                                                       |
| chaos                      | 43.3 ms                                                     | 37.8 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.2 ms: 1.14x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.43 ms: 1.13x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.31 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 79.2 ms: 1.10x faster                                                       |
| raytrace                   | 192 ms                                                      | 175 ms: 1.10x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 55.3 ns: 1.09x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 72.2 ms: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 41.1 ms: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| scimark_fft                | 184 ms                                                      | 174 ms: 1.06x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 45.6 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 487 ms: 1.05x faster                                                        |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 997 ms: 1.05x faster                                                        |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.2 ms: 1.04x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.2 ms: 1.03x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.97 ms: 1.03x faster                                                       |
| pyflate                    | 295 ms                                                      | 285 ms: 1.03x faster                                                        |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 89.0 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.10 ms: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 834 us: 1.03x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.15 us: 1.02x faster                                                       |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                        |
| fannkuch                   | 247 ms                                                      | 245 ms: 1.01x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.00x slower                                                        |
| pycparser                  | 699 ms                                                      | 706 ms: 1.01x slower                                                        |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.0 ms: 1.03x slower                                                       |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                        |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.07x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.56 ms: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.45 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 86.3 ms: 1.25x slower                                                       |
| coverage                   | 40.8 ms                                                     | 51.2 ms: 1.25x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.01 ms: 1.32x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (2): 2to3, scimark_lu
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown