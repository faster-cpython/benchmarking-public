# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 4dc2c65
- commit date: 2024-08-12
- overall geometric mean: 1.41x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.24x faster                                                    |
| html5lib       | 88.9 ms                                                | 69.6 ms: 1.28x faster                                                   |
| tornado_http   | 136 ms                                                 | 95.3 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.22x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 421 ms: 2.07x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 903 ms: 1.96x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.3 ms: 1.91x faster                                                   |
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                                   |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.48x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 146 ms: 1.29x faster                                                    |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                   |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 203 us: 1.63x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 80.5 ms: 1.23x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                    |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.91 ms: 1.65x faster                                                   |
| django_template | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                   |
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 56.8 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.15 ms: 2.51x faster                                                   |
| richards_super           | 94.7 ms                                                | 40.2 ms: 2.35x faster                                                   |
| richards                 | 79.3 ms                                                | 35.2 ms: 2.25x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 26.0 us: 2.25x faster                                                   |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.22x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 421 ms: 2.07x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 903 ms: 1.96x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 65.5 ms: 1.95x faster                                                   |
| generators               | 80.1 ms                                                | 41.3 ms: 1.94x faster                                                   |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.92x faster                                                    |
| logging_silent           | 190 ns                                                 | 99.3 ns: 1.91x faster                                                   |
| nbody                    | 154 ms                                                 | 80.3 ms: 1.91x faster                                                   |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 64.6 ms: 1.83x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 515 ms: 1.79x faster                                                    |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                    |
| chaos                    | 115 ms                                                 | 65.3 ms: 1.77x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                   |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.70x faster                                                    |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                                   |
| mako                     | 16.3 ms                                                | 9.91 ms: 1.65x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 203 us: 1.63x faster                                                    |
| go                       | 240 ms                                                 | 149 ms: 1.61x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                  |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                    |
| pyflate                  | 716 ms                                                 | 453 ms: 1.58x faster                                                    |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.88 ms: 1.51x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.51x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.51x faster                                                   |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.46 ms: 1.49x faster                                                   |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                   |
| fannkuch                 | 532 ms                                                 | 365 ms: 1.46x faster                                                    |
| tornado_http             | 136 ms                                                 | 95.3 ms: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.84 ms: 1.40x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                   |
| pylint                   | 551 ms                                                 | 404 ms: 1.37x faster                                                    |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                  |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 759 ms: 1.34x faster                                                    |
| regex_compile            | 188 ms                                                 | 146 ms: 1.29x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                   |
| html5lib                 | 88.9 ms                                                | 69.6 ms: 1.28x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                   |
| nqueens                  | 106 ms                                                 | 83.6 ms: 1.27x faster                                                   |
| 2to3                     | 348 ms                                                 | 282 ms: 1.24x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 80.5 ms: 1.23x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 820 us: 1.20x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 120 ms: 1.19x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 56.8 ms: 1.16x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 60.3 ms: 1.15x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                    |
| json                     | 5.69 ms                                                | 5.04 ms: 1.13x faster                                                   |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                    |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                   |
| sympy_expand             | 566 ms                                                 | 519 ms: 1.09x faster                                                    |
| sympy_str                | 346 ms                                                 | 323 ms: 1.07x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.67 sec: 1.06x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 24.4 ms: 1.06x faster                                                   |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                    |
| sympy_sum                | 196 ms                                                 | 191 ms: 1.03x faster                                                    |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                    |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                   |
| telco                    | 7.27 ms                                                | 7.62 ms: 1.05x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                   |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                            |

Benchmark hidden because not significant (3): bench_mp_pool, asyncio_websockets, docutils
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240812-3.14.0a0-4dc2c65-JIT/bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.23x