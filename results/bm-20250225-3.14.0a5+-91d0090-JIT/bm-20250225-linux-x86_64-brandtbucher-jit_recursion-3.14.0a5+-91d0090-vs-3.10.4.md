# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_recursion
- machine: linux-x86_64
- commit hash: 91d0090
- commit date: 2025-02-25
- overall geometric mean: 1.432x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                  |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.87x faster                                                  |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.74x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 333 ms: 2.62x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.6 ms: 1.71x faster                                                 |
| float          | 117 ms                                                 | 72.4 ms: 1.62x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.6 ms: 1.08x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.38 ms: 1.07x faster                                                 |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                |
| unpickle_pure_python | 331 us                                                 | 207 us: 1.60x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 97.5 ms: 1.18x faster                                                 |
| json_loads           | 31.2 us                                                | 30.1 us: 1.04x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                 |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                 |
| genshi_text     | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.35x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.87x faster                                                  |
| generators               | 80.1 ms                                                | 28.5 ms: 2.81x faster                                                 |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.74x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 333 ms: 2.62x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.40 ms: 2.33x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                  |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                                 |
| go                       | 240 ms                                                 | 128 ms: 1.88x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 31.2 us: 1.87x faster                                                 |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                                 |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                  |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                  |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                  |
| spectral_norm            | 170 ms                                                 | 97.4 ms: 1.74x faster                                                 |
| richards                 | 79.3 ms                                                | 45.6 ms: 1.74x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.9 ms: 1.72x faster                                                 |
| nbody                    | 154 ms                                                 | 89.6 ms: 1.71x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 75.1 ms: 1.70x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                 |
| float                    | 117 ms                                                 | 72.4 ms: 1.62x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 207 us: 1.60x faster                                                  |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.67 ms: 1.56x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                 |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                 |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                 |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                                  |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                 |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                 |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                 |
| genshi_text              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                 |
| thrift                   | 1.07 ms                                                | 765 us: 1.40x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                  |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                 |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                 |
| nqueens                  | 106 ms                                                 | 82.8 ms: 1.28x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                 |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 97.5 ms: 1.18x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 881 us: 1.12x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| async_generators         | 444 ms                                                 | 407 ms: 1.09x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.6 ms: 1.08x faster                                                 |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.38 ms: 1.07x faster                                                 |
| json_loads               | 31.2 us                                                | 30.1 us: 1.04x faster                                                 |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.51 ms: 1.03x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250225-3.14.0a5+-91d0090-JIT/bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.432x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x