# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc2
- machine: windows-amd64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 216 ms: 1.01x faster                                              |
| chameleon      | 4.98 ms                                                     | 4.89 ms: 1.02x faster                                             |
| docutils       | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                            |
| tornado_http   | 89.5 ms                                                     | 92.6 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                       | 1.00x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 266 ms: 1.38x faster                                              |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.36x faster                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.32x faster                                              |
| async_tree_none            | 291 ms                                                      | 222 ms: 1.31x faster                                              |
| async_tree_io_tg           | 771 ms                                                      | 613 ms: 1.26x faster                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                              |
| async_tree_memoization     | 339 ms                                                      | 273 ms: 1.24x faster                                              |
| async_tree_io              | 731 ms                                                      | 591 ms: 1.24x faster                                              |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.1 ms: 1.13x faster                                             |
| nbody          | 71.9 ms                                                     | 68.0 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                       | 1.06x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 82.0 ms: 1.07x faster                                             |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                       | 1.00x slower                                                      |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 6.91 us: 1.08x faster                                             |
| unpickle_list        | 2.75 us                                                     | 2.60 us: 1.06x faster                                             |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.06x faster                                              |
| pickle_pure_python   | 195 us                                                      | 185 us: 1.06x faster                                              |
| xml_etree_generate   | 55.8 ms                                                     | 54.4 ms: 1.03x faster                                             |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                             |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                            |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                             |
| json_dumps           | 5.70 ms                                                     | 5.80 ms: 1.02x slower                                             |
| pickle_list          | 2.83 us                                                     | 2.94 us: 1.04x slower                                             |
| unpickle             | 8.18 us                                                     | 8.78 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                      |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                             |
| python_startup         | 19.5 ms                                                     | 22.3 ms: 1.14x slower                                             |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.50 ms: 1.09x faster                                             |
| django_template | 22.9 ms                                                     | 22.1 ms: 1.04x faster                                             |
| Geometric mean  | (ref)                                                       | 1.06x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 266 ms: 1.38x faster                                              |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.36x faster                                              |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                             |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.32x faster                                              |
| async_tree_none            | 291 ms                                                      | 222 ms: 1.31x faster                                              |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.63 sec: 1.29x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 613 ms: 1.26x faster                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                              |
| async_tree_memoization     | 339 ms                                                      | 273 ms: 1.24x faster                                              |
| async_tree_io              | 731 ms                                                      | 591 ms: 1.24x faster                                              |
| raytrace                   | 192 ms                                                      | 162 ms: 1.19x faster                                              |
| mypy2                      | 509 ms                                                      | 433 ms: 1.18x faster                                              |
| deltablue                  | 2.16 ms                                                     | 1.90 ms: 1.14x faster                                             |
| logging_silent             | 60.5 ns                                                     | 53.3 ns: 1.14x faster                                             |
| float                      | 56.8 ms                                                     | 50.1 ms: 1.13x faster                                             |
| unpack_sequence            | 37.5 ns                                                     | 33.1 ns: 1.13x faster                                             |
| chaos                      | 43.3 ms                                                     | 38.3 ms: 1.13x faster                                             |
| generators                 | 22.5 ms                                                     | 20.2 ms: 1.12x faster                                             |
| logging_simple             | 6.28 us                                                     | 5.67 us: 1.11x faster                                             |
| coroutines                 | 14.3 ms                                                     | 12.9 ms: 1.11x faster                                             |
| logging_format             | 6.72 us                                                     | 6.09 us: 1.10x faster                                             |
| nqueens                    | 62.8 ms                                                     | 57.3 ms: 1.10x faster                                             |
| hexiom                     | 4.10 ms                                                     | 3.75 ms: 1.09x faster                                             |
| spectral_norm              | 66.9 ms                                                     | 61.2 ms: 1.09x faster                                             |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                             |
| mako                       | 7.09 ms                                                     | 6.50 ms: 1.09x faster                                             |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.35 ms: 1.09x faster                                             |
| richards_super             | 32.1 ms                                                     | 29.5 ms: 1.09x faster                                             |
| crypto_pyaes               | 48.5 ms                                                     | 44.6 ms: 1.09x faster                                             |
| richards                   | 28.4 ms                                                     | 26.2 ms: 1.08x faster                                             |
| pickle                     | 7.43 us                                                     | 6.91 us: 1.08x faster                                             |
| sqlglot_normalize          | 187 ms                                                      | 174 ms: 1.07x faster                                              |
| scimark_fft                | 184 ms                                                      | 172 ms: 1.07x faster                                              |
| go                         | 91.6 ms                                                     | 85.7 ms: 1.07x faster                                             |
| regex_compile              | 87.5 ms                                                     | 82.0 ms: 1.07x faster                                             |
| deepcopy                   | 238 us                                                      | 223 us: 1.07x faster                                              |
| unpickle_list              | 2.75 us                                                     | 2.60 us: 1.06x faster                                             |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.06x faster                                              |
| nbody                      | 71.9 ms                                                     | 68.0 ms: 1.06x faster                                             |
| pickle_pure_python         | 195 us                                                      | 185 us: 1.06x faster                                              |
| dulwich_log                | 44.3 ms                                                     | 42.0 ms: 1.06x faster                                             |
| sympy_sum                  | 91.5 ms                                                     | 87.3 ms: 1.05x faster                                             |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.8 ms: 1.05x faster                                             |
| scimark_sor                | 78.8 ms                                                     | 75.3 ms: 1.05x faster                                             |
| pyflate                    | 295 ms                                                      | 282 ms: 1.04x faster                                              |
| deepcopy_memo              | 23.7 us                                                     | 22.7 us: 1.04x faster                                             |
| scimark_lu                 | 58.9 ms                                                     | 56.5 ms: 1.04x faster                                             |
| sqlglot_optimize           | 34.5 ms                                                     | 33.2 ms: 1.04x faster                                             |
| django_template            | 22.9 ms                                                     | 22.1 ms: 1.04x faster                                             |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.04x faster                                             |
| pprint_safe_repr           | 513 ms                                                      | 494 ms: 1.04x faster                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.04x faster                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 985 us: 1.04x faster                                              |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.03x faster                                              |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                             |
| meteor_contest             | 74.6 ms                                                     | 72.2 ms: 1.03x faster                                             |
| async_generators           | 239 ms                                                      | 232 ms: 1.03x faster                                              |
| bench_thread_pool          | 857 us                                                      | 832 us: 1.03x faster                                              |
| xml_etree_generate         | 55.8 ms                                                     | 54.4 ms: 1.03x faster                                             |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                             |
| chameleon                  | 4.98 ms                                                     | 4.89 ms: 1.02x faster                                             |
| bench_mp_pool              | 69.2 ms                                                     | 68.0 ms: 1.02x faster                                             |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                             |
| sqlglot_parse              | 804 us                                                      | 793 us: 1.01x faster                                              |
| pathlib                    | 80.5 ms                                                     | 79.6 ms: 1.01x faster                                             |
| 2to3                       | 218 ms                                                      | 216 ms: 1.01x faster                                              |
| fannkuch                   | 247 ms                                                      | 248 ms: 1.00x slower                                              |
| docutils                   | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                            |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                            |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                             |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                             |
| json_dumps                 | 5.70 ms                                                     | 5.80 ms: 1.02x slower                                             |
| sympy_expand               | 284 ms                                                      | 291 ms: 1.02x slower                                              |
| tornado_http               | 89.5 ms                                                     | 92.6 ms: 1.03x slower                                             |
| pickle_list                | 2.83 us                                                     | 2.94 us: 1.04x slower                                             |
| pycparser                  | 699 ms                                                      | 733 ms: 1.05x slower                                              |
| aiohttp                    | 884 us                                                      | 946 us: 1.07x slower                                              |
| unpickle                   | 8.18 us                                                     | 8.78 us: 1.07x slower                                             |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                             |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.08x slower                                            |
| asyncio_tcp                | 487 ms                                                      | 530 ms: 1.09x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                              |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                             |
| coverage                   | 40.8 ms                                                     | 46.0 ms: 1.13x slower                                             |
| python_startup             | 19.5 ms                                                     | 22.3 ms: 1.14x slower                                             |
| telco                      | 4.13 ms                                                     | 4.74 ms: 1.15x slower                                             |
| create_gc_cycles           | 752 us                                                      | 901 us: 1.20x slower                                              |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                      |

Benchmark hidden because not significant (6): regex_dna, pidigits, xml_etree_parse, xml_etree_process, pickle_dict, regex_effbot
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.059x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown