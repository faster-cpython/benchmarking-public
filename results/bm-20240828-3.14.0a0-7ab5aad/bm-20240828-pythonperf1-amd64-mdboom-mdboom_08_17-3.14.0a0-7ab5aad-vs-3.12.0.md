# Results vs. 3.12.0

- fork: mdboom
- ref: mdboom_08_17
- machine: windows-amd64
- commit hash: 7ab5aad
- commit date: 2024-08-28
- overall geometric mean: 1.016x slower
- HPT reliability: 99.71%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 233 ms: 1.07x slower                                               |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                             |
| tornado_http   | 89.5 ms                                                     | 93.5 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                       | 1.05x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.45x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.44x faster                                               |
| async_tree_io_tg           | 771 ms                                                      | 548 ms: 1.41x faster                                               |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 394 ms: 1.27x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 267 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                               |
| async_tree_io              | 731 ms                                                      | 581 ms: 1.26x faster                                               |
| Geometric mean             | (ref)                                                       | 1.33x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 56.1 ms: 1.01x faster                                              |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                               |
| nbody          | 71.9 ms                                                     | 85.1 ms: 1.18x slower                                              |
| Geometric mean | (ref)                                                       | 1.05x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                               |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                              |
| regex_compile  | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                              |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                       | 1.00x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 96.0 ms: 1.03x slower                                              |
| xml_etree_generate   | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                              |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.06x slower                                              |
| xml_etree_process    | 37.7 ms                                                     | 40.2 ms: 1.07x slower                                              |
| json_dumps           | 5.70 ms                                                     | 6.08 ms: 1.07x slower                                              |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.07x slower                                               |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                               |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                             |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                              |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                              |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.98 ms: 1.02x faster                                              |
| django_template | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                              |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.45x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.44x faster                                               |
| async_tree_io_tg           | 771 ms                                                      | 548 ms: 1.41x faster                                               |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 394 ms: 1.27x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 267 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                               |
| async_tree_io              | 731 ms                                                      | 581 ms: 1.26x faster                                               |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                               |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.68 sec: 1.25x faster                                             |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.18x faster                                              |
| deepcopy_memo              | 23.7 us                                                     | 20.3 us: 1.17x faster                                              |
| generators                 | 22.5 ms                                                     | 20.6 ms: 1.09x faster                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                              |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                               |
| bench_thread_pool          | 857 us                                                      | 825 us: 1.04x faster                                               |
| pathlib                    | 80.5 ms                                                     | 77.9 ms: 1.03x faster                                              |
| dulwich_log                | 44.3 ms                                                     | 43.0 ms: 1.03x faster                                              |
| raytrace                   | 192 ms                                                      | 187 ms: 1.03x faster                                               |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                              |
| mako                       | 7.09 ms                                                     | 6.98 ms: 1.02x faster                                              |
| float                      | 56.8 ms                                                     | 56.1 ms: 1.01x faster                                              |
| bench_mp_pool              | 69.2 ms                                                     | 68.4 ms: 1.01x faster                                              |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                              |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                               |
| sympy_sum                  | 91.5 ms                                                     | 90.8 ms: 1.01x faster                                              |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                              |
| logging_format             | 6.72 us                                                     | 6.78 us: 1.01x slower                                              |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                              |
| json                       | 3.05 ms                                                     | 3.09 ms: 1.01x slower                                              |
| chaos                      | 43.3 ms                                                     | 44.0 ms: 1.01x slower                                              |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                               |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                              |
| nqueens                    | 62.8 ms                                                     | 64.7 ms: 1.03x slower                                              |
| xml_etree_parse            | 93.0 ms                                                     | 96.0 ms: 1.03x slower                                              |
| regex_compile              | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                              |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                               |
| xml_etree_generate         | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                              |
| mdp                        | 1.37 sec                                                    | 1.42 sec: 1.03x slower                                             |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                              |
| gc_traversal               | 1.52 ms                                                     | 1.58 ms: 1.04x slower                                              |
| logging_silent             | 60.5 ns                                                     | 62.9 ns: 1.04x slower                                              |
| meteor_contest             | 74.6 ms                                                     | 77.8 ms: 1.04x slower                                              |
| sqlglot_optimize           | 34.5 ms                                                     | 36.0 ms: 1.04x slower                                              |
| tornado_http               | 89.5 ms                                                     | 93.5 ms: 1.04x slower                                              |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                              |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                             |
| async_generators           | 239 ms                                                      | 253 ms: 1.06x slower                                               |
| hexiom                     | 4.10 ms                                                     | 4.36 ms: 1.06x slower                                              |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.06x slower                                              |
| xml_etree_process          | 37.7 ms                                                     | 40.2 ms: 1.07x slower                                              |
| go                         | 91.6 ms                                                     | 97.6 ms: 1.07x slower                                              |
| spectral_norm              | 66.9 ms                                                     | 71.3 ms: 1.07x slower                                              |
| 2to3                       | 218 ms                                                      | 233 ms: 1.07x slower                                               |
| json_dumps                 | 5.70 ms                                                     | 6.08 ms: 1.07x slower                                              |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.07x slower                                               |
| scimark_lu                 | 58.9 ms                                                     | 63.3 ms: 1.07x slower                                              |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                              |
| pprint_safe_repr           | 513 ms                                                      | 555 ms: 1.08x slower                                               |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.08x slower                                               |
| django_template            | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.14 sec: 1.09x slower                                             |
| pyflate                    | 295 ms                                                      | 325 ms: 1.10x slower                                               |
| sqlglot_parse              | 804 us                                                      | 889 us: 1.11x slower                                               |
| asyncio_tcp                | 487 ms                                                      | 539 ms: 1.11x slower                                               |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                              |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.86 ms: 1.12x slower                                              |
| scimark_fft                | 184 ms                                                      | 207 ms: 1.12x slower                                               |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.5 ms: 1.13x slower                                              |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                              |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                             |
| richards                   | 28.4 ms                                                     | 33.3 ms: 1.17x slower                                              |
| richards_super             | 32.1 ms                                                     | 37.7 ms: 1.18x slower                                              |
| scimark_sor                | 78.8 ms                                                     | 93.0 ms: 1.18x slower                                              |
| nbody                      | 71.9 ms                                                     | 85.1 ms: 1.18x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                               |
| fannkuch                   | 247 ms                                                      | 297 ms: 1.20x slower                                               |
| create_gc_cycles           | 752 us                                                      | 908 us: 1.21x slower                                               |
| telco                      | 4.13 ms                                                     | 4.99 ms: 1.21x slower                                              |
| coverage                   | 40.8 ms                                                     | 50.1 ms: 1.23x slower                                              |
| pycparser                  | 699 ms                                                      | 871 ms: 1.25x slower                                               |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240828-3.14.0a0-7ab5aad/bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.016x slower
# HPT report

- Reliability score: 99.71% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown