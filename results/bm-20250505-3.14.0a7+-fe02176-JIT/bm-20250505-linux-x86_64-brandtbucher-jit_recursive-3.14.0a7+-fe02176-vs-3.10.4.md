# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_recursive
- machine: linux-x86_64
- commit hash: fe02176
- commit date: 2025-05-05
- overall geometric mean: 1.459x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                  |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                |
| html5lib       | 88.9 ms                                                | 61.1 ms: 1.46x faster                                                 |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                                  |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.81x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 501 ms: 2.03x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.8 ms: 1.81x faster                                                 |
| nbody          | 154 ms                                                 | 95.6 ms: 1.61x faster                                                 |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.43x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 2.95 ms: 1.23x faster                                                 |
| regex_dna      | 227 ms                                                 | 196 ms: 1.16x faster                                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                |
| unpickle_pure_python | 331 us                                                 | 208 us: 1.59x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 81.2 ms: 1.22x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.20x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                                  |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.81x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.59x faster                                                 |
| generators               | 80.1 ms                                                | 31.3 ms: 2.56x faster                                                 |
| richards_super           | 94.7 ms                                                | 40.5 ms: 2.34x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                |
| richards                 | 79.3 ms                                                | 35.4 ms: 2.24x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 501 ms: 2.03x faster                                                  |
| go                       | 240 ms                                                 | 121 ms: 1.99x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                 |
| pylint                   | 551 ms                                                 | 285 ms: 1.93x faster                                                  |
| chaos                    | 115 ms                                                 | 61.9 ms: 1.86x faster                                                 |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                  |
| float                    | 117 ms                                                 | 64.8 ms: 1.81x faster                                                 |
| raytrace                 | 507 ms                                                 | 281 ms: 1.80x faster                                                  |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 76.2 ms: 1.68x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                  |
| pyflate                  | 716 ms                                                 | 440 ms: 1.63x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.8 us: 1.62x faster                                                 |
| nbody                    | 154 ms                                                 | 95.6 ms: 1.61x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 208 us: 1.59x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 75.5 ms: 1.57x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.65 ms: 1.56x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                  |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                 |
| html5lib                 | 88.9 ms                                                | 61.1 ms: 1.46x faster                                                 |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                 |
| scimark_lu               | 176 ms                                                 | 122 ms: 1.45x faster                                                  |
| logging_format           | 9.09 us                                                | 6.36 us: 1.43x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.6 ms: 1.43x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 60.8 ms: 1.39x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                 |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                 |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                                  |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                  |
| nqueens                  | 106 ms                                                 | 83.6 ms: 1.27x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                |
| regex_effbot             | 3.63 ms                                                | 2.95 ms: 1.23x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 81.2 ms: 1.22x faster                                                 |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                 |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.20x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                 |
| regex_dna                | 227 ms                                                 | 196 ms: 1.16x faster                                                  |
| scimark_fft              | 466 ms                                                 | 409 ms: 1.14x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 903 us: 1.09x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                 |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.06 ms: 1.07x faster                                                 |
| async_generators         | 444 ms                                                 | 423 ms: 1.05x faster                                                  |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x slower                                                  |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.08x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.08 ms: 1.40x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 92.3 ms: 3.84x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, coverage, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20250505-3.14.0a7+-fe02176-JIT/bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.459x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.33x