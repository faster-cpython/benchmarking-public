# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.015x slower
- HPT reliability: 99.37%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                              |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                            |
| tornado_http   | 89.5 ms                                                     | 84.2 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                       | 1.00x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                              |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                              |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                              |
| async_tree_io_tg           | 771 ms                                                      | 562 ms: 1.37x faster                                              |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.30x faster                                              |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 398 ms: 1.26x faster                                              |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.3 ms: 1.03x faster                                             |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                              |
| nbody          | 71.9 ms                                                     | 83.8 ms: 1.17x slower                                             |
| Geometric mean | (ref)                                                       | 1.04x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                              |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                             |
| regex_compile  | 87.5 ms                                                     | 93.1 ms: 1.06x slower                                             |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.10 us: 1.05x faster                                             |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.04x faster                                             |
| pickle_list          | 2.83 us                                                     | 2.73 us: 1.03x faster                                             |
| unpickle_list        | 2.75 us                                                     | 2.78 us: 1.01x slower                                             |
| xml_etree_parse      | 93.0 ms                                                     | 94.3 ms: 1.01x slower                                             |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                             |
| xml_etree_generate   | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                             |
| xml_etree_process    | 37.7 ms                                                     | 40.9 ms: 1.09x slower                                             |
| json_dumps           | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                             |
| pickle_pure_python   | 195 us                                                      | 215 us: 1.10x slower                                              |
| unpickle             | 8.18 us                                                     | 9.12 us: 1.11x slower                                             |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                              |
| tomli_loads          | 1.37 sec                                                    | 1.61 sec: 1.18x slower                                            |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                             |
| python_startup         | 19.5 ms                                                     | 21.9 ms: 1.12x slower                                             |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.85 ms: 1.03x faster                                             |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                             |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                              |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.44x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                              |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                              |
| async_tree_io_tg           | 771 ms                                                      | 562 ms: 1.37x faster                                              |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.30x faster                                              |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 398 ms: 1.26x faster                                              |
| deepcopy                   | 238 us                                                      | 191 us: 1.25x faster                                              |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                             |
| deepcopy_memo              | 23.7 us                                                     | 20.6 us: 1.15x faster                                             |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                             |
| sqlite_synth               | 1.76 us                                                     | 1.64 us: 1.08x faster                                             |
| tornado_http               | 89.5 ms                                                     | 84.2 ms: 1.06x faster                                             |
| bench_thread_pool          | 857 us                                                      | 805 us: 1.06x faster                                              |
| pathlib                    | 80.5 ms                                                     | 75.7 ms: 1.06x faster                                             |
| generators                 | 22.5 ms                                                     | 21.3 ms: 1.06x faster                                             |
| pickle                     | 7.43 us                                                     | 7.10 us: 1.05x faster                                             |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.04x faster                                             |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                              |
| asyncio_tcp                | 487 ms                                                      | 469 ms: 1.04x faster                                              |
| bench_mp_pool              | 69.2 ms                                                     | 66.6 ms: 1.04x faster                                             |
| mako                       | 7.09 ms                                                     | 6.85 ms: 1.03x faster                                             |
| pickle_list                | 2.83 us                                                     | 2.73 us: 1.03x faster                                             |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                             |
| go                         | 91.6 ms                                                     | 88.9 ms: 1.03x faster                                             |
| float                      | 56.8 ms                                                     | 55.3 ms: 1.03x faster                                             |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                             |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                             |
| crypto_pyaes               | 48.5 ms                                                     | 47.9 ms: 1.01x faster                                             |
| sympy_sum                  | 91.5 ms                                                     | 90.6 ms: 1.01x faster                                             |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                              |
| unpickle_list              | 2.75 us                                                     | 2.78 us: 1.01x slower                                             |
| xml_etree_parse            | 93.0 ms                                                     | 94.3 ms: 1.01x slower                                             |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                              |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                             |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                             |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                              |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                            |
| raytrace                   | 192 ms                                                      | 197 ms: 1.02x slower                                              |
| chaos                      | 43.3 ms                                                     | 44.9 ms: 1.04x slower                                             |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                              |
| spectral_norm              | 66.9 ms                                                     | 69.9 ms: 1.04x slower                                             |
| xml_etree_generate         | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                             |
| nqueens                    | 62.8 ms                                                     | 65.9 ms: 1.05x slower                                             |
| logging_silent             | 60.5 ns                                                     | 63.5 ns: 1.05x slower                                             |
| logging_format             | 6.72 us                                                     | 7.08 us: 1.05x slower                                             |
| sqlglot_normalize          | 187 ms                                                      | 197 ms: 1.06x slower                                              |
| meteor_contest             | 74.6 ms                                                     | 78.9 ms: 1.06x slower                                             |
| regex_compile              | 87.5 ms                                                     | 93.1 ms: 1.06x slower                                             |
| logging_simple             | 6.28 us                                                     | 6.68 us: 1.06x slower                                             |
| sqlglot_optimize           | 34.5 ms                                                     | 36.8 ms: 1.07x slower                                             |
| pprint_safe_repr           | 513 ms                                                      | 551 ms: 1.07x slower                                              |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.07x slower                                              |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                             |
| deltablue                  | 2.16 ms                                                     | 2.32 ms: 1.08x slower                                             |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                            |
| xml_etree_process          | 37.7 ms                                                     | 40.9 ms: 1.09x slower                                             |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.10x slower                                             |
| mdp                        | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                            |
| json_dumps                 | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                             |
| pyflate                    | 295 ms                                                      | 324 ms: 1.10x slower                                              |
| pickle_pure_python         | 195 us                                                      | 215 us: 1.10x slower                                              |
| pycparser                  | 699 ms                                                      | 770 ms: 1.10x slower                                              |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                             |
| unpickle                   | 8.18 us                                                     | 9.12 us: 1.11x slower                                             |
| scimark_lu                 | 58.9 ms                                                     | 65.7 ms: 1.12x slower                                             |
| sqlglot_parse              | 804 us                                                      | 902 us: 1.12x slower                                              |
| python_startup             | 19.5 ms                                                     | 21.9 ms: 1.12x slower                                             |
| hexiom                     | 4.10 ms                                                     | 4.62 ms: 1.13x slower                                             |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                             |
| unpack_sequence            | 37.5 ns                                                     | 42.7 ns: 1.14x slower                                             |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.93 ms: 1.15x slower                                             |
| richards_super             | 32.1 ms                                                     | 36.9 ms: 1.15x slower                                             |
| scimark_sor                | 78.8 ms                                                     | 90.7 ms: 1.15x slower                                             |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                              |
| scimark_fft                | 184 ms                                                      | 212 ms: 1.15x slower                                              |
| richards                   | 28.4 ms                                                     | 33.0 ms: 1.16x slower                                             |
| nbody                      | 71.9 ms                                                     | 83.8 ms: 1.17x slower                                             |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                              |
| create_gc_cycles           | 752 us                                                      | 882 us: 1.17x slower                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.4 ms: 1.18x slower                                             |
| tomli_loads                | 1.37 sec                                                    | 1.61 sec: 1.18x slower                                            |
| coverage                   | 40.8 ms                                                     | 48.5 ms: 1.19x slower                                             |
| fannkuch                   | 247 ms                                                      | 308 ms: 1.25x slower                                              |
| telco                      | 4.13 ms                                                     | 5.20 ms: 1.26x slower                                             |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (3): xml_etree_iterparse, gc_traversal, json
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.015x slower
# HPT report

- Reliability score: 99.37% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown