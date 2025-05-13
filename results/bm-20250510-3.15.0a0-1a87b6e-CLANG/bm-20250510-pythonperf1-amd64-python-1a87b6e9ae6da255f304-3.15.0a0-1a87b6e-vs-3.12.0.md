# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.225x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 212 ms: 1.03x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.56 sec: 1.06x faster                                                     |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 358 ms: 2.16x faster                                                       |
| async_tree_io              | 731 ms                                                      | 366 ms: 2.00x faster                                                       |
| async_tree_none            | 291 ms                                                      | 151 ms: 1.93x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 153 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 197 ms: 1.86x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 188 ms: 1.81x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 319 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 315 ms: 1.55x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.83x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 38.0 ms: 1.50x faster                                                      |
| nbody          | 71.9 ms                                                     | 52.5 ms: 1.37x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.29x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 68.1 ms: 1.28x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.0 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 11.8 us: 1.57x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.04 sec: 1.32x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 103 us: 1.29x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.22 us: 1.27x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.22 us: 1.24x faster                                                      |
| pickle               | 7.43 us                                                     | 6.26 us: 1.19x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 167 us: 1.17x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 47.9 ms: 1.17x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 33.2 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| unpickle             | 8.18 us                                                     | 7.86 us: 1.04x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.90 ms: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.25x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.1 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.94 ms: 1.19x faster                                                      |
| django_template | 22.9 ms                                                     | 20.3 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.9 ms: 2.61x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 358 ms: 2.16x faster                                                       |
| mdp                        | 1.37 sec                                                    | 684 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 366 ms: 2.00x faster                                                       |
| async_tree_none            | 291 ms                                                      | 151 ms: 1.93x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 153 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 197 ms: 1.86x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 188 ms: 1.81x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 13.3 us: 1.78x faster                                                      |
| deepcopy                   | 238 us                                                      | 137 us: 1.73x faster                                                       |
| comprehensions             | 14.1 us                                                     | 8.73 us: 1.62x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 49.0 ms: 1.61x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 319 ms: 1.57x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 11.8 us: 1.57x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 315 ms: 1.55x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 28.2 ms: 1.55x faster                                                      |
| go                         | 91.6 ms                                                     | 59.5 ms: 1.54x faster                                                      |
| generators                 | 22.5 ms                                                     | 14.7 ms: 1.53x faster                                                      |
| float                      | 56.8 ms                                                     | 38.0 ms: 1.50x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.44x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.48 us: 1.41x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 2.92 ms: 1.40x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 48.1 ms: 1.39x faster                                                      |
| chaos                      | 43.3 ms                                                     | 31.2 ms: 1.39x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.56 ms: 1.38x faster                                                      |
| nbody                      | 71.9 ms                                                     | 52.5 ms: 1.37x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 47.3 ms: 1.33x faster                                                      |
| richards                   | 28.4 ms                                                     | 21.4 ms: 1.32x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.04 sec: 1.32x faster                                                     |
| scimark_lu                 | 58.9 ms                                                     | 45.1 ms: 1.30x faster                                                      |
| richards_super             | 32.1 ms                                                     | 24.6 ms: 1.30x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 805 ms: 1.30x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 103 us: 1.29x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 68.1 ms: 1.28x faster                                                      |
| scimark_fft                | 184 ms                                                      | 145 ms: 1.27x faster                                                       |
| pickle_list                | 2.83 us                                                     | 2.22 us: 1.27x faster                                                      |
| raytrace                   | 192 ms                                                      | 151 ms: 1.27x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 29.8 ns: 1.26x faster                                                      |
| pyflate                    | 295 ms                                                      | 234 ms: 1.26x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 11.5 ms: 1.24x faster                                                      |
| fannkuch                   | 247 ms                                                      | 199 ms: 1.24x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.22 us: 1.24x faster                                                      |
| async_generators           | 239 ms                                                      | 194 ms: 1.23x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 39.6 ms: 1.22x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.94 ms: 1.19x faster                                                      |
| pickle                     | 7.43 us                                                     | 6.26 us: 1.19x faster                                                      |
| sympy_str                  | 175 ms                                                      | 149 ms: 1.17x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 167 us: 1.17x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 47.9 ms: 1.17x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 78.6 ms: 1.16x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 11.1 ms: 1.16x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 38.9 ms: 1.14x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 33.2 ms: 1.13x faster                                                      |
| django_template            | 22.9 ms                                                     | 20.3 ms: 1.13x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 66.3 ms: 1.13x faster                                                      |
| sympy_expand               | 284 ms                                                      | 255 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.31 ms: 1.11x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.0 ms: 1.10x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.74 us: 1.09x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.16 us: 1.09x faster                                                      |
| pycparser                  | 699 ms                                                      | 651 ms: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.56 sec: 1.06x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| unpickle                   | 8.18 us                                                     | 7.86 us: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 91.7 us: 1.04x faster                                                      |
| 2to3                       | 218 ms                                                      | 212 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.90 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 524 ms: 1.07x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.25x slower                                                      |
| python_startup             | 19.5 ms                                                     | 27.1 ms: 1.39x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 98.4 ms: 1.42x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.89 ms: 1.90x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.45 ms: 1.93x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 273 ns: 4.52x slower                                                       |
| coverage                   | 40.8 ms                                                     | 219 ms: 5.35x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (2): bench_thread_pool, telco
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.225x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown