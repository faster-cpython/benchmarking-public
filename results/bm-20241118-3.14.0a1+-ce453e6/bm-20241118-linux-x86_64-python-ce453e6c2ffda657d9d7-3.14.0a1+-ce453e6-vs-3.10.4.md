# Results vs. 3.10.4

- fork: python
- ref: ce453e6c2ffda657d9d7
- machine: linux-x86_64
- commit hash: ce453e6
- commit date: 2024-11-18
- overall geometric mean: 1.384x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                   |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 859 ms: 2.06x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 96.0 ms: 1.60x faster                                                  |
| float          | 117 ms                                                 | 79.8 ms: 1.47x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                  |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 26.8 us: 1.17x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                  |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                  |
| genshi_text     | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                   |
| generators               | 80.1 ms                                                | 27.4 ms: 2.93x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.33 ms: 2.37x faster                                                  |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 859 ms: 2.06x faster                                                   |
| go                       | 240 ms                                                 | 121 ms: 1.98x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 31.0 us: 1.89x faster                                                  |
| chaos                    | 115 ms                                                 | 61.3 ms: 1.88x faster                                                  |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                   |
| richards_super           | 94.7 ms                                                | 52.2 ms: 1.81x faster                                                  |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 72.2 ms: 1.77x faster                                                  |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                   |
| djangocms                | 38.4 us                                                | 22.0 us: 1.75x faster                                                  |
| richards                 | 79.3 ms                                                | 45.7 ms: 1.73x faster                                                  |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                   |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 69.8 ms: 1.69x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                  |
| nbody                    | 154 ms                                                 | 96.0 ms: 1.60x faster                                                  |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                   |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                   |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.48x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.48x faster                                                  |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                  |
| float                    | 117 ms                                                 | 79.8 ms: 1.47x faster                                                  |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                 |
| spectral_norm            | 170 ms                                                 | 119 ms: 1.43x faster                                                   |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                  |
| genshi_text              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| thrift                   | 1.07 ms                                                | 775 us: 1.38x faster                                                   |
| html5lib                 | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                 |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.8 ms: 1.31x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.31x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                  |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.05 ms: 1.28x faster                                                  |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                  |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                   |
| scimark_fft              | 466 ms                                                 | 379 ms: 1.23x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                  |
| json_loads               | 31.2 us                                                | 26.8 us: 1.17x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 851 us: 1.16x faster                                                   |
| json                     | 5.69 ms                                                | 4.91 ms: 1.16x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                  |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                   |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                                   |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                  |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.08x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.84 ms: 1.34x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.75 ms: 1.70x slower                                                  |
| dask                     | 441 ms                                                 | 786 ms: 1.78x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 79.9 ms: 3.33x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20241118-3.14.0a1+-ce453e6/bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.384x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.26x