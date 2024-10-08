# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_jump_backw
- machine: linux-x86_64
- commit hash: e448061
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 85.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 290 ms: 1.06x slower                                                        |
| docutils       | 2.77 sec                                               | 3.58 sec: 1.29x slower                                                      |
| tornado_http   | 103 ms                                                 | 120 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                  | 1.17x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 416 ms: 1.38x faster                                                        |
| async_tree_none            | 472 ms                                                 | 347 ms: 1.36x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 437 ms: 1.32x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 896 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 558 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 581 ms: 1.25x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 966 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                       |
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 147 ms: 1.01x faster                                                        |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| regex_effbot   | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 288 us: 1.13x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 81.4 ms: 1.10x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 57.2 ms: 1.08x faster                                                       |
| tomli_loads          | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                      |
| json_dumps           | 10.4 ms                                                | 9.97 ms: 1.04x faster                                                       |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.19 ms: 1.04x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                       |
| django_template | 34.6 ms                                                | 42.1 ms: 1.22x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 416 ms: 1.38x faster                                                        |
| deepcopy                   | 371 us                                                 | 272 us: 1.37x faster                                                        |
| async_tree_none            | 472 ms                                                 | 347 ms: 1.36x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 437 ms: 1.32x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 896 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 558 ms: 1.30x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 58.9 ms: 1.28x faster                                                       |
| scimark_fft                | 382 ms                                                 | 301 ms: 1.27x faster                                                        |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 581 ms: 1.25x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 65.7 ms: 1.25x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                       |
| nbody                      | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                       |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 966 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.86 us: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.34 ms: 1.17x faster                                                       |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 688 ms: 1.13x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 288 us: 1.13x faster                                                        |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                                        |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 81.4 ms: 1.10x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                      |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 57.2 ms: 1.08x faster                                                       |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.07x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                      |
| chaos                      | 67.0 ms                                                | 62.6 ms: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 9.97 ms: 1.04x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                        |
| json                       | 5.26 ms                                                | 5.18 ms: 1.01x faster                                                       |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                        |
| regex_compile              | 148 ms                                                 | 147 ms: 1.01x faster                                                        |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                        |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                       |
| bench_mp_pool              | 24.0 ms                                                | 24.1 ms: 1.00x slower                                                       |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                      |
| logging_format             | 7.23 us                                                | 7.45 us: 1.03x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.19 ms: 1.04x slower                                                       |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                       |
| nqueens                    | 83.3 ms                                                | 86.6 ms: 1.04x slower                                                       |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                       |
| 2to3                       | 274 ms                                                 | 290 ms: 1.06x slower                                                        |
| mdp                        | 2.63 sec                                               | 2.80 sec: 1.06x slower                                                      |
| logging_simple             | 6.46 us                                                | 6.91 us: 1.07x slower                                                       |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 531 ms: 1.08x slower                                                        |
| logging_silent             | 104 ns                                                 | 113 ns: 1.08x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 914 us: 1.09x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                       |
| generators                 | 31.2 ms                                                | 34.5 ms: 1.10x slower                                                       |
| hexiom                     | 6.41 ms                                                | 7.15 ms: 1.11x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| pycparser                  | 1.18 sec                                               | 1.32 sec: 1.12x slower                                                      |
| sympy_str                  | 300 ms                                                 | 339 ms: 1.13x slower                                                        |
| sqlglot_normalize          | 110 ms                                                 | 128 ms: 1.16x slower                                                        |
| tornado_http               | 103 ms                                                 | 120 ms: 1.17x slower                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.60 ms: 1.18x slower                                                       |
| richards                   | 45.8 ms                                                | 54.2 ms: 1.18x slower                                                       |
| sympy_expand               | 478 ms                                                 | 565 ms: 1.18x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 2.02 ms: 1.20x slower                                                       |
| deltablue                  | 3.72 ms                                                | 4.46 ms: 1.20x slower                                                       |
| coverage                   | 72.7 ms                                                | 87.4 ms: 1.20x slower                                                       |
| richards_super             | 51.5 ms                                                | 62.0 ms: 1.20x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 66.3 ms: 1.21x slower                                                       |
| django_template            | 34.6 ms                                                | 42.1 ms: 1.22x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.81 ms: 1.23x slower                                                       |
| sympy_sum                  | 169 ms                                                 | 213 ms: 1.26x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 27.3 ms: 1.28x slower                                                       |
| docutils                   | 2.77 sec                                               | 3.58 sec: 1.29x slower                                                      |
| go                         | 139 ms                                                 | 182 ms: 1.30x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240829-3.14.0a0-e448061-JIT/bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 85.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x