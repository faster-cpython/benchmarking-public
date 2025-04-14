# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.038x slower
- HPT reliability: 98.30%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 235 ms: 1.08x slower                                                        |
| docutils       | 1.66 sec                                                    | 2.99 sec: 1.80x slower                                                      |
| Geometric mean | (ref)                                                       | 1.39x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 354 ms: 2.18x faster                                                        |
| async_tree_io              | 731 ms                                                      | 378 ms: 1.93x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 315 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 48.1 ms: 1.18x faster                                                       |
| pidigits       | 152 ms                                                      | 138 ms: 1.10x faster                                                        |
| nbody          | 71.9 ms                                                     | 92.0 ms: 1.28x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 111 ms: 1.13x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 97.2 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.6 ms: 1.09x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.1 ms: 1.03x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 20.4 us: 1.11x slower                                                       |
| pickle               | 7.43 us                                                     | 8.39 us: 1.13x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 63.6 ms: 1.14x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.33 us: 1.18x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.86 us: 1.21x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 45.9 ms: 1.22x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 238 us: 1.22x slower                                                        |
| unpickle_list        | 2.75 us                                                     | 3.37 us: 1.23x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 165 us: 1.24x slower                                                        |
| json_loads           | 13.9 us                                                     | 17.4 us: 1.25x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.62 ms: 1.34x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.89 sec: 2.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.21x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                       |
| python_startup         | 19.5 ms                                                     | 27.3 ms: 1.40x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.34x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                       |
| mako            | 7.09 ms                                                     | 9.96 ms: 1.41x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.30x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 354 ms: 2.18x faster                                                        |
| async_tree_io              | 731 ms                                                      | 378 ms: 1.93x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 315 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.15 ms: 1.33x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.33 us: 1.33x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.14 sec: 1.21x faster                                                      |
| float                      | 56.8 ms                                                     | 48.1 ms: 1.18x faster                                                       |
| regex_dna                  | 126 ms                                                      | 111 ms: 1.13x faster                                                        |
| deepcopy                   | 238 us                                                      | 211 us: 1.13x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| pidigits                   | 152 ms                                                      | 138 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.6 ms: 1.09x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.1 ms: 1.03x faster                                                       |
| comprehensions             | 14.1 us                                                     | 13.8 us: 1.02x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 23.8 us: 1.00x slower                                                       |
| pycparser                  | 699 ms                                                      | 728 ms: 1.04x slower                                                        |
| async_generators           | 239 ms                                                      | 250 ms: 1.05x slower                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 2.19 us: 1.05x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 70.2 ms: 1.05x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 64.3 ns: 1.06x slower                                                       |
| 2to3                       | 218 ms                                                      | 235 ms: 1.08x slower                                                        |
| json                       | 3.05 ms                                                     | 3.31 ms: 1.09x slower                                                       |
| go                         | 91.6 ms                                                     | 100 ms: 1.10x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.89 us: 1.10x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 101 ms: 1.10x slower                                                        |
| logging_format             | 6.72 us                                                     | 7.41 us: 1.10x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.4 us: 1.11x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 97.2 ms: 1.11x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 76.9 ms: 1.11x slower                                                       |
| sympy_str                  | 175 ms                                                      | 195 ms: 1.11x slower                                                        |
| chaos                      | 43.3 ms                                                     | 48.4 ms: 1.12x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.39 us: 1.13x slower                                                       |
| pyflate                    | 295 ms                                                      | 333 ms: 1.13x slower                                                        |
| raytrace                   | 192 ms                                                      | 217 ms: 1.13x slower                                                        |
| asyncio_tcp                | 487 ms                                                      | 555 ms: 1.14x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 63.6 ms: 1.14x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 67.1 ms: 1.14x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.9 ms: 1.15x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.51 ms: 1.16x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.81 ms: 1.17x slower                                                       |
| sympy_expand               | 284 ms                                                      | 333 ms: 1.17x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 604 ms: 1.18x slower                                                        |
| scimark_fft                | 184 ms                                                      | 217 ms: 1.18x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.33 us: 1.18x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 93.2 ms: 1.18x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 89.4 ms: 1.20x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 75.3 ms: 1.20x slower                                                       |
| django_template            | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.52 sec: 1.20x slower                                                      |
| richards                   | 28.4 ms                                                     | 34.2 ms: 1.20x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.86 us: 1.21x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 45.4 ns: 1.21x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 45.9 ms: 1.22x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 238 us: 1.22x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 59.3 ms: 1.22x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.37 us: 1.23x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 165 us: 1.24x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.17 ms: 1.24x slower                                                       |
| json_loads                 | 13.9 us                                                     | 17.4 us: 1.25x slower                                                       |
| richards_super             | 32.1 ms                                                     | 40.3 ms: 1.26x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 55.6 ms: 1.27x slower                                                       |
| nbody                      | 71.9 ms                                                     | 92.0 ms: 1.28x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 967 us: 1.29x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 1.13 ms: 1.32x slower                                                       |
| fannkuch                   | 247 ms                                                      | 328 ms: 1.33x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 7.62 ms: 1.34x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.60 ms: 1.36x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 133 us: 1.40x slower                                                        |
| python_startup             | 19.5 ms                                                     | 27.3 ms: 1.40x slower                                                       |
| mako                       | 7.09 ms                                                     | 9.96 ms: 1.41x slower                                                       |
| coverage                   | 40.8 ms                                                     | 67.2 ms: 1.65x slower                                                       |
| docutils                   | 1.66 sec                                                    | 2.99 sec: 1.80x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.98 sec: 1.89x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.89 sec: 2.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.038x slower

# HPT report

- Reliability score: 98.30% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown