# Results vs. 3.10.4

- fork: methane
- ref: optimize_json_encode
- machine: linux-x86_64
- commit hash: d026be3
- commit date: 2025-04-30
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.39x faster                                                    |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                  |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.95x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.75x faster                                                    |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.74x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 503 ms: 2.02x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.5 ms: 1.69x faster                                                   |
| nbody          | 154 ms                                                 | 101 ms: 1.52x faster                                                    |
| pidigits       | 191 ms                                                 | 195 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.36x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                    |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                   |
| regex_dna      | 227 ms                                                 | 209 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                  | 1.21x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 311 us: 1.56x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 60.8 ms: 1.30x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.17x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 87.6 ms: 1.13x faster                                                   |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 6.87 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                   |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                   |
| mako            | 16.3 ms                                                | 11.7 ms: 1.39x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 48.9 ms: 1.35x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.95x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.75x faster                                                    |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.74x faster                                                    |
| generators               | 80.1 ms                                                | 29.6 ms: 2.71x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.36 ms: 2.35x faster                                                   |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                  |
| go                       | 240 ms                                                 | 112 ms: 2.15x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 28.5 us: 2.05x faster                                                   |
| chaos                    | 115 ms                                                 | 56.6 ms: 2.04x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 503 ms: 2.02x faster                                                    |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                    |
| logging_silent           | 190 ns                                                 | 96.6 ns: 1.96x faster                                                   |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                    |
| deepcopy                 | 479 us                                                 | 251 us: 1.91x faster                                                    |
| richards_super           | 94.7 ms                                                | 49.7 ms: 1.90x faster                                                   |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                    |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.84x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 72.8 ms: 1.75x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                   |
| float                    | 117 ms                                                 | 69.5 ms: 1.69x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                                   |
| pyflate                  | 716 ms                                                 | 440 ms: 1.63x faster                                                    |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.63x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 311 us: 1.56x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                    |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                   |
| nbody                    | 154 ms                                                 | 101 ms: 1.52x faster                                                    |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                    |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                   |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                   |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.44x faster                                                  |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                                  |
| coroutines               | 35.1 ms                                                | 25.2 ms: 1.39x faster                                                   |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.39x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                   |
| 2to3                     | 348 ms                                                 | 252 ms: 1.39x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 48.9 ms: 1.35x faster                                                   |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                    |
| nqueens                  | 106 ms                                                 | 80.6 ms: 1.31x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.94 ms: 1.31x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 60.8 ms: 1.30x faster                                                   |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                                    |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                    |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                  |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.17x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 87.6 ms: 1.13x faster                                                   |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                    |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 887 us: 1.11x faster                                                    |
| async_generators         | 444 ms                                                 | 401 ms: 1.11x faster                                                    |
| regex_dna                | 227 ms                                                 | 209 ms: 1.09x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                   |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                                   |
| json                     | 5.69 ms                                                | 5.62 ms: 1.01x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                    |
| pidigits                 | 191 ms                                                 | 195 ms: 1.02x slower                                                    |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 6.87 ms: 1.16x slower                                                   |
| coverage                 | 79.4 ms                                                | 92.5 ms: 1.16x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.62 ms: 1.28x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 82.0 ms: 3.41x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                            |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-d026be3/bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x