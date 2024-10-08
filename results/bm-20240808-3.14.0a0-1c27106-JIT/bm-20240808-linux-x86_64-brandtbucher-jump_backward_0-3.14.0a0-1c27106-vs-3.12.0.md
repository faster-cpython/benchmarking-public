# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 1c27106
- commit date: 2024-08-08
- overall geometric mean: 1.05x faster
- HPT reliability: 96.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                                   |
| docutils       | 2.77 sec                                               | 3.09 sec: 1.12x slower                                                 |
| tornado_http   | 103 ms                                                 | 110 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.42x faster                                                   |
| async_tree_none            | 472 ms                                                 | 338 ms: 1.39x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 879 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 441 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 935 ms: 1.24x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.2 ms: 1.21x faster                                                  |
| float          | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.41 ms: 1.06x faster                                                  |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.6 ms: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.05x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.16x faster                                                  |
| django_template | 34.6 ms                                                | 39.5 ms: 1.14x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.42x faster                                                   |
| async_tree_none            | 472 ms                                                 | 338 ms: 1.39x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                  |
| deepcopy                   | 371 us                                                 | 275 us: 1.35x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 879 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 441 ms: 1.31x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 59.2 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 935 ms: 1.24x faster                                                   |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.23x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 66.4 ms: 1.23x faster                                                  |
| nbody                      | 97.0 ms                                                | 80.2 ms: 1.21x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                  |
| float                      | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.33 ms: 1.17x faster                                                  |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.16x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.93 us: 1.14x faster                                                  |
| fannkuch                   | 417 ms                                                 | 369 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                   |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                   |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.6 ms: 1.07x faster                                                  |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                   |
| raytrace                   | 312 ms                                                 | 293 ms: 1.07x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.41 ms: 1.06x faster                                                  |
| pyflate                    | 482 ms                                                 | 459 ms: 1.05x faster                                                   |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                   |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                                  |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                  |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                 |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                   |
| nqueens                    | 83.3 ms                                                | 84.4 ms: 1.01x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.72 ms: 1.02x slower                                                  |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                 |
| logging_simple             | 6.46 us                                                | 6.63 us: 1.03x slower                                                  |
| logging_format             | 7.23 us                                                | 7.47 us: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                  |
| richards                   | 45.8 ms                                                | 47.6 ms: 1.04x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                  |
| richards_super             | 51.5 ms                                                | 54.0 ms: 1.05x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 117 ms: 1.06x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 893 us: 1.06x slower                                                   |
| tornado_http               | 103 ms                                                 | 110 ms: 1.08x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 59.2 ms: 1.08x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.94 ms: 1.08x slower                                                  |
| sympy_str                  | 300 ms                                                 | 325 ms: 1.08x slower                                                   |
| go                         | 139 ms                                                 | 151 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                   |
| telco                      | 7.10 ms                                                | 7.72 ms: 1.09x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 535 ms: 1.09x slower                                                   |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                  |
| generators                 | 31.2 ms                                                | 34.4 ms: 1.10x slower                                                  |
| deltablue                  | 3.72 ms                                                | 4.13 ms: 1.11x slower                                                  |
| docutils                   | 2.77 sec                                               | 3.09 sec: 1.12x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| sympy_expand               | 478 ms                                                 | 541 ms: 1.13x slower                                                   |
| django_template            | 34.6 ms                                                | 39.5 ms: 1.14x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 197 ms: 1.17x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 25.1 ms: 1.17x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                  |
| coverage                   | 72.7 ms                                                | 93.6 ms: 1.29x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (3): json_loads, bench_mp_pool, sqlglot_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240808-3.14.0a0-1c27106-JIT/bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.67% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x