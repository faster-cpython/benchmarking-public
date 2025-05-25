# Results vs. 3.12.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.095x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 381 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 390 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                       |
| async_tree_none            | 291 ms                                                      | 165 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 199 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.72x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.9 ms: 1.32x faster                                                      |
| nbody          | 71.9 ms                                                     | 60.1 ms: 1.20x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.4 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 111 us: 1.20x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.73 us: 1.01x faster                                                      |
| pickle               | 7.43 us                                                     | 7.52 us: 1.01x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.47 us: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.5 us: 1.06x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.20 ms: 1.09x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.31 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                      |
| python_startup         | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.54 ms: 1.28x faster                                                      |
| django_template | 22.9 ms                                                     | 23.6 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.5 ms: 2.73x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 381 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 390 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                       |
| async_tree_none            | 291 ms                                                      | 165 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 199 ms: 1.70x faster                                                       |
| mdp                        | 1.37 sec                                                    | 816 ms: 1.68x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.29 sec: 1.62x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 168 us: 1.42x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                      |
| float                      | 56.8 ms                                                     | 42.9 ms: 1.32x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.54 ms: 1.28x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 388 ms: 1.26x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 111 us: 1.20x faster                                                       |
| nbody                      | 71.9 ms                                                     | 60.1 ms: 1.20x faster                                                      |
| go                         | 91.6 ms                                                     | 77.4 ms: 1.18x faster                                                      |
| scimark_fft                | 184 ms                                                      | 156 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.78 us: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.17x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.52 us: 1.16x faster                                                      |
| pyflate                    | 295 ms                                                      | 257 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.26 ms: 1.13x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.3 ms: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.4 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.6 ms: 1.10x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 60.7 ms: 1.10x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 72.8 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 59.1 ms: 1.06x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 86.7 ms: 1.06x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.9 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.05x faster                                                      |
| fannkuch                   | 247 ms                                                      | 236 ms: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.7 ms: 1.04x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 56.7 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                                      |
| unpickle_list              | 2.75 us                                                     | 2.73 us: 1.01x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.15 ms: 1.00x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.13 ms: 1.01x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.52 us: 1.01x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 76.3 ms: 1.02x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.6 ms: 1.03x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.47 us: 1.03x slower                                                      |
| sympy_expand               | 284 ms                                                      | 294 ms: 1.04x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.29 ms: 1.04x slower                                                      |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.5 us: 1.06x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.20 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.14x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.31 us: 1.17x slower                                                      |
| python_startup             | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 91.4 ms: 1.32x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.15 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.30 ms: 1.72x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 307 ns: 5.08x slower                                                       |
| coverage                   | 40.8 ms                                                     | 288 ms: 7.06x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (9): pycparser, logging_simple, pprint_safe_repr, bench_thread_pool, logging_format, 2to3, docutils, pprint_pformat, unpack_sequence
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.095x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown