# Results vs. 3.12.0

- fork: python
- ref: 760872efecb95017db8e
- machine: linux-x86_64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.09x slower
- HPT reliability: 74.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 315 ms: 1.10x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.20 sec: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 378 ms: 1.43x faster                                                         |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 846 ms: 1.23x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 873 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.21x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.9 ms: 1.07x faster                                                        |
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| float          | 76.6 ms                                                      | 79.8 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.44 ms: 1.04x faster                                                        |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                                         |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 24.6 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.13 sec: 1.02x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 57.9 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.78 us: 1.03x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.3 us: 1.03x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 149 ms: 1.03x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                         |
| pickle_dict          | 32.5 us                                                      | 34.0 us: 1.04x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                         |
| pickle_list          | 4.43 us                                                      | 4.76 us: 1.07x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.46 ms: 1.06x faster                                                        |
| django_template | 38.2 ms                                                      | 43.4 ms: 1.14x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 378 ms: 1.43x faster                                                         |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 846 ms: 1.23x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 873 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.21x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.20x faster                                                        |
| deepcopy                   | 368 us                                                       | 308 us: 1.19x faster                                                         |
| comprehensions             | 21.9 us                                                      | 18.5 us: 1.18x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 31.3 us: 1.17x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 71.5 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.05 us: 1.11x faster                                                        |
| nbody                      | 88.0 ms                                                      | 81.9 ms: 1.07x faster                                                        |
| scimark_fft                | 301 ms                                                       | 282 ms: 1.07x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.7 ms: 1.06x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.46 ms: 1.06x faster                                                        |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.05x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 95.1 ms: 1.04x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.44 ms: 1.04x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.23 us: 1.04x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 91.4 ns: 1.03x faster                                                        |
| async_generators           | 390 ms                                                       | 380 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.71 us: 1.03x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 790 ms: 1.02x faster                                                         |
| richards                   | 45.7 ms                                                      | 44.8 ms: 1.02x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.59 us: 1.02x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.13 sec: 1.02x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.2 ms: 1.01x faster                                                        |
| json                       | 5.12 ms                                                      | 5.07 ms: 1.01x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 57.9 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 65.7 ms: 1.01x slower                                                        |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                         |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 93.1 ms: 1.02x slower                                                        |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                                         |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.30 ms: 1.02x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.78 us: 1.03x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                       |
| generators                 | 37.4 ms                                                      | 38.6 ms: 1.03x slower                                                        |
| richards_super             | 51.3 ms                                                      | 53.0 ms: 1.03x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.3 us: 1.03x slower                                                        |
| pyflate                    | 439 ms                                                       | 453 ms: 1.03x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 149 ms: 1.03x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 330 us: 1.04x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.37 ms: 1.04x slower                                                        |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                         |
| float                      | 76.6 ms                                                      | 79.8 ms: 1.04x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.6 ms: 1.04x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 34.0 us: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.05x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                         |
| sympy_str                  | 302 ms                                                       | 318 ms: 1.05x slower                                                         |
| fannkuch                   | 350 ms                                                       | 371 ms: 1.06x slower                                                         |
| sympy_sum                  | 162 ms                                                       | 173 ms: 1.07x slower                                                         |
| pickle_list                | 4.43 us                                                      | 4.76 us: 1.07x slower                                                        |
| chaos                      | 64.0 ms                                                      | 69.1 ms: 1.08x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                        |
| raytrace                   | 298 ms                                                       | 327 ms: 1.10x slower                                                         |
| sympy_expand               | 484 ms                                                       | 532 ms: 1.10x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                        |
| 2to3                       | 285 ms                                                       | 315 ms: 1.10x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.97 ms: 1.11x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.20 sec: 1.12x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.90 ms: 1.13x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.13x slower                                                         |
| django_template            | 38.2 ms                                                      | 43.4 ms: 1.14x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 27.2 ms: 1.14x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 132 ms: 1.14x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.06 ms: 1.18x slower                                                        |
| coverage                   | 66.7 ms                                                      | 80.2 ms: 1.20x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.20x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 69.5 ms: 1.21x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.49 ms: 1.58x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 91.0 ns: 1.71x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.87 ms: 1.81x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 3.28 sec: 688.92x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (5): asyncio_tcp, pickle, asyncio_websockets, bench_thread_pool, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 74.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x