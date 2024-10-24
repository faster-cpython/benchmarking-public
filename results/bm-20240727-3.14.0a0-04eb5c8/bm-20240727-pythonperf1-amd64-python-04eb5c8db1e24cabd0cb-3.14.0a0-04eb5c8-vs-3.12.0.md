# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-amd64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 234 ms: 1.07x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.3 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 249 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.45x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 548 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 559 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 391 ms: 1.28x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 83.2 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 17.5 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 58.9 ms: 1.05x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 249 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.45x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 548 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.56 sec: 1.34x faster                                                     |
| async_tree_io              | 731 ms                                                      | 559 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 391 ms: 1.28x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                       |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.17x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.6 us: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.3 ms: 1.11x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 805 us: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.7 ms: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| float                      | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.6 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 80.9 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| raytrace                   | 192 ms                                                      | 197 ms: 1.02x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.02x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.4 ms: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.43 us: 1.02x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 64.5 ms: 1.03x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.0 ms: 1.03x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.98 us: 1.04x slower                                                      |
| json                       | 3.05 ms                                                     | 3.17 ms: 1.04x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 93.3 ms: 1.04x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 50.6 ms: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 72.7 ms: 1.05x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                     |
| logging_silent             | 60.5 ns                                                     | 63.7 ns: 1.05x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 58.9 ms: 1.05x slower                                                      |
| go                         | 91.6 ms                                                     | 96.8 ms: 1.06x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 70.9 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.8 ms: 1.06x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 63.2 ms: 1.07x slower                                                      |
| 2to3                       | 218 ms                                                      | 234 ms: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.43 ms: 1.08x slower                                                      |
| pyflate                    | 295 ms                                                      | 319 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.79 ms: 1.09x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 533 ms: 1.09x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                     |
| json_dumps                 | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 886 us: 1.10x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 566 ms: 1.10x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.15 sec: 1.10x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 88.0 ms: 1.12x slower                                                      |
| scimark_fft                | 184 ms                                                      | 206 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.4 ms: 1.13x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.3 ms: 1.14x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.0 ms: 1.15x slower                                                      |
| nbody                      | 71.9 ms                                                     | 83.2 ms: 1.16x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.9 ms: 1.16x slower                                                      |
| fannkuch                   | 247 ms                                                      | 291 ms: 1.18x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.89 ms: 1.18x slower                                                      |
| pycparser                  | 699 ms                                                      | 834 ms: 1.19x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 908 us: 1.21x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.5 ms: 1.23x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (3): mako, xml_etree_parse, async_generators
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown