# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_warmup_1024
- machine: linux-x86_64
- commit hash: 39791ef
- commit date: 2025-03-04
- overall geometric mean: 1.445x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                    |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                  |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 608 ms: 2.91x faster                                                    |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 328 ms: 2.65x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.4 ms: 1.68x faster                                                   |
| float          | 117 ms                                                 | 69.9 ms: 1.68x faster                                                   |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.42x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                   |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.15x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 203 us: 1.63x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.42x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 78.9 ms: 1.26x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                    |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                   |
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                   |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 608 ms: 2.91x faster                                                    |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                   |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 328 ms: 2.65x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                   |
| go                       | 240 ms                                                 | 120 ms: 2.01x faster                                                    |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                    |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                   |
| richards_super           | 94.7 ms                                                | 50.4 ms: 1.88x faster                                                   |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                    |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                    |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                    |
| richards                 | 79.3 ms                                                | 44.0 ms: 1.80x faster                                                   |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 71.8 ms: 1.78x faster                                                   |
| spectral_norm            | 170 ms                                                 | 96.0 ms: 1.77x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 68.4 ms: 1.73x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                  |
| nbody                    | 154 ms                                                 | 91.4 ms: 1.68x faster                                                   |
| float                    | 117 ms                                                 | 69.9 ms: 1.68x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                                   |
| pyflate                  | 716 ms                                                 | 431 ms: 1.66x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 203 us: 1.63x faster                                                    |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.8 us: 1.62x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                   |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                    |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                   |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                    |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                    |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                   |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                   |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.42x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.56 ms: 1.42x faster                                                   |
| thrift                   | 1.07 ms                                                | 764 us: 1.40x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                    |
| fannkuch                 | 532 ms                                                 | 399 ms: 1.33x faster                                                    |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                    |
| nqueens                  | 106 ms                                                 | 80.8 ms: 1.31x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                   |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 66.7 ms: 1.26x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 78.9 ms: 1.26x faster                                                   |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                    |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                   |
| sympy_expand             | 566 ms                                                 | 475 ms: 1.19x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                                    |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                   |
| async_generators         | 444 ms                                                 | 404 ms: 1.10x faster                                                    |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                   |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                                   |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                    |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                    |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                                   |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.58 ms: 1.26x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.42 ms: 1.50x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                            |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250304-3.14.0a5+-39791ef-JIT/bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.445x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x