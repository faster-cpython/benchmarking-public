# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                   |
| tornado_http   | 103 ms                                                 | 92.2 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 312 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 397 ms: 1.45x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 830 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 867 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                    |
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                    |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.15x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                    |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                    |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.00x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.53 ms: 1.25x faster                                                    |
| django_template | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 312 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 397 ms: 1.45x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 830 ms: 1.43x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                    |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 867 ms: 1.33x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                                     |
| mako                       | 11.9 ms                                                | 9.53 ms: 1.25x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 60.7 ms: 1.24x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                    |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 67.0 ms: 1.22x faster                                                    |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                   |
| nbody                      | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                    |
| logging_format             | 7.23 us                                                | 6.00 us: 1.21x faster                                                    |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.30 ms: 1.18x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                    |
| fannkuch                   | 417 ms                                                 | 359 ms: 1.16x faster                                                     |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                    |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.15x faster                                                     |
| tornado_http               | 103 ms                                                 | 92.2 ms: 1.11x faster                                                    |
| pyflate                    | 482 ms                                                 | 434 ms: 1.11x faster                                                     |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                    |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.10x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                    |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                     |
| richards                   | 45.8 ms                                                | 43.6 ms: 1.05x faster                                                    |
| richards_super             | 51.5 ms                                                | 49.3 ms: 1.05x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                   |
| generators                 | 31.2 ms                                                | 30.1 ms: 1.04x faster                                                    |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                    |
| gc_traversal               | 3.79 ms                                                | 3.68 ms: 1.03x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                   |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                                    |
| dask                       | 372 ms                                                 | 363 ms: 1.02x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 67.1 ms: 1.02x faster                                                    |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                     |
| sympy_str                  | 300 ms                                                 | 295 ms: 1.01x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.00x faster                                                    |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                   |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 499 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                    |
| django_template            | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                    |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.57 ms: 1.03x slower                                                    |
| deltablue                  | 3.72 ms                                                | 3.81 ms: 1.03x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 56.3 ms: 1.03x slower                                                    |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.1 ms: 1.03x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                   |
| sympy_expand               | 478 ms                                                 | 499 ms: 1.04x slower                                                     |
| nqueens                    | 83.3 ms                                                | 87.5 ms: 1.05x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                     |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                    |
| telco                      | 7.10 ms                                                | 7.90 ms: 1.11x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                    |
| coverage                   | 72.7 ms                                                | 93.2 ms: 1.28x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                             |

Benchmark hidden because not significant (2): 2to3, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x