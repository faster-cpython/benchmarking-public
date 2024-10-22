# Results vs. 3.12.0

- fork: brandtbucher
- ref: ujb0_project_confide
- machine: linux-x86_64
- commit hash: d467f6c
- commit date: 2024-09-04
- overall geometric mean: 1.04x faster
- HPT reliability: 97.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 294 ms: 1.07x slower                                                        |
| docutils       | 2.77 sec                                               | 3.52 sec: 1.27x slower                                                      |
| tornado_http   | 103 ms                                                 | 118 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                  | 1.16x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                        |
| async_tree_none            | 472 ms                                                 | 341 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 416 ms: 1.38x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 907 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 961 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.7 ms: 1.23x faster                                                       |
| nbody          | 97.0 ms                                                | 79.9 ms: 1.21x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                       |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                        |
| regex_compile  | 148 ms                                                 | 152 ms: 1.03x slower                                                        |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 80.1 ms: 1.11x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                       |
| tomli_loads          | 2.33 sec                                               | 2.15 sec: 1.08x faster                                                      |
| json_dumps           | 10.4 ms                                                | 9.72 ms: 1.07x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.05x faster                                                        |
| json_loads           | 28.5 us                                                | 29.6 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.58 ms: 1.24x faster                                                       |
| django_template | 34.6 ms                                                | 40.5 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.3 us: 1.55x faster                                                       |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                        |
| async_tree_none            | 472 ms                                                 | 341 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 416 ms: 1.38x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 907 ms: 1.30x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 57.9 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.25x faster                                                       |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.25x faster                                                        |
| mako                       | 11.9 ms                                                | 9.58 ms: 1.24x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 66.0 ms: 1.24x faster                                                       |
| float                      | 84.7 ms                                                | 68.7 ms: 1.23x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                       |
| nbody                      | 97.0 ms                                                | 79.9 ms: 1.21x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 961 ms: 1.20x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.34 ms: 1.17x faster                                                       |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                       |
| chaos                      | 67.0 ms                                                | 59.9 ms: 1.12x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 695 ms: 1.12x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 80.1 ms: 1.11x faster                                                       |
| richards                   | 45.8 ms                                                | 41.4 ms: 1.11x faster                                                       |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                        |
| fannkuch                   | 417 ms                                                 | 380 ms: 1.10x faster                                                        |
| logging_format             | 7.23 us                                                | 6.59 us: 1.10x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                        |
| richards_super             | 51.5 ms                                                | 47.1 ms: 1.09x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 108 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.15 sec: 1.08x faster                                                      |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                        |
| logging_simple             | 6.46 us                                                | 6.00 us: 1.08x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 9.72 ms: 1.07x faster                                                       |
| logging_silent             | 104 ns                                                 | 98.3 ns: 1.06x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.05x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.56 ms: 1.04x faster                                                       |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                      |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| pyflate                    | 482 ms                                                 | 484 ms: 1.00x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 3.82 ms: 1.01x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                       |
| nqueens                    | 83.3 ms                                                | 84.5 ms: 1.02x slower                                                       |
| asyncio_websockets         | 551 ms                                                 | 560 ms: 1.02x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                      |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                        |
| regex_compile              | 148 ms                                                 | 152 ms: 1.03x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 24.9 ms: 1.04x slower                                                       |
| json_loads                 | 28.5 us                                                | 29.6 us: 1.04x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 893 us: 1.06x slower                                                        |
| 2to3                       | 274 ms                                                 | 294 ms: 1.07x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 530 ms: 1.08x slower                                                        |
| generators                 | 31.2 ms                                                | 34.1 ms: 1.09x slower                                                       |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 125 ms: 1.13x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.35 sec: 1.15x slower                                                      |
| tornado_http               | 103 ms                                                 | 118 ms: 1.15x slower                                                        |
| sympy_str                  | 300 ms                                                 | 345 ms: 1.15x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.40 ms: 1.15x slower                                                       |
| sympy_expand               | 478 ms                                                 | 559 ms: 1.17x slower                                                        |
| django_template            | 34.6 ms                                                | 40.5 ms: 1.17x slower                                                       |
| coverage                   | 72.7 ms                                                | 87.9 ms: 1.21x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.81 ms: 1.23x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 67.6 ms: 1.23x slower                                                       |
| docutils                   | 2.77 sec                                               | 3.52 sec: 1.27x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 217 ms: 1.28x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 27.5 ms: 1.29x slower                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.75 ms: 1.29x slower                                                       |
| go                         | 139 ms                                                 | 181 ms: 1.30x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 2.19 ms: 1.30x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240904-3.14.0a0-d467f6c-JIT/bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.57% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.18x