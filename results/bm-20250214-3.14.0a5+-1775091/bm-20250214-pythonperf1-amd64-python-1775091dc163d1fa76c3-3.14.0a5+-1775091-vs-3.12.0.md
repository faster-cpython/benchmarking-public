# Results vs. 3.12.0

- fork: python
- ref: 1775091dc163d1fa76c3
- machine: windows-amd64
- commit hash: 1775091
- commit date: 2025-02-14
- overall geometric mean: 1.052x faster
- HPT reliability: 63.22%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                       |
| nbody          | 71.9 ms                                                     | 69.7 ms: 1.03x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 84.2 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.8 ms: 1.05x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 143 us: 1.08x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.10x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 221 us: 1.13x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.69 ms: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.5 ms: 1.26x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.63 ms: 1.07x faster                                                       |
| django_template | 22.9 ms                                                     | 25.1 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.4 ms: 2.74x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                        |
| float                      | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.5 us: 1.21x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 60.6 ms: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.10x faster                                                       |
| async_generators           | 239 ms                                                      | 219 ms: 1.09x faster                                                        |
| go                         | 91.6 ms                                                     | 84.4 ms: 1.08x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.63 ms: 1.07x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.5 ns: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.7 ms: 1.04x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 84.2 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| nbody                      | 71.9 ms                                                     | 69.7 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.2 ms: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 837 us: 1.02x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 62.0 ms: 1.01x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.57 ms: 1.01x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                       |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                       |
| pyflate                    | 295 ms                                                      | 299 ms: 1.01x slower                                                        |
| 2to3                       | 218 ms                                                      | 221 ms: 1.02x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 75.8 ms: 1.02x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 59.9 ms: 1.02x slower                                                       |
| scimark_fft                | 184 ms                                                      | 188 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 35.1 ms: 1.02x slower                                                       |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.19 ms: 1.02x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.6 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.03x slower                                                      |
| richards                   | 28.4 ms                                                     | 29.4 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 724 ms: 1.04x slower                                                        |
| richards_super             | 32.1 ms                                                     | 33.4 ms: 1.04x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.7 ms: 1.04x slower                                                       |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 539 ms: 1.05x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.05x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.8 ms: 1.05x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 83.9 ms: 1.07x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.48 sec: 1.08x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 143 us: 1.08x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 870 us: 1.08x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.10x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.66 ms: 1.13x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 221 us: 1.13x slower                                                        |
| fannkuch                   | 247 ms                                                      | 281 ms: 1.14x slower                                                        |
| coverage                   | 40.8 ms                                                     | 46.9 ms: 1.15x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.69 ms: 1.18x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 84.2 ms: 1.22x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.5 ms: 1.26x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.98 ms: 1.30x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (5): sympy_str, logging_simple, deltablue, tomli_loads, logging_format
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250214-3.14.0a5+-1775091/bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 63.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown