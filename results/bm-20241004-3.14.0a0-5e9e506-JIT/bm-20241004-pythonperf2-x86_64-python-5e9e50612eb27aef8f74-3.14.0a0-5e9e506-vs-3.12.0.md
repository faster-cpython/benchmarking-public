# Results vs. 3.12.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-x86_64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.08x slower
- HPT reliability: 77.02%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 318 ms: 1.12x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.27 sec: 1.14x slower                                                      |
| tornado_http   | 121 ms                                                       | 124 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 326 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 312 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 417 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 833 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 559 ms: 1.25x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 842 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 566 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.0 ms: 1.09x faster                                                       |
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 77.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| regex_compile  | 144 ms                                                       | 149 ms: 1.03x slower                                                        |
| regex_dna      | 239 ms                                                       | 253 ms: 1.06x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.8 ms: 1.08x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 30.7 us: 1.06x faster                                                       |
| json_loads           | 24.4 us                                                      | 23.5 us: 1.04x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.31 us: 1.03x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 57.1 ms: 1.02x faster                                                       |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                      |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 219 us: 1.05x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 334 us: 1.05x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.7 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.1 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.20 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 44.9 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 326 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 312 ms: 1.38x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.3 us: 1.35x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 417 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 833 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 559 ms: 1.25x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 842 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 566 ms: 1.23x faster                                                        |
| deepcopy                   | 368 us                                                       | 300 us: 1.23x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                       |
| comprehensions             | 21.9 us                                                      | 19.3 us: 1.14x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 71.2 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.00 us: 1.12x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.20 ms: 1.09x faster                                                       |
| nbody                      | 88.0 ms                                                      | 81.0 ms: 1.09x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 79.8 ms: 1.08x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                       |
| scimark_fft                | 301 ms                                                       | 283 ms: 1.07x faster                                                        |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.06x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 30.7 us: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| json_loads                 | 24.4 us                                                      | 23.5 us: 1.04x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 91.1 ns: 1.04x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 780 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                      |
| pickle_list                | 4.43 us                                                      | 4.31 us: 1.03x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 57.1 ms: 1.02x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.72 us: 1.02x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 97.2 ms: 1.02x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.15 ms: 1.01x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 90.6 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.76 us: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                      |
| json                       | 5.12 ms                                                      | 5.16 ms: 1.01x slower                                                       |
| float                      | 76.6 ms                                                      | 77.5 ms: 1.01x slower                                                       |
| richards                   | 45.7 ms                                                      | 46.5 ms: 1.02x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 969 us: 1.02x slower                                                        |
| tornado_http               | 121 ms                                                       | 124 ms: 1.02x slower                                                        |
| richards_super             | 51.3 ms                                                      | 52.5 ms: 1.02x slower                                                       |
| go                         | 150 ms                                                       | 153 ms: 1.02x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.0 ms: 1.02x slower                                                       |
| pyflate                    | 439 ms                                                       | 450 ms: 1.03x slower                                                        |
| chaos                      | 64.0 ms                                                      | 65.7 ms: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| regex_compile              | 144 ms                                                       | 149 ms: 1.03x slower                                                        |
| generators                 | 37.4 ms                                                      | 38.8 ms: 1.04x slower                                                       |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                        |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 219 us: 1.05x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 334 us: 1.05x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.7 us: 1.06x slower                                                       |
| regex_dna                  | 239 ms                                                       | 253 ms: 1.06x slower                                                        |
| sympy_str                  | 302 ms                                                       | 326 ms: 1.08x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.63 ms: 1.10x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 179 ms: 1.10x slower                                                        |
| sympy_expand               | 484 ms                                                       | 536 ms: 1.11x slower                                                        |
| raytrace                   | 298 ms                                                       | 331 ms: 1.11x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                                       |
| 2to3                       | 285 ms                                                       | 318 ms: 1.12x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.13x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.27 sec: 1.14x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 134 ms: 1.16x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 27.8 ms: 1.16x slower                                                       |
| django_template            | 38.2 ms                                                      | 44.9 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 179 us: 1.18x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 7.12 ms: 1.19x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 70.2 ms: 1.22x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.1 ms: 1.30x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 5.43 ms: 1.56x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 87.5 ns: 1.65x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.80 ms: 1.76x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 2.25 sec: 472.83x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (5): logging_format, asyncio_tcp, deltablue, unpickle_list, scimark_monte_carlo
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 77.02% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x