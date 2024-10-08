# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_jump_backw
- machine: linux-x86_64
- commit hash: e448061
- commit date: 2024-08-29
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 290 ms: 1.20x faster                                                        |
| docutils       | 3.30 sec                                               | 3.58 sec: 1.09x slower                                                      |
| html5lib       | 88.9 ms                                                | 75.5 ms: 1.18x faster                                                       |
| tornado_http   | 136 ms                                                 | 120 ms: 1.14x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 347 ms: 2.10x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 437 ms: 1.99x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 966 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 581 ms: 1.75x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.91x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.3 ms: 1.91x faster                                                       |
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 147 ms: 1.28x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                       |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 288 us: 1.68x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                      |
| json_dumps           | 14.2 ms                                                | 9.97 ms: 1.42x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 81.4 ms: 1.22x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.15x faster                                                        |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.19 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                       |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                       |
| django_template | 48.2 ms                                                | 42.1 ms: 1.14x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 67.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                                        |
| generators               | 80.1 ms                                                | 34.5 ms: 2.32x faster                                                       |
| async_tree_none          | 728 ms                                                 | 347 ms: 2.10x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 58.9 ms: 2.01x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 437 ms: 1.99x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 65.7 ms: 1.95x faster                                                       |
| nbody                    | 154 ms                                                 | 80.3 ms: 1.91x faster                                                       |
| chaos                    | 115 ms                                                 | 62.6 ms: 1.84x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 966 ms: 1.83x faster                                                        |
| raytrace                 | 507 ms                                                 | 284 ms: 1.79x faster                                                        |
| deltablue                | 7.91 ms                                                | 4.46 ms: 1.77x faster                                                       |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 581 ms: 1.75x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 531 ms: 1.74x faster                                                        |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 288 us: 1.68x faster                                                        |
| logging_silent           | 190 ns                                                 | 113 ns: 1.67x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.67x faster                                                       |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                                       |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                                        |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.58x faster                                                        |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                        |
| scimark_fft              | 466 ms                                                 | 301 ms: 1.55x faster                                                        |
| richards_super           | 94.7 ms                                                | 62.0 ms: 1.53x faster                                                       |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.34 ms: 1.49x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 688 ms: 1.48x faster                                                        |
| richards                 | 79.3 ms                                                | 54.2 ms: 1.46x faster                                                       |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.86 us: 1.46x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.15 ms: 1.45x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                      |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.42x faster                                                        |
| json_dumps               | 14.2 ms                                                | 9.97 ms: 1.42x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.41x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.60 ms: 1.35x faster                                                       |
| go                       | 240 ms                                                 | 182 ms: 1.32x faster                                                        |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                       |
| thrift                   | 1.07 ms                                                | 831 us: 1.29x faster                                                        |
| regex_compile            | 188 ms                                                 | 147 ms: 1.28x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 2.02 ms: 1.27x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.4 ms: 1.22x faster                                                       |
| nqueens                  | 106 ms                                                 | 86.6 ms: 1.22x faster                                                       |
| logging_format           | 9.09 us                                                | 7.45 us: 1.22x faster                                                       |
| 2to3                     | 348 ms                                                 | 290 ms: 1.20x faster                                                        |
| logging_simple           | 8.30 us                                                | 6.91 us: 1.20x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.32 sec: 1.20x faster                                                      |
| html5lib                 | 88.9 ms                                                | 75.5 ms: 1.18x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.15x faster                                                        |
| django_template          | 48.2 ms                                                | 42.1 ms: 1.14x faster                                                       |
| tornado_http             | 136 ms                                                 | 120 ms: 1.14x faster                                                        |
| pylint                   | 551 ms                                                 | 486 ms: 1.13x faster                                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 128 ms: 1.12x faster                                                        |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                       |
| json                     | 5.69 ms                                                | 5.18 ms: 1.10x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 914 us: 1.08x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 66.3 ms: 1.04x faster                                                       |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| sympy_str                | 346 ms                                                 | 339 ms: 1.02x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.80 sec: 1.02x faster                                                      |
| bench_mp_pool            | 24.0 ms                                                | 24.1 ms: 1.00x slower                                                       |
| genshi_xml               | 66.0 ms                                                | 67.5 ms: 1.02x slower                                                       |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                       |
| regex_effbot             | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                       |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                                       |
| sympy_integrate          | 25.8 ms                                                | 27.3 ms: 1.06x slower                                                       |
| sympy_sum                | 196 ms                                                 | 213 ms: 1.08x slower                                                        |
| docutils                 | 3.30 sec                                               | 3.58 sec: 1.09x slower                                                      |
| coverage                 | 79.4 ms                                                | 87.4 ms: 1.10x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.81 ms: 1.12x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.19 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                |

Benchmark hidden because not significant (2): sympy_expand, asyncio_websockets
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-e448061-JIT/bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.28x