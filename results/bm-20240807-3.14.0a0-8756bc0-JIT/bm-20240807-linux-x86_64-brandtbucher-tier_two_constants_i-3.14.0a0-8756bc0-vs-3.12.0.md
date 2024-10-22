# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_constants_i
- machine: linux-x86_64
- commit hash: 8756bc0
- commit date: 2024-08-07
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 274 ms: 1.00x faster                                                        |
| docutils       | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                      |
| tornado_http   | 103 ms                                                 | 92.6 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 528 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 867 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.0 ms: 1.23x faster                                                       |
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                       |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                        |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 56.3 ms: 1.10x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.71 ms: 1.23x faster                                                       |
| django_template | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.42x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 528 ms: 1.38x faster                                                        |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 867 ms: 1.36x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 66.2 ms: 1.24x faster                                                       |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                        |
| nbody                      | 97.0 ms                                                | 79.0 ms: 1.23x faster                                                       |
| mako                       | 11.9 ms                                                | 9.71 ms: 1.23x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 61.4 ms: 1.22x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                       |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                       |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                       |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                                       |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                                       |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.13x faster                                                        |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                        |
| fannkuch                   | 417 ms                                                 | 371 ms: 1.12x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.54 ms: 1.11x faster                                                       |
| richards                   | 45.8 ms                                                | 41.2 ms: 1.11x faster                                                       |
| tornado_http               | 103 ms                                                 | 92.6 ms: 1.11x faster                                                       |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                        |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 56.3 ms: 1.10x faster                                                       |
| richards_super             | 51.5 ms                                                | 47.2 ms: 1.09x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 108 ms: 1.09x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                        |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 729 ms: 1.06x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.54 ms: 1.05x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.67 ms: 1.03x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 819 us: 1.03x faster                                                        |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                      |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                        |
| async_generators           | 463 ms                                                 | 456 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| 2to3                       | 274 ms                                                 | 274 ms: 1.00x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.01x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                        |
| nqueens                    | 83.3 ms                                                | 83.9 ms: 1.01x slower                                                       |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 499 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                       |
| django_template            | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.66 ms: 1.04x slower                                                       |
| generators                 | 31.2 ms                                                | 32.6 ms: 1.04x slower                                                       |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                       |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                       |
| sympy_expand               | 478 ms                                                 | 510 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                        |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                       |
| coverage                   | 72.7 ms                                                | 92.0 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (3): coroutines, sympy_str, bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240807-3.14.0a0-8756bc0-JIT/bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.05x