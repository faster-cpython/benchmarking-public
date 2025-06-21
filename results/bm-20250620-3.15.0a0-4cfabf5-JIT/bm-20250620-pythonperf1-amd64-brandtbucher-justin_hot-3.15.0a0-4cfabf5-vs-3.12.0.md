# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.104x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                   |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                       | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                   |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                   |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                   |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                   |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                   |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.61x faster                                                   |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.46x faster                                                   |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                   |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.2 ms: 1.29x faster                                                  |
| nbody          | 71.9 ms                                                     | 56.4 ms: 1.27x faster                                                  |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                       | 1.19x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.5 ms: 1.10x faster                                                  |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                   |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                       | 1.03x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 112 us: 1.19x faster                                                   |
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                     | 52.2 ms: 1.07x faster                                                  |
| xml_etree_parse      | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                  |
| xml_etree_process    | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                  |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                  |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                   |
| json_dumps           | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                  |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.65 ms: 1.25x faster                                                  |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                  |
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                   |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                   |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                   |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                   |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                   |
| mdp                        | 1.37 sec                                                    | 820 ms: 1.67x faster                                                   |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.61x faster                                                   |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.46x faster                                                   |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                   |
| deepcopy                   | 238 us                                                      | 171 us: 1.40x faster                                                   |
| deepcopy_memo              | 23.7 us                                                     | 18.4 us: 1.29x faster                                                  |
| float                      | 56.8 ms                                                     | 44.2 ms: 1.29x faster                                                  |
| nbody                      | 71.9 ms                                                     | 56.4 ms: 1.27x faster                                                  |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                                  |
| mako                       | 7.09 ms                                                     | 5.65 ms: 1.25x faster                                                  |
| unpickle_pure_python       | 133 us                                                      | 112 us: 1.19x faster                                                   |
| scimark_fft                | 184 ms                                                      | 156 ms: 1.18x faster                                                   |
| go                         | 91.6 ms                                                     | 78.5 ms: 1.17x faster                                                  |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                 |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                  |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                  |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                  |
| spectral_norm              | 66.9 ms                                                     | 59.3 ms: 1.13x faster                                                  |
| pyflate                    | 295 ms                                                      | 263 ms: 1.12x faster                                                   |
| regex_compile              | 87.5 ms                                                     | 79.5 ms: 1.10x faster                                                  |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                                  |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.9 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.34 ms: 1.09x faster                                                  |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                     | 52.2 ms: 1.07x faster                                                  |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                   |
| xml_etree_parse            | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                  |
| nqueens                    | 62.8 ms                                                     | 59.4 ms: 1.06x faster                                                  |
| crypto_pyaes               | 48.5 ms                                                     | 45.9 ms: 1.06x faster                                                  |
| fannkuch                   | 247 ms                                                      | 236 ms: 1.04x faster                                                   |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                   |
| sympy_sum                  | 91.5 ms                                                     | 88.1 ms: 1.04x faster                                                  |
| scimark_sor                | 78.8 ms                                                     | 75.9 ms: 1.04x faster                                                  |
| xml_etree_process          | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                  |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                   |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                  |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                  |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                                  |
| meteor_contest             | 74.6 ms                                                     | 73.3 ms: 1.02x faster                                                  |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                  |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                  |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                  |
| hexiom                     | 4.10 ms                                                     | 4.13 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 513 ms                                                      | 518 ms: 1.01x slower                                                   |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                 |
| pycparser                  | 699 ms                                                      | 708 ms: 1.01x slower                                                   |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                  |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                   |
| logging_format             | 6.72 us                                                     | 6.86 us: 1.02x slower                                                  |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                  |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                  |
| logging_simple             | 6.28 us                                                     | 6.49 us: 1.03x slower                                                  |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                   |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                   |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                  |
| telco                      | 4.13 ms                                                     | 4.35 ms: 1.05x slower                                                  |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                   |
| json_dumps                 | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                  |
| typing_runtime_protocols   | 95.1 us                                                     | 107 us: 1.12x slower                                                   |
| coverage                   | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                                  |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                  |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                  |
| gc_traversal               | 1.52 ms                                                     | 2.16 ms: 1.42x slower                                                  |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                  |
| logging_silent             | 60.5 ns                                                     | 319 ns: 5.28x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                           |

Benchmark hidden because not significant (3): scimark_lu, regex_v8, pprint_pformat
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250620-3.15.0a0-4cfabf5-JIT/bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown