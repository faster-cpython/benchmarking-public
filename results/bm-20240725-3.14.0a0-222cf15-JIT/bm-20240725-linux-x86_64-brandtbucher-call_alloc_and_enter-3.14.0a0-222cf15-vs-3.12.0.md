# Results vs. 3.12.0

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: 222cf15
- commit date: 2024-07-25
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.01x faster                                                        |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                      |
| tornado_http   | 103 ms                                                 | 92.7 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 535 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                       |
| nbody          | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                       |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.03x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                       |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 80.1 ms: 1.11x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 56.3 ms: 1.10x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                        |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.79 ms: 1.22x faster                                                       |
| django_template | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 28.7 us: 1.42x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                                        |
| deepcopy                   | 371 us                                                 | 272 us: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 535 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.32x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                                        |
| scimark_fft                | 382 ms                                                 | 305 ms: 1.25x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 59.9 ms: 1.25x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 66.7 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.14 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                       |
| mako                       | 11.9 ms                                                | 9.79 ms: 1.22x faster                                                       |
| float                      | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                      |
| nbody                      | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                       |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                       |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                       |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.15x faster                                                       |
| richards                   | 45.8 ms                                                | 40.2 ms: 1.14x faster                                                       |
| fannkuch                   | 417 ms                                                 | 366 ms: 1.14x faster                                                        |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 80.1 ms: 1.11x faster                                                       |
| tornado_http               | 103 ms                                                 | 92.7 ms: 1.11x faster                                                       |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                                        |
| richards_super             | 51.5 ms                                                | 46.7 ms: 1.10x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 56.3 ms: 1.10x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 721 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.57 ms: 1.04x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.64 ms: 1.04x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                       |
| dask                       | 372 ms                                                 | 365 ms: 1.02x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 827 us: 1.02x faster                                                        |
| json                       | 5.26 ms                                                | 5.18 ms: 1.02x faster                                                       |
| sympy_str                  | 300 ms                                                 | 295 ms: 1.02x faster                                                        |
| 2to3                       | 274 ms                                                 | 270 ms: 1.01x faster                                                        |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                        |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                        |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 55.8 ms: 1.02x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.03x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 503 ms: 1.03x slower                                                        |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                        |
| nqueens                    | 83.3 ms                                                | 85.7 ms: 1.03x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                       |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 25.0 ms: 1.04x slower                                                       |
| sympy_expand               | 478 ms                                                 | 498 ms: 1.04x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.04x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                      |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| telco                      | 7.10 ms                                                | 7.95 ms: 1.12x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                       |
| coverage                   | 72.7 ms                                                | 92.2 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (2): sympy_sum, json_dumps
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240725-3.14.0a0-222cf15-JIT/bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.05x