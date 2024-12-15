# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-amd64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.011x faster
- HPT reliability: 88.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 184 ms: 1.58x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 227 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 356 ms: 1.41x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 356 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.4 ms: 1.04x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 79.5 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.40 ms: 1.16x faster                                                       |
| regex_dna      | 126 ms                                                      | 111 ms: 1.14x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 89.2 ms: 1.02x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 24.5 ms: 1.72x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 57.5 ms: 1.03x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.3 ms: 1.09x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.11x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.54 sec: 1.13x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 222 us: 1.13x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.76 ms: 1.05x faster                                                       |
| django_template | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 184 ms: 1.58x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 227 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 356 ms: 1.41x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 356 ms: 1.37x faster                                                        |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.40 ms: 1.16x faster                                                       |
| regex_dna                  | 126 ms                                                      | 111 ms: 1.14x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 21.1 us: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 62.0 ms: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.9 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.76 ms: 1.05x faster                                                       |
| float                      | 56.8 ms                                                     | 54.4 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 823 us: 1.04x faster                                                        |
| go                         | 91.6 ms                                                     | 88.0 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.9 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 89.2 ms: 1.03x faster                                                       |
| generators                 | 22.5 ms                                                     | 22.2 ms: 1.02x faster                                                       |
| raytrace                   | 192 ms                                                      | 191 ms: 1.01x faster                                                        |
| async_generators           | 239 ms                                                      | 238 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.57 ms: 1.00x slower                                                       |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.00x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 60.8 ns: 1.01x slower                                                       |
| chaos                      | 43.3 ms                                                     | 43.9 ms: 1.01x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 89.2 ms: 1.02x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.4 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.86 us: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| scimark_fft                | 184 ms                                                      | 189 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.42 us: 1.02x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 57.5 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.5 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.9 ms: 1.04x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 61.5 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 195 ms: 1.04x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.04x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.31 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 737 ms: 1.05x slower                                                        |
| pyflate                    | 295 ms                                                      | 313 ms: 1.06x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                      |
| sympy_expand               | 284 ms                                                      | 302 ms: 1.07x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.2 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 556 ms: 1.08x slower                                                        |
| django_template            | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.3 ms: 1.09x slower                                                       |
| fannkuch                   | 247 ms                                                      | 271 ms: 1.10x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 87.1 ms: 1.11x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.11x slower                                                        |
| nbody                      | 71.9 ms                                                     | 79.5 ms: 1.11x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 891 us: 1.11x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.54 sec: 1.13x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.0 ms: 1.13x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 222 us: 1.13x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.76 ms: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.0 ms: 1.18x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 81.9 ms: 1.18x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.19x slower                                                        |
| mypy2                      | 509 ms                                                      | 632 ms: 1.24x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.98 ms: 1.30x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 24.5 ms: 1.72x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): docutils, nqueens
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 88.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown