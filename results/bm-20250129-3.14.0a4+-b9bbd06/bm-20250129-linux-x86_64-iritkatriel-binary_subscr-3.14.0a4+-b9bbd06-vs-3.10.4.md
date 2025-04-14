# Results vs. 3.10.4

- fork: iritkatriel
- ref: binary_subscr
- machine: linux-x86_64
- commit hash: b9bbd06
- commit date: 2025-01-29
- overall geometric mean: 1.436x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                 |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                               |
| html5lib       | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                |
| Geometric mean | (ref)                                                  | 1.36x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 628 ms: 2.82x faster                                                 |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.74x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 326 ms: 2.67x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 491 ms: 2.07x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.6 ms: 1.63x faster                                                |
| nbody          | 154 ms                                                 | 99.6 ms: 1.54x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.13 ms: 1.16x faster                                                |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.18x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                               |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 97.0 ms: 1.19x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                 |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                |
| async_tree_io            | 1.77 sec                                               | 628 ms: 2.82x faster                                                 |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.74x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 326 ms: 2.67x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 491 ms: 2.07x faster                                                 |
| pylint                   | 551 ms                                                 | 275 ms: 2.00x faster                                                 |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                                 |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.91x faster                                                |
| richards_super           | 94.7 ms                                                | 50.7 ms: 1.87x faster                                                |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                 |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                 |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                                 |
| richards                 | 79.3 ms                                                | 44.6 ms: 1.78x faster                                                |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.4 ms: 1.73x faster                                                |
| spectral_norm            | 170 ms                                                 | 98.7 ms: 1.72x faster                                                |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 76.9 ms: 1.66x faster                                                |
| float                    | 117 ms                                                 | 71.6 ms: 1.63x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.59 ms: 1.58x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.55x faster                                                |
| nbody                    | 154 ms                                                 | 99.6 ms: 1.54x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                               |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                 |
| pyflate                  | 716 ms                                                 | 476 ms: 1.51x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                |
| html5lib                 | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                 |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 733 ms: 1.39x faster                                                 |
| thrift                   | 1.07 ms                                                | 774 us: 1.39x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.69 ms: 1.38x faster                                                |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                 |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                 |
| scimark_fft              | 466 ms                                                 | 346 ms: 1.35x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 52.7 ms: 1.31x faster                                                |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.31x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                               |
| fannkuch                 | 532 ms                                                 | 421 ms: 1.26x faster                                                 |
| nqueens                  | 106 ms                                                 | 83.8 ms: 1.26x faster                                                |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 97.0 ms: 1.19x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.13 ms: 1.16x faster                                                |
| async_generators         | 444 ms                                                 | 385 ms: 1.15x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                               |
| bench_thread_pool        | 986 us                                                 | 864 us: 1.14x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                 |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                 |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                                |
| coverage                 | 79.4 ms                                                | 89.9 ms: 1.13x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.81 ms: 1.33x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                         |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250129-3.14.0a4+-b9bbd06/bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.436x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.26x