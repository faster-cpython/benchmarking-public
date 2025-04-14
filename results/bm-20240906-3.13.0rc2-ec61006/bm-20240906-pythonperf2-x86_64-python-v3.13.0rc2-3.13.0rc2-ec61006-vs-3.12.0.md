# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.004x slower
- HPT reliability: 88.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 291 ms: 1.02x slower                                               |
| chameleon      | 7.23 ms                                                      | 7.37 ms: 1.02x slower                                              |
| docutils       | 2.87 sec                                                     | 3.00 sec: 1.05x slower                                             |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                        | 1.02x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 434 ms: 1.24x faster                                               |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                               |
| async_tree_none            | 452 ms                                                       | 369 ms: 1.22x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 582 ms: 1.20x faster                                               |
| async_tree_io              | 1.04 sec                                                     | 879 ms: 1.19x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 466 ms: 1.17x faster                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 913 ms: 1.15x faster                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 615 ms: 1.13x faster                                               |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                               |
| nbody          | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                              |
| float          | 76.6 ms                                                      | 80.5 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                        | 1.02x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 143 ms: 1.00x faster                                               |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                               |
| regex_effbot   | 3.57 ms                                                      | 3.74 ms: 1.05x slower                                              |
| regex_v8       | 23.6 ms                                                      | 25.4 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                        | 1.04x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.7 us: 1.03x faster                                              |
| json_loads           | 24.4 us                                                      | 23.8 us: 1.02x faster                                              |
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                               |
| unpickle_list        | 4.66 us                                                      | 4.56 us: 1.02x faster                                              |
| unpickle             | 14.8 us                                                      | 15.0 us: 1.01x slower                                              |
| xml_etree_generate   | 86.1 ms                                                      | 87.4 ms: 1.01x slower                                              |
| pickle_list          | 4.43 us                                                      | 4.59 us: 1.04x slower                                              |
| xml_etree_process    | 58.4 ms                                                      | 60.9 ms: 1.04x slower                                              |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                              |
| unpickle_pure_python | 210 us                                                       | 229 us: 1.09x slower                                               |
| tomli_loads          | 2.16 sec                                                     | 2.42 sec: 1.12x slower                                             |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                       |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                              |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                              |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.3 ms: 1.03x slower                                              |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                              |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                              |
| async_tree_memoization_tg  | 540 ms                                                       | 434 ms: 1.24x faster                                               |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                               |
| async_tree_none            | 452 ms                                                       | 369 ms: 1.22x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 582 ms: 1.20x faster                                               |
| async_tree_io              | 1.04 sec                                                     | 879 ms: 1.19x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 466 ms: 1.17x faster                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 913 ms: 1.15x faster                                               |
| raytrace                   | 298 ms                                                       | 260 ms: 1.15x faster                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 615 ms: 1.13x faster                                               |
| crypto_pyaes               | 80.3 ms                                                      | 72.4 ms: 1.11x faster                                              |
| generators                 | 37.4 ms                                                      | 34.0 ms: 1.10x faster                                              |
| pathlib                    | 18.9 ms                                                      | 17.2 ms: 1.10x faster                                              |
| mypy2                      | 830 ms                                                       | 769 ms: 1.08x faster                                               |
| logging_simple             | 6.71 us                                                      | 6.25 us: 1.07x faster                                              |
| logging_format             | 7.48 us                                                      | 6.97 us: 1.07x faster                                              |
| chaos                      | 64.0 ms                                                      | 60.1 ms: 1.07x faster                                              |
| async_generators           | 390 ms                                                       | 368 ms: 1.06x faster                                               |
| bench_thread_pool          | 950 us                                                       | 897 us: 1.06x faster                                               |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                               |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.2 ms: 1.04x faster                                              |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                              |
| pickle_dict                | 32.5 us                                                      | 31.7 us: 1.03x faster                                              |
| json_loads                 | 24.4 us                                                      | 23.8 us: 1.02x faster                                              |
| pickle_pure_python         | 318 us                                                       | 311 us: 1.02x faster                                               |
| unpickle_list              | 4.66 us                                                      | 4.56 us: 1.02x faster                                              |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                              |
| scimark_lu                 | 98.8 ms                                                      | 96.9 ms: 1.02x faster                                              |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                               |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.02x faster                                               |
| sympy_str                  | 302 ms                                                       | 299 ms: 1.01x faster                                               |
| unpack_sequence            | 53.2 ns                                                      | 52.6 ns: 1.01x faster                                              |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                             |
| regex_compile              | 144 ms                                                       | 143 ms: 1.00x faster                                               |
| dulwich_log                | 65.4 ms                                                      | 65.1 ms: 1.00x faster                                              |
| scimark_fft                | 301 ms                                                       | 302 ms: 1.00x slower                                               |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                               |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                              |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                               |
| dask                       | 392 ms                                                       | 396 ms: 1.01x slower                                               |
| nqueens                    | 89.9 ms                                                      | 91.1 ms: 1.01x slower                                              |
| unpickle                   | 14.8 us                                                      | 15.0 us: 1.01x slower                                              |
| json                       | 5.12 ms                                                      | 5.19 ms: 1.01x slower                                              |
| xml_etree_generate         | 86.1 ms                                                      | 87.4 ms: 1.01x slower                                              |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.01x slower                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.28 ms: 1.02x slower                                              |
| pprint_safe_repr           | 807 ms                                                       | 823 ms: 1.02x slower                                               |
| chameleon                  | 7.23 ms                                                      | 7.37 ms: 1.02x slower                                              |
| deepcopy_reduce            | 3.37 us                                                      | 3.44 us: 1.02x slower                                              |
| 2to3                       | 285 ms                                                       | 291 ms: 1.02x slower                                               |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.03x slower                                              |
| deepcopy_memo              | 36.8 us                                                      | 37.7 us: 1.03x slower                                              |
| logging_silent             | 94.4 ns                                                      | 96.9 ns: 1.03x slower                                              |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.03x slower                                              |
| django_template            | 38.2 ms                                                      | 39.3 ms: 1.03x slower                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                              |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                              |
| deepcopy                   | 368 us                                                       | 381 us: 1.03x slower                                               |
| pickle_list                | 4.43 us                                                      | 4.59 us: 1.04x slower                                              |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                               |
| gunicorn                   | 1.00 ms                                                      | 1.04 ms: 1.04x slower                                              |
| nbody                      | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                              |
| xml_etree_process          | 58.4 ms                                                      | 60.9 ms: 1.04x slower                                              |
| sqlglot_optimize           | 57.5 ms                                                      | 60.1 ms: 1.04x slower                                              |
| deltablue                  | 3.24 ms                                                      | 3.39 ms: 1.05x slower                                              |
| docutils                   | 2.87 sec                                                     | 3.00 sec: 1.05x slower                                             |
| regex_effbot               | 3.57 ms                                                      | 3.74 ms: 1.05x slower                                              |
| float                      | 76.6 ms                                                      | 80.5 ms: 1.05x slower                                              |
| sympy_expand               | 484 ms                                                       | 509 ms: 1.05x slower                                               |
| fannkuch                   | 350 ms                                                       | 369 ms: 1.05x slower                                               |
| sqlglot_normalize          | 116 ms                                                       | 122 ms: 1.06x slower                                               |
| hexiom                     | 5.96 ms                                                      | 6.32 ms: 1.06x slower                                              |
| spectral_norm              | 91.6 ms                                                      | 97.8 ms: 1.07x slower                                              |
| regex_v8                   | 23.6 ms                                                      | 25.4 ms: 1.08x slower                                              |
| aiohttp                    | 1.02 ms                                                      | 1.10 ms: 1.08x slower                                              |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                               |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                              |
| unpickle_pure_python       | 210 us                                                       | 229 us: 1.09x slower                                               |
| pyflate                    | 439 ms                                                       | 481 ms: 1.10x slower                                               |
| go                         | 150 ms                                                       | 165 ms: 1.11x slower                                               |
| tomli_loads                | 2.16 sec                                                     | 2.42 sec: 1.12x slower                                             |
| richards                   | 45.7 ms                                                      | 52.0 ms: 1.14x slower                                              |
| richards_super             | 51.3 ms                                                      | 58.8 ms: 1.14x slower                                              |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                              |
| typing_runtime_protocols   | 152 us                                                       | 177 us: 1.17x slower                                               |
| coverage                   | 66.7 ms                                                      | 80.4 ms: 1.21x slower                                              |
| telco                      | 6.96 ms                                                      | 8.65 ms: 1.24x slower                                              |
| create_gc_cycles           | 1.59 ms                                                      | 2.00 ms: 1.26x slower                                              |
| gc_traversal               | 3.48 ms                                                      | 4.49 ms: 1.29x slower                                              |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (5): bench_mp_pool, xml_etree_iterparse, pycparser, pickle, xml_etree_parse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.004x slower
# HPT report

- Reliability score: 88.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.94x