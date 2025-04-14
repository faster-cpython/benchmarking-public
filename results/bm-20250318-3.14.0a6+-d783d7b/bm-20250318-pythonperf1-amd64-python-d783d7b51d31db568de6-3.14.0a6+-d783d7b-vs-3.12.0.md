# Results vs. 3.12.0

- fork: python
- ref: d783d7b51d31db568de6
- machine: windows-amd64
- commit hash: d783d7b
- commit date: 2025-03-18
- overall geometric mean: 1.033x faster
- HPT reliability: 67.69%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 418 ms: 1.84x faster                                                        |
| async_tree_io              | 731 ms                                                      | 429 ms: 1.70x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 219 ms: 1.67x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 181 ms: 1.58x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 346 ms: 1.42x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.58x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.5 ms: 1.22x faster                                                       |
| nbody          | 71.9 ms                                                     | 67.0 ms: 1.07x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 89.0 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.2 ms: 1.06x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.2 us: 1.09x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 152 us: 1.14x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 228 us: 1.17x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.93 ms: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                                       |
| django_template | 22.9 ms                                                     | 26.7 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.7 ms: 2.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 418 ms: 1.84x faster                                                        |
| async_tree_io              | 731 ms                                                      | 429 ms: 1.70x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 219 ms: 1.67x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 181 ms: 1.58x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 346 ms: 1.42x faster                                                        |
| deepcopy                   | 238 us                                                      | 187 us: 1.28x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 19.1 us: 1.24x faster                                                       |
| float                      | 56.8 ms                                                     | 46.5 ms: 1.22x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 57.2 ms: 1.17x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| nbody                      | 71.9 ms                                                     | 67.0 ms: 1.07x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.65 us: 1.07x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.00 us: 1.05x faster                                                       |
| async_generators           | 239 ms                                                      | 229 ms: 1.04x faster                                                        |
| regex_v8                   | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 58.9 ns: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.5 ms: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 90.4 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.53 ms: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.1 ms: 1.01x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.3 ms: 1.02x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 89.0 ms: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| bench_thread_pool          | 857 us                                                      | 878 us: 1.02x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 76.9 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.3 ms: 1.03x slower                                                       |
| raytrace                   | 192 ms                                                      | 199 ms: 1.03x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 60.9 ms: 1.03x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.3 ms: 1.04x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.2 ms: 1.04x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 81.9 ms: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.06x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 59.2 ms: 1.06x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 545 ms: 1.06x slower                                                        |
| pyflate                    | 295 ms                                                      | 314 ms: 1.07x slower                                                        |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                                        |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.82 us: 1.09x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.46 ms: 1.09x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.2 us: 1.09x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.36 us: 1.10x slower                                                       |
| fannkuch                   | 247 ms                                                      | 273 ms: 1.11x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 152 us: 1.14x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 228 us: 1.17x slower                                                        |
| django_template            | 22.9 ms                                                     | 26.7 ms: 1.17x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.4 ms: 1.18x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.96 ms: 1.20x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.93 ms: 1.22x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.8 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.06 ms: 1.36x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (3): scimark_fft, chaos, json
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250318-3.14.0a6+-d783d7b/bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 67.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown