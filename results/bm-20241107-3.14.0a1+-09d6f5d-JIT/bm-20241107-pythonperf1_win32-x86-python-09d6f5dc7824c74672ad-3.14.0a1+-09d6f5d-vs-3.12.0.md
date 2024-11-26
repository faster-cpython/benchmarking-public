# Results vs. 3.12.0

- fork: python
- ref: 09d6f5dc7824c74672ad
- machine: windows-x86
- commit hash: 09d6f5d
- commit date: 2024-11-07
- overall geometric mean: 1.046x faster
- HPT reliability: 98.88%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 293 ms: 1.05x slower                                                            |
| docutils       | 1.98 sec                                                        | 2.14 sec: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 276 ms: 1.27x faster                                                            |
| async_tree_io              | 693 ms                                                          | 547 ms: 1.27x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 221 ms: 1.26x faster                                                            |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 303 ms: 1.20x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 568 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 483 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 516 ms: 1.09x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 55.8 ms: 1.38x faster                                                           |
| nbody          | 127 ms                                                          | 98.5 ms: 1.29x faster                                                           |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.81 ms: 1.13x faster                                                           |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                            |
| regex_compile  | 129 ms                                                          | 121 ms: 1.06x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.83 sec: 1.20x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 70.0 ms: 1.11x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 192 us: 1.10x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 71.8 ms: 1.01x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 53.6 ms: 1.01x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 301 us: 1.05x slower                                                            |
| json_loads           | 20.4 us                                                         | 21.4 us: 1.05x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.80 ms: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.39 ms: 1.35x faster                                                           |
| django_template | 36.9 ms                                                         | 36.3 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.8 us: 1.62x faster                                                           |
| float                      | 76.7 ms                                                         | 55.8 ms: 1.38x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.39 ms: 1.35x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 69.7 ms: 1.34x faster                                                           |
| logging_silent             | 101 ns                                                          | 76.9 ns: 1.31x faster                                                           |
| deepcopy                   | 360 us                                                          | 274 us: 1.31x faster                                                            |
| spectral_norm              | 104 ms                                                          | 79.2 ms: 1.31x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.7 ms: 1.30x faster                                                           |
| nbody                      | 127 ms                                                          | 98.5 ms: 1.29x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 276 ms: 1.27x faster                                                            |
| async_tree_io              | 693 ms                                                          | 547 ms: 1.27x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.26x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 221 ms: 1.26x faster                                                            |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.83 sec: 1.20x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 303 ms: 1.20x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.22 ms: 1.20x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 568 ms: 1.19x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.3 ms: 1.19x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.25 us: 1.18x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.85 us: 1.18x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.76 us: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 483 ms: 1.13x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.81 ms: 1.13x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 82.0 ms: 1.11x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 70.0 ms: 1.11x faster                                                           |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                            |
| chaos                      | 69.4 ms                                                         | 63.3 ms: 1.10x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 192 us: 1.10x faster                                                            |
| scimark_fft                | 271 ms                                                          | 247 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 516 ms: 1.09x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.29 ms: 1.09x faster                                                           |
| fannkuch                   | 354 ms                                                          | 326 ms: 1.08x faster                                                            |
| go                         | 137 ms                                                          | 127 ms: 1.08x faster                                                            |
| generators                 | 38.5 ms                                                         | 35.8 ms: 1.07x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 62.1 ms: 1.07x faster                                                           |
| pyflate                    | 424 ms                                                          | 398 ms: 1.07x faster                                                            |
| regex_compile              | 129 ms                                                          | 121 ms: 1.06x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.18 ms: 1.06x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.96 us: 1.06x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.05 ms: 1.05x faster                                                           |
| pycparser                  | 978 ms                                                          | 931 ms: 1.05x faster                                                            |
| comprehensions             | 19.2 us                                                         | 18.4 us: 1.04x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 67.1 ms: 1.03x faster                                                           |
| django_template            | 36.9 ms                                                         | 36.3 ms: 1.02x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 71.8 ms: 1.01x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 53.6 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| sympy_sum                  | 123 ms                                                          | 125 ms: 1.02x slower                                                            |
| raytrace                   | 308 ms                                                          | 314 ms: 1.02x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 743 ms: 1.03x slower                                                            |
| nqueens                    | 93.7 ms                                                         | 97.0 ms: 1.04x slower                                                           |
| sympy_str                  | 240 ms                                                          | 248 ms: 1.04x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 90.4 ms: 1.04x slower                                                           |
| 2to3                       | 280 ms                                                          | 293 ms: 1.05x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 301 us: 1.05x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.4 us: 1.05x slower                                                           |
| async_generators           | 313 ms                                                          | 330 ms: 1.05x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 7.19 ms: 1.05x slower                                                           |
| sympy_expand               | 398 ms                                                          | 422 ms: 1.06x slower                                                            |
| json                       | 4.15 ms                                                         | 4.40 ms: 1.06x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.1 ms: 1.07x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.14 sec: 1.08x slower                                                          |
| richards                   | 41.3 ms                                                         | 45.5 ms: 1.10x slower                                                           |
| richards_super             | 46.5 ms                                                         | 51.3 ms: 1.10x slower                                                           |
| sympy_integrate            | 17.5 ms                                                         | 19.5 ms: 1.11x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 115 ms: 1.15x slower                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 56.6 ms: 1.17x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.80 ms: 1.19x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.77 ms: 1.23x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 92.9 ms: 1.23x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.08 ms: 1.28x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 167 us: 1.32x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.17 ms: 1.79x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (3): sqlglot_transpile, pprint_pformat, xml_etree_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.046x faster
# HPT report

- Reliability score: 98.88% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown