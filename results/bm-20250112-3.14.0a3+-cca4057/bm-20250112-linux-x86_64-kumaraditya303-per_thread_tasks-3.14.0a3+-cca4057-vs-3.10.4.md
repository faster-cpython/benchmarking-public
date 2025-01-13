# Results vs. 3.10.4

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: cca4057
- commit date: 2025-01-12
- overall geometric mean: 1.442x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                       |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                     |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.43x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 604 ms: 2.93x faster                                                       |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.81x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 326 ms: 2.67x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 485 ms: 2.10x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.7 ms: 1.61x faster                                                      |
| nbody          | 154 ms                                                 | 96.0 ms: 1.60x faster                                                      |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                      |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.49x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.22x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 96.4 ms: 1.20x faster                                                      |
| json_loads           | 31.2 us                                                | 26.3 us: 1.18x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                      |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                      |
| mako            | 16.3 ms                                                | 11.5 ms: 1.43x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                       |
| generators               | 80.1 ms                                                | 27.3 ms: 2.93x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 604 ms: 2.93x faster                                                       |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.81x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 326 ms: 2.67x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 485 ms: 2.10x faster                                                       |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                                       |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                      |
| chaos                    | 115 ms                                                 | 61.0 ms: 1.89x faster                                                      |
| richards_super           | 94.7 ms                                                | 51.0 ms: 1.86x faster                                                      |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                       |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                                      |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                                       |
| richards                 | 79.3 ms                                                | 44.7 ms: 1.77x faster                                                      |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                      |
| float                    | 117 ms                                                 | 72.7 ms: 1.61x faster                                                      |
| nbody                    | 154 ms                                                 | 96.0 ms: 1.60x faster                                                      |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.59x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                      |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                       |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                      |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.49x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.48x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                      |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                      |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                       |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.43x faster                                                      |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                      |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.43x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.41x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                       |
| thrift                   | 1.07 ms                                                | 771 us: 1.39x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.69 ms: 1.38x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.38x faster                                                       |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                       |
| scimark_fft              | 466 ms                                                 | 346 ms: 1.35x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 63.1 ms: 1.34x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                      |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                      |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 52.4 ms: 1.32x faster                                                      |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                      |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                     |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.22x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 96.4 ms: 1.20x faster                                                      |
| json_loads               | 31.2 us                                                | 26.3 us: 1.18x faster                                                      |
| json                     | 5.69 ms                                                | 4.88 ms: 1.17x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 863 us: 1.14x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                      |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.67 sec: 1.07x faster                                                     |
| async_generators         | 444 ms                                                 | 426 ms: 1.04x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                       |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                       |
| coverage                 | 79.4 ms                                                | 84.0 ms: 1.06x slower                                                      |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.62 ms: 1.27x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250112-3.14.0a3+-cca4057/bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.442x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.26x