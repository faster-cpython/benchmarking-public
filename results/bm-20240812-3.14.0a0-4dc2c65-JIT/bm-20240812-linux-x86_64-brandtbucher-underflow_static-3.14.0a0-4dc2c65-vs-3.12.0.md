# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 4dc2c65
- commit date: 2024-08-12
- overall geometric mean: 1.07x faster
- HPT reliability: 99.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                                    |
| docutils       | 2.77 sec                                               | 3.30 sec: 1.19x slower                                                  |
| tornado_http   | 103 ms                                                 | 95.3 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                    |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 421 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 866 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.29x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                   |
| float          | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                   |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                  | 1.13x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 146 ms: 1.02x faster                                                    |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                    |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                   |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 203 us: 1.13x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 80.5 ms: 1.11x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.07x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                    |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.18 ms: 1.04x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.91 ms: 1.20x faster                                                   |
| django_template | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.0 us: 1.56x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                    |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                    |
| deepcopy                   | 371 us                                                 | 268 us: 1.38x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 421 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 866 ms: 1.37x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                   |
| richards                   | 45.8 ms                                                | 35.2 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.29x faster                                                    |
| richards_super             | 51.5 ms                                                | 40.2 ms: 1.28x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 65.5 ms: 1.25x faster                                                   |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                   |
| nbody                      | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                   |
| float                      | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                   |
| mako                       | 11.9 ms                                                | 9.91 ms: 1.20x faster                                                   |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.30 ms: 1.18x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.6 ms: 1.16x faster                                                   |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                    |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                    |
| fannkuch                   | 417 ms                                                 | 365 ms: 1.14x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 203 us: 1.13x faster                                                    |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 80.5 ms: 1.11x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                   |
| tornado_http               | 103 ms                                                 | 95.3 ms: 1.08x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.07x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                    |
| pyflate                    | 482 ms                                                 | 453 ms: 1.06x faster                                                    |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                    |
| logging_silent             | 104 ns                                                 | 99.3 ns: 1.05x faster                                                   |
| json                       | 5.26 ms                                                | 5.04 ms: 1.04x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 820 us: 1.03x faster                                                    |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                                   |
| chaos                      | 67.0 ms                                                | 65.3 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 759 ms: 1.02x faster                                                    |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                    |
| regex_compile              | 148 ms                                                 | 146 ms: 1.02x faster                                                    |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                    |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.18 ms: 1.04x slower                                                   |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.04x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 515 ms: 1.05x slower                                                    |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.46 ms: 1.07x slower                                                   |
| hexiom                     | 6.41 ms                                                | 6.88 ms: 1.07x slower                                                   |
| telco                      | 7.10 ms                                                | 7.62 ms: 1.07x slower                                                   |
| sympy_str                  | 300 ms                                                 | 323 ms: 1.08x slower                                                    |
| sympy_expand               | 478 ms                                                 | 519 ms: 1.09x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 120 ms: 1.09x slower                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.84 ms: 1.09x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 60.3 ms: 1.10x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                   |
| sympy_sum                  | 169 ms                                                 | 191 ms: 1.13x slower                                                    |
| sympy_integrate            | 21.4 ms                                                | 24.4 ms: 1.14x slower                                                   |
| docutils                   | 2.77 sec                                               | 3.30 sec: 1.19x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                   |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                                   |
| generators                 | 31.2 ms                                                | 41.3 ms: 1.32x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (3): pprint_pformat, bench_mp_pool, nqueens
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240812-3.14.0a0-4dc2c65-JIT/bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.04% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x