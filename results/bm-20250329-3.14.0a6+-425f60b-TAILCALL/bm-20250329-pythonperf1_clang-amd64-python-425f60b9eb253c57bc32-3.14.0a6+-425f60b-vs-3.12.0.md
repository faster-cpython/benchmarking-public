# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.265x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 203 ms: 1.07x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.53 sec: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 350 ms: 2.20x faster                                                        |
| async_tree_io              | 731 ms                                                      | 350 ms: 2.09x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 151 ms: 1.89x faster                                                        |
| async_tree_none            | 291 ms                                                      | 157 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 198 ms: 1.86x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 189 ms: 1.80x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 317 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 312 ms: 1.57x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.84x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 36.9 ms: 1.54x faster                                                       |
| nbody          | 71.9 ms                                                     | 48.0 ms: 1.50x faster                                                       |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                       | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 69.1 ms: 1.27x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 12.4 ms: 1.15x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 106 us: 1.25x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 49.0 ms: 1.14x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 174 us: 1.12x faster                                                        |
| xml_etree_process    | 37.7 ms                                                     | 34.2 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.50 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.3 ms: 1.25x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.80 ms: 1.22x faster                                                       |
| django_template | 22.9 ms                                                     | 20.5 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.2 ms: 2.58x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 350 ms: 2.20x faster                                                        |
| async_tree_io              | 731 ms                                                      | 350 ms: 2.09x faster                                                        |
| mdp                        | 1.37 sec                                                    | 671 ms: 2.04x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 151 ms: 1.89x faster                                                        |
| async_tree_none            | 291 ms                                                      | 157 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 198 ms: 1.86x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 189 ms: 1.80x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 14.0 us: 1.70x faster                                                       |
| deepcopy                   | 238 us                                                      | 143 us: 1.67x faster                                                        |
| comprehensions             | 14.1 us                                                     | 8.60 us: 1.64x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 317 ms: 1.58x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 50.0 ms: 1.58x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 312 ms: 1.57x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 42.8 ms: 1.57x faster                                                       |
| float                      | 56.8 ms                                                     | 36.9 ms: 1.54x faster                                                       |
| go                         | 91.6 ms                                                     | 60.7 ms: 1.51x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 29.1 ms: 1.50x faster                                                       |
| nbody                      | 71.9 ms                                                     | 48.0 ms: 1.50x faster                                                       |
| generators                 | 22.5 ms                                                     | 15.3 ms: 1.47x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 41.8 ns: 1.45x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 2.96 ms: 1.39x faster                                                       |
| chaos                      | 43.3 ms                                                     | 31.4 ms: 1.38x faster                                                       |
| raytrace                   | 192 ms                                                      | 140 ms: 1.37x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 43.5 ms: 1.35x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.57 us: 1.34x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 10.7 ms: 1.33x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.62 ms: 1.33x faster                                                       |
| scimark_fft                | 184 ms                                                      | 139 ms: 1.33x faster                                                        |
| async_generators           | 239 ms                                                      | 183 ms: 1.31x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 48.4 ms: 1.30x faster                                                       |
| pyflate                    | 295 ms                                                      | 229 ms: 1.28x faster                                                        |
| richards                   | 28.4 ms                                                     | 22.2 ms: 1.28x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.01 ms: 1.27x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 405 ms: 1.27x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 69.1 ms: 1.27x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 828 ms: 1.26x faster                                                        |
| fannkuch                   | 247 ms                                                      | 196 ms: 1.26x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 106 us: 1.25x faster                                                        |
| richards_super             | 32.1 ms                                                     | 25.7 ms: 1.25x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 39.2 ms: 1.24x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.80 ms: 1.22x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.49 us: 1.19x faster                                                       |
| sympy_str                  | 175 ms                                                      | 149 ms: 1.18x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 78.7 ms: 1.16x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.2 ms: 1.16x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 12.4 ms: 1.15x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 11.3 ms: 1.14x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 49.0 ms: 1.14x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 65.9 ms: 1.13x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 174 us: 1.12x faster                                                        |
| django_template            | 22.9 ms                                                     | 20.5 ms: 1.12x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.62 us: 1.12x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.04 us: 1.11x faster                                                       |
| sympy_expand               | 284 ms                                                      | 257 ms: 1.10x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 34.2 ms: 1.10x faster                                                       |
| json                       | 3.05 ms                                                     | 2.78 ms: 1.10x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 87.6 us: 1.09x faster                                                       |
| pycparser                  | 699 ms                                                      | 645 ms: 1.08x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.53 sec: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                       |
| 2to3                       | 218 ms                                                      | 203 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 825 us: 1.04x faster                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.50 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| telco                      | 4.13 ms                                                     | 4.33 ms: 1.05x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.0 ms: 1.15x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.3 ms: 1.25x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.8 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.73 ms: 1.79x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.36 ms: 1.81x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                                |
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.265x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown