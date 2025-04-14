# Results vs. 3.12.0

- fork: python
- ref: 014223649c33b2febbcc
- machine: windows-amd64
- commit hash: 0142236
- commit date: 2025-02-25
- overall geometric mean: 1.051x faster
- HPT reliability: 69.69%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 219 ms: 1.55x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 342 ms: 1.43x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                       |
| nbody          | 71.9 ms                                                     | 69.2 ms: 1.04x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 85.6 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.5 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.1 ms: 1.01x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.75 ms: 1.05x faster                                                       |
| django_template | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.2 ms: 2.66x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 219 ms: 1.55x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 342 ms: 1.43x faster                                                        |
| deepcopy                   | 238 us                                                      | 181 us: 1.32x faster                                                        |
| float                      | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.9 us: 1.19x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 58.4 ms: 1.15x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.0 ms: 1.10x faster                                                       |
| async_generators           | 239 ms                                                      | 219 ms: 1.09x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                       |
| go                         | 91.6 ms                                                     | 85.5 ms: 1.07x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.9 ms: 1.06x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.75 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.5 ms: 1.04x faster                                                       |
| nbody                      | 71.9 ms                                                     | 69.2 ms: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.7 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.2 ms: 1.03x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 85.6 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| raytrace                   | 192 ms                                                      | 191 ms: 1.01x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 60.7 ns: 1.00x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.1 ms: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 63.2 ms: 1.01x slower                                                       |
| scimark_fft                | 184 ms                                                      | 186 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 34.9 ms: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.8 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.86 us: 1.02x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                        |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| pyflate                    | 295 ms                                                      | 303 ms: 1.03x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| richards                   | 28.4 ms                                                     | 29.3 ms: 1.03x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.48 us: 1.03x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.6 ms: 1.05x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.07 ms: 1.05x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 82.7 ms: 1.05x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 62.6 ms: 1.06x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.37 ms: 1.06x slower                                                       |
| pycparser                  | 699 ms                                                      | 746 ms: 1.07x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 865 us: 1.08x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 557 ms: 1.08x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                        |
| fannkuch                   | 247 ms                                                      | 270 ms: 1.10x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.1 ms: 1.13x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.67 ms: 1.13x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 84.8 ms: 1.23x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.00 ms: 1.31x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (8): bench_thread_pool, scimark_sparse_mat_mult, sympy_str, docutils, crypto_pyaes, regex_v8, deltablue, scimark_monte_carlo
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250225-3.14.0a5+-0142236/bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 69.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown