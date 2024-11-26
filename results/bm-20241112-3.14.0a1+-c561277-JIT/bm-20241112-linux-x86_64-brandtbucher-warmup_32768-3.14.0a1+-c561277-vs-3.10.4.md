# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_32768
- machine: linux-x86_64
- commit hash: c561277
- commit date: 2024-11-12
- overall geometric mean: 1.399x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                 |
| docutils       | 3.30 sec                                               | 2.83 sec: 1.16x faster                                               |
| html5lib       | 88.9 ms                                                | 66.5 ms: 1.34x faster                                                |
| Geometric mean | (ref)                                                  | 1.28x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 335 ms: 2.17x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 419 ms: 2.08x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 866 ms: 2.04x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 581 ms: 1.75x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.5 ms: 1.82x faster                                                |
| float          | 117 ms                                                 | 76.5 ms: 1.53x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.42x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 199 us: 1.66x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                               |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.28x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.09x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                |
| genshi_text     | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                |
| genshi_xml      | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                                |
| generators               | 80.1 ms                                                | 36.0 ms: 2.22x faster                                                |
| async_tree_none          | 728 ms                                                 | 335 ms: 2.17x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 419 ms: 2.08x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 866 ms: 2.04x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.96x faster                                                |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 68.0 ms: 1.88x faster                                                |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                 |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                 |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                 |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                                 |
| nbody                    | 154 ms                                                 | 84.5 ms: 1.82x faster                                                |
| richards_super           | 94.7 ms                                                | 52.2 ms: 1.82x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 65.4 ms: 1.81x faster                                                |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 581 ms: 1.75x faster                                                 |
| richards                 | 79.3 ms                                                | 45.5 ms: 1.74x faster                                                |
| pylint                   | 551 ms                                                 | 329 ms: 1.68x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 199 us: 1.66x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.61x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                               |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.68 ms: 1.56x faster                                                |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                 |
| float                    | 117 ms                                                 | 76.5 ms: 1.53x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                                 |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.70 us: 1.46x faster                                                |
| logging_format           | 9.09 us                                                | 6.25 us: 1.46x faster                                                |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                 |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.54 ms: 1.43x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                               |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 749 ms: 1.36x faster                                                 |
| fannkuch                 | 532 ms                                                 | 394 ms: 1.35x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                |
| html5lib                 | 88.9 ms                                                | 66.5 ms: 1.34x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                               |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.28x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 54.3 ms: 1.27x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                |
| sympy_str                | 346 ms                                                 | 278 ms: 1.25x faster                                                 |
| sympy_expand             | 566 ms                                                 | 483 ms: 1.17x faster                                                 |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                |
| nqueens                  | 106 ms                                                 | 90.6 ms: 1.17x faster                                                |
| json                     | 5.69 ms                                                | 4.88 ms: 1.17x faster                                                |
| docutils                 | 3.30 sec                                               | 2.83 sec: 1.16x faster                                               |
| genshi_xml               | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                |
| bench_thread_pool        | 986 us                                                 | 873 us: 1.13x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.09x faster                                                 |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                 |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                 |
| telco                    | 7.27 ms                                                | 7.69 ms: 1.06x slower                                                |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.52 ms: 1.25x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 78.4 ms: 3.27x slower                                                |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241112-3.14.0a1+-c561277-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.399x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.28x