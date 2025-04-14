# Results vs. 3.10.4

- fork: iritkatriel
- ref: binary_subscr
- machine: linux-x86_64
- commit hash: fa072fd
- commit date: 2025-01-28
- overall geometric mean: 1.436x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                 |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                               |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                |
| Geometric mean | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 623 ms: 2.84x faster                                                 |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 327 ms: 2.66x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.1 ms: 1.62x faster                                                |
| nbody          | 154 ms                                                 | 97.9 ms: 1.57x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.05 sec: 1.53x faster                                               |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                |
| genshi_text     | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                                 |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                |
| async_tree_io            | 1.77 sec                                               | 623 ms: 2.84x faster                                                 |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 327 ms: 2.66x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                 |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                 |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                 |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 31.1 us: 1.88x faster                                                |
| richards_super           | 94.7 ms                                                | 51.1 ms: 1.86x faster                                                |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                 |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                 |
| richards                 | 79.3 ms                                                | 44.6 ms: 1.78x faster                                                |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                |
| spectral_norm            | 170 ms                                                 | 97.9 ms: 1.74x faster                                                |
| logging_silent           | 190 ns                                                 | 110 ns: 1.72x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 74.9 ms: 1.71x faster                                                |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.70x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.40 ms: 1.62x faster                                                |
| float                    | 117 ms                                                 | 72.1 ms: 1.62x faster                                                |
| nbody                    | 154 ms                                                 | 97.9 ms: 1.57x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.05 sec: 1.53x faster                                               |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                                 |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                |
| pyflate                  | 716 ms                                                 | 482 ms: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                 |
| genshi_text              | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                |
| thrift                   | 1.07 ms                                                | 757 us: 1.42x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.41x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 736 ms: 1.38x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                 |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.77 ms: 1.36x faster                                                |
| scimark_fft              | 466 ms                                                 | 346 ms: 1.35x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 52.6 ms: 1.31x faster                                                |
| dulwich_log              | 84.3 ms                                                | 64.8 ms: 1.30x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                               |
| nqueens                  | 106 ms                                                 | 83.8 ms: 1.26x faster                                                |
| fannkuch                 | 532 ms                                                 | 423 ms: 1.26x faster                                                 |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.24x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                               |
| async_generators         | 444 ms                                                 | 387 ms: 1.15x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                |
| bench_thread_pool        | 986 us                                                 | 867 us: 1.14x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                 |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                 |
| telco                    | 7.27 ms                                                | 7.85 ms: 1.08x slower                                                |
| coverage                 | 79.4 ms                                                | 89.8 ms: 1.13x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.81 ms: 1.33x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                         |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250128-3.14.0a4+-fa072fd/bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.436x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.26x