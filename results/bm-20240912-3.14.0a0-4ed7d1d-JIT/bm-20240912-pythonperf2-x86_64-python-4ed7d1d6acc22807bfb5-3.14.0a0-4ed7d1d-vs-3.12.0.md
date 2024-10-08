# Results vs. 3.12.0

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.01x faster
- HPT reliability: 59.23%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 309 ms: 1.08x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.15 sec: 1.10x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 311 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 393 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 812 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 828 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.8 ms: 1.08x faster                                                       |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 74.6 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 233 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                       |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 29.5 us: 1.10x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 80.1 ms: 1.08x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.18 us: 1.06x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.9 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 98.9 ms: 1.04x faster                                                       |
| json_loads           | 24.4 us                                                      | 23.9 us: 1.02x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.13 sec: 1.02x faster                                                      |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| unpickle_list        | 4.66 us                                                      | 4.72 us: 1.01x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.23 ms: 1.08x faster                                                       |
| django_template | 38.2 ms                                                      | 42.8 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 311 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 393 ms: 1.38x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.1 us: 1.36x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 812 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 289 us: 1.28x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 828 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.2 us: 1.20x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 69.3 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.16x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 81.6 ms: 1.12x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 29.5 us: 1.10x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.23 ms: 1.08x faster                                                       |
| nbody                      | 88.0 ms                                                      | 81.8 ms: 1.08x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.1 ms: 1.08x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| pickle_list                | 4.43 us                                                      | 4.18 us: 1.06x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.15 us: 1.05x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 55.9 ms: 1.05x faster                                                       |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 98.9 ms: 1.04x faster                                                       |
| scimark_fft                | 301 ms                                                       | 290 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.69 us: 1.03x faster                                                       |
| float                      | 76.6 ms                                                      | 74.6 ms: 1.03x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 924 us: 1.03x faster                                                        |
| richards                   | 45.7 ms                                                      | 44.5 ms: 1.03x faster                                                       |
| regex_dna                  | 239 ms                                                       | 233 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.10 ms: 1.03x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                       |
| json_loads                 | 24.4 us                                                      | 23.9 us: 1.02x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.13 sec: 1.02x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 796 ms: 1.01x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.62 us: 1.01x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 64.6 ms: 1.01x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.21 ms: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| go                         | 150 ms                                                       | 149 ms: 1.00x faster                                                        |
| async_generators           | 390 ms                                                       | 393 ms: 1.01x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                      |
| unpickle_list              | 4.66 us                                                      | 4.72 us: 1.01x slower                                                       |
| richards_super             | 51.3 ms                                                      | 52.1 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 395 ms: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                        |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| pyflate                    | 439 ms                                                       | 449 ms: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                        |
| chaos                      | 64.0 ms                                                      | 65.7 ms: 1.03x slower                                                       |
| sympy_str                  | 302 ms                                                       | 313 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| raytrace                   | 298 ms                                                       | 310 ms: 1.04x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 169 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                                       |
| 2to3                       | 285 ms                                                       | 309 ms: 1.08x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.15 sec: 1.10x slower                                                      |
| bench_mp_pool              | 4.76 ms                                                      | 5.25 ms: 1.10x slower                                                       |
| sympy_expand               | 484 ms                                                       | 533 ms: 1.10x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 99.1 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 129 ms: 1.11x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 26.6 ms: 1.11x slower                                                       |
| django_template            | 38.2 ms                                                      | 42.8 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 65.7 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.98 ms: 1.17x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.28 ms: 1.19x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 181 us: 1.19x slower                                                        |
| coverage                   | 66.7 ms                                                      | 81.3 ms: 1.22x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.94 ms: 1.22x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.87 ms: 1.40x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 89.4 ns: 1.68x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (8): asyncio_tcp, scimark_monte_carlo, mdp, pprint_pformat, json, scimark_lu, generators, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-4ed7d1d-JIT/bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 59.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x