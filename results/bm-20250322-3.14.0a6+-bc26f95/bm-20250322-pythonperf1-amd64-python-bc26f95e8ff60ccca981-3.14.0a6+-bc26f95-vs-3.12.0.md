# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-amd64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.032x faster
- HPT reliability: 62.61%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 417 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_io              | 731 ms                                                      | 430 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 338 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                       |
| nbody          | 71.9 ms                                                     | 67.3 ms: 1.07x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                                       |
| unpickle             | 8.18 us                                                     | 8.42 us: 1.03x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.0 us: 1.08x slower                                                       |
| pickle               | 7.43 us                                                     | 8.11 us: 1.09x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.13x slower                                                        |
| pickle_dict          | 18.4 us                                                     | 20.8 us: 1.13x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.92 ms: 1.22x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.52 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.3 ms: 1.25x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.84 ms: 1.04x faster                                                       |
| django_template | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.7 ms: 2.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 417 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_io              | 731 ms                                                      | 430 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 338 ms: 1.45x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.46 sec: 1.44x faster                                                      |
| deepcopy                   | 238 us                                                      | 186 us: 1.28x faster                                                        |
| float                      | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.0 us: 1.19x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.16x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 59.3 ms: 1.13x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| nbody                      | 71.9 ms                                                     | 67.3 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.96 us: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.04x faster                                                       |
| async_generators           | 239 ms                                                      | 230 ms: 1.04x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.84 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| chaos                      | 43.3 ms                                                     | 42.3 ms: 1.02x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| scimark_fft                | 184 ms                                                      | 181 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.7 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.4 ms: 1.02x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.62 ms: 1.03x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.42 us: 1.03x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 50.3 ms: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                        |
| raytrace                   | 192 ms                                                      | 200 ms: 1.04x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 61.2 ms: 1.04x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 82.4 ms: 1.05x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 78.3 ms: 1.05x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.30 ms: 1.06x slower                                                       |
| pycparser                  | 699 ms                                                      | 745 ms: 1.07x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.71 us: 1.07x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.22 us: 1.08x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.0 us: 1.08x slower                                                       |
| pyflate                    | 295 ms                                                      | 318 ms: 1.08x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 554 ms: 1.08x slower                                                        |
| asyncio_tcp                | 487 ms                                                      | 526 ms: 1.08x slower                                                        |
| richards                   | 28.4 ms                                                     | 30.7 ms: 1.08x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.44 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                        |
| pickle                     | 7.43 us                                                     | 8.11 us: 1.09x slower                                                       |
| richards_super             | 32.1 ms                                                     | 35.0 ms: 1.09x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.13x slower                                                        |
| pickle_dict                | 18.4 us                                                     | 20.8 us: 1.13x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.57 sec: 1.14x slower                                                      |
| fannkuch                   | 247 ms                                                      | 282 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.82 ms: 1.17x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.92 ms: 1.22x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.8 ms: 1.22x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.52 us: 1.24x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.3 ms: 1.25x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.8 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.08 ms: 1.36x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (6): json, regex_compile, logging_silent, unpickle_list, unpack_sequence, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 62.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown