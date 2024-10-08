# Results vs. 3.12.0

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-x86_64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                |
| tornado_http   | 103 ms                                                 | 90.5 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 894 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.5 ms: 1.13x faster                                                 |
| float          | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.14x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                 |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| django_template | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                  |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 894 ms: 1.32x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                 |
| raytrace                   | 312 ms                                                 | 261 ms: 1.20x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.44 us: 1.19x faster                                                 |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                  |
| regex_compile              | 148 ms                                                 | 131 ms: 1.14x faster                                                  |
| nbody                      | 97.0 ms                                                | 85.5 ms: 1.13x faster                                                 |
| tornado_http               | 103 ms                                                 | 90.5 ms: 1.13x faster                                                 |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                 |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.6 ms: 1.11x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                                 |
| float                      | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.68 ms: 1.08x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 784 us: 1.07x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                 |
| logging_silent             | 104 ns                                                 | 97.7 ns: 1.07x faster                                                 |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                |
| scimark_fft                | 382 ms                                                 | 360 ms: 1.06x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                  |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.10 ms: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| pyflate                    | 482 ms                                                 | 466 ms: 1.04x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.4 ms: 1.04x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                  |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                  |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.02x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                |
| asyncio_tcp                | 491 ms                                                 | 482 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                                 |
| django_template            | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.01x slower                                                 |
| richards_super             | 51.5 ms                                                | 51.9 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                  |
| richards                   | 45.8 ms                                                | 46.4 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.02x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                 |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                 |
| go                         | 139 ms                                                 | 162 ms: 1.16x slower                                                  |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                 |
| telco                      | 7.10 ms                                                | 8.33 ms: 1.17x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (3): json_loads, bench_mp_pool, asyncio_tcp_ssl
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240827-3.14.0a0-04d5e93/bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x