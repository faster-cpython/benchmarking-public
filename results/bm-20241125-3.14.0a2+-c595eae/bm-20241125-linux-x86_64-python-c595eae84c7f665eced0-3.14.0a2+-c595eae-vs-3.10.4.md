# Results vs. 3.10.4

- fork: python
- ref: c595eae84c7f665eced0
- machine: linux-x86_64
- commit hash: c595eae
- commit date: 2024-11-25
- overall geometric mean: 1.386x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 431 ms: 2.02x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 934 ms: 1.89x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 564 ms: 1.80x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.98x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 96.4 ms: 1.59x faster                                                  |
| float          | 117 ms                                                 | 82.5 ms: 1.42x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                  |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 329 us: 1.47x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                  |
| json_loads           | 31.2 us                                                | 26.0 us: 1.20x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.12x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                  |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                  |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.39x faster                                                   |
| generators               | 80.1 ms                                                | 27.3 ms: 2.94x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.31 ms: 2.39x faster                                                  |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                   |
| pylint                   | 551 ms                                                 | 263 ms: 2.10x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 431 ms: 2.02x faster                                                   |
| go                       | 240 ms                                                 | 121 ms: 1.99x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 934 ms: 1.89x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 31.2 us: 1.88x faster                                                  |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                                  |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                   |
| deepcopy                 | 479 us                                                 | 264 us: 1.81x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 564 ms: 1.80x faster                                                   |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                                  |
| logging_silent           | 190 ns                                                 | 109 ns: 1.75x faster                                                   |
| djangocms                | 38.4 us                                                | 22.0 us: 1.75x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.7 ms: 1.73x faster                                                  |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                   |
| richards                 | 79.3 ms                                                | 46.4 ms: 1.71x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 70.1 ms: 1.69x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.68x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.43 ms: 1.62x faster                                                  |
| nbody                    | 154 ms                                                 | 96.4 ms: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                  |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                                   |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                   |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                 |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 329 us: 1.47x faster                                                   |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                                   |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                  |
| float                    | 117 ms                                                 | 82.5 ms: 1.42x faster                                                  |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| html5lib                 | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                   |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                   |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.91 ms: 1.32x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.1 ms: 1.32x faster                                                  |
| nqueens                  | 106 ms                                                 | 81.1 ms: 1.30x faster                                                  |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                  |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                  |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                  |
| scimark_fft              | 466 ms                                                 | 376 ms: 1.24x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                 |
| json_loads               | 31.2 us                                                | 26.0 us: 1.20x faster                                                  |
| json                     | 5.69 ms                                                | 4.84 ms: 1.17x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 851 us: 1.16x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.12x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                  |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                                   |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                   |
| coverage                 | 79.4 ms                                                | 85.1 ms: 1.07x slower                                                  |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.08x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.33x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.72 ms: 1.68x slower                                                  |
| dask                     | 441 ms                                                 | 780 ms: 1.77x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                           |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20241125-3.14.0a2+-c595eae/bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.386x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.26x