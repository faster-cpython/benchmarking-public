# Results vs. 3.12.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-amd64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.004x slower
- HPT reliability: 96.16%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 413 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 407 ms: 1.80x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 226 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.58x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 182 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 230 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 361 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 371 ms: 1.35x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.8 ms: 1.04x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 76.5 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.05x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 89.9 ms: 1.03x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 26.0 ms: 1.83x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.6 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.5 ms: 1.05x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 7.18 ms: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.15 ms: 1.01x slower                                                       |
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 413 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 407 ms: 1.80x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 226 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.58x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 182 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 230 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 361 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 371 ms: 1.35x faster                                                        |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.16x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 74.6 ms: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.05x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 812 us: 1.05x faster                                                        |
| go                         | 91.6 ms                                                     | 87.6 ms: 1.04x faster                                                       |
| float                      | 56.8 ms                                                     | 54.8 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| generators                 | 22.5 ms                                                     | 21.9 ms: 1.03x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.0 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.6 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.0 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.01x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.9 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.15 ms: 1.01x slower                                                       |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                        |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 64.3 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 89.9 ms: 1.03x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 69.1 ms: 1.03x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.2 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 722 ms: 1.03x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.04x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.5 ms: 1.05x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                      |
| json                       | 3.05 ms                                                     | 3.23 ms: 1.06x slower                                                       |
| nbody                      | 71.9 ms                                                     | 76.5 ms: 1.06x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.32 ms: 1.07x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 553 ms: 1.08x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 37.3 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.80 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 205 ms: 1.09x slower                                                        |
| pyflate                    | 295 ms                                                      | 323 ms: 1.10x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.10x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.1 ms: 1.10x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.52 ms: 1.10x slower                                                       |
| scimark_fft                | 184 ms                                                      | 205 ms: 1.11x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 67.3 ns: 1.11x slower                                                       |
| coverage                   | 40.8 ms                                                     | 45.5 ms: 1.12x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 903 us: 1.12x slower                                                        |
| richards_super             | 32.1 ms                                                     | 36.1 ms: 1.12x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 66.2 ms: 1.13x slower                                                       |
| richards                   | 28.4 ms                                                     | 32.4 ms: 1.14x slower                                                       |
| fannkuch                   | 247 ms                                                      | 282 ms: 1.14x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.75 ms: 1.15x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 91.8 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.17x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 81.6 ms: 1.18x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.92 ms: 1.26x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.18 ms: 1.26x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.09 ms: 1.46x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 26.0 ms: 1.83x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (3): docutils, raytrace, logging_format
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 96.16% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown