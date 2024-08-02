# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmer_side_exits
- machine: windows-amd64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.05x faster
- HPT reliability: 90.48%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 238 ms: 1.09x slower                                                          |
| docutils       | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                        |
| tornado_http   | 89.5 ms                                                     | 84.1 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 193 ms: 1.48x faster                                                          |
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 528 ms: 1.46x faster                                                          |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                          |
| async_tree_io              | 731 ms                                                      | 550 ms: 1.33x faster                                                          |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.31x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                          |
| Geometric mean             | (ref)                                                       | 1.38x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                         |
| float          | 56.8 ms                                                     | 45.9 ms: 1.24x faster                                                         |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                          |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                         |
| regex_compile  | 87.5 ms                                                     | 89.4 ms: 1.02x slower                                                         |
| regex_v8       | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 118 us: 1.13x faster                                                          |
| tomli_loads          | 1.37 sec                                                    | 1.27 sec: 1.07x faster                                                        |
| pickle_pure_python   | 195 us                                                      | 183 us: 1.07x faster                                                          |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                         |
| xml_etree_generate   | 55.8 ms                                                     | 54.5 ms: 1.02x faster                                                         |
| xml_etree_parse      | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                         |
| xml_etree_process    | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                         |
| json_dumps           | 5.70 ms                                                     | 5.95 ms: 1.04x slower                                                         |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                         |
| python_startup         | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.15 ms: 1.37x faster                                                         |
| django_template | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.41 sec: 1.49x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 193 ms: 1.48x faster                                                          |
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                          |
| deepcopy_memo              | 23.7 us                                                     | 16.2 us: 1.46x faster                                                         |
| async_tree_io_tg           | 771 ms                                                      | 528 ms: 1.46x faster                                                          |
| spectral_norm              | 66.9 ms                                                     | 47.4 ms: 1.41x faster                                                         |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                          |
| nbody                      | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                         |
| comprehensions             | 14.1 us                                                     | 10.1 us: 1.39x faster                                                         |
| mako                       | 7.09 ms                                                     | 5.15 ms: 1.37x faster                                                         |
| async_tree_io              | 731 ms                                                      | 550 ms: 1.33x faster                                                          |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.31x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                          |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                          |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.25x faster                                                          |
| float                      | 56.8 ms                                                     | 45.9 ms: 1.24x faster                                                         |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.10 ms: 1.22x faster                                                         |
| crypto_pyaes               | 48.5 ms                                                     | 40.9 ms: 1.19x faster                                                         |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.15x faster                                                         |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.3 ms: 1.14x faster                                                         |
| unpickle_pure_python       | 133 us                                                      | 118 us: 1.13x faster                                                          |
| pyflate                    | 295 ms                                                      | 266 ms: 1.11x faster                                                          |
| bench_thread_pool          | 857 us                                                      | 782 us: 1.10x faster                                                          |
| fannkuch                   | 247 ms                                                      | 227 ms: 1.09x faster                                                          |
| chaos                      | 43.3 ms                                                     | 40.3 ms: 1.08x faster                                                         |
| pprint_safe_repr           | 513 ms                                                      | 477 ms: 1.07x faster                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.27 sec: 1.07x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 978 ms: 1.07x faster                                                          |
| pickle_pure_python         | 195 us                                                      | 183 us: 1.07x faster                                                          |
| tornado_http               | 89.5 ms                                                     | 84.1 ms: 1.06x faster                                                         |
| pathlib                    | 80.5 ms                                                     | 75.8 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                         |
| logging_simple             | 6.28 us                                                     | 5.99 us: 1.05x faster                                                         |
| nqueens                    | 62.8 ms                                                     | 60.0 ms: 1.05x faster                                                         |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                          |
| logging_format             | 6.72 us                                                     | 6.44 us: 1.04x faster                                                         |
| logging_silent             | 60.5 ns                                                     | 58.1 ns: 1.04x faster                                                         |
| raytrace                   | 192 ms                                                      | 187 ms: 1.03x faster                                                          |
| xml_etree_generate         | 55.8 ms                                                     | 54.5 ms: 1.02x faster                                                         |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                         |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                          |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                         |
| meteor_contest             | 74.6 ms                                                     | 73.6 ms: 1.01x faster                                                         |
| xml_etree_parse            | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                         |
| richards                   | 28.4 ms                                                     | 29.0 ms: 1.02x slower                                                         |
| regex_compile              | 87.5 ms                                                     | 89.4 ms: 1.02x slower                                                         |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.02x slower                                                         |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.03x slower                                                         |
| richards_super             | 32.1 ms                                                     | 32.9 ms: 1.03x slower                                                         |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                          |
| sqlglot_parse              | 804 us                                                      | 830 us: 1.03x slower                                                          |
| sqlglot_normalize          | 187 ms                                                      | 194 ms: 1.04x slower                                                          |
| sympy_sum                  | 91.5 ms                                                     | 95.0 ms: 1.04x slower                                                         |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.07 ms: 1.04x slower                                                         |
| xml_etree_process          | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                         |
| json_dumps                 | 5.70 ms                                                     | 5.95 ms: 1.04x slower                                                         |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                         |
| telco                      | 4.13 ms                                                     | 4.39 ms: 1.06x slower                                                         |
| go                         | 91.6 ms                                                     | 97.5 ms: 1.07x slower                                                         |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                         |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                         |
| docutils                   | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                        |
| python_startup             | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                         |
| regex_v8                   | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                         |
| generators                 | 22.5 ms                                                     | 24.5 ms: 1.09x slower                                                         |
| 2to3                       | 218 ms                                                      | 238 ms: 1.09x slower                                                          |
| deltablue                  | 2.16 ms                                                     | 2.36 ms: 1.09x slower                                                         |
| sympy_integrate            | 13.0 ms                                                     | 14.2 ms: 1.09x slower                                                         |
| sympy_expand               | 284 ms                                                      | 316 ms: 1.11x slower                                                          |
| hexiom                     | 4.10 ms                                                     | 4.61 ms: 1.12x slower                                                         |
| coverage                   | 40.8 ms                                                     | 46.6 ms: 1.14x slower                                                         |
| async_generators           | 239 ms                                                      | 274 ms: 1.14x slower                                                          |
| pycparser                  | 699 ms                                                      | 802 ms: 1.15x slower                                                          |
| django_template            | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                         |
| scimark_sor                | 78.8 ms                                                     | 93.2 ms: 1.18x slower                                                         |
| create_gc_cycles           | 752 us                                                      | 910 us: 1.21x slower                                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 118 us: 1.24x slower                                                          |
| scimark_lu                 | 58.9 ms                                                     | 73.4 ms: 1.25x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                  |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_tcp
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 90.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown