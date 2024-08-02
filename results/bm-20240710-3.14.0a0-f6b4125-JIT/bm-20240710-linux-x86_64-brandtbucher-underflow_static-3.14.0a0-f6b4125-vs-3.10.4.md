# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: f6b4125
- commit date: 2024-07-10
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                    |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.13x faster                                                  |
| html5lib       | 88.9 ms                                                | 63.1 ms: 1.41x faster                                                   |
| tornado_http   | 136 ms                                                 | 92.6 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 409 ms: 2.13x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 856 ms: 2.07x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.0 ms: 1.92x faster                                                   |
| float          | 117 ms                                                 | 69.9 ms: 1.68x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.49x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.38x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                   |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                    |
| regex_effbot   | 3.63 ms                                                | 4.02 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 292 us: 1.66x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 207 us: 1.60x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 57.1 ms: 1.38x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 81.6 ms: 1.22x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                    |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.91 ms: 1.65x faster                                                   |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                   |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 58.7 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                    |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                   |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.60 ms: 2.20x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 27.4 us: 2.13x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 409 ms: 2.13x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 856 ms: 2.07x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 58.5 ms: 2.02x faster                                                   |
| richards_super           | 94.7 ms                                                | 48.0 ms: 1.97x faster                                                   |
| richards                 | 79.3 ms                                                | 40.9 ms: 1.94x faster                                                   |
| logging_silent           | 190 ns                                                 | 98.0 ns: 1.94x faster                                                   |
| nbody                    | 154 ms                                                 | 80.0 ms: 1.92x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 67.0 ms: 1.91x faster                                                   |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                    |
| chaos                    | 115 ms                                                 | 61.7 ms: 1.87x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                    |
| deepcopy                 | 479 us                                                 | 271 us: 1.76x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                   |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                    |
| float                    | 117 ms                                                 | 69.9 ms: 1.68x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 292 us: 1.66x faster                                                    |
| mako                     | 16.3 ms                                                | 9.91 ms: 1.65x faster                                                   |
| go                       | 240 ms                                                 | 146 ms: 1.65x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                  |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                    |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                   |
| pylint                   | 551 ms                                                 | 344 ms: 1.60x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 207 us: 1.60x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.65 ms: 1.56x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                   |
| logging_format           | 9.09 us                                                | 6.02 us: 1.51x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                   |
| tornado_http             | 136 ms                                                 | 92.6 ms: 1.47x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.43 sec: 1.47x faster                                                  |
| fannkuch                 | 532 ms                                                 | 362 ms: 1.47x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 697 ms: 1.46x faster                                                    |
| scimark_fft              | 466 ms                                                 | 320 ms: 1.46x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.53 ms: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                  |
| html5lib                 | 88.9 ms                                                | 63.1 ms: 1.41x faster                                                   |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.39x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 57.1 ms: 1.38x faster                                                   |
| regex_compile            | 188 ms                                                 | 136 ms: 1.38x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                   |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                   |
| thrift                   | 1.07 ms                                                | 801 us: 1.34x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                    |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                    |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 67.0 ms: 1.26x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 55.3 ms: 1.25x faster                                                   |
| nqueens                  | 106 ms                                                 | 85.1 ms: 1.24x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 81.6 ms: 1.22x faster                                                   |
| dask                     | 441 ms                                                 | 363 ms: 1.21x faster                                                    |
| sympy_sum                | 196 ms                                                 | 164 ms: 1.19x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 829 us: 1.19x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.0 ms: 1.17x faster                                                   |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                    |
| sympy_expand             | 566 ms                                                 | 496 ms: 1.14x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.13x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.12x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 58.7 ms: 1.12x faster                                                   |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                   |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                    |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                    |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                    |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                   |
| telco                    | 7.27 ms                                                | 8.00 ms: 1.10x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 4.02 ms: 1.11x slower                                                   |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                            |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240710-3.14.0a0-f6b4125-JIT/bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x