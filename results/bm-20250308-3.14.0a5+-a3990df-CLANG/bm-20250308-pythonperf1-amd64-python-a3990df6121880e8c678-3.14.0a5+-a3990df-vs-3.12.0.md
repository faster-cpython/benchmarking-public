# Results vs. 3.12.0

- fork: python
- ref: a3990df6121880e8c678
- machine: windows-amd64
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.010x faster
- HPT reliability: 90.70%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.05x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 368 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 361 ms: 1.36x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| nbody          | 71.9 ms                                                     | 64.4 ms: 1.12x faster                                                       |
| pidigits       | 152 ms                                                      | 156 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 86.7 ms: 1.01x faster                                                       |
| regex_dna      | 126 ms                                                      | 130 ms: 1.03x slower                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.88 ms: 1.16x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 17.0 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 15.4 us: 1.19x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.53 us: 1.08x faster                                                       |
| pickle               | 7.43 us                                                     | 7.68 us: 1.03x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.95 us: 1.05x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 70.6 ms: 1.08x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 103 ms: 1.11x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                        |
| unpickle             | 8.18 us                                                     | 9.50 us: 1.16x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 66.7 ms: 1.19x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 46.4 ms: 1.23x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.80 ms: 1.37x slower                                                       |
| json_loads           | 13.9 us                                                     | 19.9 us: 1.43x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 21.3 ms: 1.31x slower                                                       |
| python_startup         | 19.5 ms                                                     | 27.3 ms: 1.40x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.35x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                       |
| mako            | 7.09 ms                                                     | 8.33 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.52x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                        |
| unpack_sequence            | 37.5 ns                                                     | 25.6 ns: 1.46x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.46 sec: 1.43x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 368 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 361 ms: 1.36x faster                                                        |
| generators                 | 22.5 ms                                                     | 16.9 ms: 1.33x faster                                                       |
| deepcopy                   | 238 us                                                      | 182 us: 1.31x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.21x faster                                                       |
| float                      | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 15.4 us: 1.19x faster                                                       |
| go                         | 91.6 ms                                                     | 76.7 ms: 1.19x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.1 us: 1.18x faster                                                       |
| nbody                      | 71.9 ms                                                     | 64.4 ms: 1.12x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.94 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                       |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                        |
| unpickle_list              | 2.75 us                                                     | 2.53 us: 1.08x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.0 ms: 1.07x faster                                                       |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.8 ms: 1.04x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.04x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 76.4 ms: 1.03x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 65.4 ms: 1.02x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 86.7 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.61 ms: 1.02x slower                                                       |
| pidigits                   | 152 ms                                                      | 156 ms: 1.02x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 93.6 ms: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.42 us: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.88 us: 1.02x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.20 ms: 1.03x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| regex_dna                  | 126 ms                                                      | 130 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                        |
| pickle                     | 7.43 us                                                     | 7.68 us: 1.03x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 531 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.04x slower                                                       |
| pyflate                    | 295 ms                                                      | 306 ms: 1.04x slower                                                        |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                        |
| pycparser                  | 699 ms                                                      | 725 ms: 1.04x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.0 ms: 1.04x slower                                                       |
| scimark_fft                | 184 ms                                                      | 192 ms: 1.04x slower                                                        |
| bench_thread_pool          | 857 us                                                      | 895 us: 1.05x slower                                                        |
| pickle_list                | 2.83 us                                                     | 2.95 us: 1.05x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 63.3 ns: 1.05x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 844 us: 1.05x slower                                                        |
| 2to3                       | 218 ms                                                      | 230 ms: 1.05x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.06x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.4 ms: 1.07x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.4 ms: 1.07x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 527 ms: 1.08x slower                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 70.6 ms: 1.08x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 53.0 ms: 1.09x slower                                                       |
| sympy_expand               | 284 ms                                                      | 311 ms: 1.10x slower                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 103 ms: 1.11x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                        |
| fannkuch                   | 247 ms                                                      | 281 ms: 1.14x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 67.8 ms: 1.15x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.50 us: 1.16x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.88 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                        |
| mako                       | 7.09 ms                                                     | 8.33 ms: 1.17x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.0 ms: 1.19x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 66.7 ms: 1.19x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.64 sec: 1.20x slower                                                      |
| json                       | 3.05 ms                                                     | 3.73 ms: 1.22x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 46.4 ms: 1.23x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.33 ms: 1.29x slower                                                       |
| coverage                   | 40.8 ms                                                     | 53.2 ms: 1.30x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 21.3 ms: 1.31x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 92.6 ms: 1.34x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.80 ms: 1.37x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.3 ms: 1.40x slower                                                       |
| json_loads                 | 13.9 us                                                     | 19.9 us: 1.43x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.61 ms: 1.71x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.82x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): tomli_loads, meteor_contest
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 90.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown