# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.04x faster
- HPT reliability: 99.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                                 |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                               |
| tornado_http   | 103 ms                                                 | 96.9 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 340 ms: 1.32x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                                 |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 482 ms: 1.20x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 972 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 631 ms: 1.15x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.5 ms: 1.18x faster                                                |
| float          | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                               |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 82.2 ms: 1.08x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                 |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                |
| pickle_dict          | 35.5 us                                                | 36.4 us: 1.02x slower                                                |
| unpickle_list        | 5.29 us                                                | 5.44 us: 1.03x slower                                                |
| pickle               | 11.6 us                                                | 12.0 us: 1.03x slower                                                |
| pickle_list          | 5.08 us                                                | 5.39 us: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (2): unpickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                |
| python_startup         | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.83 ms: 1.21x faster                                                |
| django_template | 34.6 ms                                                | 36.5 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 340 ms: 1.32x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                                 |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                               |
| mako                       | 11.9 ms                                                | 9.83 ms: 1.21x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 67.7 ms: 1.21x faster                                                |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 482 ms: 1.20x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                                |
| async_tree_io              | 1.16 sec                                               | 972 ms: 1.19x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                |
| nbody                      | 97.0 ms                                                | 82.5 ms: 1.18x faster                                                |
| float                      | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                |
| fannkuch                   | 417 ms                                                 | 358 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 631 ms: 1.15x faster                                                 |
| logging_format             | 7.23 us                                                | 6.29 us: 1.15x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.41 ms: 1.15x faster                                                |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                 |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                |
| richards                   | 45.8 ms                                                | 41.8 ms: 1.10x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 709 ms: 1.09x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.3 ms: 1.09x faster                                                |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 82.2 ms: 1.08x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 37.8 us: 1.08x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                 |
| tornado_http               | 103 ms                                                 | 96.9 ms: 1.06x faster                                                |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                               |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 3.30 us: 1.01x faster                                                |
| generators                 | 31.2 ms                                                | 30.8 ms: 1.01x faster                                                |
| deepcopy                   | 371 us                                                 | 368 us: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                                 |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                 |
| pickle_dict                | 35.5 us                                                | 36.4 us: 1.02x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.44 us: 1.03x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.63 ms: 1.03x slower                                                |
| nqueens                    | 83.3 ms                                                | 86.2 ms: 1.03x slower                                                |
| pickle                     | 11.6 us                                                | 12.0 us: 1.03x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 56.8 ms: 1.04x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                               |
| bench_thread_pool          | 842 us                                                 | 876 us: 1.04x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                |
| django_template            | 34.6 ms                                                | 36.5 ms: 1.06x slower                                                |
| go                         | 139 ms                                                 | 147 ms: 1.06x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                               |
| asyncio_tcp                | 491 ms                                                 | 519 ms: 1.06x slower                                                 |
| scimark_sor                | 129 ms                                                 | 137 ms: 1.06x slower                                                 |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.39 us: 1.06x slower                                                |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                 |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.06 ms: 1.07x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                |
| telco                      | 7.10 ms                                                | 8.12 ms: 1.14x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.81 ms: 1.22x slower                                                |
| coverage                   | 72.7 ms                                                | 92.8 ms: 1.28x slower                                                |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (8): unpickle, json_dumps, sympy_str, bench_mp_pool, dulwich_log, async_generators, deltablue, dask
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.40% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x