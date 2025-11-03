# Results vs. 3.12.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.040x faster
- HPT reliability: 77.71%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 2.72 sec: 1.64x slower                                                      |
| Geometric mean | (ref)                                                       | 1.28x slower                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 316 ms: 2.44x faster                                                        |
| async_tree_io              | 731 ms                                                      | 336 ms: 2.18x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 144 ms: 1.98x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 186 ms: 1.97x faster                                                        |
| async_tree_none            | 291 ms                                                      | 163 ms: 1.79x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 309 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.86x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                       |
| pidigits       | 152 ms                                                      | 134 ms: 1.13x faster                                                        |
| nbody          | 71.9 ms                                                     | 76.9 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 111 ms: 1.13x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 88.6 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 57.7 ms: 1.13x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 87.2 ms: 1.07x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.95 ms: 1.04x slower                                                       |
| pickle               | 7.43 us                                                     | 7.91 us: 1.06x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.03 us: 1.07x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 60.1 ms: 1.08x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 20.1 us: 1.09x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.00 us: 1.09x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                        |
| xml_etree_process    | 37.7 ms                                                     | 42.5 ms: 1.13x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.8 us: 1.13x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 225 us: 1.15x slower                                                        |
| unpickle             | 8.18 us                                                     | 9.86 us: 1.20x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.17 sec: 1.59x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                       |
| mako            | 7.09 ms                                                     | 9.63 ms: 1.36x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.24x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.0 ms: 2.77x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 316 ms: 2.44x faster                                                        |
| async_tree_io              | 731 ms                                                      | 336 ms: 2.18x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 144 ms: 1.98x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 186 ms: 1.97x faster                                                        |
| async_tree_none            | 291 ms                                                      | 163 ms: 1.79x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 309 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                        |
| mdp                        | 1.37 sec                                                    | 1.01 sec: 1.36x faster                                                      |
| deepcopy                   | 238 us                                                      | 179 us: 1.33x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.34 us: 1.32x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.6 us: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.22 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                                       |
| regex_dna                  | 126 ms                                                      | 111 ms: 1.13x faster                                                        |
| pidigits                   | 152 ms                                                      | 134 ms: 1.13x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 57.7 ms: 1.13x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.1 ms: 1.10x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.07x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.2 ms: 1.07x faster                                                       |
| go                         | 91.6 ms                                                     | 86.2 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 58.0 ns: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.01x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 37.0 ns: 1.01x faster                                                       |
| pycparser                  | 699 ms                                                      | 691 ms: 1.01x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 88.6 ms: 1.01x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| scimark_fft                | 184 ms                                                      | 188 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.40 us: 1.02x slower                                                       |
| pyflate                    | 295 ms                                                      | 302 ms: 1.02x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.87 us: 1.02x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 68.6 ms: 1.02x slower                                                       |
| chaos                      | 43.3 ms                                                     | 44.5 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.04x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 534 ms: 1.04x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.95 ms: 1.04x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 72.7 ms: 1.05x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 83.4 ms: 1.06x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.91 us: 1.06x slower                                                       |
| raytrace                   | 192 ms                                                      | 205 ms: 1.06x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                       |
| nbody                      | 71.9 ms                                                     | 76.9 ms: 1.07x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.03 us: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.07x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 60.1 ms: 1.08x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.45 ms: 1.08x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 63.9 ms: 1.09x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.9 ms: 1.09x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.1 us: 1.09x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.00 us: 1.09x slower                                                       |
| async_generators           | 239 ms                                                      | 262 ms: 1.09x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                        |
| asyncio_tcp                | 487 ms                                                      | 544 ms: 1.12x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 70.1 ms: 1.12x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 83.3 ms: 1.12x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 42.5 ms: 1.13x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.4 ms: 1.13x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.8 us: 1.13x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 225 us: 1.15x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 55.9 ms: 1.15x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.96 ms: 1.16x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 1.01 ms: 1.18x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.91 ms: 1.19x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.86 us: 1.20x slower                                                       |
| fannkuch                   | 247 ms                                                      | 306 ms: 1.24x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 123 us: 1.29x slower                                                        |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                       |
| mako                       | 7.09 ms                                                     | 9.63 ms: 1.36x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.07 ms: 1.42x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.55 sec: 1.49x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.17 sec: 1.59x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.72 sec: 1.64x slower                                                      |
| coverage                   | 40.8 ms                                                     | 67.1 ms: 1.64x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (3): sympy_sum, 2to3, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251101-3.15.0a1+-2f60b8f-NOGIL/bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 77.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown