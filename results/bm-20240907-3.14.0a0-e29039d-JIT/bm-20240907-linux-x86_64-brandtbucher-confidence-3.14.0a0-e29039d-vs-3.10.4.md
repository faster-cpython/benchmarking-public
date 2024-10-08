# Results vs. 3.10.4

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: e29039d
- commit date: 2024-09-07
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                              |
| docutils       | 3.30 sec                                               | 3.01 sec: 1.10x faster                                            |
| html5lib       | 88.9 ms                                                | 64.3 ms: 1.38x faster                                             |
| tornado_http   | 136 ms                                                 | 94.9 ms: 1.44x faster                                             |
| Geometric mean | (ref)                                                  | 1.29x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 394 ms: 2.21x faster                                              |
| async_tree_io           | 1.77 sec                                               | 932 ms: 1.90x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                              |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.5 ms: 1.93x faster                                             |
| float          | 117 ms                                                 | 70.3 ms: 1.67x faster                                             |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.49x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.35x faster                                              |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                             |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                            |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                              |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 54.8 ms: 1.44x faster                                             |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 77.3 ms: 1.29x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                              |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                             |
| unpickle             | 14.4 us                                                | 15.0 us: 1.04x slower                                             |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                             |
| pickle_dict          | 29.6 us                                                | 34.8 us: 1.18x slower                                             |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                      |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                             |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.84 ms: 1.66x faster                                             |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                             |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.33x faster                                             |
| genshi_xml      | 66.0 ms                                                | 56.7 ms: 1.16x faster                                             |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                              |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                             |
| generators               | 80.1 ms                                                | 32.9 ms: 2.43x faster                                             |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 394 ms: 2.21x faster                                              |
| richards_super           | 94.7 ms                                                | 43.0 ms: 2.20x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 26.8 us: 2.18x faster                                             |
| richards                 | 79.3 ms                                                | 38.9 ms: 2.04x faster                                             |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 66.0 ms: 1.94x faster                                             |
| nbody                    | 154 ms                                                 | 79.5 ms: 1.93x faster                                             |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.92x faster                                              |
| async_tree_io            | 1.77 sec                                               | 932 ms: 1.90x faster                                              |
| asyncio_tcp              | 922 ms                                                 | 488 ms: 1.89x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 63.1 ms: 1.87x faster                                             |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                              |
| go                       | 240 ms                                                 | 130 ms: 1.85x faster                                              |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                              |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                              |
| spectral_norm            | 170 ms                                                 | 98.6 ms: 1.72x faster                                             |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                             |
| float                    | 117 ms                                                 | 70.3 ms: 1.67x faster                                             |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                              |
| mako                     | 16.3 ms                                                | 9.84 ms: 1.66x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.64x faster                                             |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                              |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                              |
| coroutines               | 35.1 ms                                                | 22.3 ms: 1.58x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                             |
| hexiom                   | 10.4 ms                                                | 6.83 ms: 1.52x faster                                             |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                              |
| pylint                   | 551 ms                                                 | 371 ms: 1.49x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.36 ms: 1.48x faster                                             |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                             |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 54.8 ms: 1.44x faster                                             |
| tornado_http             | 136 ms                                                 | 94.9 ms: 1.44x faster                                             |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.43x faster                                              |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 718 ms: 1.42x faster                                              |
| html5lib                 | 88.9 ms                                                | 64.3 ms: 1.38x faster                                             |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                             |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                              |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                             |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                             |
| regex_compile            | 188 ms                                                 | 139 ms: 1.35x faster                                              |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.33x faster                                             |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 77.3 ms: 1.29x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                              |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                             |
| nqueens                  | 106 ms                                                 | 85.5 ms: 1.24x faster                                             |
| dulwich_log              | 84.3 ms                                                | 68.6 ms: 1.23x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 57.9 ms: 1.19x faster                                             |
| bench_thread_pool        | 986 us                                                 | 836 us: 1.18x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                             |
| genshi_xml               | 66.0 ms                                                | 56.7 ms: 1.16x faster                                             |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                              |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.15x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                             |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                              |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                             |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                             |
| docutils                 | 3.30 sec                                               | 3.01 sec: 1.10x faster                                            |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.10x faster                                            |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                             |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                              |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                              |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                              |
| gc_traversal             | 3.62 ms                                                | 3.74 ms: 1.03x slower                                             |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                             |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.04x slower                                             |
| telco                    | 7.27 ms                                                | 7.81 ms: 1.07x slower                                             |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                             |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                             |
| pickle_dict              | 29.6 us                                                | 34.8 us: 1.18x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                             |
| unpack_sequence          | 60.0 ns                                                | 107 ns: 1.78x slower                                              |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                      |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240907-3.14.0a0-e29039d-JIT/bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.22x