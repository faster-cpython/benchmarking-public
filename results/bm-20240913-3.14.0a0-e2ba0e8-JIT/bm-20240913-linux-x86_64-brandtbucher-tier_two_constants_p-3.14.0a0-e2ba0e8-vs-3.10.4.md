# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_constants_p
- machine: linux-x86_64
- commit hash: e2ba0e8
- commit date: 2024-09-13
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                        |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                      |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.36x faster                                                       |
| tornado_http   | 136 ms                                                 | 95.1 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 320 ms: 2.27x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 400 ms: 2.18x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 888 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 577 ms: 1.76x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.7 ms: 1.88x faster                                                       |
| float          | 117 ms                                                 | 69.6 ms: 1.68x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                       |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 54.1 ms: 1.46x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 76.9 ms: 1.29x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                       |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.15x faster                                                        |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                                       |
| unpickle_list        | 5.20 us                                                | 5.34 us: 1.03x slower                                                       |
| pickle               | 10.7 us                                                | 11.8 us: 1.10x slower                                                       |
| pickle_dict          | 29.6 us                                                | 34.6 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                       |
| django_template | 48.2 ms                                                | 35.8 ms: 1.35x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.33x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                       |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                                       |
| async_tree_none          | 728 ms                                                 | 320 ms: 2.27x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 400 ms: 2.18x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.16x faster                                                       |
| richards_super           | 94.7 ms                                                | 45.1 ms: 2.10x faster                                                       |
| richards                 | 79.3 ms                                                | 39.6 ms: 2.00x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 888 ms: 1.99x faster                                                        |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 67.3 ms: 1.90x faster                                                       |
| nbody                    | 154 ms                                                 | 81.7 ms: 1.88x faster                                                       |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 63.3 ms: 1.87x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 502 ms: 1.84x faster                                                        |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                                        |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                        |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 577 ms: 1.76x faster                                                        |
| deepcopy                 | 479 us                                                 | 277 us: 1.73x faster                                                        |
| spectral_norm            | 170 ms                                                 | 99.6 ms: 1.71x faster                                                       |
| float                    | 117 ms                                                 | 69.6 ms: 1.68x faster                                                       |
| mako                     | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                       |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                       |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.60x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                      |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.51x faster                                                       |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.48x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.05 ms: 1.47x faster                                                       |
| pylint                   | 551 ms                                                 | 376 ms: 1.47x faster                                                        |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 54.1 ms: 1.46x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.46x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.47 ms: 1.45x faster                                                       |
| tornado_http             | 136 ms                                                 | 95.1 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                      |
| fannkuch                 | 532 ms                                                 | 374 ms: 1.42x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                                      |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.36x faster                                                       |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.35x faster                                                       |
| thrift                   | 1.07 ms                                                | 797 us: 1.35x faster                                                        |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 76.9 ms: 1.29x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                        |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 68.3 ms: 1.23x faster                                                       |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                       |
| nqueens                  | 106 ms                                                 | 86.5 ms: 1.22x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 58.7 ms: 1.18x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                       |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.15x faster                                                        |
| sympy_str                | 346 ms                                                 | 302 ms: 1.14x faster                                                        |
| json                     | 5.69 ms                                                | 5.02 ms: 1.13x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.12x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.12x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                       |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.12x faster                                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                        |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                       |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                        |
| pickle_list              | 5.08 us                                                | 5.11 us: 1.01x slower                                                       |
| unpickle_list            | 5.20 us                                                | 5.34 us: 1.03x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                       |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                        |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                       |
| pickle                   | 10.7 us                                                | 11.8 us: 1.10x slower                                                       |
| telco                    | 7.27 ms                                                | 8.07 ms: 1.11x slower                                                       |
| pickle_dict              | 29.6 us                                                | 34.6 us: 1.17x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                       |
| unpack_sequence          | 60.0 ns                                                | 108 ns: 1.80x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                                |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240913-3.14.0a0-e2ba0e8-JIT/bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.22x