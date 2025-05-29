# Results vs. 3.12.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.196x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 206 ms: 1.06x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.56 sec: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 355 ms: 2.17x faster                                                        |
| async_tree_io              | 731 ms                                                      | 357 ms: 2.05x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 154 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 200 ms: 1.83x faster                                                        |
| async_tree_none            | 291 ms                                                      | 161 ms: 1.81x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 192 ms: 1.77x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 314 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 315 ms: 1.55x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.82x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.4 ms: 1.34x faster                                                       |
| nbody          | 71.9 ms                                                     | 57.7 ms: 1.25x faster                                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 74.6 ms: 1.17x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.4 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 11.8 us: 1.56x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.07 us: 1.36x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.11 us: 1.30x faster                                                       |
| pickle               | 7.43 us                                                     | 6.10 us: 1.22x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 116 us: 1.15x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 50.1 ms: 1.11x faster                                                       |
| unpickle             | 8.18 us                                                     | 7.50 us: 1.09x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.2 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 186 us: 1.05x faster                                                        |
| xml_etree_parse      | 93.0 ms                                                     | 89.6 ms: 1.04x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.78 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.9 ms: 1.29x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.14 ms: 1.16x faster                                                       |
| django_template | 22.9 ms                                                     | 21.3 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.4 ms: 2.56x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 355 ms: 2.17x faster                                                        |
| async_tree_io              | 731 ms                                                      | 357 ms: 2.05x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 154 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 200 ms: 1.83x faster                                                        |
| async_tree_none            | 291 ms                                                      | 161 ms: 1.81x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 192 ms: 1.77x faster                                                        |
| deepcopy                   | 238 us                                                      | 149 us: 1.60x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 314 ms: 1.60x faster                                                        |
| pickle_dict                | 18.4 us                                                     | 11.8 us: 1.56x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 315 ms: 1.55x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 45.2 ms: 1.48x faster                                                       |
| comprehensions             | 14.1 us                                                     | 9.62 us: 1.47x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.45x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 16.7 us: 1.42x faster                                                       |
| pickle_list                | 2.83 us                                                     | 2.07 us: 1.36x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.55 us: 1.35x faster                                                       |
| float                      | 56.8 ms                                                     | 42.4 ms: 1.34x faster                                                       |
| go                         | 91.6 ms                                                     | 68.7 ms: 1.33x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 45.7 ns: 1.32x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 33.1 ms: 1.32x faster                                                       |
| raytrace                   | 192 ms                                                      | 146 ms: 1.31x faster                                                        |
| generators                 | 22.5 ms                                                     | 17.3 ms: 1.30x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.11 us: 1.30x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 61.0 ms: 1.29x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 46.0 ms: 1.28x faster                                                       |
| chaos                      | 43.3 ms                                                     | 34.0 ms: 1.28x faster                                                       |
| async_generators           | 239 ms                                                      | 189 ms: 1.27x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 1.71 ms: 1.27x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.26 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.04 ms: 1.25x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 11.4 ms: 1.25x faster                                                       |
| nbody                      | 71.9 ms                                                     | 57.7 ms: 1.25x faster                                                       |
| richards_super             | 32.1 ms                                                     | 26.0 ms: 1.23x faster                                                       |
| richards                   | 28.4 ms                                                     | 23.1 ms: 1.23x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 51.2 ms: 1.23x faster                                                       |
| pickle                     | 7.43 us                                                     | 6.10 us: 1.22x faster                                                       |
| scimark_fft                | 184 ms                                                      | 152 ms: 1.22x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 74.6 ms: 1.17x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 898 ms: 1.16x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 442 ms: 1.16x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.14 ms: 1.16x faster                                                       |
| pyflate                    | 295 ms                                                      | 255 ms: 1.15x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 42.0 ms: 1.15x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 116 us: 1.15x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.53 us: 1.14x faster                                                       |
| logging_format             | 6.72 us                                                     | 5.95 us: 1.13x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.5 ms: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| sympy_str                  | 175 ms                                                      | 156 ms: 1.12x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 50.1 ms: 1.11x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 82.4 ms: 1.11x faster                                                       |
| json                       | 3.05 ms                                                     | 2.75 ms: 1.11x faster                                                       |
| unpickle                   | 8.18 us                                                     | 7.50 us: 1.09x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.0 ms: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| django_template            | 22.9 ms                                                     | 21.3 ms: 1.08x faster                                                       |
| sympy_expand               | 284 ms                                                      | 264 ms: 1.07x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 35.2 ms: 1.07x faster                                                       |
| fannkuch                   | 247 ms                                                      | 230 ms: 1.07x faster                                                        |
| regex_v8                   | 14.2 ms                                                     | 13.4 ms: 1.07x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.56 sec: 1.06x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 70.4 ms: 1.06x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 89.7 us: 1.06x faster                                                       |
| 2to3                       | 218 ms                                                      | 206 ms: 1.06x faster                                                        |
| pycparser                  | 699 ms                                                      | 663 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 186 us: 1.05x faster                                                        |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.6 ms: 1.04x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                      |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 37.7 ns: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.78 ms: 1.01x slower                                                       |
| coverage                   | 40.8 ms                                                     | 41.7 ms: 1.02x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.35 ms: 1.05x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 520 ms: 1.07x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 88.8 ms: 1.28x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.9 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.68 ms: 1.76x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.79x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.196x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown