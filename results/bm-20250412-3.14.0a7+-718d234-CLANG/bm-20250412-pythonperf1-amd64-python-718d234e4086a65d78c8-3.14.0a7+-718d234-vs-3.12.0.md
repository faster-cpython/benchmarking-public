# Results vs. 3.12.0

- fork: python
- ref: 718d234e4086a65d78c8
- machine: windows-amd64
- commit hash: 718d234
- commit date: 2025-04-12
- overall geometric mean: 1.283x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 202 ms: 1.08x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 348 ms: 2.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 339 ms: 2.15x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 148 ms: 1.92x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 193 ms: 1.90x faster                                                        |
| async_tree_none            | 291 ms                                                      | 155 ms: 1.89x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 184 ms: 1.84x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 315 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 308 ms: 1.59x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.88x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 36.1 ms: 1.57x faster                                                       |
| nbody          | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 66.8 ms: 1.31x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.06x faster                                                       |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 12.1 us: 1.52x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.01 sec: 1.35x faster                                                      |
| pickle_list          | 2.83 us                                                     | 2.10 us: 1.35x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.04 us: 1.34x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 104 us: 1.28x faster                                                        |
| pickle               | 7.43 us                                                     | 6.18 us: 1.20x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 165 us: 1.19x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 47.6 ms: 1.17x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 32.7 ms: 1.15x faster                                                       |
| unpickle             | 8.18 us                                                     | 7.26 us: 1.13x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.6 us: 1.02x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.78 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.8 ms: 1.38x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.75 ms: 1.23x faster                                                       |
| django_template | 22.9 ms                                                     | 19.5 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.7 ms: 2.62x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 348 ms: 2.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 339 ms: 2.15x faster                                                        |
| mdp                        | 1.37 sec                                                    | 667 ms: 2.06x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 148 ms: 1.92x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 193 ms: 1.90x faster                                                        |
| async_tree_none            | 291 ms                                                      | 155 ms: 1.89x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 184 ms: 1.84x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 13.3 us: 1.78x faster                                                       |
| deepcopy                   | 238 us                                                      | 136 us: 1.75x faster                                                        |
| comprehensions             | 14.1 us                                                     | 8.30 us: 1.70x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 47.7 ms: 1.65x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 27.3 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 315 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 308 ms: 1.59x faster                                                        |
| float                      | 56.8 ms                                                     | 36.1 ms: 1.57x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.34 sec: 1.57x faster                                                      |
| go                         | 91.6 ms                                                     | 58.5 ms: 1.57x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 12.1 us: 1.52x faster                                                       |
| generators                 | 22.5 ms                                                     | 15.1 ms: 1.49x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 46.5 ms: 1.44x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 2.85 ms: 1.44x faster                                                       |
| chaos                      | 43.3 ms                                                     | 30.2 ms: 1.44x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.46 us: 1.43x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 42.4 ns: 1.43x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.55 ms: 1.40x faster                                                       |
| nbody                      | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                       |
| raytrace                   | 192 ms                                                      | 139 ms: 1.38x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 375 ms: 1.37x faster                                                        |
| richards                   | 28.4 ms                                                     | 20.8 ms: 1.37x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 770 ms: 1.36x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.01 sec: 1.35x faster                                                      |
| pickle_list                | 2.83 us                                                     | 2.10 us: 1.35x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.04 us: 1.34x faster                                                       |
| scimark_fft                | 184 ms                                                      | 137 ms: 1.34x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 46.9 ms: 1.34x faster                                                       |
| richards_super             | 32.1 ms                                                     | 24.1 ms: 1.33x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 10.9 ms: 1.31x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 66.8 ms: 1.31x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 45.0 ms: 1.31x faster                                                       |
| async_generators           | 239 ms                                                      | 184 ms: 1.30x faster                                                        |
| fannkuch                   | 247 ms                                                      | 190 ms: 1.30x faster                                                        |
| unpack_sequence            | 37.5 ns                                                     | 29.2 ns: 1.28x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 104 us: 1.28x faster                                                        |
| pyflate                    | 295 ms                                                      | 231 ms: 1.28x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 38.9 ms: 1.25x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.75 ms: 1.23x faster                                                       |
| pickle                     | 7.43 us                                                     | 6.18 us: 1.20x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.19x faster                                                       |
| sympy_str                  | 175 ms                                                      | 147 ms: 1.19x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 37.3 ms: 1.19x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 165 us: 1.19x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.49 us: 1.18x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 77.7 ms: 1.18x faster                                                       |
| django_template            | 22.9 ms                                                     | 19.5 ms: 1.18x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 11.0 ms: 1.17x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 47.6 ms: 1.17x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.41 us: 1.16x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 32.7 ms: 1.15x faster                                                       |
| logging_format             | 6.72 us                                                     | 5.89 us: 1.14x faster                                                       |
| sympy_expand               | 284 ms                                                      | 250 ms: 1.14x faster                                                        |
| unpickle                   | 8.18 us                                                     | 7.26 us: 1.13x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 435 ms: 1.12x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 67.0 ms: 1.11x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 86.6 us: 1.10x faster                                                       |
| json                       | 3.05 ms                                                     | 2.81 ms: 1.08x faster                                                       |
| 2to3                       | 218 ms                                                      | 202 ms: 1.08x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| pycparser                  | 699 ms                                                      | 648 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.06x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.6 us: 1.02x faster                                                       |
| telco                      | 4.13 ms                                                     | 4.05 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.78 ms: 1.02x slower                                                       |
| coverage                   | 40.8 ms                                                     | 42.5 ms: 1.04x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.0 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.8 ms: 1.38x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.38 ms: 1.84x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.86 ms: 1.88x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                                |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.283x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown