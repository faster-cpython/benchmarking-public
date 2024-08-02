# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.01x slower
- HPT reliability: 64.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 304 ms: 1.06x slower                                                       |
| docutils       | 2.87 sec                                                     | 3.09 sec: 1.08x slower                                                     |
| Geometric mean | (ref)                                                        | 1.05x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 432 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                                       |
| async_tree_none            | 452 ms                                                       | 377 ms: 1.20x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 886 ms: 1.18x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 914 ms: 1.15x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 476 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 620 ms: 1.12x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                       |
| nbody          | 88.0 ms                                                      | 84.1 ms: 1.05x faster                                                      |
| float          | 76.6 ms                                                      | 75.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                        | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 136 ms: 1.06x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                      |
| regex_v8       | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.8 ms: 1.05x faster                                                      |
| pickle_dict          | 32.5 us                                                      | 31.1 us: 1.05x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 99.0 ms: 1.04x faster                                                      |
| tomli_loads          | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                     |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.00x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 58.6 ms: 1.00x slower                                                      |
| pickle_list          | 4.43 us                                                      | 4.48 us: 1.01x slower                                                      |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                      |
| unpickle_list        | 4.66 us                                                      | 4.93 us: 1.06x slower                                                      |
| unpickle             | 14.8 us                                                      | 16.0 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                                      |
| python_startup         | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                      |
| django_template | 38.2 ms                                                      | 41.0 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 432 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.1 us: 1.21x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                                       |
| async_tree_none            | 452 ms                                                       | 377 ms: 1.20x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 886 ms: 1.18x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 914 ms: 1.15x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 476 ms: 1.14x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 70.5 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 620 ms: 1.12x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 83.0 ms: 1.10x faster                                                      |
| mako                       | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                      |
| generators                 | 37.4 ms                                                      | 34.8 ms: 1.08x faster                                                      |
| logging_format             | 7.48 us                                                      | 7.02 us: 1.07x faster                                                      |
| regex_compile              | 144 ms                                                       | 136 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                       |
| richards                   | 45.7 ms                                                      | 43.2 ms: 1.06x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 81.8 ms: 1.05x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.39 us: 1.05x faster                                                      |
| pickle_dict                | 32.5 us                                                      | 31.1 us: 1.05x faster                                                      |
| nbody                      | 88.0 ms                                                      | 84.1 ms: 1.05x faster                                                      |
| fannkuch                   | 350 ms                                                       | 336 ms: 1.04x faster                                                       |
| raytrace                   | 298 ms                                                       | 286 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 99.0 ms: 1.04x faster                                                      |
| scimark_fft                | 301 ms                                                       | 293 ms: 1.03x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                     |
| pprint_safe_repr           | 807 ms                                                       | 787 ms: 1.03x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                     |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.3 ms: 1.03x faster                                                      |
| regex_effbot               | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.13 ms: 1.02x faster                                                      |
| float                      | 76.6 ms                                                      | 75.5 ms: 1.02x faster                                                      |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 36.5 us: 1.01x faster                                                      |
| mdp                        | 2.57 sec                                                     | 2.56 sec: 1.01x faster                                                     |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                     |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.00x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 58.6 ms: 1.00x slower                                                      |
| asyncio_tcp                | 378 ms                                                       | 381 ms: 1.01x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.48 us: 1.01x slower                                                      |
| dask                       | 392 ms                                                       | 401 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.03x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                                      |
| chaos                      | 64.0 ms                                                      | 65.7 ms: 1.03x slower                                                      |
| sympy_str                  | 302 ms                                                       | 310 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                      |
| pyflate                    | 439 ms                                                       | 453 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                     |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 94.9 ms: 1.06x slower                                                      |
| unpickle_list              | 4.66 us                                                      | 4.93 us: 1.06x slower                                                      |
| sympy_integrate            | 23.9 ms                                                      | 25.4 ms: 1.06x slower                                                      |
| 2to3                       | 285 ms                                                       | 304 ms: 1.06x slower                                                       |
| django_template            | 38.2 ms                                                      | 41.0 ms: 1.07x slower                                                      |
| go                         | 150 ms                                                       | 161 ms: 1.08x slower                                                       |
| unpickle                   | 14.8 us                                                      | 16.0 us: 1.08x slower                                                      |
| docutils                   | 2.87 sec                                                     | 3.09 sec: 1.08x slower                                                     |
| deepcopy_reduce            | 3.37 us                                                      | 3.64 us: 1.08x slower                                                      |
| logging_silent             | 94.4 ns                                                      | 102 ns: 1.08x slower                                                       |
| sympy_expand               | 484 ms                                                       | 525 ms: 1.08x slower                                                       |
| deepcopy                   | 368 us                                                       | 408 us: 1.11x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 64.0 ms: 1.11x slower                                                      |
| regex_v8                   | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 130 ms: 1.12x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.68 ms: 1.12x slower                                                      |
| python_startup             | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                                      |
| deltablue                  | 3.24 ms                                                      | 3.74 ms: 1.16x slower                                                      |
| telco                      | 6.96 ms                                                      | 8.23 ms: 1.18x slower                                                      |
| scimark_lu                 | 98.8 ms                                                      | 117 ms: 1.18x slower                                                       |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                      |
| typing_runtime_protocols   | 152 us                                                       | 187 us: 1.23x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.97 ms: 1.24x slower                                                      |
| scimark_sor                | 109 ms                                                       | 137 ms: 1.25x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.88 ms: 1.40x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (11): pickle, richards_super, sqlite_synth, dulwich_log, meteor_contest, async_generators, regex_dna, bench_mp_pool, asyncio_websockets, tornado_http, bench_thread_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 64.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x