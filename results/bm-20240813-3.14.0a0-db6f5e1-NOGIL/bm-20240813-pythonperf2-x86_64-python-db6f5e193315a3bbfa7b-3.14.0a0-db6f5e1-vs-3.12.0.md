# Results vs. 3.12.0

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-x86_64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.44x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 437 ms: 1.53x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.51 sec: 1.22x slower                                                      |
| tornado_http   | 121 ms                                                       | 166 ms: 1.37x slower                                                        |
| Geometric mean | (ref)                                                        | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 891 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 366 ms: 1.18x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 471 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 632 ms: 1.10x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 948 ms: 1.10x faster                                                        |
| async_tree_none            | 452 ms                                                       | 419 ms: 1.08x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 521 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 683 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 146 ms: 1.90x slower                                                        |
| nbody          | 88.0 ms                                                      | 201 ms: 2.28x slower                                                        |
| Geometric mean | (ref)                                                        | 1.60x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                       |
| regex_compile  | 144 ms                                                       | 233 ms: 1.62x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| json_loads           | 24.4 us                                                      | 29.7 us: 1.22x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 119 ms: 1.38x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.5 ms: 1.42x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 3.41 sec: 1.58x slower                                                      |
| xml_etree_process    | 58.4 ms                                                      | 97.6 ms: 1.67x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 598 us: 1.88x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 406 us: 1.94x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.42x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| python_startup         | 11.6 ms                                                      | 17.1 ms: 1.47x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.42x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 69.3 ms: 1.82x slower                                                       |
| mako            | 10.0 ms                                                      | 22.2 ms: 2.21x slower                                                       |
| Geometric mean  | (ref)                                                        | 2.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 3.48 ms                                                      | 2.79 ms: 1.24x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 891 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 366 ms: 1.18x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 471 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 632 ms: 1.10x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 948 ms: 1.10x faster                                                        |
| async_tree_none            | 452 ms                                                       | 419 ms: 1.08x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.05x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 521 ms: 1.04x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 683 ms: 1.02x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.02x faster                                                        |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.94 ms: 1.04x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 19.8 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| generators                 | 37.4 ms                                                      | 41.3 ms: 1.10x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 448 ms: 1.18x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.90 sec: 1.20x slower                                                      |
| json                       | 5.12 ms                                                      | 6.16 ms: 1.20x slower                                                       |
| json_loads                 | 24.4 us                                                      | 29.7 us: 1.22x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.51 sec: 1.22x slower                                                      |
| deepcopy                   | 368 us                                                       | 453 us: 1.23x slower                                                        |
| mdp                        | 2.57 sec                                                     | 3.25 sec: 1.27x slower                                                      |
| coroutines                 | 23.0 ms                                                      | 29.3 ms: 1.27x slower                                                       |
| async_generators           | 390 ms                                                       | 521 ms: 1.33x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.72 ms: 1.36x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 32.6 ms: 1.36x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| tornado_http               | 121 ms                                                       | 166 ms: 1.37x slower                                                        |
| scimark_fft                | 301 ms                                                       | 413 ms: 1.37x slower                                                        |
| meteor_contest             | 128 ms                                                       | 176 ms: 1.37x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 119 ms: 1.38x slower                                                        |
| comprehensions             | 21.9 us                                                      | 30.2 us: 1.38x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 14.5 ms: 1.42x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 52.3 us: 1.42x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.77 sec: 1.43x slower                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 4.85 us: 1.44x slower                                                       |
| python_startup             | 11.6 ms                                                      | 17.1 ms: 1.47x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 133 ms: 1.48x slower                                                        |
| sympy_str                  | 302 ms                                                       | 456 ms: 1.51x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 122 ms: 1.51x slower                                                        |
| telco                      | 6.96 ms                                                      | 10.6 ms: 1.52x slower                                                       |
| 2to3                       | 285 ms                                                       | 437 ms: 1.53x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 3.41 sec: 1.58x slower                                                      |
| regex_compile              | 144 ms                                                       | 233 ms: 1.62x slower                                                        |
| coverage                   | 66.7 ms                                                      | 109 ms: 1.63x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 265 ms: 1.63x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 189 ms: 1.64x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 95.4 ms: 1.66x slower                                                       |
| fannkuch                   | 350 ms                                                       | 583 ms: 1.67x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 97.6 ms: 1.67x slower                                                       |
| logging_format             | 7.48 us                                                      | 12.6 us: 1.68x slower                                                       |
| sympy_expand               | 484 ms                                                       | 823 ms: 1.70x slower                                                        |
| logging_simple             | 6.71 us                                                      | 11.6 us: 1.73x slower                                                       |
| pyflate                    | 439 ms                                                       | 774 ms: 1.76x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 1.45 sec: 1.79x slower                                                      |
| bench_thread_pool          | 950 us                                                       | 1.70 ms: 1.79x slower                                                       |
| richards                   | 45.7 ms                                                      | 82.7 ms: 1.81x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 3.00 sec: 1.82x slower                                                      |
| django_template            | 38.2 ms                                                      | 69.3 ms: 1.82x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 282 us: 1.86x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 171 ms: 1.86x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 598 us: 1.88x slower                                                        |
| float                      | 76.6 ms                                                      | 146 ms: 1.90x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.39 ms: 1.91x slower                                                       |
| richards_super             | 51.3 ms                                                      | 99.3 ms: 1.93x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 406 us: 1.94x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 134 ms: 1.94x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 186 ns: 1.97x slower                                                        |
| chaos                      | 64.0 ms                                                      | 127 ms: 1.98x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 11.9 ms: 2.00x slower                                                       |
| raytrace                   | 298 ms                                                       | 610 ms: 2.05x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.87 ms: 2.08x slower                                                       |
| mako                       | 10.0 ms                                                      | 22.2 ms: 2.21x slower                                                       |
| go                         | 150 ms                                                       | 333 ms: 2.23x slower                                                        |
| nbody                      | 88.0 ms                                                      | 201 ms: 2.28x slower                                                        |
| scimark_sor                | 109 ms                                                       | 256 ms: 2.35x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 248 ms: 2.51x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.31 ms: 2.57x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.44x slower                                                                |

Benchmark hidden because not significant (1): create_gc_cycles
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240813-3.14.0a0-db6f5e1-NOGIL/bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.08x