# Results vs. 3.12.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: windows-amd64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.043x faster
- HPT reliability: 68.25%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 414 ms: 1.77x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                       |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.10x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 86.4 ms: 1.01x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.9 ms: 1.02x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.4 ms: 1.07x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 226 us: 1.16x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.83 ms: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.6 ms: 1.20x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.77 ms: 1.05x faster                                                       |
| django_template | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 414 ms: 1.77x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                        |
| deepcopy                   | 238 us                                                      | 184 us: 1.30x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                       |
| float                      | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.9 us: 1.19x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 58.5 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                       |
| async_generators           | 239 ms                                                      | 218 ms: 1.10x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.10x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| go                         | 91.6 ms                                                     | 86.6 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.77 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.2 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.4 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                                       |
| scimark_fft                | 184 ms                                                      | 181 ms: 1.02x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 86.4 ms: 1.01x faster                                                       |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                       |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| sympy_str                  | 175 ms                                                      | 174 ms: 1.01x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 75.0 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.58 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 34.9 ms: 1.01x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.5 ms: 1.02x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.9 ms: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.40 us: 1.02x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 61.7 ns: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.86 us: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| pyflate                    | 295 ms                                                      | 304 ms: 1.03x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 50.1 ms: 1.03x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.5 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.5 ms: 1.04x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                       |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                        |
| pycparser                  | 699 ms                                                      | 735 ms: 1.05x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 542 ms: 1.06x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.35 ms: 1.06x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 84.2 ms: 1.07x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 62.9 ms: 1.07x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.07x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.4 ms: 1.07x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 882 us: 1.10x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                        |
| fannkuch                   | 247 ms                                                      | 274 ms: 1.11x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.15x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 226 us: 1.16x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.17x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.8 ms: 1.17x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.61 sec: 1.18x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.83 ms: 1.20x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.6 ms: 1.20x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 86.2 ms: 1.25x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.00 ms: 1.32x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.20 ms: 1.60x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (5): docutils, raytrace, bench_thread_pool, nqueens, nbody
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 68.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown