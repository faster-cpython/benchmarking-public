# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 1c27106
- commit date: 2024-08-08
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                   |
| docutils       | 3.30 sec                                               | 3.09 sec: 1.07x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                  |
| tornado_http   | 136 ms                                                 | 110 ms: 1.23x faster                                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 338 ms: 2.15x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 441 ms: 1.97x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 935 ms: 1.89x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.94x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.2 ms: 1.91x faster                                                  |
| float          | 117 ms                                                 | 71.6 ms: 1.64x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.47x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                  |
| regex_dna      | 227 ms                                                 | 213 ms: 1.06x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.41 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.40x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.6 ms: 1.16x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                   |
| json_loads           | 31.2 us                                                | 28.5 us: 1.10x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.59x faster                                                  |
| genshi_text     | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                  |
| django_template | 48.2 ms                                                | 39.5 ms: 1.22x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                   |
| generators               | 80.1 ms                                                | 34.4 ms: 2.33x faster                                                  |
| async_tree_none          | 728 ms                                                 | 338 ms: 2.15x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 59.2 ms: 2.00x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 441 ms: 1.97x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 30.0 us: 1.95x faster                                                  |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 66.4 ms: 1.93x faster                                                  |
| deltablue                | 7.91 ms                                                | 4.13 ms: 1.92x faster                                                  |
| nbody                    | 154 ms                                                 | 80.2 ms: 1.91x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 935 ms: 1.89x faster                                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                                   |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                   |
| richards_super           | 94.7 ms                                                | 54.0 ms: 1.75x faster                                                  |
| deepcopy                 | 479 us                                                 | 275 us: 1.74x faster                                                   |
| raytrace                 | 507 ms                                                 | 293 ms: 1.73x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 535 ms: 1.72x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                  |
| richards                 | 79.3 ms                                                | 47.6 ms: 1.66x faster                                                  |
| float                    | 117 ms                                                 | 71.6 ms: 1.64x faster                                                  |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.37 ms: 1.59x faster                                                  |
| go                       | 240 ms                                                 | 151 ms: 1.59x faster                                                   |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.59x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                   |
| pyflate                  | 716 ms                                                 | 459 ms: 1.56x faster                                                   |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.55x faster                                                   |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.72 ms: 1.50x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.94 ms: 1.50x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.33 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                   |
| fannkuch                 | 532 ms                                                 | 369 ms: 1.44x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.93 us: 1.42x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.40x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                 |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.37x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                  |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                                   |
| pylint                   | 551 ms                                                 | 408 ms: 1.35x faster                                                   |
| html5lib                 | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                  |
| genshi_text              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                  |
| nqueens                  | 106 ms                                                 | 84.4 ms: 1.25x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.63 us: 1.25x faster                                                  |
| thrift                   | 1.07 ms                                                | 859 us: 1.25x faster                                                   |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                   |
| tornado_http             | 136 ms                                                 | 110 ms: 1.23x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 117 ms: 1.23x faster                                                   |
| django_template          | 48.2 ms                                                | 39.5 ms: 1.22x faster                                                  |
| logging_format           | 9.09 us                                                | 7.47 us: 1.22x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 59.2 ms: 1.17x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.6 ms: 1.16x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                  |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                   |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 893 us: 1.10x faster                                                   |
| json_loads               | 31.2 us                                                | 28.5 us: 1.10x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.09 sec: 1.07x faster                                                 |
| sympy_str                | 346 ms                                                 | 325 ms: 1.07x faster                                                   |
| regex_dna                | 227 ms                                                 | 213 ms: 1.06x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.41 ms: 1.06x faster                                                  |
| sympy_expand             | 566 ms                                                 | 541 ms: 1.05x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 25.1 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                                  |
| telco                    | 7.27 ms                                                | 7.72 ms: 1.06x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                  |
| coverage                 | 79.4 ms                                                | 93.6 ms: 1.18x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, sympy_sum
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240808-3.14.0a0-1c27106-JIT/bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.24x