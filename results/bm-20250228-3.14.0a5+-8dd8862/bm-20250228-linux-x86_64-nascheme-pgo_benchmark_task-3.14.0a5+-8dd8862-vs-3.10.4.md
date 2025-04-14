# Results vs. 3.10.4

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-x86_64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.470x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 593 ms: 2.98x faster                                                   |
| async_tree_none         | 728 ms                                                 | 248 ms: 2.94x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 306 ms: 2.84x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 468 ms: 2.17x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.7 ms: 1.68x faster                                                  |
| nbody          | 154 ms                                                 | 96.8 ms: 1.59x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.40x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| regex_v8       | 27.8 ms                                                | 22.9 ms: 1.21x faster                                                  |
| regex_dna      | 227 ms                                                 | 188 ms: 1.21x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.14 ms: 1.16x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.55x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 227 us: 1.46x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 56.5 ms: 1.40x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 129 ms: 1.30x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 93.9 ms: 1.23x faster                                                  |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                  |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                  |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 154 us: 3.53x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 593 ms: 2.98x faster                                                   |
| async_tree_none          | 728 ms                                                 | 248 ms: 2.94x faster                                                   |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 306 ms: 2.84x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.15 ms: 2.51x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 468 ms: 2.17x faster                                                   |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                   |
| chaos                    | 115 ms                                                 | 57.6 ms: 2.01x faster                                                  |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                  |
| richards_super           | 94.7 ms                                                | 48.8 ms: 1.94x faster                                                  |
| deepcopy                 | 479 us                                                 | 250 us: 1.91x faster                                                   |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                   |
| spectral_norm            | 170 ms                                                 | 91.1 ms: 1.87x faster                                                  |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                   |
| richards                 | 79.3 ms                                                | 42.8 ms: 1.85x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 64.2 ms: 1.84x faster                                                  |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.77x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.7 ms: 1.73x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.01 ms: 1.73x faster                                                  |
| float                    | 117 ms                                                 | 69.7 ms: 1.68x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                  |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                   |
| nbody                    | 154 ms                                                 | 96.8 ms: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.3 ms: 1.57x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.55x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                                   |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                   |
| logging_format           | 9.09 us                                                | 6.08 us: 1.50x faster                                                  |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                  |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| fannkuch                 | 532 ms                                                 | 364 ms: 1.46x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 227 us: 1.46x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 700 ms: 1.45x faster                                                   |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                  |
| scimark_fft              | 466 ms                                                 | 323 ms: 1.44x faster                                                   |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                  |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.5 ms: 1.40x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                 |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| nqueens                  | 106 ms                                                 | 79.4 ms: 1.33x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                  |
| thrift                   | 1.07 ms                                                | 817 us: 1.31x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 129 ms: 1.30x faster                                                   |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.30x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 66.9 ms: 1.26x faster                                                  |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 93.9 ms: 1.23x faster                                                  |
| meteor_contest           | 120 ms                                                 | 98.2 ms: 1.22x faster                                                  |
| async_generators         | 444 ms                                                 | 365 ms: 1.22x faster                                                   |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 22.9 ms: 1.21x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                  |
| regex_dna                | 227 ms                                                 | 188 ms: 1.21x faster                                                   |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.14 ms: 1.16x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                  |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                  |
| telco                    | 7.27 ms                                                | 6.81 ms: 1.07x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 88.7 ms: 1.12x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.83 ms: 1.33x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.6 ms: 3.44x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.470x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.24x