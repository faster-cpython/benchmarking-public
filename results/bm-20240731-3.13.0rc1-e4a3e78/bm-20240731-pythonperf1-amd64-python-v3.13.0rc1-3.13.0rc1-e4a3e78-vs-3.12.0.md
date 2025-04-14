# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc1
- machine: windows-amd64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.027x faster
- HPT reliability: 94.82%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                              |
| chameleon      | 4.98 ms                                                     | 5.10 ms: 1.02x slower                                             |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                            |
| tornado_http   | 89.5 ms                                                     | 92.0 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 272 ms: 1.35x faster                                              |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                              |
| async_tree_none            | 291 ms                                                      | 228 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                              |
| async_tree_io_tg           | 771 ms                                                      | 627 ms: 1.23x faster                                              |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                              |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                              |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.1 ms: 1.13x faster                                             |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                              |
| nbody          | 71.9 ms                                                     | 76.8 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                       | 1.02x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 83.9 ms: 1.04x faster                                             |
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                              |
| regex_v8       | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                             |
| xml_etree_parse      | 93.0 ms                                                     | 91.5 ms: 1.02x faster                                             |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                             |
| pickle_pure_python   | 195 us                                                      | 194 us: 1.01x faster                                              |
| xml_etree_process    | 37.7 ms                                                     | 38.4 ms: 1.02x slower                                             |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                             |
| json_dumps           | 5.70 ms                                                     | 5.90 ms: 1.04x slower                                             |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                            |
| unpickle_pure_python | 133 us                                                      | 138 us: 1.04x slower                                              |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                             |
| python_startup         | 19.5 ms                                                     | 22.5 ms: 1.15x slower                                             |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.66 ms: 1.06x faster                                             |
| django_template | 22.9 ms                                                     | 22.7 ms: 1.01x faster                                             |
| Geometric mean  | (ref)                                                       | 1.04x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 272 ms: 1.35x faster                                              |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                              |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.29x faster                                             |
| async_tree_none            | 291 ms                                                      | 228 ms: 1.28x faster                                              |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.68 sec: 1.25x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                              |
| async_tree_io_tg           | 771 ms                                                      | 627 ms: 1.23x faster                                              |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                              |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                              |
| raytrace                   | 192 ms                                                      | 164 ms: 1.18x faster                                              |
| mypy2                      | 509 ms                                                      | 439 ms: 1.16x faster                                              |
| float                      | 56.8 ms                                                     | 50.1 ms: 1.13x faster                                             |
| coroutines                 | 14.3 ms                                                     | 13.0 ms: 1.10x faster                                             |
| generators                 | 22.5 ms                                                     | 20.6 ms: 1.09x faster                                             |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                             |
| logging_silent             | 60.5 ns                                                     | 56.1 ns: 1.08x faster                                             |
| logging_simple             | 6.28 us                                                     | 5.85 us: 1.07x faster                                             |
| chaos                      | 43.3 ms                                                     | 40.4 ms: 1.07x faster                                             |
| deltablue                  | 2.16 ms                                                     | 2.01 ms: 1.07x faster                                             |
| logging_format             | 6.72 us                                                     | 6.29 us: 1.07x faster                                             |
| mako                       | 7.09 ms                                                     | 6.66 ms: 1.06x faster                                             |
| bench_thread_pool          | 857 us                                                      | 813 us: 1.05x faster                                              |
| nqueens                    | 62.8 ms                                                     | 59.8 ms: 1.05x faster                                             |
| sympy_sum                  | 91.5 ms                                                     | 87.6 ms: 1.05x faster                                             |
| regex_compile              | 87.5 ms                                                     | 83.9 ms: 1.04x faster                                             |
| sqlglot_normalize          | 187 ms                                                      | 180 ms: 1.04x faster                                              |
| spectral_norm              | 66.9 ms                                                     | 64.3 ms: 1.04x faster                                             |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                              |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                             |
| go                         | 91.6 ms                                                     | 88.6 ms: 1.03x faster                                             |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.03x faster                                              |
| crypto_pyaes               | 48.5 ms                                                     | 47.4 ms: 1.02x faster                                             |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                             |
| meteor_contest             | 74.6 ms                                                     | 73.3 ms: 1.02x faster                                             |
| sqlglot_optimize           | 34.5 ms                                                     | 33.9 ms: 1.02x faster                                             |
| xml_etree_parse            | 93.0 ms                                                     | 91.5 ms: 1.02x faster                                             |
| sqlglot_transpile          | 1.02 ms                                                     | 1.01 ms: 1.01x faster                                             |
| django_template            | 22.9 ms                                                     | 22.7 ms: 1.01x faster                                             |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                              |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                             |
| pickle_pure_python         | 195 us                                                      | 194 us: 1.01x faster                                              |
| hexiom                     | 4.10 ms                                                     | 4.08 ms: 1.00x faster                                             |
| pprint_safe_repr           | 513 ms                                                      | 512 ms: 1.00x faster                                              |
| pyflate                    | 295 ms                                                      | 298 ms: 1.01x slower                                              |
| deepcopy_reduce            | 2.09 us                                                     | 2.11 us: 1.01x slower                                             |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                            |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.4 ms: 1.01x slower                                             |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                             |
| xml_etree_process          | 37.7 ms                                                     | 38.4 ms: 1.02x slower                                             |
| sympy_expand               | 284 ms                                                      | 289 ms: 1.02x slower                                              |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                             |
| pathlib                    | 80.5 ms                                                     | 82.3 ms: 1.02x slower                                             |
| chameleon                  | 4.98 ms                                                     | 5.10 ms: 1.02x slower                                             |
| tornado_http               | 89.5 ms                                                     | 92.0 ms: 1.03x slower                                             |
| bench_mp_pool              | 69.2 ms                                                     | 71.1 ms: 1.03x slower                                             |
| json_dumps                 | 5.70 ms                                                     | 5.90 ms: 1.04x slower                                             |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                            |
| unpickle_pure_python       | 133 us                                                      | 138 us: 1.04x slower                                              |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                              |
| gc_traversal               | 1.52 ms                                                     | 1.58 ms: 1.04x slower                                             |
| scimark_fft                | 184 ms                                                      | 192 ms: 1.04x slower                                              |
| scimark_sor                | 78.8 ms                                                     | 81.9 ms: 1.04x slower                                             |
| scimark_lu                 | 58.9 ms                                                     | 61.4 ms: 1.04x slower                                             |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                             |
| deepcopy_memo              | 23.7 us                                                     | 24.9 us: 1.05x slower                                             |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                            |
| nbody                      | 71.9 ms                                                     | 76.8 ms: 1.07x slower                                             |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                              |
| fannkuch                   | 247 ms                                                      | 271 ms: 1.10x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                              |
| coverage                   | 40.8 ms                                                     | 45.7 ms: 1.12x slower                                             |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                             |
| regex_v8                   | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                             |
| python_startup             | 19.5 ms                                                     | 22.5 ms: 1.15x slower                                             |
| telco                      | 4.13 ms                                                     | 4.79 ms: 1.16x slower                                             |
| create_gc_cycles           | 752 us                                                      | 917 us: 1.22x slower                                              |
| asyncio_tcp                | 487 ms                                                      | 631 ms: 1.30x slower                                              |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                      |

Benchmark hidden because not significant (6): deepcopy, richards, sqlglot_parse, regex_effbot, richards_super, pprint_pformat
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 94.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown