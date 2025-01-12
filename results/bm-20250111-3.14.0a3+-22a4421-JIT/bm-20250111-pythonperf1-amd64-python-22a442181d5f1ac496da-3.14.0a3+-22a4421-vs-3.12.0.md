# Results vs. 3.12.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-amd64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.077x faster
- HPT reliability: 99.16%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 405 ms: 1.80x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 351 ms: 1.39x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 39.3 ms: 1.44x faster                                                       |
| nbody          | 71.9 ms                                                     | 53.9 ms: 1.33x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.5 ms: 1.10x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.24x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.4 ms: 1.08x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.01 us: 1.06x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.07x slower                                                        |
| pickle               | 7.43 us                                                     | 7.97 us: 1.07x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.85 us: 1.08x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.02 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.3 ms: 1.06x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.6 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.08 ms: 1.39x faster                                                       |
| django_template | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 405 ms: 1.80x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.37 sec: 1.53x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.3 us: 1.45x faster                                                       |
| float                      | 56.8 ms                                                     | 39.3 ms: 1.44x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.08 ms: 1.39x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 351 ms: 1.39x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 49.8 ms: 1.34x faster                                                       |
| nbody                      | 71.9 ms                                                     | 53.9 ms: 1.33x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 61.3 ms: 1.29x faster                                                       |
| scimark_fft                | 184 ms                                                      | 143 ms: 1.29x faster                                                        |
| deepcopy                   | 238 us                                                      | 188 us: 1.26x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.04 ms: 1.25x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.24x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.4 ms: 1.20x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.2 ms: 1.18x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 53.0 ms: 1.11x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 948 ms: 1.10x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 79.5 ms: 1.10x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.6 ms: 1.09x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.4 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 476 ms: 1.08x faster                                                        |
| pyflate                    | 295 ms                                                      | 276 ms: 1.07x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 57.0 ns: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.0 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 89.8 ms: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.62 us: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.5 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.21 us: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 174 ms: 1.01x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 79.9 ms: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.2 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 63.5 ms: 1.01x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 820 us: 1.02x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.04x slower                                                       |
| raytrace                   | 192 ms                                                      | 200 ms: 1.04x slower                                                        |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| pycparser                  | 699 ms                                                      | 734 ms: 1.05x slower                                                        |
| generators                 | 22.5 ms                                                     | 23.7 ms: 1.05x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.35 ms: 1.05x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.05x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.06x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.3 ms: 1.06x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.01 us: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.07x slower                                                        |
| pickle                     | 7.43 us                                                     | 7.97 us: 1.07x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 37.1 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 202 ms: 1.08x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.85 us: 1.08x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                      |
| async_generators           | 239 ms                                                      | 261 ms: 1.09x slower                                                        |
| unpickle_list              | 2.75 us                                                     | 3.02 us: 1.10x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 537 ms: 1.10x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 41.5 ns: 1.11x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.7 ms: 1.17x slower                                                       |
| richards_super             | 32.1 ms                                                     | 37.9 ms: 1.18x slower                                                       |
| richards                   | 28.4 ms                                                     | 33.6 ms: 1.19x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                        |
| django_template            | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 83.5 ms: 1.21x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.6 ms: 1.21x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.00 ms: 1.22x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.00 ms: 1.32x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (2): bench_thread_pool, fannkuch
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 99.16% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown