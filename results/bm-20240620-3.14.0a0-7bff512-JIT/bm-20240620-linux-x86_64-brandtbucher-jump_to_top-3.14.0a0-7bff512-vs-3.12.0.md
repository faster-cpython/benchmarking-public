# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_to_top
- machine: linux-x86_64
- commit hash: 7bff512
- commit date: 2024-06-20
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.01x faster                                               |
| tornado_http   | 103 ms                                                 | 93.3 ms: 1.10x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                               |
| async_tree_none            | 472 ms                                                 | 366 ms: 1.29x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 450 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 570 ms: 1.27x faster                                               |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 986 ms: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 611 ms: 1.19x faster                                               |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.2 ms: 1.22x faster                                              |
| float          | 84.7 ms                                                | 70.2 ms: 1.21x faster                                              |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.14x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.85 ms: 1.07x slower                                              |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                               |
| regex_v8       | 23.1 ms                                                | 26.8 ms: 1.16x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                             |
| pickle_pure_python   | 324 us                                                 | 290 us: 1.12x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 80.4 ms: 1.11x faster                                              |
| unpickle             | 15.9 us                                                | 14.4 us: 1.10x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 57.6 ms: 1.07x faster                                              |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                               |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                              |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                              |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                              |
| pickle_list          | 5.08 us                                                | 5.31 us: 1.05x slower                                              |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                       |

Benchmark hidden because not significant (2): unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.39 ms: 1.06x slower                                              |
| python_startup         | 9.55 ms                                                | 10.8 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.63 ms: 1.23x faster                                              |
| django_template | 34.6 ms                                                | 36.6 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.42x faster                                              |
| deepcopy                   | 371 us                                                 | 275 us: 1.35x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                               |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                              |
| async_tree_none            | 472 ms                                                 | 366 ms: 1.29x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 450 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 570 ms: 1.27x faster                                               |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                               |
| mako                       | 11.9 ms                                                | 9.63 ms: 1.23x faster                                              |
| nbody                      | 97.0 ms                                                | 79.2 ms: 1.22x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 67.0 ms: 1.22x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 61.6 ms: 1.22x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                             |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.21x faster                                               |
| float                      | 84.7 ms                                                | 70.2 ms: 1.21x faster                                              |
| logging_format             | 7.23 us                                                | 5.99 us: 1.21x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 986 ms: 1.20x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 611 ms: 1.19x faster                                               |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.83 us: 1.18x faster                                              |
| fannkuch                   | 417 ms                                                 | 353 ms: 1.18x faster                                               |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.41 ms: 1.15x faster                                              |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                              |
| pickle_pure_python         | 324 us                                                 | 290 us: 1.12x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 80.4 ms: 1.11x faster                                              |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                               |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                               |
| tornado_http               | 103 ms                                                 | 93.3 ms: 1.10x faster                                              |
| unpickle                   | 15.9 us                                                | 14.4 us: 1.10x faster                                              |
| richards                   | 45.8 ms                                                | 41.9 ms: 1.10x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 710 ms: 1.09x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                               |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                              |
| richards_super             | 51.5 ms                                                | 48.0 ms: 1.07x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 57.6 ms: 1.07x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                             |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                              |
| gc_traversal               | 3.79 ms                                                | 3.59 ms: 1.06x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.52 ms: 1.05x faster                                              |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                              |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                             |
| dask                       | 372 ms                                                 | 363 ms: 1.02x faster                                               |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.02x faster                                               |
| dulwich_log                | 68.5 ms                                                | 67.1 ms: 1.02x faster                                              |
| sympy_str                  | 300 ms                                                 | 294 ms: 1.02x faster                                               |
| bench_thread_pool          | 842 us                                                 | 827 us: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                              |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                               |
| 2to3                       | 274 ms                                                 | 273 ms: 1.01x faster                                               |
| asyncio_tcp                | 491 ms                                                 | 490 ms: 1.00x faster                                               |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                               |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                              |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                              |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                              |
| hexiom                     | 6.41 ms                                                | 6.51 ms: 1.01x slower                                              |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                               |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                               |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                              |
| nqueens                    | 83.3 ms                                                | 85.4 ms: 1.03x slower                                              |
| sympy_integrate            | 21.4 ms                                                | 22.0 ms: 1.03x slower                                              |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                               |
| sympy_expand               | 478 ms                                                 | 499 ms: 1.04x slower                                               |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.04x slower                                              |
| scimark_lu                 | 118 ms                                                 | 123 ms: 1.04x slower                                               |
| pickle_list                | 5.08 us                                                | 5.31 us: 1.05x slower                                              |
| django_template            | 34.6 ms                                                | 36.6 ms: 1.06x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.39 ms: 1.06x slower                                              |
| regex_effbot               | 3.61 ms                                                | 3.85 ms: 1.07x slower                                              |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                               |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                              |
| python_startup             | 9.55 ms                                                | 10.8 ms: 1.13x slower                                              |
| regex_v8                   | 23.1 ms                                                | 26.8 ms: 1.16x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                              |
| coverage                   | 72.7 ms                                                | 94.1 ms: 1.29x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (5): async_generators, unpickle_list, pickle_dict, bench_mp_pool, json
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240620-3.14.0a0-7bff512-JIT/bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x