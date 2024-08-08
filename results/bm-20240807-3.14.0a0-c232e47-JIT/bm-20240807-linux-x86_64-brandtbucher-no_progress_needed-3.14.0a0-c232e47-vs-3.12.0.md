# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: c232e47
- commit date: 2024-08-07
- overall geometric mean: 1.03x faster
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                                      |
| docutils       | 2.77 sec                                               | 6.89 sec: 2.49x slower                                                    |
| tornado_http   | 103 ms                                                 | 93.1 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                  | 1.32x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 398 ms: 1.44x faster                                                      |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 880 ms: 1.34x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 432 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.26x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.4 ms: 1.22x faster                                                     |
| float          | 84.7 ms                                                | 71.0 ms: 1.19x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                      |
| regex_dna      | 212 ms                                                 | 224 ms: 1.05x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 99.6 ms: 1.07x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.03x faster                                                      |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.71 ms: 1.23x faster                                                     |
| django_template | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.5 us: 1.48x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 398 ms: 1.44x faster                                                      |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                      |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 880 ms: 1.34x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 432 ms: 1.34x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.26x faster                                                      |
| scimark_fft                | 382 ms                                                 | 304 ms: 1.25x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 66.1 ms: 1.24x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                    |
| mako                       | 11.9 ms                                                | 9.71 ms: 1.23x faster                                                     |
| nbody                      | 97.0 ms                                                | 79.4 ms: 1.22x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.15 ms: 1.22x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.21x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                     |
| logging_format             | 7.23 us                                                | 6.01 us: 1.20x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                                     |
| float                      | 84.7 ms                                                | 71.0 ms: 1.19x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                     |
| richards                   | 45.8 ms                                                | 39.7 ms: 1.16x faster                                                     |
| spectral_norm              | 115 ms                                                 | 99.5 ms: 1.15x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                                     |
| richards_super             | 51.5 ms                                                | 45.4 ms: 1.14x faster                                                     |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                                      |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.12x faster                                                      |
| tornado_http               | 103 ms                                                 | 93.1 ms: 1.10x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 107 ms: 1.10x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                      |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                      |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 99.6 ms: 1.07x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                     |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 733 ms: 1.06x faster                                                      |
| logging_silent             | 104 ns                                                 | 99.8 ns: 1.05x faster                                                     |
| json                       | 5.26 ms                                                | 5.08 ms: 1.03x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 817 us: 1.03x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.03x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                     |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                    |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.01x faster                                                     |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                     |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                      |
| django_template            | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 502 ms: 1.02x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.02x slower                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.73 ms: 1.03x slower                                                     |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                     |
| go                         | 139 ms                                                 | 144 ms: 1.04x slower                                                      |
| nqueens                    | 83.3 ms                                                | 86.3 ms: 1.04x slower                                                     |
| sympy_expand               | 478 ms                                                 | 496 ms: 1.04x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.71 ms: 1.05x slower                                                     |
| generators                 | 31.2 ms                                                | 32.8 ms: 1.05x slower                                                     |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.05x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                      |
| telco                      | 7.10 ms                                                | 7.83 ms: 1.10x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 60.6 ms: 1.11x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                     |
| coverage                   | 72.7 ms                                                | 91.4 ms: 1.26x slower                                                     |
| pycparser                  | 1.18 sec                                               | 1.64 sec: 1.39x slower                                                    |
| docutils                   | 2.77 sec                                               | 6.89 sec: 2.49x slower                                                    |
| raytrace                   | 312 ms                                                 | 5.00 sec: 16.03x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240807-3.14.0a0-c232e47-JIT/bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.45% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x