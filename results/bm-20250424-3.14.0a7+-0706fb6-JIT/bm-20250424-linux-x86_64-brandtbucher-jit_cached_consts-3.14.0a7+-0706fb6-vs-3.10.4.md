# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 0706fb6
- commit date: 2025-04-24
- overall geometric mean: 1.463x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                      |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                    |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 593 ms: 2.98x faster                                                      |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.3 ms: 1.74x faster                                                     |
| float          | 117 ms                                                 | 70.8 ms: 1.65x faster                                                     |
| pidigits       | 191 ms                                                 | 194 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.41x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.05 ms: 1.19x faster                                                     |
| regex_dna      | 227 ms                                                 | 198 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 208 us: 1.59x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                     |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                     |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                     |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.13x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 593 ms: 2.98x faster                                                      |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                      |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                     |
| deltablue                | 7.91 ms                                                | 2.98 ms: 2.65x faster                                                     |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.36x faster                                                    |
| richards_super           | 94.7 ms                                                | 41.7 ms: 2.27x faster                                                     |
| richards                 | 79.3 ms                                                | 35.9 ms: 2.21x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.03x faster                                                     |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                     |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                      |
| go                       | 240 ms                                                 | 125 ms: 1.92x faster                                                      |
| logging_silent           | 190 ns                                                 | 99.5 ns: 1.91x faster                                                     |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                      |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                      |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 73.4 ms: 1.74x faster                                                     |
| nbody                    | 154 ms                                                 | 88.3 ms: 1.74x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                    |
| pyflate                  | 716 ms                                                 | 427 ms: 1.68x faster                                                      |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                      |
| float                    | 117 ms                                                 | 70.8 ms: 1.65x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 208 us: 1.59x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.65 ms: 1.56x faster                                                     |
| comprehensions           | 28.8 us                                                | 18.6 us: 1.55x faster                                                     |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                     |
| logging_format           | 9.09 us                                                | 6.08 us: 1.49x faster                                                     |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                     |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                     |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                      |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                      |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                     |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                     |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.42x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 60.6 ms: 1.39x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.68 ms: 1.38x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 742 ms: 1.37x faster                                                      |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                     |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                      |
| nqueens                  | 106 ms                                                 | 81.9 ms: 1.29x faster                                                     |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.29x faster                                                      |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                     |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.05 ms: 1.19x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                     |
| regex_dna                | 227 ms                                                 | 198 ms: 1.14x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 894 us: 1.10x faster                                                      |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                     |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                      |
| async_generators         | 444 ms                                                 | 422 ms: 1.05x faster                                                      |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                     |
| json                     | 5.69 ms                                                | 5.50 ms: 1.03x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                      |
| pidigits                 | 191 ms                                                 | 194 ms: 1.02x slower                                                      |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                     |
| coverage                 | 79.4 ms                                                | 93.2 ms: 1.17x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.79 ms: 1.32x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 81.8 ms: 3.40x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250424-3.14.0a7+-0706fb6-JIT/bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.463x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.30x