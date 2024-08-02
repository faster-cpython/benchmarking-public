# Results vs. 3.12.0

- fork: brandtbucher
- ref: peel
- machine: linux-x86_64
- commit hash: ee3b5e3
- commit date: 2024-05-10
- overall geometric mean: 1.00x faster
- HPT reliability: 98.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                        |
| chameleon      | 7.41 ms                                                | 6.97 ms: 1.06x faster                                       |
| tornado_http   | 103 ms                                                 | 97.5 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.30x faster                                        |
| async_tree_none            | 472 ms                                                 | 364 ms: 1.30x faster                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 458 ms: 1.26x faster                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                        |
| async_tree_io              | 1.16 sec                                               | 954 ms: 1.21x faster                                        |
| async_tree_memoization     | 578 ms                                                 | 478 ms: 1.21x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 985 ms: 1.20x faster                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 624 ms: 1.16x faster                                        |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.2 ms: 1.19x faster                                       |
| nbody          | 97.0 ms                                                | 83.9 ms: 1.16x faster                                       |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                        |
| regex_effbot   | 3.61 ms                                                | 3.51 ms: 1.03x faster                                       |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                        |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                      |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                        |
| xml_etree_generate   | 89.2 ms                                                | 83.3 ms: 1.07x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 151 ms: 1.06x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                        |
| unpickle_pure_python | 230 us                                                 | 227 us: 1.01x faster                                        |
| unpickle             | 15.9 us                                                | 15.6 us: 1.01x faster                                       |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.01x faster                                       |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                       |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                       |
| unpickle_list        | 5.29 us                                                | 5.52 us: 1.04x slower                                       |
| pickle_list          | 5.08 us                                                | 5.60 us: 1.10x slower                                       |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.60 ms: 1.10x slower                                       |
| python_startup         | 9.55 ms                                                | 10.9 ms: 1.14x slower                                       |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.59 ms: 1.24x faster                                       |
| django_template | 34.6 ms                                                | 36.3 ms: 1.05x slower                                       |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.30x faster                                        |
| async_tree_none            | 472 ms                                                 | 364 ms: 1.30x faster                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 458 ms: 1.26x faster                                        |
| mako                       | 11.9 ms                                                | 9.59 ms: 1.24x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                        |
| async_tree_io              | 1.16 sec                                               | 954 ms: 1.21x faster                                        |
| async_tree_memoization     | 578 ms                                                 | 478 ms: 1.21x faster                                        |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                      |
| async_tree_io_tg           | 1.18 sec                                               | 985 ms: 1.20x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 68.2 ms: 1.20x faster                                       |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                       |
| float                      | 84.7 ms                                                | 71.2 ms: 1.19x faster                                       |
| spectral_norm              | 115 ms                                                 | 97.1 ms: 1.18x faster                                       |
| fannkuch                   | 417 ms                                                 | 359 ms: 1.16x faster                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 624 ms: 1.16x faster                                        |
| nbody                      | 97.0 ms                                                | 83.9 ms: 1.16x faster                                       |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                        |
| logging_format             | 7.23 us                                                | 6.50 us: 1.11x faster                                       |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                       |
| richards                   | 45.8 ms                                                | 41.5 ms: 1.11x faster                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.58 ms: 1.10x faster                                       |
| logging_simple             | 6.46 us                                                | 5.85 us: 1.10x faster                                       |
| pathlib                    | 19.3 ms                                                | 17.7 ms: 1.09x faster                                       |
| richards_super             | 51.5 ms                                                | 47.7 ms: 1.08x faster                                       |
| deepcopy_memo              | 40.7 us                                                | 37.8 us: 1.08x faster                                       |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                        |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 83.3 ms: 1.07x faster                                       |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                        |
| chameleon                  | 7.41 ms                                                | 6.97 ms: 1.06x faster                                       |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 151 ms: 1.06x faster                                        |
| tornado_http               | 103 ms                                                 | 97.5 ms: 1.05x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                       |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                       |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                       |
| regex_effbot               | 3.61 ms                                                | 3.51 ms: 1.03x faster                                       |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                      |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                       |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                      |
| unpickle_pure_python       | 230 us                                                 | 227 us: 1.01x faster                                        |
| unpickle                   | 15.9 us                                                | 15.6 us: 1.01x faster                                       |
| pickle_dict                | 35.5 us                                                | 35.0 us: 1.01x faster                                       |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                        |
| dulwich_log                | 68.5 ms                                                | 68.8 ms: 1.00x slower                                       |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                        |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                       |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                        |
| async_generators           | 463 ms                                                 | 469 ms: 1.01x slower                                        |
| sympy_str                  | 300 ms                                                 | 305 ms: 1.02x slower                                        |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                       |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                        |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                       |
| dask                       | 372 ms                                                 | 380 ms: 1.02x slower                                        |
| deepcopy                   | 371 us                                                 | 381 us: 1.03x slower                                        |
| gc_traversal               | 3.79 ms                                                | 3.90 ms: 1.03x slower                                       |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                        |
| asyncio_websockets         | 551 ms                                                 | 568 ms: 1.03x slower                                        |
| nqueens                    | 83.3 ms                                                | 85.9 ms: 1.03x slower                                       |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                        |
| scimark_lu                 | 118 ms                                                 | 122 ms: 1.04x slower                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                      |
| unpickle_list              | 5.29 us                                                | 5.52 us: 1.04x slower                                       |
| bench_thread_pool          | 842 us                                                 | 879 us: 1.04x slower                                        |
| sqlglot_optimize           | 54.8 ms                                                | 57.2 ms: 1.04x slower                                       |
| django_template            | 34.6 ms                                                | 36.3 ms: 1.05x slower                                       |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                        |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                        |
| asyncio_tcp                | 491 ms                                                 | 520 ms: 1.06x slower                                        |
| hexiom                     | 6.41 ms                                                | 6.80 ms: 1.06x slower                                       |
| sympy_expand               | 478 ms                                                 | 510 ms: 1.07x slower                                        |
| sympy_integrate            | 21.4 ms                                                | 22.9 ms: 1.07x slower                                       |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                        |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.60 ms: 1.10x slower                                       |
| pickle_list                | 5.08 us                                                | 5.60 us: 1.10x slower                                       |
| python_startup             | 9.55 ms                                                | 10.9 ms: 1.14x slower                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.84 ms: 1.25x slower                                       |
| coverage                   | 72.7 ms                                                | 92.0 ms: 1.26x slower                                       |
| telco                      | 7.10 ms                                                | 172 ms: 24.24x slower                                       |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                |

Benchmark hidden because not significant (7): meteor_contest, deltablue, deepcopy_reduce, coroutines, json, bench_mp_pool, json_dumps
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240510-3.14.0a0-ee3b5e3-JIT/bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.57% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x