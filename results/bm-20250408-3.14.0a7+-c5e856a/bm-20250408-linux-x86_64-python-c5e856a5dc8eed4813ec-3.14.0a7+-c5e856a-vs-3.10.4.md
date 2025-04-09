# Results vs. 3.10.4

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: linux-x86_64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.480x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.40x faster                                                   |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 59.8 ms: 1.49x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 604 ms: 2.93x faster                                                   |
| async_tree_none         | 728 ms                                                 | 255 ms: 2.85x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.81x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 479 ms: 2.12x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.66x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.9 ms: 1.78x faster                                                  |
| nbody          | 154 ms                                                 | 90.2 ms: 1.70x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.46x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 123 ms: 1.54x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                  |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                  |
| django_template | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                  |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 48.5 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 604 ms: 2.93x faster                                                   |
| async_tree_none          | 728 ms                                                 | 255 ms: 2.85x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.81x faster                                                   |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.34x faster                                                 |
| go                       | 240 ms                                                 | 108 ms: 2.22x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 479 ms: 2.12x faster                                                   |
| chaos                    | 115 ms                                                 | 54.6 ms: 2.11x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                                  |
| logging_silent           | 190 ns                                                 | 92.5 ns: 2.05x faster                                                  |
| pylint                   | 551 ms                                                 | 276 ms: 1.99x faster                                                   |
| raytrace                 | 507 ms                                                 | 255 ms: 1.99x faster                                                   |
| deepcopy                 | 479 us                                                 | 245 us: 1.95x faster                                                   |
| richards_super           | 94.7 ms                                                | 48.7 ms: 1.95x faster                                                  |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.90x faster                                                   |
| richards                 | 79.3 ms                                                | 42.8 ms: 1.85x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 65.1 ms: 1.82x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                                  |
| float                    | 117 ms                                                 | 65.9 ms: 1.78x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                  |
| spectral_norm            | 170 ms                                                 | 98.5 ms: 1.72x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.04 ms: 1.72x faster                                                  |
| nbody                    | 154 ms                                                 | 90.2 ms: 1.70x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                 |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.35 us: 1.55x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                   |
| regex_compile            | 188 ms                                                 | 123 ms: 1.54x faster                                                   |
| logging_format           | 9.09 us                                                | 5.91 us: 1.54x faster                                                  |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                   |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                  |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                  |
| html5lib                 | 88.9 ms                                                | 59.8 ms: 1.49x faster                                                  |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 703 ms: 1.45x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                                  |
| 2to3                     | 348 ms                                                 | 250 ms: 1.40x faster                                                   |
| scimark_fft              | 466 ms                                                 | 336 ms: 1.39x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.68 ms: 1.38x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 48.5 ms: 1.36x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                  |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                   |
| nqueens                  | 106 ms                                                 | 80.0 ms: 1.32x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                   |
| sympy_str                | 346 ms                                                 | 264 ms: 1.31x faster                                                   |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| sympy_expand             | 566 ms                                                 | 448 ms: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                  |
| async_generators         | 444 ms                                                 | 391 ms: 1.13x faster                                                   |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 874 us: 1.13x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.07x faster                                                  |
| json                     | 5.69 ms                                                | 5.43 ms: 1.05x faster                                                  |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 85.0 ms: 1.07x slower                                                  |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.61 ms: 1.27x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.0 ms: 3.42x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.480x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.27x