# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-amd64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.02x faster
- HPT reliability: 80.11%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 233 ms: 1.07x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.88 sec: 1.13x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 96.3 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.46x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 536 ms: 1.44x faster                                                       |
| async_tree_io              | 731 ms                                                      | 539 ms: 1.36x faster                                                       |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.1 ms: 1.41x faster                                                      |
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 152 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 125 ms: 1.01x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 91.7 ms: 1.05x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 183 us: 1.07x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 52.4 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                                     |
| xml_etree_process    | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 135 us: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.08 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.3 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.19 ms: 1.37x faster                                                      |
| django_template | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.46x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.3 us: 1.45x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 536 ms: 1.44x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 46.8 ms: 1.43x faster                                                      |
| nbody                      | 71.9 ms                                                     | 51.1 ms: 1.41x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.50 sec: 1.39x faster                                                     |
| mako                       | 7.09 ms                                                     | 5.19 ms: 1.37x faster                                                      |
| async_tree_io              | 731 ms                                                      | 539 ms: 1.36x faster                                                       |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.34x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| deepcopy                   | 238 us                                                      | 191 us: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                       |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.09 ms: 1.22x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 40.6 ms: 1.20x faster                                                      |
| pyflate                    | 295 ms                                                      | 256 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.2 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.11x faster                                                      |
| fannkuch                   | 247 ms                                                      | 229 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 478 ms: 1.07x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.6 ms: 1.07x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 183 us: 1.07x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.4 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 987 ms: 1.06x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.3 ns: 1.06x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                                     |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.7 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.2 ms: 1.03x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.13 us: 1.02x faster                                                      |
| regex_dna                  | 126 ms                                                      | 125 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.1 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 152 ms: 1.00x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.69 us: 1.00x faster                                                      |
| raytrace                   | 192 ms                                                      | 192 ms: 1.00x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 135 us: 1.01x slower                                                       |
| pycparser                  | 699 ms                                                      | 709 ms: 1.02x slower                                                       |
| json                       | 3.05 ms                                                     | 3.14 ms: 1.03x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 835 us: 1.04x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.7 ms: 1.05x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.60 ms: 1.05x slower                                                      |
| pathlib                    | 80.5 ms                                                     | 84.7 ms: 1.05x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.06x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 73.2 ms: 1.06x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                      |
| 2to3                       | 218 ms                                                      | 233 ms: 1.07x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.08 ms: 1.07x slower                                                      |
| async_generators           | 239 ms                                                      | 257 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 201 ms: 1.08x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 96.3 ms: 1.08x slower                                                      |
| sympy_str                  | 175 ms                                                      | 189 ms: 1.08x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 98.7 ms: 1.08x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                      |
| richards                   | 28.4 ms                                                     | 30.9 ms: 1.09x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.3 ms: 1.09x slower                                                      |
| richards_super             | 32.1 ms                                                     | 35.1 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.8 ms: 1.09x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 536 ms: 1.10x slower                                                       |
| go                         | 91.6 ms                                                     | 101 ms: 1.10x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 14.7 ms: 1.13x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.88 sec: 1.13x slower                                                     |
| django_template            | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.72 ms: 1.14x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 90.5 ms: 1.15x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.74 ms: 1.16x slower                                                      |
| sympy_expand               | 284 ms                                                      | 329 ms: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.4 ms: 1.19x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 935 us: 1.24x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 120 us: 1.27x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 75.9 ms: 1.29x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 3.06 ms: 3.57x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 80.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown