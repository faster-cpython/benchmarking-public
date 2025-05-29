# Results vs. 3.12.0

- fork: python
- ref: 4f18916c5c28321f363e
- machine: windows-amd64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 201 ms: 1.09x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 352 ms: 2.19x faster                                                        |
| async_tree_io              | 731 ms                                                      | 345 ms: 2.12x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 194 ms: 1.90x faster                                                        |
| async_tree_none            | 291 ms                                                      | 156 ms: 1.86x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 184 ms: 1.84x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 318 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 313 ms: 1.56x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.86x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 35.9 ms: 1.58x faster                                                       |
| nbody          | 71.9 ms                                                     | 54.1 ms: 1.33x faster                                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 67.2 ms: 1.30x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 12.7 ms: 1.13x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                       |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 11.5 us: 1.60x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.05 us: 1.38x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.03 sec: 1.33x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 102 us: 1.31x faster                                                        |
| unpickle_list        | 2.75 us                                                     | 2.18 us: 1.26x faster                                                       |
| pickle               | 7.43 us                                                     | 6.02 us: 1.23x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 164 us: 1.19x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 46.9 ms: 1.19x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 32.7 ms: 1.15x faster                                                       |
| unpickle             | 8.18 us                                                     | 7.41 us: 1.10x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.87 ms: 1.03x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 68.1 ms: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                       |
| python_startup         | 19.5 ms                                                     | 27.9 ms: 1.43x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.35x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.98 ms: 1.18x faster                                                       |
| django_template | 22.9 ms                                                     | 19.8 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.0 ms: 2.59x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 352 ms: 2.19x faster                                                        |
| async_tree_io              | 731 ms                                                      | 345 ms: 2.12x faster                                                        |
| mdp                        | 1.37 sec                                                    | 672 ms: 2.04x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 194 ms: 1.90x faster                                                        |
| async_tree_none            | 291 ms                                                      | 156 ms: 1.86x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 184 ms: 1.84x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 13.0 us: 1.82x faster                                                       |
| deepcopy                   | 238 us                                                      | 135 us: 1.76x faster                                                        |
| comprehensions             | 14.1 us                                                     | 8.45 us: 1.67x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 47.2 ms: 1.67x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 26.8 ms: 1.63x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 11.5 us: 1.60x faster                                                       |
| float                      | 56.8 ms                                                     | 35.9 ms: 1.58x faster                                                       |
| go                         | 91.6 ms                                                     | 58.1 ms: 1.58x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 318 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 313 ms: 1.56x faster                                                        |
| generators                 | 22.5 ms                                                     | 15.0 ms: 1.51x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 40.9 ns: 1.48x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.44 us: 1.46x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.45x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 46.2 ms: 1.45x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 2.87 ms: 1.43x faster                                                       |
| chaos                      | 43.3 ms                                                     | 30.7 ms: 1.41x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.53 ms: 1.41x faster                                                       |
| raytrace                   | 192 ms                                                      | 139 ms: 1.38x faster                                                        |
| pickle_list                | 2.83 us                                                     | 2.05 us: 1.38x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 46.2 ms: 1.36x faster                                                       |
| richards                   | 28.4 ms                                                     | 21.0 ms: 1.35x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.03 sec: 1.33x faster                                                      |
| richards_super             | 32.1 ms                                                     | 24.1 ms: 1.33x faster                                                       |
| nbody                      | 71.9 ms                                                     | 54.1 ms: 1.33x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 793 ms: 1.32x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 102 us: 1.31x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 67.2 ms: 1.30x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 394 ms: 1.30x faster                                                        |
| scimark_fft                | 184 ms                                                      | 142 ms: 1.30x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 11.0 ms: 1.30x faster                                                       |
| pyflate                    | 295 ms                                                      | 228 ms: 1.29x faster                                                        |
| async_generators           | 239 ms                                                      | 187 ms: 1.28x faster                                                        |
| unpack_sequence            | 37.5 ns                                                     | 29.5 ns: 1.27x faster                                                       |
| fannkuch                   | 247 ms                                                      | 194 ms: 1.27x faster                                                        |
| unpickle_list              | 2.75 us                                                     | 2.18 us: 1.26x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 46.8 ms: 1.26x faster                                                       |
| pickle                     | 7.43 us                                                     | 6.02 us: 1.23x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 39.3 ms: 1.23x faster                                                       |
| sympy_str                  | 175 ms                                                      | 146 ms: 1.20x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 164 us: 1.19x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 46.9 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.15 ms: 1.19x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.98 ms: 1.18x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 10.9 ms: 1.18x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 77.5 ms: 1.18x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.49 us: 1.18x faster                                                       |
| django_template            | 22.9 ms                                                     | 19.8 ms: 1.16x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 64.6 ms: 1.16x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 32.7 ms: 1.15x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.4 ms: 1.15x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.54 us: 1.13x faster                                                       |
| logging_format             | 6.72 us                                                     | 5.93 us: 1.13x faster                                                       |
| sympy_expand               | 284 ms                                                      | 252 ms: 1.13x faster                                                        |
| regex_v8                   | 14.2 ms                                                     | 12.7 ms: 1.13x faster                                                       |
| pycparser                  | 699 ms                                                      | 630 ms: 1.11x faster                                                        |
| unpickle                   | 8.18 us                                                     | 7.41 us: 1.10x faster                                                       |
| 2to3                       | 218 ms                                                      | 201 ms: 1.09x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 88.9 us: 1.07x faster                                                       |
| json                       | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 834 us: 1.03x faster                                                        |
| telco                      | 4.13 ms                                                     | 4.08 ms: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                       |
| coverage                   | 40.8 ms                                                     | 41.5 ms: 1.02x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.87 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 68.1 ms: 1.05x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 516 ms: 1.06x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.5 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.9 ms: 1.43x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.83x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.80 ms: 1.84x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                                |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown