# Results vs. 3.12.0

- fork: brandtbucher
- ref: ujb0_project
- machine: linux-x86_64
- commit hash: 8b9b14d
- commit date: 2024-09-03
- overall geometric mean: 1.03x faster
- HPT reliability: 95.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 296 ms: 1.08x slower                                                |
| docutils       | 2.77 sec                                               | 3.51 sec: 1.27x slower                                              |
| tornado_http   | 103 ms                                                 | 117 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.16x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 317 ms: 1.42x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 413 ms: 1.39x faster                                                |
| async_tree_none            | 472 ms                                                 | 340 ms: 1.39x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 885 ms: 1.34x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                |
| async_tree_io              | 1.16 sec                                               | 953 ms: 1.21x faster                                                |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.1 ms: 1.23x faster                                               |
| nbody          | 97.0 ms                                                | 80.7 ms: 1.20x faster                                               |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.14x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 155 ms: 1.04x slower                                                |
| regex_effbot   | 3.61 ms                                                | 3.87 ms: 1.07x slower                                               |
| regex_dna      | 212 ms                                                 | 230 ms: 1.08x slower                                                |
| regex_v8       | 23.1 ms                                                | 26.4 ms: 1.14x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 197 us: 1.17x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 54.2 ms: 1.14x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 78.4 ms: 1.14x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                               |
| tomli_loads          | 2.33 sec                                               | 2.15 sec: 1.08x faster                                              |
| json_dumps           | 10.4 ms                                                | 9.96 ms: 1.04x faster                                               |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                |
| json_loads           | 28.5 us                                                | 29.6 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                               |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.92 ms: 1.20x faster                                               |
| django_template | 34.6 ms                                                | 39.7 ms: 1.15x slower                                               |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.1 us: 1.56x faster                                               |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 317 ms: 1.42x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 413 ms: 1.39x faster                                                |
| async_tree_none            | 472 ms                                                 | 340 ms: 1.39x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 885 ms: 1.34x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                                |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 58.2 ms: 1.29x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 65.9 ms: 1.24x faster                                               |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                               |
| float                      | 84.7 ms                                                | 69.1 ms: 1.23x faster                                               |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                |
| async_tree_io              | 1.16 sec                                               | 953 ms: 1.21x faster                                                |
| nbody                      | 97.0 ms                                                | 80.7 ms: 1.20x faster                                               |
| mako                       | 11.9 ms                                                | 9.92 ms: 1.20x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.79 us: 1.20x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 197 us: 1.17x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 54.2 ms: 1.14x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 78.4 ms: 1.14x faster                                               |
| fannkuch                   | 417 ms                                                 | 367 ms: 1.14x faster                                                |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.52 ms: 1.12x faster                                               |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                |
| logging_simple             | 6.46 us                                                | 5.95 us: 1.08x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                               |
| tomli_loads                | 2.33 sec                                               | 2.15 sec: 1.08x faster                                              |
| logging_format             | 7.23 us                                                | 6.68 us: 1.08x faster                                               |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.53 ms: 1.05x faster                                               |
| gc_traversal               | 3.79 ms                                                | 3.60 ms: 1.05x faster                                               |
| pyflate                    | 482 ms                                                 | 461 ms: 1.05x faster                                                |
| logging_silent             | 104 ns                                                 | 99.8 ns: 1.05x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 743 ms: 1.04x faster                                                |
| richards                   | 45.8 ms                                                | 43.9 ms: 1.04x faster                                               |
| json_dumps                 | 10.4 ms                                                | 9.96 ms: 1.04x faster                                               |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                              |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                |
| richards_super             | 51.5 ms                                                | 52.5 ms: 1.02x slower                                               |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                               |
| json_loads                 | 28.5 us                                                | 29.6 us: 1.04x slower                                               |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 25.0 ms: 1.04x slower                                               |
| regex_compile              | 148 ms                                                 | 155 ms: 1.04x slower                                                |
| coroutines                 | 23.2 ms                                                | 24.5 ms: 1.06x slower                                               |
| bench_thread_pool          | 842 us                                                 | 894 us: 1.06x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.87 ms: 1.07x slower                                               |
| asyncio_tcp                | 491 ms                                                 | 529 ms: 1.08x slower                                                |
| 2to3                       | 274 ms                                                 | 296 ms: 1.08x slower                                                |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.08x slower                                                |
| generators                 | 31.2 ms                                                | 34.6 ms: 1.11x slower                                               |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                               |
| pycparser                  | 1.18 sec                                               | 1.33 sec: 1.13x slower                                              |
| sqlglot_normalize          | 110 ms                                                 | 125 ms: 1.14x slower                                                |
| regex_v8                   | 23.1 ms                                                | 26.4 ms: 1.14x slower                                               |
| tornado_http               | 103 ms                                                 | 117 ms: 1.14x slower                                                |
| telco                      | 7.10 ms                                                | 8.13 ms: 1.15x slower                                               |
| django_template            | 34.6 ms                                                | 39.7 ms: 1.15x slower                                               |
| sympy_str                  | 300 ms                                                 | 344 ms: 1.15x slower                                                |
| hexiom                     | 6.41 ms                                                | 7.42 ms: 1.16x slower                                               |
| sympy_expand               | 478 ms                                                 | 559 ms: 1.17x slower                                                |
| coverage                   | 72.7 ms                                                | 86.6 ms: 1.19x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.22x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 67.1 ms: 1.22x slower                                               |
| sqlglot_parse              | 1.36 ms                                                | 1.72 ms: 1.27x slower                                               |
| docutils                   | 2.77 sec                                               | 3.51 sec: 1.27x slower                                              |
| sympy_integrate            | 21.4 ms                                                | 27.4 ms: 1.28x slower                                               |
| sympy_sum                  | 169 ms                                                 | 217 ms: 1.28x slower                                                |
| go                         | 139 ms                                                 | 179 ms: 1.29x slower                                                |
| sqlglot_transpile          | 1.68 ms                                                | 2.17 ms: 1.29x slower                                               |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (2): json, nqueens
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240903-3.14.0a0-8b9b14d-JIT/bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.18x