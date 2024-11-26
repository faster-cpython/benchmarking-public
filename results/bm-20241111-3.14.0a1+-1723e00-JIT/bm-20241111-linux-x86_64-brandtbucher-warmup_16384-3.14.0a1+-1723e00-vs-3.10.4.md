# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_16384
- machine: linux-x86_64
- commit hash: 1723e00
- commit date: 2024-11-11
- overall geometric mean: 1.400x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                 |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                               |
| html5lib       | 88.9 ms                                                | 66.5 ms: 1.34x faster                                                |
| Geometric mean | (ref)                                                  | 1.28x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 334 ms: 2.18x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 420 ms: 2.07x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 866 ms: 2.04x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 586 ms: 1.73x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.6 ms: 1.86x faster                                                |
| float          | 117 ms                                                 | 77.1 ms: 1.52x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.42x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 194 us: 1.71x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                               |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.50x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                |
| django_template | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                |
| genshi_xml      | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                |
| generators               | 80.1 ms                                                | 35.8 ms: 2.24x faster                                                |
| async_tree_none          | 728 ms                                                 | 334 ms: 2.18x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 420 ms: 2.07x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 866 ms: 2.04x faster                                                 |
| richards_super           | 94.7 ms                                                | 48.4 ms: 1.96x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                |
| richards                 | 79.3 ms                                                | 41.2 ms: 1.92x faster                                                |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                                |
| logging_silent           | 190 ns                                                 | 99.5 ns: 1.91x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 67.8 ms: 1.88x faster                                                |
| go                       | 240 ms                                                 | 128 ms: 1.87x faster                                                 |
| nbody                    | 154 ms                                                 | 82.6 ms: 1.86x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 64.5 ms: 1.83x faster                                                |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                 |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                                 |
| deepcopy                 | 479 us                                                 | 273 us: 1.76x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 586 ms: 1.73x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.71x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                |
| pylint                   | 551 ms                                                 | 333 ms: 1.66x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                |
| float                    | 117 ms                                                 | 77.1 ms: 1.52x faster                                                |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.50x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.98 ms: 1.49x faster                                                |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.83 us: 1.47x faster                                                |
| scimark_fft              | 466 ms                                                 | 323 ms: 1.44x faster                                                 |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                               |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.70 ms: 1.38x faster                                                |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.36x faster                                                |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 749 ms: 1.36x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                               |
| html5lib                 | 88.9 ms                                                | 66.5 ms: 1.34x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                 |
| django_template          | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 65.6 ms: 1.28x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 55.5 ms: 1.25x faster                                                |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                 |
| nqueens                  | 106 ms                                                 | 89.2 ms: 1.19x faster                                                |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                |
| json                     | 5.69 ms                                                | 4.90 ms: 1.16x faster                                                |
| genshi_xml               | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                               |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.14x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 876 us: 1.13x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                 |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                 |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                 |
| telco                    | 7.27 ms                                                | 7.72 ms: 1.06x slower                                                |
| coverage                 | 79.4 ms                                                | 86.2 ms: 1.09x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.52 ms: 1.25x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 78.3 ms: 3.26x slower                                                |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241111-3.14.0a1+-1723e00-JIT/bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.400x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x