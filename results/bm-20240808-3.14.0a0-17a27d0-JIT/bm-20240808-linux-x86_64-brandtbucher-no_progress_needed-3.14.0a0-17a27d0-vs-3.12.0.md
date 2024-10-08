# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 17a27d0
- commit date: 2024-08-08
- overall geometric mean: 1.09x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 2.98 sec: 1.08x slower                                                    |
| tornado_http   | 103 ms                                                 | 92.3 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 428 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.1 ms: 1.21x faster                                                     |
| float          | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.63 ms: 1.01x slower                                                     |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                      |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 80.3 ms: 1.11x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                      |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.18 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.77 ms: 1.22x faster                                                     |
| django_template | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.7 us: 1.52x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                      |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 428 ms: 1.35x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 66.7 ms: 1.23x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                    |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                      |
| mako                       | 11.9 ms                                                | 9.77 ms: 1.22x faster                                                     |
| nbody                      | 97.0 ms                                                | 80.1 ms: 1.21x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.3 ms: 1.21x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.21x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                     |
| float                      | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                     |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                     |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                      |
| chaos                      | 67.0 ms                                                | 57.1 ms: 1.17x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                     |
| richards                   | 45.8 ms                                                | 39.6 ms: 1.16x faster                                                     |
| fannkuch                   | 417 ms                                                 | 366 ms: 1.14x faster                                                      |
| richards_super             | 51.5 ms                                                | 45.5 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.51 ms: 1.12x faster                                                     |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                      |
| tornado_http               | 103 ms                                                 | 92.3 ms: 1.11x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 80.3 ms: 1.11x faster                                                     |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 107 ms: 1.10x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                     |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                     |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                      |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                                      |
| logging_silent             | 104 ns                                                 | 99.8 ns: 1.05x faster                                                     |
| gc_traversal               | 3.79 ms                                                | 3.65 ms: 1.04x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.3 ms: 1.04x faster                                                     |
| json                       | 5.26 ms                                                | 5.07 ms: 1.04x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 819 us: 1.03x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                    |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                      |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.63 ms: 1.01x slower                                                     |
| nqueens                    | 83.3 ms                                                | 84.0 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                      |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.18 ms: 1.03x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.04x slower                                                     |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                     |
| go                         | 139 ms                                                 | 144 ms: 1.04x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 57.0 ms: 1.04x slower                                                     |
| sympy_expand               | 478 ms                                                 | 501 ms: 1.05x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.74 ms: 1.05x slower                                                     |
| generators                 | 31.2 ms                                                | 32.8 ms: 1.05x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.98 sec: 1.08x slower                                                    |
| telco                      | 7.10 ms                                                | 7.73 ms: 1.09x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                     |
| coverage                   | 72.7 ms                                                | 91.6 ms: 1.26x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (2): 2to3, bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240808-3.14.0a0-17a27d0-JIT/bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x