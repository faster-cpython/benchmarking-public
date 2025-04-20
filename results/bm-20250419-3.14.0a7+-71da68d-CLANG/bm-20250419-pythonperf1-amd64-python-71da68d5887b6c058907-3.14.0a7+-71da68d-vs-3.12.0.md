# Results vs. 3.12.0

- fork: python
- ref: 71da68d5887b6c058907
- machine: windows-amd64
- commit hash: 71da68d
- commit date: 2025-04-19
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 204 ms: 1.07x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 351 ms: 2.20x faster                                                        |
| async_tree_io              | 731 ms                                                      | 344 ms: 2.13x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                        |
| async_tree_none            | 291 ms                                                      | 155 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 196 ms: 1.88x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 184 ms: 1.84x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 310 ms: 1.58x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.86x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 36.0 ms: 1.58x faster                                                       |
| nbody          | 71.9 ms                                                     | 55.2 ms: 1.30x faster                                                       |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 67.1 ms: 1.30x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.0 ms: 1.09x faster                                                       |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 11.8 us: 1.57x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.05 us: 1.38x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.05 us: 1.34x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.02 sec: 1.34x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 103 us: 1.30x faster                                                        |
| pickle               | 7.43 us                                                     | 6.06 us: 1.23x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 162 us: 1.21x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 47.7 ms: 1.17x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 32.8 ms: 1.15x faster                                                       |
| unpickle             | 8.18 us                                                     | 7.46 us: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.1 ms: 1.03x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.55 ms: 1.03x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.81 ms: 1.22x faster                                                       |
| django_template | 22.9 ms                                                     | 19.6 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.1 ms: 2.59x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 351 ms: 2.20x faster                                                        |
| async_tree_io              | 731 ms                                                      | 344 ms: 2.13x faster                                                        |
| mdp                        | 1.37 sec                                                    | 668 ms: 2.05x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                        |
| async_tree_none            | 291 ms                                                      | 155 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 196 ms: 1.88x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 184 ms: 1.84x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 13.1 us: 1.80x faster                                                       |
| deepcopy                   | 238 us                                                      | 136 us: 1.75x faster                                                        |
| comprehensions             | 14.1 us                                                     | 8.17 us: 1.73x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 48.4 ms: 1.63x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 27.0 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 310 ms: 1.58x faster                                                        |
| go                         | 91.6 ms                                                     | 58.0 ms: 1.58x faster                                                       |
| float                      | 56.8 ms                                                     | 36.0 ms: 1.58x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 11.8 us: 1.57x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.34 sec: 1.57x faster                                                      |
| generators                 | 22.5 ms                                                     | 15.0 ms: 1.50x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 41.4 ns: 1.46x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 46.3 ms: 1.45x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.46 us: 1.44x faster                                                       |
| chaos                      | 43.3 ms                                                     | 30.2 ms: 1.43x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 2.88 ms: 1.42x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.54 ms: 1.40x faster                                                       |
| raytrace                   | 192 ms                                                      | 138 ms: 1.40x faster                                                        |
| pickle_list                | 2.83 us                                                     | 2.05 us: 1.38x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 45.8 ms: 1.37x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.05 us: 1.34x faster                                                       |
| richards                   | 28.4 ms                                                     | 21.3 ms: 1.34x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 783 ms: 1.34x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.02 sec: 1.34x faster                                                      |
| scimark_fft                | 184 ms                                                      | 138 ms: 1.33x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 388 ms: 1.32x faster                                                        |
| richards_super             | 32.1 ms                                                     | 24.3 ms: 1.32x faster                                                       |
| async_generators           | 239 ms                                                      | 182 ms: 1.32x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 44.8 ms: 1.31x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 10.9 ms: 1.31x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 28.6 ns: 1.31x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 67.1 ms: 1.30x faster                                                       |
| nbody                      | 71.9 ms                                                     | 55.2 ms: 1.30x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 103 us: 1.30x faster                                                        |
| pyflate                    | 295 ms                                                      | 229 ms: 1.29x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 39.0 ms: 1.24x faster                                                       |
| pickle                     | 7.43 us                                                     | 6.06 us: 1.23x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.81 ms: 1.22x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 162 us: 1.21x faster                                                        |
| fannkuch                   | 247 ms                                                      | 205 ms: 1.21x faster                                                        |
| sympy_str                  | 175 ms                                                      | 146 ms: 1.20x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.19x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.48 us: 1.19x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 77.0 ms: 1.19x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 11.1 ms: 1.17x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 37.8 ms: 1.17x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 47.7 ms: 1.17x faster                                                       |
| django_template            | 22.9 ms                                                     | 19.6 ms: 1.17x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 424 ms: 1.15x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 32.8 ms: 1.15x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.51 us: 1.14x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 65.5 ms: 1.14x faster                                                       |
| sympy_expand               | 284 ms                                                      | 251 ms: 1.13x faster                                                        |
| logging_format             | 6.72 us                                                     | 5.95 us: 1.13x faster                                                       |
| unpickle                   | 8.18 us                                                     | 7.46 us: 1.10x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.0 ms: 1.09x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 87.3 us: 1.09x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| 2to3                       | 218 ms                                                      | 204 ms: 1.07x faster                                                        |
| pycparser                  | 699 ms                                                      | 653 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                       |
| json                       | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| telco                      | 4.13 ms                                                     | 3.96 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.1 ms: 1.03x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.55 ms: 1.03x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| coverage                   | 40.8 ms                                                     | 51.9 ms: 1.27x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.8 ms: 1.28x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.71 ms: 1.78x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.38 ms: 1.83x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                                |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown