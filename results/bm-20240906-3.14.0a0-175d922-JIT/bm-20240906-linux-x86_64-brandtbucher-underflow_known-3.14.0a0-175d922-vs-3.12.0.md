# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 175d922
- commit date: 2024-09-06
- overall geometric mean: 1.07x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                   |
| docutils       | 2.77 sec                                               | 3.01 sec: 1.09x slower                                                 |
| tornado_http   | 103 ms                                                 | 97.0 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                                   |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.32x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 898 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.5 ms: 1.22x faster                                                  |
| float          | 84.7 ms                                                | 70.3 ms: 1.20x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                  |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                   |
| unpickle             | 15.9 us                                                | 15.0 us: 1.06x faster                                                  |
| unpickle_list        | 5.29 us                                                | 5.16 us: 1.02x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.9 us: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.00x faster                                                  |
| pickle               | 11.6 us                                                | 11.6 us: 1.00x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.81 ms: 1.21x faster                                                  |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.0 us: 1.56x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                                   |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                   |
| deepcopy                   | 371 us                                                 | 264 us: 1.41x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.32x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 898 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                  |
| scimark_fft                | 382 ms                                                 | 305 ms: 1.25x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 66.9 ms: 1.22x faster                                                  |
| nbody                      | 97.0 ms                                                | 79.5 ms: 1.22x faster                                                  |
| mako                       | 11.9 ms                                                | 9.81 ms: 1.21x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                 |
| richards_super             | 51.5 ms                                                | 42.6 ms: 1.21x faster                                                  |
| float                      | 84.7 ms                                                | 70.3 ms: 1.20x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.23 ms: 1.20x faster                                                  |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                  |
| spectral_norm              | 115 ms                                                 | 99.7 ms: 1.15x faster                                                  |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                  |
| richards                   | 45.8 ms                                                | 40.0 ms: 1.14x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.14x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                  |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                  |
| fannkuch                   | 417 ms                                                 | 376 ms: 1.11x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                  |
| logging_silent             | 104 ns                                                 | 94.5 ns: 1.10x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                   |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                   |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                   |
| tornado_http               | 103 ms                                                 | 97.0 ms: 1.06x faster                                                  |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.66 ms: 1.04x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                 |
| unpickle_list              | 5.29 us                                                | 5.16 us: 1.02x faster                                                  |
| pickle_dict                | 35.5 us                                                | 34.9 us: 1.02x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                  |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.00x faster                                                  |
| pickle                     | 11.6 us                                                | 11.6 us: 1.00x slower                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.37 ms: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 495 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.71 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                   |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                   |
| pickle_list                | 5.08 us                                                | 5.18 us: 1.02x slower                                                  |
| nqueens                    | 83.3 ms                                                | 85.2 ms: 1.02x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                  |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                   |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                  |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 58.3 ms: 1.06x slower                                                  |
| generators                 | 31.2 ms                                                | 33.3 ms: 1.07x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.07x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.88 ms: 1.07x slower                                                  |
| docutils                   | 2.77 sec                                               | 3.01 sec: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                  |
| telco                      | 7.10 ms                                                | 7.97 ms: 1.12x slower                                                  |
| coverage                   | 72.7 ms                                                | 86.0 ms: 1.18x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                  |
| unpack_sequence            | 54.0 ns                                                | 111 ns: 2.06x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (6): sympy_str, bench_thread_pool, pidigits, dulwich_log, bench_mp_pool, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240906-3.14.0a0-175d922-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x