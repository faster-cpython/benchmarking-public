# Results vs. 3.12.0

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: windows-amd64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.04x faster
- HPT reliability: 74.95%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 91.1 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 241 ms: 1.52x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 522 ms: 1.48x faster                                                       |
| async_tree_none            | 291 ms                                                      | 207 ms: 1.41x faster                                                       |
| async_tree_io              | 731 ms                                                      | 530 ms: 1.38x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 250 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 381 ms: 1.29x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.41x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.3 ms: 1.04x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 75.2 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 85.0 ms: 1.03x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 15.8 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 193 us: 1.01x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.80 ms: 1.02x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 38.5 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 7.09 ms                                                     | 6.88 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 241 ms: 1.52x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 522 ms: 1.48x faster                                                       |
| async_tree_none            | 291 ms                                                      | 207 ms: 1.41x faster                                                       |
| async_tree_io              | 731 ms                                                      | 530 ms: 1.38x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 250 ms: 1.36x faster                                                       |
| deepcopy                   | 238 us                                                      | 177 us: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 381 ms: 1.29x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.63 sec: 1.28x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.25x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| raytrace                   | 192 ms                                                      | 169 ms: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.99 ms: 1.08x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 793 us: 1.08x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.88 us: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.33 us: 1.06x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.1 ns: 1.06x faster                                                      |
| sqlglot_normalize          | 187 ms                                                      | 178 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.4 ms: 1.05x faster                                                      |
| float                      | 56.8 ms                                                     | 54.3 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.0 ms: 1.04x faster                                                      |
| go                         | 91.6 ms                                                     | 88.1 ms: 1.04x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.8 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.88 ms: 1.03x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 85.0 ms: 1.03x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.98 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 67.4 ms: 1.03x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 33.6 ms: 1.03x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.02x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.7 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 193 us: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.9 ms: 1.00x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| async_generators           | 239 ms                                                      | 241 ms: 1.01x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 59.4 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.01x slower                                                     |
| spectral_norm              | 66.9 ms                                                     | 67.8 ms: 1.01x slower                                                      |
| pyflate                    | 295 ms                                                      | 299 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 91.1 ms: 1.02x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.80 ms: 1.02x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.5 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                                      |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 528 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| nbody                      | 71.9 ms                                                     | 75.2 ms: 1.05x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 843 us: 1.05x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 83.0 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| asyncio_tcp                | 487 ms                                                      | 528 ms: 1.08x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.8 ms: 1.11x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.6 ms: 1.11x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                      |
| scimark_fft                | 184 ms                                                      | 207 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.91 ms: 1.14x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.17x slower                                                      |
| fannkuch                   | 247 ms                                                      | 290 ms: 1.18x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 899 us: 1.19x slower                                                       |
| pycparser                  | 699 ms                                                      | 852 ms: 1.22x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (5): xml_etree_iterparse, django_template, pathlib, xml_etree_parse, xml_etree_generate
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240723-3.14.0a0-2c1b1e7/bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 74.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown