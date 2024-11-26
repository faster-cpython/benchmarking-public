# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_2048
- machine: linux-x86_64
- commit hash: f863657
- commit date: 2024-11-12
- overall geometric mean: 1.390x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.31x faster                                                |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                              |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 333 ms: 2.19x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 415 ms: 2.10x faster                                                |
| async_tree_io           | 1.77 sec                                               | 862 ms: 2.05x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 576 ms: 1.77x faster                                                |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.9 ms: 1.87x faster                                               |
| float          | 117 ms                                                 | 76.0 ms: 1.54x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.43x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.39x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                               |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                               |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.29x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 79.3 ms: 1.25x faster                                               |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                               |
| django_template | 48.2 ms                                                | 36.4 ms: 1.32x faster                                               |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                               |
| genshi_xml      | 66.0 ms                                                | 58.4 ms: 1.13x faster                                               |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                                |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                               |
| generators               | 80.1 ms                                                | 35.8 ms: 2.24x faster                                               |
| async_tree_none          | 728 ms                                                 | 333 ms: 2.19x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 415 ms: 2.10x faster                                                |
| richards_super           | 94.7 ms                                                | 45.7 ms: 2.07x faster                                               |
| async_tree_io            | 1.77 sec                                               | 862 ms: 2.05x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                               |
| richards                 | 79.3 ms                                                | 39.9 ms: 1.99x faster                                               |
| logging_silent           | 190 ns                                                 | 97.9 ns: 1.94x faster                                               |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                               |
| nbody                    | 154 ms                                                 | 81.9 ms: 1.87x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 68.3 ms: 1.87x faster                                               |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 65.1 ms: 1.82x faster                                               |
| go                       | 240 ms                                                 | 134 ms: 1.79x faster                                                |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 576 ms: 1.77x faster                                                |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                               |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| pylint                   | 551 ms                                                 | 349 ms: 1.58x faster                                                |
| pyflate                  | 716 ms                                                 | 459 ms: 1.56x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                               |
| float                    | 117 ms                                                 | 76.0 ms: 1.54x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                               |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.48x faster                                                |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                               |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.13 ms: 1.46x faster                                               |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.62 ms: 1.40x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                              |
| regex_compile            | 188 ms                                                 | 135 ms: 1.39x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 733 ms: 1.39x faster                                                |
| fannkuch                 | 532 ms                                                 | 387 ms: 1.37x faster                                                |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                              |
| thrift                   | 1.07 ms                                                | 790 us: 1.36x faster                                                |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.36x faster                                               |
| django_template          | 48.2 ms                                                | 36.4 ms: 1.32x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.7 ms: 1.32x faster                                               |
| 2to3                     | 348 ms                                                 | 267 ms: 1.31x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.29x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 136 ms: 1.27x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 79.3 ms: 1.25x faster                                               |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                               |
| sqlglot_optimize         | 69.2 ms                                                | 56.4 ms: 1.23x faster                                               |
| nqueens                  | 106 ms                                                 | 87.7 ms: 1.21x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 21.9 ms: 1.18x faster                                               |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                |
| json                     | 5.69 ms                                                | 4.91 ms: 1.16x faster                                               |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                               |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                               |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                              |
| genshi_xml               | 66.0 ms                                                | 58.4 ms: 1.13x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                               |
| bench_thread_pool        | 986 us                                                 | 877 us: 1.12x faster                                                |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                |
| sympy_expand             | 566 ms                                                 | 504 ms: 1.12x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                               |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                              |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.03x slower                                               |
| telco                    | 7.27 ms                                                | 7.63 ms: 1.05x slower                                               |
| coverage                 | 79.4 ms                                                | 85.1 ms: 1.07x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.52 ms: 1.25x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 78.8 ms: 3.28x slower                                               |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                        |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241112-3.14.0a1+-f863657-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.390x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.28x