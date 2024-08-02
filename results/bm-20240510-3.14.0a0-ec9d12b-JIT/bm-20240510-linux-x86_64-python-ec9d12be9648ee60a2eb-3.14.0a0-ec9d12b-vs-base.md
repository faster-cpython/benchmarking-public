# Results vs. base

- fork: python
- ref: ec9d12be9648ee60a2eb
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.00x faster
- HPT reliability: 77.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json | results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                                                          | 280 ms: 1.04x slower                                                                                                |
| chameleon      | 7.08 ms                                                                                                         | 7.00 ms: 1.01x faster                                                                                               |
| docutils       | 2.81 sec                                                                                                        | 2.97 sec: 1.06x slower                                                                                              |
| html5lib       | 68.3 ms                                                                                                         | 67.7 ms: 1.01x faster                                                                                               |
| tornado_http   | 93.9 ms                                                                                                         | 97.6 ms: 1.04x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json | results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 78.6 ms                                                                                                         | 71.6 ms: 1.10x faster                                                                                               |
| nbody          | 88.0 ms                                                                                                         | 80.9 ms: 1.09x faster                                                                                               |
| pidigits       | 189 ms                                                                                                          | 188 ms: 1.00x faster                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.06x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json | results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.78 ms                                                                                                         | 3.55 ms: 1.07x faster                                                                                               |
| regex_v8       | 25.1 ms                                                                                                         | 24.3 ms: 1.04x faster                                                                                               |
| regex_compile  | 135 ms                                                                                                          | 139 ms: 1.03x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json | results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.10 sec                                                                                                        | 1.95 sec: 1.07x faster                                                                                              |
| xml_etree_parse      | 163 ms                                                                                                          | 152 ms: 1.07x faster                                                                                                |
| xml_etree_generate   | 89.0 ms                                                                                                         | 83.1 ms: 1.07x faster                                                                                               |
| xml_etree_iterparse  | 108 ms                                                                                                          | 101 ms: 1.06x faster                                                                                                |
| pickle_dict          | 35.1 us                                                                                                         | 33.5 us: 1.05x faster                                                                                               |
| xml_etree_process    | 61.5 ms                                                                                                         | 59.1 ms: 1.04x faster                                                                                               |
| json_dumps           | 10.7 ms                                                                                                         | 10.4 ms: 1.03x faster                                                                                               |
| pickle_pure_python   | 310 us                                                                                                          | 300 us: 1.03x faster                                                                                                |
| unpickle             | 16.1 us                                                                                                         | 15.6 us: 1.03x faster                                                                                               |
| pickle               | 11.7 us                                                                                                         | 11.8 us: 1.01x slower                                                                                               |
| unpickle_pure_python | 220 us                                                                                                          | 222 us: 1.01x slower                                                                                                |
| unpickle_list        | 5.34 us                                                                                                         | 5.44 us: 1.02x slower                                                                                               |
| pickle_list          | 5.29 us                                                                                                         | 5.47 us: 1.03x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json | results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.3 ms                                                                                                         | 11.0 ms: 1.06x slower                                                                                               |
| python_startup_no_site | 7.08 ms                                                                                                         | 7.63 ms: 1.08x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.07x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json | results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                                                                         | 9.56 ms: 1.16x faster                                                                                               |
| django_template | 35.1 ms                                                                                                         | 36.3 ms: 1.04x slower                                                                                               |
| genshi_text     | 23.7 ms                                                                                                         | 24.7 ms: 1.04x slower                                                                                               |
| genshi_xml      | 51.7 ms                                                                                                         | 57.9 ms: 1.12x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.01x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                | results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json | results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| scimark_fft              | 382 ms                                                                                                          | 319 ms: 1.19x faster                                                                                                |
| mako                     | 11.1 ms                                                                                                         | 9.56 ms: 1.16x faster                                                                                               |
| richards                 | 48.0 ms                                                                                                         | 41.8 ms: 1.15x faster                                                                                               |
| richards_super           | 54.5 ms                                                                                                         | 47.6 ms: 1.14x faster                                                                                               |
| scimark_sparse_mat_mult  | 5.10 ms                                                                                                         | 4.49 ms: 1.14x faster                                                                                               |
| spectral_norm            | 115 ms                                                                                                          | 102 ms: 1.13x faster                                                                                                |
| float                    | 78.6 ms                                                                                                         | 71.6 ms: 1.10x faster                                                                                               |
| crypto_pyaes             | 74.5 ms                                                                                                         | 67.9 ms: 1.10x faster                                                                                               |
| nbody                    | 88.0 ms                                                                                                         | 80.9 ms: 1.09x faster                                                                                               |
| fannkuch                 | 400 ms                                                                                                          | 371 ms: 1.08x faster                                                                                                |
| pprint_safe_repr         | 764 ms                                                                                                          | 708 ms: 1.08x faster                                                                                                |
| tomli_loads              | 2.10 sec                                                                                                        | 1.95 sec: 1.07x faster                                                                                              |
| pprint_pformat           | 1.56 sec                                                                                                        | 1.45 sec: 1.07x faster                                                                                              |
| xml_etree_parse          | 163 ms                                                                                                          | 152 ms: 1.07x faster                                                                                                |
| scimark_monte_carlo      | 67.9 ms                                                                                                         | 63.4 ms: 1.07x faster                                                                                               |
| xml_etree_generate       | 89.0 ms                                                                                                         | 83.1 ms: 1.07x faster                                                                                               |
| regex_effbot             | 3.78 ms                                                                                                         | 3.55 ms: 1.07x faster                                                                                               |
| deepcopy_memo            | 40.3 us                                                                                                         | 37.9 us: 1.06x faster                                                                                               |
| xml_etree_iterparse      | 108 ms                                                                                                          | 101 ms: 1.06x faster                                                                                                |
| pickle_dict              | 35.1 us                                                                                                         | 33.5 us: 1.05x faster                                                                                               |
| xml_etree_process        | 61.5 ms                                                                                                         | 59.1 ms: 1.04x faster                                                                                               |
| regex_v8                 | 25.1 ms                                                                                                         | 24.3 ms: 1.04x faster                                                                                               |
| json_dumps               | 10.7 ms                                                                                                         | 10.4 ms: 1.03x faster                                                                                               |
| pickle_pure_python       | 310 us                                                                                                          | 300 us: 1.03x faster                                                                                                |
| pyflate                  | 474 ms                                                                                                          | 459 ms: 1.03x faster                                                                                                |
| unpickle                 | 16.1 us                                                                                                         | 15.6 us: 1.03x faster                                                                                               |
| sqlite_synth             | 2.94 us                                                                                                         | 2.87 us: 1.03x faster                                                                                               |
| logging_format           | 6.42 us                                                                                                         | 6.28 us: 1.02x faster                                                                                               |
| chaos                    | 60.3 ms                                                                                                         | 59.3 ms: 1.02x faster                                                                                               |
| pycparser                | 1.16 sec                                                                                                        | 1.15 sec: 1.02x faster                                                                                              |
| chameleon                | 7.08 ms                                                                                                         | 7.00 ms: 1.01x faster                                                                                               |
| json                     | 5.44 ms                                                                                                         | 5.39 ms: 1.01x faster                                                                                               |
| comprehensions           | 16.8 us                                                                                                         | 16.7 us: 1.01x faster                                                                                               |
| html5lib                 | 68.3 ms                                                                                                         | 67.7 ms: 1.01x faster                                                                                               |
| pidigits                 | 189 ms                                                                                                          | 188 ms: 1.00x faster                                                                                                |
| meteor_contest           | 111 ms                                                                                                          | 110 ms: 1.00x faster                                                                                                |
| telco                    | 173 ms                                                                                                          | 173 ms: 1.00x faster                                                                                                |
| pickle                   | 11.7 us                                                                                                         | 11.8 us: 1.01x slower                                                                                               |
| asyncio_tcp_ssl          | 1.85 sec                                                                                                        | 1.86 sec: 1.01x slower                                                                                              |
| asyncio_websockets       | 563 ms                                                                                                          | 567 ms: 1.01x slower                                                                                                |
| unpickle_pure_python     | 220 us                                                                                                          | 222 us: 1.01x slower                                                                                                |
| pathlib                  | 17.6 ms                                                                                                         | 17.7 ms: 1.01x slower                                                                                               |
| bench_mp_pool            | 23.8 ms                                                                                                         | 24.0 ms: 1.01x slower                                                                                               |
| sqlglot_transpile        | 1.62 ms                                                                                                         | 1.64 ms: 1.01x slower                                                                                               |
| thrift                   | 820 us                                                                                                          | 830 us: 1.01x slower                                                                                                |
| logging_silent           | 104 ns                                                                                                          | 106 ns: 1.01x slower                                                                                                |
| coverage                 | 93.8 ms                                                                                                         | 95.1 ms: 1.01x slower                                                                                               |
| create_gc_cycles         | 1.80 ms                                                                                                         | 1.83 ms: 1.02x slower                                                                                               |
| unpickle_list            | 5.34 us                                                                                                         | 5.44 us: 1.02x slower                                                                                               |
| dask                     | 371 ms                                                                                                          | 379 ms: 1.02x slower                                                                                                |
| sqlglot_optimize         | 55.2 ms                                                                                                         | 56.5 ms: 1.02x slower                                                                                               |
| asyncio_tcp              | 510 ms                                                                                                          | 522 ms: 1.02x slower                                                                                                |
| typing_runtime_protocols | 167 us                                                                                                          | 171 us: 1.02x slower                                                                                                |
| deepcopy_reduce          | 3.27 us                                                                                                         | 3.36 us: 1.03x slower                                                                                               |
| sqlglot_normalize        | 109 ms                                                                                                          | 112 ms: 1.03x slower                                                                                                |
| regex_compile            | 135 ms                                                                                                          | 139 ms: 1.03x slower                                                                                                |
| flaskblogging            | 8.94 ms                                                                                                         | 9.23 ms: 1.03x slower                                                                                               |
| pickle_list              | 5.29 us                                                                                                         | 5.47 us: 1.03x slower                                                                                               |
| generators               | 29.3 ms                                                                                                         | 30.3 ms: 1.03x slower                                                                                               |
| deepcopy                 | 366 us                                                                                                          | 378 us: 1.03x slower                                                                                                |
| django_template          | 35.1 ms                                                                                                         | 36.3 ms: 1.04x slower                                                                                               |
| go                       | 144 ms                                                                                                          | 149 ms: 1.04x slower                                                                                                |
| 2to3                     | 269 ms                                                                                                          | 280 ms: 1.04x slower                                                                                                |
| tornado_http             | 93.9 ms                                                                                                         | 97.6 ms: 1.04x slower                                                                                               |
| genshi_text              | 23.7 ms                                                                                                         | 24.7 ms: 1.04x slower                                                                                               |
| raytrace                 | 267 ms                                                                                                          | 278 ms: 1.04x slower                                                                                                |
| scimark_sor              | 130 ms                                                                                                          | 136 ms: 1.04x slower                                                                                                |
| async_generators         | 446 ms                                                                                                          | 466 ms: 1.05x slower                                                                                                |
| hexiom                   | 6.28 ms                                                                                                         | 6.58 ms: 1.05x slower                                                                                               |
| bench_thread_pool        | 833 us                                                                                                          | 877 us: 1.05x slower                                                                                                |
| gc_traversal             | 3.67 ms                                                                                                         | 3.87 ms: 1.06x slower                                                                                               |
| docutils                 | 2.81 sec                                                                                                        | 2.97 sec: 1.06x slower                                                                                              |
| mdp                      | 2.57 sec                                                                                                        | 2.72 sec: 1.06x slower                                                                                              |
| dulwich_log              | 65.8 ms                                                                                                         | 69.6 ms: 1.06x slower                                                                                               |
| python_startup           | 10.3 ms                                                                                                         | 11.0 ms: 1.06x slower                                                                                               |
| scimark_lu               | 117 ms                                                                                                          | 125 ms: 1.07x slower                                                                                                |
| python_startup_no_site   | 7.08 ms                                                                                                         | 7.63 ms: 1.08x slower                                                                                               |
| sympy_str                | 279 ms                                                                                                          | 301 ms: 1.08x slower                                                                                                |
| nqueens                  | 80.3 ms                                                                                                         | 87.0 ms: 1.08x slower                                                                                               |
| sympy_expand             | 469 ms                                                                                                          | 510 ms: 1.09x slower                                                                                                |
| sympy_sum                | 157 ms                                                                                                          | 172 ms: 1.10x slower                                                                                                |
| sympy_integrate          | 20.5 ms                                                                                                         | 22.6 ms: 1.10x slower                                                                                               |
| pylint                   | 319 ms                                                                                                          | 354 ms: 1.11x slower                                                                                                |
| genshi_xml               | 51.7 ms                                                                                                         | 57.9 ms: 1.12x slower                                                                                               |
| deltablue                | 3.27 ms                                                                                                         | 3.73 ms: 1.14x slower                                                                                               |
| Geometric mean           | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (13): async_tree_io, logging_simple, regex_dna, sqlglot_parse, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, json_loads, coroutines, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 77.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x