# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: e666b14
- commit date: 2024-09-08
- overall geometric mean: 1.393x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 288 ms: 1.21x faster                                                        |
| docutils       | 3.30 sec                                               | 3.23 sec: 1.02x faster                                                      |
| html5lib       | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                       |
| tornado_http   | 136 ms                                                 | 104 ms: 1.31x faster                                                        |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 416 ms: 2.09x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 938 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.7 ms: 1.90x faster                                                       |
| float          | 117 ms                                                 | 71.4 ms: 1.64x faster                                                       |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.47x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 154 ms: 1.22x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                       |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 201 us: 1.65x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 330 us: 1.47x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 53.9 ms: 1.47x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 77.2 ms: 1.29x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                        |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                       |
| unpickle             | 14.4 us                                                | 14.9 us: 1.03x slower                                                       |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                       |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                       |
| pickle_dict          | 29.6 us                                                | 34.7 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.75 ms: 1.67x faster                                                       |
| genshi_text     | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                       |
| django_template | 48.2 ms                                                | 37.8 ms: 1.27x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 58.7 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                       |
| generators               | 80.1 ms                                                | 33.2 ms: 2.41x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 25.2 us: 2.32x faster                                                       |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                        |
| richards_super           | 94.7 ms                                                | 44.3 ms: 2.14x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 416 ms: 2.09x faster                                                        |
| richards                 | 79.3 ms                                                | 39.4 ms: 2.01x faster                                                       |
| chaos                    | 115 ms                                                 | 57.5 ms: 2.01x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 66.5 ms: 1.92x faster                                                       |
| nbody                    | 154 ms                                                 | 80.7 ms: 1.90x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 938 ms: 1.89x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 506 ms: 1.82x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                        |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                        |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                        |
| raytrace                 | 507 ms                                                 | 284 ms: 1.79x faster                                                        |
| go                       | 240 ms                                                 | 135 ms: 1.77x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                       |
| logging_silent           | 190 ns                                                 | 109 ns: 1.73x faster                                                        |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.70x faster                                                        |
| mako                     | 16.3 ms                                                | 9.75 ms: 1.67x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 71.4 ms: 1.66x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.65x faster                                                        |
| float                    | 117 ms                                                 | 71.4 ms: 1.64x faster                                                       |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                                        |
| pyflate                  | 716 ms                                                 | 458 ms: 1.56x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                       |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                      |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.75 ms: 1.47x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 330 us: 1.47x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 53.9 ms: 1.47x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.41 ms: 1.47x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.49 ms: 1.45x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                      |
| logging_format           | 9.09 us                                                | 6.36 us: 1.43x faster                                                       |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.43x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.89 us: 1.41x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.42 ms: 1.40x faster                                                       |
| genshi_text              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 746 ms: 1.36x faster                                                        |
| pylint                   | 551 ms                                                 | 412 ms: 1.34x faster                                                        |
| html5lib                 | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                       |
| tornado_http             | 136 ms                                                 | 104 ms: 1.31x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 77.2 ms: 1.29x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                       |
| django_template          | 48.2 ms                                                | 37.8 ms: 1.27x faster                                                       |
| nqueens                  | 106 ms                                                 | 84.0 ms: 1.26x faster                                                       |
| regex_compile            | 188 ms                                                 | 154 ms: 1.22x faster                                                        |
| 2to3                     | 348 ms                                                 | 288 ms: 1.21x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.32 sec: 1.19x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 121 ms: 1.18x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 58.7 ms: 1.13x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 61.6 ms: 1.12x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 75.4 ms: 1.12x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                       |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                       |
| sympy_str                | 346 ms                                                 | 322 ms: 1.07x faster                                                        |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                        |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                                       |
| sympy_expand             | 566 ms                                                 | 533 ms: 1.06x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 24.9 ms: 1.04x faster                                                       |
| sympy_sum                | 196 ms                                                 | 190 ms: 1.03x faster                                                        |
| docutils                 | 3.30 sec                                               | 3.23 sec: 1.02x faster                                                      |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                        |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                        |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.03x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                                       |
| pickle_list              | 5.08 us                                                | 5.29 us: 1.04x slower                                                       |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                                       |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                       |
| telco                    | 7.27 ms                                                | 8.02 ms: 1.10x slower                                                       |
| pickle_dict              | 29.6 us                                                | 34.7 us: 1.17x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                       |
| unpack_sequence          | 60.0 ns                                                | 145 ns: 2.41x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                                |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240908-3.14.0a0-e666b14-JIT/bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.393x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.27x