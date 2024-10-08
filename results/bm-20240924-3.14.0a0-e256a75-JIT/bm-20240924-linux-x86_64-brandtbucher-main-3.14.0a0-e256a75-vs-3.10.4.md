# Results vs. 3.10.4

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                        |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                      |
| html5lib       | 88.9 ms                                                | 64.7 ms: 1.37x faster                                       |
| tornado_http   | 136 ms                                                 | 94.5 ms: 1.44x faster                                       |
| Geometric mean | (ref)                                                  | 1.29x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 317 ms: 2.30x faster                                        |
| async_tree_memoization  | 870 ms                                                 | 401 ms: 2.17x faster                                        |
| async_tree_io           | 1.77 sec                                               | 885 ms: 2.00x faster                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 573 ms: 1.77x faster                                        |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.3 ms: 1.93x faster                                       |
| float          | 117 ms                                                 | 69.2 ms: 1.69x faster                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                  | 1.50x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                        |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                       |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                        |
| regex_effbot   | 3.63 ms                                                | 3.83 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                      |
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                        |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                        |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                       |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                       |
| xml_etree_generate   | 99.4 ms                                                | 77.2 ms: 1.29x faster                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                        |
| json_loads           | 31.2 us                                                | 27.0 us: 1.15x faster                                       |
| pickle_list          | 5.08 us                                                | 5.16 us: 1.02x slower                                       |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                       |
| pickle_dict          | 29.6 us                                                | 34.3 us: 1.16x slower                                       |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                       |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.80 ms: 1.67x faster                                       |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                       |
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                       |
| genshi_xml      | 66.0 ms                                                | 57.3 ms: 1.15x faster                                       |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                        |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.47x faster                                       |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                       |
| async_tree_none          | 728 ms                                                 | 317 ms: 2.30x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 26.7 us: 2.19x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 401 ms: 2.17x faster                                        |
| richards_super           | 94.7 ms                                                | 45.2 ms: 2.10x faster                                       |
| richards                 | 79.3 ms                                                | 39.4 ms: 2.01x faster                                       |
| async_tree_io            | 1.77 sec                                               | 885 ms: 2.00x faster                                        |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                       |
| nbody                    | 154 ms                                                 | 79.3 ms: 1.93x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 66.4 ms: 1.92x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 61.9 ms: 1.91x faster                                       |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                        |
| asyncio_tcp              | 922 ms                                                 | 493 ms: 1.87x faster                                        |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                        |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                        |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                        |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 573 ms: 1.77x faster                                        |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                       |
| spectral_norm            | 170 ms                                                 | 100.0 ms: 1.70x faster                                      |
| float                    | 117 ms                                                 | 69.2 ms: 1.69x faster                                       |
| mako                     | 16.3 ms                                                | 9.80 ms: 1.67x faster                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                       |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                      |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                        |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                       |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.16 ms: 1.56x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                       |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.52x faster                                       |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                        |
| pylint                   | 551 ms                                                 | 371 ms: 1.49x faster                                        |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                       |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                       |
| tornado_http             | 136 ms                                                 | 94.5 ms: 1.44x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                      |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.43x faster                                        |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                       |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                       |
| html5lib                 | 88.9 ms                                                | 64.7 ms: 1.37x faster                                       |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                      |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 748 ms: 1.36x faster                                        |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                       |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                        |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                       |
| xml_etree_generate       | 99.4 ms                                                | 77.2 ms: 1.29x faster                                       |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                       |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                        |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                        |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.25x faster                                       |
| nqueens                  | 106 ms                                                 | 86.4 ms: 1.22x faster                                       |
| sqlglot_optimize         | 69.2 ms                                                | 58.0 ms: 1.19x faster                                       |
| bench_thread_pool        | 986 us                                                 | 835 us: 1.18x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                       |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                        |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                        |
| json_loads               | 31.2 us                                                | 27.0 us: 1.15x faster                                       |
| genshi_xml               | 66.0 ms                                                | 57.3 ms: 1.15x faster                                       |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                        |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                       |
| json                     | 5.69 ms                                                | 5.03 ms: 1.13x faster                                       |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                        |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                      |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                      |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                        |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                        |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                        |
| async_generators         | 444 ms                                                 | 450 ms: 1.01x slower                                        |
| pickle_list              | 5.08 us                                                | 5.16 us: 1.02x slower                                       |
| gc_traversal             | 3.62 ms                                                | 3.70 ms: 1.02x slower                                       |
| regex_effbot             | 3.63 ms                                                | 3.83 ms: 1.06x slower                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                       |
| coverage                 | 79.4 ms                                                | 85.6 ms: 1.08x slower                                       |
| telco                    | 7.27 ms                                                | 7.93 ms: 1.09x slower                                       |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                       |
| pickle_dict              | 29.6 us                                                | 34.3 us: 1.16x slower                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                       |
| unpack_sequence          | 60.0 ns                                                | 107 ns: 1.78x slower                                        |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.21x