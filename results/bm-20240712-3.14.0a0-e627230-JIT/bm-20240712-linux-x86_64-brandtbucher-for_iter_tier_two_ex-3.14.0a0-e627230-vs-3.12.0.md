# Results vs. 3.12.0

- fork: brandtbucher
- ref: for_iter_tier_two_ex
- machine: linux-x86_64
- commit hash: e627230
- commit date: 2024-07-12
- overall geometric mean: 1.08x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                                        |
| docutils       | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                      |
| tornado_http   | 103 ms                                                 | 92.8 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                        |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 848 ms: 1.39x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.7 ms: 1.22x faster                                                       |
| nbody          | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                       |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                                        |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.06x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                        |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.70 ms: 1.23x faster                                                       |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                        |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 28.5 us: 1.43x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 848 ms: 1.39x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                        |
| deepcopy                   | 371 us                                                 | 273 us: 1.36x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 60.5 ms: 1.24x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                       |
| mako                       | 11.9 ms                                                | 9.70 ms: 1.23x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.23x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 66.8 ms: 1.23x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                      |
| float                      | 84.7 ms                                                | 69.7 ms: 1.22x faster                                                       |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                        |
| nbody                      | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                       |
| logging_format             | 7.23 us                                                | 6.05 us: 1.19x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.33 ms: 1.17x faster                                                       |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                        |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                       |
| fannkuch                   | 417 ms                                                 | 365 ms: 1.14x faster                                                        |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                        |
| richards                   | 45.8 ms                                                | 41.2 ms: 1.11x faster                                                       |
| tornado_http               | 103 ms                                                 | 92.8 ms: 1.11x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                       |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                        |
| pyflate                    | 482 ms                                                 | 441 ms: 1.09x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                                       |
| meteor_contest             | 112 ms                                                 | 104 ms: 1.08x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                       |
| richards_super             | 51.5 ms                                                | 48.3 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.56 ms: 1.04x faster                                                       |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                                       |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                       |
| dask                       | 372 ms                                                 | 362 ms: 1.03x faster                                                        |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.71 ms: 1.02x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                                       |
| sympy_str                  | 300 ms                                                 | 294 ms: 1.02x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 830 us: 1.01x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 55.5 ms: 1.01x slower                                                       |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                        |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.50 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                        |
| mdp                        | 2.63 sec                                               | 2.68 sec: 1.02x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                       |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                       |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 22.1 ms: 1.03x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                      |
| sympy_expand               | 478 ms                                                 | 496 ms: 1.04x slower                                                        |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                                       |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                       |
| coverage                   | 72.7 ms                                                | 92.0 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (3): bench_mp_pool, pycparser, scimark_sor
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240712-3.14.0a0-e627230-JIT/bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x