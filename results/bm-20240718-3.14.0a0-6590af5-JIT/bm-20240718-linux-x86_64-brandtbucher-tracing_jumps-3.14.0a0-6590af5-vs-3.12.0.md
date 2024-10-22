# Results vs. 3.12.0

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 6590af5
- commit date: 2024-07-18
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 2.88 sec: 1.04x slower                                               |
| tornado_http   | 103 ms                                                 | 92.5 ms: 1.11x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.52x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 844 ms: 1.40x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.8 ms: 1.18x faster                                                |
| nbody          | 97.0 ms                                                | 82.4 ms: 1.18x faster                                                |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                |
| regex_dna      | 212 ms                                                 | 228 ms: 1.08x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                                |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                 |
| json_loads           | 28.5 us                                                | 27.4 us: 1.04x faster                                                |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                         |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.65 ms: 1.23x faster                                                |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.52x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 844 ms: 1.40x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                                |
| deepcopy                   | 371 us                                                 | 276 us: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 60.4 ms: 1.24x faster                                                |
| mako                       | 11.9 ms                                                | 9.65 ms: 1.23x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 66.7 ms: 1.23x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                 |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                                |
| float                      | 84.7 ms                                                | 71.8 ms: 1.18x faster                                                |
| nbody                      | 97.0 ms                                                | 82.4 ms: 1.18x faster                                                |
| fannkuch                   | 417 ms                                                 | 358 ms: 1.17x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.35 ms: 1.16x faster                                                |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.16x faster                                                |
| pyflate                    | 482 ms                                                 | 421 ms: 1.15x faster                                                 |
| richards                   | 45.8 ms                                                | 40.8 ms: 1.12x faster                                                |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                |
| tornado_http               | 103 ms                                                 | 92.5 ms: 1.11x faster                                                |
| richards_super             | 51.5 ms                                                | 46.5 ms: 1.11x faster                                                |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                                |
| meteor_contest             | 112 ms                                                 | 104 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.57 ms: 1.04x faster                                                |
| json_loads                 | 28.5 us                                                | 27.4 us: 1.04x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                |
| dask                       | 372 ms                                                 | 363 ms: 1.03x faster                                                 |
| async_generators           | 463 ms                                                 | 451 ms: 1.03x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.71 ms: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                |
| bench_thread_pool          | 842 us                                                 | 826 us: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                               |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                                |
| mdp                        | 2.63 sec                                               | 2.61 sec: 1.01x faster                                               |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| nqueens                    | 83.3 ms                                                | 83.8 ms: 1.01x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 55.3 ms: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 498 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                 |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.88 sec: 1.04x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.67 ms: 1.04x slower                                                |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.04x slower                                                |
| sympy_expand               | 478 ms                                                 | 501 ms: 1.05x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                 |
| generators                 | 31.2 ms                                                | 33.0 ms: 1.06x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.08x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.09x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                |
| telco                      | 7.10 ms                                                | 8.08 ms: 1.14x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                |
| coverage                   | 72.7 ms                                                | 90.9 ms: 1.25x slower                                                |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (6): json, scimark_sor, bench_mp_pool, 2to3, json_dumps, sympy_sum
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240718-3.14.0a0-6590af5-JIT/bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x