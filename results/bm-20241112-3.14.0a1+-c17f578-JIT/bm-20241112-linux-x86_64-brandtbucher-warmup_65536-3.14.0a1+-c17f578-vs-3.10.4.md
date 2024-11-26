# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_65536
- machine: linux-x86_64
- commit hash: c17f578
- commit date: 2024-11-12
- overall geometric mean: 1.398x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                 |
| docutils       | 3.30 sec                                               | 2.81 sec: 1.17x faster                                               |
| html5lib       | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                |
| Geometric mean | (ref)                                                  | 1.28x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 332 ms: 2.19x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 417 ms: 2.08x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 868 ms: 2.04x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 580 ms: 1.75x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.5 ms: 1.86x faster                                                |
| float          | 117 ms                                                 | 77.1 ms: 1.52x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.42x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.13x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 200 us: 1.65x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                               |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                |
| django_template | 48.2 ms                                                | 36.1 ms: 1.34x faster                                                |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                |
| genshi_xml      | 66.0 ms                                                | 57.2 ms: 1.15x faster                                                |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.25x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                |
| generators               | 80.1 ms                                                | 36.4 ms: 2.20x faster                                                |
| async_tree_none          | 728 ms                                                 | 332 ms: 2.19x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 417 ms: 2.08x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 868 ms: 2.04x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                |
| logging_silent           | 190 ns                                                 | 98.7 ns: 1.92x faster                                                |
| go                       | 240 ms                                                 | 127 ms: 1.88x faster                                                 |
| nbody                    | 154 ms                                                 | 82.5 ms: 1.86x faster                                                |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 69.0 ms: 1.85x faster                                                |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 65.2 ms: 1.81x faster                                                |
| richards_super           | 94.7 ms                                                | 52.4 ms: 1.81x faster                                                |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                 |
| richards                 | 79.3 ms                                                | 45.2 ms: 1.75x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 580 ms: 1.75x faster                                                 |
| pylint                   | 551 ms                                                 | 327 ms: 1.69x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.66x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 200 us: 1.65x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                               |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.71 ms: 1.55x faster                                                |
| pyflate                  | 716 ms                                                 | 464 ms: 1.54x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                 |
| float                    | 117 ms                                                 | 77.1 ms: 1.52x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                                |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                |
| scimark_fft              | 466 ms                                                 | 326 ms: 1.43x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                                 |
| spectral_norm            | 170 ms                                                 | 120 ms: 1.42x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                                |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                 |
| thrift                   | 1.07 ms                                                | 788 us: 1.36x faster                                                 |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                 |
| html5lib                 | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.34x faster                                                 |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.34x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.33x faster                                                |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                               |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 65.7 ms: 1.28x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 54.2 ms: 1.28x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                 |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.81 sec: 1.17x faster                                               |
| nqueens                  | 106 ms                                                 | 90.5 ms: 1.17x faster                                                |
| genshi_xml               | 66.0 ms                                                | 57.2 ms: 1.15x faster                                                |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                                |
| json                     | 5.69 ms                                                | 4.97 ms: 1.15x faster                                                |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| bench_thread_pool        | 986 us                                                 | 869 us: 1.14x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                 |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                 |
| coverage                 | 79.4 ms                                                | 84.1 ms: 1.06x slower                                                |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.33x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.67x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 79.2 ms: 3.30x slower                                                |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                         |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241112-3.14.0a1+-c17f578-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.398x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.27x