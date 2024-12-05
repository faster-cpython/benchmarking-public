# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_cold_16
- machine: linux-x86_64
- commit hash: 189256b
- commit date: 2024-12-04
- overall geometric mean: 1.431x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                   |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 623 ms: 2.84x faster                                                   |
| async_tree_none         | 728 ms                                                 | 271 ms: 2.69x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 340 ms: 2.56x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.52x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.5 ms: 1.91x faster                                                  |
| float          | 117 ms                                                 | 75.9 ms: 1.54x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.44x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                  |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 194 us: 1.71x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 94.9 ms: 1.22x faster                                                  |
| json_loads           | 31.2 us                                                | 26.3 us: 1.19x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                  |
| django_template | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 56.7 ms: 1.17x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 623 ms: 2.84x faster                                                   |
| async_tree_none          | 728 ms                                                 | 271 ms: 2.69x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 340 ms: 2.56x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                  |
| richards_super           | 94.7 ms                                                | 42.8 ms: 2.22x faster                                                  |
| generators               | 80.1 ms                                                | 36.8 ms: 2.18x faster                                                  |
| richards                 | 79.3 ms                                                | 37.9 ms: 2.09x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                  |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                                   |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                                  |
| nbody                    | 154 ms                                                 | 80.5 ms: 1.91x faster                                                  |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 69.4 ms: 1.84x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 65.5 ms: 1.80x faster                                                  |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                   |
| go                       | 240 ms                                                 | 135 ms: 1.78x faster                                                   |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                   |
| raytrace                 | 507 ms                                                 | 289 ms: 1.76x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.71x faster                                                   |
| djangocms                | 38.4 us                                                | 22.5 us: 1.71x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                  |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                   |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                  |
| float                    | 117 ms                                                 | 75.9 ms: 1.54x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                  |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.48x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.05 ms: 1.47x faster                                                  |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.75 us: 1.44x faster                                                  |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                  |
| scimark_fft              | 466 ms                                                 | 327 ms: 1.42x faster                                                   |
| django_template          | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                  |
| thrift                   | 1.07 ms                                                | 784 us: 1.37x faster                                                   |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                                   |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.32x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.97 ms: 1.30x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                  |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 55.9 ms: 1.24x faster                                                  |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 68.6 ms: 1.23x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 94.9 ms: 1.22x faster                                                  |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                   |
| json_loads               | 31.2 us                                                | 26.3 us: 1.19x faster                                                  |
| nqueens                  | 106 ms                                                 | 89.7 ms: 1.18x faster                                                  |
| json                     | 5.69 ms                                                | 4.85 ms: 1.17x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 56.7 ms: 1.17x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 879 us: 1.12x faster                                                   |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                  |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                                   |
| telco                    | 7.27 ms                                                | 7.53 ms: 1.04x slower                                                  |
| coverage                 | 79.4 ms                                                | 83.6 ms: 1.05x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.04 ms: 1.39x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241204-3.14.0a2+-189256b-JIT/bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.431x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x