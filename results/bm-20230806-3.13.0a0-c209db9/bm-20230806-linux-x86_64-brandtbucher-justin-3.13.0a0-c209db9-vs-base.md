
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.75 sec: 1.04x slower                                        |
| tornado_http   | 95.0 ms                                                               | 97.3 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 97.1 ms                                                               | 102 ms: 1.05x slower                                          |
| float          | 80.0 ms                                                               | 84.4 ms: 1.06x slower                                         |
| pidigits       | 189 ms                                                                | 200 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.69 ms                                                               | 3.39 ms: 1.09x faster                                         |
| regex_dna      | 215 ms                                                                | 200 ms: 1.07x faster                                          |
| regex_v8       | 23.1 ms                                                               | 22.0 ms: 1.05x faster                                         |
| regex_compile  | 137 ms                                                                | 150 ms: 1.09x slower                                          |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle               | 10.8 us                                                               | 10.5 us: 1.03x faster                                         |
| json_loads           | 25.6 us                                                               | 25.4 us: 1.01x faster                                         |
| unpickle_list        | 4.90 us                                                               | 4.96 us: 1.01x slower                                         |
| unpickle             | 14.9 us                                                               | 15.1 us: 1.01x slower                                         |
| pickle_pure_python   | 294 us                                                                | 300 us: 1.02x slower                                          |
| xml_etree_process    | 57.7 ms                                                               | 59.0 ms: 1.02x slower                                         |
| json_dumps           | 9.67 ms                                                               | 9.89 ms: 1.02x slower                                         |
| xml_etree_iterparse  | 103 ms                                                                | 106 ms: 1.03x slower                                          |
| xml_etree_generate   | 83.4 ms                                                               | 86.1 ms: 1.03x slower                                         |
| unpickle_pure_python | 212 us                                                                | 222 us: 1.05x slower                                          |
| tomli_loads          | 2.31 sec                                                              | 2.58 sec: 1.12x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (3): pickle_list, xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 9.37 ms                                                               | 9.39 ms: 1.00x slower                                         |
| python_startup_no_site | 6.85 ms                                                               | 6.88 ms: 1.00x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.9 ms                                                               | 12.1 ms: 1.11x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot             | 3.69 ms                                                               | 3.39 ms: 1.09x faster                                         |
| regex_dna                | 215 ms                                                                | 200 ms: 1.07x faster                                          |
| regex_v8                 | 23.1 ms                                                               | 22.0 ms: 1.05x faster                                         |
| pickle                   | 10.8 us                                                               | 10.5 us: 1.03x faster                                         |
| spectral_norm            | 111 ms                                                                | 109 ms: 1.02x faster                                          |
| json_loads               | 25.6 us                                                               | 25.4 us: 1.01x faster                                         |
| python_startup           | 9.37 ms                                                               | 9.39 ms: 1.00x slower                                         |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                        |
| python_startup_no_site   | 6.85 ms                                                               | 6.88 ms: 1.00x slower                                         |
| logging_format           | 6.52 us                                                               | 6.56 us: 1.00x slower                                         |
| logging_simple           | 5.99 us                                                               | 6.01 us: 1.00x slower                                         |
| create_gc_cycles         | 1.50 ms                                                               | 1.51 ms: 1.01x slower                                         |
| asyncio_tcp              | 486 ms                                                                | 490 ms: 1.01x slower                                          |
| json                     | 4.82 ms                                                               | 4.86 ms: 1.01x slower                                         |
| async_tree_io            | 1.18 sec                                                              | 1.19 sec: 1.01x slower                                        |
| scimark_sor              | 123 ms                                                                | 125 ms: 1.01x slower                                          |
| unpickle_list            | 4.90 us                                                               | 4.96 us: 1.01x slower                                         |
| unpickle                 | 14.9 us                                                               | 15.1 us: 1.01x slower                                         |
| deepcopy_reduce          | 3.15 us                                                               | 3.20 us: 1.02x slower                                         |
| async_tree_memoization   | 584 ms                                                                | 594 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed  | 717 ms                                                                | 732 ms: 1.02x slower                                          |
| pathlib                  | 18.7 ms                                                               | 19.1 ms: 1.02x slower                                         |
| pickle_pure_python       | 294 us                                                                | 300 us: 1.02x slower                                          |
| scimark_monte_carlo      | 67.4 ms                                                               | 68.9 ms: 1.02x slower                                         |
| raytrace                 | 274 ms                                                                | 280 ms: 1.02x slower                                          |
| deepcopy                 | 354 us                                                                | 362 us: 1.02x slower                                          |
| xml_etree_process        | 57.7 ms                                                               | 59.0 ms: 1.02x slower                                         |
| json_dumps               | 9.67 ms                                                               | 9.89 ms: 1.02x slower                                         |
| sqlite_synth             | 2.74 us                                                               | 2.80 us: 1.02x slower                                         |
| tornado_http             | 95.0 ms                                                               | 97.3 ms: 1.02x slower                                         |
| dulwich_log              | 65.5 ms                                                               | 67.2 ms: 1.03x slower                                         |
| sqlglot_parse            | 1.29 ms                                                               | 1.32 ms: 1.03x slower                                         |
| dask                     | 518 ms                                                                | 532 ms: 1.03x slower                                          |
| async_tree_none          | 480 ms                                                                | 493 ms: 1.03x slower                                          |
| sqlglot_transpile        | 1.60 ms                                                               | 1.65 ms: 1.03x slower                                         |
| xml_etree_iterparse      | 103 ms                                                                | 106 ms: 1.03x slower                                          |
| generators               | 28.2 ms                                                               | 29.1 ms: 1.03x slower                                         |
| telco                    | 7.80 ms                                                               | 8.05 ms: 1.03x slower                                         |
| xml_etree_generate       | 83.4 ms                                                               | 86.1 ms: 1.03x slower                                         |
| richards                 | 47.0 ms                                                               | 48.7 ms: 1.04x slower                                         |
| sqlglot_normalize        | 104 ms                                                                | 108 ms: 1.04x slower                                          |
| docutils                 | 2.65 sec                                                              | 2.75 sec: 1.04x slower                                        |
| pycparser                | 1.15 sec                                                              | 1.19 sec: 1.04x slower                                        |
| richards_super           | 53.8 ms                                                               | 55.9 ms: 1.04x slower                                         |
| async_generators         | 447 ms                                                                | 466 ms: 1.04x slower                                          |
| pprint_safe_repr         | 711 ms                                                                | 741 ms: 1.04x slower                                          |
| typing_runtime_protocols | 146 us                                                                | 152 us: 1.04x slower                                          |
| sqlglot_optimize         | 52.4 ms                                                               | 54.6 ms: 1.04x slower                                         |
| mypy2                    | 335 ms                                                                | 350 ms: 1.04x slower                                          |
| pprint_pformat           | 1.46 sec                                                              | 1.52 sec: 1.04x slower                                        |
| bench_thread_pool        | 826 us                                                                | 864 us: 1.05x slower                                          |
| crypto_pyaes             | 70.5 ms                                                               | 73.8 ms: 1.05x slower                                         |
| unpickle_pure_python     | 212 us                                                                | 222 us: 1.05x slower                                          |
| nbody                    | 97.1 ms                                                               | 102 ms: 1.05x slower                                          |
| scimark_lu               | 112 ms                                                                | 118 ms: 1.05x slower                                          |
| float                    | 80.0 ms                                                               | 84.4 ms: 1.06x slower                                         |
| gc_traversal             | 3.77 ms                                                               | 3.99 ms: 1.06x slower                                         |
| pidigits                 | 189 ms                                                                | 200 ms: 1.06x slower                                          |
| deltablue                | 3.20 ms                                                               | 3.42 ms: 1.07x slower                                         |
| go                       | 137 ms                                                                | 147 ms: 1.07x slower                                          |
| chaos                    | 60.8 ms                                                               | 65.5 ms: 1.08x slower                                         |
| scimark_fft              | 355 ms                                                                | 385 ms: 1.08x slower                                          |
| meteor_contest           | 106 ms                                                                | 115 ms: 1.09x slower                                          |
| pyflate                  | 444 ms                                                                | 485 ms: 1.09x slower                                          |
| regex_compile            | 137 ms                                                                | 150 ms: 1.09x slower                                          |
| deepcopy_memo            | 37.8 us                                                               | 41.9 us: 1.11x slower                                         |
| mako                     | 10.9 ms                                                               | 12.1 ms: 1.11x slower                                         |
| unpack_sequence          | 44.7 ns                                                               | 49.8 ns: 1.11x slower                                         |
| mdp                      | 2.54 sec                                                              | 2.83 sec: 1.12x slower                                        |
| tomli_loads              | 2.31 sec                                                              | 2.58 sec: 1.12x slower                                        |
| fannkuch                 | 393 ms                                                                | 468 ms: 1.19x slower                                          |
| scimark_sparse_mat_mult  | 4.75 ms                                                               | 5.70 ms: 1.20x slower                                         |
| comprehensions           | 20.5 us                                                               | 25.0 us: 1.22x slower                                         |
| nqueens                  | 79.6 ms                                                               | 98.9 ms: 1.24x slower                                         |
| hexiom                   | 5.98 ms                                                               | 7.61 ms: 1.27x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.04x slower                                                  |

Benchmark hidden because not significant (7): pickle_list, logging_silent, xml_etree_parse, bench_mp_pool, coverage, coroutines, pickle_dict
