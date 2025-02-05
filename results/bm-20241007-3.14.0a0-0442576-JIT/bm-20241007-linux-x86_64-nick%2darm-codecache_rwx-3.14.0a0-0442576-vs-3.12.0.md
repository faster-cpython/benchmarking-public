# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.094x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 274 ms: 1.00x faster                                               |
| docutils       | 2.77 sec                                               | 2.89 sec: 1.04x slower                                             |
| tornado_http   | 103 ms                                                 | 94.6 ms: 1.08x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 319 ms: 1.48x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                               |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                               |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.3 ms: 1.19x faster                                              |
| nbody          | 97.0 ms                                                | 82.0 ms: 1.18x faster                                              |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.63 ms: 1.01x slower                                              |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 77.8 ms: 1.15x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 54.6 ms: 1.13x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                               |
| unpickle             | 15.9 us                                                | 14.5 us: 1.09x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                              |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                               |
| json_loads           | 28.5 us                                                | 26.8 us: 1.07x faster                                              |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.06x faster                                               |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                              |
| json_dumps           | 10.4 ms                                                | 9.98 ms: 1.04x faster                                              |
| pickle_list          | 5.08 us                                                | 4.96 us: 1.03x faster                                              |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                              |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                       |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                              |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                              |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.83 ms: 1.21x faster                                              |
| django_template | 34.6 ms                                                | 35.1 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.5 us: 1.54x faster                                              |
| async_tree_none            | 472 ms                                                 | 319 ms: 1.48x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                               |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                               |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                               |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                              |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 66.6 ms: 1.23x faster                                              |
| richards                   | 45.8 ms                                                | 37.6 ms: 1.22x faster                                              |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                              |
| mako                       | 11.9 ms                                                | 9.83 ms: 1.21x faster                                              |
| richards_super             | 51.5 ms                                                | 42.6 ms: 1.21x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 62.7 ms: 1.20x faster                                              |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                              |
| float                      | 84.7 ms                                                | 71.3 ms: 1.19x faster                                              |
| nbody                      | 97.0 ms                                                | 82.0 ms: 1.18x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.32 ms: 1.17x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                              |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 77.8 ms: 1.15x faster                                              |
| chaos                      | 67.0 ms                                                | 59.1 ms: 1.13x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 54.6 ms: 1.13x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 686 ms: 1.13x faster                                               |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                               |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                               |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                               |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                               |
| unpickle                   | 15.9 us                                                | 14.5 us: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                              |
| tornado_http               | 103 ms                                                 | 94.6 ms: 1.08x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                             |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                               |
| logging_silent             | 104 ns                                                 | 97.7 ns: 1.07x faster                                              |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                               |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.07x faster                                               |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                               |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.07x faster                                              |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.06x faster                                               |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                               |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                               |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                              |
| json_dumps                 | 10.4 ms                                                | 9.98 ms: 1.04x faster                                              |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.04x faster                                              |
| pickle_list                | 5.08 us                                                | 4.96 us: 1.03x faster                                              |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                              |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                              |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                               |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                              |
| 2to3                       | 274 ms                                                 | 274 ms: 1.00x faster                                               |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                              |
| regex_effbot               | 3.61 ms                                                | 3.63 ms: 1.01x slower                                              |
| asyncio_tcp                | 491 ms                                                 | 494 ms: 1.01x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                               |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                             |
| django_template            | 34.6 ms                                                | 35.1 ms: 1.02x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                              |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| gc_traversal               | 3.79 ms                                                | 3.88 ms: 1.02x slower                                              |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.03x slower                                               |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                               |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.03x slower                                             |
| sympy_expand               | 478 ms                                                 | 495 ms: 1.03x slower                                               |
| docutils                   | 2.77 sec                                               | 2.89 sec: 1.04x slower                                             |
| nqueens                    | 83.3 ms                                                | 87.1 ms: 1.05x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.79 ms: 1.06x slower                                              |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                               |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                              |
| telco                      | 7.10 ms                                                | 7.58 ms: 1.07x slower                                              |
| sqlglot_optimize           | 54.8 ms                                                | 58.7 ms: 1.07x slower                                              |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                              |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                              |
| generators                 | 31.2 ms                                                | 34.6 ms: 1.11x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                              |
| coverage                   | 72.7 ms                                                | 86.0 ms: 1.18x slower                                              |
| unpack_sequence            | 54.0 ns                                                | 106 ns: 1.96x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 60.3 ms: 2.51x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (2): async_generators, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.094x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x