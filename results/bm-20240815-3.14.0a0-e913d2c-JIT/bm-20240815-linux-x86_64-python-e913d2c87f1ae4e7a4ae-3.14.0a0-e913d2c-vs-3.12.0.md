# Results vs. 3.12.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.08x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                  |
| docutils       | 2.77 sec                                               | 3.01 sec: 1.09x slower                                                |
| tornado_http   | 103 ms                                                 | 93.4 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 535 ms: 1.36x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 905 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                 |
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                 |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                 |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 81.6 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.08x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 57.5 ms: 1.07x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                  |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                 |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.00x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.98 ms: 1.19x faster                                                 |
| django_template | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                  |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 535 ms: 1.36x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.32x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 905 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                 |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 66.4 ms: 1.23x faster                                                 |
| nbody                      | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                |
| logging_format             | 7.23 us                                                | 6.00 us: 1.21x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                 |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.11 ms: 1.19x faster                                                 |
| mako                       | 11.9 ms                                                | 9.98 ms: 1.19x faster                                                 |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 63.6 ms: 1.18x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.31 ms: 1.17x faster                                                 |
| richards                   | 45.8 ms                                                | 39.4 ms: 1.16x faster                                                 |
| richards_super             | 51.5 ms                                                | 44.7 ms: 1.15x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                 |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                  |
| fannkuch                   | 417 ms                                                 | 369 ms: 1.13x faster                                                  |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                  |
| tornado_http               | 103 ms                                                 | 93.4 ms: 1.10x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 81.6 ms: 1.09x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.08x faster                                                 |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 57.5 ms: 1.07x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 743 ms: 1.04x faster                                                  |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                |
| gc_traversal               | 3.79 ms                                                | 3.67 ms: 1.03x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                 |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 817 us: 1.03x faster                                                  |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.00x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 499 ms: 1.02x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                  |
| nqueens                    | 83.3 ms                                                | 85.2 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 175 ms: 1.04x slower                                                  |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                 |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                  |
| generators                 | 31.2 ms                                                | 32.6 ms: 1.04x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 57.8 ms: 1.05x slower                                                 |
| sympy_expand               | 478 ms                                                 | 506 ms: 1.06x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.81 ms: 1.06x slower                                                 |
| django_template            | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.9 ms: 1.07x slower                                                 |
| docutils                   | 2.77 sec                                               | 3.01 sec: 1.09x slower                                                |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                 |
| coverage                   | 72.7 ms                                                | 87.5 ms: 1.20x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (3): sqlglot_transpile, bench_mp_pool, sympy_str
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x