# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_lto
- machine: linux-x86_64
- commit hash: f5bcb83
- commit date: 2024-12-13
- overall geometric mean: 1.405x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                               |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                             |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.35x faster                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 624 ms: 2.84x faster                                               |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.69x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 342 ms: 2.54x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                               |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.8 ms: 1.85x faster                                              |
| float          | 117 ms                                                 | 76.1 ms: 1.54x faster                                              |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.43x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                               |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.38 ms: 1.07x faster                                              |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.16x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 199 us: 1.66x faster                                               |
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                             |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 54.9 ms: 1.44x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 77.6 ms: 1.28x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 95.2 ms: 1.21x faster                                              |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                              |
| Geometric mean       | (ref)                                                  | 1.37x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.19x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.4 ms: 1.57x faster                                              |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                              |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                              |
| genshi_xml      | 66.0 ms                                                | 60.3 ms: 1.10x faster                                              |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                               |
| async_tree_io            | 1.77 sec                                               | 624 ms: 2.84x faster                                               |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.69x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 342 ms: 2.54x faster                                               |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                              |
| generators               | 80.1 ms                                                | 37.4 ms: 2.14x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                              |
| pylint                   | 551 ms                                                 | 293 ms: 1.88x faster                                               |
| richards                 | 79.3 ms                                                | 42.3 ms: 1.87x faster                                              |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                               |
| nbody                    | 154 ms                                                 | 82.8 ms: 1.85x faster                                              |
| richards_super           | 94.7 ms                                                | 51.3 ms: 1.85x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 69.3 ms: 1.84x faster                                              |
| chaos                    | 115 ms                                                 | 62.9 ms: 1.83x faster                                              |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 66.0 ms: 1.79x faster                                              |
| deepcopy                 | 479 us                                                 | 276 us: 1.74x faster                                               |
| djangocms                | 38.4 us                                                | 22.5 us: 1.71x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 199 us: 1.66x faster                                               |
| raytrace                 | 507 ms                                                 | 305 ms: 1.66x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.60x faster                                              |
| comprehensions           | 28.8 us                                                | 18.1 us: 1.59x faster                                              |
| mako                     | 16.3 ms                                                | 10.4 ms: 1.57x faster                                              |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                               |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                               |
| go                       | 240 ms                                                 | 155 ms: 1.55x faster                                               |
| float                    | 117 ms                                                 | 76.1 ms: 1.54x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                              |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                              |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                               |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 54.9 ms: 1.44x faster                                              |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                               |
| scimark_fft              | 466 ms                                                 | 329 ms: 1.41x faster                                               |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                              |
| logging_simple           | 8.30 us                                                | 5.92 us: 1.40x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                              |
| logging_format           | 9.09 us                                                | 6.55 us: 1.39x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 740 ms: 1.38x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                              |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                               |
| fannkuch                 | 532 ms                                                 | 388 ms: 1.37x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                             |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.35x faster                                              |
| hexiom                   | 10.4 ms                                                | 7.77 ms: 1.34x faster                                              |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                               |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 77.6 ms: 1.28x faster                                              |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                              |
| sympy_sum                | 196 ms                                                 | 159 ms: 1.24x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 20.9 ms: 1.23x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                               |
| dulwich_log              | 84.3 ms                                                | 68.6 ms: 1.23x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 56.4 ms: 1.23x faster                                              |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 95.2 ms: 1.21x faster                                              |
| sympy_str                | 346 ms                                                 | 288 ms: 1.20x faster                                               |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                              |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.18x faster                                              |
| json                     | 5.69 ms                                                | 4.90 ms: 1.16x faster                                              |
| sympy_expand             | 566 ms                                                 | 490 ms: 1.15x faster                                               |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                              |
| bench_thread_pool        | 986 us                                                 | 881 us: 1.12x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                              |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                               |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                             |
| genshi_xml               | 66.0 ms                                                | 60.3 ms: 1.10x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.38 ms: 1.07x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                              |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                               |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                               |
| telco                    | 7.27 ms                                                | 7.62 ms: 1.05x slower                                              |
| coverage                 | 79.4 ms                                                | 83.6 ms: 1.05x slower                                              |
| mypy2                    | 894 ms                                                 | 967 ms: 1.08x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.19x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.57 ms: 1.26x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                              |
| bench_mp_pool            | 24.0 ms                                                | 81.3 ms: 3.38x slower                                              |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                       |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241213-3.14.0a2+-f5bcb83-JIT/bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.405x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.29x