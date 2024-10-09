# Results vs. 3.12.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-x86_64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.06x slower
- HPT reliability: 57.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 317 ms: 1.11x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.22 sec: 1.12x slower                                                      |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 324 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 777 ms: 1.35x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 820 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 84.3 ms: 1.04x faster                                                       |
| float          | 76.6 ms                                                      | 75.7 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 249 ms: 1.04x slower                                                        |
| regex_compile  | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.1 ms: 1.09x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 30.9 us: 1.05x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.24 us: 1.04x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 56.7 ms: 1.03x faster                                                       |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| unpickle_list        | 4.66 us                                                      | 4.60 us: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 324 us: 1.02x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 148 ms: 1.03x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.5 us: 1.05x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (2): json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.5 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.16 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 42.9 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 324 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 777 ms: 1.35x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.4 us: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 820 ms: 1.27x faster                                                        |
| deepcopy                   | 368 us                                                       | 294 us: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.8 us: 1.17x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 70.2 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.14x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 82.6 ms: 1.11x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.16 ms: 1.09x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 79.1 ms: 1.09x faster                                                       |
| scimark_fft                | 301 ms                                                       | 278 ms: 1.08x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 30.9 us: 1.05x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 768 ms: 1.05x faster                                                        |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                        |
| nbody                      | 88.0 ms                                                      | 84.3 ms: 1.04x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.17 us: 1.04x faster                                                       |
| pickle_list                | 4.43 us                                                      | 4.24 us: 1.04x faster                                                       |
| richards                   | 45.7 ms                                                      | 44.3 ms: 1.03x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 56.7 ms: 1.03x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                      |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.53 us: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.72 us: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.13 ms: 1.02x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 64.3 ms: 1.02x faster                                                       |
| async_generators           | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| float                      | 76.6 ms                                                      | 75.7 ms: 1.01x faster                                                       |
| unpickle_list              | 4.66 us                                                      | 4.60 us: 1.01x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.21 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                        |
| fannkuch                   | 350 ms                                                       | 356 ms: 1.02x slower                                                        |
| json                       | 5.12 ms                                                      | 5.22 ms: 1.02x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 324 us: 1.02x slower                                                        |
| go                         | 150 ms                                                       | 154 ms: 1.03x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                                        |
| pyflate                    | 439 ms                                                       | 452 ms: 1.03x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.5 ns: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.03x slower                                                      |
| generators                 | 37.4 ms                                                      | 38.8 ms: 1.04x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.4 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                       |
| regex_dna                  | 239 ms                                                       | 249 ms: 1.04x slower                                                        |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                        |
| raytrace                   | 298 ms                                                       | 312 ms: 1.05x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.5 us: 1.05x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                        |
| sympy_str                  | 302 ms                                                       | 319 ms: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 173 ms: 1.07x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| sympy_expand               | 484 ms                                                       | 529 ms: 1.09x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.65 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.97 ms: 1.11x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.53 ms: 1.11x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 99.7 ms: 1.11x slower                                                       |
| 2to3                       | 285 ms                                                       | 317 ms: 1.11x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.22 sec: 1.12x slower                                                      |
| django_template            | 38.2 ms                                                      | 42.9 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 131 ms: 1.13x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 27.2 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.5 ms: 1.16x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.87 ms: 1.18x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 7.09 ms: 1.19x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 181 us: 1.20x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 69.4 ms: 1.21x slower                                                       |
| coverage                   | 66.7 ms                                                      | 84.0 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.62 ms: 1.33x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 88.0 ns: 1.66x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.57 sec: 330.22x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (9): regex_effbot, scimark_monte_carlo, mdp, scimark_lu, json_loads, richards_super, bench_thread_pool, tornado_http, tomli_loads
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 57.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x