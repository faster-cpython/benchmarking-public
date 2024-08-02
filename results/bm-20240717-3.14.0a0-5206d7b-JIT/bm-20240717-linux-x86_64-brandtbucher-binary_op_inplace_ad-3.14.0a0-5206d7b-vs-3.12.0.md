# Results vs. 3.12.0

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: 5206d7b
- commit date: 2024-07-17
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.01x faster                                                        |
| docutils       | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                      |
| tornado_http   | 103 ms                                                 | 94.2 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                        |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 844 ms: 1.40x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 840 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                       |
| float          | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                       |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 81.8 ms: 1.09x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.07x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                        |
| json_loads           | 28.5 us                                                | 27.5 us: 1.04x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.81 ms: 1.21x faster                                                       |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                        |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 844 ms: 1.40x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 840 ms: 1.38x faster                                                        |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 60.6 ms: 1.24x faster                                                       |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                        |
| nbody                      | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                       |
| mako                       | 11.9 ms                                                | 9.81 ms: 1.21x faster                                                       |
| float                      | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 68.1 ms: 1.20x faster                                                       |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.31 ms: 1.17x faster                                                       |
| fannkuch                   | 417 ms                                                 | 360 ms: 1.16x faster                                                        |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                        |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                       |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                        |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 710 ms: 1.09x faster                                                        |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                        |
| tornado_http               | 103 ms                                                 | 94.2 ms: 1.09x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 81.8 ms: 1.09x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| richards                   | 45.8 ms                                                | 42.2 ms: 1.09x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.07x faster                                                        |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.07x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                       |
| richards_super             | 51.5 ms                                                | 48.7 ms: 1.06x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                        |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.5 us: 1.04x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.67 ms: 1.03x faster                                                       |
| dask                       | 372 ms                                                 | 362 ms: 1.03x faster                                                        |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.66 ms: 1.02x faster                                                       |
| async_generators           | 463 ms                                                 | 456 ms: 1.02x faster                                                        |
| sympy_str                  | 300 ms                                                 | 295 ms: 1.01x faster                                                        |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 835 us: 1.01x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 68.1 ms: 1.01x faster                                                       |
| 2to3                       | 274 ms                                                 | 273 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                        |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 55.8 ms: 1.02x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 503 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                        |
| nqueens                    | 83.3 ms                                                | 85.9 ms: 1.03x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.65 ms: 1.04x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                       |
| sympy_expand               | 478 ms                                                 | 498 ms: 1.04x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                       |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                       |
| scimark_lu                 | 118 ms                                                 | 123 ms: 1.05x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                       |
| go                         | 139 ms                                                 | 147 ms: 1.06x slower                                                        |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.09x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                       |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (3): json_dumps, bench_mp_pool, scimark_sor
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240717-3.14.0a0-5206d7b-JIT/bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x