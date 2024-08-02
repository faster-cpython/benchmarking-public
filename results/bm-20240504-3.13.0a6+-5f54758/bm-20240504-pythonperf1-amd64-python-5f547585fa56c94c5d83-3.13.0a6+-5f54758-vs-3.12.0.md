# Results vs. 3.12.0

- fork: python
- ref: 5f547585fa56c94c5d83
- machine: windows-amd64
- commit hash: 5f54758
- commit date: 2024-05-04
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 207 ms: 1.05x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.64 ms: 1.07x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 81.8 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 263 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 212 ms: 1.34x faster                                                        |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.30x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 268 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 614 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 585 ms: 1.25x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 49.9 ms: 1.14x faster                                                       |
| nbody          | 71.9 ms                                                     | 66.1 ms: 1.09x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.6 ms: 1.13x faster                                                       |
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 17.6 ms: 1.23x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 176 us: 1.11x faster                                                        |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 53.9 ms: 1.04x faster                                                       |
| pickle               | 7.43 us                                                     | 7.22 us: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.61 ms: 1.02x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.58 us: 1.05x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.05 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): pickle_dict, tomli_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.42 ms: 1.10x faster                                                       |
| django_template | 22.9 ms                                                     | 21.5 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 263 ms: 1.40x faster                                                        |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 212 ms: 1.34x faster                                                        |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.61 sec: 1.31x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.30x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 268 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 614 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 585 ms: 1.25x faster                                                        |
| raytrace                   | 192 ms                                                      | 156 ms: 1.23x faster                                                        |
| generators                 | 22.5 ms                                                     | 18.6 ms: 1.21x faster                                                       |
| mypy2                      | 509 ms                                                      | 423 ms: 1.20x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 50.3 ns: 1.20x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.86 ms: 1.16x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.0 ms: 1.14x faster                                                       |
| float                      | 56.8 ms                                                     | 49.9 ms: 1.14x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.6 ms: 1.13x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 77.6 ms: 1.13x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 176 us: 1.11x faster                                                        |
| deepcopy                   | 238 us                                                      | 214 us: 1.11x faster                                                        |
| logging_simple             | 6.28 us                                                     | 5.67 us: 1.11x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.1 ms: 1.10x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.42 ms: 1.10x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.11 us: 1.10x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 171 ms: 1.10x faster                                                        |
| richards_super             | 32.1 ms                                                     | 29.3 ms: 1.10x faster                                                       |
| richards                   | 28.4 ms                                                     | 25.9 ms: 1.10x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 81.8 ms: 1.09x faster                                                       |
| go                         | 91.6 ms                                                     | 84.0 ms: 1.09x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                       |
| sympy_str                  | 175 ms                                                      | 161 ms: 1.09x faster                                                        |
| nbody                      | 71.9 ms                                                     | 66.1 ms: 1.09x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 57.8 ms: 1.09x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 964 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 473 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.4 ms: 1.08x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 84.6 ms: 1.08x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.79 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.64 ms: 1.07x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 64.7 ms: 1.07x faster                                                       |
| django_template            | 22.9 ms                                                     | 21.5 ms: 1.07x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 62.8 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.06x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 757 us: 1.06x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 22.3 us: 1.06x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 963 us: 1.06x faster                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 32.6 ms: 1.06x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 74.7 ms: 1.05x faster                                                       |
| 2to3                       | 218 ms                                                      | 207 ms: 1.05x faster                                                        |
| scimark_fft                | 184 ms                                                      | 176 ms: 1.05x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 818 us: 1.05x faster                                                        |
| sympy_expand               | 284 ms                                                      | 271 ms: 1.05x faster                                                        |
| mdp                        | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                                      |
| pyflate                    | 295 ms                                                      | 283 ms: 1.04x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 56.8 ms: 1.04x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.9 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.1 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| pickle                     | 7.43 us                                                     | 7.22 us: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 79.1 ms: 1.02x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.61 ms: 1.02x faster                                                       |
| fannkuch                   | 247 ms                                                      | 243 ms: 1.01x faster                                                        |
| aiohttp                    | 884 us                                                      | 900 us: 1.02x slower                                                        |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.58 us: 1.05x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 100.0 us: 1.05x slower                                                      |
| coverage                   | 40.8 ms                                                     | 43.2 ms: 1.06x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.05 us: 1.08x slower                                                       |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                                        |
| json                       | 3.05 ms                                                     | 3.38 ms: 1.11x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.16x slower                                                       |
| dask                       | 263 ms                                                      | 316 ms: 1.20x slower                                                        |
| create_gc_cycles           | 752 us                                                      | 906 us: 1.20x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 17.6 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (8): asyncio_tcp, regex_effbot, pickle_dict, tomli_loads, crypto_pyaes, unpickle_list, scimark_sparse_mat_mult, python_startup_no_site
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240504-3.13.0a6+-5f54758/bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown