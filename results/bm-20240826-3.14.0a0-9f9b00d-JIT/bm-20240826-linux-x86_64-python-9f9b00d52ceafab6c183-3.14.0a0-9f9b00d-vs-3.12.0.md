# Results vs. 3.12.0

- fork: python
- ref: 9f9b00d52ceafab6c183
- machine: linux-x86_64
- commit hash: 9f9b00d
- commit date: 2024-08-26
- overall geometric mean: 1.08x faster
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                                  |
| docutils       | 2.77 sec                                               | 3.06 sec: 1.10x slower                                                |
| tornado_http   | 103 ms                                                 | 94.7 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 400 ms: 1.45x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 891 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                 |
| nbody          | 97.0 ms                                                | 82.7 ms: 1.17x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                 |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 77.4 ms: 1.15x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.08x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.87 ms: 1.20x faster                                                 |
| django_template | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.9 us: 1.52x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 400 ms: 1.45x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                  |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 891 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                 |
| scimark_fft                | 382 ms                                                 | 305 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 65.9 ms: 1.24x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.16 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                |
| float                      | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                 |
| mako                       | 11.9 ms                                                | 9.87 ms: 1.20x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                                 |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                 |
| nbody                      | 97.0 ms                                                | 82.7 ms: 1.17x faster                                                 |
| richards                   | 45.8 ms                                                | 39.3 ms: 1.17x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 77.4 ms: 1.15x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                 |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| richards_super             | 51.5 ms                                                | 45.5 ms: 1.13x faster                                                 |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                  |
| fannkuch                   | 417 ms                                                 | 370 ms: 1.13x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                 |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                  |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.08x faster                                                 |
| tornado_http               | 103 ms                                                 | 94.7 ms: 1.08x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                  |
| meteor_contest             | 112 ms                                                 | 104 ms: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                  |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 822 us: 1.02x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.01x faster                                                 |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 493 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.87 ms: 1.02x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                 |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                  |
| django_template            | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                 |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                 |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 58.3 ms: 1.06x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.85 ms: 1.07x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.9 ms: 1.07x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| docutils                   | 2.77 sec                                               | 3.06 sec: 1.10x slower                                                |
| telco                      | 7.10 ms                                                | 8.01 ms: 1.13x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                 |
| go                         | 139 ms                                                 | 171 ms: 1.23x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (4): coroutines, bench_mp_pool, sympy_str, json_loads
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240826-3.14.0a0-9f9b00d-JIT/bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.63% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x