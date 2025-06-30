# Results vs. 3.12.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.095x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 390 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.1 ms: 1.29x faster                                                      |
| nbody          | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.0 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 38.7 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.57 us: 1.05x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.94 us: 1.07x slower                                                      |
| pickle               | 7.43 us                                                     | 8.09 us: 1.09x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.1 us: 1.09x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.34 ms: 1.11x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.36 us: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.58 ms: 1.08x faster                                                      |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 390 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| mdp                        | 1.37 sec                                                    | 811 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.32 sec: 1.59x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                       |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.32x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 44.1 ms: 1.29x faster                                                      |
| go                         | 91.6 ms                                                     | 77.5 ms: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 428 ms: 1.14x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 79.0 ms: 1.11x faster                                                      |
| nbody                      | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.7 ns: 1.09x faster                                                      |
| raytrace                   | 192 ms                                                      | 177 ms: 1.08x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 61.9 ms: 1.08x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.58 ms: 1.08x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.5 ms: 1.07x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.0 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| async_generators           | 239 ms                                                      | 226 ms: 1.06x faster                                                       |
| scimark_fft                | 184 ms                                                      | 175 ms: 1.05x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.00 us: 1.05x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 493 ms: 1.04x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.2 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.0 ms: 1.04x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.49 us: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| pyflate                    | 295 ms                                                      | 287 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.02 sec: 1.02x faster                                                     |
| deltablue                  | 2.16 ms                                                     | 2.13 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.53 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 62.1 ms: 1.01x faster                                                      |
| json                       | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.2 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                       |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 59.7 ms: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 288 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 4.19 ms: 1.02x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.7 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.57 us: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.94 us: 1.07x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                       |
| fannkuch                   | 247 ms                                                      | 267 ms: 1.08x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 40.6 ns: 1.08x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.09 us: 1.09x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.1 us: 1.09x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.34 ms: 1.11x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.61 ms: 1.12x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.36 us: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.8 ms: 1.19x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 95.9 ms: 1.39x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.21 ms: 1.45x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (2): bench_thread_pool, pycparser
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.095x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown