# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.038x faster
- HPT reliability: 56.55%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 421 ms: 1.83x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 221 ms: 1.66x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.8 ms: 1.21x faster                                                       |
| nbody          | 71.9 ms                                                     | 68.9 ms: 1.04x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 86.0 ms: 1.02x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.6 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.8 us: 1.03x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.76 us: 1.01x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.8 ms: 1.02x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.95 us: 1.04x slower                                                       |
| pickle               | 7.43 us                                                     | 7.84 us: 1.05x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.0 ms: 1.06x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.95 us: 1.09x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.7 us: 1.13x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 224 us: 1.15x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.68 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.89 ms: 1.03x faster                                                       |
| django_template | 22.9 ms                                                     | 24.9 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.1 ms: 2.77x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 421 ms: 1.83x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 221 ms: 1.66x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.46x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                        |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.3 us: 1.25x faster                                                       |
| float                      | 56.8 ms                                                     | 46.8 ms: 1.21x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.6 us: 1.15x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 60.7 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                       |
| async_generators           | 239 ms                                                      | 222 ms: 1.08x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 41.6 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| nbody                      | 71.9 ms                                                     | 68.9 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.6 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.8 us: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 832 us: 1.03x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.89 ms: 1.03x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.2 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.5 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 86.0 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| go                         | 91.6 ms                                                     | 90.3 ms: 1.01x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                      |
| unpickle_list              | 2.75 us                                                     | 2.76 us: 1.01x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.33 us: 1.01x slower                                                       |
| json                       | 3.05 ms                                                     | 3.09 ms: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.7 ms: 1.02x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.8 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.84 us: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                        |
| raytrace                   | 192 ms                                                      | 197 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 35.5 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| scimark_fft                | 184 ms                                                      | 190 ms: 1.03x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 62.5 ns: 1.03x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 728 ms: 1.04x slower                                                        |
| pickle_list                | 2.83 us                                                     | 2.95 us: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                       |
| pyflate                    | 295 ms                                                      | 309 ms: 1.05x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.30 ms: 1.05x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.84 us: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.4 ms: 1.06x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.0 ms: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 302 ms: 1.06x slower                                                        |
| richards                   | 28.4 ms                                                     | 30.3 ms: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 521 ms: 1.07x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 549 ms: 1.07x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.07x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.7 ms: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.9 ms: 1.08x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.0 ms: 1.09x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.95 us: 1.09x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 888 us: 1.10x slower                                                        |
| fannkuch                   | 247 ms                                                      | 276 ms: 1.12x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                      |
| json_loads                 | 13.9 us                                                     | 15.7 us: 1.13x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.69 ms: 1.14x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 224 us: 1.15x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 90.7 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 43.9 ns: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.68 ms: 1.17x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.1 ms: 1.18x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 83.5 ms: 1.21x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.00 ms: 1.32x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (2): crypto_pyaes, sympy_str
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 56.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown