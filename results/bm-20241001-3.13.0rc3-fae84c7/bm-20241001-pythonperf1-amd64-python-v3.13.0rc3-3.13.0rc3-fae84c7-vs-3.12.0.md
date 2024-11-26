# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc3
- machine: windows-amd64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 216 ms: 1.01x faster                                              |
| chameleon      | 4.98 ms                                                     | 4.89 ms: 1.02x faster                                             |
| docutils       | 1.66 sec                                                    | 1.56 sec: 1.07x faster                                            |
| tornado_http   | 89.5 ms                                                     | 92.2 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                       | 1.01x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 506 ms: 1.52x faster                                              |
| async_tree_io              | 731 ms                                                      | 516 ms: 1.42x faster                                              |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.41x faster                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 370 ms: 1.36x faster                                              |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 374 ms: 1.31x faster                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 286 ms: 1.28x faster                                              |
| async_tree_memoization     | 339 ms                                                      | 270 ms: 1.26x faster                                              |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.3 ms: 1.13x faster                                             |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                              |
| nbody          | 71.9 ms                                                     | 71.0 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                       | 1.05x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                              |
| regex_compile  | 87.5 ms                                                     | 83.8 ms: 1.04x faster                                             |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                             |
| regex_v8       | 14.2 ms                                                     | 17.1 ms: 1.20x slower                                             |
| Geometric mean | (ref)                                                       | 1.01x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 183 us: 1.07x faster                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                             |
| xml_etree_generate   | 55.8 ms                                                     | 53.0 ms: 1.05x faster                                             |
| unpickle_list        | 2.75 us                                                     | 2.66 us: 1.03x faster                                             |
| pickle               | 7.43 us                                                     | 7.21 us: 1.03x faster                                             |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                             |
| xml_etree_parse      | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                             |
| unpickle_pure_python | 133 us                                                      | 130 us: 1.02x faster                                              |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                             |
| json_dumps           | 5.70 ms                                                     | 5.78 ms: 1.01x slower                                             |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                            |
| unpickle             | 8.18 us                                                     | 8.49 us: 1.04x slower                                             |
| pickle_list          | 2.83 us                                                     | 3.11 us: 1.10x slower                                             |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                      |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                             |
| python_startup         | 19.5 ms                                                     | 22.4 ms: 1.15x slower                                             |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.68 ms: 1.06x faster                                             |
| django_template | 22.9 ms                                                     | 22.1 ms: 1.04x faster                                             |
| Geometric mean  | (ref)                                                       | 1.05x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 506 ms: 1.52x faster                                              |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.47 sec: 1.42x faster                                            |
| async_tree_io              | 731 ms                                                      | 516 ms: 1.42x faster                                              |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.41x faster                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 370 ms: 1.36x faster                                              |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                             |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 374 ms: 1.31x faster                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 286 ms: 1.28x faster                                              |
| async_tree_memoization     | 339 ms                                                      | 270 ms: 1.26x faster                                              |
| mypy2                      | 509 ms                                                      | 431 ms: 1.18x faster                                              |
| raytrace                   | 192 ms                                                      | 165 ms: 1.17x faster                                              |
| logging_silent             | 60.5 ns                                                     | 53.2 ns: 1.14x faster                                             |
| deltablue                  | 2.16 ms                                                     | 1.90 ms: 1.13x faster                                             |
| float                      | 56.8 ms                                                     | 50.3 ms: 1.13x faster                                             |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                             |
| nqueens                    | 62.8 ms                                                     | 56.9 ms: 1.10x faster                                             |
| logging_simple             | 6.28 us                                                     | 5.70 us: 1.10x faster                                             |
| logging_format             | 6.72 us                                                     | 6.11 us: 1.10x faster                                             |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                             |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                             |
| async_generators           | 239 ms                                                      | 219 ms: 1.09x faster                                              |
| bench_thread_pool          | 857 us                                                      | 786 us: 1.09x faster                                              |
| spectral_norm              | 66.9 ms                                                     | 61.5 ms: 1.09x faster                                             |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.08x faster                                             |
| richards_super             | 32.1 ms                                                     | 29.8 ms: 1.08x faster                                             |
| richards                   | 28.4 ms                                                     | 26.4 ms: 1.07x faster                                             |
| go                         | 91.6 ms                                                     | 85.4 ms: 1.07x faster                                             |
| dulwich_log                | 44.3 ms                                                     | 41.4 ms: 1.07x faster                                             |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                              |
| sqlglot_normalize          | 187 ms                                                      | 175 ms: 1.07x faster                                              |
| pickle_pure_python         | 195 us                                                      | 183 us: 1.07x faster                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                             |
| hexiom                     | 4.10 ms                                                     | 3.85 ms: 1.07x faster                                             |
| docutils                   | 1.66 sec                                                    | 1.56 sec: 1.07x faster                                            |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.1 ms: 1.06x faster                                             |
| mako                       | 7.09 ms                                                     | 6.68 ms: 1.06x faster                                             |
| crypto_pyaes               | 48.5 ms                                                     | 45.7 ms: 1.06x faster                                             |
| sympy_sum                  | 91.5 ms                                                     | 86.8 ms: 1.05x faster                                             |
| xml_etree_generate         | 55.8 ms                                                     | 53.0 ms: 1.05x faster                                             |
| deepcopy                   | 238 us                                                      | 226 us: 1.05x faster                                              |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                              |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                              |
| scimark_fft                | 184 ms                                                      | 176 ms: 1.05x faster                                              |
| regex_compile              | 87.5 ms                                                     | 83.8 ms: 1.04x faster                                             |
| pprint_safe_repr           | 513 ms                                                      | 492 ms: 1.04x faster                                              |
| sqlglot_transpile          | 1.02 ms                                                     | 980 us: 1.04x faster                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                            |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                             |
| deepcopy_memo              | 23.7 us                                                     | 22.8 us: 1.04x faster                                             |
| django_template            | 22.9 ms                                                     | 22.1 ms: 1.04x faster                                             |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.04x faster                                             |
| unpickle_list              | 2.75 us                                                     | 2.66 us: 1.03x faster                                             |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                             |
| pickle                     | 7.43 us                                                     | 7.21 us: 1.03x faster                                             |
| sqlglot_optimize           | 34.5 ms                                                     | 33.5 ms: 1.03x faster                                             |
| scimark_lu                 | 58.9 ms                                                     | 57.2 ms: 1.03x faster                                             |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                             |
| scimark_sor                | 78.8 ms                                                     | 76.9 ms: 1.02x faster                                             |
| xml_etree_parse            | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                             |
| unpickle_pure_python       | 133 us                                                      | 130 us: 1.02x faster                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.50 ms: 1.02x faster                                             |
| json                       | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                             |
| sqlglot_parse              | 804 us                                                      | 789 us: 1.02x faster                                              |
| chameleon                  | 4.98 ms                                                     | 4.89 ms: 1.02x faster                                             |
| pathlib                    | 80.5 ms                                                     | 79.3 ms: 1.01x faster                                             |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                              |
| nbody                      | 71.9 ms                                                     | 71.0 ms: 1.01x faster                                             |
| meteor_contest             | 74.6 ms                                                     | 73.9 ms: 1.01x faster                                             |
| 2to3                       | 218 ms                                                      | 216 ms: 1.01x faster                                              |
| mdp                        | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                            |
| fannkuch                   | 247 ms                                                      | 246 ms: 1.00x faster                                              |
| unpack_sequence            | 37.5 ns                                                     | 37.8 ns: 1.01x slower                                             |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                             |
| json_dumps                 | 5.70 ms                                                     | 5.78 ms: 1.01x slower                                             |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                             |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                            |
| tornado_http               | 89.5 ms                                                     | 92.2 ms: 1.03x slower                                             |
| unpickle                   | 8.18 us                                                     | 8.49 us: 1.04x slower                                             |
| asyncio_tcp                | 487 ms                                                      | 517 ms: 1.06x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                              |
| create_gc_cycles           | 752 us                                                      | 807 us: 1.07x slower                                              |
| aiohttp                    | 884 us                                                      | 950 us: 1.07x slower                                              |
| pycparser                  | 699 ms                                                      | 758 ms: 1.09x slower                                              |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                             |
| pickle_list                | 2.83 us                                                     | 3.11 us: 1.10x slower                                             |
| telco                      | 4.13 ms                                                     | 4.61 ms: 1.12x slower                                             |
| coverage                   | 40.8 ms                                                     | 45.9 ms: 1.12x slower                                             |
| python_startup             | 19.5 ms                                                     | 22.4 ms: 1.15x slower                                             |
| regex_v8                   | 14.2 ms                                                     | 17.1 ms: 1.20x slower                                             |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                      |

Benchmark hidden because not significant (3): bench_mp_pool, sympy_expand, pickle_dict
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.068x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown