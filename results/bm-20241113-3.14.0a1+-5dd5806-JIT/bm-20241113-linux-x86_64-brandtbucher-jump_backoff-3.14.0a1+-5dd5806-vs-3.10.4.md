# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-x86_64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.396x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                 |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                               |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                |
| Geometric mean | (ref)                                                  | 1.26x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 332 ms: 2.19x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 420 ms: 2.07x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 863 ms: 2.05x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.8 ms: 1.83x faster                                                |
| float          | 117 ms                                                 | 76.2 ms: 1.54x faster                                                |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.42x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.83 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 195 us: 1.70x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                               |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 55.9 ms: 1.42x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 82.8 ms: 1.20x faster                                                |
| json_loads           | 31.2 us                                                | 26.3 us: 1.18x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                |
| genshi_text     | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                |
| genshi_xml      | 66.0 ms                                                | 59.5 ms: 1.11x faster                                                |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.19x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                |
| richards_super           | 94.7 ms                                                | 41.9 ms: 2.26x faster                                                |
| generators               | 80.1 ms                                                | 35.6 ms: 2.25x faster                                                |
| async_tree_none          | 728 ms                                                 | 332 ms: 2.19x faster                                                 |
| richards                 | 79.3 ms                                                | 37.5 ms: 2.12x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 420 ms: 2.07x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 863 ms: 2.05x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                |
| logging_silent           | 190 ns                                                 | 95.5 ns: 1.99x faster                                                |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 69.2 ms: 1.85x faster                                                |
| nbody                    | 154 ms                                                 | 83.8 ms: 1.83x faster                                                |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 65.3 ms: 1.81x faster                                                |
| go                       | 240 ms                                                 | 134 ms: 1.80x faster                                                 |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                 |
| raytrace                 | 507 ms                                                 | 285 ms: 1.78x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 195 us: 1.70x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.64x faster                                                |
| comprehensions           | 28.8 us                                                | 17.7 us: 1.63x faster                                                |
| pylint                   | 551 ms                                                 | 342 ms: 1.61x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                               |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                |
| pyflate                  | 716 ms                                                 | 453 ms: 1.58x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                |
| float                    | 117 ms                                                 | 76.2 ms: 1.54x faster                                                |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                 |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.48x faster                                                |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                |
| hexiom                   | 10.4 ms                                                | 7.15 ms: 1.45x faster                                                |
| scimark_fft              | 466 ms                                                 | 322 ms: 1.45x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 55.9 ms: 1.42x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 719 ms: 1.42x faster                                                 |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                 |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                               |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.80 ms: 1.35x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.33x faster                                                |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                 |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                |
| dulwich_log              | 84.3 ms                                                | 67.2 ms: 1.26x faster                                                |
| genshi_text              | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 55.7 ms: 1.24x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 21.0 ms: 1.23x faster                                                |
| sympy_sum                | 196 ms                                                 | 161 ms: 1.22x faster                                                 |
| nqueens                  | 106 ms                                                 | 87.7 ms: 1.21x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 82.8 ms: 1.20x faster                                                |
| json_loads               | 31.2 us                                                | 26.3 us: 1.18x faster                                                |
| json                     | 5.69 ms                                                | 4.83 ms: 1.18x faster                                                |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 877 us: 1.12x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                |
| sympy_expand             | 566 ms                                                 | 506 ms: 1.12x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 59.5 ms: 1.11x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.79 sec: 1.02x faster                                               |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                 |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                                 |
| telco                    | 7.27 ms                                                | 7.48 ms: 1.03x slower                                                |
| regex_effbot             | 3.63 ms                                                | 3.83 ms: 1.06x slower                                                |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.34 ms: 1.20x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                         |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.396x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.28x