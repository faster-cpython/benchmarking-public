# Results vs. 3.12.0

- fork: python
- ref: c695e37a3f95c225ee08
- machine: windows-x86
- commit hash: c695e37
- commit date: 2024-11-13
- overall geometric mean: 1.046x faster
- HPT reliability: 98.88%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 294 ms: 1.05x slower                                                            |
| docutils       | 1.98 sec                                                        | 2.15 sec: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 267 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 221 ms: 1.26x faster                                                            |
| async_tree_none            | 298 ms                                                          | 241 ms: 1.24x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                            |
| async_tree_io              | 693 ms                                                          | 567 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 568 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 467 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 497 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 55.3 ms: 1.39x faster                                                           |
| nbody          | 127 ms                                                          | 97.0 ms: 1.31x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.83 ms: 1.11x faster                                                           |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                            |
| regex_compile  | 129 ms                                                          | 122 ms: 1.06x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.81 sec: 1.22x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 188 us: 1.12x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 70.2 ms: 1.11x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 114 ms: 1.01x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 74.3 ms: 1.03x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 55.3 ms: 1.04x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.4 us: 1.05x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 302 us: 1.06x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 8.76 ms: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.32 ms: 1.36x faster                                                           |
| django_template | 36.9 ms                                                         | 36.5 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.4 us: 1.64x faster                                                           |
| float                      | 76.7 ms                                                         | 55.3 ms: 1.39x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.32 ms: 1.36x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 267 ms: 1.31x faster                                                            |
| scimark_sor                | 130 ms                                                          | 98.9 ms: 1.31x faster                                                           |
| deepcopy                   | 360 us                                                          | 275 us: 1.31x faster                                                            |
| nbody                      | 127 ms                                                          | 97.0 ms: 1.31x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 71.9 ms: 1.30x faster                                                           |
| logging_silent             | 101 ns                                                          | 78.1 ns: 1.29x faster                                                           |
| spectral_norm              | 104 ms                                                          | 82.5 ms: 1.26x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 221 ms: 1.26x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.7 ms: 1.25x faster                                                           |
| async_tree_none            | 298 ms                                                          | 241 ms: 1.24x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                            |
| async_tree_io              | 693 ms                                                          | 567 ms: 1.22x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.81 sec: 1.22x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 568 ms: 1.19x faster                                                            |
| logging_simple             | 9.75 us                                                         | 8.26 us: 1.18x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.27 ms: 1.18x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.8 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 467 ms: 1.17x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.77 us: 1.17x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.92 us: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 497 ms: 1.13x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 188 us: 1.12x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.83 ms: 1.11x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 3.22 ms: 1.11x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 82.5 ms: 1.11x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 70.2 ms: 1.11x faster                                                           |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                            |
| go                         | 137 ms                                                          | 127 ms: 1.09x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                           |
| chaos                      | 69.4 ms                                                         | 65.1 ms: 1.07x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.17 ms: 1.06x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 62.5 ms: 1.06x faster                                                           |
| scimark_fft                | 271 ms                                                          | 255 ms: 1.06x faster                                                            |
| generators                 | 38.5 ms                                                         | 36.3 ms: 1.06x faster                                                           |
| regex_compile              | 129 ms                                                          | 122 ms: 1.06x faster                                                            |
| pyflate                    | 424 ms                                                          | 402 ms: 1.05x faster                                                            |
| fannkuch                   | 354 ms                                                          | 336 ms: 1.05x faster                                                            |
| pycparser                  | 978 ms                                                          | 933 ms: 1.05x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 67.5 ms: 1.02x faster                                                           |
| comprehensions             | 19.2 us                                                         | 18.8 us: 1.02x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                                          |
| django_template            | 36.9 ms                                                         | 36.5 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.49 sec: 1.01x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.52 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| xml_etree_parse            | 113 ms                                                          | 114 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| raytrace                   | 308 ms                                                          | 314 ms: 1.02x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 735 ms: 1.02x slower                                                            |
| sympy_sum                  | 123 ms                                                          | 125 ms: 1.02x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 89.0 ms: 1.02x slower                                                           |
| async_generators           | 313 ms                                                          | 322 ms: 1.03x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 74.3 ms: 1.03x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 97.1 ms: 1.04x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 55.3 ms: 1.04x slower                                                           |
| sympy_str                  | 240 ms                                                          | 250 ms: 1.05x slower                                                            |
| 2to3                       | 280 ms                                                          | 294 ms: 1.05x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.4 us: 1.05x slower                                                           |
| richards_super             | 46.5 ms                                                         | 49.0 ms: 1.06x slower                                                           |
| richards                   | 41.3 ms                                                         | 43.6 ms: 1.06x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 302 us: 1.06x slower                                                            |
| coverage                   | 48.4 ms                                                         | 51.5 ms: 1.06x slower                                                           |
| hexiom                     | 6.82 ms                                                         | 7.28 ms: 1.07x slower                                                           |
| sympy_expand               | 398 ms                                                          | 425 ms: 1.07x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.15 sec: 1.08x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                           |
| json                       | 4.15 ms                                                         | 4.63 ms: 1.11x slower                                                           |
| sympy_integrate            | 17.5 ms                                                         | 19.6 ms: 1.12x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 116 ms: 1.15x slower                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 57.2 ms: 1.18x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.76 ms: 1.18x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 92.8 ms: 1.23x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.24x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.01 ms: 1.27x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 164 us: 1.30x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.16 ms: 1.78x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                    |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241113-3.14.0a1+-c695e37-JIT/bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.046x faster
# HPT report

- Reliability score: 98.88% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown