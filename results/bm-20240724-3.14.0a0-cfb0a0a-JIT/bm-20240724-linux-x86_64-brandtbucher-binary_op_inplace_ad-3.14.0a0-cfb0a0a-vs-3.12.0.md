# Results vs. 3.12.0

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: cfb0a0a
- commit date: 2024-07-24
- overall geometric mean: 1.08x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.00x faster                                                        |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                      |
| tornado_http   | 103 ms                                                 | 95.4 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 871 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.29x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.8 ms: 1.21x faster                                                       |
| float          | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                       |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                       |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                        |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 56.7 ms: 1.09x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                        |
| json_loads           | 28.5 us                                                | 28.1 us: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.21 ms: 1.04x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.80 ms: 1.21x faster                                                       |
| django_template | 34.6 ms                                                | 35.8 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                                        |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 871 ms: 1.36x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.29x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 60.1 ms: 1.25x faster                                                       |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 67.4 ms: 1.22x faster                                                       |
| nbody                      | 97.0 ms                                                | 79.8 ms: 1.21x faster                                                       |
| mako                       | 11.9 ms                                                | 9.80 ms: 1.21x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                      |
| float                      | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.22 ms: 1.20x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                       |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                       |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                        |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                       |
| fannkuch                   | 417 ms                                                 | 365 ms: 1.14x faster                                                        |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                        |
| richards                   | 45.8 ms                                                | 40.8 ms: 1.12x faster                                                       |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                                        |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                        |
| richards_super             | 51.5 ms                                                | 46.7 ms: 1.10x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 56.7 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                        |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                       |
| meteor_contest             | 112 ms                                                 | 104 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                                       |
| tornado_http               | 103 ms                                                 | 95.4 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.05x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.60 ms: 1.03x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.68 ms: 1.03x faster                                                       |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                       |
| async_generators           | 463 ms                                                 | 453 ms: 1.02x faster                                                        |
| dask                       | 372 ms                                                 | 365 ms: 1.02x faster                                                        |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.01x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 831 us: 1.01x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                 | 273 ms: 1.00x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                        |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                                        |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.55 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 56.0 ms: 1.02x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                        |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.03x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.21 ms: 1.04x slower                                                       |
| dulwich_log                | 68.5 ms                                                | 71.2 ms: 1.04x slower                                                       |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                       |
| nqueens                    | 83.3 ms                                                | 87.1 ms: 1.05x slower                                                       |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                        |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                      |
| sympy_expand               | 478 ms                                                 | 506 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 128 ms: 1.09x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                       |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                       |
| coverage                   | 72.7 ms                                                | 92.1 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (4): sympy_str, coroutines, bench_mp_pool, json_dumps
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240724-3.14.0a0-cfb0a0a-JIT/bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x