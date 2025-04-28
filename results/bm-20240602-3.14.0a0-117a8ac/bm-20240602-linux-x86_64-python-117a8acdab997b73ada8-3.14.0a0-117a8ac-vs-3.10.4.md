# Results vs. 3.10.4

- fork: python
- ref: 117a8acdab997b73ada8
- machine: linux-x86_64
- commit hash: 117a8ac
- commit date: 2024-06-02
- overall geometric mean: 1.385x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.32x faster                                                  |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                |
| html5lib       | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                 |
| tornado_http   | 136 ms                                                 | 91.8 ms: 1.48x faster                                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 370 ms: 1.97x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 936 ms: 1.89x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 462 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 601 ms: 1.69x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.85x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.5 ms: 1.73x faster                                                 |
| float          | 117 ms                                                 | 77.1 ms: 1.52x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                 |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 27.5 us: 1.14x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 14.2 ms: 1.03x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.91 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                 |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.39x faster                                                  |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                 |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                 |
| async_tree_none          | 728 ms                                                 | 370 ms: 1.97x faster                                                  |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 936 ms: 1.89x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 462 ms: 1.88x faster                                                  |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                  |
| pylint                   | 551 ms                                                 | 307 ms: 1.79x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 73.2 ms: 1.75x faster                                                 |
| nbody                    | 154 ms                                                 | 88.5 ms: 1.73x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.07 ms: 1.71x faster                                                 |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 601 ms: 1.69x faster                                                  |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                  |
| go                       | 240 ms                                                 | 143 ms: 1.67x faster                                                  |
| richards_super           | 94.7 ms                                                | 57.2 ms: 1.66x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                  |
| richards                 | 79.3 ms                                                | 50.5 ms: 1.57x faster                                                 |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                  |
| pyflate                  | 716 ms                                                 | 464 ms: 1.54x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| float                    | 117 ms                                                 | 77.1 ms: 1.52x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 38.6 us: 1.51x faster                                                 |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                  |
| tornado_http             | 136 ms                                                 | 91.8 ms: 1.48x faster                                                 |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                 |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                                 |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                 |
| deepcopy                 | 479 us                                                 | 353 us: 1.36x faster                                                  |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                 |
| html5lib                 | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                 |
| 2to3                     | 348 ms                                                 | 265 ms: 1.32x faster                                                  |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                 |
| thrift                   | 1.07 ms                                                | 819 us: 1.31x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.9 ms: 1.31x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.22 us: 1.29x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 65.4 ms: 1.29x faster                                                 |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.28x faster                                                  |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                 |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.23x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                |
| bench_thread_pool        | 986 us                                                 | 824 us: 1.20x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                |
| json_loads               | 31.2 us                                                | 27.5 us: 1.14x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| json                     | 5.69 ms                                                | 5.20 ms: 1.09x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.91 us: 1.04x faster                                                 |
| python_startup           | 14.6 ms                                                | 14.2 ms: 1.03x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 439 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                 |
| coverage                 | 79.4 ms                                                | 91.6 ms: 1.15x slower                                                 |
| telco                    | 7.27 ms                                                | 8.42 ms: 1.16x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.91 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.28 ms: 1.18x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (24) of results/bm-20240602-3.14.0a0-117a8ac/bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.385x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.24x