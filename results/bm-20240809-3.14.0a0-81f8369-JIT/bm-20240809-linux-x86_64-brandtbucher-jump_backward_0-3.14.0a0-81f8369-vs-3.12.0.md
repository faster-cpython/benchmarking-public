# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 81f8369
- commit date: 2024-08-09
- overall geometric mean: 1.06x faster
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 283 ms: 1.03x slower                                                   |
| docutils       | 2.77 sec                                               | 3.08 sec: 1.11x slower                                                 |
| tornado_http   | 103 ms                                                 | 107 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                   |
| async_tree_none            | 472 ms                                                 | 333 ms: 1.42x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 881 ms: 1.34x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 434 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 921 ms: 1.26x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                  |
| nbody          | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.08x faster                                                   |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 80.0 ms: 1.11x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 293 us: 1.10x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.2 ms: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                   |
| json_loads           | 28.5 us                                                | 27.2 us: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.84 ms: 1.21x faster                                                  |
| django_template | 34.6 ms                                                | 39.3 ms: 1.14x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                   |
| async_tree_none            | 472 ms                                                 | 333 ms: 1.42x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                  |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 881 ms: 1.34x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 434 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 59.8 ms: 1.26x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 921 ms: 1.26x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 66.6 ms: 1.23x faster                                                  |
| float                      | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                  |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                   |
| nbody                      | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                  |
| mako                       | 11.9 ms                                                | 9.84 ms: 1.21x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.80 us: 1.19x faster                                                  |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.30 ms: 1.18x faster                                                  |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                                  |
| scimark_sor                | 129 ms                                                 | 113 ms: 1.14x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                  |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                   |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                                   |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 80.0 ms: 1.11x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 293 us: 1.10x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.10x faster                                                   |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.2 ms: 1.08x faster                                                  |
| regex_compile              | 148 ms                                                 | 138 ms: 1.08x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.06x faster                                                   |
| logging_silent             | 104 ns                                                 | 98.3 ns: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                   |
| json_loads                 | 28.5 us                                                | 27.2 us: 1.05x faster                                                  |
| json                       | 5.26 ms                                                | 5.03 ms: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.71 ms: 1.02x faster                                                  |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.37 ms: 1.01x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                 |
| nqueens                    | 83.3 ms                                                | 85.4 ms: 1.03x slower                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.73 ms: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                  |
| 2to3                       | 274 ms                                                 | 283 ms: 1.03x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                   |
| tornado_http               | 103 ms                                                 | 107 ms: 1.05x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 58.1 ms: 1.06x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.83 ms: 1.07x slower                                                  |
| sympy_str                  | 300 ms                                                 | 320 ms: 1.07x slower                                                   |
| go                         | 139 ms                                                 | 150 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 530 ms: 1.08x slower                                                   |
| coroutines                 | 23.2 ms                                                | 25.2 ms: 1.09x slower                                                  |
| telco                      | 7.10 ms                                                | 7.75 ms: 1.09x slower                                                  |
| sympy_expand               | 478 ms                                                 | 530 ms: 1.11x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                  |
| docutils                   | 2.77 sec                                               | 3.08 sec: 1.11x slower                                                 |
| generators                 | 31.2 ms                                                | 35.1 ms: 1.12x slower                                                  |
| django_template            | 34.6 ms                                                | 39.3 ms: 1.14x slower                                                  |
| deltablue                  | 3.72 ms                                                | 4.24 ms: 1.14x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 197 ms: 1.16x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 25.0 ms: 1.17x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                  |
| coverage                   | 72.7 ms                                                | 92.7 ms: 1.28x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (6): regex_effbot, regex_dna, json_dumps, bench_mp_pool, richards, richards_super
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240809-3.14.0a0-81f8369-JIT/bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.32% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x