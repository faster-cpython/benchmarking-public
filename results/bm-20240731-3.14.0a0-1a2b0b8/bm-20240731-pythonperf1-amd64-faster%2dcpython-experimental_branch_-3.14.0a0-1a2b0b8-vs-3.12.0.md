# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.02x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 234 ms: 1.07x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                               |
| tornado_http   | 89.5 ms                                                     | 93.4 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 246 ms: 1.49x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.45x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 543 ms: 1.42x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 573 ms: 1.28x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                                 |
| nbody          | 71.9 ms                                                     | 92.0 ms: 1.28x slower                                                                |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                                |
| regex_compile  | 87.5 ms                                                     | 95.0 ms: 1.09x slower                                                                |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 66.0 ms: 1.01x slower                                                                |
| xml_etree_parse      | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                                |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 58.1 ms: 1.04x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.43 ms: 1.13x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.61 sec: 1.18x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                                |
| python_startup         | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.25 ms: 1.02x slower                                                                |
| django_template | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 246 ms: 1.49x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.45x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 543 ms: 1.42x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 573 ms: 1.28x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                                 |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                                |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.85 sec: 1.13x faster                                                               |
| deepcopy_memo              | 23.7 us                                                     | 21.1 us: 1.12x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.08x faster                                                                |
| bench_thread_pool          | 857 us                                                      | 808 us: 1.06x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 42.7 ms: 1.04x faster                                                                |
| generators                 | 22.5 ms                                                     | 22.0 ms: 1.02x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                                |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                                 |
| sympy_sum                  | 91.5 ms                                                     | 92.1 ms: 1.01x slower                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.0 ms: 1.01x slower                                                                |
| raytrace                   | 192 ms                                                      | 196 ms: 1.02x slower                                                                 |
| logging_simple             | 6.28 us                                                     | 6.39 us: 1.02x slower                                                                |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                                 |
| xml_etree_parse            | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                                |
| mako                       | 7.09 ms                                                     | 7.25 ms: 1.02x slower                                                                |
| logging_format             | 6.72 us                                                     | 6.89 us: 1.03x slower                                                                |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                                 |
| nqueens                    | 62.8 ms                                                     | 64.9 ms: 1.03x slower                                                                |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.04x slower                                                                 |
| chaos                      | 43.3 ms                                                     | 44.9 ms: 1.04x slower                                                                |
| json                       | 3.05 ms                                                     | 3.17 ms: 1.04x slower                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                                |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 58.1 ms: 1.04x slower                                                                |
| tornado_http               | 89.5 ms                                                     | 93.4 ms: 1.04x slower                                                                |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.05x slower                                                                |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                                                |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                               |
| meteor_contest             | 74.6 ms                                                     | 79.0 ms: 1.06x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 64.4 ns: 1.06x slower                                                                |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                               |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 51.8 ms: 1.07x slower                                                                |
| 2to3                       | 218 ms                                                      | 234 ms: 1.07x slower                                                                 |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                                |
| pycparser                  | 699 ms                                                      | 752 ms: 1.08x slower                                                                 |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                                |
| regex_compile              | 87.5 ms                                                     | 95.0 ms: 1.09x slower                                                                |
| go                         | 91.6 ms                                                     | 99.7 ms: 1.09x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                                |
| sympy_expand               | 284 ms                                                      | 311 ms: 1.10x slower                                                                 |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.10x slower                                                                |
| asyncio_tcp                | 487 ms                                                      | 539 ms: 1.11x slower                                                                 |
| spectral_norm              | 66.9 ms                                                     | 74.1 ms: 1.11x slower                                                                |
| pprint_safe_repr           | 513 ms                                                      | 569 ms: 1.11x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.16 sec: 1.11x slower                                                               |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                                                 |
| python_startup             | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                                |
| scimark_lu                 | 58.9 ms                                                     | 65.5 ms: 1.11x slower                                                                |
| pyflate                    | 295 ms                                                      | 330 ms: 1.12x slower                                                                 |
| hexiom                     | 4.10 ms                                                     | 4.61 ms: 1.13x slower                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.88 ms: 1.13x slower                                                                |
| sqlglot_parse              | 804 us                                                      | 906 us: 1.13x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.43 ms: 1.13x slower                                                                |
| scimark_fft                | 184 ms                                                      | 212 ms: 1.15x slower                                                                 |
| richards_super             | 32.1 ms                                                     | 37.0 ms: 1.15x slower                                                                |
| richards                   | 28.4 ms                                                     | 32.8 ms: 1.16x slower                                                                |
| coverage                   | 40.8 ms                                                     | 47.4 ms: 1.16x slower                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.2 ms: 1.17x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                                 |
| create_gc_cycles           | 752 us                                                      | 885 us: 1.18x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.61 sec: 1.18x slower                                                               |
| telco                      | 4.13 ms                                                     | 4.93 ms: 1.19x slower                                                                |
| fannkuch                   | 247 ms                                                      | 301 ms: 1.22x slower                                                                 |
| scimark_sor                | 78.8 ms                                                     | 96.5 ms: 1.22x slower                                                                |
| nbody                      | 71.9 ms                                                     | 92.0 ms: 1.28x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (4): float, bench_mp_pool, pathlib, coroutines
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown