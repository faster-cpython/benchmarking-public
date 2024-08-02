# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: f6b4125
- commit date: 2024-07-10
- overall geometric mean: 1.08x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 275 ms: 1.00x slower                                                    |
| docutils       | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                  |
| tornado_http   | 103 ms                                                 | 92.6 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                    |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 848 ms: 1.39x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                   |
| nbody          | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                    |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                   |
| regex_effbot   | 3.61 ms                                                | 4.02 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 207 us: 1.11x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 292 us: 1.11x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 81.6 ms: 1.09x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                   |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                            |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.91 ms: 1.20x faster                                                   |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 27.4 us: 1.49x faster                                                   |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 848 ms: 1.39x faster                                                    |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 58.5 ms: 1.28x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 67.0 ms: 1.22x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                  |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                   |
| nbody                      | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                   |
| logging_format             | 7.23 us                                                | 6.02 us: 1.20x faster                                                   |
| mako                       | 11.9 ms                                                | 9.91 ms: 1.20x faster                                                   |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.19x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                   |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                    |
| fannkuch                   | 417 ms                                                 | 362 ms: 1.15x faster                                                    |
| richards                   | 45.8 ms                                                | 40.9 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.53 ms: 1.12x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 697 ms: 1.11x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 207 us: 1.11x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 292 us: 1.11x faster                                                    |
| tornado_http               | 103 ms                                                 | 92.6 ms: 1.11x faster                                                   |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.43 sec: 1.10x faster                                                  |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 81.6 ms: 1.09x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                    |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                    |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.08x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                   |
| richards_super             | 51.5 ms                                                | 48.0 ms: 1.07x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                   |
| logging_silent             | 104 ns                                                 | 98.0 ns: 1.07x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                    |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.05x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.60 ms: 1.03x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 164 ms: 1.03x faster                                                    |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                                   |
| dask                       | 372 ms                                                 | 363 ms: 1.02x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 67.0 ms: 1.02x faster                                                   |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                   |
| sympy_str                  | 300 ms                                                 | 295 ms: 1.02x faster                                                    |
| bench_thread_pool          | 842 us                                                 | 829 us: 1.02x faster                                                    |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                   |
| 2to3                       | 274 ms                                                 | 275 ms: 1.00x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                    |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.3 ms: 1.01x slower                                                   |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.02x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 500 ms: 1.02x slower                                                    |
| nqueens                    | 83.3 ms                                                | 85.1 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 22.0 ms: 1.03x slower                                                   |
| hexiom                     | 6.41 ms                                                | 6.65 ms: 1.04x slower                                                   |
| sympy_expand               | 478 ms                                                 | 496 ms: 1.04x slower                                                    |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                   |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                    |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 4.02 ms: 1.11x slower                                                   |
| telco                      | 7.10 ms                                                | 8.00 ms: 1.13x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                   |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                            |

Benchmark hidden because not significant (2): bench_mp_pool, json_dumps
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240710-3.14.0a0-f6b4125-JIT/bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x