# Results vs. 3.12.0

- fork: python
- ref: 759a54d28ffe7eac8c23
- machine: linux-x86_64
- commit hash: 759a54d
- commit date: 2024-10-22
- overall geometric mean: 1.09x slower
- HPT reliability: 87.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 314 ms: 1.10x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.22 sec: 1.12x slower                                                       |
| tornado_http   | 121 ms                                                       | 124 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 377 ms: 1.43x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                         |
| async_tree_none            | 452 ms                                                       | 342 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 328 ms: 1.31x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 842 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 564 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 870 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| nbody          | 88.0 ms                                                      | 85.6 ms: 1.03x faster                                                        |
| float          | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 242 ms: 1.01x slower                                                         |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.3 ms: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.29x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.42 ms: 1.06x faster                                                        |
| django_template | 38.2 ms                                                      | 43.4 ms: 1.14x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 377 ms: 1.43x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                         |
| async_tree_none            | 452 ms                                                       | 342 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 328 ms: 1.31x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 842 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 564 ms: 1.24x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 30.0 us: 1.23x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 870 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                         |
| deepcopy                   | 368 us                                                       | 309 us: 1.19x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.8 us: 1.17x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.03 us: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.2 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.09x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.42 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.12 us: 1.05x faster                                                        |
| scimark_fft                | 301 ms                                                       | 287 ms: 1.05x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 63.1 ms: 1.04x faster                                                        |
| nbody                      | 88.0 ms                                                      | 85.6 ms: 1.03x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.54 us: 1.03x faster                                                        |
| scimark_sor                | 109 ms                                                       | 106 ms: 1.03x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 794 ms: 1.02x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 97.3 ms: 1.02x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                         |
| richards_super             | 51.3 ms                                                      | 51.0 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.6 ms: 1.00x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                       |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.01x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.29 ms: 1.02x slower                                                        |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                        |
| tornado_http               | 121 ms                                                       | 124 ms: 1.02x slower                                                         |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| go                         | 150 ms                                                       | 154 ms: 1.03x slower                                                         |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.26 ms: 1.03x slower                                                        |
| pyflate                    | 439 ms                                                       | 452 ms: 1.03x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 60.3 ms: 1.03x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.66 sec: 1.03x slower                                                       |
| float                      | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 98.2 ns: 1.04x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 95.7 ms: 1.04x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.40 ms: 1.05x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                         |
| generators                 | 37.4 ms                                                      | 39.7 ms: 1.06x slower                                                        |
| sympy_str                  | 302 ms                                                       | 323 ms: 1.07x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| fannkuch                   | 350 ms                                                       | 380 ms: 1.09x slower                                                         |
| chaos                      | 64.0 ms                                                      | 69.5 ms: 1.09x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 177 ms: 1.09x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.10x slower                                                        |
| 2to3                       | 285 ms                                                       | 314 ms: 1.10x slower                                                         |
| sympy_expand               | 484 ms                                                       | 534 ms: 1.10x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.75 ms: 1.11x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.22 sec: 1.12x slower                                                       |
| raytrace                   | 298 ms                                                       | 336 ms: 1.13x slower                                                         |
| django_template            | 38.2 ms                                                      | 43.4 ms: 1.14x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 103 ms: 1.15x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 27.6 ms: 1.15x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 133 ms: 1.15x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 181 us: 1.19x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.21 ms: 1.21x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 69.6 ms: 1.21x slower                                                        |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.29x slower                                                        |
| coverage                   | 66.7 ms                                                      | 86.3 ms: 1.29x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.53 ms: 1.59x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.89 ms: 1.82x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.18 sec: 458.00x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (3): async_generators, bench_thread_pool, richards
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241022-3.14.0a1+-759a54d-JIT/bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 87.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x