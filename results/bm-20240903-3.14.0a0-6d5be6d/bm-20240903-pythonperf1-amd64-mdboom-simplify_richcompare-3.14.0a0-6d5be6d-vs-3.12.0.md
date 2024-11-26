# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.004x slower
- HPT reliability: 98.63%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.6 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 558 ms: 1.38x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                                       |
| async_tree_io              | 731 ms                                                      | 572 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 80.9 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 91.4 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 66.1 ms: 1.01x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.7 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 58.5 ms: 1.05x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.08x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.92 ms: 1.02x faster                                                      |
| django_template | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 558 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.56 sec: 1.35x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                                       |
| async_tree_io              | 731 ms                                                      | 572 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                       |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.9 us: 1.19x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                      |
| go                         | 91.6 ms                                                     | 84.5 ms: 1.08x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.8 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 816 us: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.8 ms: 1.03x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.92 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 89.9 ms: 1.02x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.9 ms: 1.01x faster                                                      |
| chaos                      | 43.3 ms                                                     | 42.8 ms: 1.01x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 68.5 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| raytrace                   | 192 ms                                                      | 191 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.82 us: 1.01x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.1 ms: 1.01x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.38 us: 1.02x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.7 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 190 ms: 1.02x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.0 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.0 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.7 ns: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.9 ms: 1.04x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 91.4 ms: 1.04x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 93.6 ms: 1.05x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 58.5 ms: 1.05x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.32 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.70 ms: 1.05x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 543 ms: 1.06x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 62.6 ms: 1.06x slower                                                      |
| pycparser                  | 699 ms                                                      | 744 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                     |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.08x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 532 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 323 ms: 1.10x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 884 us: 1.10x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| richards                   | 28.4 ms                                                     | 31.6 ms: 1.11x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 87.7 ms: 1.11x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                       |
| scimark_fft                | 184 ms                                                      | 207 ms: 1.12x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.2 ms: 1.12x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.1 ms: 1.13x slower                                                      |
| nbody                      | 71.9 ms                                                     | 80.9 ms: 1.13x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| fannkuch                   | 247 ms                                                      | 288 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 908 us: 1.21x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.03 ms: 1.22x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (3): float, spectral_norm, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.004x slower
# HPT report

- Reliability score: 98.63% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown