# Results vs. 3.10.4

- fork: brandtbucher
- ref: hoist
- machine: linux-x86_64
- commit hash: 5e272c0
- commit date: 2024-05-09
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                         |
| chameleon      | 9.68 ms                                                | 7.17 ms: 1.35x faster                                        |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                       |
| html5lib       | 88.9 ms                                                | 69.2 ms: 1.28x faster                                        |
| tornado_http   | 136 ms                                                 | 97.9 ms: 1.39x faster                                        |
| Geometric mean | (ref)                                                  | 1.27x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 368 ms: 1.98x faster                                         |
| async_tree_io           | 1.77 sec                                               | 936 ms: 1.89x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 480 ms: 1.81x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 623 ms: 1.63x faster                                         |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.0 ms: 1.90x faster                                        |
| float          | 117 ms                                                 | 71.3 ms: 1.64x faster                                        |
| pidigits       | 191 ms                                                 | 197 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                  | 1.45x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.35x faster                                         |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                        |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.82 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                       |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.60x faster                                         |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                         |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                        |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 83.4 ms: 1.19x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.14x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                         |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                        |
| pickle_list          | 5.08 us                                                | 5.47 us: 1.08x slower                                        |
| unpickle             | 14.4 us                                                | 16.0 us: 1.11x slower                                        |
| pickle               | 10.7 us                                                | 12.2 us: 1.15x slower                                        |
| pickle_dict          | 29.6 us                                                | 34.2 us: 1.15x slower                                        |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.32x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 7.65 ms: 1.29x slower                                        |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.53 ms: 1.71x faster                                        |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                        |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.29x faster                                        |
| genshi_xml      | 66.0 ms                                                | 57.4 ms: 1.15x faster                                        |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 176 us: 3.10x faster                                         |
| generators               | 80.1 ms                                                | 29.9 ms: 2.67x faster                                        |
| deltablue                | 7.91 ms                                                | 3.74 ms: 2.12x faster                                        |
| async_tree_none          | 728 ms                                                 | 368 ms: 1.98x faster                                         |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                        |
| richards_super           | 94.7 ms                                                | 48.7 ms: 1.94x faster                                        |
| nbody                    | 154 ms                                                 | 81.0 ms: 1.90x faster                                        |
| async_tree_io            | 1.77 sec                                               | 936 ms: 1.89x faster                                         |
| richards                 | 79.3 ms                                                | 42.6 ms: 1.86x faster                                        |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 69.4 ms: 1.84x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 64.5 ms: 1.83x faster                                        |
| async_tree_memoization   | 870 ms                                                 | 480 ms: 1.81x faster                                         |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                         |
| asyncio_tcp              | 922 ms                                                 | 521 ms: 1.77x faster                                         |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                        |
| spectral_norm            | 170 ms                                                 | 99.0 ms: 1.72x faster                                        |
| mako                     | 16.3 ms                                                | 9.53 ms: 1.71x faster                                        |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.71x faster                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                        |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                         |
| float                    | 117 ms                                                 | 71.3 ms: 1.64x faster                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 623 ms: 1.63x faster                                         |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                         |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                       |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.60x faster                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 37.5 us: 1.56x faster                                        |
| pylint                   | 551 ms                                                 | 357 ms: 1.55x faster                                         |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.85 ms: 1.52x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                         |
| fannkuch                 | 532 ms                                                 | 365 ms: 1.46x faster                                         |
| scimark_fft              | 466 ms                                                 | 323 ms: 1.44x faster                                         |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.56 ms: 1.42x faster                                        |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                         |
| logging_format           | 9.09 us                                                | 6.48 us: 1.40x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                       |
| tornado_http             | 136 ms                                                 | 97.9 ms: 1.39x faster                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                       |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                        |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                        |
| regex_compile            | 188 ms                                                 | 139 ms: 1.35x faster                                         |
| chameleon                | 9.68 ms                                                | 7.17 ms: 1.35x faster                                        |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                        |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.32x faster                                        |
| thrift                   | 1.07 ms                                                | 814 us: 1.32x faster                                         |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                       |
| deepcopy                 | 479 us                                                 | 369 us: 1.30x faster                                         |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.29x faster                                        |
| html5lib                 | 88.9 ms                                                | 69.2 ms: 1.28x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 3.26 us: 1.28x faster                                        |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                         |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                         |
| sqlglot_optimize         | 69.2 ms                                                | 57.1 ms: 1.21x faster                                        |
| nqueens                  | 106 ms                                                 | 87.7 ms: 1.21x faster                                        |
| dulwich_log              | 84.3 ms                                                | 70.5 ms: 1.20x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 83.4 ms: 1.19x faster                                        |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                         |
| genshi_xml               | 66.0 ms                                                | 57.4 ms: 1.15x faster                                        |
| aiohttp                  | 1.44 ms                                                | 1.25 ms: 1.15x faster                                        |
| pathlib                  | 20.5 ms                                                | 17.9 ms: 1.15x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.14x faster                                         |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                         |
| bench_thread_pool        | 986 us                                                 | 869 us: 1.13x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                        |
| gunicorn                 | 1.53 ms                                                | 1.36 ms: 1.13x faster                                        |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                         |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.11x faster                                         |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                       |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                         |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                        |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                        |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                        |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                         |
| mdp                      | 2.85 sec                                               | 2.81 sec: 1.01x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                         |
| pidigits                 | 191 ms                                                 | 197 ms: 1.03x slower                                         |
| regex_effbot             | 3.63 ms                                                | 3.82 ms: 1.05x slower                                        |
| async_generators         | 444 ms                                                 | 472 ms: 1.06x slower                                         |
| pickle_list              | 5.08 us                                                | 5.47 us: 1.08x slower                                        |
| flaskblogging            | 8.58 ms                                                | 9.32 ms: 1.09x slower                                        |
| coverage                 | 79.4 ms                                                | 87.1 ms: 1.10x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.01 ms: 1.11x slower                                        |
| unpickle                 | 14.4 us                                                | 16.0 us: 1.11x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.82 ms: 1.12x slower                                        |
| pickle                   | 10.7 us                                                | 12.2 us: 1.15x slower                                        |
| pickle_dict              | 29.6 us                                                | 34.2 us: 1.15x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.65 ms: 1.29x slower                                        |
| telco                    | 7.27 ms                                                | 173 ms: 23.78x slower                                        |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: djangocms, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240509-3.14.0a0-5e272c0-JIT/bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.21x