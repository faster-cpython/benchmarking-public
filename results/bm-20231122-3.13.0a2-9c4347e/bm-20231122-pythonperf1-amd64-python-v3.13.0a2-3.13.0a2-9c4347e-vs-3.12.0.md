# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 210 ms: 1.04x faster                                            |
| chameleon      | 4.98 ms                                                     | 4.81 ms: 1.04x faster                                           |
| docutils       | 1.66 sec                                                    | 1.55 sec: 1.07x faster                                          |
| tornado_http   | 89.5 ms                                                     | 86.1 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 264 ms: 1.10x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 453 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 482 ms: 1.04x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 361 ms: 1.02x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 281 ms: 1.01x faster                                            |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.3 ms: 1.09x faster                                           |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                           |
| regex_dna      | 126 ms                                                      | 122 ms: 1.03x faster                                            |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 179 us: 1.09x faster                                            |
| pickle               | 7.43 us                                                     | 6.94 us: 1.07x faster                                           |
| xml_etree_generate   | 55.8 ms                                                     | 53.2 ms: 1.05x faster                                           |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                            |
| json_loads           | 13.9 us                                                     | 13.4 us: 1.04x faster                                           |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.50 ms: 1.03x faster                                           |
| unpickle_list        | 2.75 us                                                     | 2.70 us: 1.02x faster                                           |
| unpickle             | 8.18 us                                                     | 8.09 us: 1.01x faster                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                           |
| xml_etree_parse      | 93.0 ms                                                     | 92.3 ms: 1.01x faster                                           |
| pickle_dict          | 18.4 us                                                     | 19.1 us: 1.04x slower                                           |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (2): tomli_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 19.9 ms: 1.02x slower                                           |
| python_startup_no_site | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                           |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.48 ms: 1.09x faster                                           |
| django_template | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                           |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.37x faster                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 73.9 us: 1.29x faster                                           |
| raytrace                   | 192 ms                                                      | 163 ms: 1.18x faster                                            |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                           |
| generators                 | 22.5 ms                                                     | 20.0 ms: 1.13x faster                                           |
| crypto_pyaes               | 48.5 ms                                                     | 43.3 ms: 1.12x faster                                           |
| sympy_str                  | 175 ms                                                      | 156 ms: 1.12x faster                                            |
| logging_silent             | 60.5 ns                                                     | 54.1 ns: 1.12x faster                                           |
| sympy_sum                  | 91.5 ms                                                     | 82.3 ms: 1.11x faster                                           |
| regex_compile              | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                           |
| async_tree_none            | 291 ms                                                      | 264 ms: 1.10x faster                                            |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.10x faster                                           |
| pickle_pure_python         | 195 us                                                      | 179 us: 1.09x faster                                            |
| mako                       | 7.09 ms                                                     | 6.48 ms: 1.09x faster                                           |
| deepcopy                   | 238 us                                                      | 218 us: 1.09x faster                                            |
| sqlglot_normalize          | 187 ms                                                      | 171 ms: 1.09x faster                                            |
| float                      | 56.8 ms                                                     | 52.3 ms: 1.09x faster                                           |
| go                         | 91.6 ms                                                     | 84.3 ms: 1.09x faster                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 453 ms: 1.08x faster                                            |
| bench_mp_pool              | 69.2 ms                                                     | 64.0 ms: 1.08x faster                                           |
| nqueens                    | 62.8 ms                                                     | 58.2 ms: 1.08x faster                                           |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                           |
| hexiom                     | 4.10 ms                                                     | 3.81 ms: 1.08x faster                                           |
| deltablue                  | 2.16 ms                                                     | 2.01 ms: 1.07x faster                                           |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                           |
| docutils                   | 1.66 sec                                                    | 1.55 sec: 1.07x faster                                          |
| pprint_safe_repr           | 513 ms                                                      | 479 ms: 1.07x faster                                            |
| pickle                     | 7.43 us                                                     | 6.94 us: 1.07x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 41.4 ms: 1.07x faster                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.9 ms: 1.07x faster                                           |
| sqlglot_parse              | 804 us                                                      | 752 us: 1.07x faster                                            |
| json                       | 3.05 ms                                                     | 2.85 ms: 1.07x faster                                           |
| pprint_pformat             | 1.05 sec                                                    | 979 ms: 1.07x faster                                            |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.06x faster                                           |
| sqlglot_optimize           | 34.5 ms                                                     | 32.5 ms: 1.06x faster                                           |
| sqlglot_transpile          | 1.02 ms                                                     | 965 us: 1.06x faster                                            |
| sympy_expand               | 284 ms                                                      | 269 ms: 1.06x faster                                            |
| async_generators           | 239 ms                                                      | 227 ms: 1.05x faster                                            |
| spectral_norm              | 66.9 ms                                                     | 63.6 ms: 1.05x faster                                           |
| xml_etree_generate         | 55.8 ms                                                     | 53.2 ms: 1.05x faster                                           |
| asyncio_tcp                | 487 ms                                                      | 465 ms: 1.05x faster                                            |
| django_template            | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                           |
| scimark_lu                 | 58.9 ms                                                     | 56.4 ms: 1.04x faster                                           |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 482 ms: 1.04x faster                                            |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.46 ms: 1.04x faster                                           |
| 2to3                       | 218 ms                                                      | 210 ms: 1.04x faster                                            |
| tornado_http               | 89.5 ms                                                     | 86.1 ms: 1.04x faster                                           |
| json_loads                 | 13.9 us                                                     | 13.4 us: 1.04x faster                                           |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                           |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.02 sec: 1.04x faster                                          |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                           |
| chameleon                  | 4.98 ms                                                     | 4.81 ms: 1.04x faster                                           |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                            |
| json_dumps                 | 5.70 ms                                                     | 5.50 ms: 1.03x faster                                           |
| logging_simple             | 6.28 us                                                     | 6.07 us: 1.03x faster                                           |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.03x faster                                            |
| logging_format             | 6.72 us                                                     | 6.51 us: 1.03x faster                                           |
| meteor_contest             | 74.6 ms                                                     | 72.6 ms: 1.03x faster                                           |
| fannkuch                   | 247 ms                                                      | 241 ms: 1.02x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 361 ms: 1.02x faster                                            |
| unpickle_list              | 2.75 us                                                     | 2.70 us: 1.02x faster                                           |
| async_tree_none_tg         | 285 ms                                                      | 281 ms: 1.01x faster                                            |
| pyflate                    | 295 ms                                                      | 291 ms: 1.01x faster                                            |
| unpickle                   | 8.18 us                                                     | 8.09 us: 1.01x faster                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                           |
| mdp                        | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                          |
| xml_etree_parse            | 93.0 ms                                                     | 92.3 ms: 1.01x faster                                           |
| pathlib                    | 80.5 ms                                                     | 79.9 ms: 1.01x faster                                           |
| python_startup             | 19.5 ms                                                     | 19.9 ms: 1.02x slower                                           |
| pickle_dict                | 18.4 us                                                     | 19.1 us: 1.04x slower                                           |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                           |
| scimark_sor                | 78.8 ms                                                     | 85.4 ms: 1.08x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                           |
| telco                      | 4.13 ms                                                     | 4.57 ms: 1.11x slower                                           |
| coverage                   | 40.8 ms                                                     | 45.8 ms: 1.12x slower                                           |
| mypy2                      | 509 ms                                                      | 584 ms: 1.15x slower                                            |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (14): bench_thread_pool, create_gc_cycles, deepcopy_memo, async_tree_io_tg, gc_traversal, async_tree_io, tomli_loads, scimark_fft, pickle_list, nbody, regex_effbot, async_tree_memoization, aiohttp, pycparser
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown