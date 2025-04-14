# Results vs. 3.10.4

- fork: brandtbucher
- ref: yes_underflow
- machine: linux-x86_64
- commit hash: 4112331
- commit date: 2025-02-14
- overall geometric mean: 1.395x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                |
| html5lib       | 88.9 ms                                                | 69.0 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 633 ms: 2.79x faster                                                  |
| async_tree_none         | 728 ms                                                 | 271 ms: 2.68x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 329 ms: 2.64x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.53x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.0 ms: 1.77x faster                                                 |
| nbody          | 154 ms                                                 | 89.3 ms: 1.72x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.46x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.05 ms: 1.19x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                 |
| regex_dna      | 227 ms                                                 | 202 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 202 us: 1.64x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 96.1 ms: 1.20x faster                                                 |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.95 ms: 1.64x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                 |
| django_template | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 66.7 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 633 ms: 2.79x faster                                                  |
| async_tree_none          | 728 ms                                                 | 271 ms: 2.68x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 329 ms: 2.64x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                 |
| pylint                   | 551 ms                                                 | 286 ms: 1.93x faster                                                  |
| deltablue                | 7.91 ms                                                | 4.22 ms: 1.88x faster                                                 |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 63.4 ms: 1.86x faster                                                 |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                  |
| spectral_norm            | 170 ms                                                 | 93.0 ms: 1.83x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 70.8 ms: 1.80x faster                                                 |
| float                    | 117 ms                                                 | 66.0 ms: 1.77x faster                                                 |
| raytrace                 | 507 ms                                                 | 289 ms: 1.75x faster                                                  |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                                  |
| nbody                    | 154 ms                                                 | 89.3 ms: 1.72x faster                                                 |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.66x faster                                                 |
| mako                     | 16.3 ms                                                | 9.95 ms: 1.64x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.64x faster                                                  |
| generators               | 80.1 ms                                                | 49.5 ms: 1.62x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                  |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.50x faster                                                 |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                 |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.45 ms: 1.45x faster                                                 |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                 |
| logging_silent           | 190 ns                                                 | 134 ns: 1.42x faster                                                  |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                 |
| hexiom                   | 10.4 ms                                                | 7.68 ms: 1.35x faster                                                 |
| django_template          | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                 |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                  |
| logging_format           | 9.09 us                                                | 6.83 us: 1.33x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.59 sec: 1.32x faster                                                |
| logging_simple           | 8.30 us                                                | 6.27 us: 1.32x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 770 ms: 1.32x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                 |
| html5lib                 | 88.9 ms                                                | 69.0 ms: 1.29x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.23 sec: 1.28x faster                                                |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 54.7 ms: 1.26x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                 |
| richards_super           | 94.7 ms                                                | 75.9 ms: 1.25x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                |
| richards                 | 79.3 ms                                                | 64.2 ms: 1.23x faster                                                 |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                  |
| nqueens                  | 106 ms                                                 | 87.9 ms: 1.20x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 96.1 ms: 1.20x faster                                                 |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 70.5 ms: 1.20x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.05 ms: 1.19x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| regex_dna                | 227 ms                                                 | 202 ms: 1.12x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                |
| bench_thread_pool        | 986 us                                                 | 890 us: 1.11x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                  |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                                 |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| async_generators         | 444 ms                                                 | 412 ms: 1.08x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 66.7 ms: 1.01x slower                                                 |
| telco                    | 7.27 ms                                                | 7.67 ms: 1.06x slower                                                 |
| coverage                 | 79.4 ms                                                | 90.3 ms: 1.14x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.65 ms: 1.28x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 81.0 ms: 3.37x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250214-3.14.0a4+-4112331-JIT/bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.395x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.29x