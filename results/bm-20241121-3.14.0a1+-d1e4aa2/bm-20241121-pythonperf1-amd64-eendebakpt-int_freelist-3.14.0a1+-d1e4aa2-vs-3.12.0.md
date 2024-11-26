# Results vs. 3.12.0

- fork: eendebakpt
- ref: int_freelist
- machine: windows-amd64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.026x slower
- HPT reliability: 99.61%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                    |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                  |
| Geometric mean | (ref)                                                       | 1.03x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                    |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                                    |
| async_tree_io              | 731 ms                                                      | 563 ms: 1.30x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                    |
| async_tree_io_tg           | 771 ms                                                      | 629 ms: 1.23x faster                                                    |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                    |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                    |
| float          | 56.8 ms                                                     | 56.2 ms: 1.01x faster                                                   |
| nbody          | 71.9 ms                                                     | 78.8 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                       | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.09x faster                                                    |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                   |
| regex_compile  | 87.5 ms                                                     | 91.6 ms: 1.05x slower                                                   |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                       | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 94.0 ms: 1.01x slower                                                   |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.0 ms: 1.01x slower                                                   |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                   |
| xml_etree_generate   | 55.8 ms                                                     | 58.3 ms: 1.04x slower                                                   |
| xml_etree_process    | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                   |
| tomli_loads          | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                  |
| pickle_pure_python   | 195 us                                                      | 231 us: 1.18x slower                                                    |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                    |
| json_dumps           | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                   |
| python_startup         | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                    |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                                    |
| async_tree_io              | 731 ms                                                      | 563 ms: 1.30x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                    |
| async_tree_io_tg           | 771 ms                                                      | 629 ms: 1.23x faster                                                    |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                    |
| deepcopy                   | 238 us                                                      | 195 us: 1.22x faster                                                    |
| comprehensions             | 14.1 us                                                     | 12.4 us: 1.14x faster                                                   |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                   |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.09x faster                                                    |
| deepcopy_memo              | 23.7 us                                                     | 22.0 us: 1.08x faster                                                   |
| pathlib                    | 80.5 ms                                                     | 76.1 ms: 1.06x faster                                                   |
| bench_thread_pool          | 857 us                                                      | 820 us: 1.04x faster                                                    |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                   |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                   |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                    |
| deepcopy_reduce            | 2.09 us                                                     | 2.03 us: 1.03x faster                                                   |
| dulwich_log                | 44.3 ms                                                     | 43.1 ms: 1.03x faster                                                   |
| sympy_sum                  | 91.5 ms                                                     | 90.2 ms: 1.01x faster                                                   |
| go                         | 91.6 ms                                                     | 90.5 ms: 1.01x faster                                                   |
| spectral_norm              | 66.9 ms                                                     | 66.2 ms: 1.01x faster                                                   |
| float                      | 56.8 ms                                                     | 56.2 ms: 1.01x faster                                                   |
| xml_etree_parse            | 93.0 ms                                                     | 94.0 ms: 1.01x slower                                                   |
| json                       | 3.05 ms                                                     | 3.09 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.0 ms: 1.01x slower                                                   |
| crypto_pyaes               | 48.5 ms                                                     | 49.1 ms: 1.01x slower                                                   |
| chaos                      | 43.3 ms                                                     | 44.0 ms: 1.01x slower                                                   |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.60 ms: 1.02x slower                                                   |
| logging_format             | 6.72 us                                                     | 6.85 us: 1.02x slower                                                   |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                    |
| logging_simple             | 6.28 us                                                     | 6.42 us: 1.02x slower                                                   |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                    |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                                    |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                  |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                    |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                   |
| nqueens                    | 62.8 ms                                                     | 65.1 ms: 1.04x slower                                                   |
| xml_etree_generate         | 55.8 ms                                                     | 58.3 ms: 1.04x slower                                                   |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.05x slower                                                   |
| regex_compile              | 87.5 ms                                                     | 91.6 ms: 1.05x slower                                                   |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                   |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                    |
| meteor_contest             | 74.6 ms                                                     | 78.9 ms: 1.06x slower                                                   |
| python_startup_no_site     | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                   |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                  |
| sqlglot_normalize          | 187 ms                                                      | 199 ms: 1.07x slower                                                    |
| scimark_fft                | 184 ms                                                      | 197 ms: 1.07x slower                                                    |
| pyflate                    | 295 ms                                                      | 319 ms: 1.08x slower                                                    |
| sqlglot_optimize           | 34.5 ms                                                     | 37.4 ms: 1.08x slower                                                   |
| logging_silent             | 60.5 ns                                                     | 65.7 ns: 1.09x slower                                                   |
| xml_etree_process          | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                   |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                   |
| sympy_expand               | 284 ms                                                      | 311 ms: 1.10x slower                                                    |
| nbody                      | 71.9 ms                                                     | 78.8 ms: 1.10x slower                                                   |
| pprint_pformat             | 1.05 sec                                                    | 1.15 sec: 1.10x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.11x slower                                                   |
| pprint_safe_repr           | 513 ms                                                      | 572 ms: 1.11x slower                                                    |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                   |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.0 ms: 1.12x slower                                                   |
| hexiom                     | 4.10 ms                                                     | 4.61 ms: 1.12x slower                                                   |
| scimark_lu                 | 58.9 ms                                                     | 66.3 ms: 1.13x slower                                                   |
| tomli_loads                | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                  |
| fannkuch                   | 247 ms                                                      | 279 ms: 1.13x slower                                                    |
| richards_super             | 32.1 ms                                                     | 36.5 ms: 1.14x slower                                                   |
| sqlglot_parse              | 804 us                                                      | 918 us: 1.14x slower                                                    |
| richards                   | 28.4 ms                                                     | 32.7 ms: 1.15x slower                                                   |
| coverage                   | 40.8 ms                                                     | 47.4 ms: 1.16x slower                                                   |
| scimark_sor                | 78.8 ms                                                     | 91.6 ms: 1.16x slower                                                   |
| telco                      | 4.13 ms                                                     | 4.85 ms: 1.17x slower                                                   |
| pickle_pure_python         | 195 us                                                      | 231 us: 1.18x slower                                                    |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                    |
| bench_mp_pool              | 69.2 ms                                                     | 81.8 ms: 1.18x slower                                                   |
| json_dumps                 | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                   |
| python_startup             | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                   |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                    |
| gc_traversal               | 1.52 ms                                                     | 1.92 ms: 1.26x slower                                                   |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.83x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                            |

Benchmark hidden because not significant (2): mako, generators
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.026x slower
# HPT report

- Reliability score: 99.61% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown