# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_warmup_2048
- machine: linux-x86_64
- commit hash: 004e970
- commit date: 2025-03-03
- overall geometric mean: 1.448x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                    |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                  |
| html5lib       | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.88x faster                                                    |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 331 ms: 2.62x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 486 ms: 2.09x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.6 ms: 1.68x faster                                                   |
| nbody          | 154 ms                                                 | 94.1 ms: 1.63x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.41x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.35 ms: 1.08x faster                                                   |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.16x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 204 us: 1.62x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 78.2 ms: 1.27x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                    |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.59x faster                                                   |
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                   |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.49x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.40x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.88x faster                                                    |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                   |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 331 ms: 2.62x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 486 ms: 2.09x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                   |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                                    |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                    |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                   |
| richards_super           | 94.7 ms                                                | 50.2 ms: 1.89x faster                                                   |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                    |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                    |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                    |
| richards                 | 79.3 ms                                                | 43.5 ms: 1.82x faster                                                   |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                   |
| spectral_norm            | 170 ms                                                 | 99.1 ms: 1.71x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                  |
| pyflate                  | 716 ms                                                 | 426 ms: 1.68x faster                                                    |
| float                    | 117 ms                                                 | 69.6 ms: 1.68x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.36 ms: 1.63x faster                                                   |
| nbody                    | 154 ms                                                 | 94.1 ms: 1.63x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 204 us: 1.62x faster                                                    |
| comprehensions           | 28.8 us                                                | 17.8 us: 1.62x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                   |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.59x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                                   |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                   |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                    |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                   |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                                   |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                    |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                   |
| html5lib                 | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                   |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.48 ms: 1.44x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                   |
| thrift                   | 1.07 ms                                                | 752 us: 1.42x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 744 ms: 1.37x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                    |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                   |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                    |
| nqueens                  | 106 ms                                                 | 81.1 ms: 1.30x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                                   |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.30x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 78.2 ms: 1.27x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                   |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 67.2 ms: 1.25x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                  |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                    |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 879 us: 1.12x faster                                                    |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.71 us: 1.12x faster                                                   |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                    |
| async_generators         | 444 ms                                                 | 407 ms: 1.09x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.35 ms: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                                   |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                   |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                    |
| telco                    | 7.27 ms                                                | 7.59 ms: 1.04x slower                                                   |
| coverage                 | 79.4 ms                                                | 84.2 ms: 1.06x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.77 ms: 1.32x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.42 ms: 1.50x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                            |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250303-3.14.0a5+-004e970-JIT/bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.448x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x