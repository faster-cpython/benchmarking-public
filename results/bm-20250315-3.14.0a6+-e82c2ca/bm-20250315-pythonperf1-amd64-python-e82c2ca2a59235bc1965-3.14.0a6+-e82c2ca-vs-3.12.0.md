# Results vs. 3.12.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.035x faster
- HPT reliability: 64.88%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 416 ms: 1.85x faster                                                        |
| async_tree_io              | 731 ms                                                      | 427 ms: 1.71x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 342 ms: 1.43x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.40 ms: 1.15x faster                                                       |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 86.8 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.79 us: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.49 us: 1.04x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.8 ms: 1.05x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| pickle               | 7.43 us                                                     | 8.03 us: 1.08x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.1 us: 1.08x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.6 ms: 1.10x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 20.6 us: 1.12x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.14x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.99 ms: 1.23x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.51 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.84 ms: 1.04x faster                                                       |
| django_template | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.6 ms: 2.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 416 ms: 1.85x faster                                                        |
| async_tree_io              | 731 ms                                                      | 427 ms: 1.71x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.43 sec: 1.46x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 342 ms: 1.43x faster                                                        |
| deepcopy                   | 238 us                                                      | 188 us: 1.26x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 19.2 us: 1.24x faster                                                       |
| float                      | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 55.3 ms: 1.21x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.40 ms: 1.15x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.15x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.2 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.04x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.84 ms: 1.04x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| async_generators           | 239 ms                                                      | 234 ms: 1.02x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 59.5 ns: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.1 ms: 1.02x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 86.8 ms: 1.01x faster                                                       |
| chaos                      | 43.3 ms                                                     | 43.7 ms: 1.01x slower                                                       |
| json                       | 3.05 ms                                                     | 3.09 ms: 1.02x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.79 us: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| raytrace                   | 192 ms                                                      | 197 ms: 1.03x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 50.1 ms: 1.03x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.3 ms: 1.03x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.2 ms: 1.03x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 61.0 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.49 us: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                        |
| richards_super             | 32.1 ms                                                     | 33.4 ms: 1.04x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.5 ms: 1.04x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.8 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 83.4 ms: 1.06x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| pyflate                    | 295 ms                                                      | 314 ms: 1.07x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 547 ms: 1.07x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.39 ms: 1.07x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.73 us: 1.07x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 524 ms: 1.07x slower                                                        |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                        |
| pickle                     | 7.43 us                                                     | 8.03 us: 1.08x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.26 us: 1.08x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.08x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.6 ms: 1.10x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 41.4 ns: 1.10x slower                                                       |
| fannkuch                   | 247 ms                                                      | 276 ms: 1.12x slower                                                        |
| pickle_dict                | 18.4 us                                                     | 20.6 us: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.14x slower                                                        |
| django_template            | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                        |
| coverage                   | 40.8 ms                                                     | 48.0 ms: 1.18x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.64 sec: 1.19x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.92 ms: 1.19x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.99 ms: 1.23x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.51 us: 1.24x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.1 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.04 ms: 1.34x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (6): nbody, go, scimark_fft, scimark_monte_carlo, scimark_sparse_mat_mult, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 64.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown