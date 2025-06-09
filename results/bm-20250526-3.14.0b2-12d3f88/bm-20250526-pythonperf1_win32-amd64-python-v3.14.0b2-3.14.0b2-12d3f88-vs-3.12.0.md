# Results vs. 3.12.0

- fork: python
- ref: v3.14.0b2
- machine: windows-amd64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 224 ms: 1.25x faster                                                  |
| docutils       | 1.98 sec                                                        | 1.64 sec: 1.21x faster                                                |
| Geometric mean | (ref)                                                           | 1.23x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 212 ms: 1.72x faster                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                  |
| async_tree_none            | 298 ms                                                          | 175 ms: 1.70x faster                                                  |
| async_tree_io              | 693 ms                                                          | 408 ms: 1.70x faster                                                  |
| async_tree_io_tg           | 677 ms                                                          | 409 ms: 1.65x faster                                                  |
| async_tree_memoization_tg  | 350 ms                                                          | 212 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                  |
| async_tree_none_tg         | 278 ms                                                          | 174 ms: 1.60x faster                                                  |
| Geometric mean             | (ref)                                                           | 1.67x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 64.3 ms: 1.97x faster                                                 |
| float          | 76.7 ms                                                         | 44.5 ms: 1.73x faster                                                 |
| pidigits       | 199 ms                                                          | 149 ms: 1.34x faster                                                  |
| Geometric mean | (ref)                                                           | 1.66x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 82.5 ms: 1.57x faster                                                 |
| regex_effbot   | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                 |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                  |
| regex_v8       | 15.0 ms                                                         | 14.5 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                           | 1.23x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 135 us: 1.56x faster                                                  |
| tomli_loads          | 2.20 sec                                                        | 1.44 sec: 1.52x faster                                                |
| json_loads           | 20.4 us                                                         | 14.7 us: 1.38x faster                                                 |
| pickle_pure_python   | 286 us                                                          | 212 us: 1.35x faster                                                  |
| xml_etree_process    | 53.2 ms                                                         | 39.7 ms: 1.34x faster                                                 |
| xml_etree_parse      | 113 ms                                                          | 89.1 ms: 1.27x faster                                                 |
| xml_etree_generate   | 72.1 ms                                                         | 56.9 ms: 1.27x faster                                                 |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.0 ms: 1.20x faster                                                 |
| json_dumps           | 7.40 ms                                                         | 6.27 ms: 1.18x faster                                                 |
| Geometric mean       | (ref)                                                           | 1.33x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                 |
| python_startup         | 22.4 ms                                                         | 26.2 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.68 ms: 1.49x faster                                                 |
| django_template | 36.9 ms                                                         | 25.4 ms: 1.45x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 32.2 ms: 2.84x faster                                                 |
| mdp                        | 1.91 sec                                                        | 818 ms: 2.34x faster                                                  |
| deepcopy                   | 360 us                                                          | 171 us: 2.10x faster                                                  |
| deepcopy_memo              | 38.4 us                                                         | 18.5 us: 2.07x faster                                                 |
| nbody                      | 127 ms                                                          | 64.3 ms: 1.97x faster                                                 |
| generators                 | 38.5 ms                                                         | 19.8 ms: 1.95x faster                                                 |
| deepcopy_reduce            | 3.23 us                                                         | 1.83 us: 1.76x faster                                                 |
| chaos                      | 69.4 ms                                                         | 39.5 ms: 1.76x faster                                                 |
| go                         | 137 ms                                                          | 78.6 ms: 1.75x faster                                                 |
| spectral_norm              | 104 ms                                                          | 60.1 ms: 1.73x faster                                                 |
| float                      | 76.7 ms                                                         | 44.5 ms: 1.73x faster                                                 |
| async_tree_memoization     | 364 ms                                                          | 212 ms: 1.72x faster                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                  |
| async_tree_none            | 298 ms                                                          | 175 ms: 1.70x faster                                                  |
| async_tree_io              | 693 ms                                                          | 408 ms: 1.70x faster                                                  |
| scimark_sor                | 130 ms                                                          | 76.7 ms: 1.69x faster                                                 |
| raytrace                   | 308 ms                                                          | 183 ms: 1.68x faster                                                  |
| async_tree_io_tg           | 677 ms                                                          | 409 ms: 1.65x faster                                                  |
| async_tree_memoization_tg  | 350 ms                                                          | 212 ms: 1.65x faster                                                  |
| deltablue                  | 3.58 ms                                                         | 2.18 ms: 1.65x faster                                                 |
| comprehensions             | 19.2 us                                                         | 11.7 us: 1.64x faster                                                 |
| hexiom                     | 6.82 ms                                                         | 4.24 ms: 1.61x faster                                                 |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.4 ms: 1.60x faster                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                  |
| async_tree_none_tg         | 278 ms                                                          | 174 ms: 1.60x faster                                                  |
| scimark_lu                 | 93.2 ms                                                         | 58.5 ms: 1.59x faster                                                 |
| regex_compile              | 129 ms                                                          | 82.5 ms: 1.57x faster                                                 |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.56x faster                                                  |
| scimark_fft                | 271 ms                                                          | 177 ms: 1.53x faster                                                  |
| logging_simple             | 9.75 us                                                         | 6.38 us: 1.53x faster                                                 |
| logging_format             | 10.4 us                                                         | 6.81 us: 1.53x faster                                                 |
| tomli_loads                | 2.20 sec                                                        | 1.44 sec: 1.52x faster                                                |
| coroutines                 | 20.9 ms                                                         | 13.9 ms: 1.51x faster                                                 |
| pyflate                    | 424 ms                                                          | 284 ms: 1.49x faster                                                  |
| mako                       | 9.96 ms                                                         | 6.68 ms: 1.49x faster                                                 |
| richards                   | 41.3 ms                                                         | 28.0 ms: 1.48x faster                                                 |
| crypto_pyaes               | 69.2 ms                                                         | 46.9 ms: 1.48x faster                                                 |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.62 ms: 1.48x faster                                                 |
| nqueens                    | 93.7 ms                                                         | 63.8 ms: 1.47x faster                                                 |
| pprint_pformat             | 1.50 sec                                                        | 1.03 sec: 1.46x faster                                                |
| django_template            | 36.9 ms                                                         | 25.4 ms: 1.45x faster                                                 |
| richards_super             | 46.5 ms                                                         | 32.0 ms: 1.45x faster                                                 |
| pprint_safe_repr           | 721 ms                                                          | 508 ms: 1.42x faster                                                  |
| sympy_integrate            | 17.5 ms                                                         | 12.5 ms: 1.41x faster                                                 |
| sympy_str                  | 240 ms                                                          | 171 ms: 1.40x faster                                                  |
| dulwich_log                | 58.5 ms                                                         | 41.9 ms: 1.39x faster                                                 |
| json                       | 4.15 ms                                                         | 2.98 ms: 1.39x faster                                                 |
| json_loads                 | 20.4 us                                                         | 14.7 us: 1.38x faster                                                 |
| sympy_sum                  | 123 ms                                                          | 89.1 ms: 1.38x faster                                                 |
| fannkuch                   | 354 ms                                                          | 258 ms: 1.37x faster                                                  |
| async_generators           | 313 ms                                                          | 230 ms: 1.36x faster                                                  |
| sympy_expand               | 398 ms                                                          | 293 ms: 1.36x faster                                                  |
| pickle_pure_python         | 286 us                                                          | 212 us: 1.35x faster                                                  |
| pycparser                  | 978 ms                                                          | 727 ms: 1.35x faster                                                  |
| pidigits                   | 199 ms                                                          | 149 ms: 1.34x faster                                                  |
| xml_etree_process          | 53.2 ms                                                         | 39.7 ms: 1.34x faster                                                 |
| regex_effbot               | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                 |
| sqlite_synth               | 2.07 us                                                         | 1.61 us: 1.29x faster                                                 |
| xml_etree_parse            | 113 ms                                                          | 89.1 ms: 1.27x faster                                                 |
| xml_etree_generate         | 72.1 ms                                                         | 56.9 ms: 1.27x faster                                                 |
| 2to3                       | 280 ms                                                          | 224 ms: 1.25x faster                                                  |
| docutils                   | 1.98 sec                                                        | 1.64 sec: 1.21x faster                                                |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.0 ms: 1.20x faster                                                 |
| telco                      | 5.51 ms                                                         | 4.66 ms: 1.18x faster                                                 |
| json_dumps                 | 7.40 ms                                                         | 6.27 ms: 1.18x faster                                                 |
| meteor_contest             | 86.9 ms                                                         | 73.7 ms: 1.18x faster                                                 |
| typing_runtime_protocols   | 126 us                                                          | 107 us: 1.18x faster                                                  |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                  |
| regex_v8                   | 15.0 ms                                                         | 14.5 ms: 1.04x faster                                                 |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                 |
| coverage                   | 48.4 ms                                                         | 51.2 ms: 1.06x slower                                                 |
| python_startup             | 22.4 ms                                                         | 26.2 ms: 1.17x slower                                                 |
| gc_traversal               | 1.44 ms                                                         | 2.14 ms: 1.49x slower                                                 |
| create_gc_cycles           | 652 us                                                          | 1.31 ms: 2.02x slower                                                 |
| logging_silent             | 101 ns                                                          | 328 ns: 3.24x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.41x faster                                                          |
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.42x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown