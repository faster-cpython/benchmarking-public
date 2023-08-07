
# Results vs. base

- fork: brandtbucher
- ref: uops_enabled
- machine: linux-x86_64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.06x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.93 sec                                                                    | 3.05 sec: 1.04x slower                                                    |
| tornado_http   | 121 ms                                                                      | 125 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 81.2 ms                                                                     | 86.9 ms: 1.07x slower                                                     |
| nbody          | 87.3 ms                                                                     | 98.3 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.06x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.68 ms                                                                     | 3.69 ms: 1.00x slower                                                     |
| regex_dna      | 246 ms                                                                      | 249 ms: 1.01x slower                                                      |
| regex_v8       | 23.6 ms                                                                     | 24.9 ms: 1.05x slower                                                     |
| regex_compile  | 152 ms                                                                      | 171 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.05x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle             | 15.3 us                                                                     | 14.8 us: 1.03x faster                                                     |
| unpickle_list        | 4.73 us                                                                     | 4.68 us: 1.01x faster                                                     |
| json_dumps           | 10.4 ms                                                                     | 10.4 ms: 1.00x slower                                                     |
| xml_etree_process    | 60.3 ms                                                                     | 60.8 ms: 1.01x slower                                                     |
| json_loads           | 25.4 us                                                                     | 25.9 us: 1.02x slower                                                     |
| xml_etree_parse      | 152 ms                                                                      | 155 ms: 1.02x slower                                                      |
| pickle               | 9.96 us                                                                     | 10.2 us: 1.02x slower                                                     |
| pickle_pure_python   | 317 us                                                                      | 329 us: 1.04x slower                                                      |
| xml_etree_generate   | 86.1 ms                                                                     | 90.0 ms: 1.05x slower                                                     |
| xml_etree_iterparse  | 107 ms                                                                      | 112 ms: 1.05x slower                                                      |
| unpickle_pure_python | 224 us                                                                      | 237 us: 1.06x slower                                                      |
| pickle_dict          | 31.8 us                                                                     | 33.8 us: 1.06x slower                                                     |
| pickle_list          | 4.17 us                                                                     | 4.54 us: 1.09x slower                                                     |
| tomli_loads          | 2.39 sec                                                                    | 2.84 sec: 1.19x slower                                                    |
| Geometric mean       | (ref)                                                                       | 1.04x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.63 ms                                                                     | 8.70 ms: 1.01x slower                                                     |
| python_startup         | 11.6 ms                                                                     | 11.7 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.4 ms                                                                     | 12.3 ms: 1.18x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| bench_mp_pool            | 4.80 ms                                                                     | 4.55 ms: 1.05x faster                                                     |
| unpickle                 | 15.3 us                                                                     | 14.8 us: 1.03x faster                                                     |
| coverage                 | 92.3 ms                                                                     | 90.8 ms: 1.02x faster                                                     |
| unpickle_list            | 4.73 us                                                                     | 4.68 us: 1.01x faster                                                     |
| deepcopy_reduce          | 3.53 us                                                                     | 3.51 us: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                    |
| json_dumps               | 10.4 ms                                                                     | 10.4 ms: 1.00x slower                                                     |
| regex_effbot             | 3.68 ms                                                                     | 3.69 ms: 1.00x slower                                                     |
| python_startup_no_site   | 8.63 ms                                                                     | 8.70 ms: 1.01x slower                                                     |
| sqlite_synth             | 2.76 us                                                                     | 2.78 us: 1.01x slower                                                     |
| python_startup           | 11.6 ms                                                                     | 11.7 ms: 1.01x slower                                                     |
| xml_etree_process        | 60.3 ms                                                                     | 60.8 ms: 1.01x slower                                                     |
| deepcopy                 | 391 us                                                                      | 395 us: 1.01x slower                                                      |
| async_generators         | 406 ms                                                                      | 410 ms: 1.01x slower                                                      |
| regex_dna                | 246 ms                                                                      | 249 ms: 1.01x slower                                                      |
| asyncio_tcp              | 370 ms                                                                      | 374 ms: 1.01x slower                                                      |
| pprint_pformat           | 1.69 sec                                                                    | 1.71 sec: 1.01x slower                                                    |
| async_tree_cpu_io_mixed  | 716 ms                                                                      | 727 ms: 1.02x slower                                                      |
| logging_simple           | 6.80 us                                                                     | 6.91 us: 1.02x slower                                                     |
| pprint_safe_repr         | 825 ms                                                                      | 839 ms: 1.02x slower                                                      |
| async_tree_io            | 1.08 sec                                                                    | 1.10 sec: 1.02x slower                                                    |
| json_loads               | 25.4 us                                                                     | 25.9 us: 1.02x slower                                                     |
| logging_silent           | 98.7 ns                                                                     | 101 ns: 1.02x slower                                                      |
| pathlib                  | 19.2 ms                                                                     | 19.6 ms: 1.02x slower                                                     |
| async_tree_memoization   | 567 ms                                                                      | 578 ms: 1.02x slower                                                      |
| xml_etree_parse          | 152 ms                                                                      | 155 ms: 1.02x slower                                                      |
| async_tree_none          | 468 ms                                                                      | 478 ms: 1.02x slower                                                      |
| unpack_sequence          | 54.5 ns                                                                     | 55.7 ns: 1.02x slower                                                     |
| dask                     | 590 ms                                                                      | 603 ms: 1.02x slower                                                      |
| json                     | 5.17 ms                                                                     | 5.29 ms: 1.02x slower                                                     |
| pickle                   | 9.96 us                                                                     | 10.2 us: 1.02x slower                                                     |
| logging_format           | 7.34 us                                                                     | 7.53 us: 1.03x slower                                                     |
| generators               | 37.0 ms                                                                     | 38.0 ms: 1.03x slower                                                     |
| create_gc_cycles         | 1.63 ms                                                                     | 1.67 ms: 1.03x slower                                                     |
| dulwich_log              | 68.6 ms                                                                     | 70.5 ms: 1.03x slower                                                     |
| tornado_http             | 121 ms                                                                      | 125 ms: 1.03x slower                                                      |
| scimark_sor              | 147 ms                                                                      | 151 ms: 1.03x slower                                                      |
| sqlglot_parse            | 1.44 ms                                                                     | 1.49 ms: 1.03x slower                                                     |
| telco                    | 8.02 ms                                                                     | 8.30 ms: 1.04x slower                                                     |
| sqlglot_transpile        | 1.84 ms                                                                     | 1.91 ms: 1.04x slower                                                     |
| mypy2                    | 372 ms                                                                      | 386 ms: 1.04x slower                                                      |
| bench_thread_pool        | 963 us                                                                      | 998 us: 1.04x slower                                                      |
| sqlglot_normalize        | 118 ms                                                                      | 122 ms: 1.04x slower                                                      |
| docutils                 | 2.93 sec                                                                    | 3.05 sec: 1.04x slower                                                    |
| pickle_pure_python       | 317 us                                                                      | 329 us: 1.04x slower                                                      |
| pycparser                | 1.32 sec                                                                    | 1.38 sec: 1.04x slower                                                    |
| xml_etree_generate       | 86.1 ms                                                                     | 90.0 ms: 1.05x slower                                                     |
| scimark_monte_carlo      | 67.9 ms                                                                     | 71.0 ms: 1.05x slower                                                     |
| xml_etree_iterparse      | 107 ms                                                                      | 112 ms: 1.05x slower                                                      |
| mdp                      | 2.57 sec                                                                    | 2.71 sec: 1.05x slower                                                    |
| typing_runtime_protocols | 151 us                                                                      | 159 us: 1.05x slower                                                      |
| regex_v8                 | 23.6 ms                                                                     | 24.9 ms: 1.05x slower                                                     |
| unpickle_pure_python     | 224 us                                                                      | 237 us: 1.06x slower                                                      |
| sqlglot_optimize         | 59.1 ms                                                                     | 62.5 ms: 1.06x slower                                                     |
| spectral_norm            | 94.9 ms                                                                     | 101 ms: 1.06x slower                                                      |
| pickle_dict              | 31.8 us                                                                     | 33.8 us: 1.06x slower                                                     |
| crypto_pyaes             | 72.9 ms                                                                     | 77.6 ms: 1.06x slower                                                     |
| float                    | 81.2 ms                                                                     | 86.9 ms: 1.07x slower                                                     |
| raytrace                 | 275 ms                                                                      | 295 ms: 1.07x slower                                                      |
| chaos                    | 63.0 ms                                                                     | 68.0 ms: 1.08x slower                                                     |
| deltablue                | 3.66 ms                                                                     | 3.96 ms: 1.08x slower                                                     |
| go                       | 173 ms                                                                      | 188 ms: 1.08x slower                                                      |
| pyflate                  | 514 ms                                                                      | 559 ms: 1.09x slower                                                      |
| meteor_contest           | 133 ms                                                                      | 144 ms: 1.09x slower                                                      |
| pickle_list              | 4.17 us                                                                     | 4.54 us: 1.09x slower                                                     |
| scimark_lu               | 98.5 ms                                                                     | 107 ms: 1.09x slower                                                      |
| gc_traversal             | 3.58 ms                                                                     | 3.92 ms: 1.10x slower                                                     |
| nbody                    | 87.3 ms                                                                     | 98.3 ms: 1.13x slower                                                     |
| regex_compile            | 152 ms                                                                      | 171 ms: 1.13x slower                                                      |
| deepcopy_memo            | 38.9 us                                                                     | 44.3 us: 1.14x slower                                                     |
| scimark_fft              | 306 ms                                                                      | 349 ms: 1.14x slower                                                      |
| mako                     | 10.4 ms                                                                     | 12.3 ms: 1.18x slower                                                     |
| tomli_loads              | 2.39 sec                                                                    | 2.84 sec: 1.19x slower                                                    |
| fannkuch                 | 389 ms                                                                      | 482 ms: 1.24x slower                                                      |
| nqueens                  | 91.5 ms                                                                     | 114 ms: 1.24x slower                                                      |
| comprehensions           | 21.9 us                                                                     | 27.9 us: 1.27x slower                                                     |
| hexiom                   | 6.47 ms                                                                     | 8.48 ms: 1.31x slower                                                     |
| scimark_sparse_mat_mult  | 4.17 ms                                                                     | 6.61 ms: 1.58x slower                                                     |
| Geometric mean           | (ref)                                                                       | 1.06x slower                                                              |

Benchmark hidden because not significant (4): richards_super, pidigits, coroutines, richards
