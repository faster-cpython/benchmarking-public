# Results vs. 3.12.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-amd64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.035x faster
- HPT reliability: 51.52%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                        |
| async_tree_io              | 731 ms                                                      | 411 ms: 1.78x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 49.6 ms: 1.14x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 72.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 112 ms: 1.12x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 85.1 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.8 ms: 1.05x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.72 us: 1.07x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.94 us: 1.07x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 143 us: 1.07x slower                                                        |
| pickle               | 7.43 us                                                     | 8.13 us: 1.09x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                        |
| pickle_dict          | 18.4 us                                                     | 20.6 us: 1.12x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.63 ms: 1.16x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.50 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.6 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                                       |
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                        |
| async_tree_io              | 731 ms                                                      | 411 ms: 1.78x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.40 sec: 1.49x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.41x faster                                                        |
| deepcopy                   | 238 us                                                      | 180 us: 1.32x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.8 us: 1.19x faster                                                       |
| float                      | 56.8 ms                                                     | 49.6 ms: 1.14x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.12x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                       |
| go                         | 91.6 ms                                                     | 84.1 ms: 1.09x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 61.5 ms: 1.09x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.4 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 827 us: 1.04x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| async_generators           | 239 ms                                                      | 232 ms: 1.03x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 47.1 ms: 1.03x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 85.1 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.3 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.4 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.8 ms: 1.02x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 79.6 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 58.6 ms: 1.00x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 61.1 ns: 1.01x slower                                                       |
| nbody                      | 71.9 ms                                                     | 72.7 ms: 1.01x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 35.6 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.1 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                        |
| pycparser                  | 699 ms                                                      | 723 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 531 ms: 1.04x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 77.4 ms: 1.04x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.25 ms: 1.04x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.8 ms: 1.05x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 83.1 ms: 1.05x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.06x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                       |
| fannkuch                   | 247 ms                                                      | 262 ms: 1.06x slower                                                        |
| json                       | 3.05 ms                                                     | 3.23 ms: 1.06x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.72 us: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 302 ms: 1.07x slower                                                        |
| unpickle_list              | 2.75 us                                                     | 2.94 us: 1.07x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 862 us: 1.07x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 143 us: 1.07x slower                                                        |
| pyflate                    | 295 ms                                                      | 317 ms: 1.07x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                      |
| richards                   | 28.4 ms                                                     | 30.9 ms: 1.09x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.9 ms: 1.09x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.13 us: 1.09x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 538 ms: 1.10x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                        |
| pickle_dict                | 18.4 us                                                     | 20.6 us: 1.12x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.9 ms: 1.15x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.63 ms: 1.16x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 83.2 ms: 1.20x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.6 ms: 1.21x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.50 us: 1.24x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.00 ms: 1.31x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.63x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (6): raytrace, scimark_sparse_mat_mult, logging_simple, scimark_fft, sympy_str, unpack_sequence
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 51.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown