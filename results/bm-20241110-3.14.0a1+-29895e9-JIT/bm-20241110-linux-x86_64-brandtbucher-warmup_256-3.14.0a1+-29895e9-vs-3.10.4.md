# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_256
- machine: linux-x86_64
- commit hash: 29895e9
- commit date: 2024-11-10
- overall geometric mean: 1.393x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.26x faster                                               |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.14x faster                                             |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                              |
| Geometric mean | (ref)                                                  | 1.25x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 417 ms: 2.09x faster                                               |
| async_tree_io           | 1.77 sec                                               | 861 ms: 2.05x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 584 ms: 1.74x faster                                               |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.9 ms: 1.90x faster                                              |
| float          | 117 ms                                                 | 76.5 ms: 1.53x faster                                              |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.44x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.37x faster                                               |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                              |
| regex_dna      | 227 ms                                                 | 215 ms: 1.06x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 196 us: 1.69x faster                                               |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                             |
| pickle_pure_python   | 484 us                                                 | 328 us: 1.48x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.43x faster                                              |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.29x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 78.2 ms: 1.27x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                               |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                               |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                              |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                              |
| genshi_text     | 31.8 ms                                                | 25.3 ms: 1.26x faster                                              |
| genshi_xml      | 66.0 ms                                                | 57.1 ms: 1.16x faster                                              |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.25x faster                                               |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                              |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                               |
| generators               | 80.1 ms                                                | 36.7 ms: 2.18x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 417 ms: 2.09x faster                                               |
| richards_super           | 94.7 ms                                                | 46.1 ms: 2.06x faster                                              |
| async_tree_io            | 1.77 sec                                               | 861 ms: 2.05x faster                                               |
| richards                 | 79.3 ms                                                | 39.7 ms: 2.00x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                              |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                              |
| logging_silent           | 190 ns                                                 | 99.5 ns: 1.91x faster                                              |
| nbody                    | 154 ms                                                 | 80.9 ms: 1.90x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 68.1 ms: 1.88x faster                                              |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                               |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 64.6 ms: 1.83x faster                                              |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                               |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 584 ms: 1.74x faster                                               |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 196 us: 1.69x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                             |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                              |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                               |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                               |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                              |
| float                    | 117 ms                                                 | 76.5 ms: 1.53x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                              |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                               |
| pylint                   | 551 ms                                                 | 370 ms: 1.49x faster                                               |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                              |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                              |
| pickle_pure_python       | 484 us                                                 | 328 us: 1.48x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.07 ms: 1.47x faster                                              |
| scimark_fft              | 466 ms                                                 | 322 ms: 1.45x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.43x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                              |
| fannkuch                 | 532 ms                                                 | 383 ms: 1.39x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 739 ms: 1.38x faster                                               |
| regex_compile            | 188 ms                                                 | 137 ms: 1.37x faster                                               |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                             |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                             |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                              |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.33x faster                                              |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.29x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 78.2 ms: 1.27x faster                                              |
| genshi_text              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                              |
| 2to3                     | 348 ms                                                 | 278 ms: 1.26x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                               |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                              |
| nqueens                  | 106 ms                                                 | 87.6 ms: 1.21x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 58.1 ms: 1.19x faster                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 145 ms: 1.19x faster                                               |
| genshi_xml               | 66.0 ms                                                | 57.1 ms: 1.16x faster                                              |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.15x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                               |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                               |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                              |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                              |
| json                     | 5.69 ms                                                | 4.99 ms: 1.14x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                               |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.14x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                              |
| sympy_expand             | 566 ms                                                 | 500 ms: 1.13x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                              |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                             |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                               |
| bench_thread_pool        | 986 us                                                 | 886 us: 1.11x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                              |
| regex_dna                | 227 ms                                                 | 215 ms: 1.06x faster                                               |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                               |
| async_generators         | 444 ms                                                 | 449 ms: 1.01x slower                                               |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                              |
| coverage                 | 79.4 ms                                                | 84.0 ms: 1.06x slower                                              |
| telco                    | 7.27 ms                                                | 7.72 ms: 1.06x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.38 ms: 1.21x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                              |
| bench_mp_pool            | 24.0 ms                                                | 80.3 ms: 3.35x slower                                              |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                       |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241110-3.14.0a1+-29895e9-JIT/bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.393x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.29x