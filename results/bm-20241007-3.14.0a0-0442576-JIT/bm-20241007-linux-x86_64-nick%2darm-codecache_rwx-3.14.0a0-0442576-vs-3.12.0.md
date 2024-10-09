# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.06x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 274 ms: 1.00x faster                                               |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                             |
| tornado_http   | 103 ms                                                 | 95.4 ms: 1.08x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 880 ms: 1.34x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                               |
| async_tree_io              | 1.16 sec                                               | 889 ms: 1.30x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                               |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.5 ms: 1.22x faster                                              |
| float          | 84.7 ms                                                | 71.3 ms: 1.19x faster                                              |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.14x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                              |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                               |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.13x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 76.5 ms: 1.16x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 54.5 ms: 1.13x faster                                              |
| unpickle             | 15.9 us                                                | 14.2 us: 1.12x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 97.7 ms: 1.09x faster                                              |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                               |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                              |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                               |
| json_dumps           | 10.4 ms                                                | 9.97 ms: 1.04x faster                                              |
| pickle_dict          | 35.5 us                                                | 35.6 us: 1.00x slower                                              |
| unpickle_list        | 5.29 us                                                | 5.33 us: 1.01x slower                                              |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                              |
| pickle_list          | 5.08 us                                                | 5.26 us: 1.03x slower                                              |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                       |

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
| mako            | 11.9 ms                                                | 9.79 ms: 1.22x faster                                              |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                              |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                              |
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                               |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 880 ms: 1.34x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                               |
| async_tree_io              | 1.16 sec                                               | 889 ms: 1.30x faster                                               |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                               |
| scimark_fft                | 382 ms                                                 | 306 ms: 1.25x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 65.8 ms: 1.24x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                              |
| richards                   | 45.8 ms                                                | 37.3 ms: 1.23x faster                                              |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.23x faster                                              |
| nbody                      | 97.0 ms                                                | 79.5 ms: 1.22x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                             |
| mako                       | 11.9 ms                                                | 9.79 ms: 1.22x faster                                              |
| richards_super             | 51.5 ms                                                | 42.7 ms: 1.21x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 62.4 ms: 1.20x faster                                              |
| float                      | 84.7 ms                                                | 71.3 ms: 1.19x faster                                              |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 76.5 ms: 1.16x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                              |
| spectral_norm              | 115 ms                                                 | 99.3 ms: 1.16x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.39 ms: 1.15x faster                                              |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.14x faster                                              |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.14x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 54.5 ms: 1.13x faster                                              |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                               |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                               |
| unpickle                   | 15.9 us                                                | 14.2 us: 1.12x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 702 ms: 1.10x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 97.7 ms: 1.09x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                             |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                               |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                               |
| tornado_http               | 103 ms                                                 | 95.4 ms: 1.08x faster                                              |
| logging_silent             | 104 ns                                                 | 97.5 ns: 1.07x faster                                              |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                              |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                               |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                               |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                               |
| gc_traversal               | 3.79 ms                                                | 3.56 ms: 1.07x faster                                              |
| go                         | 139 ms                                                 | 131 ms: 1.06x faster                                               |
| json                       | 5.26 ms                                                | 5.01 ms: 1.05x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                               |
| json_dumps                 | 10.4 ms                                                | 9.97 ms: 1.04x faster                                              |
| async_generators           | 463 ms                                                 | 449 ms: 1.03x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                              |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                              |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                              |
| dulwich_log                | 68.5 ms                                                | 67.5 ms: 1.01x faster                                              |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                              |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.01x faster                                               |
| 2to3                       | 274 ms                                                 | 274 ms: 1.00x faster                                               |
| pickle_dict                | 35.5 us                                                | 35.6 us: 1.00x slower                                              |
| asyncio_tcp                | 491 ms                                                 | 494 ms: 1.01x slower                                               |
| unpickle_list              | 5.29 us                                                | 5.33 us: 1.01x slower                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                              |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                             |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                              |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                              |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                               |
| nqueens                    | 83.3 ms                                                | 85.9 ms: 1.03x slower                                              |
| sympy_expand               | 478 ms                                                 | 494 ms: 1.03x slower                                               |
| pickle_list                | 5.08 us                                                | 5.26 us: 1.03x slower                                              |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                             |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                               |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                              |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                               |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.82 ms: 1.06x slower                                              |
| telco                      | 7.10 ms                                                | 7.58 ms: 1.07x slower                                              |
| sqlglot_optimize           | 54.8 ms                                                | 58.5 ms: 1.07x slower                                              |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                              |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                              |
| generators                 | 31.2 ms                                                | 34.5 ms: 1.11x slower                                              |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.13x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.16x slower                                              |
| coverage                   | 72.7 ms                                                | 87.7 ms: 1.21x slower                                              |
| unpack_sequence            | 54.0 ns                                                | 108 ns: 2.00x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 60.7 ms: 2.53x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                       |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x