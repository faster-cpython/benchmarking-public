# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_8192
- machine: linux-x86_64
- commit hash: 1236a9d
- commit date: 2024-11-12
- overall geometric mean: 1.405x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                              |
| html5lib       | 88.9 ms                                                | 66.6 ms: 1.33x faster                                               |
| Geometric mean | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 332 ms: 2.19x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 418 ms: 2.08x faster                                                |
| async_tree_io           | 1.77 sec                                               | 860 ms: 2.06x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 581 ms: 1.75x faster                                                |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.9 ms: 1.85x faster                                               |
| float          | 117 ms                                                 | 76.6 ms: 1.53x faster                                               |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.43x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                               |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.15x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 195 us: 1.69x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.61x faster                                              |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.43x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.28x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 78.9 ms: 1.26x faster                                               |
| json_loads           | 31.2 us                                                | 27.0 us: 1.15x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.07x faster                                                |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                               |
| django_template | 48.2 ms                                                | 35.6 ms: 1.35x faster                                               |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.30x faster                                               |
| genshi_xml      | 66.0 ms                                                | 56.0 ms: 1.18x faster                                               |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.48x faster                                               |
| richards_super           | 94.7 ms                                                | 41.8 ms: 2.26x faster                                               |
| generators               | 80.1 ms                                                | 36.3 ms: 2.21x faster                                               |
| async_tree_none          | 728 ms                                                 | 332 ms: 2.19x faster                                                |
| richards                 | 79.3 ms                                                | 36.7 ms: 2.16x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 418 ms: 2.08x faster                                                |
| async_tree_io            | 1.77 sec                                               | 860 ms: 2.06x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.0 us: 1.95x faster                                               |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                               |
| logging_silent           | 190 ns                                                 | 100.0 ns: 1.90x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 68.0 ms: 1.88x faster                                               |
| nbody                    | 154 ms                                                 | 82.9 ms: 1.85x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 64.0 ms: 1.85x faster                                               |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                                |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                |
| deepcopy                 | 479 us                                                 | 270 us: 1.78x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 581 ms: 1.75x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 195 us: 1.69x faster                                                |
| comprehensions           | 28.8 us                                                | 17.5 us: 1.64x faster                                               |
| pylint                   | 551 ms                                                 | 336 ms: 1.64x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                               |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.61x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                               |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                               |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                |
| float                    | 117 ms                                                 | 76.6 ms: 1.53x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                               |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                |
| logging_format           | 9.09 us                                                | 6.05 us: 1.50x faster                                               |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.02 ms: 1.48x faster                                               |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                |
| scimark_fft              | 466 ms                                                 | 320 ms: 1.46x faster                                                |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.43x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                              |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                |
| fannkuch                 | 532 ms                                                 | 392 ms: 1.35x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.35x faster                                               |
| django_template          | 48.2 ms                                                | 35.6 ms: 1.35x faster                                               |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.80 ms: 1.35x faster                                               |
| html5lib                 | 88.9 ms                                                | 66.6 ms: 1.33x faster                                               |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.32x faster                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.30x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.28x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.27x faster                                               |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 78.9 ms: 1.26x faster                                               |
| dulwich_log              | 84.3 ms                                                | 67.0 ms: 1.26x faster                                               |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                               |
| sympy_str                | 346 ms                                                 | 289 ms: 1.20x faster                                                |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.18x faster                                               |
| genshi_xml               | 66.0 ms                                                | 56.0 ms: 1.18x faster                                               |
| json_loads               | 31.2 us                                                | 27.0 us: 1.15x faster                                               |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                               |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                              |
| json                     | 5.69 ms                                                | 4.97 ms: 1.15x faster                                               |
| bench_thread_pool        | 986 us                                                 | 867 us: 1.14x faster                                                |
| sympy_expand             | 566 ms                                                 | 500 ms: 1.13x faster                                                |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                              |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.07x faster                                                |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                |
| telco                    | 7.27 ms                                                | 7.57 ms: 1.04x slower                                               |
| coverage                 | 79.4 ms                                                | 84.9 ms: 1.07x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.32x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.69 ms: 1.66x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 78.2 ms: 3.26x slower                                               |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241112-3.14.0a1+-1236a9d-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.405x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x