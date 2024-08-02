# Results vs. 3.10.4

- fork: saulshanabrook
- ref: optimzer_type_versio
- machine: linux-x86_64
- commit hash: 1520928
- commit date: 2024-05-20
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                                          |
| chameleon      | 9.68 ms                                                | 7.04 ms: 1.38x faster                                                         |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                        |
| html5lib       | 88.9 ms                                                | 68.4 ms: 1.30x faster                                                         |
| tornado_http   | 136 ms                                                 | 97.0 ms: 1.41x faster                                                         |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 382 ms: 1.91x faster                                                          |
| async_tree_io           | 1.77 sec                                               | 941 ms: 1.88x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 467 ms: 1.86x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 617 ms: 1.65x faster                                                          |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.3 ms: 1.89x faster                                                         |
| float          | 117 ms                                                 | 72.4 ms: 1.62x faster                                                         |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                                          |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                         |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                          |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.0 ms: 1.20x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                          |
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                                          |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                         |
| unpickle_list        | 5.20 us                                                | 5.33 us: 1.03x slower                                                         |
| pickle_list          | 5.08 us                                                | 5.38 us: 1.06x slower                                                         |
| pickle               | 10.7 us                                                | 12.1 us: 1.14x slower                                                         |
| unpickle             | 14.4 us                                                | 16.7 us: 1.16x slower                                                         |
| pickle_dict          | 29.6 us                                                | 36.1 us: 1.22x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.33x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.63 ms: 1.29x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.99 ms: 1.63x faster                                                         |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                         |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                          |
| generators               | 80.1 ms                                                | 30.3 ms: 2.64x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.75 ms: 2.11x faster                                                         |
| richards_super           | 94.7 ms                                                | 47.5 ms: 2.00x faster                                                         |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                                         |
| richards                 | 79.3 ms                                                | 41.3 ms: 1.92x faster                                                         |
| async_tree_none          | 728 ms                                                 | 382 ms: 1.91x faster                                                          |
| nbody                    | 154 ms                                                 | 81.3 ms: 1.89x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 62.7 ms: 1.89x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 941 ms: 1.88x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 68.5 ms: 1.86x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 467 ms: 1.86x faster                                                          |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                          |
| logging_silent           | 190 ns                                                 | 108 ns: 1.75x faster                                                          |
| asyncio_tcp              | 922 ms                                                 | 526 ms: 1.75x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                         |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.70x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 617 ms: 1.65x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                          |
| mako                     | 16.3 ms                                                | 9.99 ms: 1.63x faster                                                         |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                          |
| float                    | 117 ms                                                 | 72.4 ms: 1.62x faster                                                         |
| scimark_sor              | 220 ms                                                 | 137 ms: 1.61x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                         |
| pylint                   | 551 ms                                                 | 355 ms: 1.55x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 37.7 us: 1.55x faster                                                         |
| pyflate                  | 716 ms                                                 | 470 ms: 1.52x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                                          |
| fannkuch                 | 532 ms                                                 | 361 ms: 1.47x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                         |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                                          |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 701 ms: 1.45x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                        |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                                         |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.43x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.54 ms: 1.43x faster                                                         |
| tornado_http             | 136 ms                                                 | 97.0 ms: 1.41x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                        |
| chameleon                | 9.68 ms                                                | 7.04 ms: 1.38x faster                                                         |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                         |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.33x faster                                                         |
| deepcopy                 | 479 us                                                 | 364 us: 1.32x faster                                                          |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                         |
| thrift                   | 1.07 ms                                                | 816 us: 1.31x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                        |
| html5lib                 | 88.9 ms                                                | 68.4 ms: 1.30x faster                                                         |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 3.28 us: 1.27x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                                          |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                                          |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                         |
| nqueens                  | 106 ms                                                 | 85.9 ms: 1.23x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 69.5 ms: 1.21x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 57.0 ms: 1.21x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.0 ms: 1.20x faster                                                         |
| dask                     | 441 ms                                                 | 380 ms: 1.16x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                         |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 865 us: 1.14x faster                                                          |
| sympy_str                | 346 ms                                                 | 303 ms: 1.14x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                        |
| sympy_expand             | 566 ms                                                 | 512 ms: 1.11x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                                          |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                          |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                         |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                         |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 568 ms: 1.02x slower                                                          |
| unpickle_list            | 5.20 us                                                | 5.33 us: 1.03x slower                                                         |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                          |
| pickle_list              | 5.08 us                                                | 5.38 us: 1.06x slower                                                         |
| flaskblogging            | 8.58 ms                                                | 9.22 ms: 1.08x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 3.92 ms: 1.08x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.82 ms: 1.12x slower                                                         |
| telco                    | 7.27 ms                                                | 8.23 ms: 1.13x slower                                                         |
| pickle                   | 10.7 us                                                | 12.1 us: 1.14x slower                                                         |
| unpickle                 | 14.4 us                                                | 16.7 us: 1.16x slower                                                         |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                         |
| pickle_dict              | 29.6 us                                                | 36.1 us: 1.22x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.63 ms: 1.29x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                                  |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, hexiom, mdp, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240520-3.14.0a0-1520928-JIT/bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.20x