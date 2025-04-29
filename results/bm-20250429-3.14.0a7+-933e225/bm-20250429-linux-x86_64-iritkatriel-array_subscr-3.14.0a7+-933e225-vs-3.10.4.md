# Results vs. 3.10.4

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 933e225
- commit date: 2025-04-29
- overall geometric mean: 1.451x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                              |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 595 ms: 2.97x faster                                                |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.3 ms: 1.71x faster                                               |
| nbody          | 154 ms                                                 | 95.1 ms: 1.61x faster                                               |
| pidigits       | 191 ms                                                 | 194 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.40x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.18 ms: 1.14x faster                                               |
| regex_dna      | 227 ms                                                 | 204 ms: 1.11x faster                                                |
| Geometric mean | (ref)                                                  | 1.23x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                              |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                               |
| django_template | 48.2 ms                                                | 31.8 ms: 1.52x faster                                               |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                |
| async_tree_io            | 1.77 sec                                               | 595 ms: 2.97x faster                                                |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                |
| generators               | 80.1 ms                                                | 29.3 ms: 2.73x faster                                               |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                              |
| deltablue                | 7.91 ms                                                | 3.40 ms: 2.33x faster                                               |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                |
| chaos                    | 115 ms                                                 | 56.4 ms: 2.05x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                               |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                |
| logging_silent           | 190 ns                                                 | 97.9 ns: 1.94x faster                                               |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                |
| richards_super           | 94.7 ms                                                | 49.9 ms: 1.90x faster                                               |
| deepcopy                 | 479 us                                                 | 257 us: 1.87x faster                                                |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.84x faster                                               |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 72.4 ms: 1.76x faster                                               |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                               |
| float                    | 117 ms                                                 | 68.3 ms: 1.71x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.14 ms: 1.69x faster                                               |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 72.6 ms: 1.63x faster                                               |
| nbody                    | 154 ms                                                 | 95.1 ms: 1.61x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                              |
| pyflate                  | 716 ms                                                 | 449 ms: 1.59x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                               |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.52x faster                                               |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                               |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                               |
| dulwich_log              | 84.3 ms                                                | 58.6 ms: 1.44x faster                                               |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.44x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                                |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                               |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                              |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                               |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                |
| nqueens                  | 106 ms                                                 | 80.6 ms: 1.31x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                                |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                                |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                              |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| scimark_fft              | 466 ms                                                 | 386 ms: 1.21x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.19x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.63 ms: 1.15x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.18 ms: 1.14x faster                                               |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                |
| async_generators         | 444 ms                                                 | 397 ms: 1.12x faster                                                |
| bench_thread_pool        | 986 us                                                 | 886 us: 1.11x faster                                                |
| regex_dna                | 227 ms                                                 | 204 ms: 1.11x faster                                                |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                               |
| json                     | 5.69 ms                                                | 5.40 ms: 1.05x faster                                               |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                |
| pidigits                 | 191 ms                                                 | 194 ms: 1.02x slower                                                |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                               |
| coverage                 | 79.4 ms                                                | 93.1 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.64 ms: 1.28x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.2 ms: 3.42x slower                                               |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250429-3.14.0a7+-933e225/bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.451x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x