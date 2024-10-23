# Results vs. 3.12.0

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 031f320
- commit date: 2024-10-23
- overall geometric mean: 1.09x slower
- HPT reliability: 72.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 317 ms: 1.11x slower                                                                   |
| docutils       | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                                                 |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 371 ms: 1.45x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 321 ms: 1.34x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 337 ms: 1.34x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 409 ms: 1.33x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 819 ms: 1.27x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 560 ms: 1.24x faster                                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 861 ms: 1.22x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                                   |
| nbody          | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                                                  |
| float          | 76.6 ms                                                      | 80.7 ms: 1.05x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                                   |
| regex_effbot   | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                                  |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                                   |
| regex_v8       | 23.6 ms                                                      | 24.8 ms: 1.05x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.0 ms: 1.08x faster                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 56.9 ms: 1.03x faster                                                                  |
| tomli_loads          | 2.16 sec                                                     | 2.13 sec: 1.02x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.01x faster                                                                   |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                                  |
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                                   |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                                                   |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                                  |
| pickle_pure_python   | 318 us                                                       | 340 us: 1.07x slower                                                                   |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.11 ms: 1.05x slower                                                                  |
| python_startup         | 11.6 ms                                                      | 15.1 ms: 1.30x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.44 ms: 1.06x faster                                                                  |
| django_template | 38.2 ms                                                      | 43.8 ms: 1.15x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 371 ms: 1.45x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 321 ms: 1.34x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 337 ms: 1.34x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 409 ms: 1.33x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 819 ms: 1.27x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 560 ms: 1.24x faster                                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 861 ms: 1.22x faster                                                                   |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.21x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                                   |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                                  |
| deepcopy                   | 368 us                                                       | 316 us: 1.17x faster                                                                   |
| comprehensions             | 21.9 us                                                      | 18.9 us: 1.16x faster                                                                  |
| coroutines                 | 23.0 ms                                                      | 20.4 ms: 1.13x faster                                                                  |
| deepcopy_reduce            | 3.37 us                                                      | 3.04 us: 1.11x faster                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 73.2 ms: 1.10x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 80.0 ms: 1.08x faster                                                                  |
| mako                       | 10.0 ms                                                      | 9.44 ms: 1.06x faster                                                                  |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                                   |
| scimark_fft                | 301 ms                                                       | 288 ms: 1.05x faster                                                                   |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                                   |
| logging_format             | 7.48 us                                                      | 7.18 us: 1.04x faster                                                                  |
| nbody                      | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 784 ms: 1.03x faster                                                                   |
| async_generators           | 390 ms                                                       | 380 ms: 1.03x faster                                                                   |
| xml_etree_process          | 58.4 ms                                                      | 56.9 ms: 1.03x faster                                                                  |
| dulwich_log                | 65.4 ms                                                      | 63.8 ms: 1.02x faster                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                                 |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                                   |
| scimark_lu                 | 98.8 ms                                                      | 97.2 ms: 1.02x faster                                                                  |
| tomli_loads                | 2.16 sec                                                     | 2.13 sec: 1.02x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.01x faster                                                                   |
| regex_effbot               | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                                  |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                                  |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.25 ms: 1.01x slower                                                                  |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                                   |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                                                   |
| json                       | 5.12 ms                                                      | 5.21 ms: 1.02x slower                                                                  |
| spectral_norm              | 91.6 ms                                                      | 93.3 ms: 1.02x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 3.29 ms: 1.02x slower                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 70.3 ms: 1.02x slower                                                                  |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                                   |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                                   |
| generators                 | 37.4 ms                                                      | 38.9 ms: 1.04x slower                                                                  |
| pyflate                    | 439 ms                                                       | 456 ms: 1.04x slower                                                                   |
| regex_v8                   | 23.6 ms                                                      | 24.8 ms: 1.05x slower                                                                  |
| go                         | 150 ms                                                       | 157 ms: 1.05x slower                                                                   |
| pycparser                  | 1.23 sec                                                     | 1.30 sec: 1.05x slower                                                                 |
| float                      | 76.6 ms                                                      | 80.7 ms: 1.05x slower                                                                  |
| python_startup_no_site     | 8.64 ms                                                      | 9.11 ms: 1.05x slower                                                                  |
| richards                   | 45.7 ms                                                      | 48.3 ms: 1.06x slower                                                                  |
| chaos                      | 64.0 ms                                                      | 67.7 ms: 1.06x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                                                   |
| sympy_str                  | 302 ms                                                       | 321 ms: 1.06x slower                                                                   |
| richards_super             | 51.3 ms                                                      | 54.6 ms: 1.06x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 340 us: 1.07x slower                                                                   |
| fannkuch                   | 350 ms                                                       | 375 ms: 1.07x slower                                                                   |
| sympy_sum                  | 162 ms                                                       | 175 ms: 1.08x slower                                                                   |
| raytrace                   | 298 ms                                                       | 323 ms: 1.08x slower                                                                   |
| logging_silent             | 94.4 ns                                                      | 103 ns: 1.09x slower                                                                   |
| sqlglot_parse              | 1.38 ms                                                      | 1.52 ms: 1.10x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 533 ms: 1.10x slower                                                                   |
| telco                      | 6.96 ms                                                      | 7.69 ms: 1.10x slower                                                                  |
| nqueens                    | 89.9 ms                                                      | 99.5 ms: 1.11x slower                                                                  |
| 2to3                       | 285 ms                                                       | 317 ms: 1.11x slower                                                                   |
| docutils                   | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.99 ms: 1.12x slower                                                                  |
| sympy_integrate            | 23.9 ms                                                      | 27.3 ms: 1.14x slower                                                                  |
| django_template            | 38.2 ms                                                      | 43.8 ms: 1.15x slower                                                                  |
| sqlglot_normalize          | 116 ms                                                       | 135 ms: 1.16x slower                                                                   |
| coverage                   | 66.7 ms                                                      | 79.3 ms: 1.19x slower                                                                  |
| typing_runtime_protocols   | 152 us                                                       | 182 us: 1.20x slower                                                                   |
| hexiom                     | 5.96 ms                                                      | 7.20 ms: 1.21x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 69.7 ms: 1.21x slower                                                                  |
| python_startup             | 11.6 ms                                                      | 15.1 ms: 1.30x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 5.80 ms: 1.67x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 2.92 ms: 1.84x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 2.57 sec: 539.56x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, logging_simple, bench_thread_pool
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241023-3.14.0a1+-031f320-JIT/bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 72.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x