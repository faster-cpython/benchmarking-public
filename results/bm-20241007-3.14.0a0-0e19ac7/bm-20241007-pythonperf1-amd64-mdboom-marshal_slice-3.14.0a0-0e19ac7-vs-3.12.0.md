# Results vs. 3.12.0

- fork: mdboom
- ref: marshal_slice
- machine: windows-amd64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.01x slower
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                              |
| tornado_http   | 89.5 ms                                                     | 92.9 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                       | 1.03x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.45x faster                                                |
| async_tree_none_tg         | 285 ms                                                      | 201 ms: 1.42x faster                                                |
| async_tree_none            | 291 ms                                                      | 207 ms: 1.41x faster                                                |
| async_tree_io_tg           | 771 ms                                                      | 566 ms: 1.36x faster                                                |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.30x faster                                                |
| async_tree_io              | 731 ms                                                      | 573 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 56.0 ms: 1.01x faster                                               |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                |
| nbody          | 71.9 ms                                                     | 81.0 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                       | 1.03x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                               |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                               |
| regex_compile  | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                       | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.12 us: 1.04x faster                                               |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                               |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.02x slower                                               |
| pickle_list          | 2.83 us                                                     | 2.90 us: 1.03x slower                                               |
| xml_etree_generate   | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                               |
| xml_etree_process    | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                               |
| pickle_pure_python   | 195 us                                                      | 215 us: 1.10x slower                                                |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                               |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.13x slower                                                |
| unpickle             | 8.18 us                                                     | 9.30 us: 1.14x slower                                               |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                              |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                        |

Benchmark hidden because not significant (3): unpickle_list, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                               |
| python_startup         | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.93 ms: 1.02x faster                                               |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                               |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.45x faster                                                |
| async_tree_none_tg         | 285 ms                                                      | 201 ms: 1.42x faster                                                |
| async_tree_none            | 291 ms                                                      | 207 ms: 1.41x faster                                                |
| async_tree_io_tg           | 771 ms                                                      | 566 ms: 1.36x faster                                                |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.56 sec: 1.35x faster                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.30x faster                                                |
| deepcopy                   | 238 us                                                      | 185 us: 1.28x faster                                                |
| async_tree_io              | 731 ms                                                      | 573 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                               |
| deepcopy_memo              | 23.7 us                                                     | 20.1 us: 1.18x faster                                               |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                               |
| generators                 | 22.5 ms                                                     | 20.9 ms: 1.08x faster                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.08x faster                                               |
| go                         | 91.6 ms                                                     | 87.1 ms: 1.05x faster                                               |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                               |
| bench_thread_pool          | 857 us                                                      | 819 us: 1.05x faster                                                |
| pickle                     | 7.43 us                                                     | 7.12 us: 1.04x faster                                               |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                               |
| mako                       | 7.09 ms                                                     | 6.93 ms: 1.02x faster                                               |
| pathlib                    | 80.5 ms                                                     | 78.8 ms: 1.02x faster                                               |
| sympy_sum                  | 91.5 ms                                                     | 90.0 ms: 1.02x faster                                               |
| float                      | 56.8 ms                                                     | 56.0 ms: 1.01x faster                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                               |
| dulwich_log                | 44.3 ms                                                     | 43.8 ms: 1.01x faster                                               |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                |
| chaos                      | 43.3 ms                                                     | 43.5 ms: 1.00x slower                                               |
| logging_simple             | 6.28 us                                                     | 6.33 us: 1.01x slower                                               |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.02x slower                                               |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                |
| logging_format             | 6.72 us                                                     | 6.82 us: 1.02x slower                                               |
| crypto_pyaes               | 48.5 ms                                                     | 49.3 ms: 1.02x slower                                               |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                              |
| meteor_contest             | 74.6 ms                                                     | 76.3 ms: 1.02x slower                                               |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                |
| pickle_list                | 2.83 us                                                     | 2.90 us: 1.03x slower                                               |
| spectral_norm              | 66.9 ms                                                     | 68.8 ms: 1.03x slower                                               |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                               |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                                |
| unpack_sequence            | 37.5 ns                                                     | 38.5 ns: 1.03x slower                                               |
| nqueens                    | 62.8 ms                                                     | 64.6 ms: 1.03x slower                                               |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                               |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                              |
| pycparser                  | 699 ms                                                      | 720 ms: 1.03x slower                                                |
| regex_compile              | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                               |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                               |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                |
| tornado_http               | 89.5 ms                                                     | 92.9 ms: 1.04x slower                                               |
| xml_etree_generate         | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                               |
| logging_silent             | 60.5 ns                                                     | 63.1 ns: 1.04x slower                                               |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                               |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                               |
| pprint_safe_repr           | 513 ms                                                      | 542 ms: 1.06x slower                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.72 ms: 1.06x slower                                               |
| hexiom                     | 4.10 ms                                                     | 4.37 ms: 1.07x slower                                               |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                               |
| xml_etree_process          | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                               |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                               |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                |
| pyflate                    | 295 ms                                                      | 319 ms: 1.08x slower                                                |
| asyncio_tcp                | 487 ms                                                      | 532 ms: 1.09x slower                                                |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                               |
| sqlglot_parse              | 804 us                                                      | 880 us: 1.09x slower                                                |
| pickle_pure_python         | 195 us                                                      | 215 us: 1.10x slower                                                |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                               |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.4 ms: 1.11x slower                                               |
| scimark_fft                | 184 ms                                                      | 205 ms: 1.11x slower                                                |
| scimark_lu                 | 58.9 ms                                                     | 65.8 ms: 1.12x slower                                               |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.13x slower                                                |
| nbody                      | 71.9 ms                                                     | 81.0 ms: 1.13x slower                                               |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                               |
| python_startup             | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                               |
| richards                   | 28.4 ms                                                     | 32.2 ms: 1.14x slower                                               |
| unpickle                   | 8.18 us                                                     | 9.30 us: 1.14x slower                                               |
| scimark_sor                | 78.8 ms                                                     | 90.4 ms: 1.15x slower                                               |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                |
| fannkuch                   | 247 ms                                                      | 288 ms: 1.17x slower                                                |
| telco                      | 4.13 ms                                                     | 4.84 ms: 1.17x slower                                               |
| coverage                   | 40.8 ms                                                     | 49.2 ms: 1.20x slower                                               |
| create_gc_cycles           | 752 us                                                      | 917 us: 1.22x slower                                                |
| json                       | 3.05 ms                                                     | 4.27 ms: 1.40x slower                                               |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                        |

Benchmark hidden because not significant (4): bench_mp_pool, unpickle_list, pickle_dict, xml_etree_parse
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.62% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown