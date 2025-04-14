# Results vs. 3.10.4

- fork: python
- ref: 1b27f36eb0ef146aa60b
- machine: linux-x86_64
- commit hash: 1b27f36
- commit date: 2025-02-13
- overall geometric mean: 1.487x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                   |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                 |
| html5lib       | 88.9 ms                                                | 57.8 ms: 1.54x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 608 ms: 2.91x faster                                                   |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.82x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 528 ms: 1.92x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.8 ms: 1.78x faster                                                  |
| nbody          | 154 ms                                                 | 92.7 ms: 1.66x faster                                                  |
| pidigits       | 191 ms                                                 | 212 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 123 ms: 1.53x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.11 ms: 1.17x faster                                                  |
| regex_dna      | 227 ms                                                 | 197 ms: 1.15x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.81 sec: 1.74x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 208 us: 1.59x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                  |
| json_dumps           | 14.2 ms                                                | 12.3 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                                   |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.6 ms: 1.57x faster                                                  |
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                  |
| mako            | 16.3 ms                                                | 11.1 ms: 1.46x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 48.0 ms: 1.38x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 153 us: 3.57x faster                                                   |
| generators               | 80.1 ms                                                | 27.3 ms: 2.93x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 608 ms: 2.91x faster                                                   |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.82x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.43x faster                                                  |
| chaos                    | 115 ms                                                 | 54.3 ms: 2.13x faster                                                  |
| logging_silent           | 190 ns                                                 | 91.0 ns: 2.08x faster                                                  |
| scimark_sor              | 220 ms                                                 | 106 ms: 2.07x faster                                                   |
| spectral_norm            | 170 ms                                                 | 81.9 ms: 2.07x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.2 us: 2.07x faster                                                  |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 58.7 ms: 2.01x faster                                                  |
| richards_super           | 94.7 ms                                                | 47.1 ms: 2.01x faster                                                  |
| go                       | 240 ms                                                 | 121 ms: 1.98x faster                                                   |
| deepcopy                 | 479 us                                                 | 243 us: 1.97x faster                                                   |
| richards                 | 79.3 ms                                                | 40.2 ms: 1.97x faster                                                  |
| raytrace                 | 507 ms                                                 | 259 ms: 1.96x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 528 ms: 1.92x faster                                                   |
| float                    | 117 ms                                                 | 65.8 ms: 1.78x faster                                                  |
| pyflate                  | 716 ms                                                 | 403 ms: 1.78x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 73.2 ms: 1.75x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.81 sec: 1.74x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                  |
| scimark_lu               | 176 ms                                                 | 105 ms: 1.67x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.50 us: 1.67x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.55 ms: 1.66x faster                                                  |
| nbody                    | 154 ms                                                 | 92.7 ms: 1.66x faster                                                  |
| scimark_fft              | 466 ms                                                 | 284 ms: 1.64x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 3.99 ms: 1.62x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.51 ms: 1.60x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 208 us: 1.59x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.1 ms: 1.59x faster                                                  |
| django_template          | 48.2 ms                                                | 30.6 ms: 1.57x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.39 us: 1.54x faster                                                  |
| html5lib                 | 88.9 ms                                                | 57.8 ms: 1.54x faster                                                  |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                  |
| regex_compile            | 188 ms                                                 | 123 ms: 1.53x faster                                                   |
| logging_format           | 9.09 us                                                | 5.94 us: 1.53x faster                                                  |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.46x faster                                                  |
| thrift                   | 1.07 ms                                                | 736 us: 1.46x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.2 ms: 1.44x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                 |
| pathlib                  | 20.5 ms                                                | 14.7 ms: 1.39x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 48.0 ms: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 741 ms: 1.37x faster                                                   |
| nqueens                  | 106 ms                                                 | 77.1 ms: 1.37x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                   |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                   |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.34x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 63.9 ms: 1.32x faster                                                  |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 53.1 ms: 1.30x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.11 ms: 1.17x faster                                                  |
| json_dumps               | 14.2 ms                                                | 12.3 ms: 1.16x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.63 us: 1.15x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                  |
| regex_dna                | 227 ms                                                 | 197 ms: 1.15x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                  |
| async_generators         | 444 ms                                                 | 403 ms: 1.10x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                                   |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.06x faster                                                   |
| json                     | 5.69 ms                                                | 5.45 ms: 1.04x faster                                                  |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                                  |
| telco                    | 7.27 ms                                                | 7.07 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.88 sec: 1.01x slower                                                 |
| coverage                 | 79.4 ms                                                | 80.8 ms: 1.02x slower                                                  |
| pidigits                 | 191 ms                                                 | 212 ms: 1.11x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.83 ms: 1.33x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.53 ms: 1.56x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 79.5 ms: 3.31x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.46x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250213-3.14.0a5+-1b27f36-CLANG,JIT/bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.487x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: 1.29x