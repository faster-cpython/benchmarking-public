# Results vs. 3.12.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.010x faster
- HPT reliability: 97.39%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.79 sec: 1.68x slower                                                     |
| Geometric mean | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 322 ms: 2.39x faster                                                       |
| async_tree_io              | 731 ms                                                      | 344 ms: 2.12x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.97x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 187 ms: 1.96x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.74x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 304 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.85x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.6 ms: 1.25x faster                                                      |
| pidigits       | 152 ms                                                      | 134 ms: 1.14x faster                                                       |
| nbody          | 71.9 ms                                                     | 83.1 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 92.6 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 57.7 ms: 1.13x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.86 ms: 1.03x slower                                                      |
| pickle               | 7.43 us                                                     | 7.73 us: 1.04x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.7 us: 1.07x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.06 us: 1.08x slower                                                      |
| json_loads           | 13.9 us                                                     | 15.5 us: 1.11x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 63.1 ms: 1.13x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.14 us: 1.14x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.4 ms: 1.18x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 159 us: 1.19x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.80 us: 1.20x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 235 us: 1.20x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.42 sec: 1.77x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.1 ms: 1.17x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.2 ms: 1.19x slower                                                      |
| mako            | 7.09 ms                                                     | 9.92 ms: 1.40x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.29x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.7 ms: 2.81x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 322 ms: 2.39x faster                                                       |
| async_tree_io              | 731 ms                                                      | 344 ms: 2.12x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.97x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 187 ms: 1.96x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.74x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 304 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.14 ms: 1.34x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.34 us: 1.32x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.05 sec: 1.31x faster                                                     |
| float                      | 56.8 ms                                                     | 45.6 ms: 1.25x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                      |
| deepcopy                   | 238 us                                                      | 205 us: 1.16x faster                                                       |
| pidigits                   | 152 ms                                                      | 134 ms: 1.14x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.0 us: 1.13x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 57.7 ms: 1.13x faster                                                      |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.8 ms: 1.09x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 459 ms: 1.06x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.01x faster                                                      |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 62.0 ns: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.86 ms: 1.03x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.73 us: 1.04x slower                                                      |
| chaos                      | 43.3 ms                                                     | 45.2 ms: 1.04x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.00 us: 1.04x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 95.5 ms: 1.04x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.19 us: 1.04x slower                                                      |
| pyflate                    | 295 ms                                                      | 309 ms: 1.05x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.58 us: 1.05x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 92.6 ms: 1.06x slower                                                      |
| sympy_str                  | 175 ms                                                      | 187 ms: 1.07x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 40.1 ns: 1.07x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.7 us: 1.07x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.9 ms: 1.07x slower                                                      |
| async_generators           | 239 ms                                                      | 258 ms: 1.08x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 15.4 ms: 1.08x slower                                                      |
| raytrace                   | 192 ms                                                      | 207 ms: 1.08x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.06 us: 1.08x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 64.0 ms: 1.09x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 560 ms: 1.09x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 86.4 ms: 1.10x slower                                                      |
| json_loads                 | 13.9 us                                                     | 15.5 us: 1.11x slower                                                      |
| sympy_expand               | 284 ms                                                      | 316 ms: 1.11x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.59 ms: 1.12x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 77.5 ms: 1.12x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 63.1 ms: 1.13x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.44 ms: 1.13x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.14 us: 1.14x slower                                                      |
| scimark_fft                | 184 ms                                                      | 211 ms: 1.14x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 72.1 ms: 1.15x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 76.9 ms: 1.15x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 85.9 ms: 1.15x slower                                                      |
| nbody                      | 71.9 ms                                                     | 83.1 ms: 1.16x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 56.2 ms: 1.16x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.9 ms: 1.16x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.1 ms: 1.17x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.4 ms: 1.18x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.2 ms: 1.19x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 159 us: 1.19x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.80 us: 1.20x slower                                                      |
| richards                   | 28.4 ms                                                     | 34.1 ms: 1.20x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 235 us: 1.20x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.07 ms: 1.20x slower                                                      |
| fannkuch                   | 247 ms                                                      | 299 ms: 1.21x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.03 ms: 1.22x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.06 ms: 1.24x slower                                                      |
| richards_super             | 32.1 ms                                                     | 39.9 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 982 us: 1.31x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 127 us: 1.34x slower                                                       |
| mako                       | 7.09 ms                                                     | 9.92 ms: 1.40x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.63 sec: 1.56x slower                                                     |
| coverage                   | 40.8 ms                                                     | 67.7 ms: 1.66x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.79 sec: 1.68x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.42 sec: 1.77x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, go, generators
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250816-3.15.0a0-3663b2a-NOGIL/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 97.39% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown