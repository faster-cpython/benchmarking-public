# Results vs. 3.12.0

- fork: python
- ref: 6343486eb60ac5a9e154
- machine: windows-amd64
- commit hash: 6343486
- commit date: 2024-07-02
- overall geometric mean: 1.01x faster
- HPT reliability: 80.47%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 81.5 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 191 ms: 1.49x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 525 ms: 1.47x faster                                                       |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io              | 731 ms                                                      | 539 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.39x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| float          | 56.8 ms                                                     | 56.3 ms: 1.01x faster                                                      |
| nbody          | 71.9 ms                                                     | 79.9 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 122 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 85.4 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 17.3 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 93.9 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.99 ms: 1.05x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.12x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.0 ms: 1.05x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| mako            | 7.09 ms                                                     | 7.64 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 191 ms: 1.49x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 525 ms: 1.47x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.52 sec: 1.38x faster                                                     |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io              | 731 ms                                                      | 539 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.30x faster                                                       |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.8 us: 1.14x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 767 us: 1.12x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 81.5 ms: 1.10x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 76.0 ms: 1.06x faster                                                      |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 66.1 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.1 ms: 1.04x faster                                                      |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.03x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 476 ms: 1.02x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 85.4 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 185 ms: 1.01x faster                                                       |
| float                      | 56.8 ms                                                     | 56.3 ms: 1.01x faster                                                      |
| chaos                      | 43.3 ms                                                     | 43.2 ms: 1.00x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 93.9 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 34.9 ms: 1.01x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 67.6 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| go                         | 91.6 ms                                                     | 92.9 ms: 1.01x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.54 ms: 1.01x slower                                                      |
| async_generators           | 239 ms                                                      | 243 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                     |
| richards_super             | 32.1 ms                                                     | 33.4 ms: 1.04x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 535 ms: 1.04x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.9 ms: 1.04x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.29 ms: 1.05x slower                                                      |
| richards                   | 28.4 ms                                                     | 29.7 ms: 1.05x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.0 ms: 1.05x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 78.3 ms: 1.05x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.99 ms: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| pyflate                    | 295 ms                                                      | 311 ms: 1.06x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 51.2 ms: 1.06x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 83.9 ms: 1.07x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 64.7 ns: 1.07x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                                      |
| mako                       | 7.09 ms                                                     | 7.64 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 63.8 ms: 1.08x slower                                                      |
| pycparser                  | 699 ms                                                      | 759 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.1 ms: 1.10x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 889 us: 1.11x slower                                                       |
| coverage                   | 40.8 ms                                                     | 45.2 ms: 1.11x slower                                                      |
| nbody                      | 71.9 ms                                                     | 79.9 ms: 1.11x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.12x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| scimark_fft                | 184 ms                                                      | 211 ms: 1.15x slower                                                       |
| fannkuch                   | 247 ms                                                      | 285 ms: 1.16x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.99 ms: 1.17x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.17x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 892 us: 1.19x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.97 ms: 1.20x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 17.3 ms: 1.21x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (8): regex_effbot, logging_simple, logging_format, nqueens, sympy_integrate, mdp, deltablue, generators
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240702-3.14.0a0-6343486/bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 80.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown