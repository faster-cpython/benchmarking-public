# Results vs. 3.12.0

- fork: python
- ref: dbd23790dbd662169905
- machine: windows-amd64
- commit hash: dbd2379
- commit date: 2024-11-23
- overall geometric mean: 1.020x slower
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                        |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 580 ms: 1.33x faster                                                        |
| async_tree_io              | 731 ms                                                      | 582 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 397 ms: 1.23x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 277 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 412 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 80.0 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 90.1 ms: 1.03x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 13.9 us                                                     | 14.1 us: 1.02x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 94.7 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.4 ms: 1.05x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.4 ms: 1.10x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 152 us: 1.14x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.63 ms: 1.16x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 229 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.6 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.00 ms: 1.01x faster                                                       |
| django_template | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                        |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 580 ms: 1.33x faster                                                        |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 582 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 397 ms: 1.23x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 277 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 412 ms: 1.22x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.16x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.5 us: 1.10x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 807 us: 1.06x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 76.1 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.5 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 89.4 ms: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 89.7 ms: 1.02x faster                                                       |
| mako                       | 7.09 ms                                                     | 7.00 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.76 us: 1.01x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 48.8 ms: 1.01x slower                                                       |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.34 us: 1.01x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 67.9 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.02x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 94.7 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                       |
| chaos                      | 43.3 ms                                                     | 44.4 ms: 1.03x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 90.1 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 58.4 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 732 ms: 1.05x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 78.2 ms: 1.05x slower                                                       |
| raytrace                   | 192 ms                                                      | 202 ms: 1.05x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.5 ms: 1.06x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 64.0 ns: 1.06x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.71 ms: 1.06x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 304 ms: 1.07x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.48 sec: 1.08x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 555 ms: 1.08x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 63.9 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.5 ms: 1.09x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                       |
| scimark_fft                | 184 ms                                                      | 201 ms: 1.09x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.49 ms: 1.09x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.4 ms: 1.10x slower                                                       |
| pyflate                    | 295 ms                                                      | 324 ms: 1.10x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.11x slower                                                       |
| nbody                      | 71.9 ms                                                     | 80.0 ms: 1.11x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 89.7 ms: 1.14x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.6 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 152 us: 1.14x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 921 us: 1.14x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.75 ms: 1.15x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                      |
| richards_super             | 32.1 ms                                                     | 37.4 ms: 1.16x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.63 ms: 1.16x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 229 us: 1.17x slower                                                        |
| fannkuch                   | 247 ms                                                      | 289 ms: 1.17x slower                                                        |
| richards                   | 28.4 ms                                                     | 33.4 ms: 1.18x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 81.9 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                        |
| python_startup             | 19.5 ms                                                     | 23.6 ms: 1.21x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.87 ms: 1.23x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (3): generators, float, json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.020x slower
# HPT report

- Reliability score: 99.75% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown