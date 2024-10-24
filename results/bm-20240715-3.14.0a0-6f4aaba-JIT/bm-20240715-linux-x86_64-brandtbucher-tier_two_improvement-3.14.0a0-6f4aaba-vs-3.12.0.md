# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 6f4aaba
- commit date: 2024-07-15
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                                        |
| docutils       | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                      |
| tornado_http   | 103 ms                                                 | 93.5 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.49x faster                                                        |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 849 ms: 1.39x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 545 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                       |
| nbody          | 97.0 ms                                                | 81.2 ms: 1.19x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.05x slower                                                       |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                        |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                      |
| xml_etree_generate  | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                       |
| pickle_pure_python  | 324 us                                                 | 298 us: 1.09x faster                                                        |
| xml_etree_process   | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                       |
| xml_etree_parse     | 159 ms                                                 | 147 ms: 1.08x faster                                                        |
| xml_etree_iterparse | 107 ms                                                 | 98.9 ms: 1.08x faster                                                       |
| json_loads          | 28.5 us                                                | 27.9 us: 1.02x faster                                                       |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| Geometric mean      | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.74 ms: 1.22x faster                                                       |
| django_template | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.49x faster                                                        |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.41x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 849 ms: 1.39x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                        |
| deepcopy                   | 371 us                                                 | 274 us: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 545 ms: 1.33x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                        |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 61.3 ms: 1.22x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 67.0 ms: 1.22x faster                                                       |
| mako                       | 11.9 ms                                                | 9.74 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                       |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                       |
| nbody                      | 97.0 ms                                                | 81.2 ms: 1.19x faster                                                       |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                       |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                        |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.44 ms: 1.14x faster                                                       |
| fannkuch                   | 417 ms                                                 | 367 ms: 1.14x faster                                                        |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 694 ms: 1.12x faster                                                        |
| pyflate                    | 482 ms                                                 | 433 ms: 1.12x faster                                                        |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.11x faster                                                       |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                       |
| tornado_http               | 103 ms                                                 | 93.5 ms: 1.10x faster                                                       |
| richards_super             | 51.5 ms                                                | 47.3 ms: 1.09x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 298 us: 1.09x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.58 ms: 1.06x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                       |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.2 ms: 1.04x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                       |
| dask                       | 372 ms                                                 | 364 ms: 1.02x faster                                                        |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.65 ms: 1.02x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.5 ms: 1.01x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 834 us: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                                        |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 56.0 ms: 1.02x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.59 ms: 1.03x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                       |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                        |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 509 ms: 1.04x slower                                                        |
| nqueens                    | 83.3 ms                                                | 86.5 ms: 1.04x slower                                                       |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                      |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                        |
| sympy_expand               | 478 ms                                                 | 503 ms: 1.05x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.05x slower                                                       |
| scimark_lu                 | 118 ms                                                 | 127 ms: 1.08x slower                                                        |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| telco                      | 7.10 ms                                                | 7.96 ms: 1.12x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                       |
| coverage                   | 72.7 ms                                                | 94.5 ms: 1.30x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (5): unpickle_pure_python, json, pycparser, sympy_sum, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240715-3.14.0a0-6f4aaba-JIT/bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x