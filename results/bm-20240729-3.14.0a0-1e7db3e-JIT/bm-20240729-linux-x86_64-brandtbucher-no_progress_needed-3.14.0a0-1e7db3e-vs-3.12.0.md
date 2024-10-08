# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 1e7db3e
- commit date: 2024-07-29
- overall geometric mean: 1.06x faster
- HPT reliability: 96.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 289 ms: 1.05x slower                                                      |
| docutils       | 2.77 sec                                               | 3.09 sec: 1.11x slower                                                    |
| tornado_http   | 103 ms                                                 | 94.7 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 394 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.36x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.27x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.1 ms: 1.21x faster                                                     |
| float          | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 151 ms: 1.02x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                     |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 57.9 ms: 1.07x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                      |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.63 ms: 1.24x faster                                                     |
| django_template | 34.6 ms                                                | 38.0 ms: 1.10x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 27.9 us: 1.46x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 394 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                      |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.36x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.27x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                     |
| mako                       | 11.9 ms                                                | 9.63 ms: 1.24x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 67.0 ms: 1.22x faster                                                     |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                      |
| nbody                      | 97.0 ms                                                | 80.1 ms: 1.21x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.21x faster                                                     |
| float                      | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                     |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 63.7 ms: 1.18x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.42 ms: 1.14x faster                                                     |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                      |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                     |
| fannkuch                   | 417 ms                                                 | 375 ms: 1.11x faster                                                      |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                     |
| tornado_http               | 103 ms                                                 | 94.7 ms: 1.08x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                      |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 57.9 ms: 1.07x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                      |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                      |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.03x faster                                                     |
| richards                   | 45.8 ms                                                | 44.7 ms: 1.03x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 757 ms: 1.02x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                     |
| json                       | 5.26 ms                                                | 5.20 ms: 1.01x faster                                                     |
| dask                       | 372 ms                                                 | 368 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 839 us: 1.00x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.62 sec: 1.00x faster                                                    |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.00x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.71 ms: 1.01x slower                                                     |
| regex_compile              | 148 ms                                                 | 151 ms: 1.02x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                    |
| async_generators           | 463 ms                                                 | 473 ms: 1.02x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 507 ms: 1.03x slower                                                      |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                     |
| 2to3                       | 274 ms                                                 | 289 ms: 1.05x slower                                                      |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                      |
| sympy_str                  | 300 ms                                                 | 322 ms: 1.07x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 119 ms: 1.08x slower                                                      |
| go                         | 139 ms                                                 | 152 ms: 1.09x slower                                                      |
| generators                 | 31.2 ms                                                | 34.1 ms: 1.09x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 186 ms: 1.10x slower                                                      |
| django_template            | 34.6 ms                                                | 38.0 ms: 1.10x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 60.4 ms: 1.10x slower                                                     |
| docutils                   | 2.77 sec                                               | 3.09 sec: 1.11x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 132 ms: 1.12x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 176 us: 1.12x slower                                                      |
| telco                      | 7.10 ms                                                | 7.98 ms: 1.12x slower                                                     |
| nqueens                    | 83.3 ms                                                | 94.6 ms: 1.14x slower                                                     |
| sympy_expand               | 478 ms                                                 | 545 ms: 1.14x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 24.8 ms: 1.16x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                     |
| hexiom                     | 6.41 ms                                                | 8.07 ms: 1.26x slower                                                     |
| coverage                   | 72.7 ms                                                | 91.6 ms: 1.26x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (3): pprint_pformat, richards_super, bench_mp_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240729-3.14.0a0-1e7db3e-JIT/bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x