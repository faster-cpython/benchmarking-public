# Results vs. 3.12.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.137x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 215 ms: 1.02x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 378 ms: 2.04x faster                                                       |
| async_tree_io              | 731 ms                                                      | 379 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 336 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.9 ms: 1.31x faster                                                      |
| float          | 56.8 ms                                                     | 43.5 ms: 1.30x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.0 ms: 1.12x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 107 us: 1.25x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 49.9 ms: 1.12x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.47 ms: 1.04x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 200 us: 1.02x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.86 us: 1.04x slower                                                      |
| pickle               | 7.43 us                                                     | 7.85 us: 1.06x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.89 us: 1.09x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.5 us: 1.11x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.27 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.43 ms: 1.31x faster                                                      |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.6 ms: 2.72x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 378 ms: 2.04x faster                                                       |
| async_tree_io              | 731 ms                                                      | 379 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| mdp                        | 1.37 sec                                                    | 811 ms: 1.69x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 336 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.46x faster                                                     |
| deepcopy                   | 238 us                                                      | 165 us: 1.45x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.7 us: 1.42x faster                                                      |
| scimark_fft                | 184 ms                                                      | 137 ms: 1.34x faster                                                       |
| nbody                      | 71.9 ms                                                     | 54.9 ms: 1.31x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.43 ms: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 43.5 ms: 1.30x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 107 us: 1.25x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 839 ms: 1.25x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 412 ms: 1.24x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| go                         | 91.6 ms                                                     | 75.8 ms: 1.21x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.76 us: 1.19x faster                                                      |
| pyflate                    | 295 ms                                                      | 250 ms: 1.18x faster                                                       |
| fannkuch                   | 247 ms                                                      | 213 ms: 1.16x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.24 ms: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.0 ms: 1.12x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 49.9 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.4 ms: 1.11x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.1 ms: 1.10x faster                                                      |
| raytrace                   | 192 ms                                                      | 176 ms: 1.10x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.7 ms: 1.09x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.5 ns: 1.09x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 45.0 ms: 1.08x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.85 us: 1.07x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 35.4 ns: 1.06x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.37 us: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.0 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.0 ms: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 64.0 ms: 1.04x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.47 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.9 ms: 1.04x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 76.1 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| telco                      | 4.13 ms                                                     | 4.04 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| 2to3                       | 218 ms                                                      | 215 ms: 1.02x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 58.3 ms: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| hexiom                     | 4.10 ms                                                     | 4.14 ms: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 200 us: 1.02x slower                                                       |
| pycparser                  | 699 ms                                                      | 716 ms: 1.03x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                       |
| sympy_expand               | 284 ms                                                      | 291 ms: 1.03x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.86 us: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.85 us: 1.06x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.89 us: 1.09x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.5 us: 1.11x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.27 us: 1.16x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.2 ms: 1.25x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 90.1 ms: 1.30x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.12 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.29 ms: 1.72x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (3): bench_thread_pool, regex_v8, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.137x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown